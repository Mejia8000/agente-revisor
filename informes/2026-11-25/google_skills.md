# google/skills

_Se leyeron 15,000 de 99,891 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Este repositorio público de Google contiene habilidades y scripts listos para usar que ayudan a agentes de IA a configurar y operar productos de Google Cloud, como Gemini, GKE y BigQuery.

## Qué es
Hechos:
- Es un repositorio de Google llamado google/skills con 24 674 estrellas.
- Contiene "Agent Skills": instrucciones y código para que agentes de IA usen productos y tecnologías de Google, principalmente Google Cloud.
- Se instala con el comando `npx skills add google/skills`, lo que requiere tener Node.js.
- Incluye skills para Google Cloud (IAM, GKE, BigQuery, Cloud Storage), IA/ML (Gemini, Genkit, Model Garden, RAG), bases de datos, seguridad, hosting web y publicidad.
- También trae plugins para Claude Code, Codex y Antigravity CLI.
- Está bajo licencia Apache 2.0, que permite copiar, modificar y distribuir el código.

Suposiciones:
- Que todos los skills funcionan igual en cualquier entorno: sin confirmar.

## Qué hay nuevo
Hechos:
- El README lista muchos skills organizados por categoría, incluidos varios relacionados con Gemini API, Agent Platform, GKE, BigQuery y API Gateway.
- Incluye scripts de ejemplo en Python y Bash para tareas como analizar tráfico de agentes, validar especificaciones OpenAPI, calcular costos de ajuste de modelos (tuning) y registrar servicios en Agent Registry.
- Hay ejemplos de código para llamar a Gemini con el GenAI SDK, el SDK de OpenAI y el SDK de Vertex AI.

Suposiciones:
- Que esta lista está actualizada a la fecha actual: sin confirmar.

## Cosas útiles
Hechos:
- Modelos mencionados en ejemplos: gemini-4-argon, glm-5-maas, Gemma 4, Llama 3.1, Qwen 3 y otros (en scripts de inferencia y tuning).
- APIs: Google Cloud APIs, Gemini API, Agent Registry API, Skill Registry API, Vertex AI APIs, Cloud Monitoring API.
- Herramientas gratis: el repositorio y sus scripts son de código abierto bajo Apache 2.0.
- Ejemplos de código reutilizables:
  - `analyze_traffic.py`: clasifica patrones de tráfico (estable, ráfagas, estacional) y recomienda umbrales de alerta.
  - `validate_apigw_openapi.py` y `validate_mcp_openapi.py`: revisan especificaciones OpenAPI para API Gateway.
  - `calculate_cost.py`: estima costos por hora de despliegue en Model Garden.
  - `tune_open_model.py`: lanza trabajos de ajuste (fine-tuning) de modelos.
  - Scripts de ejemplo para llamar a Gemini desde Python.

Suposiciones:
- Que estos ejemplos se pueden copiar y usar sin cambios en otros proyectos: sin confirmar.

## Avisos
Hechos:
- Requiere Node.js y npx para instalar los skills.
- Muchos scripts necesitan una cuenta de Google Cloud, un proyecto GCP y credenciales configuradas con gcloud.
- Algunos servicios de Google Cloud tienen costo (Vertex AI, Vector Search, GKE, BigQuery, etc.).
- El archivo `calculate_cost.py` advierte que su tabla de precios puede estar desactualizada y que la factura real puede diferir por región, descuentos o reservas.
- Algunos scripts dependen de librerías específicas de Google Cloud (google-cloud-aiplatform, vertexai, etc.).
- Licencia: Apache 2.0.

Suposiciones:
- Que usar estos skills no genera costos en Google Cloud: sin confirmar (muchos servicios son de pago).
- Que el código es seguro para producción sin revisión previa: sin confirmar.

## ¿Sirve para sus proyectos?
Sus proyectos: un conector a la API de Gemini en Cloudflare, una IA propia llamada Musa que entrena en Kaggle, y apps web publicadas con GitHub y Cloudflare.

- Conector a la API de Gemini en Cloudflare: No directamente. El repositorio tiene ejemplos de cómo llamar a Gemini desde Python, pero están orientados a Google Cloud y Vertex AI, no a Cloudflare Workers ni Cloudflare Pages. Se puede usar como referencia de código, pero no es un conector listo para Cloudflare.
- IA propia llamada Musa que entrena en Kaggle: No. Los skills y scripts están diseñados para productos de Google Cloud (Vertex AI, Model Garden, Agent Platform), no para Kaggle. No hay evidencia de que soporten entrenamiento o modelos en Kaggle.
- Apps web publicadas con GitHub y Cloudflare: No directamente. Hay skills para Google Cloud Run, Firebase y API Gateway de Google Cloud, pero no para publicar o gestionar apps en Cloudflare ni para despliegue automático desde GitHub a Cloudflare. Se podría usar como referencia para monitoreo o estructura, pero no es una herramienta para esos proyectos.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
