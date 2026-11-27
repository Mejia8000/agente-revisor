# google-gemini/cookbook

_Se revisaron los cambios: 3 commits, 7 archivos._

EN UNA LÍNEA: Correcciones menores de sintaxis y texto en las guías oficiales para conectar con la API de Gemini mediante JavaScript, comandos REST y Python.

UTILIDAD: Media

## Qué es
Es el repositorio oficial de Google ("Gemini Cookbook") que contiene recetas, tutoriales y código de ejemplo para aprender a integrar y usar los modelos de inteligencia artificial Gemini en distintas aplicaciones y lenguajes.

## Qué cambió
- **Corrección de caracteres en JavaScript:** Se arreglaron símbolos dañados (comillas y guiones largos que se leían mal por un error de codificación de texto) en las guías de inicio rápido de JavaScript (`Audio.js`, `Counting_Tokens.js`, `File_API.js`).
- **Arreglo en llamadas REST (comandos de terminal):** En los cuadernos de audio, video y modelos por REST, se corrigió el formato de los envíos de datos (JSON) para que usen comillas dobles válidas y se encerraron las direcciones web (URLs) entre comillas al usar `curl`.
- **Versión de la librería en Python:** En el cuaderno para generar historias animadas en video, se fijó que se instale obligatoriamente la versión 2.9.0 o superior del paquete oficial (`google-genai>=2.9.0`).

## Cosas útiles
- **Comandos REST corregidos:** Muestran la forma exacta de estructurar llamadas directas (vía `curl`) para consultar listas de modelos (aparece mencionado `gemini-3.1-pro-preview`) y subir archivos de audio o video a la API sin librerías externas.
- **Línea de instalación limpia:** El comando `%pip install -U -q "google-genai>=2.9.0"` listo para copiar si trabajas con cuadernos de Python.
- **Guías en JavaScript:** Muestras de código para medir consumo de texto (contar tokens) y manejar archivos multimedia.

## Avisos
- **Requisitos:** Necesitas tener una clave de acceso (`GEMINI_API_KEY`) generada en Google AI Studio para probar los ejemplos.
- **Costos y límites:** La API de Gemini ofrece un nivel de uso gratuito con límites de peticiones por minuto; si te pasas, empezará a cobrar o bloqueará peticiones (*sin confirmar* los límites exactos de cuota actuales dentro de este cambio).
- **Licencia:** El texto no especifica la licencia de este repositorio (*sin confirmar* si es Apache 2.0 u otra habitual de Google).
- **Riesgo técnico:** Si usas peticiones directas (REST/curl) en tus sistemas, enviar JSON con comillas simples provocará errores de comunicación; debes usar comillas dobles bien escapadas como enseña el parche.

## ¿Sirve para sus proyectos?
Sí. Es muy útil si estás creando conectores para hablar con la API de Gemini en tus aplicaciones web o automatizaciones. Te permite ver la forma correcta de enviar audios, videos y textos usando el plan gratuito de Google, y los arreglos de este cambio evitan errores típicos al copiar y pegar código para tus peticiones HTTP o scripts en JavaScript.
