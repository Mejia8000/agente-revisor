# google/guava

_Se revisaron los cambios: 4 commits, 18 archivos._

EN UNA LÍNEA: Google simplificó su librería Guava para Java al usar clases estándar del lenguaje en lugar de copias propias.
UTILIDAD: alta (para proyectos en Java)

## Qué es
Guava es un conjunto de librerías básicas de Google para el lenguaje Java. El repositorio tiene 51,930 estrellas. Incluye código para trabajar con colecciones, mapas, caché y funciones de hash.

## Qué cambió
Hechos del material:
- Se quitaron las copias propias de las clases LongAdder y Striped64 en las versiones para Android (java7) de caché y hash. Ahora usan directamente la clase java.util.concurrent.atomic.LongAdder de Java, igual que la versión normal de Guava.
- Se borraron los archivos LongAdder.java, Striped64.java y LongAddables.java de las carpetas de caché y hash en Android.
- En la clase RegularImmutableMap se cambió la tabla hash: ahora guarda índices de entrada empezando en 1 (el 0 significa que no hay nada). Esto permite tablas de hasta 255 entradas con tipo byte, 65,535 con short y más con int.
- La función Multisets.inferDistinctElements ahora también acepta conjuntos (Set) y devuelve su tamaño; antes solo funcionaba con Multiset y usaba el valor 11 por defecto.
- Se agregó el método isEmpty() a la clase AbstractMapBasedMultiset, tanto en Android como en la versión principal de Guava.
- Se borraron reglas de ProGuard para la clase Striped64 porque esa clase ya no existe.
- Se agregaron pruebas para revisar los límites de las tablas hash con 255, 256, 65,535 y 65,536 entradas.

Suposiciones (sin confirmar):
- Que estos cambios hacen el código más rápido o más fácil de mantener.
- Que la librería sigue funcionando igual en versiones antiguas de Android.

## Cosas útiles
- Guava es gratis y de código abierto (licencia Apache 2.0, visible en los archivos del repositorio).
- La clase java.util.concurrent.atomic.LongAdder de Java, útil para contadores seguros cuando muchos hilos escriben al mismo tiempo.
- Ejemplos de prueba en ImmutableMapTest e ImmutableBiMapTest que se pueden reutilizar para crear mapas inmutables con tamaño esperado.
- El método isEmpty() para multisets.
- Soporte para conjuntos (Set) al calcular cuántos elementos distintos tiene una colección.

## Avisos
- Es solo para Java. Si sus proyectos no usan Java, esta librería no sirve directamente.
- Licencia Apache 2.0: es permisiva, pero si se redistribuye el código hay que incluir los avisos de copyright y licencia.
- No hay costos mencionados porque es software libre.
- Se eliminó un archivo de prueba llamado LongAdderTest; no se sabe si eso deja sin probar alguna función (sin confirmar).
- No hay información sobre compatibilidad con versiones muy antiguas de Android (sin confirmar).

## ¿Sirve para sus proyectos?
Sí, si sus proyectos están en Java. Guava ofrece herramientas gratis para caché, colecciones y hash que pueden ayudar en apps web, conectores a APIs y automatizaciones personales. No, si sus proyectos usan otro lenguaje diferente a Java, porque esta librería es solo para Java.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
