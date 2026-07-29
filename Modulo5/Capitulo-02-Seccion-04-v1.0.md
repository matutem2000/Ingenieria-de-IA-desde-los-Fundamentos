# Módulo 5 – Capítulo 02 – Sección 04

# Gestión de errores: rate limiting, timeouts, reintentos con backoff exponencial

Los sistemas de producción que consumen APIs de LLM enfrentan tres categorías de errores transitorios que deben manejarse con estrategias de reintento: errores 429 (rate limit excedido), errores 5xx (fallo del servidor del proveedor) y timeouts de conexión o lectura. La respuesta correcta a un 429 no es reintentar inmediatamente —lo que agravaría la sobrecarga— sino esperar el tiempo indicado en el header `Retry-After` o aplicar backoff exponencial con jitter: `wait = min(base * 2^attempt + random.uniform(0, 1), max_wait)`. Los SDKs oficiales implementan retry automático por defecto (2 reintentos en OpenAI y Anthropic), pero para sistemas de alto volumen es necesario configurar estrategias más robustas con bibliotecas como `tenacity` (Python) que permiten definir el número de reintentos, la condición de reintento, el backoff y el logging de cada intento fallido. Los timeouts deben configurarse en dos niveles: timeout de conexión (típicamente 10-30s) y timeout de lectura (60-300s para respuestas largas), evitando que una llamada lenta bloquee un hilo o una coroutine indefinidamente.

## Puntos críticos en gestión de errores de API

- Backoff exponencial con jitter: la fórmula `wait = min(cap, base * 2^n) + random(0, 1)` distribuye los reintentos en el tiempo evitando que múltiples workers reintenten simultáneamente y amplifiquen el problema de rate limiting
- Diferenciación de errores retryables vs permanentes: errores 400 (parámetro inválido) y 401 (API key inválida) no deben reintentarse; errores 429, 500, 502, 503 y 529 son candidatos a reintento con backoff
- Circuit breaker: después de N fallos consecutivos en una ventana de tiempo, dejar de llamar a la API por un período de cooldown y devolver un error inmediato o usar un fallback, evitando saturar recursos propios esperando respuestas que no llegarán
- Dead letter queue: en sistemas asíncronos con colas de mensajes (SQS, RabbitMQ), los mensajes que fallan tras el máximo de reintentos deben enrutarse a una DLQ para inspección manual en lugar de perderse silenciosamente
- Logging de contexto en errores: loggear junto al error el `request_id` de la API, el modelo usado, el número de tokens del prompt y el attempt número facilita el diagnóstico retrospectivo en sistemas con alta concurrencia

## Para recordar

Un sistema que no maneja correctamente los errores transitorios de una API externa no es un sistema de producción; la resiliencia ante fallos del proveedor debe diseñarse desde el primer sprint, no agregarse como parche tras el primer incidente.
