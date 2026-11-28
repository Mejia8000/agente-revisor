# NVIDIA/cutlass

_Se leyeron 15,000 de 2,335,003 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: CUTLASS es una biblioteca gratuita de NVIDIA para crear programas muy rápidos de multiplicación de matrices en tarjetas gráficas NVIDIA usando CUDA.

UTILIDAD: baja

## Qué es
- Es una colección de herramientas de código abierto (licencia BSD-3-Clause) creada por NVIDIA.
- Sirve para programar kernels de CUDA, que son funciones que se ejecutan en la tarjeta gráfica para hacer álgebra lineal, especialmente multiplicación de matrices (GEMM).
- Funciona en tarjetas NVIDIA desde la arquitectura Volta hasta Blackwell.
- Tiene una parte en C++ (plantillas) y una parte en Python llamada CuTe DSL.
- Es una biblioteca "header-only" para C++, lo que significa que se incluye directamente en otros proyectos sin necesidad de compilarla por separado.

## Qué hay nuevo
- La versión del README es 4.9.0, fechada en noviembre de 2026.
- Agrega soporte para la arquitectura Rubin de NVIDIA, enfocada en kernels de baja latencia y operaciones FP6.
- CuTe DSL (la versión en Python) ahora permite usar ciertas funciones sin activar una opción especial.
- Agrega ejemplos nuevos para GEMM distribuido con JAX y NCCL4Py.
- Mejora la velocidad de importación en Python (unos 25% más rápido).
- Corrige errores en descriptores TMA y en algunas operaciones empaquetadas.
- Según el README, CuTe DSL dejará de ser versión beta a finales del verano de 2026 (sin confirmar si se cumplirá esta fecha).

## Cosas útiles
- Ejemplos de código listos para reutilizar en C++ y Python para multiplicación de matrices y convoluciones en GPU.
- CuTe DSL: permite escribir kernels CUDA en Python sin necesidad de saber C++ avanzado.
- cutlass_profiler: herramienta gratuita para medir y probar el rendimiento de los kernels.
- Ejemplos en cuadernos de Jupyter para GEMM agrupada (usada en modelos de lenguaje tipo MoE) y sincronización entre kernels.
- Licencia gratuita (BSD-3-Clause).

## Avisos
- Requiere una tarjeta gráfica NVIDIA con soporte CUDA (no sirve en tarjetas de otras marcas ni solo en CPU).
- Requiere instalar CUDA Toolkit (versión mínima 11.4, recomendada 12.8).
- La parte en C++ requiere un compilador que soporte C++17.
- Algunas funciones nuevas solo funcionan en tarjetas recientes (Hopper, Blackwell, Rubin).
- Hay errores conocidos: algunas instrucciones FP8 empaquetadas pueden generar resultados incorrectos debido a un error en CUDA Toolkit.
- CuTe DSL está en versión beta pública, por lo que puede cambiar en el futuro.
- No es una biblioteca de modelos de IA lista para usar; es para personas que programan sus propios kernels de GPU.
- No tiene costo de licencia, pero se necesita hardware NVIDIA.

## ¿Sirve para sus proyectos?
No. Porque:
- Sus proyectos son de IA gratis con conectores a APIs, modelos propios, apps web y automatizaciones.
- CUTLASS es de bajo nivel y está enfocado en escribir kernels para tarjetas NVIDIA, no en conectar APIs de IA ni en desarrollar aplicaciones web.
- Requiere conocimientos de CUDA, C++ o Python avanzado para kernels de GPU, y disponer de una tarjeta NVIDIA.
- No está diseñado para automatizaciones sencillas ni para desarrollo web tradicional.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
