# google/adk-python

_Se leyeron 15,000 de 793,566 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: ADK es una herramienta gratuita de Google en Python para crear, probar y desplegar agentes de IA que usan modelos como Gemini.

## Qué es
Hechos (lo que muestra el material):
- Es un kit de desarrollo de código abierto de Google, con licencia Apache 2.0.
- Está escrito en Python y se instala con `pip install google-adk`.
- Requiere Python 3.11 o superior.
- La versión del repositorio es 2.15.1.
- Sirve para construir agentes de IA, evaluarlos y desplegarlos.
- Está optimizado para Gemini de Google, pero dice ser compatible con otros modelos (modelo-agnóstico).
- Permite crear flujos de trabajo con varios agentes, reglas de enrutamiento, reintentos, memoria y nodos dinámicos.
- Tiene una interfaz web para probar agentes (`adk web`).
- Puede desplegarse en contenedores Docker o en Google Cloud Run.

Suposiciones:
- Que funcione en otros servicios en la nube además de Google Cloud: sin confirmar.

## Qué hay nuevo
Hechos (lo que muestra el material):
- El README presenta el proyecto como "Agent Development Kit (ADK) 2.0".
- Incluye "Agent Config" para crear agentes sin escribir código, usando archivos YAML.
- Incluye flujo de confirmación de herramientas con intervención humana (human-in-the-loop).
- Soporta flujos basados en grafos (`Workflow`) con nodos dinámicos, bucles y reintentos.
- Soporta protocolo A2A (agente a agente) y herramientas MCP.
- Incluye ejemplos de código listos para usar en la carpeta `contributing/samples/`.

Suposiciones:
- Que la versión 2.0 traiga cambios importantes respecto a versiones anteriores: sin confirmar (el material no compara con versiones previas).

## Cosas útiles
Hechos (modelos, APIs o herramientas gratis, ejemplos de código que se puedan reutilizar):
- Paquete gratuito en PyPI: `google-adk`.
- Código de ejemplo para crear un agente con `Agent(...)` y un flujo con `Workflow(...)`.
- Comandos de línea de comandos: `adk run`, `adk web`, `adk eval`, `adk deploy`.
- Ejemplos listos para usar en `contributing/samples/` (agentes de búsqueda, ejecución de código, triaje de pull requests, análisis de documentos, etc.).
- Documentación en https://adk.dev/
- Plantillas de configuración de agentes en YAML (`root_agent.yaml`).
- Compatibilidad opcional con modelos de Anthropic, OpenAI, LangGraph, LlamaIndex y CrewAI (requiere instalar extras adicionales).

Suposiciones:
- Que todos los ejemplos funcionen sin cambios en su entorno: sin confirmar.

## Avisos
Hechos (requisitos, licencia, costos, límites, riesgos):
- Requisito: Python 3.11+.
- Licencia: Apache 2.0 (permite uso comercial y modificación).
- El código es gratis, pero usar la API de Gemini de Google puede tener costos (Google no publica precios en este repositorio).
- Despliegue en "Agent Runtime on Gemini Enterprise Agent Platform" (antes Vertex AI Agent Engine) puede implicar costos de Google Cloud: sin confirmar precios.
- Algunas funciones están marcadas como experimentales (por ejemplo, `run_live`).
- Hay muchas dependencias opcionales de Google Cloud u otros proveedores; instalar todo puede ser pesado.
- No hay mención de soporte para Cloudflare ni para Kaggle en este material.

Suposiciones:
- Que el uso de Gemini sea gratuito: sin confirmar (depende del plan de Google).
- Que se pueda desplegar sin costo en Cloudflare: sin confirmar.

## ¿Sirve para sus proyectos?
- Conector a la API de Gemini en Cloudflare: No. El material solo muestra despliegue en Docker y Google Cloud Run. No menciona Cloudflare Workers, Cloudflare Pages ni su API de Gateway. Cualquier integración con Cloudflare sería sin confirmar y requeriría trabajo adicional.
- IA propia llamada Musa que entrena en Kaggle: No. ADK sirve para orquestar agentes que ya usan modelos entrenados; no es una plataforma para entrenar modelos nuevos. Kaggle no aparece en el material.
- Apps web publicadas con GitHub y Cloudflare: Parcial. Puede guardar el código en GitHub, pero el despliegue recomendado es Google Cloud Run o Docker, no Cloudflare. Para usar Cloudflare necesitaría adaptar el código por su cuenta: sin confirmar.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
