# google-deepmind/mujoco

_Se revisaron los cambios: 9 commits, 15 archivos._

EN UNA LÍNEA: El simulador de física MuJoco de Google DeepMind recibió mejoras de velocidad en contactos, matrices y su solver de restricciones.

UTILIDAD: baja

## Qué es
MuJoco es un simulador de física de propósito general para sistemas con muchas articulaciones y contactos. Es un repositorio público de Google DeepMind en GitHub con más de 18 000 estrellas. El código está escrito principalmente en C y C++.

## Qué cambió
Hechos (lo que muestra el material):
- Se optimizó el cálculo de restricciones de contacto con cono elíptico (fricción en contactos).
- Se creó la función mj_effLower para armar la parte triangular inferior de una matriz dispersa (CSR) de la métrica discreta, junto con funciones para calcular su tamaño y memoria temporal.
- Se aceleró la suma escalar incremental en matrices dispersas cuando el factor de escala es cero.
- Se aceleró la factorización de Cholesky densa (mju_cholFactor) y se corrigió un error al factorizar un panel de dos columnas con rango deficiente.
- Se aceleró la factorización de la matriz de inercia dispersa (mj_factorI).
- Se aceleró el solver PGS, incluyendo bloques para contactos elípticos de tamaño 3, 4 y 6.
- Se aceleró el conteo de restricciones de contacto y la rotación del Jacobiano para objetos flexibles (flex).
- Se agregaron pruebas automáticas que comparan las versiones rápidas con versiones de referencia lentas.

Suposiciones (sin confirmar):
- Que estas mejoras reducen el tiempo de ejecución en simulaciones reales, porque el material no muestra mediciones de velocidad.
- Que mj_effLower se usa en todos los casos donde antes se usaba MakeMetricLower.

## Cosas útiles
- Funciones del motor que se pueden reutilizar: mj_effLower, mj_effLowerCap, mj_effLowerScratch, rotateJac3, mju_cholFactor, mj_factorI, solPGS, mju_addToSclSparseInc.
- Ejemplos de código en los archivos de prueba (test) que muestran cómo verificar contactos elípticos, factorización de inercia, Cholesky y el solver PGS.
- Repositorio público en GitHub.

## Avisos
- Es código de bajo nivel en C/C++; no es una herramienta lista para usar desde una aplicación web sin una capa de conexión para otros lenguajes (no se muestra en el material).
- No se indica la licencia, el costo ni los términos de uso en el material revisado (sin confirmar).
- Requiere conocimientos de compilación, gestión de memoria y física de cuerpos rígidos.
- Los cambios son internos del motor; no son una herramienta de IA ni un conector a APIs web.

## ¿Sirve para sus proyectos?
No. Sus proyectos son personales con IA gratis, conectores a APIs, modelos propios, apps web y automatizaciones. MuJoco es un simulador de física en C/C++ orientado a robótica y dinámica, no una herramienta de IA generativa ni de integración web. Solo serviría si un proyecto necesita simulación física realista y puede integrar código C/C++ (sin confirmar si existen conexiones fáciles para web).

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
