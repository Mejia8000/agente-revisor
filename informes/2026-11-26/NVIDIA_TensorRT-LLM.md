# NVIDIA/TensorRT-LLM

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: TensorRT-LLM es una herramienta gratuita de NVIDIA para hacer correr modelos de lenguaje y generación de imágenes más rápido en tarjetas gráficas NVIDIA.

UTILIDAD: media

## Qué es
Hechos del material:
- Es una librería de código abierto (licencia Apache 2) creada por NVIDIA.
- Sirve para optimizar la inferencia (uso) de modelos de lenguaje grandes (LLM) y modelos de generación visual en tarjetas gráficas NVIDIA.
- Tiene una interfaz de programación en Python para definir y ejecutar estos modelos, desde una sola tarjeta hasta varios servidores.
- Está construido sobre PyTorch y se puede modificar y ampliar.
- Incluye ejemplos de código y documentación de inicio rápido.
- Recopila datos de uso anónimos por defecto, pero se puede desactivar.

Suposición: que sea fácil de instalar para alguien sin experiencia (sin confirmar).

## Qué hay nuevo
Hechos del material:
- Agregó soporte para modelos de generación de imágenes (diffusion models).
- Tiene soporte desde el primer día para modelos GPT-OSS-120B y GPT-OSS-20B de OpenAI y para EXAONE 4.0 de LG AI Research.
- Incluye optimizaciones para modelos como Llama 4, DeepSeek-R1 y Qwen3.5 en tarjetas NVIDIA nuevas (Blackwell, B200).
- Es completamente de código abierto y su desarrollo está en GitHub.
- Tiene mejoras en compresión de memoria, decodificación especulativa y atención para textos largos.

Suposición: que estas mejoras se noten en una computadora personal común (sin confirmar).

## Cosas útiles
Hechos del material:
- Código bajo licencia Apache 2, gratis para usar y modificar.
- Ejemplos de código reutilizables, incluido uno para ejecutar DeepSeek.
- Modelos ya optimizados y quantizados (FP8, FP4) en Hugging Face de NVIDIA.
- Guías de instalación y de inicio rápido en su documentación.
- Integración con Triton Inference Server y NVIDIA Dynamo para poner modelos en producción.
- Herramientas para medir el rendimiento (benchmarking).

Suposición: que los ejemplos funcionen sin cambios en cualquier equipo (sin confirmar).

## Avisos
Hechos del material:
- Requiere tarjetas gráficas NVIDIA con CUDA y Python (el README menciona CUDA 13.4.1, Python 3.10 y 3.12 como versiones de referencia).
- El software es gratis bajo licencia Apache 2. El material no indica el costo del hardware necesario (sin confirmar).
- La recolección de datos de uso está activada por defecto; se puede desactivar con variables de entorno, un archivo, código Python o una bandera en la línea de comandos.
- Algunas funciones antiguas se eliminan después de tres meses de aviso (política de deprecación).
- El repositorio es muy grande; no es necesario clonarlo todo para usarlo.

Suposición: que funcione en tarjetas gráficas de otras marcas (sin confirmar).

## ¿Sirve para sus proyectos?
No, salvo que ya tengan una tarjeta gráfica NVIDIA y quieran ejecutar modelos propios localmente. No está diseñado para conectarse a APIs externas gratuitas ni para apps web simples sin una GPU propia de NVIDIA.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
