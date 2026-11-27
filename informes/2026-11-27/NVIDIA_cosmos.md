# NVIDIA/cosmos

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: NVIDIA Cosmos es una plataforma abierta de modelos de IA para entender y simular el mundo físico, enfocada en robots y vehículos autónomos.

UTILIDAD: media

## Qué es
Hechos:
- Es un repositorio de NVIDIA con 12 476 estrellas.
- Es una plataforma abierta con modelos base, conjuntos de datos y herramientas para crear IA física (robots, autos autónomos, infraestructura inteligente, manufactura, salud y agricultura).
- La versión actual es Cosmos 3, una familia de modelos "omnimodales" que trabajan con texto, imagen, audio y acción.
- Tiene dos partes: Reasoner (entrada de texto y visión, salida de texto) y Generator (entrada de texto, visión, audio y acción; salida de visión, audio y acción).
- Hay tres modelos base: Super (64B), Nano (16B) y Edge (4B), pensados para distintos equipos NVIDIA.
- Existen versiones FP8 que ocupan menos espacio de almacenamiento.
- Hay modelos de ejemplo ya ajustados para conducción, robótica, texto a imagen e imagen a video.
- Incluye un libro de recetas (cookbook) con instrucciones para ejecutar agentes.
- Se puede probar en el navegador sin instalar nada en build.nvidia.com.
- Se puede servir con una API compatible con OpenAI usando vLLM, vLLM-Omni o NIM.
- El código y los modelos están bajo la licencia OpenMDW-1.1.

Suposiciones:
- Que se pueda usar en hardware que no sea de NVIDIA: sin confirmar.
- Que la prueba en el navegador sea gratuita sin límites: sin confirmar.

## Qué hay nuevo
Hechos (según el material):
- Octubre de 2026: ejemplo de simulación interactiva del mundo con checkpoints y recetas de entrenamiento.
- Julio de 2026: se liberó Cosmos3-Edge, un modelo de 4B para uso en tiempo real en Jetson AGX Orin, Thor y RTX Pro 6000.
- Mayo de 2026: se liberó Cosmos 3 con colección en Hugging Face y reporte técnico.

Suposiciones:
- Ninguna adicional.

## Cosas útiles
Hechos:
- Modelos disponibles: Cosmos3-Super (64B), Cosmos3-Nano (16B), Cosmos3-Edge (4B) y versiones FP8.
- Checkpoints de ejemplo para simulación de autos, políticas de robots, texto a imagen e imagen a video.
- Código de ejemplo en Python para generar un video con diffusers y Cosmos3OmniPipeline.
- Recetas para inferencia, entrenamiento adicional (SFT, LoRA, distilación) y evaluación de modelos.
- Herramientas relacionadas: Cosmos Framework (entrenamiento), Cosmos Curator (datos) y Cosmos Evaluator (pruebas).
- Backends soportados: Diffusers, Transformers, vLLM, vLLM-Omni, SGLang, TensorRT-LLM y NIM.
- API compatible con OpenAI para servir los modelos.
- Guardrails de seguridad activados por defecto.

Suposiciones:
- Que todos los modelos y herramientas sean gratuitos para uso personal: sin confirmar.
- Que el código de ejemplo funcione en cualquier computadora: sin confirmar (requiere GPU CUDA y descarga de 16B).

## Avisos
Hechos:
- Se necesita solicitar acceso a un repositorio protegido en Hugging Face (nvidia/Cosmos-1.0-Guardrail) y usar un token de lectura.
- La primera ejecución descarga un checkpoint de 16B y los pasos de cálculo son exigentes.
- Para correr localmente se necesita hardware NVIDIA potente (por ejemplo H200, B200, RTX Pro 6000, H100 o Jetson AGX Orin, según el modelo).
- Licencia: OpenMDW-1.1 para código y modelos; hay una licencia personalizada por correo cosmos-license@nvidia.com.
- El proyecto puede descargar software de terceros de código abierto; hay que revisar esas licencias antes de usarlo.
- Limitaciones conocidas: puede generar errores en videos largos, alta resolución o escenas físicamente complejas (inconsistencia en el tiempo, objetos que se transforman, dinámicas poco realistas).
- Para aplicaciones críticas de seguridad se necesita validación adicional y análisis de seguridad del sistema.
- Los guardrails vienen activados por defecto.

Suposiciones:
- Que el uso en build.nvidia.com tenga algún costo: sin confirmar.
- Que la licencia OpenMDW-1.1 permita uso comercial sin restricciones: sin confirmar.

## ¿Sirve para sus proyectos?
No. Para proyectos personales con IA gratis, conectores a APIs, modelos propios, apps web y automatizaciones, este material no es práctico si no se tiene una GPU NVIDIA potente, porque los modelos son grandes (hasta 64B) y requieren hardware especializado. Aunque se puede probar en el navegador y servir una API compatible con OpenAI, eso depende de contar con infraestructura propia y revisar la licencia, por lo que no se ajusta bien a proyectos personales gratuitos sin ese hardware.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
