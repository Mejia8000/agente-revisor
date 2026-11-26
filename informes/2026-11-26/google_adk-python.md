# google/adk-python

_Se revisaron los cambios: 3 commits, 96 archivos._

EN UNA LÍNEA: El kit de herramientas ADK para Python recibió cambios internos en la escritura de tipos de datos y una función experimental para registrar el razonamiento de los modelos de IA.

UTILIDAD: media

## Qué es
Hecho: Es un kit de herramientas de código abierto escrito en Python para crear, evaluar y desplegar agentes de inteligencia artificial.
Hecho: El repositorio público tiene más de 22.000 estrellas.
Hecho: Está diseñado para usarse principalmente escribiendo código Python ("code-first").

## Qué cambió
Hecho: En muchos archivos se modernizó la forma de escribir los tipos de datos de Python. Por ejemplo, `Optional[str]` se escribió como `str | None`, y `List[str]` como `list[str]`. Esto no cambia el funcionamiento del programa.
Hecho: Se agregó soporte experimental para "partes de razonamiento" en los mensajes de IA generativa que usa la telemetría. Esto permite separar el texto que el modelo genera al "pensar" del texto que entrega como respuesta final.
Hecho: Se agregó "reasoning" como una característica experimental que se puede activar en la configuración de telemetría.
Suposición: Esta función ayuda a entender mejor cómo llega el modelo a sus respuestas (sin confirmar).

## Cosas útiles
Hecho: El código está disponible públicamente y se puede copiar o adaptar en proyectos propios.
Hecho: Incluye archivos de ejemplo para desplegar agentes en servicios como Agent Engine, Cloud Run y GKE.
Suposición: Se puede usar sin pagar licencia por el kit, porque es de código abierto (sin confirmar si hay costos de uso asociados).

## Avisos
Hecho: Se necesita saber programar en Python para usar este kit; no es una herramienta visual de "arrastrar y soltar".
Hecho: La función de razonamiento está marcada como experimental, así que puede cambiar o desaparecer en versiones futuras.
Suposición: Desplegar agentes en Google Cloud puede generar costos en la nube, aunque el kit en sí sea gratis (sin confirmar montos ni condiciones).
Suposición: Algunas funciones de despliegue requieren una cuenta de Google Cloud (sin confirmar).

## ¿Sirve para sus proyectos?
Sí, con reservas. Sirve si quiere crear sus propios agentes de IA con Python y conectarlos a APIs o automatizaciones personales. No es la mejor opción si solo busca conectores listos para usar o apps web sin programar, porque este kit requiere escribir código y el cambio nuevo es solo de telemetría interna.

_(Informe hecho por nvidia/nemotron-3.5-super-vl:free, respaldo)_
