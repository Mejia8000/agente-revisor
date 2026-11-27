# google/sentencepiece

_Se leyeron 15,000 de 38,204 líneas de código. (límite de 15,000; súbalo en fuentes.json)_

EN UNA LÍNEA: Una biblioteca rápida y de código abierto para entrenar y ejecutar tokenizadores de texto (dividir texto en subpalabras y reconstruirlo) orientada a modelos de lenguaje.

UTILIDAD: Media

## Qué es
Es una herramienta desarrollada originalmente en C++ (con interfaz para Python y línea de comandos) que toma texto en bruto y lo convierte en números (tokens) o fragmentos de palabras (subpalabras), y viceversa. 
- Implementa algoritmos de tokenización como BPE (Byte-Pair-Encoding) y Unigram.
- Trata los espacios en blanco como caracteres normales (usando el símbolo ` `), lo que permite reconstruir el texto original exactamente igual sin perder información ni depender de reglas específicas de un idioma.
- Es el tokenizador utilizado por arquitecturas de modelos conocidos como T5, LLaMA o Gemma.

## Qué hay nuevo
A partir del código fuente y documentación provista:
- **SentencePiece Lite:** Un motor de ejecución en C++20 ultraligero y sin dependencias externas pesadas (sin Abseil ni Protobuf en ejecución), diseñado para móviles y dispositivos limitados. Usa archivos en formato FlatBuffers (`.spm.fb`) y carga directa en memoria (`mmap`).
- **Caché de tokens (`TokenCache`):** Sistema de aceleración en memoria para reutilizar fragmentos de texto procesados frecuentemente.
- **Búsqueda global y cobertura automática (`auto_character_coverage`):** Algoritmo con árbol de Fenwick en el entrenamiento BPE para balancear automáticamente cuántos caracteres únicos y cuántas subpalabras incluir sin fijar la cobertura manualmente.
- **Soporte ampliado para Python moderno:** Compatibilidad declarada hasta Python 3.13/3.14/3.15 y soporte para Python sin bloqueo global de intérprete (*free-threading / GIL disabled*).
- **Herramientas añadidas:** Scripts de evaluación de compresión y perplejidad (`spm_eval`), conversión de modelos a formato FlatBuffer (`spm_to_fb`) y unificación de código C++ en un solo archivo (`amalgamate.py`).

## Cosas útiles
- **Instalación directa en Python:** Se instala gratis con:
  ```bash
  pip install sentencepiece
  ```
- **Código reutilizable en Python para entrenar y usar un tokenizador:**
  ```python
  import sentencepiece as spm

  # 1. Entrenar con un archivo de texto en bruto
  spm.SentencePieceTrainer.train(input='mi_texto.txt', model_prefix='mi_modelo', vocab_size=1000)

  # 2. Cargar el modelo generado
  sp = spm.SentencePieceProcessor(model_file='mi_modelo.model')

  # 3. Convertir texto a IDs numéricos y a fragmentos
  ids = sp.encode("Hola mundo", return_type=int)
  piezas = sp.encode("Hola mundo", return_type=str)

  # 4. Reconstruir texto original (detokenizar)
  texto_recuperado = sp.decode(ids)
  ```
- **Herramientas de línea de comandos integradas:** Utilidades ejecutables como `spm_train` (entrenamiento), `spm_encode` (tokenización), `spm_decode` (decodificación), `spm_normalize` (normalización de caracteres) y `spm_export_vocab` (exportar el vocabulario a texto).

## Avisos
- **Licencia:** Apache 2.0 (permite uso comercial, modificación y distribución gratuita).
- **Costos:** Completamente gratuito y de código abierto.
- **Aclaración oficial:** El repositorio indica expresamente que no es un producto oficial respaldado por Google.
- **Requisitos técnicos:** 
  - Para Python precompilado: Python 3.10 o superior.
  - Para compilar desde código fuente o usar la versión *Lite*: Compilador compatible con C++20 y CMake.
  - Advertencia con `pybind11`: Si se compila el módulo Python a mano, las versiones de pybind11 iguales o superiores a 3.1 provocan una degradación de rendimiento de 2x a 3x en ciertas operaciones por la gestión de memoria interna.
- **Límites:** No es un modelo de lenguaje en sí mismo, solamente prepara y traduce el texto a números para alimentar modelos de IA.

## ¿Sirve para sus proyectos?
**Sí, pero solo para proyectos específicos (No para la mayoría de tareas web cotidianas).**

- **Modelos propios:** **Sí.** Si vas a entrenar o ejecutar localmente redes neuronales o modelos de lenguaje propios (como transformadores en PyTorch o C++), este componente es esencial para armar el vocabulario y procesar los textos antes de enviarlos a la red.
- **Conectores a APIs de IA gratuitas o comerciales:** **No.** Si tu objetivo es únicamente enviar peticiones a APIs de lenguaje externas (como las de Google Gemini, OpenAI o Claude), estas reciben cadenas de texto normales por HTTP/REST y se encargan internamente de la tokenización, por lo que no necesitas SentencePiece en tu flujo.
- **Apps web y automatizaciones comunes:** **No.** Salvo que tu aplicación web requiera medir tokens exactos de modelos que usen este formato antes de procesarlos, añadirlo sumará complejidad innecesaria.
