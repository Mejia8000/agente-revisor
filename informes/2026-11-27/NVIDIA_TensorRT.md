# NVIDIA/TensorRT

_Se leyeron 15,000 de 287,636 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Kit de herramientas y código abierto de NVIDIA para acelerar y ejecutar modelos de inteligencia artificial al máximo rendimiento en tarjetas gráficas NVIDIA.

UTILIDAD: Media

## Qué es
Es la parte abierta (código fuente de conectores, plugins y ejemplos) de NVIDIA TensorRT, un sistema diseñado para optimizar modelos de redes neuronales (exportados desde entornos como PyTorch u ONNX) y ejecutarlos con la menor latencia y el mayor rendimiento posible en procesadores gráficos (GPU) de NVIDIA.

## Qué hay nuevo
- Publicación de TensorRT 11.X (versión 11.5.0.63 en los archivos del repositorio).
- Se eliminaron sistemas antiguos: ya no se admiten redes con tipos débiles (reemplazadas por redes estrictamente tipadas) ni cuantización implícita (reemplazada por cuantización explícita).
- Se descarta la arquitectura de extensiones `IPluginV2` en favor de `IPluginV3`.
- Se retira la herramienta TREX y se reemplaza por Nsight Deep Learning Designer.
- Fin de soporte para Python 3.9 e inferiores; ahora se requiere Python 3.10 a 3.14.
- Compatibilidad añadida y recomendada para versiones de CUDA 12.9 y 13.5.
- Incorporación de recursos para agentes de código ("Agentic Coding Skills") en el repositorio.

## Cosas útiles
- Instalación rápida del paquete oficial en Python mediante: `pip install tensorrt`.
- Scripts de ejemplo funcionales:
  - En `demo/DeBERTa/`: scripts listos para exportar modelos de Hugging Face a formato ONNX (`deberta_pytorch2onnx.py`), limpiarlos para TensorRT (`deberta_onnx_modify.py`) y medir tiempos de respuesta (`deberta_tensorrt_inference.py`).
  - En `scripts/convert_te_onnx_to_trt_onnx.py`: conversor para adaptar modelos de precisión FP8 hacia el estándar ONNX Opset 19.
- Gestor de memoria para modelos grandes (`Weight Streaming`): permite ejecutar modelos pesados limitando el uso de memoria de la GPU y transmitiendo pesos desde la memoria central.

## Avisos
- Requisito de hardware estricto: Requiere obligatoriamente tarjetas gráficas o dispositivos de NVIDIA (PC, servidores o placas Jetson). No funciona en tarjetas de otras marcas (AMD, Intel) ni en procesadores convencionales (CPU).
- Requisitos de entorno: Necesita controladores compatibles con CUDA (12.9 o 13.5) y cuDNN 8.9.
- Compatibilidad rígida: Los modelos compilados por TensorRT (archivos de motor `.engine`) solo funcionan en la misma tarjeta gráfica y versión exacta con la que fueron generados; no se pueden mover libremente a otras máquinas con hardware diferente.
- Licencia: Código distribuido bajo licencia permisiva Apache 2.0 (gratuita para proyectos personales y comerciales).
- Curva técnica alta: No es una interfaz gráfica ni una aplicación para usuarios finales; requiere programar en C++ o Python y configurar entornos de compilación (como Docker o CMake si se construye desde la fuente).

## ¿Sirve para sus proyectos?
- Conectores a APIs externas: No. Si tus automatizaciones o páginas web llaman a modelos a través de servicios en la nube, TensorRT no interviene en absoluto.
- Modelos propios locales: Sí, pero solo si dispones de una tarjeta gráfica NVIDIA y necesitas exprimir la velocidad de respuesta al máximo. Si no tienes hardware NVIDIA, no te servirá.
- Aplicaciones web y automatizaciones: En general no de forma directa. Solo te serviría si tu propia aplicación web incluye un servidor interno que ejecute la IA localmente en tu propia máquina con GPU. Para flujos web convencionales, su complejidad de configuración suele ser innecesaria frente a soluciones más sencillas (sin confirmar).
