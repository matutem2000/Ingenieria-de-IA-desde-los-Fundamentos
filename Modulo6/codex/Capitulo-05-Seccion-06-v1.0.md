# Módulo 6 – Capítulo 05 – Sección 06

# Cierre: la recuperación es el cuello de botella más común en sistemas RAG

La evidencia empírica de equipos de AI Engineering que han publicado post-mortems y análisis de sus sistemas RAG es consistente: cuando un sistema RAG produce respuestas de baja calidad, la causa raíz en la mayoría de los casos es la recuperación deficiente, no la generación deficiente. Un LLM de alta calidad como Claude 3 Opus o GPT-4o no puede generar respuestas correctas si los chunks recuperados no contienen la información necesaria; por el contrario, incluso modelos de menor calidad generan respuestas aceptables cuando el contexto recuperado es preciso y relevante. Esta asimetría implica que el diseño y la optimización del retriever deben ser la primera prioridad en cualquier proyecto RAG: invertir en recuperación híbrida, reranking y evaluación continua del Recall@K antes de escalar el modelo de generación o añadir técnicas de prompt engineering. La arquitectura del retriever moderno de producción combina invariablemente: búsqueda vectorial de alta calidad con embeddings especializados, BM25 o SPLADE para matching léxico exacto, fusión RRF o weighted, reranking cross-encoder sobre los top-100, y un pipeline de evaluación automatizado que mide Recall@K y MRR en cada despliegue.

*"Si no puedes encontrar la información, ninguna cantidad de inteligencia en el sistema la puede generar."* — Ellen Voorhees, investigadora de NIST y coordinadora del benchmark TREC, sobre la primacía del retrieval en sistemas de question answering

## Principio rector

Optimizar primero el retriever, medir Recall@K con un dataset de evaluación representativo, y solo después de alcanzar un Recall@5 >0.75 invertir en optimizaciones del generador; el cuello de botella de la recuperación no puede ser resuelto con mejoras al prompt o al modelo de generación.
