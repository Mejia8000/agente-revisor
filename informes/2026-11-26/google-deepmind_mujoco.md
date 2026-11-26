# google-deepmind/mujoco

_Se leyeron 15,000 de 516,943 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: MuJoCo es un simulador de física gratuito de Google DeepMind para robótica y movimiento, con versión para Python y navegador.
UTILIDAD: media

## Qué es
Hechos del material:
- MuJoCo significa Multi-Joint dynamics with Contact.
- Es un motor de física de propósito general.
- Está mantenido por Google DeepMind.
- Tiene 18 502 estrellas en GitHub.
- Sirve para simular robots, biomecánica, gráficos, animación y machine learning.
- Tiene una API en lenguaje C.
- Incluye visualización interactiva en escritorio y en navegadores web.
- Tiene enlaces para Python y un plugin para Unity.
- La versión del código es 4.0.2.
- El código fuente tiene licencia Apache 2.0.
- Los documentos, imágenes y videos de la carpeta doc tienen licencia CC BY 4.0.
- El README dice que no es un producto oficialmente soportado de Google.
- Hay lanzamientos versionados aproximadamente la primera semana de cada mes.
- Funciona en Linux, Windows y macOS.
- Se puede probar en el navegador sin instalar nada en mujoco.org y live.mujoco.org.

## Qué hay nuevo
Hechos:
- El material muestra la versión 4.0.2.
- El README dice que lanzan versiones aproximadamente la primera semana de cada mes.
Suposición:
- Sin confirmar qué cambios específicos trae la versión 4.0.2, porque el material no incluye el changelog detallado.

## Cosas útiles
- Enlaces de Python: se instalan con el comando `pip install mujoco` (requiere Python 3.11 o superior).
- Tutoriales en Google Colab: introducción, edición de modelos, rollout, LQR y mínimos cuadrados.
- MuJoCo Playground: entrenamiento de políticas de robots con GPU, teleoperación, identificación de sistema y despliegue sim-to-real en PyTorch.
- MuJoCo XLA (MJX): para flujos de trabajo con JAX.
- MuJoCo Menagerie: colección de modelos de robots listos para usar.
- Ejemplos de código en C++: simulador básico, compilador de modelos y renderizado.
- Aplicación MuJoCo Studio y visor `simulate`.
- Enlaces para JavaScript/WebAssembly, C#/Unity, MATLAB, Swift, Java, Julia y Rust.
- Convertidores de modelos desde OpenSim, SDFormat, OBJ y Onshape.

## Avisos
- Requiere Python 3.11 o superior para los enlaces de Python.
- La dependencia principal de Python es numpy. Para rendering se necesita opcionalmente glfw y pyopengl.
- Compilar desde el código fuente en la rama principal puede ser inestable (sin confirmar para versiones estables, pero el README lo advierte).
- El código fuente está bajo licencia Apache 2.0; los documentos bajo CC BY 4.0.
- No es un producto oficialmente soportado de Google.
- La versión en navegador (WebAssembly) es más lenta que la versión nativa en C.
- Es un simulador de física, no una plataforma de IA generativa ni un conector de APIs listo para usar sin trabajo adicional.

## ¿Sirve para sus proyectos?
Sí, con límites. Esta evaluación es una suposición sin confirmar porque el material no describe sus proyectos específicos.
- Para proyectos personales con IA gratis y modelos propios: sí, porque tiene enlaces de Python gratuitos, tutoriales en Colab y MuJoCo Playground para entrenar políticas de robots.
- Para automatizaciones: sí, se puede controlar con Python.
- Para conectores de APIs: no directamente, hay que programar la integración.
- Para apps web: limitado. Tiene soporte WebAssembly y enlaces de JavaScript, pero el material no muestra ejemplos listos para integrar en una aplicación web típica, y la versión en navegador es más lenta que la nativa.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
