# Módulo 12 – Capítulo 02 – Sección 03

# ADR 002: estrategia de RAG — chunking, embedding y base vectorial

El ADR-002 documenta las decisiones centrales del pipeline RAG: la estrategia de chunking, el modelo de embedding y la base de datos vectorial. La evaluación de chunking comparó tamaños de 256, 512 y 1024 tokens con overlaps de 32, 64 y 128 tokens, midiendo context precision en el conjunto de evaluación RAGAS; el tamaño de 512 tokens con 64 de overlap fue seleccionado por maximizar context precision (0.81) mientras mantiene chunks con semántica coherente. Para embeddings, la comparación entre text-embedding-3-small (1536 dims, 0.00002 USD/1k tokens) y text-embedding-3-large (3072 dims, 0.00013 USD/1k tokens) mostró una diferencia de 0.04 puntos en recall@5 a un costo 6.5x mayor, justificando la elección del modelo small. La base vectorial Qdrant fue seleccionada sobre ChromaDB y Pinecone porque es la única que soporta búsqueda híbrida nativa (sparse BM25 + dense embeddings) con fusión RRF sin configuración adicional.

## Decisiones técnicas del pipeline RAG

- Chunking: RecursiveCharacterTextSplitter a 512 tokens con 64 de overlap, preservando límites de párrafo y código
- Estrategia de chunking semántico: fallback a chunking por párrafos para documentos con estructura markdown definida
- Modelo de embedding: text-embedding-3-small seleccionado por recall@5 de 0.82 a 6.5x menor costo que text-embedding-3-large
- Base vectorial: Qdrant v1.9 con índice HNSW (m=16, ef_construction=100) y cuantización escalar para reducción de memoria
- Búsqueda híbrida: RRF (k=60) combinando BM25 sparse y embeddings densos, con reranking Cohere sobre top-20 resultados

## Para recordar

Las decisiones de chunking y embedding se documentan en el ADR-002 porque tienen consecuencias directas en el costo de ingesta, el costo de query y la calidad de recuperación — cambiarlas requiere re-indexar toda la colección.
