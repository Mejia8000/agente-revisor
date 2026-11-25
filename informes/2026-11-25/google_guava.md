# google/guava

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: Es una colección de herramientas y componentes esenciales de Google para programar en el lenguaje Java.

## Qué es
Es un paquete de librerías de código para desarrolladores de Java. Ofrece utilidades listas para usar que facilitan tareas comunes: nuevas formas de agrupar datos (colecciones como multimapas), estructuras que no se pueden modificar (inmutables), manejo de grafos matemáticos, herramientas para tareas simultáneas (concurrencia), lectura y escritura de archivos (I/O), cálculo de huellas digitales de datos (hashing) y manipulación de texto y números primitivos. Cuenta con dos variantes: una estándar para computadoras/servidores (JRE) y otra para aplicaciones móviles (Android).

## Qué hay nuevo
* Se indica la versión `33.8.0` (en variantes para JRE y Android) en los ejemplos de instalación.
* Informan que dejaron de publicar versiones preliminares en binario (*snapshots*) en los repositorios centrales de Maven; ahora solo distribuyen versiones finales terminadas, manteniendo únicamente la documentación preliminar disponible en la web.

## Cosas útiles
* **Ejemplos de configuración:** Códigos listos para copiar y pegar en gestores de proyectos Java comunes (Maven y Gradle).
* **Acceso rápido a documentación:** Enlaces directos para consultar el funcionamiento de clases específicas (por ejemplo, `guava.dev/ImmutableList`).
* *(No contiene modelos de inteligencia artificial ni servicios web de consumo directo).*

## Avisos
* **Requisitos:** Para la versión principal se necesita Java (JDK) versión 1.8 o superior. Para la versión móvil, está probado en Android nivel de API 24 en adelante.
* **Funciones inestables (`@Beta`):** Cualquier parte del código marcada como beta puede cambiar o borrarse por completo en cualquier actualización posterior.
* **Riesgo de seguridad:** Los autores aclaran expresamente que sus componentes no están diseñados para filtrar ni defenderse de atacantes maliciosos; no debe usarse como frontera entre código confiable y código no seguro.
* **Persistencia / Guardado:** No se garantiza que los objetos guardados (serializados) puedan ser leídos por versiones futuras de la librería.
* **Compatibilidad de sistema:** Ciertas funciones de lectura/escritura (`com.google.common.io`) podrían no operar bien fuera de sistemas Linux.
* **Dependencias:** Requiere obligatoriamente un componente adicional en ejecución llamado `failureaccess:1.0.3`.
* **Costos y Licencia:** El documento no menciona los términos de licencia ni costos *(sin confirmar: habitualmente las librerías de código abierto de Google son gratuitas)*.

## ¿Sirve para sus proyectos?
**No.** 
Guava es una librería diseñada pura y exclusivamente para aplicaciones escritas en **Java** o Android. Sus proyectos actuales consisten en:
1. Un conector en Cloudflare (normalmente ejecutado en JavaScript o TypeScript).
2. Un modelo de IA (Musa) entrenado en Kaggle (ecosistema típicamente basado en Python).
3. Páginas y aplicaciones web alojadas en GitHub y Cloudflare.

Al no utilizar Java en su infraestructura técnica actual, no puede integrarse directamente en ninguno de sus desarrollos.
