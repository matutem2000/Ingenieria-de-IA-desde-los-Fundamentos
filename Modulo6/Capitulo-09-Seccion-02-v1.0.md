# Módulo 6 – Capítulo 09 – Sección 02

# Optimización del retriever: ajuste de K, reranking y filtros de relevancia

La optimización del retriever es la palanca de mayor impacto en la mejora de la calidad de un sistema RAG, y debe abordarse sistemáticamente evaluando el impacto de cada cambio sobre el dataset de evaluación antes de implementarlo en producción. El parámetro K (número de chunks recuperados) tiene un impacto directo en Recall@K: aumentar K siempre mejora el Recall (hay más oportunidades de incluir el chunk relevante) pero aumenta el costo de tokens de contexto para el LLM y puede introducir el "lost-in-the-middle" effect donde el LLM pierde atención en chunks ubicados en posiciones medias del contexto extenso. El valor óptimo de K es específico del caso de uso: sistemas de QA factual con respuestas en un único chunk suelen funcionar bien con K=3–5; sistemas de síntesis que requieren integrar información de múltiples fuentes necesitan K=10–20. El reranking es la optimización de mayor ROI: añadir un cross-encoder como Cohere Rerank o BGE Reranker que re-ordena los top-100 chunks recuperados mejora la Precision@5 (los 5 chunks enviados al LLM) en 15–25% sin cambiar el sistema de recuperación subyacente.

## Técnicas de optimización del retriever

- Ajuste experimental de K: medir Recall@K para K=1,3,5,10,15,20 sobre el golden dataset; trazar la curva Recall@K vs. K; el "knee" de la curva (punto donde el incremento marginal de Recall por unidad adicional de K disminuye drásticamente) indica el K óptimo para balancear cobertura y costo de contexto
- Reranking two-stage: first-stage retrieval de top-50 o top-100 chunks con búsqueda vectorial/híbrida rápida, second-stage reranking con cross-encoder; medir Precision@5 antes y después del reranking; mejoras típicas de 15–25 puntos porcentuales en Precision@5; justifica el overhead de latencia de 200–500ms del reranker
- Umbral de relevancia (score threshold): rechazar chunks con score de similitud coseno por debajo de un umbral (típicamente 0.6–0.75) para evitar incluir en el contexto chunks que son los "menos malos" en un corpus que no tiene información relevante; mejora faithfulness al reducir chunks irrelevantes en el contexto
- Maximal Marginal Relevance (MMR): algoritmo de diversificación que selecciona los K chunks que maximizan la relevancia con la query y minimizan la redundancia entre ellos; útil para queries que requieren cobertura de múltiples aspectos; implementado en LangChain con `MMRRetriever`; parámetro lambda controla balance entre relevancia y diversidad
- Búsqueda híbrida con peso alpha dinámico: ajustar el peso relativo de dense vs. sparse retrieval (parámetro alpha en la fusión RRF o weighted) según el tipo de query detectado; queries léxicamente específicas (nombres propios, códigos) usan alpha bajo (más peso a BM25); queries semánticas usan alpha alto (más peso al vectorial)
- Fine-tuning del modelo de embedding sobre datos de relevancia: si el análisis de errores muestra que el retriever falla sistemáticamente en un tipo específico de queries, generar datos de fine-tuning contrastivo (triplas de query, chunk_positivo, chunk_negativo_difícil) del corpus de dominio y hacer fine-tuning del modelo de embedding con sentence-transformers

## Para recordar

Medir el impacto de cada optimización del retriever sobre el golden dataset completo antes de combinar múltiples optimizaciones; la combinación de K óptimo + reranking + threshold de relevancia puede acumularse a una mejora de 20–35 puntos en Precision@5.
