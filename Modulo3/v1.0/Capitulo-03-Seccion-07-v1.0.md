# Estrategias para optimizar el consumo de tokens

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Optimizar tokens no es solo una medida de ahorro económico. Reducir el consumo mejora la latencia de respuesta, libera espacio para información de mayor valor y hace que el razonamiento del modelo sea más preciso al eliminar el ruido del contexto.

Las estrategias de optimización operan en dos niveles: el nivel del prompt —qué se incluye y cómo se formula— y el nivel de la arquitectura —cómo se selecciona, almacena y recupera la información antes de enviarla al modelo.

---

# Estrategias en el nivel del prompt

## Eliminar contexto redundante

Antes de enviar una solicitud, conviene revisar si el contexto contiene información repetida. El mismo dato puede aparecer en las instrucciones del sistema, en un documento recuperado y en el historial conversacional simultáneamente. El modelo no gana claridad por recibir tres veces el mismo hecho; solo pierde espacio disponible.

Una política útil: si un dato ya está en el system prompt, no lo repita en los documentos RAG. Si está en los documentos, no lo reformule en las instrucciones.

## Recuperar solo los documentos relevantes

Los sistemas RAG pueden devolver cinco, diez o veinte documentos por consulta. Enviarlos todos al modelo por precaución es un error habitual. Cada documento que no aporta al razonamiento consume tokens y puede diluir la atención del modelo sobre los que sí importan.

La solución es diseñar el proceso de recuperación con umbral de relevancia: solo incluir documentos cuya similitud supere un valor mínimo. En la práctica, dos o tres documentos de alta relevancia superan en efectividad a diez de relevancia media.

## Limitar los ejemplos few-shot

Los ejemplos few-shot tienen un costo fijo en tokens que se paga en cada solicitud. Si el modelo ya tiene suficiente capacidad para la tarea sin ejemplos —o si los ejemplos ya están incorporados en el fine-tuning— incluirlos es un gasto innecesario.

La práctica recomendada es comenzar sin ejemplos, medir la calidad de las respuestas y agregar ejemplos solo si el rendimiento no es aceptable. Menos ejemplos bien elegidos son más efectivos que muchos ejemplos genéricos.

## Normalizar respuestas de herramientas

Los resultados devueltos por herramientas externas —APIs, bases de datos, ejecutores de código— pueden ser muy verbosos: respuestas JSON completas, encabezados HTTP, mensajes de debug. Enviarlos tal cual al modelo desperdicia tokens en información que no aporta al razonamiento.

La solución es un paso de normalización: extraer solo los campos relevantes, convertir JSON complejo en texto estructurado conciso y eliminar metadatos que el modelo no necesita.

## Mantener instrucciones compactas

El system prompt tiende a crecer con el tiempo a medida que se agregan nuevas reglas, restricciones y comportamientos esperados. Una auditoría periódica del system prompt suele revelar instrucciones redundantes, contradictorias o ya superadas por otras.

Un system prompt eficiente es aquel que contiene solo las instrucciones que el modelo no puede inferir de su entrenamiento o del contexto de la conversación.

---

# Estrategias en el nivel de la arquitectura

## Caching de contexto

Los principales proveedores ofrecen mecanismos de **caching de prefijos** que permiten reutilizar partes del contexto entre solicitudes sin volver a procesarlas. Cuando una porción del contexto —como el system prompt o una base de conocimiento estática— permanece igual entre consultas, el proveedor puede computarla una vez y cobrar una fracción del precio en las solicitudes subsiguientes.

Esta técnica es especialmente rentable en aplicaciones con system prompts extensos o con documentos de referencia que se incorporan a cada consulta. El ahorro puede ser sustancial cuando el volumen de solicitudes es alto.

La implementación práctica varía según el proveedor: algunos lo hacen automáticamente cuando detectan prefijos repetidos, otros requieren que el sistema marque explícitamente qué fragmentos son candidatos al cache.

## Separar historial, memoria y RAG

Mezclar tres fuentes de información distintas en un único bloque de texto aumenta el consumo de tokens y complica el razonamiento del modelo. Una arquitectura bien diseñada mantiene separados:

- el **historial conversacional**: los últimos N intercambios del turno actual;
- la **memoria persistente**: hechos y preferencias de largo plazo del usuario;
- los **documentos RAG**: información recuperada específicamente para esta consulta.

Esta separación permite aplicar políticas de optimización distintas a cada capa, y al modelo le resulta más sencillo discriminar entre qué es contexto inmediato y qué es conocimiento de base.

---

# Herramientas para medir tokens

Optimizar sin medir es opinar sin evidencia. Las herramientas de conteo de tokens permiten instrumentar la aplicación y detectar dónde se concentra el consumo.

**Anthropic:** la API expone el campo `usage` en cada respuesta, que devuelve `input_tokens` y `output_tokens`. La biblioteca oficial también ofrece el método `count_tokens` para estimar el consumo antes de enviar la solicitud.

**OpenAI:** la biblioteca `tiktoken` permite contar tokens localmente para todos los modelos de la familia GPT, sin necesidad de hacer una llamada a la API.

**Herramientas de observabilidad:** plataformas como LangSmith, Helicone o Phoenix permiten registrar y visualizar el consumo de tokens por sesión, por usuario y por tipo de consulta, facilitando la detección de patrones de uso ineficiente.

La instrumentación mínima recomendada para cualquier aplicación en producción es registrar, para cada solicitud: tokens de entrada, tokens de salida, costo estimado y latencia. Con esos cuatro datos es posible detectar regresiones y oportunidades de optimización de forma continua.

---

# Métricas para el seguimiento operativo

El seguimiento sistemático del consumo de tokens requiere definir métricas concretas:

- **Tokens promedio por solicitud:** establece la línea base de consumo y permite detectar derivaciones hacia arriba que indican acumulación de contexto no gestionada.
- **Ratio input/output:** una relación muy alta de tokens de salida respecto a los de entrada puede indicar que el modelo está generando respuestas más extensas de lo necesario.
- **Costo por conversación:** calcula el costo total de una sesión completa, no solo de cada solicitud individual. Permite comparar estrategias de administración del contexto.
- **Tiempo de respuesta:** correlaciona el consumo de tokens con la latencia percibida por el usuario.

---

# Buenas prácticas

- Instrumentar el consumo de tokens desde el primer día de desarrollo, no al detectar problemas en producción.
- Revisar el system prompt cada tres meses para eliminar instrucciones obsoletas.
- Establecer un umbral de tokens de entrada máximo por solicitud y alertar cuando se supere.
- Aplicar normalización a todas las respuestas de herramientas externas antes de incluirlas en el contexto.
- Evaluar la posibilidad de usar caching de prefijos en aplicaciones con system prompts extensos o bases de conocimiento estáticas.

---

# Resumen

La optimización de tokens opera en múltiples niveles simultáneamente: el contenido del prompt, la arquitectura de recuperación y las capacidades de la plataforma. Las aplicaciones que miden, controlan y optimizan el consumo de tokens de forma sistemática no solo reducen costos sino que, en la mayoría de los casos, también mejoran la calidad de las respuestas al eliminar el ruido del contexto.

En la próxima sección estudiaremos los patrones arquitectónicos más importantes para administrar el contexto en aplicaciones de producción.
