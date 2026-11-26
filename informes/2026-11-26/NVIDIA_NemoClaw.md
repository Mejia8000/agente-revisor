# NVIDIA/NemoClaw

_Se revisaron los cambios: 1 commits, 5 archivos._

EN UNA LÍNEA: NVIDIA actualizó la documentación de NemoClaw, su herramienta para crear agentes de IA seguros dentro de OpenShell, y agregó una nueva forma de desplegarlos usando archivos YAML.
UTILIDAD: media

## Qué es
Hecho: NemoClaw es un proyecto de código abierto (licencia Apache-2.0) de NVIDIA para crear agentes de IA especializados.
Hecho: Combina un modelo de IA, un conjunto de instrucciones y herramientas (llamado "open agent harness") y el runtime NVIDIA OpenShell, que ejecuta al agente en un entorno aislado (sandbox) con control sobre archivos, procesos y red.
Hecho: Existen dos versiones: v0 y v1 (llamada Agent Configs). La v1 usa un archivo YAML para definir el despliegue, permite prever cambios con el comando `plan` y aplicarlos con `apply`, mediante una CLI o un SDK de Rust.
Hecho: Soporta agentes como OpenClaw, Hermes y LangChain Deep Agents Code.
Hecho: Las plataformas principalmente probadas son Linux y DGX Spark; también documenta límites para macOS, Windows (WSL), DGX Station y servidores Linux sin interfaz gráfica.
Suposición (sin confirmar): Que se puedan usar modelos propios sin costo.

## Qué cambió
Hecho: Se modificó la página principal (docs/index.mdx) y la descripción general (docs/about/overview.mdx) para explicar los cambios en "Agent Configs".
Hecho: Se agregó una imagen que muestra el flujo: definir el despliegue en YAML, prever cambios con `plan` y desplegar con `apply`.
Hecho: Se actualizó un script de vista previa (scripts/fern-preview-config.mts) y sus pruebas para manejar enlaces de la versión v1.
Hecho: La transición de la versión v0 a la v1 está planeada para terminar en el primer trimestre de 2027.
Suposición (sin confirmar): Que el cambio en la documentación refleje un cambio real en el software y no solo en los textos.

## Cosas útiles
Hecho: Licencia Apache-2.0 (código abierto).
Hecho: Se menciona un archivo YAML para definir despliegues de forma reutilizable.
Hecho: Comandos `plan` y `apply` para revisar y aplicar cambios.
Hecho: Un texto de ayuda (prompt) listo para copiar y pegar en un asistente de programación y configurar NemoClaw.
Suposición (sin confirmar): Que existan modelos o APIs completamente gratis dentro de NemoClaw (el texto menciona modelos hospedados como NVIDIA Nemotron, pero no dice si son gratuitos).
Suposición (sin confirmar): Que los ejemplos de configuración se puedan copiar directamente a proyectos personales.

## Avisos
Hecho: Requiere instalar OpenShell y NemoClaw.
Hecho: Por defecto el proyecto envía datos de uso (telemetría) a NVIDIA; se puede desactivar con `export NEMOCLAW_DISABLE_TELEMETRY=1`.
Hecho: Licencia: Apache-2.0.
Hecho: Funciona principalmente en Linux y DGX Spark; macOS, Windows (WSL) y servidores sin pantalla tienen limitaciones documentadas.
Suposición (sin confirmar): Que usar modelos hospedados (como NVIDIA Nemotron) tenga costo.
Suposición (sin confirmar): Que DGX Spark sea hardware caro o necesario.
Riesgo: La versión v0 será reemplazada por la v1 en 2027, lo que puede obligar a migrar despliegues existentes.

## ¿Sirve para sus proyectos?
No: no se confirma que sea gratuito para proyectos personales, y está pensado principalmente para Linux y entornos NVIDIA (DGX Spark), no para apps web o automatizaciones sencillas.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
