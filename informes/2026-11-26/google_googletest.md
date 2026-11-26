# google/googletest

_Se leyeron 15,000 de 95,726 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: GoogleTest es un framework gratuito de pruebas unitarias y mock para código C++.
UTILIDAD: baja

## Qué es
Hechos (lo que muestra el material):
- Es un framework de pruebas para el lenguaje de programación C++.
- Combina GoogleTest y GoogleMock, dos herramientas que antes estaban separadas.
- Permite escribir pruebas unitarias que se ejecutan solas.
- Incluye GoogleMock para crear "mocks", que son imitaciones de funciones o clases para probar el código de forma aislada.
- Se usa en proyectos conocidos como Chromium, LLVM, Protocol Buffers y OpenCV.
- La versión 1.18.0 requiere como mínimo el estándar C++17.
- Tiene documentación en línea gratuita en GitHub Pages.

Suposiciones: ninguna.

## Qué hay nuevo
Hechos:
- Está disponible la versión 1.18.0.
- La rama 1.18.x requiere al menos C++17.
- La documentación oficial ahora está en GitHub Pages y se recomienda usarla en lugar de leer el repositorio directamente.
- Se planea agregar una dependencia a la librería Abseil (sin confirmar si ya se agregó).

## Cosas útiles
Hechos:
- El código es gratuito y de código abierto (se ven licencias tipo BSD en los archivos).
- Incluye macros y funciones listas para usar en C++, como EXPECT_CALL, ON_CALL y MOCK_METHOD.
- Tiene matchers (comparadores) y acciones predefinidas para valores, textos, contenedores y excepciones.
- Soporta correr pruebas en paralelo para que terminen más rápido.
- Se puede compilar con CMake o Bazel.
- Hay extensiones gratuitas para Visual Studio Code (GoogleTest Adapter y C++ TestMate) para ver y ejecutar pruebas.
- Existen herramientas relacionadas gratuitas como GTest Runner, GoogleTest UI y gtest-parallel.

## Avisos
Hechos:
- Solo sirve para proyectos en lenguaje C++. No es para Python, JavaScript ni otros lenguajes.
- Requiere instalar un compilador de C++ (como GCC o Clang) y herramientas como CMake o Bazel.
- La versión 1.18.x exige C++17 o superior.
- Los archivos de integración continua muestran pruebas en Linux y macOS, principalmente con contenedores Docker.
- La licencia es BSD: permite uso gratuito, pero obliga a conservar los avisos de copyright al compartir el código.
- No incluye conectores a servicios de inteligencia artificial ni funciones para crear apps web.

Suposiciones:
- Puede ser difícil de usar si no se conoce bien C++ (sin confirmar).
- Algunas funciones avanzadas de mocks y plantillas pueden requerir experiencia en C++ (sin confirmar).

## ¿Sirve para sus proyectos?
No. GoogleTest está hecho para probar código escrito en C++. No está diseñado para conectores a APIs de IA, modelos propios, apps web ni automatizaciones generales. Solo le serviría si sus proyectos personales incluyen código C++ que quiera probar automáticamente.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
