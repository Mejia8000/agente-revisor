# NVIDIA/open-gpu-kernel-modules

_Se leyeron 15,000 de 1,713,624 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Es el código fuente abierto de los controladores de kernel de NVIDIA para tarjetas gráficas en Linux.

UTILIDAD: baja

## Qué es
Hechos (lo que muestra el material):
- Es el código fuente de los módulos del kernel de NVIDIA para Linux, versión 620.73.04.
- Lo publica NVIDIA en GitHub.
- Incluye código para compilar los módulos del kernel (nvidia.ko, nvidia-modeset.ko, nvidia-drm.ko, nvidia-uvm.ko).
- Incluye scripts de Python para extraer firmware de las tarjetas gráficas para los controladores Nouveau y Nova.
- Incluye código del controlador DRM de NVIDIA para gestionar pantallas, conectores y colores en Linux.
- Tiene licencia MIT (se lee en los archivos de código).
- Soporta GPUs desde la serie Turing en adelante (RTX 20 y posteriores, incluidas Quadro, Tesla, A100, H100 y otras).
- Soporta Linux kernel 4.15 o superior.
- Se compila en arquitecturas x86_64 y aarch64.

Suposiciones (sin confirmar):
- Que el código esté completo y funcione tal como se publica.
- Que NVIDIA acepte cambios externos en el código.

## Qué hay nuevo
Hechos (lo que muestra el material):
- La versión publicada es 620.73.04.
- La lista de GPUs soportadas incluye modelos recientes como RTX 5090, RTX 5080, RTX PRO Blackwell, GB200 y B200.
- Incluye código para gestión avanzada de color en pantallas (PQ, HDR, pipelines de color).

Suposiciones (sin confirmar):
- Que esta versión traiga mejoras respecto a versiones anteriores.

## Cosas útiles
Hechos (lo que muestra el material):
- Código fuente completo bajo licencia MIT, gratuito para ver, modificar y compilar.
- Scripts de Python en la carpeta `nouveau/` para extraer firmware binario de las GPUs.
- Ejemplos de código C para el kernel de Linux (colas de hilos, tablas PCI, utilidades comunes, controlador DRM).
- Instrucciones de compilación con `make modules`.
- Soporte para compilar para otra arquitectura (cross-compiling) de x86_64 a aarch64.

Suposiciones (sin confirmar):
- Que estos scripts y código se puedan reutilizar en otros proyectos.
- Que el código del controlador de pantalla sirva como referencia para otros proyectos similares.

## Avisos
Hechos (lo que muestra el material):
- Requiere instalar el controlador de usuario de NVIDIA versión 620.73.04 (archivo .run con opción --no-kernel-modules).
- Requiere firmware GSP correspondiente.
- Solo funciona en GPUs Turing o posteriores (no sirve para tarjetas más viejas).
- Solo es para Linux.
- El código se publica como copia de cada versión del controlador, sin historial detallado de cambios individuales.
- Las contribuciones requieren aceptar un Acuerdo de Licencia de Contribuidor (CLA).
- Compilar módulos del kernel requiere conocimientos avanzados y puede afectar la estabilidad del sistema.

Suposiciones (sin confirmar):
- Que usar este código en un sistema importante pueda causar problemas si no se compila correctamente.
- Que no hay soporte oficial para usos fuera de los controladores de NVIDIA.

## ¿Sirve para sus proyectos?
No.

Por qué:
- Sus proyectos son: proyectos personales con IA gratis, conectores a APIs, modelos propios, apps web y automatizaciones.
- Este material es código de bajo nivel para controlar hardware de gráficos NVIDIA en el kernel de Linux.
- No contiene modelos de IA, APIs de IA, herramientas para entrenar modelos, ni ejemplos para crear apps web o conectores a servicios web.
- No es útil para automatizaciones de IA ni para desarrollo web.

Suposiciones (sin confirmar):
- Que alguien quiera modificar el driver de gráficos para un proyecto personal muy específico.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
