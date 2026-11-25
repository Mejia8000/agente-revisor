# Agente revisor

Creado por **José Ramón Mejía** (Managua, Nicaragua), 2026.

Un agente que vigila GitHub por ti y te explica en español lo que encuentra, sin pagar nada.

## Qué hace
- Dos veces al día busca los repositorios de **Google y NVIDIA** que tuvieron cambios.
- Si un repositorio es nuevo para él, **lee el código completo** (hasta 15 000 líneas); si ya lo conocía, lee solo lo que cambió.
- **Gemini** escribe un informe en español sencillo: qué es, qué hay nuevo, qué sirve gratis, avisos y si es útil. Si Gemini está ocupado, lo hace **NVIDIA Nemotron** (gratis por OpenRouter).
- Empieza por los más importantes (más estrellas) y deja todo en `informes/AAAA-MM-DD/`, con un `RESUMEN.md` de una línea por repositorio.
- También puede vigilar páginas web y avisar qué cambió.

## Cómo usarlo
1. Copia (fork) este repositorio.
2. En Settings → Secrets → Actions agrega `GEMINI_API_KEY` (gratis en aistudio.google.com) y, si quieres respaldo, `OPENROUTER_API_KEY`.
3. Edita `fuentes.json` para agregar organizaciones, repositorios o páginas web. Al guardar, corre solo.

## Licencia
MIT. Si usas o copias este proyecto, conserva el nombre del autor y el aviso de la licencia.
