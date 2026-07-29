# Módulo 7 – Capítulo 03 – Sección 05

# Gestión de errores en herramientas: qué hacer cuando la herramienta falla

Los fallos de herramientas en producción son inevitables: APIs externas devuelven timeouts o 5xx errors, el intérprete de código lanza excepciones, las búsquedas no devuelven resultados relevantes, y el filesystem devuelve permisos denegados. La gestión de errores de herramientas no debe ser delegada al LLM por defecto: el agente necesita una política explícita de manejo de errores que especifique si debe reintentar, intentar con una herramienta alternativa, simplificar la tarea o escalar al humano. El error más común en sistemas agénticos de producción no es que las herramientas fallen, sino que el agente no sabe qué hacer cuando fallan: sin política de error, puede entrar en bucles de reintento, inventar resultados plausibles o simplemente quedar bloqueado. La respuesta de error devuelta al agente debe ser informativa pero acotada: incluir el tipo de error, la causa probable y (cuando sea posible) una sugerencia de acción alternativa.

## Puntos críticos

- **Retry con backoff exponencial**: para fallos transitorios (timeouts, rate limits HTTP 429), implementar retry automático con backoff exponencial (1s, 2s, 4s) y máximo 3 intentos antes de reportar fallo al agente
- **Fallback de herramienta**: definir herramientas alternativas para operaciones críticas (p.ej., si `search_web_api` falla, intentar con `search_web_scraper`); el agente debe recibir la opción de alternativa en el mensaje de error
- **Error messages informativos**: la respuesta de error devuelta al LLM debe incluir el código de error, la causa probable en lenguaje natural y qué no debe intentar el agente ("Error 429: API rate limit reached. Do not retry for at least 60 seconds. Consider using cached results or a different search tool.")
- **Graceful degradation**: cuando una herramienta falla sin recuperación posible, el agente debe poder completar la tarea parcialmente y comunicar al usuario qué fue completado y qué no, en lugar de fallar en silencio
- **Logging de fallos de herramienta**: registrar cada fallo con timestamp, parámetros de entrada, código de error y contexto del agente en el momento del fallo; estos logs son la fuente principal para diagnosticar patrones de fallo en producción

## Para recordar

El manejo de errores de herramientas debe diseñarse antes de que ocurran los primeros fallos en producción: una política de error documentada y codificada en el sistema prompt del agente produce comportamiento predecible; la ausencia de política produce comportamiento emergente impredecible.
