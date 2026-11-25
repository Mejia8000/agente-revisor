#!/usr/bin/env python3
"""Agente revisor: vigila organizaciones, repositorios y webs; Gemini lee el código
y escribe un informe en español. Corre gratis en GitHub Actions (sin tokens de Claude)."""
import datetime as dt, hashlib, html, json, os, re, subprocess, sys, tempfile, time
import urllib.error, urllib.request

RAIZ = os.path.dirname(os.path.abspath(__file__))
CFG = json.load(open(os.path.join(RAIZ, "fuentes.json"), encoding="utf-8"))
LIM = CFG["limites"]
RUTA_ESTADO = os.path.join(RAIZ, "estado.json")
HOY = dt.date.today().isoformat()
INICIO = time.time()
TIEMPO_MAX = 100 * 60  # segundos; el trabajo de Actions se corta a los 120 min
GH_TOKEN = os.environ.get("GITHUB_TOKEN", "")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY", "")
OR_KEY = os.environ.get("OPENROUTER_API_KEY", "")
SOLO = os.environ.get("REVISAR_AHORA", "").strip()  # dueño/repo o URL para revisar ya

EXT = {".py", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".go", ".rs", ".java", ".kt", ".c", ".cc",
       ".cpp", ".h", ".hpp", ".cu", ".cuh", ".swift", ".dart", ".rb", ".php", ".cs", ".scala",
       ".sh", ".toml", ".yaml", ".yml", ".proto", ".sql", ".html", ".css", ".vue", ".svelte"}
SALTAR = {".git", "node_modules", "vendor", "third_party", "third-party", "dist", "build", "out",
          "__pycache__", ".venv", "venv", "site-packages", "external", "deps", "testdata"}


# ---------- utilidades ----------
def log(*a):
    print(*a, flush=True)


def http(url, datos=None, cab=None, intentos=3):
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    for i in range(intentos):
        req = urllib.request.Request(url, data=cuerpo, headers=dict(cab or {}))
        if cuerpo:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and i < intentos - 1:
                espera = 60 * (i + 1)
                log(f"  {e.code}: espero {espera}s y reintento")
                time.sleep(espera)
                continue
            raise


def gh(ruta):
    cab = {"Accept": "application/vnd.github+json", "User-Agent": "agente-revisor"}
    if GH_TOKEN:
        cab["Authorization"] = "Bearer " + GH_TOKEN
    return json.loads(http("https://api.github.com" + ruta, cab=cab))


def cargar_estado():
    if os.path.exists(RUTA_ESTADO):
        return json.load(open(RUTA_ESTADO, encoding="utf-8"))
    return {"ultima": None, "repos": {}, "cola": [], "webs": {}}


def guardar_estado(est):
    json.dump(est, open(RUTA_ESTADO, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def numeros(nombre):
    return tuple(int(n) for n in re.findall(r"\d+", nombre))


# ---------- modelos ----------
_modelo = {"gemini": CFG["modelos"]["gemini"], "or": None}


def elegir_gemini():
    """Si el nombre configurado ya no existe, toma el Flash más nuevo disponible."""
    datos = json.loads(http("https://generativelanguage.googleapis.com/v1beta/models?pageSize=200",
                            cab={"x-goog-api-key": GEMINI_KEY}))
    malos = ("lite", "image", "tts", "live", "audio", "embedding", "preview", "exp")
    cand = [m["name"].split("/")[-1] for m in datos.get("models", [])
            if "generateContent" in m.get("supportedGenerationMethods", [])
            and "flash" in m["name"] and not any(x in m["name"] for x in malos)]
    if not cand:
        raise RuntimeError("No encontré un modelo Flash de Gemini disponible")
    return max(cand, key=numeros)


def gemini(prompt):
    for _ in range(2):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{_modelo['gemini']}:generateContent"
        try:
            r = json.loads(http(url, {"contents": [{"parts": [{"text": prompt}]}],
                                      "generationConfig": {"temperature": 0.2}},
                                cab={"x-goog-api-key": GEMINI_KEY}))
            return "".join(p.get("text", "") for p in r["candidates"][0]["content"]["parts"])
        except urllib.error.HTTPError as e:
            if e.code == 404:
                _modelo["gemini"] = elegir_gemini()
                log("  Modelo Gemini cambiado a", _modelo["gemini"])
                continue
            raise
    raise RuntimeError("Gemini no respondió")


def openrouter(prompt):
    """Respaldo: Nemotron gratis por OpenRouter (elige el de más contexto)."""
    if not _modelo["or"]:
        pedido = CFG["modelos"]["openrouter_respaldo"]
        if pedido.startswith("auto"):
            ms = json.loads(http("https://openrouter.ai/api/v1/models"))["data"]
            ms = [m for m in ms if "nemotron" in m["id"] and m["id"].endswith(":free")]
            if not ms:
                raise RuntimeError("No hay Nemotron gratis en OpenRouter ahora")
            m = max(ms, key=lambda m: m.get("context_length") or 0)
            _modelo["or"] = (m["id"], m.get("context_length") or 100000)
        else:
            _modelo["or"] = (pedido, 100000)
    mid, ctx = _modelo["or"]
    prompt = prompt[: int(ctx * 3)]  # ~3 caracteres por token, con margen
    r = json.loads(http("https://openrouter.ai/api/v1/chat/completions",
                        {"model": mid, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2},
                        cab={"Authorization": "Bearer " + OR_KEY}))
    return r["choices"][0]["message"]["content"] + f"\n\n_(Informe hecho por {mid}, respaldo)_"


def analizar(prompt):
    try:
        return gemini(prompt)
    except Exception as e:
        log("  Gemini falló:", e)
        if not OR_KEY:
            raise
        return openrouter(prompt)


INSTRUCCIONES = """Eres un revisor técnico. Escribe en español sencillo, para alguien que no sabe inglés.
Separa hechos (lo que muestra el material) de suposiciones; marca las suposiciones como "sin confirmar". No inventes.
Usa EXACTAMENTE este formato:
EN UNA LÍNEA: (resumen de una sola frase)
## Qué es
## {nuevo}
## Cosas útiles
(modelos, APIs o herramientas gratis, ejemplos de código que se puedan reutilizar)
## Avisos
(requisitos, licencia, costos, límites, riesgos)
## ¿Sirve para sus proyectos?
(sus proyectos: un conector a la API de Gemini en Cloudflare, una IA propia llamada Musa que entrena en Kaggle,
y apps web publicadas con GitHub y Cloudflare). Di sí o no y por qué.
"""


# ---------- repositorios ----------
def descubrir(est):
    desde = est["ultima"] or (dt.datetime.utcnow() - dt.timedelta(days=LIM["dias_atras_primera_vez"])).isoformat() + "Z"
    en_cola = {c["repo"] for c in est["cola"]}

    def considerar(r):
        nombre = r["full_name"]
        if r.get("fork") or r.get("archived") or nombre in en_cola:
            return
        if r.get("stargazers_count", 0) < LIM.get("min_estrellas", 0) and nombre not in CFG["repositorios"]:
            return
        if r["pushed_at"] > est["repos"].get(nombre, {}).get("pushed", ""):
            est["cola"].append({"repo": nombre, "pushed": r["pushed_at"], "estrellas": r.get("stargazers_count", 0)})
            en_cola.add(nombre)

    for org in CFG["organizaciones"]:
        pag = 1
        while pag <= 10:
            lote = gh(f"/orgs/{org}/repos?sort=pushed&direction=desc&per_page=100&page={pag}")
            for r in lote:
                if r["pushed_at"] < desde:
                    break
                considerar(r)
            if len(lote) < 100 or lote[-1]["pushed_at"] < desde:
                break
            pag += 1
    for nombre in CFG["repositorios"]:
        considerar(gh(f"/repos/{nombre}"))
    # Lo más importante primero (más estrellas); lo que lleva más de 14 días esperando se descarta.
    limite = (dt.datetime.utcnow() - dt.timedelta(days=14)).isoformat() + "Z"
    minimo = LIM.get("min_estrellas", 0)
    est["cola"] = sorted([c for c in est["cola"] if c["repo"] in CFG["repositorios"]
                          or (c["pushed"] >= limite and c["estrellas"] >= minimo)],
                         key=lambda c: -c["estrellas"])


def leer_codigo(carpeta, maximo):
    archivos = []
    for base, dirs, nombres in os.walk(carpeta):
        dirs[:] = [d for d in dirs if d not in SALTAR and not d.startswith(".")]
        for n in nombres:
            ruta = os.path.join(base, n)
            rel = os.path.relpath(ruta, carpeta)
            es_readme = base == carpeta and n.lower().startswith("readme")
            if (es_readme or os.path.splitext(n)[1].lower() in EXT) and os.path.getsize(ruta) < 300_000:
                prueba = "test" in rel.lower()
                archivos.append((0 if es_readme else (2 if prueba else 1), rel.count(os.sep), rel, ruta))
    archivos.sort()
    total = leidas = 0
    partes = []
    for _, _, rel, ruta in archivos:
        try:
            lineas = open(ruta, encoding="utf-8", errors="ignore").read().splitlines()
        except OSError:
            continue
        total += len(lineas)
        if leidas < maximo:
            tomar = lineas[: maximo - leidas]
            leidas += len(tomar)
            partes.append(f"\n===== {rel} =====\n" + "\n".join(tomar))
    return "".join(partes), leidas, total


def revisar_repo(nombre, est):
    info = gh(f"/repos/{nombre}")
    rama = info["default_branch"]
    sha = gh(f"/repos/{nombre}/commits/{rama}")["sha"]
    previo = est["repos"].get(nombre, {}).get("sha")
    maximo = LIM["lineas_max_por_repo"]
    cab = f"Repositorio: {nombre}\nDescripción: {info.get('description') or '-'}\nEstrellas: {info.get('stargazers_count')}\n"
    material, nota = None, ""
    if previo == sha:  # el cambio fue en otra rama: nada nuevo en la principal
        est["repos"][nombre]["pushed"] = info["pushed_at"]
        return None, None

    if previo:
        try:
            comp = gh(f"/repos/{nombre}/compare/{previo}...{sha}")
            msgs = "\n".join("- " + c["commit"]["message"].splitlines()[0] for c in comp["commits"][-50:])
            parches, n = [], 0
            for f in comp.get("files", []):
                p = f.get("patch", "")
                if n + p.count("\n") > maximo:
                    break
                n += p.count("\n")
                parches.append(f"\n===== {f['filename']} ({f['status']}) =====\n{p}")
            material = cab + f"Cambios desde la última revisión ({len(comp['commits'])} commits):\n{msgs}\n" + "".join(parches)
            nota = f"Se revisaron los cambios: {len(comp['commits'])} commits, {len(comp.get('files', []))} archivos."
            titulo_nuevo = "Qué cambió"
        except Exception as e:
            log("  No pude comparar, leo completo:", e)

    if material is None:
        titulo_nuevo = "Qué hay nuevo"
        if info.get("size", 0) > 300_000:  # más de ~300 MB: solo el README
            try:
                readme = http(f"https://raw.githubusercontent.com/{nombre}/{rama}/README.md").decode("utf-8", "ignore")
            except Exception:
                readme = "(sin README)"
            material = cab + "Repositorio demasiado grande para clonarlo; solo README:\n" + readme[:200_000]
            nota = "Repositorio muy grande: se leyó solo el README."
        else:
            with tempfile.TemporaryDirectory() as tmp:
                subprocess.run(["git", "clone", "-q", "--depth", "1", f"https://github.com/{nombre}.git", tmp],
                               check=True, timeout=600)
                codigo, leidas, total = leer_codigo(tmp, maximo)
            material = cab + "Código completo:\n" + codigo
            nota = f"Se leyeron {leidas:,} de {total:,} líneas de código." + (
                "" if leidas >= total else f" (límite de {maximo:,}; súbalo en fuentes.json)")

    texto = analizar(INSTRUCCIONES.format(nuevo=titulo_nuevo) + "\n---\n" + material)
    est["repos"][nombre] = {"sha": sha, "pushed": info["pushed_at"], "revisado": HOY}
    return texto, nota


# ---------- webs ----------
def texto_web(url):
    crudo = http(url, cab={"User-Agent": "Mozilla/5.0 agente-revisor"}).decode("utf-8", "ignore")
    crudo = re.sub(r"(?is)<(script|style|noscript).*?</\1>", " ", crudo)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", crudo))).strip()


def revisar_web(url, est):
    nuevo = texto_web(url)
    h = hashlib.sha1(nuevo.encode()).hexdigest()
    previo = est["webs"].get(url, {})
    if previo.get("hash") == h:
        return None, None
    carpeta = os.path.join(RAIZ, ".webs")
    os.makedirs(carpeta, exist_ok=True)
    archivo = os.path.join(carpeta, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    viejo = open(archivo, encoding="utf-8").read() if os.path.exists(archivo) else ""
    material = f"Página: {url}\n\nVERSIÓN ANTERIOR:\n{viejo[:150_000] or '(primera vez)'}\n\nVERSIÓN ACTUAL:\n{nuevo[:150_000]}"
    texto = analizar(INSTRUCCIONES.format(nuevo="Qué cambió" if viejo else "Qué hay nuevo") + "\n---\n" + material)
    open(archivo, "w", encoding="utf-8").write(nuevo)
    est["webs"][url] = {"hash": h, "revisado": HOY}
    return texto, "Página web " + ("con cambios." if viejo else "revisada por primera vez.")


# ---------- informes ----------
def guardar_informe(nombre, texto, nota):
    carpeta = os.path.join(RAIZ, "informes", HOY)
    os.makedirs(carpeta, exist_ok=True)
    archivo = re.sub(r"[^\w.-]+", "_", nombre)[:120] + ".md"
    open(os.path.join(carpeta, archivo), "w", encoding="utf-8").write(f"# {nombre}\n\n_{nota}_\n\n{texto}\n")
    linea = next((l for l in texto.splitlines() if l.upper().startswith("EN UNA L")), "").split(":", 1)[-1].strip()
    with open(os.path.join(carpeta, "RESUMEN.md"), "a", encoding="utf-8") as f:
        f.write(f"- [{nombre}]({archivo}) — {linea or 'ver informe'}\n")


def main():
    if not GEMINI_KEY:
        sys.exit("Falta el secreto GEMINI_API_KEY")
    est = cargar_estado()
    if SOLO:  # revisión inmediata pedida a mano
        tarea = [SOLO]
    else:
        inicio_corrida = dt.datetime.utcnow().isoformat() + "Z"
        try:
            descubrir(est)
        except Exception as e:  # si GitHub falla, igual se trabaja la cola que ya había
            log("No pude buscar novedades:", e)
            inicio_corrida = est["ultima"]
        est["ultima"] = inicio_corrida
        guardar_estado(est)
        tarea = CFG["webs"] + [c["repo"] for c in est["cola"][: LIM["repos_por_corrida"]]]
    log(f"Por revisar: {len(tarea)} | en cola total: {len(est['cola'])}")

    for item in tarea:
        if time.time() - INICIO > TIEMPO_MAX:
            log("Se acabó el tiempo de esta corrida; sigue mañana.")
            break
        log("→", item)
        try:
            if item.startswith("http"):
                texto, nota = revisar_web(item, est)
            else:
                texto, nota = revisar_repo(item, est)
                est["cola"] = [c for c in est["cola"] if c["repo"] != item]
            if texto:
                guardar_informe(item, texto, nota)
        except Exception as e:
            log("  Error, queda para la próxima:", e)
        guardar_estado(est)
        time.sleep(60)  # Gemini gratis se satura por minuto con códigos grandes
    log("Pendientes en cola:", len(est["cola"]))


if __name__ == "__main__":
    main()
