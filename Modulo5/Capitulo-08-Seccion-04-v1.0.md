# Módulo 5 – Capítulo 08 – Sección 04

# Métricas operativas: P50/P95/P99 de latencia, tasa de error y costo por petición

Las métricas operativas de un sistema de IA deben capturar tanto las dimensiones técnicas (latencia, errores, disponibilidad) como las dimensiones económicas (costo por request, costo por usuario, costo por feature) que son únicas en sistemas basados en APIs de pago por uso. La latencia de un LLM es bimodal: el Time to First Token (TTFT) es la latencia percibida por el usuario en interfaces de streaming y depende de la carga del servidor del proveedor; el tiempo de generación completo depende además del número de tokens de salida. Las métricas de percentil (P50, P95, P99) son más informativas que la media porque la media enmascara outliers: si el P99 de latencia es 30 segundos mientras la media es 3 segundos, hay un 1% de requests que degrada significativamente la experiencia de usuario y eso no se ve en la media. La tasa de error en sistemas de IA tiene dos dimensiones: errores técnicos (HTTP 4xx/5xx del proveedor, timeouts, rate limits) que el sistema de monitoreo detecta automáticamente, y "errores de calidad" (respuestas incorrectas o insatisfactorias) que requieren métricas de evaluación para detectarse.

## Métricas operativas específicas de sistemas de IA

- TTFT (Time to First Token): tiempo desde que el request llega al servicio hasta que el primer token de la respuesta llega al cliente; el KPI más importante en interfaces de chat streaming; target típico: P95 < 1 segundo para experiencia fluida
- Tiempo de generación completo (TTTOK - Time to Last Token): incluye TTFT más el tiempo de generación del resto de la respuesta; depende de `output_tokens * velocidad_del_modelo`; target típico: P95 < 5-10 segundos para respuestas medias
- Tokens por request (media e histograma): monitorear la distribución de `input_tokens` y `output_tokens` por feature y tipo de query; spikes en `input_tokens` pueden indicar un bug de contexto que accumula historial sin límite
- Costo por request y costo por usuario activo: `costo_diario / DAU` (Daily Active Users) es la métrica de eficiencia económica del sistema; permite proyectar el costo a escala y comparar el costo de diferentes configuraciones de modelo
- Tasa de cache hit: en sistemas con prompt caching habilitado (Anthropic) o caché semántica, el porcentaje de requests que reutilizan tokens cacheados reduce el costo; monitorear esta tasa y su impacto en el costo total valida la inversión en la arquitectura de caching

## Para recordar

El P99 de latencia de un sistema de IA es a menudo 5-10x mayor que el P50, porque las respuestas largas, los contextos complejos y los momentos de carga alta del proveedor se acumulan en la cola de la distribución; diseñar la UX para manejar graciosamente los casos de alta latencia es tan importante como optimizar la latencia media.
