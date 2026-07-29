# Módulo 5 – Capítulo 04 – Sección 03

# Integración con bases de datos relacionales y documentales

Las aplicaciones de IA frecuentemente necesitan leer datos de bases de datos relacionales (PostgreSQL, MySQL) o documentales (MongoDB, Elasticsearch) para enriquecer el contexto del LLM, y escribir los resultados del procesamiento de vuelta a esas mismas bases de datos como parte de un pipeline. El patrón más común en aplicaciones de chat empresarial es la recuperación de datos del usuario antes de construir el prompt: una consulta SQL que obtiene el perfil, historial de compras o estado de cuenta del usuario, serializada a texto o JSON, se inserta en el contexto del LLM para personalizar la respuesta. Las bases de datos vectoriales como pgvector (extensión de PostgreSQL), Qdrant o Chroma almacenan embeddings junto a la metadata del documento original, permitiendo búsqueda semántica sin salir del stack de base de datos existente en el caso de pgvector. La escritura de resultados del LLM en la base de datos debe tratarse con las mismas garantías de consistencia que cualquier escritura: usar transacciones donde corresponda, validar el schema del JSON de salida antes de insertarlo, y registrar en una tabla de auditoría los prompts y respuestas junto al registro procesado para trazabilidad.

## Aspectos técnicos de la integración con bases de datos

- pgvector con SQLAlchemy: instalar la extensión PostgreSQL `CREATE EXTENSION vector`, definir columnas `Vector(1536)` con SQLAlchemy y Alembic para migraciones, y ejecutar búsqueda por similitud coseno con `order by embedding <=> '[...]'::vector LIMIT 10`
- SQLAlchemy async para integración no bloqueante: usar `AsyncSession` de SQLAlchemy 2.0 con `asyncpg` para que las consultas a la base de datos no bloqueen el event loop de asyncio cuando se procesan múltiples requests concurrentes
- MongoDB para documentos semiestructurados: almacenar prompts, respuestas y metadata en colecciones MongoDB con un schema como `{prompt_id, model, input_tokens, output_tokens, latency_ms, prompt_text, response_text, created_at}` para análisis posterior con aggregation pipelines
- Connection pooling: configurar `pool_size` y `max_overflow` en SQLAlchemy, o el pool de motor de Motor (MongoDB async) para no agotar las conexiones de la base de datos bajo carga concurrente de requests de IA
- Caché de resultados con Redis: para queries frecuentes cuya respuesta del LLM es determinista (misma entrada → misma respuesta), cachear en Redis con TTL apropiado reduce la latencia y el costo de llamadas repetidas al modelo

## Buena práctica

Separar la capa de acceso a datos de la lógica de llamada al LLM con interfaces claras (repositorios o servicios de datos) permite testear cada capa independientemente con mocks y evita el acoplamiento entre el schema de la base de datos y los prompts.
