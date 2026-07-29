# Módulo 12 – Capítulo 04 – Sección 02

# Implementación de herramientas: contratos de interfaz, manejo de errores y logging

Cada herramienta del agente es una función Python decorada con `@tool` de LangChain, con un docstring que el LLM usa para decidir cuándo llamarla y un esquema Pydantic que define y valida los argumentos. El contrato de interfaz de `search_knowledge_base` acepta `query: str` (longitud máxima 500 caracteres), `filters: Optional[dict]` con campos `document_type`, `team` y `date_range`, y `top_k: int` (valor por defecto 5, máximo 10); devuelve una lista de objetos `Document` con campos `content`, `source_url`, `score` y `metadata`. El manejo de errores de cada herramienta sigue el patrón de retornar un objeto de error estructurado en lugar de lanzar excepciones — esto permite al agente razonar sobre el fallo y decidir si reintenta con parámetros diferentes o informa al usuario. Cada llamada a herramienta emite un log estructurado JSON con `tool_name`, `args`, `duration_ms`, `result_count` y `trace_id` para trazabilidad end-to-end con OpenTelemetry.

## Aspectos de implementación de herramientas

- Decorador @tool con docstring descriptivo: el LLM infiere cuándo usar la herramienta desde la descripción en lenguaje natural
- Validación de inputs: Pydantic BaseModel para cada herramienta con Field validators y longitudes máximas configuradas
- Manejo de errores: retorno de ToolError(error_code, message, retry_suggested) en lugar de excepciones sin capturar
- Timeout por herramienta: asyncio.wait_for con timeout de 5 segundos, con ToolTimeoutError si la herramienta excede el límite
- Logging estructurado: JSON con trace_id, tool_name, args_hash, duration_ms, result_size y status (success/error/timeout)

## Buena práctica

Las herramientas del agente deben retornar errores informativos en lugar de propagar excepciones — el agente necesita contexto sobre el fallo para razonar si debe reintentar, usar otra herramienta o informar la limitación al usuario.
