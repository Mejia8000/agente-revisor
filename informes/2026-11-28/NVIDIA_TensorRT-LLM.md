# NVIDIA/TensorRT-LLM

_Se revisaron los cambios: 8 commits, 111 archivos._

EN UNA LÍNEA: Sistema de aceleración de modelos de NVIDIA que ahora compila código en paralelo y mejora el soporte para modelos con imágenes y texto.

UTILIDAD: Baja

## Qué es
TensorRT-LLM es un programa especializado de NVIDIA para hacer que los modelos de inteligencia artificial (modelos de lenguaje) funcionen mucho más rápido en sus tarjetas gráficas (GPU). Sirve para montar servidores propios de IA de alto rendimiento.

## Qué cambió
* **Compilación más rápida en paralelo:** Al iniciar, el sistema ahora puede compilar funciones internas de la tarjeta gráfica (llamadas *kernels*) usando procesos secundarios en paralelo y compartiendo los archivos generados en una carpeta temporal (`/tmp`), evitando repetir trabajo en el mismo equipo.
* **Aceleración para modelos multimodales:** Se activó el uso de gráficos CUDA (optimizaciones directas en la GPU) para acelerar la lectura inicial de peticiones en modelos que procesan texto junto con imágenes o vídeo (como Qwen-VL, Gemma multimodal o Cosmos).
* **Compatibilidad con Anthropic mejorada:** En la función de servidor web, si un texto es demasiado largo para el modelo, el sistema ahora avisa con un error de inmediato antes de intentar transmitir la respuesta, imitando la respuesta oficial de la API de Anthropic.
* **Seguridad en la configuración:** Se corrigieron los comandos de inicio del servidor para que no alteren los datos o diccionarios de configuración originales del usuario.
* **Actualización interna:** Se actualizaron versiones de librerías secundarias del proyecto (como herramientas para procesar XML y bloquear archivos).

## Cosas útiles
* **Compatibilidad de servidor:** Incluye un servidor web integrado (`trtllm-serve`) capaz de responder imitando el formato de las APIs de OpenAI y Anthropic (`/v1/messages`).
* No incluye modelos nuevos listos para usar ni acceso a APIs gratuitas.

## Avisos
* **Requisitos de hardware estrictos:** Requiere tarjetas gráficas NVIDIA potentes y modernas. Muchas de las mejoras recientes van dirigidas a arquitecturas de gama alta o centros de datos (como Hopper o Blackwell).
* **Requisitos de memoria:** La nueva compilación en procesos secundarios solo se activa si la tarjeta gráfica tiene al menos 8 GB de memoria de vídeo (VRAM) libre.
* **Licencia y costos:** El código es libre (Apache-2.0), pero ponerlo en marcha requiere hardware costoso o pagar alquiler de servidores con GPU en la nube.
* **Complejidad:** La instalación y configuración son avanzadas y no funciona en ordenadores convencionales sin tarjeta gráfica NVIDIA dedicada.

## ¿Sirve para sus proyectos?
**No.** 
Para proyectos personales basados en conectores a APIs gratuitas, aplicaciones web estándar o automatizaciones ligeras, esta herramienta es excesivamente compleja e innecesaria. Solo tendría utilidad si contaras con un servidor propio equipado con tarjetas gráficas NVIDIA de alta gama para alojar tus propios modelos locales.
