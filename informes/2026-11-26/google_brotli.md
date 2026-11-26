# google/brotli

_Se leyeron 15,000 de 72,584 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Brotli es una librería gratuita de compresión sin pérdida creada por Google que hace archivos más pequeños usando LZ77, codificación de Huffman y modelado de contexto.
UTILIDAD: alta

## Qué es
Hechos:
- Es un algoritmo de compresión sin pérdida de propósito general.
- Combina una variante moderna de LZ77, codificación de Huffman y modelado de contexto de segundo orden.
- Su especificación está definida en el estándar RFC 7932.
- Es código abierto bajo la licencia MIT.
- El repositorio tiene 15,165 estrellas.
- La versión de la librería es 1.2.0.
- Está escrito principalmente en C y tiene bindings para Python, JavaScript, C#, Haxe y Dart.
- Se puede instalar en Linux con `apt install brotli` y en MacOS con `brew install brotli`.
- El módulo de Python se instala con `pip install brotli`.
- No guarda información extra como checksums ni el tamaño de los datos descomprimidos (es un formato de "stream").

Suposiciones:
- Se usa comúnmente para comprimir páginas web en servidores HTTP (sin confirmar).

## Qué hay nuevo
Hechos:
- El material no incluye un registro de cambios ni menciona novedades recientes más allá de la versión 1.2.0.

## Cosas útiles
Hechos:
- Código fuente en C bajo licencia MIT.
- Bindings para Python (`pip install brotli`).
- Decodificador en JavaScript para usar en navegadores o Node.js (`js/decode.js`, `js/cli.js`).
- Ejemplos de código en C para comprimir y descomprimir datos (`c/dec/`, `c/enc/`).
- Herramienta de línea de comandos en C para descomprimir (`research/brotli_decoder.c`).
- Herramientas para crear diccionarios personalizados (`research/dictionary_generator.cc`, `research/durchschlag.cc`, `research/sieve.cc`).
- Diccionario estático incluido con palabras comunes para mejorar la compresión de textos pequeños.

Suposiciones:
- Los ejemplos de código se pueden copiar y reutilizar en otros proyectos sin cambios importantes (sin confirmar).

## Avisos
Hechos:
- Licencia MIT: gratuita y permisiva.
- Para compilar desde código fuente se necesitan herramientas como CMake, Bazel o vcpkg.
- El módulo de Python requiere Python 3.10 o versiones más recientes.
- El formato no incluye checksums ni longitud de datos descomprimidos, así que no detecta si alguien modifica partes del archivo comprimido.
- No es una herramienta de inteligencia artificial ni se conecta a APIs de IA.

Suposiciones:
- Puede ser necesario adaptar el código de ejemplo para usarlo en proyectos propios (sin confirmar).

## ¿Sirve para sus proyectos?
Sí, para apps web y automatizaciones; no para IA directamente.
Por qué:
- Sirve para apps web porque Brotli es un formato estándar de compresión usado para reducir el tamaño de datos transferidos por internet.
- Sirve para automatizaciones porque permite comprimir y descomprimir archivos con código reutilizable en C, Python y JavaScript.
- No sirve directamente para proyectos de IA gratis, conectores a APIs de IA o modelos propios, porque no es una librería de IA ni tiene funciones de conexión a servicios de inteligencia artificial.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
