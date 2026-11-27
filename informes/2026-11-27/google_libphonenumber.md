# google/libphonenumber

_Se revisaron los cambios: 5 commits, 9 archivos._

EN UNA LÍNEA: Google actualizó su librería para leer, escribir y validar números de teléfono de otros países en Java, C++ y JavaScript, corrigiendo errores y mejorando la detección de números con letras.
UTILIDAD: alta

## Qué es
Hechos: Es una librería de Google escrita en Java, C++ y JavaScript. Sirve para analizar, formatear y validar números de teléfono internacionales. El repositorio tiene 18 368 estrellas.

## Qué cambió
Hechos:
- Se corrigió un error en Java y C++: cuando el código de país no se encontraba en el texto del teléfono, el programa usaba un índice incorrecto. Ahora revisa primero si lo encontró.
- En C++, se corrigió el formato de la extensión del teléfono (por ejemplo, "ext=1234") al usar el estándar RFC3966, para que coincida con la versión de Java.
- Se cambió la detección de números que usan letras en lugar de dígitos (como "800 FLOWERS"). Antes usaba una expresión regular compleja; ahora cuenta las letras directamente y rechaza textos muy largos (más de 250 caracteres).
- Se agregó un enlace en el archivo README a una versión para Salesforce llamada NumberForge.
- Se agregaron pruebas para verificar que los cambios funcionan.

Suposiciones (sin confirmar): que estos cambios corrigen problemas que ocurrían en uso real.

## Cosas útiles
- Librería pública de Google para Java, C++ y JavaScript.
- El README lista versiones para otros lenguajes: Dart, Delphi, Elixir, R y Salesforce (NumberForge).
- Ejemplos de código en las pruebas: cómo detectar números con letras y cómo formatear una extensión con ";ext=".

## Avisos
Hechos:
- El material solo muestra cambios en las versiones de C++ y Java; no se detalla qué cambió en JavaScript.
- Hay un nuevo límite de 250 caracteres para detectar números con letras en C++ y Java.
- El material no muestra la licencia, los costos ni los requisitos de instalación.

Suposiciones (sin confirmar): que la librería es gratuita y que funciona en aplicaciones web.

## ¿Sirve para sus proyectos?
Sí. Sirve para apps web y automatizaciones que necesiten validar o formatear números de teléfono de varios países. También puede ayudar a limpiar datos de teléfonos antes de usarlos con modelos de IA o conectores a APIs, aunque el material no menciona inteligencia artificial.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
