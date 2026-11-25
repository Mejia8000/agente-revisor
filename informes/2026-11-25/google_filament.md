# google/filament

_Repositorio muy grande: se leyó solo el README._

EN UNA LÍNEA: Filament es un motor gratuito de Google para crear gráficos 3D realistas en tiempo real en celulares, computadoras y navegadores web.

## Qué es
Hechos:
- Es un motor de renderizado en tiempo real basado en física (PBR), es decir, dibuja objetos 3D con luz y materiales que se comportan como en la vida real.
- Funciona en Android, iOS, Windows, Linux, macOS, WebGPU y WebGL 2.0. El README también menciona WASM.
- Tiene más de 20.000 estrellas en GitHub.
- Ofrece versiones estables para descargar y librerías para Android (Maven) e iOS (CocoaPods).
- Tiene APIs en C++, Java para Android y JavaScript.
- Incluye herramientas como matc (compilador de materiales), cmgen y visores de modelos glTF.
- Los ejemplos de texturas y mapas de entorno tienen licencia CC0.
- El README advierte que no es un producto oficialmente soportado por Google.

Suposiciones:
- Que la versión 1.81.0 sea la más reciente: sin confirmar.

## Qué hay nuevo
Hechos:
- El README no muestra una lista de novedades ni cambios recientes.

Suposiciones:
- Que existan mejoras en versiones más nuevas: sin confirmar.

## Cosas útiles
- Código de ejemplo en C++ para crear el motor, la cámara, la escena y renderizar un frame.
- Dependencia para Android: `com.google.android.filament:filament-android:1.81.0`.
- Dependencia para iOS: `pod 'Filament', '~> 1.81.0'`.
- Herramientas gratis incluidas: matc, cmgen, matedit y un visor de archivos glTF.
- Modelos y texturas de ejemplo bajo licencia CC0 en la carpeta `third_party`.
- Documentación en inglés sobre materiales y renderizado PBR.

## Avisos
- Requisitos: se necesita saber programar en C++ (o Java/JavaScript) y entender conceptos de gráficos 3D.
- Licencia: el README solo remite al archivo LICENSE; no se muestra el texto completo de la licencia aquí.
- Costo: el README no menciona precios, parece ser de uso gratuito.
- Límites: es solo para renderizado 3D; no sirve para inteligencia artificial ni para conectar a APIs de servicios web.
- Riesgos: Google avisa que no es un producto oficialmente soportado. El repositorio es muy grande y solo se revisó el archivo README.

## ¿Sirve para sus proyectos?
No. Sus proyectos son un conector a la API de Gemini en Cloudflare, una IA llamada Musa que entrena en Kaggle, y apps web publicadas con GitHub y Cloudflare. Filament es un motor de gráficos 3D, no sirve para conectar a APIs de IA, no sirve para entrenar modelos de IA, y aunque puede dibujar en la web (WebGL2/WebGPU), no es una herramienta para publicar apps web comunes. Solo le serviría si alguna de sus apps web necesita renderizado 3D avanzado en tiempo real.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
