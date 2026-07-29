# Módulo 12 – Capítulo 01 – Sección 03

## Arquitectura de alto nivel: componentes, flujos de datos y estructura del repositorio

Un sistema de IA en producción puede describirse en términos de sus componentes, pero solo se comprende en términos de sus flujos de datos. La pregunta que la arquitectura de alto nivel debe responder no es "¿qué piezas tiene el sistema?" sino "¿cómo viaja la información desde el documento original hasta la respuesta del usuario?" Esa pregunta tiene dos respuestas correspondientes a los dos flujos principales del sistema: el flujo de ingesta, que transforma documentos en vectores indexados, y el flujo de consulta, que transforma la pregunta de un usuario en una respuesta fundamentada en el conocimiento disponible.

El flujo de ingesta es asíncrono y tolerante a fallos. Un usuario o un proceso automatizado envía un documento al endpoint `/ingest` de la API; el endpoint valida el payload, encola la tarea en Redis mediante Celery y devuelve un `task_id` de seguimiento. El worker Celery procesa la tarea en background: el documento pasa por el parser correspondiente a su tipo (LlamaParse para PDF, python-markdown para Markdown, BeautifulSoup para HTML de Confluence), luego por el chunker RecursiveCharacterTextSplitter configurado a 512 tokens con 64 de overlap, luego por el embedder text-embedding-3-small de OpenAI, y finalmente el vector resultante se hace upsert en la colección `knowledge_base` de Qdrant junto con sus metadatos de payload. Un hash SHA-256 del contenido del documento detecta documentos duplicados o sin cambios, evitando re-indexaciones costosas.

El flujo de consulta es síncrono y evaluable. El usuario envía una petición al endpoint `/query` con su query en texto libre; el middleware de autenticación verifica el JWT y extrae los claims de autorización; el InputValidator aplica tres capas de validación (schema Pydantic, lista negra de injection, clasificador de intent); el agente LangGraph recibe la query validada y comienza su ciclo ReAct: llama a `search_knowledge_base`, que internamente embedda la query con text-embedding-3-small, ejecuta búsqueda híbrida RRF en Qdrant y aplica reranking con Cohere Rerank sobre los top-20 resultados; el agente recibe los top-5 chunks, razona sobre ellos y decide si necesita búsquedas adicionales o puede construir la respuesta; GPT-4o genera la respuesta final citando las fuentes; el OutputFilter escanea la respuesta en busca de PII antes de devolverla al usuario.

La arquitectura sigue un patrón de capas bien definidas con interfaces explícitas entre cada capa. Esto no es solo una decisión estética: permite reemplazar cualquier componente sin afectar al resto. Si se necesita cambiar text-embedding-3-small por un modelo de embedding fine-tuned, solo cambia el implementador de la interfaz de embedding — el agente, el chunker y el filtro de output no saben nada del cambio. Si se necesita sustituir Cohere por un reranker local, solo cambia el reranker — el pipeline de búsqueda híbrida lo llama con la misma interfaz.

Antes de escribir la primera línea de código, el repositorio debe tener una estructura de directorios que refleje la arquitectura del sistema. Esta estructura actúa como mapa del código para cualquier ingeniero que llegue al proyecto:

```
technical-assistant/
├── docs/
│   ├── adr/                    # ADR-001 al ADR-004
│   └── architecture.md         # Diagrama Mermaid de alto nivel
├── src/
│   ├── api/                    # FastAPI: endpoints, middleware, schemas
│   ├── agent/                  # LangGraph: grafo, nodos, herramientas
│   ├── rag/                    # Pipeline RAG: ingesta, chunking, retrieval
│   ├── security/               # InputValidator, OutputFilter, auth
│   └── observability/          # OpenTelemetry instrumentation
├── tests/
│   ├── unit/                   # Tests por componente con mocks
│   ├── integration/            # Tests con dependencias reales (Qdrant test)
│   └── evaluation/             # Scripts RAGAS, golden dataset, red teaming
├── infra/
│   ├── terraform/              # Módulos networking, compute, services
│   └── k8s/                   # Manifests Kubernetes y Argo Rollouts
├── .github/
│   └── workflows/              # CI/CD pipeline con stages build/test/evaluate/deploy
├── docker-compose.yml          # Stack de desarrollo local completo
├── Dockerfile                  # Multi-stage build para producción
└── .env.example                # Variables de entorno documentadas
```

Esta estructura separa el código de aplicación (`src/`), los tests por tipo, la infraestructura como código (`infra/`) y la documentación de decisiones (`docs/adr/`). Cada directorio tiene una responsabilidad única y sus dependencias fluyen en una sola dirección: `api/` depende de `agent/` y `security/`, `agent/` depende de `rag/`, `rag/` no depende de ningún módulo interno — solo de servicios externos.

## Componentes principales del sistema

- **Ingesta asíncrona**: parser de documentos por tipo MIME, chunker RecursiveCharacterTextSplitter, embedder text-embedding-3-small, upsert en Qdrant con idempotencia por hash SHA-256 del contenido. Cola Celery + Redis para procesamiento tolerante a fallos.
- **Base vectorial Qdrant**: colección `knowledge_base` con índices HNSW (m=16, ef_construction=100), payload indexes en `document_type`, `team` e `ingested_at`, y vectores sparse BM25 para soporte de búsqueda híbrida nativa.
- **Pipeline de recuperación**: búsqueda híbrida RRF (k=60) sobre embeddings densos y BM25 sparse, reranking Cohere rerank-english-v3.0 sobre top-20, selección de top-5 y compresión de contexto con LLMChainExtractor.
- **Agente ReAct con LangGraph**: grafo de estado con nodos `reason`, `act`, `observe` y `respond`, herramientas `search_knowledge_base`, `get_document_by_id` y `list_available_sources`, max_iterations=5 con fallback a respuesta parcial.
- **API REST FastAPI**: endpoints `/query`, `/ingest` y `/health`, middleware de autenticación JWT RS256, rate limiting por usuario, InputValidator multicapa y OutputFilter con detección de PII.

> **Nota del Arquitecto**: La estructura de directorios del repositorio comunica las decisiones arquitectónicas antes de que el lector abra un solo archivo. Un directorio `security/` al mismo nivel que `agent/` dice "la seguridad es un componente de primera clase, no un afterthought". Un directorio `evaluation/` con los scripts RAGAS dice "la evaluación es parte del proceso de desarrollo, no una verificación final". Dedicar 15 minutos a diseñar esta estructura antes del primer commit ahorra semanas de refactoring posterior.

La arquitectura de alto nivel debe resolverse en papel antes de escribir la primera línea de código. Cada componente introduce latencia, costo y complejidad operativa que deben justificarse explícitamente. Las decisiones técnicas más impactantes — modelo de embedding, framework agéntico, base vectorial — se documentan en los ADRs del Capítulo 2, que registran no solo qué se eligió sino por qué, qué alternativas se evaluaron y qué consecuencias se anticipan.

**Para recordar**: La arquitectura de alto nivel y la estructura del repositorio son artefactos de diseño previos a la implementación — el árbol de directorios es el mapa del sistema que permite a cualquier ingeniero orientarse desde el primer día.
