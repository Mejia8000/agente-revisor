# NVIDIA/Megatron-LM

_Se revisaron los cambios: 6 commits, 43 archivos._

EN UNA LÍNEA: Herramienta avanzada de NVIDIA para entrenar modelos de inteligencia artificial gigantescos en supercomputadoras y redes de muchas tarjetas gráficas.

UTILIDAD: Baja

## Qué es
Es un sistema especializado de NVIDIA para entrenar modelos masivos de lenguaje (como GPT) repartiendo el trabajo de cálculo entre decenas o cientos de procesadores gráficos (tarjetas GPU potentes). No está pensado para usar modelos en el día a día, sino para crearlos y entrenarlos a escala empresarial.

## Qué cambió
- **Mayor seguridad al cargar archivos:** Se modificó la lectura de archivos de guardado (`.metadata` de PyTorch) para restringir qué tipos de datos se pueden abrir. Esto evita que un archivo manipulado con malas intenciones ejecute programas dañinos en el servidor.
- **Mejoras en el optimizador "Muon":** Se reorganizó la forma en que las tarjetas gráficas se reparten el trabajo para evitar esperas innecesarias cuando los cálculos ya están dentro del mismo procesador.
- **Compatibilidad con nuevas librerías:** Se adaptó el código para funcionar con versiones recientes de *Transformer Engine* (versión 2.21 en adelante) y se actualizó el paquete de aceleración *FlashAttention-4*.
- **Correcciones matemáticas:** Se arregló la forma en que se miden ciertos gradientes distribuidos (parámetro `softmax_offset`) para que no se omitan partes del cálculo al entrenar en paralelo.
- **Ajustes en pruebas internas:** Se separaron pruebas de red (comunicación NCCL) para evitar fallos y bloqueos en las pruebas automáticas.

## Cosas útiles
- **Código de seguridad reutilizable:** El archivo `megatron/core/safe_globals.py` tiene un ejemplo práctico de cómo crear una lista blanca de clases seguras para `pickle` en Python, lo cual sirve si en algún proyecto propio necesitas abrir archivos serializados evitando virus o inyecciones de código.
- *Nota:* En esta actualización no se incluyen APIs gratuitas ni modelos de IA listos para descargar.

## Avisos
- **Requisitos de hardware extremos:** Requiere tarjetas gráficas empresariales muy caras de NVIDIA (como A100, H100 o Blackwell GB200) y Linux. No está diseñado para funcionar en computadoras de escritorio comunes ni en procesadores convencionales (CPU).
- **Costos elevados:** Alquilar la infraestructura necesaria en la nube para usar Megatron-LM tiene costos muy altos (sin confirmar el costo exacto por hora, pero suele ser de cientos a miles de dólares en gran escala).
- **Riesgo y complejidad:** Si se configuran mal los parámetros de paralelismo o las versiones de las librerías auxiliares de NVIDIA, los procesos de entrenamiento fallan o se bloquean por completo.

## ¿Sirve para sus proyectos?
**No.** 
Megatron-LM es una herramienta para laboratorios y empresas que entrenan modelos masivos desde cero en granjas de servidores. Para proyectos personales con APIs gratuitas, aplicaciones web o automatizaciones, esta herramienta es totalmente innecesaria, incompatible con niveles gratuitos y requiere conocimientos de computación distribuida de alto nivel. Para tus objetivos es mucho más práctico usar librerías ligeras como las de Hugging Face o conectarte a proveedores de modelos vía API estándar.
