# google/elephant-goldfish-model

_Se leyeron 8,760 de 8,760 líneas de código._

EN UNA LÍNEA: EGM es un plugin gratuito de código abierto para diseñar y revisar especificaciones de software con asistentes de inteligencia artificial.

## Qué es
Hechos:
- Es un plugin de código abierto para asistentes de programación con IA.
- Tiene dos partes: Elephant guarda la información del proyecto y escribe la especificación; Goldfish revisa el borrador y el código sin ver la conversación anterior, para encontrar suposiciones ocultas y errores.
- Tú decides los cambios de arquitectura y apruebas la especificación antes de programar.
- Incluye herramientas para lluvia de ideas, redactar diseños, revisar documentos, resolver problemas, documentar código, buscar diferencias entre diseño y código, y hacer revisiones rápidas.
- Se puede instalar en ChatGPT para escritorio, Codex, Claude Code y Antigravity CLI.
- Tiene licencia Apache 2.0.
- No es un producto oficialmente soportado por Google.
- Tiene 23,016 estrellas en GitHub.

Suposiciones (sin confirmar):
- Que funciona con cualquier modelo de inteligencia artificial.
- Que no cuesta dinero usarlo (el código es gratis, pero el asistente de IA puede tener costo).

## Qué hay nuevo
Hechos:
- El material muestra el repositorio actual con documentación, scripts para empaquetar el plugin y un adaptador experimental para OpenCode.
- Incluye pruebas de aislamiento para revisores en Claude, Codex, Copilot y Cursor.

Suposiciones (sin confirmar):
- Que el proyecto se actualiza con frecuencia.
- Que hay una versión nueva reciente.

## Cosas útiles
Hechos:
- Código completo disponible en GitHub bajo licencia Apache 2.0.
- Ocho habilidades reutilizables: egm-brainstorm, egm-draft, egm-review, egm-drift-report, egm-bootstrap, egm-lite, egm-resolve y egm-review-loop.
- Ejemplos de comandos que se pueden copiar, como revisar un documento de diseño o buscar diferencias entre el diseño y el código.
- Scripts para crear paquetes del plugin y preparar lanzamientos.
- Sitio de documentación en egm.dev.
- Pruebas de ejemplo para cada habilidad.

Suposiciones (sin confirmar):
- Que los ejemplos de código se pueden reutilizar en otros proyectos sin problemas.
- Que incluye modelos o APIs de inteligencia artificial gratis (el material no menciona ningún modelo ni API específica).

## Avisos
Hechos:
- Requiere un asistente de IA compatible (ChatGPT para escritorio, Codex, Claude Code o Antigravity) para funcionar.
- Las revisiones de Goldfish necesitan que el asistente cree subagentes con contexto nuevo; si no puede, EGM detiene la revisión.
- Una revisión no reemplaza las pruebas ni el juicio de una persona.
- No es un producto oficialmente soportado por Google.
- Tiene licencia Apache 2.0.
- Los archivos dicen Copyright 2026 Google LLC.

Suposiciones (sin confirmar):
- Que no hay costos ocultos.
- Que funciona directamente con Cloudflare o GitHub Actions.
- Que es seguro para compartir datos sensibles (el material menciona un documento de privacidad, pero no se incluye su contenido).

## ¿Sirve para sus proyectos?
No para los tres proyectos tal cual. EGM diseña y revisa especificaciones de software con asistentes de IA; no conecta a la API de Gemini, no entrena inteligencia artificial en Kaggle y no despliega aplicaciones en Cloudflare. Sí puede ayudar a redactar y revisar la documentación de las aplicaciones web publicadas con GitHub y Cloudflare, pero sin confirmar que se integre directamente con esos servicios.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
