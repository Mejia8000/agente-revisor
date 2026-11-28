# google/benchmark

_Se leyeron 15,000 de 25,125 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Una herramienta para medir con alta precisión cuánto tiempo y memoria tardan en ejecutarse funciones o algoritmos pequeños en C++, Python y Rust.

UTILIDAD: Baja

## Qué es
Es una biblioteca creada por Google para hacer "microbenchmarking" (pruebas de rendimiento de código muy pequeño, de forma parecida a las pruebas unitarias). Permite calcular tiempos de CPU, tiempos reales, uso de memoria, análisis de complejidad matemática (Big-O) y exportar los resultados a formatos como texto o JSON. Aunque su base está en C++, incluye adaptadores para usarse desde Python y Rust.

## Qué hay nuevo
* El repositorio muestra la versión 1.10.0 en sus conectores de Rust y Python.
* Incluye compatibilidad en Python para ejecuciones sin GIL (Free-threading / Python 3.14t y 3.15t) mediante `nanobind`.
* *(Al no incluirse un registro de cambios o versiones anteriores en los archivos analizados, no se pueden verificar otras novedades frente a versiones pasadas; sin confirmar).*

## Cosas útiles
* **Adaptador para Python (`google_benchmark`):** Permite medir funciones de Python fácilmente usando el decorador `@benchmark.register`.
* **Herramienta de comparación (`tools/compare.py`):** Un script en Python que compara dos archivos de resultados y realiza pruebas estadísticas (test U de Mann-Whitney) para determinar si un cambio en el código realmente lo hizo más rápido o más lento.
* **Ejemplos de código listos:** Archivos como `example.py` muestran cómo pausar el cronómetro para excluir preparaciones, medir memoria o configurar argumentos de prueba.

## Avisos
* **Licencia y costo:** Es gratuito y de código abierto bajo la licencia Apache-2.0.
* **Requisitos:** Para compilar la librería base se requiere un compilador compatible con C++17, CMake y Git. Para usar el paquete de Python se requiere Python 3.10 o superior.
* **Límites y riesgos:** El rendimiento del procesador (como el ahorro de energía o escalado de frecuencia de la CPU) y la seguridad del sistema operativo (ASLR) pueden alterar las mediciones y generar variaciones falsas.

## ¿Sirve para sus proyectos?
**No.** 
Tus proyectos se enfocan en aplicaciones web, automatizaciones e integraciones con APIs de inteligencia artificial. Esta herramienta está diseñada para optimización de algoritmos de bajo nivel (a nivel de microsegundos o nanosegundos). Medir llamadas a APIs externas o flujos web no requiere esta clase de librerías y agregaría complejidad técnica innecesaria.
