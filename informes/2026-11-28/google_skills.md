# google/skills

_Se revisaron los cambios: 1 commits, 4 archivos._

EN UNA LÍNEA: Actualización en las instrucciones de configuración para que los asistentes esperen unos minutos mientras se activan los permisos automáticos en Google Cloud.

UTILIDAD: Baja

## Qué es
Es un repositorio de Google que contiene guías e instrucciones ("skills") para que agentes de inteligencia artificial puedan realizar tareas y administrar recursos dentro de la plataforma empresarial Google Cloud Platform (GCP).

## Qué cambió
En esta actualización (versiones 1.5.0 y 1.6.0 de las herramientas de *Cloud Operator*):
- **Tiempos de espera por permisos:** Se le indica al agente que, si falla el acceso en la organización de la empresa del usuario, espere unos 2 minutos y reintente (hasta 10 o 15 minutos en total), ya que el acceso automático suele tardar ese tiempo en activarse tras el primer uso.
- **Manejo de errores:** Si aparece el error de que los agentes a nivel de organización no están habilitados, se le ordena al asistente no insistir ni pedir cambios de roles, ya que la función directamente no está disponible allí.
- **Identificación:** Se actualizaron las cadenas de texto (`User-Agent`) que identifican la versión de la herramienta al hacer peticiones a Google Cloud.

## Cosas útiles
- Ejemplos de comandos de consola (`gcloud`) para obtener la cuenta activa (`gcloud config get-value account`) o el dominio principal de una organización de Google Cloud.
- Pautas sobre cómo programar agentes de IA para que gestionen tiempos de espera y reintentos ante problemas de permisos temporales.

## Avisos
- **Incompatible con cuentas personales:** El documento especifica textualmente que Cloud Operator no admite cuentas personales de Google (como las que terminan en `@gmail.com`).
- **Requiere entorno corporativo:** Es obligatorio contar con una cuenta de organización empresarial dentro de Google Cloud.
- **Costos:** Aunque las instrucciones de este repositorio son abiertas, el uso de servicios en Google Cloud generalmente requiere tarjetas de crédito y puede generar costos (*sin confirmar* el precio exacto de Cloud Operator).

## ¿Sirve para sus proyectos?
No. Está diseñado únicamente para gestionar infraestructura de Google Cloud en cuentas empresariales u organizaciones. Como tus proyectos son personales, con herramientas gratuitas o modelos propios, esta actualización no te aporta nada aplicable (el sistema rechaza explícitamente cuentas personales gratuitas de Google).
