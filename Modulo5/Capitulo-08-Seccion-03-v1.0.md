# Módulo 5 – Capítulo 08 – Sección 03

# Logging estructurado: prompts, respuestas, tokens y latencia

El logging estructurado en sistemas de IA va más allá del logging de aplicación tradicional: debe capturar el prompt completo enviado al modelo, la respuesta completa recibida, los tokens de entrada y salida, la latencia total y por componente, el modelo y versión usados, y los metadatos de contexto de negocio (usuario, sesión, feature, versión de prompt) para que cada log sea autónomamente diagnósticable sin necesidad de consultar otros sistemas. La estructura de un log de llamada al LLM como JSON tiene los campos críticos: `timestamp`, `request_id`, `trace_id`, `model`, `prompt_version`, `input_tokens`, `output_tokens`, `cached_tokens`, `latency_ms`, `cost_usd`, `finish_reason`, `user_id`, `session_id`. El almacenamiento de prompts y respuestas completos tiene implicaciones de volumen: una respuesta de 500 tokens a 4 bytes/token son 2KB por request; a 10.000 requests/día son 20MB/día o 7GB/año; decidir qué retener (prompts completos, solo metadata, muestra aleatoria) es una decisión de diseño con implicaciones de costo de almacenamiento y privacidad. Las plataformas de logging cloud (Datadog Logs, CloudWatch Logs, Google Cloud Logging) soportan consultas JSON estructuradas que permiten filtrar por `model = "claude-3-5-sonnet" AND cost_usd > 0.10` en segundos sobre millones de logs.

## Aspectos técnicos del logging estructurado para IA

- Logger JSON en Python: `import structlog; log = structlog.get_logger(); log.info("llm_call", model=model, input_tokens=usage.input_tokens, output_tokens=usage.output_tokens, latency_ms=elapsed, cost_usd=cost)` genera un JSON parseable automáticamente por cualquier plataforma de logging
- Nivel de detalle configurable: en desarrollo loggear el prompt completo y la respuesta completa; en producción loggear solo metadata (tokens, latencia, costo) por defecto, con logging completo activable via feature flag para debugging específico de un `user_id` o `session_id`
- Retención diferenciada: metadata de llamadas (tokens, latencia, costo, request_id) → retención de 90 días para análisis de tendencias; prompts y respuestas → retención de 7-30 días por privacidad y costo de almacenamiento; eventos de seguridad → retención de 1 año por compliance
- Logs de seguridad separados: loggear en un stream separado los intentos de jailbreak detectados, las respuestas que activaron filtros de contenido, y las consultas de usuarios con patrones anómalos, con retención extendida y acceso restringido por rol
- Correlación con métricas de negocio: añadir campos de negocio al log de la llamada al LLM (`feature: "email_assistant"`, `plan: "enterprise"`, `locale: "es-AR"`) permite analizar el costo y la calidad desagregado por feature y segmento de usuario

## Idea central

Los logs de producción de un sistema de IA son simultáneamente datos de operación (para diagnóstico de incidentes), datos de evaluación (para detectar degradaciones de calidad), y datos de entrenamiento potencial (para fine-tuning futuro); su calidad y estructura impactan múltiples equipos durante el ciclo de vida del sistema.
