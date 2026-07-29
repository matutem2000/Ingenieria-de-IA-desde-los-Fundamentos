# Módulo 12 – Capítulo 03 – Sección 04

# Pipeline de recuperación: búsqueda híbrida, reranking y compresión de contexto

El pipeline de recuperación implementa tres etapas: búsqueda híbrida para obtener candidatos, reranking para ordenar por relevancia semántica y compresión para ajustar el contexto al límite de tokens del LLM. La búsqueda híbrida combina embeddings densos (text-embedding-3-small) y embeddings sparse BM25 usando Reciprocal Rank Fusion con parámetro k=60; RRF asigna un score 1/(k+rank) a cada documento en cada lista y suma los scores, produciendo un ranking fusionado que supera tanto la búsqueda densa como la BM25 sola en recall@10. Los top-20 resultados de la búsqueda híbrida pasan por Cohere Rerank (rerank-english-v3.0), que evalúa la relevancia semántica de cada chunk respecto a la query original y los reordena; solo los top-5 chunks después del reranking se incluyen en el contexto. La compresión de contexto con LLMChainExtractor reduce cada chunk a las frases más relevantes para la query, disminuyendo el uso de tokens en el prompt entre 30% y 50%.

## Etapas del pipeline de recuperación

- Embedding de query: text-embedding-3-small aplicado a la query normalizada, con cache de 5 minutos para queries repetidas
- Búsqueda híbrida: RRF k=60 sobre búsqueda densa (top-20) y BM25 sparse (top-20), retornando top-20 fusionados
- Reranking: Cohere rerank-english-v3.0 sobre top-20 candidatos, seleccionando top-5 por relevance_score >= 0.3
- Compresión de contexto: LLMChainExtractor con GPT-3.5-turbo para extraer frases relevantes y reducir tokens en 30-50%
- Construcción del prompt: contexto comprimido + query + system prompt con instrucciones de grounding y cita de fuentes

## Para recordar

El reranking es el componente con mayor impacto en la calidad del contexto recuperado — eliminar el paso de reranking en favor de más velocidad suele degradar faithfulness entre 0.10 y 0.15 puntos en RAGAS.
