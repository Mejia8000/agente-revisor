# google/langextract

_Se revisaron los cambios: 2 commits, 3 archivos._

EN UNA LÍNEA: Librería de Python para extraer datos ordenados a partir de texto con IA, que ahora maneja mejor los errores y formatos en tareas por lotes de Gemini.

UTILIDAD: Media

## Qué es
Es una herramienta en Python desarrollada por Google (`langextract`) pensada para leer textos largos o desorganizados y extraer información estructurada (como datos en formato JSON o tablas) usando modelos de inteligencia artificial, indicando de qué parte del texto original salió cada dato.

## Qué cambió
En esta actualización se arreglaron dos detalles al trabajar en modo por lotes (*batch*, procesar muchos textos a la vez) con la IA Gemini:
1. **Control de formato personalizado:** Ahora el sistema acepta y envía correctamente las configuraciones de formato y esquemas JSON que defina el usuario (`response_schema`, `response_json_schema`, `response_mime_type`).
2. **Mejor control de errores:** Si el archivo de resultados por lotes contiene una línea dañada o que no sea un objeto JSON válido, la herramienta avisa del fallo sin mostrar el texto del documento en el mensaje de error (evitando exponer datos privados) y permite ignorar el fallo si así se configuró.

## Cosas útiles
* **Código reutilizable para esquemas:** En los archivos de prueba se muestra cómo enviar un esquema JSON a Gemini para obligar al modelo a responder con una estructura de datos exacta.
* **Integración con Gemini:** La librería permite conectarse a los modelos de lenguaje de Google.

## Avisos
* **Requisitos:** Requiere programar en Python y tener instaladas librerías de conexión con Google (como `google-genai`).
* **Costos y límites:** El código modificado interactúa con servicios de Google Cloud (Vertex AI y almacenamiento en Cloud Storage). Aunque la API estándar de Gemini ofrece niveles gratuitos (*sin confirmar* si este modo exacto por lotes entra en la cuota gratuita), el uso en Google Cloud generalmente requiere registrar una cuenta y puede generar costos si se superan los límites de prueba.
* **Licencia:** Es un proyecto público en GitHub de Google, pero la licencia exacta no se especifica en el texto provisto (*sin confirmar*).

## ¿Sirve para sus proyectos?
Sí. Es muy útil si creas automatizaciones o aplicaciones web donde recibes textos sin formato (correos, mensajes, documentos) y necesitas que una IA extraiga datos clave organizados en JSON para guardarlos en una base de datos. Además, al soportar la API de Gemini, facilita hacer pruebas aprovechando las opciones de acceso que ofrece Google.
