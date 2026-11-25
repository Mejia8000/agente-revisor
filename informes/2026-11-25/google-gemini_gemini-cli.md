# google-gemini/gemini-cli

_Se leyeron 15,000 de 772,373 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Un asistente de inteligencia artificial para la terminal que ayuda a programar, pensado principalmente para empresas con licencias de Gemini Code Assist en Google Cloud.

## Qué es
Es una aplicación para la línea de comandos (terminal) programada en Node.js y TypeScript. Funciona como un agente interactivo que puede leer el código de tus proyectos, editar archivos, proponer planes de desarrollo, correr comandos y conectarse a herramientas externas (servidores MCP).

## Qué hay nuevo
- **Cambio de enfoque:** El proyecto aclara que ya no cuenta con acceso gratuito para cuentas individuales ni planes personales comunes (Google AI Pro/Ultra), los cuales fueron trasladados a una herramienta llamada *Antigravity CLI*.
- **Uso empresarial prioritario:** Queda mantenido principalmente para clientes con licencias de *Gemini Code Assist* (Standard/Enterprise) y proyectos en Google Cloud, además de cuentas con clave de API de pago o Vertex AI.
- **Limitación de modelos:** Se advierte que no está optimizado para los modelos de la serie *Gemini 4* (como Gemini 4 Argon) ni para medir el rendimiento de los modelos (benchmarks).
- **Herramientas añadidas en el código:** Se prueban y gestionan funciones como el modo de planificación antes de actuar (`plan_mode`), subagentes especializados, memoria persistente de sesión (`auto_memory`) y un sistema de control de tareas (`task tracker`).

## Cosas útiles
- **Ejemplo reutilizable de llamadas a la API:** El archivo `scripts/send_gemini_request.sh` contiene un ejemplo claro en Bash de cómo enviar peticiones HTTP usando `curl` al endpoint REST de Gemini (`https://generativelanguage.googleapis.com/v1beta/models/...`) tanto en modo normal (`generateContent`) como en streaming (`streamGenerateContent`).
- **Modo para scripts y automatización:** Permite pedir respuestas en formato estructurado JSON sin interfaz gráfica usando el comando:
  `gemini -p "tu instrucción" --output-format json`
- **Modelos y APIs:** Permite configurar manualmente modelos existentes como `gemini-2.5-flash` usando el parámetro `-m` junto con la variable `GEMINI_API_KEY`.
- **Integraciones:** Se puede conectar con herramientas externas mediante el protocolo MCP para tareas como generación de imágenes/video (Imagen, Veo) o integración con GitHub.

## Avisos
- **Licencia:** Apache 2.0 (código abierto, permisiva).
- **Costos:** No tiene capa gratuita para usuarios comunes en esta herramienta. Requiere pagar por uso mediante clave de API de Google AI Studio, Vertex AI o contar con una licencia corporativa de *Gemini Code Assist*.
- **Requisitos del sistema:** Requiere Node.js / npm. Para entornos aislados y seguros (sandboxing), requiere herramientas como Docker, Podman o perfiles de seguridad del sistema operativo.
- **Riesgos:** Al ser un agente con capacidad de modificar archivos y ejecutar comandos en la máquina, puede alterar código de manera destructiva si no se revisa antes de aceptar los cambios.

## ¿Sirve para sus proyectos?
- **Conector a la API de Gemini en Cloudflare:** **No**. Esta herramienta está construida para correr en la terminal de un computador o servidor con Node.js y componentes binarios nativos, por lo que no puede ejecutarse dentro del entorno restringido de Cloudflare Workers. *(Nota útil: el script `send_gemini_request.sh` sí te sirve como guía de cómo hacer la llamada HTTP directa).*
- **IA propia llamada Musa que entrena en Kaggle:** **No**. Esta herramienta no sirve para entrenar modelos de machine learning, pesos ni redes neuronales propias; es solo una interfaz de usuario y automatización para interactuar con los modelos comerciales de Google Gemini.
- **Apps web publicadas con GitHub y Cloudflare:** **No**. No es una librería pensada para formar parte del código de una página web ni para ser usada por tus usuarios finales en el navegador. Solo te serviría de forma externa en tu propia computadora de trabajo como ayudante para escribir o corregir el código *(sin confirmar, ya que esto depende de si posees una clave de API de pago o licencia compatible)*.
