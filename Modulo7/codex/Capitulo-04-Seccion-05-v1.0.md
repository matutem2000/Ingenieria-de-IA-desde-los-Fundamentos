# Módulo 7 – Capítulo 04 – Sección 05

# Vectorización de memorias: búsqueda semántica sobre el historial del agente

La vectorización de memorias convierte unidades de información —fragmentos de conversaciones, hechos extraídos, resultados de tareas— en embeddings de alta dimensión (1536 dimensiones en text-embedding-3-large de OpenAI, 1024 en voyage-3 de Anthropic) que capturan el significado semántico del texto, permitiendo recuperar memorias relevantes mediante búsqueda por similaridad coseno en lugar de búsqueda exacta por keywords. Este enfoque permite al agente recuperar memorias contextualmene relevantes aunque usen terminología diferente a la query actual: "problemas con la autenticación" puede recuperar un episodio anterior sobre "errores de login" sin coincidencia textual. Las implementaciones de vectorstore más usadas en producción incluyen Pinecone (SaaS, ANN con HNSW), Weaviate (self-hosted o cloud, multimodal), Chroma (embebido en proceso, desarrollo local) y pgvector (extensión de PostgreSQL para almacenamiento vectorial en la misma base de datos relacional). La calidad de la recuperación depende tanto del modelo de embedding elegido como del chunking strategy aplicado a las memorias.

## Aspectos técnicos

- **Chunking strategy**: dividir memorias largas (transcripciones de sesión, documentos) en fragmentos de tamaño óptimo (256-512 tokens) con overlap (10-20%) para no perder contexto en los límites de chunk; el tamaño óptimo depende del modelo de embedding y del tipo de consulta esperada
- **Modelo de embedding**: el modelo de embedding debe elegirse según el tipo de contenido (texto general, código, multilingüe); text-embedding-3-large para texto en inglés, multilingual-e5-large para contenido multilingüe, code2vec o voyage-code-2 para memorias de código
- **Filtrado por metadata antes del ANN search**: aplicar filtros hard (user_id, date_range, type) antes de la búsqueda vectorial para reducir el espacio de búsqueda y mejorar precisión; la mayoría de vectorstores soportan filtrado pre-ANN vía metadata fields
- **Hybrid search**: combinar búsqueda vectorial (semántica) con búsqueda keyword (BM25) usando RRF (Reciprocal Rank Fusion) para mejorar recall; Weaviate y Pinecone soportan hybrid search nativo; especialmente útil cuando las queries incluyen identificadores exactos (nombres propios, IDs)
- **Re-ranking post-retrieval**: aplicar un cross-encoder (p.ej. cohere-rerank-3, bge-reranker-v2-m3) sobre los top-k candidatos recuperados para re-ordenarlos por relevancia real antes de inyectarlos en el contexto; mejora precision@3 en 15-30% sobre retrieval puro

## Buena práctica

Evaluar la calidad del retrieval de memorias con un conjunto de queries de test antes de desplegar en producción: medir precision@3 y recall@10 sobre un conjunto anotado de (query, memorias_relevantes); un retrieval con precision@3 < 0.7 produce memorias irrelevantes en el contexto que confunden más que ayudan.
