# NVIDIA/TensorRT-LLM

_Se revisaron los cambios: 4 commits, 25 archivos._

EN UNA LÍNEA: TensorRT-LLM de NVIDIA optimiza la ejecución de modelos de lenguaje en GPUs NVIDIA, con soporte nuevo para chips Rubin y correcciones en sus pruebas internas.
UTILIDAD: media

## Qué es
Hechos:
- Es un repositorio de NVIDIA con 15 140 estrellas.
- Ofrece una API de Python para definir modelos de lenguaje grandes (LLM).
- Incluye optimizaciones para hacer inferencia eficiente en GPUs NVIDIA.
- Tiene componentes para crear tiempos de ejecución (runtimes) en Python y C++.

Suposiciones:
- Que es gratuito para uso personal: sin confirmar (algunos archivos nuevos muestran licencia Apache 2.0, pero el material no muestra la licencia completa del repositorio).

## Qué cambió
Hechos:
- Se agregó soporte para la arquitectura Rubin (SM107) en la función GVR (Guess-Verify-Refine), además de Blackwell.
- Se aceptan valores index_topk de 512, 1024 y 2048, y ratios de compresión 1 y 4.
- Se agregó una clase PreparedRowTopK para ejecutar con conciencia de localidad en Rubin.
- Se agregaron pruebas nuevas para Rubin y se actualizaron pruebas existentes.
- Se actualizaron dependencias en ejemplos de escaneo de seguridad (por ejemplo, openai de 3.59.0 a 3.60.0, huggingface-hub de 2.4.0 a 2.5.0).
- Se corrigió un error de ordenamiento en pruebas internas (CBTS).

Suposiciones:
- Que estos cambios mejoran la velocidad en proyectos reales: sin confirmar (el material no incluye mediciones de rendimiento).
- Que el chip Rubin está disponible para el usuario: sin confirmar.

## Cosas útiles
- API de Python para definir LLMs (hecho).
- Ejemplos de código y pruebas en la carpeta tests/ que se pueden revisar (hecho).
- Actualizaciones de librerías como openai y huggingface-hub en los archivos de ejemplo (hecho).

## Avisos
- Requiere GPU NVIDIA (se mencionan Hopper, Blackwell y Rubin).
- Algunas funciones solo funcionan en Rubin (SM107).
- Algunas combinaciones de parámetros no soportadas usan un camino alternativo (hecho).
- Hay que preparar la ejecución antes de capturar gráficos CUDA y cerrar los recursos al terminar (hecho).
- Las pruebas nuevas exigen una GPU Rubin para correr (hecho).
- Está dirigido a usuarios con experiencia en CUDA e inferencia de modelos: sin confirmar.

## ¿Sirve para sus proyectos?
No, salvo que tenga una GPU NVIDIA compatible y quiera ejecutar sus propios modelos de lenguaje localmente con la mayor velocidad posible. Para conectarse a APIs externas, crear apps web sencillas o hacer automatizaciones sin GPU NVIDIA, esta herramienta no es adecuada.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
