# google/adk-recipes

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: Colección de ejemplos y plantillas de código de Google para crear agentes de inteligencia artificial y automatizaciones.

UTILIDAD: Media

## Qué es
Es un repositorio con guías y ejemplos prácticos (llamados "recetas") basados en el kit de desarrollo de agentes de Google (ADK o *Agent Development Kit*). Enseña cómo armar agentes inteligentes para resolver tareas comunes como búsqueda de información (RAG), control de sesiones de memoria, seguridad y conexiones de autenticación (OAuth).

## Qué hay nuevo
El texto facilitado es la presentación general del repositorio; no detalla una lista de cambios recientes o novedades de una versión específica.

## Cosas útiles
* **Ejemplos prácticos de código:** Plantillas en la carpeta `core/` para aprender a programar memoria en agentes, flujos OAuth, guardarraíles de seguridad y técnicas de RAG.
* **Casos de uso aplicados:** Ejemplos en `contrib/` y `plugins/` como búsqueda de productos comerciales o probadores virtuales.
* **Variedad de lenguajes:** Cuenta con kits de desarrollo (SDKs) para usar el código en Python, TypeScript (JavaScript), Go, Java y Kotlin.

## Avisos
* **Licencia:** Apache 2.0 (permisiva y de código abierto).
* **Costos y servicios:** Varios ejemplos están pensados para desplegarse en plataformas como Cloud Run o Gemini Enterprise; el uso de estos servicios en la nube puede implicar costos asociados.
* **Modelos propios:** El documento no aclara si se pueden conectar modelos locales o totalmente desconectados de Google (*sin confirmar*).
* **Sin soporte oficial:** Google advierte explícitamente que no es un producto con soporte oficial de la empresa y que el código es solo para demostración o como base de inicio, no para usarse en producción final directamente.

## ¿Sirve para sus proyectos?
**Sí**, pero adaptándolo. Sirve como referencia si quieres crear automatizaciones o integrar agentes en aplicaciones web utilizando Python o TypeScript, ya que muestra cómo estructurar la memoria y los conectores. Sin embargo, no está pensado de fábrica para modelos locales propios y muchos componentes se orientan a la nube de Google, por lo que adaptarlo para que funcione únicamente con herramientas o APIs 100% gratis requerirá esfuerzo extra por tu parte (*sin confirmar* la complejidad de desacoplarlo del ecosistema de Google).
