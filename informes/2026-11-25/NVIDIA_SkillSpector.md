# NVIDIA/SkillSpector

_Se leyeron 15,000 de 278,511 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: SkillSpector es un escáner gratuito de NVIDIA que revisa habilidades de agentes de inteligencia artificial antes de instalarlas para buscar vulnerabilidades, patrones maliciosos y riesgos de seguridad.

## Qué es
- Es un escáner de seguridad para habilidades de agentes de IA, como las usadas por Claude Code, Codex y MCP.
- Detecta vulnerabilidades, inyección de instrucciones (prompt injection), robo de datos (data exfiltration) y riesgos en la cadena de suministro.
- Pertenece al pipeline NVIDIA Verified Skills, que escanea, evalúa y firma habilidades antes de publicarlas.
- El material indica que el repositorio tiene 27,663 estrellas en GitHub.
- Usa dos etapas: análisis estático rápido y, opcionalmente, evaluación semántica con un modelo de lenguaje (LLM).
- Tiene 71 patrones de detección divididos en 17 categorías.
- Puede generar reportes en terminal, JSON, Markdown y SARIF.
- Asigna una puntuación de riesgo de 0 a 100 con recomendación de instalar o no instalar.
- Según una investigación citada en el material, de 31,132 habilidades analizadas, el 26.1% contenía al menos una vulnerabilidad y el 5.2% mostraba intención maliciosa probable.

## Qué hay nuevo
El material no menciona novedades específicas de esta versión.

## Cosas útiles
- Herramienta gratuita y de código abierto bajo licencia Apache 2.0.
- Se puede instalar con pip, uv o ejecutar con Docker sin instalar Python.
- Funciona como servidor MCP para que agentes de IA lo usen como herramienta de seguridad.
- Consulta OSV.dev de forma gratuita y sin clave de API para buscar vulnerabilidades conocidas en dependencias.
- Ejemplo de código reutilizable en Python:
  ```python
  from skillspector import graph
  from skillspector.cleanup import cleanup_result

  result = graph.invoke({
      "input_path": "/ruta/a/habilidad",
      "output_format": "json",
      "use_llm": False,
  })
  print(f"Puntuación: {result['risk_score']}/100")
  cleanup_result(result)
  ```
- Ejemplo de código para usar como gate de instalación en CI (bloquea si el reporte no es seguro).
- Soporta proveedores de IA como OpenAI, Anthropic, Gemini (Google Cloud), Ollama, Azure OpenAI y NVIDIA Build.

## Avisos
- Requiere Python 3.12 o 3.13 para usar archivos precompilados; versiones más nuevas pueden necesitar compilar desde código fuente y pueden fallar.
- El análisis con IA es opcional, pero si se activa, envía el contenido de los archivos al proveedor elegido, lo que puede tener costo según ese proveedor.
- OSV.dev es gratuito, pero envía nombres de dependencias a ese servicio externo.
- Límites: 100 MiB por entrada, 10,000 archivos en un ZIP, 1 MB por archivo analizado, máximo 32 habilidades en escaneo recursivo y 18 minutos de tiempo total del flujo.
- No es un "sandbox": no ejecuta la habilidad analizada, pero no protege al usuario si decide instalarla de todas formas.
- El servidor MCP por HTTP no tiene autenticación y solo acepta conexiones locales (127.0.0.1).

## ¿Sirve para sus proyectos?
No. SkillSpector está diseñado para revisar habilidades de agentes de IA antes de instalarlas. El material no muestra que sirva para conectar la API de Gemini en Cloudflare, para entrenar una IA llamada Musa en Kaggle, ni para auditar apps web publicadas en GitHub y Cloudflare. Aunque soporta el proveedor Gemini de Google Cloud, eso no cubre los proyectos que usted mencionó.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
