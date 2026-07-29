# Módulo 12 – Capítulo 08 – Sección 02

# Tracing distribuido: seguimiento de una petición desde el usuario hasta el modelo y de vuelta

El tracing distribuido del sistema integrador captura el ciclo de vida completo de una petición: desde que el cliente HTTP envía la request al endpoint `/query` de FastAPI hasta que recibe la respuesta final. El span raíz `http.request` contiene el método HTTP, path y código de respuesta; sus spans hijo son: `auth.validate_jwt` (verificación del token), `input.validate` (validación Pydantic + lista negra de injection), `agent.run` (span raíz del agente que contiene todos los pasos ReAct), y `output.filter` (PII scanning de la respuesta). Dentro de `agent.run`, los spans hijo son: `agent.thought_{n}` (razonamiento del LLM en cada iteración), `tool.search_knowledge_base` (que contiene sus propios sub-spans: `embedding.query`, `qdrant.search` y `cohere.rerank`), y `agent.final_answer` (generación de la respuesta final con el modelo). Cada span incluye atributos: `duration_ms`, `tokens_used`, `model_name`, `error` (si aplica) y `trace_id` para correlación cross-service.

## Spans del trace distribuido

- `http.request`: span raíz con método, path, status_code, user_id y client_ip hasheada
- `auth.validate_jwt`: verificación de firma RS256, extracción de claims y validación de expiración
- `agent.run`: span contenedor del ciclo ReAct con atributos iterations_count y task_completed (boolean)
- `tool.search_knowledge_base`: span de herramienta con sub-spans embedding, qdrant.search y cohere.rerank
- `llm.generate`: span de generación LLM con model_name, prompt_tokens, completion_tokens y finish_reason

## Para recordar

El tracing distribuido no es solo para debugging — es la fuente de verdad sobre la latencia de cada componente en producción, y es el único mecanismo para identificar qué etapa del pipeline está causando una degradación de P95 sin instrumentación adicional.
