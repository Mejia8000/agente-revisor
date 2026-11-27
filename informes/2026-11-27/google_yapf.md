# google/yapf

_Se leyeron 15,000 de 24,369 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Es una herramienta gratuita para ordenar y formatear automáticamente el código escrito en lenguaje Python según guías de estilo estándar.

UTILIDAD: Media

## Qué es
Es un formateador de código para Python (originalmente desarrollado bajo la cuenta de Google, aunque aclaran que no es un producto oficial de la empresa). Su función principal es tomar código que está desordenado, mal espaciado o con saltos de línea irregulares, y reescribirlo de forma limpia siguiendo reglas de estilo establecidas (como PEP8, Google o Facebook). Se puede ejecutar desde la terminal del sistema o importarse como biblioteca dentro de un script de Python.

## Qué hay nuevo
* Se encuentra en la versión 0.43.0.
* El documento detalla que aún no soporta características recientes introducidas en Python 3.12 (específicamente la sintaxis de tipos de PEP 695 y el formato avanzado de f-strings de PEP 701).
* *(Sin confirmar)*: No se proporciona el registro de cambios (changelog) completo en el texto para saber qué ajustes específicos se hicieron entre la 0.42 y la 0.43.0.

## Cosas útiles
* **Herramienta gratuita y abierta:** Se puede instalar y usar sin costo mediante comandos habituales de Python (`pip install yapf`).
* **Uso directo en código propio (API de Python):** Permite formatear cadenas de texto o archivos completos desde un script usando funciones listas para copiar:
  ```python
  from yapf.yapflib.yapf_api import FormatCode

  # Formatea una cadena de texto con código Python
  codigo_limpio, cambiado = FormatCode("def funcion( a,b ): return a+b")
  print(codigo_limpio)
  # Resultado: def funcion(a, b):\n    return a + b
  ```
* **Uso por línea de comandos (Terminal):** Puedes formatear archivos directamente en tu disco sin abrir un editor:
  * `yapf -i archivo.py` (reescribe y arregla el archivo en su lugar).
  * `yapf -d archivo.py` (muestra los cambios necesarios en formato "diff" sin alterar el archivo).
* **Integración con Git:** Incluye soporte y scripts para integrarse con `pre-commit`, lo que permite revisar y ordenar el código automáticamente antes de guardar cambios en un repositorio.

## Avisos
* **Requisitos:** Requiere tener instalado Python versión 3.7 o superior.
* **Licencia y Costos:** Es gratuito bajo la licencia Apache 2.0 (permite uso personal y comercial).
* **Límites:** El proyecto sigue indicando que está en etapa de desarrollo "beta".
* **Riesgos estéticos:** El documento advierte que en estructuras de datos muy grandes o diccionarios complejos, el formateador automático puede producir un resultado visualmente incómodo. Para esos casos, se debe pausar manualmente la herramienta agregando el comentario `# yapf: disable` en el código.

## ¿Sirve para sus proyectos?
**Sí (como herramienta de soporte).** 
No genera modelos de inteligencia artificial, no procesa llamadas a APIs por sí mismo ni construye aplicaciones web. Sin embargo, si programas tus automatizaciones, conectores de IA o aplicaciones web utilizando el lenguaje Python, esta herramienta te sirve para mantener todo tu código limpio, legible y con un formato profesional de manera automática.
