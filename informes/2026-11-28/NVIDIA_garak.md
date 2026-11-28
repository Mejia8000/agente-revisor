# NVIDIA/garak

_Se leyeron 15,000 de 92,203 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Garak es una herramienta gratuita de línea de comandos que busca fallos de seguridad en modelos de lenguaje (IA), como inyección de prompts o filtración de datos.
UTILIDAD: alta

## Qué es
- Garak es un escáner de vulnerabilidades para LLM (modelos de lenguaje grandes).
- Es gratuito y de código abierto bajo licencia Apache 2.0.
- Lo desarrolla NVIDIA con la comunidad.
- Prueba fallos como: alucinaciones, fuga de datos, inyección de prompts, información falsa, contenido tóxico y jailbreaks (saltarse reglas del modelo).
- Se compara con herramientas como nmap o Metasploit, pero para IA.
- Soporta muchos modelos: Hugging Face, OpenAI, AWS Bedrock, Replicate, Cohere, Groq, Ollama, modelos locales (llama.cpp/gguf) y cualquier API REST.
- Funciona desde la terminal en Linux, macOS y Windows (hay pruebas automáticas para Windows, aunque el README dice que se desarrolla en Linux y macOS).
- Genera informes en JSONL y HTML.
- Tiene más de 10,000 estrellas en GitHub.
- Versión mostrada en el material: 0.17.2.pre1.
- Estado de desarrollo: Alpha.

## Qué hay nuevo
- Incluye sistema de intervalos de confianza para los resultados.
- Tiene una puntuación llamada TBSA para resumir el riesgo de un informe.
- Soporta modelos NIM de NVIDIA.
- Permite crear pruebas y detectores propios.
- (sin confirmar) Que la versión 0.17.2.pre1 sea estable para uso diario, porque está en estado Alpha.

## Cosas útiles
- Instalación gratuita con `pip install garak`.
- Soporta modelos gratuitos de Hugging Face que se pueden ejecutar en la propia computadora.
- Ejemplos de comandos listos para copiar y usar con OpenAI y Hugging Face.
- Código de ejemplo para escribir tus propias pruebas (probes) y detectores.
- Herramientas gratuitas para analizar informes: `analyze_log`, `count_tokens`, `tbsa` y conversión a informes AVID.
- Modo interactivo para probar modelos sin escribir comandos largos.
- Documentación en docs.garak.ai y garak.readthedocs.io (idioma no confirmado, se asume inglés).

## Avisos
- Requiere Python 3.11 a 3.14.
- Algunos modelos necesitan clave de API (OpenAI, Replicate, Cohere, Groq, Bedrock, NIM). Esas claves pueden tener costo externo (sin confirmar montos).
- El detector de toxicidad Perspective necesita su propia clave de API.
- Algunos detectores necesitan tarjeta gráfica (CUDA) o librerías como `libmagic`.
- El estado es Alpha, puede tener errores (sin confirmar cuáles ni cuán graves).
- No garantiza encontrar todas las vulnerabilidades (sin confirmar).
- Usar modelos comerciales por API puede generar costos aparte de la herramienta (sin confirmar montos).
- Licencia: Apache 2.0.

## ¿Sirve para sus proyectos?
Sí. Sirve para proyectos personales con IA gratis porque permite probar conectores a APIs y modelos propios antes de usarlos en apps web o automatizaciones. Ayuda a verificar que un modelo no filtre datos ni acepte instrucciones maliciosas. La herramienta es gratis, pero si se conecta a modelos de pago por API, esos modelos pueden cobrar por su uso (sin confirmar montos).

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
