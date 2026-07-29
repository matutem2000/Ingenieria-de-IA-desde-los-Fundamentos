# Módulo 12 – Capítulo 01 – Sección 04

# Stack tecnológico: selección justificada de modelos, bases de datos, frameworks y herramientas

Cada componente del stack del proyecto final se selecciona con criterios técnicos explícitos, no por popularidad. El modelo de lenguaje principal es GPT-4o (gpt-4o-2024-08-06) justificado por su ventana de contexto de 128k tokens, su rendimiento en tareas de razonamiento técnico y su soporte a function calling con JSON mode estructurado; la alternativa evaluada y descartada fue Claude 3.5 Sonnet por latencia levemente mayor en el percentil P99 para este caso de uso. Para embeddings se usa text-embedding-3-small (1536 dimensiones) en lugar de text-embedding-3-large porque ofrece 90% del rendimiento a un tercio del costo, según benchmarks en MTEB. Qdrant se selecciona sobre Pinecone por soportar despliegue local con Docker para desarrollo, filtros por payload arbitrarios sin costo adicional, y API compatible tanto con gRPC como HTTP REST.

## Selección justificada del stack

- LLM: GPT-4o (gpt-4o-2024-08-06) por context window de 128k, JSON mode nativo y latencia P95 < 2s medida en benchmark interno
- Embeddings: text-embedding-3-small (OpenAI) seleccionado sobre ada-002 por 62% de mejora en MTEB con 5x menor dimensionalidad comprimida
- Base vectorial: Qdrant v1.9 por soporte de búsqueda híbrida nativa (sparse + dense), filtros por payload y despliegue Docker sin licencia
- Framework agéntico: LangGraph sobre LangChain por soporte de grafos de estado con ciclos, checkpointing y control granular del flujo
- Infraestructura: FastAPI + Uvicorn + Docker Compose (dev) / Kubernetes (prod), observabilidad con OpenTelemetry + Grafana

## Buena práctica

Documentar la alternativa evaluada y descartada para cada componente del stack es parte de la decisión técnica — sin ese registro, el equipo repetirá la evaluación en cada revisión de arquitectura.
