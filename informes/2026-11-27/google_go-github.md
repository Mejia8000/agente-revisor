# google/go-github

_Se leyeron 15,000 de 181,250 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Biblioteca oficial en Go para conectarse y automatizar todas las funciones de la API REST v3 de GitHub.

UTILIDAD: Media.

## Qué es
Es una librería escrita en el lenguaje de programación Go (`golang`) mantenida por Google. Sirve para interactuar mediante código con la plataforma GitHub: gestionar repositorios, leer o crear incidencias (issues), disparar flujos de trabajo (GitHub Actions), procesar eventos web (webhooks), administrar permisos, tokens y gestionar secretos.

## Qué hay nuevo
En la versión actual mostrada (`v93`):
* Soporte para APIs avanzadas de GitHub como Copilot Spaces y tareas de agentes (`AgentTasksService`).
* Gestión de secretos y variables específicas para agentes (`AgentsService`).
* Integración con nuevas funciones de Go (como iteradores introducidos en Go 1.23 mediante métodos `*Iter` para recorrer páginas de resultados automáticamente).
* Compatibilidad estricta con la política de soporte de versiones de Go (requiere la versión mayor actual o la inmediatamente anterior).

## Cosas útiles
* **Ejemplos de código reutilizables:**
  * Creación y autenticación de un cliente básico con token personal:
    ```go
    client, err := github.NewClient(github.WithAuthToken("TU_TOKEN_AQUI"))
    ```
  * Manejo simplificado de paginación e iteradores de resultados:
    ```go
    iter := client.Repositories.ListIter(ctx, "tu-usuario", nil)
    for repo, err := range iter {
        if err != nil { log.Fatal(err) }
        // procesar repo
    }
    ```
  * Validación y procesamiento de Webhooks entrantes mediante `github.ValidatePayload` y `github.ParseWebHook`.
* **Herramientas complementarias mencionadas:**
  * Soporte para autenticación como GitHub App (`jferrl/go-githubauth`).
  * Control y reintento automático de límites de peticiones (`gofri/go-github-ratelimit`).
  * Simulación de respuestas para pruebas unitarias sin tocar la red (`migueleliasweb/go-github-mock`).

## Avisos
* **Requisitos:** Requiere tener instalado Go (versión moderna/reciente) y configurar el proyecto usando módulos de Go (`go.mod`).
* **Límites de uso:** GitHub impone límites de peticiones por hora (*rate limits*) tanto primarios (por volumen) como secundarios (por concurrencia). La librería incluye tipos para detectar estos errores (`RateLimitError`, `AbuseRateLimitError`), pero debes manejarlos en tu código.
* **Licencia:** Distribuido bajo licencia de tipo BSD (permisiva, uso libre comercial y personal).
* **Costos:** La biblioteca es gratuita y de código abierto. La API pública de GitHub es gratis para la mayoría de tareas en repositorios abiertos/personales, pero ciertas funciones empresariales o de Actions pueden implicar costos en tu cuenta de GitHub *(sin confirmar según el plan que tengas)*.
* **Seguridad:** Los clientes autenticados adjuntan el token en las cabeceras de red; la documentación advierte expresamente no compartir la misma instancia de cliente entre distintos usuarios.

## ¿Sirve para sus proyectos?
**Sí**, pero únicamente si desarrollas tus automatizaciones o el backend de tus aplicaciones web en el lenguaje Go. 

* **Para automatizaciones:** Es ideal para crear scripts o bots que revisen código, sincronicen repositorios o ejecuten tareas automáticas basadas en eventos de GitHub.
* **Para proyectos con IA gratis / conectores:** Permite que tus agentes o modelos lean y escriban código, creen "pull requests" o gestionen repositorios en GitHub. 
* **Limitación:** Si tus aplicaciones web y proyectos de IA están desarrollados en Python o JavaScript/TypeScript, esta biblioteca no te servirá y requerirás librerías equivalentes en esos lenguajes.
