# NVIDIA/Megatron-LM

_Se revisaron los cambios: 4 commits, 32 archivos._

EN UNA LÍNEA: NVIDIA agregó soporte opcional para Liger RMSNorm, actualizó pruebas de inferencia en H100 y cambió cómo su sistema de integración continua usa los tokens de GitHub.

UTILIDAD: baja

## Qué es
Megatron-LM es un repositorio de NVIDIA para investigar y entrenar modelos de lenguaje tipo transformer a gran escala. Tiene más de 18 mil estrellas. Incluye código para modelos como GPT y HybridModel, que puede usar mezcla de expertos (MoE).

## Qué cambió
Hechos del material:
- Se agregó una opción llamada `rmsnorm_impl` para elegir el tipo de normalización en HybridModel: "te" (Transformer Engine, el predeterminado) o "liger" (Liger RMSNorm).
- Se crearon nuevos archivos de código para usar Liger RMSNorm: `megatron/core/ops/norm/backends.py` y `megatron/core/ops/norm/liger_norm.py`.
- GPTModel no acepta la opción "liger"; solo HybridModel.
- Para usar "liger" se necesitan otros ajustes: `normalization="RMSNorm"`, `transformer_impl="transformer_engine"`, `fused_residual_rmsnorm=False`, entre otros.
- Se agregó `liger-kernel==0.8.5` como dependencia opcional, solo para sistemas Linux.
- Se actualizaron los valores esperados (archivos golden values) de varias pruebas de inferencia en tarjetas H100, como latencia, tiempos y uso de memoria.
- En el sistema de pruebas automáticas (CI) de GitHub, ahora se usan dos tokens distintos: uno para leer información (`READ_TOKEN`) y otro para aprobar (`APPROVAL_TOKEN`).
- Se corrigió cómo se registran las pérdidas de balanceo de carga de MoE para evitar errores al leer la configuración.
- Se agregaron pruebas nuevas para Liger RMSNorm y para el comportamiento determinista de los kernels.

Suposiciones (sin confirmar):
- Que separar los tokens de GitHub mejora la seguridad del sistema de pruebas.
- Que Liger RMSNorm puede ahorrar memoria en algunos casos (el material no lo dice).

## Cosas útiles
- Código para activar Liger RMSNorm en HybridModel: usar `--normalization RMSNorm --rmsnorm-impl liger`.
- Clase `LigerRMSNorm` en `megatron/core/ops/norm/liger_norm.py`, reutilizable como backend de normalización.
- Función `get_norm_module_spec` en `megatron/core/ops/norm/backends.py`.
- Pruebas de ejemplo que comparan Liger contra Transformer Engine (`tests/unit_tests/ops/test_liger_norm.py` y `tests/unit_tests/models/test_liger_hybrid.py`).
- Scripts y flujos de CI para manejar tokens de lectura y aprobación en GitHub.
- Valores actualizados de referencia para pruebas de inferencia en H100.

## Avisos
- Requiere tarjetas gráficas NVIDIA; las pruebas se hicieron en H100.
- Liger RMSNorm solo sirve para HybridModel, no para GPTModel.
- No es más rápido: el material dice que Liger suele ser más lento que Transformer Engine.
- `liger-kernel` solo tiene archivos precompilados para Linux; en otros sistemas puede no funcionar.
- Hay que instalar `liger-kernel` por separado (versión 0.8.5 o superior).
- Los cambios de CI dependen de secretos internos de NVIDIA y no se pueden copiar tal cual a otros proyectos sin adaptación.
- El material no menciona la licencia ni los costos (sin confirmar).

## ¿Sirve para sus proyectos?
No. Este repositorio es para entrenar modelos grandes de IA con muchos GPUs, no para proyectos personales gratuitos, conectores a APIs sencillas, apps web o automatizaciones ligeras. Aunque tiene código útil de normalización, depende de un entorno complejo y hardware potente.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
