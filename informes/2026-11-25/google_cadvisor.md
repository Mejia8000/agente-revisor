# google/cadvisor

_Se leyeron 15,000 de 55,737 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA:
Herramienta para Linux que mide en tiempo real el consumo de memoria, procesador, disco y red de contenedores en ejecución.

## Qué es
* Es un programa en segundo plano (daemon) desarrollado en Go que analiza el uso de recursos y rendimiento de contenedores (como Docker, Podman o containerd) y de la máquina que los aloja.
* Muestra los datos a través de una interfaz web integrada (por defecto en el puerto 8080), una API REST y una ruta de métricas para Prometheus (`/metrics`).
* Puede exportar las estadísticas a diferentes bases de datos y sistemas externos como InfluxDB, Elasticsearch, Kafka, Redis, BigQuery, StatsD o salida estándar (stdout).

## Qué hay nuevo
* El repositorio incluye cambios y archivos fechados en 2024 y 2025 (como nuevos scripts de arranque `entrypoint.sh`, comprobación de estado `healthcheck.sh` y modularización interna de plugins).
* No se incluye un archivo de historial de versiones (CHANGELOG) en el material provisto, por lo que no es posible confirmar detalles de novedades frente a versiones previas.

## Cosas útiles
* **Imagen oficial de Docker lista para usar:** Se puede ejecutar directamente mediante el comando mostrado en la documentación:
  ```bash
  sudo docker run \
    --volume=/:/rootfs:ro \
    --volume=/var/run:/var/run:ro \
    --volume=/sys:/sys:ro \
    --volume=/var/lib/docker/:/var/lib/docker:ro \
    --volume=/dev/disk/:/dev/disk:ro \
    --publish=8080:8080 \
    --detach=true \
    --name=cadvisor \
    --privileged \
    --device=/dev/kmsg \
    ghcr.io/google/cadvisor:0.55.1
  ```
* **Librería cliente en Go:** Código reutilizable en las carpetas `client/` y `client/v2/` para conectar y consultar la API de cAdvisor desde otras aplicaciones Go (con ejemplo funcional en `client/clientexample/main.go`).
* **Colector de métricas de aplicaciones:** Permite recolectar métricas expuestas dentro de los propios contenedores mediante formatos de texto o Prometheus (`collector/`).

## Avisos
* **Requisitos del sistema:** Funciona sobre sistemas operativos Linux; depende directamente de características del núcleo Linux como `cgroups`, `/proc` y `/sys`.
* **Permisos y riesgos:** En despliegues con Docker requiere ejecutarse en modo privilegiado (`--privileged`) y con acceso a volúmenes críticos del sistema anfitrión. Ciertas funciones de inspección de almacenamiento (como `thin_ls` en devicemapper) pueden impactar el rendimiento de disco (IOPS) si se activan.
* **Dependencias opcionales:** Algunas mediciones avanzadas de procesador (`perf`, `resctrl`) requieren compilación con CGo y librerías del sistema como `libpfm`.
* **Licencia y costo:** Es software de código abierto bajo la Licencia Apache 2.0 (gratuito).

## ¿Sirve para sus proyectos?
**No.**

* **Conector a la API de Gemini en Cloudflare:** No sirve. Cloudflare Workers es un entorno de computación sin servidor (*serverless*) sin acceso al kernel de Linux ni demonios de contenedores Docker.
* **IA Musa entrenada en Kaggle:** No sirve. Los cuadernos de Kaggle no otorgan los permisos de administrador ni el control de sistema operativo necesarios para gestionar servicios de monitorización a nivel de nodo *(suposición sobre las restricciones del entorno Kaggle: sin confirmar)*.
* **Apps web en GitHub y Cloudflare:** No sirve. Estas plataformas alojan sitios estáticos o funciones en el borde (*edge*), mientras que cAdvisor está diseñado para servidores físicos o virtuales (como clusters de Kubernetes o máquinas con Docker) donde tú gestionas la infraestructura.
