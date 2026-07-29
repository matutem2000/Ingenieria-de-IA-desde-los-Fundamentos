# Módulo 12 – Capítulo 01 – Sección 03

# Arquitectura de alto nivel: componentes, flujos de datos y decisiones técnicas iniciales

La arquitectura del sistema integrador sigue un patrón de capas bien definidas: una capa de ingesta y preprocesamiento de documentos, una capa de almacenamiento vectorial con Qdrant, una capa de recuperación con búsqueda híbrida (BM25 + embeddings densos), un agente ReAct implementado con LangGraph, y una API REST con FastAPI como punto de entrada. El flujo de datos para una consulta de usuario atraviesa: validación de input, embedding de la query con text-embedding-3-small de OpenAI, recuperación de los top-k chunks con reranking mediante Cohere Rerank, construcción del contexto comprimido, razonamiento del agente y generación de respuesta con GPT-4o. El flujo de datos para la ingesta corre de forma asíncrona: parseo de documentos con LlamaParse, chunking con RecursiveCharacterTextSplitter a 512 tokens con 64 de overlap, embedding y upsert en Qdrant. Las decisiones técnicas iniciales de mayor impacto son la elección del modelo de embedding (latencia vs calidad) y el límite de tokens del contexto inyectado al LLM.

## Componentes principales

- Ingesta asíncrona: parser de documentos, chunker, embedder y upsert en Qdrant con idempotencia por hash de contenido
- Base vectorial: Qdrant con índices HNSW, colecciones por tipo de documento y filtros por metadatos (fecha, fuente, equipo)
- Pipeline de recuperación: búsqueda híbrida RRF (Reciprocal Rank Fusion) de BM25 + embeddings + reranking Cohere
- Agente ReAct: implementado con LangGraph, con herramientas search_knowledge_base, get_document y list_sources
- API REST: FastAPI con endpoints /query, /ingest y /health, autenticación JWT y rate limiting por usuario

## Para recordar

La arquitectura de alto nivel debe resolverse en papel antes de escribir la primera línea de código — cada componente introduce latencia, costo y complejidad operativa que deben justificarse explícitamente.
