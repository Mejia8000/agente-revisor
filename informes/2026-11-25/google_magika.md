# google/magika

_Se leyeron 15,000 de 62,223 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Magika es una herramienta gratuita de código abierto que usa inteligencia artificial para detectar el tipo de contenido de archivos.

## Qué es
- Magika identifica el tipo de contenido de un archivo (por ejemplo, PDF, imagen, código Python).
- Es del repositorio google/magika en GitHub y tiene 18 863 estrellas.
- Usa un modelo de IA de pocos megabytes que responde en milisegundos, incluso en un solo CPU.
- Fue entrenado con unos 100 millones de archivos en más de 200 tipos de contenido.
- Tiene una precisión promedio de aproximadamente 99 % en sus pruebas internas.
- Google lo usa en Gmail, Drive y Safe Browsing para enviar archivos a escáneres de seguridad.
- Está integrado con VirusTotal y abuse.ch.
- Se puede usar como herramienta de línea de comandos, paquete de Python, y tiene bindings para JavaScript/TypeScript, Go y Rust.
- Hay una demo web que funciona en el navegador sin instalar nada.
- Licencia: Apache 2.0.
- El README advierte que no es un proyecto oficial de Google y que Google no da garantías sobre su calidad.

## Qué hay nuevo
- La versión 2.0 está en etapa de candidato a release (2.0.0rc0), no es la versión final estable.
- El núcleo está reescrito en Rust y pesa unas 5 veces menos en disco.
- Soporta más de 400 tipos de contenido (antes eran 216).
- Tiene aceleración con GPU en macOS (Metal) y en Rust con CUDA.
- Puede analizar muchos archivos al mismo tiempo en paralelo.
- Soporta más plataformas, incluyendo Alpine Linux.
- Se planea superar los 1000 tipos de contenido y lanzar un modelo más pequeño y rápido (sin confirmar fecha).

## Cosas útiles
- Modelo activo: standard_v3_3.
- Herramientas gratis: CLI de Magika, paquete Python (`pip install magika`), paquete JavaScript (`npm install magika`), bindings de Rust y Go.
- Ejemplo de código Python: `from magika import Magika; m = Magika(); res = m.identify_bytes(b'function log(msg) {console.log(msg);}')`.
- Ejemplo de línea de comandos: `magika archivo` o `magika -r carpeta/`.
- Salida en formato JSON para integrar con otros programas.
- Demo web gratuita: https://securityresearch.google/magika/demo/magika-demo/
- Código completo en GitHub bajo licencia Apache 2.0.

## Avisos
- Licencia: Apache 2.0 (gratuito y de código abierto).
- Requisitos: Python 3.8 o superior para el paquete de Python; Rust para compilar desde código fuente; el binding de Go necesita cgo y ONNX Runtime.
- La versión actual es 2.0.0rc0, un candidato a release, no una versión final estable.
- El binding de JavaScript no usa los resolutores de formato nativos de Rust, solo heurísticas básicas y el modelo de IA.
- Magika solo lee una parte limitada del archivo (inicio y final), no el archivo completo.
- Puede equivocarse en la detección; tiene modos de confianza (alta, media, mejor intento).
- No es un proyecto oficial de Google y no tiene soporte oficial ni garantías.

## ¿Sirve para sus proyectos?
- Conector a la API de Gemini en Cloudflare: Sí, probablemente. Tiene binding de JavaScript que corre en el navegador y en Node, y se puede usar para detectar el tipo de archivo antes de enviarlo a Gemini. Sin confirmar que funcione en Cloudflare Workers.
- IA propia llamada Musa que entrena en Kaggle: No directamente. Magika detecta tipos de archivo, no entrena modelos de IA. Podría servir para clasificar archivos de entrenamiento, pero eso no está confirmado en el material.
- Apps web publicadas con GitHub y Cloudflare: Sí. Tiene binding de JavaScript para el navegador y una demo web que corre localmente, por lo que se puede integrar en apps web y publicar en GitHub y Cloudflare. Sin confirmar detalles de despliegue en Cloudflare Pages o Workers.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
