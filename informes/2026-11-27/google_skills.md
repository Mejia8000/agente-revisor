# google/skills

_Se revisaron los cambios: 2 commits, 5 archivos._

EN UNA LÍNEA: Corrección en las instrucciones de Google Cloud Operator para operar únicamente por organización y evitar errores al invocar proyectos individuales.
UTILIDAD: Baja

## Qué es
Es un conjunto de instrucciones de texto (habilidades o *skills*) diseñadas para que agentes de inteligencia artificial sepan cómo interactuar y configurar el asistente de operaciones de Google Cloud ("Cloud Operator") mediante un servidor de herramientas llamado `autocloud`.

## Qué cambió
* **Eliminación del parámetro de proyecto:** Se instruye a la IA a no llamar nunca a Cloud Operator indicando un `project` directamente, ya que el servicio solo funciona a nivel de organización (`organization`). Antes, llamar con un proyecto provocaba un error de permiso (`RUN_NOT_ALLOWED`).
* **Mensaje al usuario más preciso:** Se ajustó la regla para que el asistente no le diga al usuario que el operador ya comenzó a trabajar antes de que la orden realmente se haya enviado o aprobado.
* **Manejo de errores:** Se actualizó la tabla de solución de problemas para distinguir si el fallo ocurrió por enviar el parámetro de proyecto por error o si la organización realmente no tiene habilitado el servicio.
* **Subida de versiones:** La habilidad de configuración subió a la versión 1.4.0 y la de operación a la 1.5.0.

## Cosas útiles
Comandos de la herramienta de Google Cloud (`gcloud`) que se pueden reutilizar en automatizaciones propias:
* `gcloud projects get-ancestors {project_id} --format=json`: útil para consultar qué organización o carpeta es dueña de un proyecto.
* `gcloud organizations list --filter="displayName={domain}" --format=json`: para listar y filtrar organizaciones por nombre de dominio.
* `gcloud auth application-default login`: comando estándar para autenticar tu cuenta de usuario en local.

## Avisos
* **No admite cuentas personales gratuitas:** El documento indica explícitamente que Cloud Operator no funciona con cuentas personales de Google (como cuentas `@gmail.com`) ni con proyectos sueltos sin organización empresarial.
* **Riesgo de costos:** Aunque los archivos del repositorio son texto abierto, operar recursos dentro de Google Cloud puede generar cargos en facturación.
* **Requisitos:** Requiere tener instalada la consola `gcloud`, credenciales de usuario configuradas y un servidor MCP compatible (`autocloud`).

## ¿Sirve para sus proyectos?
**No.**
**Por qué:** Tus proyectos se enfocan en inteligencia artificial gratuita, modelos propios y herramientas personales. Este cambio solo afecta a instrucciones para gestionar infraestructura corporativa de Google Cloud bajo cuentas de organización pagas, descartando expresamente cuentas de correo comunes o proyectos sin estructura empresarial.
