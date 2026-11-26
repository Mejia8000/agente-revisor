# google/libphonenumber

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: Es una librería de Google para leer, formatear y validar números de teléfono de cualquier país en Java, C++ y JavaScript.

UTILIDAD: alta

## Qué es
Hechos:
- Es una librería de Google escrita en Java, C++ y JavaScript.
- Sirve para analizar, formatear y validar números de teléfono de todos los países.
- La versión Java se usa en Android desde la versión 4.0.
- Puede identificar el tipo de número (móvil, fijo, gratuito, VoIP, etc.), comparar si dos números podrían ser iguales, buscar números dentro de un texto, y dar información de ubicación, operador original y zona horaria.
- Hay demostraciones web para Java y JavaScript.
- Hay ejemplos de código Java para usar la librería.
- Existen versiones hechas por otras personas para Python, PHP, JavaScript, Go, Swift y más lenguajes.

Suposiciones:
- Es útil para aplicaciones móviles (sin confirmar, aunque el README dice que está optimizada para teléfonos inteligentes y usada por Android).
- Se puede usar en proyectos personales sin pagar (sin confirmar, el material no dice si es gratis ni cuál es la licencia).

## Qué hay nuevo
Hechos:
- El material no detalla novedades de una versión específica.
- Dice que la versión en Maven es 8.12.57, pero la demostración de Java está en v9.0.44 y tiene retrasos en su actualización.

Suposiciones:
- Ninguna.

## Cosas útiles
- Ejemplos de código Java listos para usar: convertir un número de Suiza a formato internacional, nacional y E164.
- Herramienta para formatear el número mientras la persona escribe cada dígito.
- Herramienta para obtener la ciudad o región de un número (por ejemplo, Zúrich).
- Herramienta para saber el operador original de un número.
- Demos web de Java y JavaScript para probar sin instalar nada.
- Lista de versiones de la librería para otros lenguajes (Python, PHP, JavaScript, Go, Swift, etc.).

## Avisos
- Requisitos: en Android, la versión Java lee los datos desde Class#getResourcesAsStream; se recomienda empaquetar los datos y leerlos desde AssetManager (mejor práctica de Android).
- La demostración web de Java no está actualizada con la última versión de la librería.
- La herramienta de operador solo da la compañía original asignada al rango del número, no la compañía actual (por portabilidad numérica).
- Las versiones para otros lenguajes son hechas por terceros; Google no revisa su calidad ni su mantenimiento.
- El material no menciona licencia, costos ni límites de uso (sin confirmar si hay costos o restricciones).

## ¿Sirve para sus proyectos?
Sí. Sirve para apps web (tiene versión JavaScript y demos en el navegador) y automatizaciones (tiene ejemplos en Java y versiones para Python, PHP, etc.) que necesiten validar, formatear o obtener datos de números de teléfono. No es una herramienta de inteligencia artificial ni una API externa, pero puede usarse como utilidad dentro de conectores o procesos automáticos que manejen teléfonos.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
