# NVIDIA/Megatron-LM

_Se revisaron los cambios: 2 commits, 7 archivos._

EN UNA LÍNEA: Correcciones internas en Megatron-LM para evitar bloqueos entre tarjetas gráficas y errores de memoria al generar texto rápido en grandes servidores.
UTILIDAD: baja

## Qué es
Megatron-LM es un sistema de código abierto desarrollado por NVIDIA para entrenar y ejecutar modelos de lenguaje gigantescos repartidos entre muchas tarjetas gráficas (GPUs) de alto rendimiento.

## Qué cambió
- **Corrección en la memoria de generación rápida (MTP):** Al reorganizar solicitudes activas de forma asíncrona, el sistema ahora usa un mapa de índices para asegurarse de que cada petición lea exactamente sus propios datos y tokens anteriores, evitando que se mezclen datos de usuarios o tareas distintas.
- **Evitar bloqueos en modelos MoE (Mezcla de Expertos):** En la inferencia paralela, las operaciones de comunicación entre tarjetas gráficas se dejaron en el canal principal (*main stream* de CUDA) para evitar que las GPUs se queden colgadas esperando datos de las demás. Solo el cálculo matemático pesado se envía al canal secundario.
- **Nuevas pruebas:** Se agregaron pruebas internas automatizadas para asegurar que ambas correcciones funcionen correctamente en entornos de múltiples GPUs.

## Cosas útiles
- No hay modelos descargables gratuitos ni APIs listas para consumir en esta actualización.
- El código modificado es interno del motor (escrito en Python y PyTorch para CUDA), por lo que no aporta plantillas reutilizables para aplicaciones cotidianas.

## Avisos
- **Requisitos extremos:** Exige infraestructura de servidor con múltiples tarjetas gráficas NVIDIA potentes conectadas entre sí (generalmente configuraciones empresariales).
- **Costos:** Ejecutar o probar este software requiere infraestructura de nube o servidores físicos de costo muy elevado.
- **Licencia:** Megatron-LM suele distribuirse bajo licencia abierta de tipo Apache 2.0 *(sin confirmar en este extracto)*.
- **Dificultad:** Es software de nivel de investigación y optimización de bajo nivel de hardware, no apto para desarrollo web estándar.

## ¿Sirve para sus proyectos?
No. No sirve para proyectos personales con IA gratis, automatizaciones ni aplicaciones web. Megatron-LM está diseñado para centros de datos y clústeres gigantescos de tarjetas gráficas. Para conectar APIs o correr modelos locales en proyectos pequeños o páginas web, herramientas como Ollama o conectores directos a APIs en la nube son las opciones adecuadas.
