# NVIDIA/TensorRT-LLM

_Se revisaron los cambios: 15 commits, 60 archivos._

EN UNA LÍNEA:
Actualización de TensorRT-LLM que mejora los tiempos de espera en streaming, añade limpieza en errores para extensiones de postprocesamiento y optimiza modelos como DeepSeek y MiniMax.

UTILIDAD:
Baja

## Qué es
Es la plataforma de NVIDIA para optimizar y servir modelos de lenguaje (LLM) a máxima velocidad en tarjetas gráficas (GPU) de NVIDIA, mediante entornos de ejecución en Python y C++.

## Qué cambió
- **Limpieza en extensiones de salida (`postprocessor_hook`)**: Se añadió un método opcional llamado `on_request_end(request_id, reason)` para que las funciones personalizadas que procesan el texto generado puedan liberar memoria si una petición falla antes de terminar.
- **Tiempos de espera por inactividad en streaming**: En el cliente HTTP desagregado, las respuestas en tiempo real (streaming) ya no se cortan por un tiempo total fijo; ahora el temporizador vigila únicamente que la conexión no se quede en silencio sin enviar datos durante demasiado tiempo.
- **Aclaración sobre LoRA y CUDA Graphs**: Se documentó y ajustó el parámetro `max_loras`. Por defecto reserva espacio para 8 adaptadores simultáneos en grafos CUDA; si se sobrepasa este límite en ejecución, el lote falla.
- **Reorganización del servidor de red**: Se centralizó la lógica que abre puertos TCP (`_bind_listener`) para los distintos modos de comando (`trtllm-serve`, generación visual, etc.).
- **Optimización en transferencias internas (Attention-DP)**: Se agrupan los envíos de texto de entrada entre procesos en bloques de hasta 4 MiB para reducir demoras de red interna.
- **Ajustes en modelos específicos**: Correcciones en la sincronización de hilos para MiniMax M3 y optimizaciones de comunicación y precarga en memoria L2 para DeepSeek-V4.1 en arquitecturas modernas (como NVIDIA Blackwell).

## Cosas útiles
- **Código reutilizable para ganchos de postprocesamiento**: Si utiliza los hooks de `tensorrt_llm.executor`, puede implementar limpieza de memoria ante fallos:
  ```python
  class MiFiltro:

      def __init__(self):
          self._buffers = {}

      def __call__(self, chunk):
          # procesar texto...
          if chunk.is_final:
              self._buffers.pop(chunk.request_id, None)
          return emit(chunk.text_diff)

      def on_request_end(self, request_id: int, reason: str) -> None:
          # Limpieza si la petición falló antes del final
          self._buffers.pop(request_id, None)
```
- **Ejemplo de configuración de adaptadores LoRA (`config.yaml`)**:
  ```yaml
  lora_config:
    lora_target_modules: ['attn_q', 'attn_k', 'attn_v']
    max_lora_rank: 8
    max_loras: 16 # Ajusta la cantidad máxima de adaptadores en GPU
```

## Avisos
- **Requisitos técnicos**: Exige hardware con GPU NVIDIA compatible y controladores CUDA instalados localmente.
- **Riesgo de fallo en LoRA**: Si activa grafos CUDA y recibe peticiones con más adaptadores LoRA simultáneos que el valor configurado en `max_loras` (8 por defecto), el motor lanzará una excepción y cancelará las peticiones activas.
- **Licencia y costes**: Licencia Apache 2.0 (gratuita), pero requiere infraestructura GPU propia o alquilada (lo que implica costes de hardware altos).

## ¿Sirve para sus proyectos?
No. Sus proyectos están basados en automatizaciones, aplicaciones web y conectores a APIs gratuitas externas o modelos propios ligeros. TensorRT-LLM es un compilador y servidor de inferencia pesado diseñado para infraestructura empresarial con tarjetas gráficas dedicadas de NVIDIA, por lo que añade una complejidad técnica y requerimientos de servidor innecesarios para su caso de uso.
