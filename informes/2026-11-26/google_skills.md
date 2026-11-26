# google/skills

_Se revisaron los cambios: 4 commits, 58 archivos._

EN UNA LÍNEA: El repositorio google/skills agregó un complemento para Google Home y actualizó habilidades de API Gateway, solución de problemas de GKE/Kueue y configuración de Cloud Operator para agentes de IA.

UTILIDAD: media

## Qué es
- Repositorio público de Google llamado "skills" con 24,706 estrellas en GitHub.
- Contiene "habilidades" (skills) para que agentes de IA configuren productos y tecnologías de Google.
- Incluye complementos para Claude Code, Codex CLI, Gemini CLI, VS Code/GitHub Copilot/Cursor y Antigravity.
- Las habilidades son archivos de configuración e instrucciones que un agente de IA puede leer y ejecutar.

## Qué cambió
- Se agregó el complemento "google-home-developer" para buscar documentación oficial de Google Home, Matter y OpenThread, y consultar diagnósticos de integración de hogar inteligente a través de un servidor MCP remoto (https://homedevelopers.googleapis.com/mcp).
- Se actualizaron habilidades de Google Cloud API Gateway: seguridad y límites de velocidad, servidor MCP, autoría de especificaciones OpenAPI y solución de problemas. Incluyen correcciones de cuotas, seguridad de MCP y validación de especificaciones.
- Se endureció la habilidad "gke-kueue-troubleshooting" a la versión 1.1.1 con mejoras de seguridad, ocultación de datos sensibles, análisis de registros y validación de informes.
- Se agregó la habilidad "cloud-operator-admin-setup" (versión 1.0.0) para que administradores de organización activen, configuren y den acceso al Agente Cloud Operator en Google Cloud.
- Varias habilidades ahora exigen una etiqueta de atribución de uso al ejecutar comandos gcloud, REST o MCP.

## Cosas útiles
- Complemento google-home-developer: código público con licencia Apache-2.0; busca documentación pública sin credenciales y se conecta al servidor MCP de Google Home.
- Ejemplos de instalación para Antigravity, Claude Code, Codex CLI, Gemini CLI y VS Code/Cursor.
- Scripts de validación reutilizables: check_quota_metrics.py, validate_mcp_openapi.py, validate_apigw_openapi.py y lint_openapi_for_gateway.py.
- Ejemplos de comandos gcloud y YAML para configurar API Gateway, claves de API, JWT, cuotas y backends de Cloud Run.
- Comandos curl y gcloud de la habilidad cloud-operator-admin-setup para configurar Cloud Operator en una organización de Google Cloud.

## Avisos
- Requisitos: muchas habilidades necesitan Google Cloud CLI (gcloud), Python 3.10+, PyYAML, un proyecto de Google Cloud con facturación activa y las APIs habilitadas.
- Costos: API Gateway tiene un nivel gratuito mensual, pero exige una cuenta de facturación activa; el uso por encima del nivel y la transferencia de datos de salida se cobran (sin confirmar los precios actuales exactos).
- Licencia: el complemento google-home-developer y las habilidades usan licencia Apache-2.0.
- Límites: la documentación pública del servidor MCP funciona sin credenciales; los diagnósticos de Cloud-to-cloud y la documentación del Programa de Socios requieren OAuth 2.0 o credenciales predeterminadas en un proyecto de Google Cloud con homedevelopers.googleapis.com habilitado.
- Riesgos: las habilidades advierten no usar solo claves de API para autenticar usuarios finales, no cambiar métricas de cuota mientras una puerta de enlace usa una configuración anterior, y activar la comprobación de IAM del invocador en el backend antes de quitar acceso público (para evitar errores 403).
- (sin confirmar) No se confirma si todos los scripts de validación funcionan fuera de Google Cloud ni si todos los precios descritos están vigentes.

## ¿Sirve para sus proyectos?
Sí, con condiciones. El complemento Google Home y los ejemplos de API Gateway pueden reutilizarse en automatizaciones de hogar inteligente y apps web que se conecten a APIs de Google. Sin embargo, muchas habilidades requieren un proyecto de Google Cloud, facturación activa y la CLI de gcloud, por lo que no son completamente gratuitas ni independientes de Google Cloud para proyectos personales con IA gratis y modelos propios.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
