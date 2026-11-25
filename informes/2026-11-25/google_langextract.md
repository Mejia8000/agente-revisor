# google/langextract

_Se leyeron 15,000 de 45,636 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: LangExtract es una librería de Python de Google que extrae datos estructurados de textos con IA y marca exactamente dónde aparece cada dato en el texto original.

## Qué es
Hechos del material:
- Es una librería de Python, versión 1.7.2 (archivo pyproject.toml).
- El repositorio es google/langextract y tiene 39 396 estrellas (README).
- Extrae información estructurada (nombres, emociones, relaciones, medicamentos) de textos no estructurados usando modelos de lenguaje (LLM).
- Cada extracción incluye su ubicación exacta en el texto fuente (source grounding con char_interval).
- Soporta modelos de Gemini (Google), OpenAI y modelos locales con Ollama.
- Genera un archivo HTML interactivo para revisar miles de extracciones en su contexto original.
- La licencia es Apache 2.0.
- El archivo de aviso (Disclaimer) dice que no es un producto oficialmente soportado de Google.

## Qué hay nuevo
Hecho: Los archivos proporcionados no incluyen un registro de cambios (changelog) que compare esta versión con versiones anteriores, por lo tanto no se puede confirmar qué funciones son nuevas.
Suposición: Las funciones mostradas (soporte para varios proveedores, visualización HTML, grounding preciso) pueden ser recientes, pero eso está sin confirmar.

## Cosas útiles
Modelos y APIs (hechos del material):
- Gemini: model_id como "gemini-3.5-flash", "gemini-3.1-flash-lite" y modelos Pro. Requiere API key de AI Studio o Vertex AI.
- OpenAI: model_id como "gpt-4o" y "gpt-4o-mini". Requiere API key y la instalación opcional `pip install langextract[openai]`.
- Ollama (local): model_id como "gemma2:2b". No requiere API key, pero hay que instalar y ejecutar Ollama localmente.
Herramientas gratis (hechos):
- La librería es de código abierto bajo licencia Apache 2.0.
- Hay una demostración en vivo en el navegador sin instalar nada: https://google-langextract.hf.space/ (README).
- Hay ejemplos listos para copiar: extracción de "Romeo y Juliet", extracción de medicamentos, estructuración de reportes de radiología (RadExtract), uso con Ollama y creación de proveedores personalizados.
Ejemplos de código reutilizables (hechos):
- Función `lx.extract(...)` con texto, instrucciones y ejemplos.
- Guardado en archivo `.jsonl` y generación de HTML con `lx.visualize(...)`.
- Soporte para procesar documentos largos desde URLs con `fetch_urls=True`.

## Avisos
Requisitos (hechos):
- Python 3.10 o superior.
- Instalación con `pip install langextract`.
- Para modelos en la nube se necesita una API key (variable de entorno `LANGEXTRACT_API_KEY` o similar).
Costos (hechos y sin confirmar):
- Gemini y OpenAI son servicios de pago que cobran por tokens; el README sugiere un plan de pago para producción y hacer pruebas pequeñas para estimar costos.
- Ollama local no cobra por API, pero requiere hardware propio (sin confirmar costos de hardware).
Límites (hechos):
- Cada pasada adicional de extracción (`extraction_passes > 1`) reprocesa los tokens y puede aumentar el costo.
- Descargar textos de URLs con `fetch_urls=True` tiene riesgos de seguridad (SSRF, accesos internos); solo se recomienda con URLs de confianza y en entorno aislado.
- Los modelos de Gemini tienen fechas de retiro; hay que revisar la documentación oficial.
Riesgos (hechos):
- El modelo de IA puede extraer información de los ejemplos en lugar del texto de entrada, o inventar datos; LangExtract marca estos casos con `char_interval = None` y se recomienda filtrarlos.
- No es un producto oficialmente soportado de Google (Disclaimer).
- Para aplicaciones de salud se aplican términos adicionales de Health AI Developer Foundations.

## ¿Sirve para sus proyectos?
Sus proyectos: conector a la API de Gemini en Cloudflare, IA propia llamada Musa que entrena en Kaggle, y apps web publicadas con GitHub y Cloudflare.

Respuesta: Sí, con condiciones, y algunos puntos están sin confirmar.

1. Conector a la API de Gemini en Cloudflare: Sí. LangExtract soporta Gemini y permite pasar una API key, por lo que puede usarse como base para un conector. Sin confirmar: que funcione directamente en Cloudflare Workers o Pages, ya que esos entornos tienen límites para ejecutar librerías Python pesadas y dependencias de red.
2. IA propia llamada Musa que entrena en Kaggle: Sí, para extraer información de textos usando ejemplos, pero no es una herramienta para entrenar modelos desde cero. Sin confirmar: que Kaggle permita instalar `langextract` y acceder a APIs externas como Gemini desde sus notebooks.
3. Apps web publicadas con GitHub y Cloudflare: Sí, se puede integrar en el backend de una app web que ejecute Python. No es solo para el frontend. Sin confirmar: cómo se despliega y guarda las API keys de forma segura en Cloudflare, y si GitHub Actions o Cloudflare Pages admiten las dependencias de esta librería.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
