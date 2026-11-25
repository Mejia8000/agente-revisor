# NVIDIA/NemoClaw

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: NVIDIA NemoClaw es una herramienta gratuita de NVIDIA para ejecutar agentes de inteligencia artificial de forma más segura dentro de entornos aislados llamados OpenShell.

## Qué es
Hechos:
- Es un proyecto de código abierto de NVIDIA con licencia Apache 2.0.
- Sirve para ejecutar agentes de inteligencia artificial (OpenClaw, Hermes y LangChain Deep Agents Code) dentro de "sandboxes" o entornos aislados de NVIDIA OpenShell.
- Incluye una herramienta de línea de comandos llamada NemoClaw CLI.
- Tiene funciones de seguridad como reglas de red, control de salida de datos, límites de procesos y contenedores.
- La instalación express funciona en sistemas DGX o Windows Subsystem for Linux (WSL).
- Está en etapa alfa (alpha).

Suposiciones:
- Ninguna confirmada por el material.

## Qué hay nuevo
Hechos:
- La forma recomendada de usar NemoClaw ahora son los "Agent Configs", que son más simples y flexibles.
- Todo el desarrollo futuro se centrará en Agent Configs.
- Existe una guía para migrar desde la versión anterior.
- Existe una versión ligera llamada "nemoclaw-light" para Hermes en terminales simples; se instala y se elimina sola cuando ya no se necesita.

Suposiciones (sin confirmar):
- Que Agent Configs reemplace por completo la experiencia anterior en el futuro.

## Cosas útiles
Hechos:
- La herramienta y su documentación son gratuitas y están en docs.nvidia.com/nemoclaw/latest/
- Hay guías rápidas para instalar y usar cada agente soportado.
- Hay ejemplos de la comunidad en github.com/NVIDIA/nemoclaw-community
- Hay un script para preparar el entorno de desarrollo: ./scripts/dev-setup.sh

Suposiciones (sin confirmar):
- Que los ejemplos de la comunidad se puedan copiar y usar directamente en otros proyectos sin cambios.

## Avisos
Hechos:
- Requisitos: hay que revisar los "Prerequisites" antes de instalar; se menciona host DGX o WSL soportado.
- Licencia: Apache 2.0.
- Es un proyecto alfa, por lo que no hay garantía de tiempos de respuesta para preguntas, errores o propuestas.
- El programa puede descargar materiales de internet; el usuario es responsable de revisar sus licencias y seguridad.
- Se proporciona "tal cual" (AS IS), sin garantía.
- No se debe reportar problemas de seguridad en issues públicos; hay que usar canales privados de NVIDIA.

Suposiciones (sin confirmar):
- Que no haya costos por usar la herramienta en sí (los costos dependerían de la infraestructura y del proveedor de inferencia).
- Que funcione en cualquier computadora sin requisitos de hardware especiales.

## ¿Sirve para sus proyectos?
No. NemoClaw está diseñado para ejecutar agentes de inteligencia artificial específicos (OpenClaw, Hermes y LangChain Deep Agents Code) dentro de entornos NVIDIA OpenShell. El material no menciona integración con la API de Gemini, entrenamiento en Kaggle, ni publicación de aplicaciones web en GitHub o Cloudflare. Por lo tanto, no sirve directamente para un conector a Gemini en Cloudflare, para una IA llamada Musa entrenada en Kaggle, ni para apps web publicadas con GitHub y Cloudflare.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
