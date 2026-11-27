# NVIDIA/auto-ontology

_Se leyeron 15,000 de 195,534 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Auto Ontology es una librería abierta de NVIDIA que crea automáticamente mapas semánticos sobre bases de datos para que agentes de IA respondan preguntas con SQL de forma más precisa y explicable.

UTILIDAD: media

## Qué es
- Es un framework de Python de NVIDIA, con licencia Apache-2.0 (código libre).
- Construye una "ontología": un mapa que relaciona conceptos de negocio (como "cliente" o "factura") con las tablas y columnas donde están guardados.
- Permite que agentes de IA generen consultas SQL, expliquen los pasos seguidos y validen las respuestas contra los datos.
- Se conecta a 11 motores de bases de datos: PostgreSQL, MySQL, Databricks, Snowflake, ClickHouse, Trino, Google BigQuery, Apache Kyuubi, HeavyDB, DuckDB y SQLite.
- Expone la información a agentes mediante MCP, CLI y API REST.
- Usa Postgres 17 con pgvector para guardar el catálogo y los vectores de búsqueda.
- Incluye interfaz web, backend y servicio de ingestión en contenedores Docker.

## Qué hay nuevo
- El material no detalla cambios respecto a versiones anteriores; solo indica la versión 1.3.0 del servidor.
- Señala que ocupa el primer lugar en dos benchmarks de precisión de preguntas a bases de datos (BIRD-Interact y BEAVER). Esto es un hecho del material, pero no se confirma que se aplique a proyectos personales pequeños (sin confirmar).
- Es compatible con Apache Ossie, un estándar abierto para intercambiar modelos semánticos.

## Cosas útiles
- Ejemplo de código en Python para llamar a la API REST (`POST /api/chat/completions`) y leer la respuesta por eventos.
- Ejemplos de configuración para conectar el servidor MCP con Cursor y Claude Desktop.
- Conectores listos para usar con 11 motores de bases de datos.
- Ejemplo de pregunta, SQL generado y pasos de razonamiento que se pueden reutilizar como referencia.
- Exportación e importación de modelos en formato Ossie YAML.
- Código abierto bajo licencia Apache-2.0.

## Avisos
- El inicio rápido requiere Docker con Compose v2, la herramienta `uv` y una clave de API de NVIDIA (`nvapi-...`) obtenida en build.nvidia.com.
- Por defecto usa modelos de NVIDIA NIM; el material no dice si son gratuitos ni cuánto cuestan (sin confirmar).
- Requiere Python 3.12 o superior (menos de 3.14).
- La instalación completa levanta varios contenedores y usa los puertos 3000, 3001, 3002, 3003 y 5432.
- Servicios opcionales como Vault (credenciales) y KumoRFM (predicciones) dependen de términos externos y no están activos por defecto.
- El software se proporciona "tal cual", sin garantía, y los materiales externos (modelos, servicios) tienen sus propias licencias.
- Está pensado para entornos empresariales con muchas fuentes de datos y definiciones complejas; si solo hay una fuente y pocas preguntas, SQL directo puede ser suficiente.

## ¿Sirve para sus proyectos?
No. Para proyectos personales con IA gratis, es demasiado pesado: necesita servidor, base de datos, vectores y probablemente claves de API de NVIDIA que pueden tener costo (sin confirmar). Aunque tiene conectores y ejemplos de código útiles, no es una herramienta ligera para empezar rápido sin infraestructura ni costo potencial.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
