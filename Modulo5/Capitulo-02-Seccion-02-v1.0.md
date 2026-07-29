# Módulo 5 – Capítulo 02 – Sección 02

# Parámetros de inferencia: temperatura, top-p, top-k, max_tokens y su efecto

Los parámetros de inferencia controlan el proceso de muestreo durante la generación de tokens y tienen efecto directo en la creatividad, coherencia, costo y latencia de las respuestas; elegirlos correctamente es tan importante como el diseño del prompt. La `temperature` (rango 0.0-2.0 en OpenAI, 0.0-1.0 en Anthropic) escala los logits antes del softmax: a temperatura 0 el modelo es determinista seleccionando siempre el token de mayor probabilidad, a temperatura alta la distribución se aplana favoreciendo tokens menos probables y generando salidas más variadas. `top_p` (nucleus sampling, rango 0.0-1.0) recorta el vocabulario al subconjunto de tokens cuya probabilidad acumulada alcanza `p`, limitando la cola de opciones improbables; `top_k` hace lo mismo pero tomando los `k` tokens de mayor probabilidad sin importar su suma acumulada. Anthropic recomienda no modificar ambos (`top_p` y `top_k`) simultáneamente con `temperature`, ya que interactúan de forma compleja; OpenAI recomienda modificar temperatura O top_p pero no ambos.

## Aspectos técnicos de los parámetros de muestreo

- `temperature=0.0`: produce respuestas deterministas útiles para tareas de extracción estructurada, clasificación o generación de código donde la reproducibilidad es requerida; temperatura cercana a 0 pero no exactamente 0 a veces estabiliza casos límite
- `temperature=0.7-1.0`: rango común para generación creativa, redacción de contenido y respuestas conversacionales donde se desea variedad sin perder coherencia semántica
- `max_tokens` (o `max_completion_tokens` en OpenAI): limita la longitud de la respuesta en tokens; tiene impacto directo en el costo de la llamada y en el tiempo total de respuesta; truncar respuestas con `max_tokens` bajo puede generar salidas JSON incompletas
- `top_p=0.95`: valor de producción común que retiene el 95% de la masa de probabilidad, eliminando opciones de muy baja probabilidad sin forzar al modelo a ser determinista
- `stop_sequences`: complementa `max_tokens` para terminar la generación ante un delimitador específico como `\n\n`, `</output>` o `###`, garantizando salidas bien delimitadas sin desperdiciar tokens

## Buena práctica

Documentar los valores de temperatura y otros hiperparámetros usados en producción junto con el prompt versionado, ya que cambios en estos parámetros pueden alterar el comportamiento del sistema tanto como cambios en el texto del prompt.
