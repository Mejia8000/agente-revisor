# google/osv-scanner

_Se leyeron 15,000 de 47,286 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Herramienta de seguridad que detecta y ayuda a corregir vulnerabilidades en las librerías de tus proyectos y contenedores usando la base de datos pública OSV.dev.

UTILIDAD: Media

## Qué es
Es un programa de línea de comandos desarrollado en Go por Google. Su función principal es revisar los archivos donde declaras tus librerías (como `package.json` en Node.js o `requirements.txt` en Python) o imágenes de Docker, contrastarlos contra la base de datos abierta OSV.dev y avisarte si alguna librería tiene fallos de seguridad conocidos. 

## Qué hay nuevo
Según el código y la documentación de la versión 2 (v2.7.1 beta):
- **Servidor MCP experimental (`osv-scanner experimental-mcp`):** Permite comunicarse con sistemas de inteligencia artificial usando el protocolo abierto MCP (a través de entrada estándar o servidor web SSE).
- **Corrección guiada experimental (`fix` y `update`):** Sugiere y aplica actualizaciones de versiones directamente en tus manifiestos y archivos de bloqueo para resolver fallos.
- **Escaneo de contenedores Docker:** Analiza imágenes capa por capa detectando fallos en paquetes del sistema (Alpine, Debian, Ubuntu) y dependencias de lenguajes.
- **Análisis de licencias:** Permite verificar qué licencias de software usan tus librerías y detectar violaciones respecto a una lista permitida.
- **Análisis de uso real de código:** Puede verificar en Go y Rust si tu código realmente llama a la función vulnerable, reduciendo alertas falsas.

## Cosas útiles
- **Conector MCP para IA:** Incluye herramientas listas para agentes inteligentes (`scan_vulnerable_dependencies`, `get_vulnerability_details`, `ignore_vulnerability`) que un modelo de IA puede invocar.
- **APIs públicas y gratuitas:** Funciona conectándose a OSV.dev y deps.dev sin requerir pagos ni claves obligatorias iniciales.
- **Modo sin internet:** Permite descargar las bases de datos para realizar escaneos locales sin conexión (`--offline --download-offline-databases`).
- **Comandos reutilizables:**
  - Escanear una carpeta: `osv-scanner scan source -r /ruta/a/tu/proyecto`
  - Escanear una imagen de Docker: `osv-scanner scan image nombre-imagen:tag`
  - Revisar licencias permitidas: `osv-scanner --licenses="MIT,Apache-2.0" /ruta/a/tu/proyecto`
  - Levantar servidor MCP para agentes de IA: `osv-scanner experimental-mcp --sse localhost:8080`

## Avisos
- **Requisitos:** Requiere descargar el archivo ejecutable compilado, o tener instalado Go para compilarlo, o Docker para correr su contenedor oficial. Para análisis profundo en Go o Rust, requiere tener instaladas las herramientas de dichos lenguajes.
- **Licencia:** Código bajo licencia Apache-2.0 (libre y permisiva).
- **Riesgo en comando `fix`:** El propio repositorio advierte que usar la corrección automática (`fix`) en código de terceros no confiable es riesgoso, ya que puede desencadenar la ejecución de scripts del gestor de paquetes.
- **Privacidad y red:** En su modo habitual envía nombres y versiones de paquetes a servicios externos (OSV.dev y deps.dev), aunque no transmite tu código fuente propio.
- **Límites de las APIs:** Si bien las consultas a OSV.dev y deps.dev son gratuitas, los límites específicos de peticiones por minuto están *sin confirmar* en los archivos provistos.

## ¿Sirve para sus proyectos?
Sí.
- **Para apps web y automatizaciones:** Es muy útil para agregarlo a tus flujos de trabajo y verificar periódicamente que tus dependencias de Python, JavaScript u otros lenguajes no tengan vulnerabilidades críticas ni problemas de licencias.
- **Para proyectos personales con IA:** Gracias a su comando `experimental-mcp`, puedes conectar tus modelos o asistentes de IA directamente a esta herramienta para que analicen la seguridad de proyectos de forma autónoma.
- **Aclaración:** No genera texto ni crea aplicaciones web por sí mismo; es exclusivamente una utilidad de diagnóstico y mantenimiento de seguridad.
