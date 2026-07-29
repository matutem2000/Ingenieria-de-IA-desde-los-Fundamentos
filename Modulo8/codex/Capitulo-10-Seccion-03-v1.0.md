# Módulo 8 – Capítulo 10 – Sección 03

# Fallback patterns: usar nube cuando el modelo local falla o supera su capacidad

Los fallback patterns en arquitecturas híbridas son mecanismos que detectan automáticamente cuando el modelo local no puede responder de forma satisfactoria y escalan la petición a un recurso alternativo más capaz, típicamente un modelo de nube, sin intervención del usuario y con latencia adicional mínima. Los escenarios que deben activar el fallback incluyen: errores técnicos del servidor local (timeout, OOM, error HTTP 5xx), baja confianza de la respuesta detectada por un clasificador post-procesamiento, longitud del contexto que excede el límite del modelo local, y respuestas que activan filtros de calidad (demasiado cortas, fuera del dominio, con alucinaciones detectadas). El fallback basado en longitud de contexto es el más simple de implementar: si el número de tokens del prompt excede el `num_ctx` máximo del modelo local (ej: 8.192 para un modelo Ollama básico), la petición se enruta automáticamente a la API de nube que soporta contextos de 128K o más; este fallback es determinístico y no requiere clasificación. El fallback basado en calidad es más sofisticado: requiere un verificador rápido (otro modelo pequeño o un sistema de reglas) que evalúe la respuesta del modelo local antes de devolverla al usuario, y decide si la calidad es suficiente o si debe regenerarse con un modelo más potente; este overhead de verificación debe ser suficientemente bajo (<100ms) para no afectar la latencia percibida en el caso normal.

## Implementación de fallback patterns

- Timeout-based fallback: configurar un timeout estricto para el modelo local (ej: 5 segundos para la primera respuesta); si se supera, cancelar la petición local y reenviarla al modelo de nube; implementar con `asyncio.wait_for()` en Python o timeouts HTTP en el nivel de proxy
- Circuit breaker pattern: si el modelo local falla N veces en una ventana de tiempo W, abrir el circuit breaker y enrutar todo el tráfico a la nube durante un tiempo de recuperación T; evita thundering herd de fallbacks cuando el servidor local está degradado; implementable con librerías como `pybreaker` o `tenacity`
- Cascading fallback: jerarquía de modelos local_7B → local_13B → cloud_economica → cloud_frontera; cada nivel se activa solo si el anterior falla o no supera el umbral de calidad; permite un balance fino entre latencia adicional de cada fallback y calidad de respuesta
- Response quality gate: un clasificador binario ligero (DistilBERT o ONNX) que analiza la respuesta del modelo local en <50ms y predice si un humano la consideraría satisfactoria; score por debajo del umbral activa el fallback a la nube; el clasificador se entrena en logs de feedback de producción (thumbs up/down)
- Logging de fallbacks: registrar cada fallback con el motivo (timeout, error, baja calidad, contexto largo), el modelo origen y el modelo destino; esta telemetría permite analizar las causas de fallback y tomar decisiones informadas sobre si vale la pena mejorar el modelo local o ajustar los umbrales

## Para recordar

El fallback pattern no es una señal de que el modelo local no funciona: es una característica de diseño deliberada que hace que la arquitectura sea más resiliente y que las peticiones marginales que excedan la capacidad del modelo local reciban la mejor respuesta posible.
