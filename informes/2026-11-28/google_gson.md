# google/gson

_Se revisaron los cambios: 5 commits, 10 archivos._

EN UNA LÍNEA: Biblioteca de Java para convertir objetos de código a texto en formato JSON y viceversa, con mejoras recientes en fechas, números grandes y colas de prioridad.
UTILIDAD: Baja

## Qué es
Es una herramienta para programadores que usan el lenguaje Java. Su función es tomar datos u objetos dentro de un programa y transformarlos al formato de texto JSON (muy usado en internet para enviar información), así como hacer el proceso inverso: recibir texto JSON y reconstruir los datos dentro de Java.

## Qué cambió
En las últimas 5 actualizaciones se incluyeron los siguientes cambios:
* **Soporte para colas de prioridad:** Se añadió una nueva pieza opcional (`PriorityQueueTypeAdapterFactory`) para guardar y leer colecciones de tipo `PriorityQueue` en su orden natural.
* **Manejo de números gigantes:** Ahora `JsonTreeWriter` permite procesar números enteros y decimales extremadamente grandes (`BigInteger` y `BigDecimal`) sin dar error de número infinito por equivocación.
* **Validación de fechas corregida:** Se ajustó la lectura de fechas en formato estándar (ISO 8601) para rechazar textos que traigan caracteres de sobra o zonas horarias incorrectas después de la letra 'Z'.
* **Lectura de texto mejorada:** Se reorganizó internamente cómo se lee o se ignora el texto JSON, controlando mejor los caracteres especiales de texto (Unicode) cuando se usa la validación estricta.
* **Aclaración en documentación:** Se detalló en el código fuente en qué situaciones exactas se produce el error de formato `JsonSyntaxException`.

## Cosas útiles
* **Adaptador para colas:** Si programas en Java, puedes registrar la nueva clase de colas de prioridad usando: `new GsonBuilder().registerTypeAdapterFactory(new PriorityQueueTypeAdapterFactory()).create()`.
* **Disponibilidad:** Es software libre y gratuito. *(Sin confirmar: no incluye modelos de inteligencia artificial, conectores de red ni APIs web listas para usar, ya que solo procesa datos locales).*

## Avisos
* **Requisitos:** Solo funciona dentro del lenguaje de programación Java.
* **Licencia:** Apache 2.0 (código abierto, gratuita y de uso comercial permitido).
* **Costos:** Cero costos directos.
* **Límites y riesgos:** 
  * La nueva función para `PriorityQueue` no admite reglas de orden personalizadas (*comparators*); si tu cola tiene una regla personalizada, el programa lanzará un error.
  * Si activas el modo estricto (`STRICT`), los textos con caracteres Unicode incompletos o mal formados ahora fallarán de inmediato.
  * La clase interna de fechas (`ISO8601Utils`) quedó marcada como desaconsejada (*deprecated*); se sugiere usar las herramientas de fecha modernas de Java (`java.time`).

## ¿Sirve para sus proyectos?
**No.** 
Tus proyectos están enfocados en inteligencia artificial gratis (conectores a APIs, modelos locales), aplicaciones web y automatizaciones. Gson es un componente exclusivo para el lenguaje Java y solo sirve para convertir texto JSON. A menos que decidas construir tus automatizaciones o el servidor web específicamente en Java, no te servirá; en proyectos típicos de IA y automatización (que suelen construirse en Python o JavaScript) se utilizan las funciones de JSON que ya vienen incluidas en esos lenguajes sin necesidad de esta librería.
