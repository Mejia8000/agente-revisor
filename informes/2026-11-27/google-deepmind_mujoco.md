# google-deepmind/mujoco

_Se revisaron los cambios: 18 commits, 61 archivos._

EN UNA LÍNEA: Actualización del simulador físico MuJoCo que acelera cálculos matemáticos y corrige fallos en la detección de contactos con objetos deformables.

UTILIDAD: Baja

## Qué es
Es un simulador de física creado por Google DeepMind, utilizado principalmente para robótica, biomecánica y entrenamiento de inteligencia artificial orientada al movimiento físico (aprendizaje por refuerzo).

## Qué cambió
* **Resolución matemática más rápida:** Se aceleraron las operaciones con matrices grandes y dispersas y se cambió el algoritmo numérico (usando factorización Cholesky directa en el modo "Newton") para resolver modelos deformables más rápido y sin advertencias falsas de inestabilidad.
* **Corrección en colisiones 2D:** Se arregló un problema donde las colisiones entre formas de cápsula y mallas flexibles 2D (como telas) fallaban o generaban errores matemáticos (valores "NaN" o no válidos).
* **Detección de choques acelerada:** Se optimizó el descarte inicial de colisiones (fase amplia) mediante algoritmos de ordenamiento más rápidos (*radix sort*) y pruebas mejoradas de cajas delimitadoras.
* **Tratamiento de errores en gráficos:** En el renderizador (Filament), pasar configuraciones o datos inválidos ahora genera advertencias (*warnings*) en vez de provocar cierres o errores críticos directos.

## Cosas útiles
* El motor es completamente gratuito y de código abierto.
* Dispone de librerías para Python y C/C++ muy optimizadas para cálculo físico y simulación de articulaciones o robots.
* *(Nota: No incluye APIs de lenguaje, modelos LLM ni componentes para páginas web).*

## Avisos
* **Licencia:** Apache 2.0 (gratuito, código abierto para uso personal y comercial).
* **Compatibilidad:** Los modelos de simulación existentes que dependían del contacto entre cápsulas y telas 2D pueden cambiar ligeramente de comportamiento tras las correcciones.
* **Requisitos:** Requiere entornos de desarrollo con C/C++ o Python; si se usa aceleración masiva en tarjeta gráfica (MuJoCo Warp), requiere hardware compatible (sin confirmar si aplica solo a tarjetas NVIDIA).

## ¿Sirve para sus proyectos?
No. 
Sus proyectos se centran en aplicaciones web, automatizaciones y conectores de IA gratuita (como modelos de lenguaje o procesamiento de texto). MuJoCo está diseñado únicamente para simulación de físicas y movimientos mecánicos complejos, por lo que no aporta funcionalidad a sistemas web ni a flujos de trabajo automatizados.
