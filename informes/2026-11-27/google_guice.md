# google/guice

_Se leyeron 15,000 de 115,040 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Guice es un framework gratuito de Google para administrar dependencias en aplicaciones Java 11 o superior.
UTILIDAD: baja

## Qué es
Hechos:
- Guice es un framework ligero de inyección de dependencias para Java 11 y versiones superiores.
- Fue creado por Google y está disponible en el repositorio google/guice.
- Tiene 12 736 estrellas en GitHub.
- Su licencia es Apache 2.0, que permite uso gratuito, incluso comercial.
- Se distribuye a través de Maven Central y se puede agregar con Maven, Gradle u otros sistemas de construcción.
- Las versiones disponibles incluyen la 6.0.0 y la 7.0.0. La versión 6.0.0 soporta paquetes javax y mayormente jakarta; la 7.0.0 soporta paquetes jakarta.
- Incluye clases principales como Guice, Injector, Module, AbstractModule, Binder, Binding, Key, Provider, Inject y Singleton.
- Permite vincular interfaces con sus implementaciones, crear instancias únicas (singleton), inyectar dependencias en constructores, campos y métodos, y usar módulos para organizar la configuración.
- Incluye una herramienta llamada OsgiWrapper para generar metadatos OSGi en archivos JAR.
- Tiene extensiones opcionales como servlet, persist, jmx, jndi, spring, testlib y otras.

Suposiciones:
- Ninguna en esta sección.

## Qué hay nuevo
Hechos:
- El material menciona dos versiones recientes: 6.0.0 y 7.0.0.
- La diferencia principal entre ellas es el soporte de javax (versión 6) o jakarta (versión 7).
- Existe un archivo que lista cambios de API por extensión (core, assistedinject, dagger-adapter, grapher, jmx, jndi, persist, servlet, spring, structs2, testlib, throwingproviders).

Suposiciones:
- Que haya novedades importantes más allá de lo listado: sin confirmar.

## Cosas útiles
Hechos:
- Código fuente completo y gratuito bajo licencia Apache 2.0.
- Ejemplos de código reutilizables en archivos como AbstractModule.java, Binder.java y Guice.java.
- Ejemplo de módulo:
  ```java
  public class MiModulo extends AbstractModule {
    protected void configure() {
      bind(Servicio.class).to(ServicioImpl.class).in(Singleton.class);
    }
  }
  ```
- Ejemplo de creación de inyector:
  ```java
  Injector inyector = Guice.createInjector(new MiModulo());
  Servicio servicio = inyector.getInstance(Servicio.class);
  ```
- Herramienta OsgiWrapper para envolver JAR con metadatos OSGi.
- Extensiones listas para usar: servlet (para aplicaciones web Java), persist (para persistencia), testlib (para pruebas), entre otras.

Suposiciones:
- Que los ejemplos de código funcionen sin cambios en otros proyectos: sin confirmar.

## Avisos
Hechos:
- Requiere Java 11 o superior.
- Solo funciona con el lenguaje de programación Java.
- La licencia es Apache 2.0.
- Algunas funciones, como la interceptación de métodos, requieren que la generación de bytecode esté habilitada.
- El material indica que el lenguaje de bindings (EDSL) es difícil de aprender solo leyendo la documentación de métodos.
- No se mencionan costos; al ser de código abierto, no hay costo de licencia.

Suposiciones:
- Que no haya costos ocultos de uso: sin confirmar.
- Que sirva para aplicaciones web modernas sin configuración extra: sin confirmar.

## ¿Sirve para sus proyectos?
No.
Por qué: Sus proyectos son de inteligencia artificial gratis (conectores a APIs, modelos propios), apps web y automatizaciones. Guice es un framework para organizar código en Java; no incluye modelos de IA, ni conectores a APIs de IA, ni herramientas para crear apps web o automatizaciones por sí solo. Solo sería útil si ya están desarrollando en Java y necesitan administrar dependencias dentro de su propia aplicación.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
