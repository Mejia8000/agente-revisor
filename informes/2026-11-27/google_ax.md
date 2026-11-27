# google/ax

_Se leyeron 15,000 de 53,866 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: AX es un programa gratuito de Google para organizar y ejecutar muchas tareas de agentes de inteligencia artificial en clústeres, pero aún está en desarrollo temprano y puede cambiar mucho.

UTILIDAD: media

## Qué es
Hechos:
- AX (Agent Executor) es software de código abierto de Google bajo licencia Apache 2.0.
- Es un "runtime de orquestación de agentes": ejecuta muchas tareas autónomas de agentes en un clúster, con aislamiento y límites de recursos.
- Funciona sobre Agent Substrate, otro programa de Google que aísla las tareas y las puede pausar y reanudar.
- Se controla con archivos YAML y comandos como `ax apply`, `ax get`, `ax describe`, `ax suspend`, `ax resume` y `ax ssh`.
- Tiene cuatro piezas principales: Task (tarea), Workspace (espacio de trabajo con repositorios y archivos), Model (modelo de lenguaje) y Gateway (control de qué sitios puede visitar una tarea y cómo se inyectan contraseñas).
- Puede entrar a una tarea en ejecución con `ax ssh` si se activa `spec.debug: true`.
- La versión más reciente mencionada es v0.4.0-rc.2, una versión preliminar.
- Se puede instalar en Linux y macOS con un comando de descarga.

Suposiciones:
- Ninguna en esta sección.

## Qué hay nuevo
Hechos:
- El aviso del README dice que AX está en desarrollo activo y que es muy probable que haya cambios importantes que rompan compatibilidad antes de la versión estable.
- Incluye forma de instalar localmente (`ax local start`) y en clústeres Kubernetes (`ax install`).
- Incluye una interfaz web local llamada AX Studio (`ax studio`).
- Incluye ejemplos listos para copiar en la carpeta `examples/` y un script de recorrido en `hack/tour.sh`.

Suposiciones:
- No se puede saber qué cambió respecto a versiones anteriores porque el material no incluye historial de versiones (sin confirmar).

## Cosas útiles
Hechos:
- Código gratuito bajo licencia Apache 2.0.
- Instalador con un comando: `curl -fsSL ... | sh`.
- CLI llamada `ax` con comandos similares a `kubectl`.
- Ejemplo de tarea mínima en `examples/simple.yaml`.
- Ejemplo de grupo de trabajadores en `examples/workerpool.yaml`.
- Script de recorrido en `hack/tour.sh` que muestra tareas, espacios de trabajo, puertas de enlace y suspensión.
- Paquete de cliente en Go (`client/client.go`) para conectar con ax-server desde otro programa.
- Ejemplos de manifiestos para Gateway, Workspace, Task y Model.
- Imágenes preconstruidas de agentes publicadas en `agentexecutor/images`.

Suposiciones:
- Que los ejemplos se pueden copiar y usar en otros proyectos sin cambios: sin confirmar, porque dependen de tener AX y Agent Substrate instalados.
- Que AX Studio es gratuita y funciona sin configuración extra: sin confirmar, el material solo dice que existe.

## Avisos
Hechos:
- Licencia: Apache License 2.0.
- Advertencia oficial: está en desarrollo intenso y es muy probable que haya cambios importantes que rompan compatibilidad antes de la versión estable.
- La API es `v1alpha1` (versión alfa, puede cambiar sin aviso).
- ax-server no autentica a quienes se conectan todavía (según un comentario en el código de red).
- Requiere Agent Substrate instalado en el clúster.
- Requiere PostgreSQL para guardar la información de ax-server.
- Para modo local en macOS se necesita Docker, OrbStack, Docker Desktop o Colima (al menos 6 GiB de RAM).
- Los nombres de tareas y espacios deben tener máximo 63 caracteres, solo minúsculas, números y guiones.
- Hay límites de tamaño: la configuración de una tarea no puede superar 16 KiB en JSON; el archivo YAML de lanzamiento no puede superar unos 31 KiB; los valores de variables de entorno no pueden superar 32 KiB.
- Se necesita `kubectl` para algunas operaciones (se puede instalar automáticamente en `~/.ax/bin`).
- El paquete de cliente Go está en alfa y no tiene garantía de compatibilidad.

Suposiciones:
- Que usar AX en un servidor propio o en la nube tiene costo de infraestructura (servidor, base de datos): sin confirmar, el software es gratis pero el hardware no.
- Que conectar a modelos de lenguaje (como Gemini) puede tener costo según el proveedor: sin confirmar, depende de cada proveedor.

## ¿Sirve para sus proyectos?
No. Sus proyectos son personales, con IA gratis, conectores a APIs, modelos propios, apps web y automatizaciones. AX no es una herramienta sencilla para eso: requiere instalar y mantener un clúster (Kubernetes o Kind), Agent Substrate y PostgreSQL; está en desarrollo temprano con cambios que pueden romper todo; y su documentación y comandos están en inglés. Puede servir solo si ya tiene un clúster listo y quiere ejecutar muchos agentes aislados a gran escala.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
