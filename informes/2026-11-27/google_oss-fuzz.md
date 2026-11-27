# google/oss-fuzz

_Se revisaron los cambios: 18 commits, 140 archivos._

EN UNA LÍNEA: Actualización masiva de las imágenes de prueba a Ubuntu 24.04 con ajustes de compilación y la incorporación del proyecto Quinn.

UTILIDAD: Baja

## Qué es
OSS-Fuzz es un servicio y plataforma creada por Google para realizar "fuzzing" continuo (técnica que introduce datos aleatorios o inesperados de forma automática para encontrar fallos y vulnerabilidades de seguridad) en proyectos de software de código abierto.

## Qué cambió
* **Migración a Ubuntu 24.04:** Decenas de proyectos (como ImageMagick, OpenSSL, Boost, Flatbuffers, Tor, Wasmedge, entre muchos otros) cambiaron sus entornos de compilación de versiones anteriores a Ubuntu 24.04.
* **Ajustes en dependencias del sistema:** Se actualizó la referencia de paquetes en varios proyectos, cambiando el paquete desactualizado `python` por `python-is-python3`.
* **Correcciones para detectores de memoria (MSan/Sanitizers):** Se añadieron modificaciones y opciones de compilación en proyectos como Flatbuffers, LXC, Libarchive, Poco, Suricata y Yara para evitar errores y falsos positivos provocados por versiones recientes de librerías del sistema (`glibc`).
* **Nuevo proyecto integrado:** Se añadieron los archivos de configuración y scripts para probar por primera vez el proyecto en Rust llamado `quinn`.
* **Actualización de versiones de desarrollo:** En proyectos como WasmEdge, se actualizaron las dependencias internas de LLVM 12 a LLVM 18.

## Cosas útiles
* **Ejemplos de configuración para Rust:** El archivo `projects/quinn/build.sh` sirve como ejemplo simple y reutilizable de cómo automatizar la compilación de pruebas de seguridad usando `cargo fuzz`.
* **Scripts de compilación avanzada:** Contiene ejemplos de scripts de consola (`build.sh`) que muestran cómo compilar librerías complejas en C/C++ de forma estática (como OpenSSL).
* *Nota:* No contiene modelos de IA ni APIs web preparadas para consumo.

## Avisos
* **Licencia:** El repositorio utiliza la licencia Apache 2.0 (código abierto y gratuito).
* **Requisitos:** Requiere el uso de Docker y conocimientos técnicos avanzados sobre compilación a bajo nivel (C, C++, Rust), librerías del sistema y herramientas de sanitización de memoria.
* **Riesgos / Suposición sin confirmar:** Aunque los ajustes resuelven incompatibilidades con Ubuntu 24.04 en el entorno de pruebas, es posible (sin confirmar) que algunos proyectos requieran ajustes adicionales si surgen problemas en ejecuciones prolongadas.

## ¿Sirve para sus proyectos?
No. Tu enfoque está en la creación de aplicaciones web, automatizaciones y conectores para APIs o modelos de inteligencia artificial. Este repositorio es un sistema interno de pruebas de vulnerabilidades para software de infraestructura y lenguajes de bajo nivel; no ofrece funciones, conectores ni modelos aplicables a tus proyectos actuales.
