# google/ax

_Se revisaron los cambios: 1 commits, 3 archivos._

EN UNA LÍNEA: Google lanzó AX, un runtime de código abierto para orquestar agentes de IA con tareas y sesiones.
UTILIDAD: media

## Qué es
Hechos:
- AX (Agent Executor) es un runtime de código abierto de Google para orquestar agentes.
- Tiene 14,926 estrellas en su repositorio.
- Permite crear tareas con un objetivo (`goal`) y un ID de sesión (`sessionId`) para unir varios turnos de una misma conversación.
- El sistema guarda y pasa el ID de sesión, pero no guarda el historial ni el estado de la conversación.
- Si no se define un ID de sesión, el servidor asigna uno automáticamente.
- El ID de sesión no se puede cambiar después de crear la tarea.

Suposiciones (sin confirmar):
- Que Google mantiene activamente el proyecto.
- Que la palabra "atespace" en el documento significa "namespace" o espacio de nombres.

## Qué cambió
Hechos:
- Se agregó el archivo `docs/session.md` con una guía de sesiones.
- Se actualizó el README para incluir esa guía en la tabla de documentación.
- Se aclaró en `docs/manifests.md` que `spec.sessionId` es un ID de correlación y que AX no almacena el estado de la sesión.

## Cosas útiles
Hechos:
- Ejemplo de YAML para crear una tarea con `sessionId` que se puede copiar y reutilizar.
- Explicación de cómo viaja el ID de sesión con la tarea (`ax describe task`, `AX_TASK_YAML`, `$AX_METADATA_URL/...`).
- Documentación sobre manifiestos, runners, observabilidad y redes.

Suposiciones (sin confirmar):
- Que el ejemplo de YAML funciona igual en otros entornos sin cambios.

## Avisos
Hechos:
- AX no almacena el historial ni el estado de la sesión; el usuario debe proveer su propio almacenamiento.
- AX no revisa si las tareas con el mismo ID de sesión están relacionadas, ordenadas o en el mismo "atespace".
- No se muestra la licencia en el material revisado.
- Parece requerir infraestructura propia (control plane, runners, cluster).

Suposiciones (sin confirmar):
- Que usar AX es gratis (es código abierto, pero operarlo puede costar dinero en servidores o nube).
- Que incluye conectores listos para APIs o modelos propios.

## ¿Sirve para sus proyectos?
No. Porque parece requerir infraestructura propia, no confirma que sea gratis ni que traiga conectores a APIs o modelos propios, y no guarda el historial de la sesión, por lo que habría que construir eso adicionalmente.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
