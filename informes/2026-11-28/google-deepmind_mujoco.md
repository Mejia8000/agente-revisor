# google-deepmind/mujoco

_Se revisaron los cambios: 3 commits, 31 archivos._

EN UNA LÍNEA: MuJoCo agregó soporte para cámaras con proyección fisheye y distorsión de lente, y corrigió la búsqueda de archivos de mallas en modelos incluidos.

UTILIDAD: media

## Qué es
Hecho: MuJoCo es un simulador de física de propósito general para sistemas con muchas articulaciones y contacto.
Hecho: Pertenece al repositorio google-deepmind/mujoco y tiene 18,543 estrellas.
Hecho: Permite definir cámaras dentro de los modelos de simulación.

## Qué cambió
Hecho: Se agregó la proyección de cámara "fisheye" (modelo Kannala-Brandt), además de las ya existentes "perspective" y "orthographic".
Hecho: Se agregó el atributo "distortion" para cámaras, que acepta hasta 8 coeficientes de distorsión de lente.
Hecho: Se corrigió un error para que los archivos "flexcomp" se busquen en la carpeta de mallas (meshdir) al incluir modelos desde otros archivos.
Hecho: Se actualizaron la documentación, los esquemas XML, el código fuente en C, Python, C# (Unity), WebAssembly y las pruebas automáticas.
Suposición: Que estos cambios ya están publicados y listos para usar: sin confirmar.

## Cosas útiles
Hecho: La API de Python incluye las constantes mjNDISTCOEF, cam_distortion y mjtProjection (con el nuevo valor mjPROJ_FISHEYE).
Hecho: Los bindings para C# (Unity) y WebAssembly ya incluyen el campo cam_distortion y el tipo mjPROJ_FISHEYE.
Hecho: Las pruebas de código muestran cómo leer y escribir cámaras con distorsión y proyección fisheye desde archivos XML.
Hecho: El esquema XML ahora acepta el atributo distortion en el elemento camera, con hasta 8 valores numéricos.
Suposición: Que esos ejemplos de prueba se pueden copiar y reutilizar en otros proyectos: sin confirmar.

## Avisos
Hecho: La distorsión de lente es ignorada por el renderizador clásico OpenGL y por los sensores de cámara.
Hecho: No se puede adjuntar un sensor de distancia (rangefinder) ni un sensor de proyección de cámara (camprojection) a una cámara fisheye; da error al compilar.
Hecho: La distorsión no está permitida en cámaras con proyección ortográfica.
Hecho: Se recomienda especificar el tamaño del sensor (sensorsize) junto con la distancia focal (focal o focalpixel) para cámaras fisheye.
Suposición: Que se requiere obligatoriamente la versión mujoco >= 4.0.2: sin confirmar (el código solo tiene una nota pendiente sobre esto).
Suposición: Que el software es gratuito y su licencia permite uso personal: sin confirmar (el material no menciona licencia ni costos).
Suposición: Que los bindings de WebAssembly permiten usar MuJoCo directamente en apps web: sin confirmar.

## ¿Sirve para sus proyectos?
No.
Por qué: Sus proyectos se centran en inteligencia artificial gratis, conectores a APIs, modelos propios, apps web y automatizaciones. MuJoCo es un simulador de física, no una herramienta de inteligencia artificial ni un conector a APIs. Aunque tiene bindings para Python, C# y WebAssembly, el material no muestra ejemplos de uso en apps web ni automatizaciones, y sus nuevas funciones (cámaras fisheye y distorsión de lente) son específicas de simulación visual, no de inteligencia artificial.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
