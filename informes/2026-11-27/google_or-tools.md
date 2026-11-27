# google/or-tools

_Se revisaron los cambios: 2 commits, 10 archivos._

EN UNA LÍNEA: Google añadió y actualizó las guías de migración a la versión 10.0-rc.1 para sus herramientas de optimización de rutas y restricciones (CP-SAT).

UTILIDAD: Baja

## Qué es
Google OR-Tools es un conjunto de herramientas de programación gratuitas y de código abierto creado para resolver problemas de optimización matemática y logística (por ejemplo: encontrar la ruta más corta para varios camiones de reparto, planificar horarios de trabajo o resolver problemas con reglas estrictas).

## Qué cambió
Los cambios en esta actualización corresponden a documentación técnica (guías de migración de la versión 9.15 a la versión 10.0-rc.1):
* **Separación del módulo de rutas:** El código de cálculo de rutas ahora está en su propio módulo independiente (`routing`) y se acortaron nombres de clases principales (por ejemplo, `RoutingModel` pasa a ser simplemente `Model`, y `RoutingIndexManager` pasa a ser `IndexManager`).
* **Python modernizado:** En rutas se eliminó la biblioteca interna antigua (SWIG) y se pasó a `pybind11`. Todas las funciones cambiaron de formato de nombres en mayúsculas a formato estándar de Python en minúsculas con guiones bajos (`snake_case`).
* **Avisos de código obsoleto en CP-SAT:** En Python, usar nombres antiguos en mayúsculas (`NewIntVar`, `Solve`, etc.) ahora genera advertencias de código obsoleto (`DeprecationWarning`) de forma predeterminada.
* **Cambios en otros lenguajes:** En C++ se prohíbe duplicar modelos directamente para evitar errores de memoria (se debe usar `.Clone()`), y en Java los datos de CP-SAT ahora se manejan mediante conectores nativos para mayor velocidad.
* **Requisitos más altos del sistema:** Se necesita como mínimo C++20, Java 21, Python entre 3.10 y 3.15 (se retira el soporte a Python 3.9) y .NET 8.0.

## Cosas útiles
* **Ejemplos de código actualizados:** Las guías proporcionan ejemplos completos en Python, C++, Java y C# listos para copiar y adaptar en problemas de rutas con restricciones de tiempo y capacidad.
* **Herramienta gratuita:** El solucionador sigue siendo gratuito y de código abierto bajo la licencia Apache 2.0.

## Avisos
* **Rompe código previo:** Si actualizas la biblioteca a la versión 10, los programas antiguos dejarán de funcionar hasta que se actualicen las importaciones y nombres de funciones.
* **No compatible con versiones viejas de sistemas:** Si tu entorno usa Python 3.9 o Java anterior a la versión 21, no podrás usar esta nueva versión de OR-Tools.
* **No es Inteligencia Artificial generativa:** Es un optimizador de investigación operativa (algoritmos matemáticos y búsqueda de restricciones), no tiene relación con modelos de lenguaje (LLMs) ni redes neuronales.

## ¿Sirve para sus proyectos?
**No** (para la mayoría de tus proyectos actuales).
* **Por qué:** No sirve para conectar APIs de IA ni para entrenar o ejecutar modelos de lenguaje propios. Solo te serviría si en alguna app web o automatización necesitas resolver un problema específico de logística pesada, como calcular la mejor ruta física para entregas o armar calendarios automáticos de turnos de trabajo.
