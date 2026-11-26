# NVIDIA/Megatron-LM

_Se leyeron 15,000 de 900,584 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Megatron-LM es una biblioteca de NVIDIA para entrenar modelos de lenguaje grandes en muchas GPUs a la vez.
UTILIDAD: baja

## Qué es
Hechos:
- Es un repositorio de código abierto de NVIDIA con 18,539 estrellas en GitHub.
- Tiene dos partes: Megatron-LM (ejemplos y scripts listos para entrenar) y Megatron Core (biblioteca de piezas para construir sistemas de entrenamiento propios).
- Está optimizado para GPUs NVIDIA y divide el modelo entre varias tarjetas usando paralelismo de tensor, pipeline, datos, expertos y contexto.
- Soporta precisión mixta FP16, BF16, FP8 y FP4.
- Incluye scripts para entrenar modelos GPT, híbridos, visión-lenguaje (LLaVA) y aprendizaje por refuerzo.
- Tiene una herramienta llamada Megatron Bridge para convertir modelos entre Hugging Face y Megatron.
- Licencia: Apache 2.0.
- Requiere Python 3.12 o superior y PyTorch 2.6.0 o superior.

## Qué hay nuevo
Hechos (según el archivo README del repositorio):
- Versión 0.19.0 de Megatron Core con modelos híbridos, mejor balanceo de routers MoE, envío de secuencias empaquetadas y descarga de activaciones compatible con CUDA Graphs.
- Soporte inicial para DeepSeek-V4 en la rama de desarrollo.
- Resultados de rendimiento publicados para modelos como DeepSeek-V3 y Qwen3 en sistemas con 256 GPUs.
- Se menciona que Megatron Bridge se unirá al repositorio principal (con fecha 2026/11 en el documento).

## Cosas útiles
Hechos:
- Código de ejemplo para entrenar un modelo GPT pequeño en un ciclo sencillo: examples/run_simple_mcore_train_loop.py.
- Scripts de entrenamiento listos para modelos BERT, GPT-3, LLaMA, GPT-OSS, Mamba y series financieras.
- Herramientas para preparar datos de texto (tools/preprocess_data.py) y crear cachés de datasets (tools/prepare_cache.py).
- Ejemplos de servidores de generación de texto (tools/run_text_generation_server.py y examples/inference/).
- Se puede instalar gratis desde PyPI con: uv pip install megatron-core
- Hay documentación oficial enlazada desde el repositorio.

## Avisos
Hechos:
- Está hecho para entrenamiento a gran escala en clusters con muchas GPUs NVIDIA (los benchmarks usan 256 GPUs).
- No es una herramienta ligera para un solo ordenador personal.
- Requiere conocimientos avanzados de entrenamiento distribuido y configuración de GPUs.
- Algunas noticias del README tienen fechas de 2026; no se puede confirmar si son reales o planes futuros sin revisar el repositorio en vivo.
- Megatron Bridge está en un repositorio separado (NVIDIA-NeMo/Megatron-Bridge); su licencia y disponibilidad no se confirman en este material.

Suposiciones (sin confirmar):
- Que se puede ejecutar en una GPU de consumo común.
- Que todos los ejemplos funcionan sin ajustes en cualquier equipo.

## ¿Sirve para sus proyectos?
No. Sus proyectos son personales, con IA gratis, conectores a APIs, modelos propios, apps web y automatizaciones. Esta biblioteca está diseñada para entrenar modelos enormes en clusters de muchas GPUs NVIDIA, no para proyectos personales ligeros ni para crear apps web sencillas. Aunque tiene ejemplos de inferencia, su enfoque principal es el entrenamiento distribuido a gran escala, lo que requiere hardware costoso y conocimientos avanzados.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
