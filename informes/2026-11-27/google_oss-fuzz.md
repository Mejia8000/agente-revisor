# google/oss-fuzz

_Se leyeron 15,000 de 284,595 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: OSS-Fuzz es una herramienta de Google que busca errores y fallos de seguridad en software de código abierto usando pruebas automáticas llamadas fuzzing.
UTILIDAD: media

## Qué es
Hechos:
- Es un repositorio de Google en GitHub con más de 12,000 estrellas.
- Es un servicio continuo de fuzzing para software de código abierto.
- El fuzzing es una técnica que envía datos a un programa para encontrar errores, como desbordamientos de búfer, que pueden ser problemas de seguridad.
- Soporta lenguajes de programación como C/C++, Rust, Go, Python, Java/JVM, JavaScript y Lua.
- Usa motores de fuzzing como libFuzzer, AFL++ y Honggfuzz, junto con herramientas llamadas Sanitizers y ClusterFuzz.
- Hasta mayo de 2025, ayudó a corregir más de 13,000 vulnerabilidades y 50,000 errores en más de 1,000 proyectos.
- Su licencia es Apache 2.0.

Suposiciones:
- Que el servicio de Google es gratuito para proyectos de código abierto: sin confirmar.

## Qué hay nuevo
Hechos:
- Hay publicaciones de blog de 2023 y 2024 sobre el uso de inteligencia artificial para encontrar más vulnerabilidades con fuzzing.
- El código incluye soporte para sistemas operativos como Ubuntu 24.04 en varios proyectos.
- Incluye scripts para crear imágenes de Docker y ejecutar fuzzing en sistemas de integración continua.

Suposiciones:
- Que la inteligencia artificial ya está disponible para cualquier usuario de la herramienta pública: sin confirmar.

## Cosas útiles
Hechos:
- Ejemplos de fuzzers listos para copiar y adaptar en C++, Python, Java y JavaScript dentro de la carpeta projects/.
- Plantillas para crear nuevos proyectos de fuzzing (archivos Dockerfile, build.sh y project.yaml).
- Un script de Python para encontrar en qué versión apareció un error (infra/bisector.py).
- ClusterFuzzLite, una herramienta gratuita de código abierto para ejecutar tu propio sistema de fuzzing sin depender de Google.
- Documentación pública en https://google.github.io/oss-fuzz.

Suposiciones:
- Que todos los ejemplos funcionan sin cambios en cualquier proyecto propio: sin confirmar.

## Avisos
Hechos:
- Requiere instalar y usar Docker para la mayoría de las tareas.
- Algunos scripts necesitan herramientas externas como gcloud, gsutil o wget.
- El código está bajo licencia Apache 2.0.
- Soporta principalmente las arquitecturas x86_64 e i386.
- No es una plataforma para crear aplicaciones web ni para entrenar modelos de inteligencia artificial.

Suposiciones:
- Que usar el servicio de Google no tiene costo: sin confirmar.
- Que ejecutar ClusterFuzzLite en la nube no genera costos de infraestructura: sin confirmar.

## ¿Sirve para sus proyectos?
No. OSS-Fuzz está diseñado para buscar fallos de seguridad en software que ya existe, no para crear aplicaciones web, conectores a APIs ni modelos de inteligencia artificial. Solo le sería útil si quiere probar la seguridad de una API o automatización que ya haya programado, pero no le ayuda a construirlas.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
