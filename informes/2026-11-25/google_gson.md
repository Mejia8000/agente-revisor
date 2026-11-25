# google/gson

_Se leyeron 15,000 de 59,147 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Gson es una biblioteca gratuita de Java que convierte objetos Java a texto JSON y viceversa.

## Qué es
Hechos:
- Es una biblioteca de Java para serialización y deserialización JSON.
- Convierte objetos Java a JSON y convierte texto JSON a objetos Java.
- Funciona con clases existentes aunque no se tenga el código fuente de esas clases.
- Soporta tipos genéricos de Java, por ejemplo `List<MiClase>`.
- La versión mencionada en las instrucciones de instalación es 2.15.0.
- El repositorio tiene 24 235 estrellas.
- Está bajo la licencia Apache 2.0.
- El README dice que no es un producto oficialmente soportado por Google.
- Está en modo mantenimiento: se corrigen errores existentes, pero es probable que no se añadan funciones grandes nuevas.

## Qué hay nuevo
Hechos:
- La versión 2.15.0 requiere Java 8 como mínimo para usarla.
- Para compilar el proyecto desde el código fuente se necesita JDK 17 o superior (se recomienda JDK 21).
- Para Android, la versión 2.15.0 requiere como mínimo API level 24.

Suposiciones sin confirmar: Qué cambios específicos trae la versión 2.15.0 respecto a versiones anteriores, porque el material no lista novedades detalladas.

## Cosas útiles
Herramientas gratis:
- Dependencia para Gradle: `implementation 'com.google.code.gson:gson:2.15.0'`
- Dependencia para Maven con `groupId com.google.code.gson`, `artifactId gson` y versión `2.15.0`.
- Archivo JAR disponible para descarga en Maven Central.

Ejemplos de código que se pueden reutilizar:
- Crear una instancia: `Gson gson = new Gson();`
- Convertir objeto a JSON: `String json = gson.toJson(objeto);`
- Convertir JSON a objeto: `MiClase obj = gson.fromJson(json, MiClase.class);`
- Usar `GsonBuilder` para opciones personalizadas, como formato bonito, nombres de campos, fechas y excluir campos.
- Clase `RuntimeTypeAdapterFactory` (en la carpeta extras) para manejar objetos que pueden ser de diferentes subtipos.
- Clase `UtcDateTypeAdapter` (en la carpeta extras) para manejar fechas en formato UTC.
- Clases `JsonObject`, `JsonArray` y `JsonParser` para trabajar con JSON como un árbol de datos.
- Clases `JsonReader` y `JsonWriter` para leer y escribir JSON por flujo (streaming).

## Avisos
Requisitos:
- Java 8 o superior para usar Gson 2.15.0.
- JDK 17 o superior para compilar el proyecto desde el código fuente.

Licencia:
- Apache 2.0, que permite uso gratuito, modificación y distribución.

Límites:
- No se recomienda usar en Android porque la reflexión abierta causa problemas con la optimización y ofuscación de aplicaciones (R8/ProGuard). Si se usa en Android, la versión 2.15.0 requiere API level 24 como mínimo.
- No soporta bien características específicas de Kotlin o Scala, como tipos que no pueden ser nulos o constructores con valores predeterminados.
- Las instancias de Gson son seguras para usar en varios hilos al mismo tiempo.

Riesgos:
- Si el JSON está mal formado, lanza excepciones como `JsonSyntaxException` o `JsonIOException`.
- En Android, la ofuscación puede hacer que los campos desaparezcan y provoque errores en tiempo de ejecución.
- El README indica que no es un producto oficialmente soportado por Google.

Modo mantenimiento (sin confirmar que no habrá cambios grandes, pero el README dice que es probable que no se añadan funciones nuevas).

## ¿Sirve para sus proyectos?
- Conector a la API de Gemini en Cloudflare: No. Hecho: Gson es una biblioteca para Java. No hay información en el material sobre Cloudflare ni sobre la API de Gemini. Sin confirmar: que Cloudflare admita ejecutar código Java o que exista una integración directa con Gemini.
- IA propia llamada Musa que entrena en Kaggle: No. Hecho: Gson solo convierte objetos a JSON y viceversa; no entrena modelos de inteligencia artificial ni tiene relación con Kaggle. Sin confirmar: que se use para procesar datos de entrada o salida de Musa.
- Apps web publicadas con GitHub y Cloudflare: No. Hecho: Gson es una biblioteca de backend para aplicaciones Java, no una herramienta para publicar páginas web estáticas ni funciones serverless típicas de GitHub Pages o Cloudflare Pages. Sin confirmar: que se use en un servidor Java separado detrás de esos servicios.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
