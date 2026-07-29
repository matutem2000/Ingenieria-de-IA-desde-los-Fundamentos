# Módulo 6 – Capítulo 01 – Sección 04

# Tipos de RAG: naive RAG, advanced RAG y modular RAG

La taxonomía de sistemas RAG evolucionó de implementaciones simples hacia arquitecturas sofisticadas a medida que los equipos de ingeniería identificaron los puntos de fallo del enfoque inicial. El naive RAG, formalizado en el paper original de Lewis et al. (2020), implementa el ciclo básico de embed-retrieve-generate con búsqueda de similitud coseno y prompt de concatenación directa; sus limitaciones incluyen baja precision en recuperación, sensibilidad al tamaño del chunk y ausencia de mecanismos de verificación de relevancia. El advanced RAG incorpora mejoras en las tres etapas: pre-retrieval (query rewriting, HyDE, decomposición), retrieval (búsqueda híbrida, reranking con modelos cross-encoder) y post-retrieval (compresión de contexto, selección de chunks relevantes); frameworks como LlamaIndex y LangChain implementan estos patrones como módulos configurables. El modular RAG (propuesto por Yunfan Gao et al., 2023) va más allá al conceptualizar el sistema como un conjunto de módulos intercambiables: un Search Module, un Memory Module, un Fusion Module y un Routing Module que pueden reconfigurarse dinámicamente según el tipo de consulta.

## Características técnicas de cada variante

- Naive RAG: implementación lineal de embed-retrieve-generate sin optimizaciones; Recall@5 típico de 40–55% en benchmarks estándar como BEIR; adecuado solo para corpus pequeños y homogéneos
- Advanced RAG pre-retrieval: técnicas de query transformation (HyDE genera documentos hipotéticos, step-back prompting extrae conceptos generalizados) que mejoran el vector de consulta antes de la búsqueda
- Advanced RAG post-retrieval: reranking con modelos cross-encoder (ms-marco-MiniLM-L6-v2, Cohere Rerank) que re-ordena los chunks recuperados por relevancia semántica real, no por similitud coseno
- Modular RAG: desacoplamiento de responsabilidades en módulos independientes que permiten sustituir el retriever (vectorial, BM25, knowledge graph) sin modificar el pipeline de generación
- Routing dinámico en Modular RAG: clasificador que dirige cada consulta al módulo de recuperación más apropiado según la categoría detectada (factual, comparativa, temporal, de síntesis)
- Self-RAG como extensión avanzada: el LLM emite tokens especiales (ISREL, ISSUP, ISUSE) para decidir dinámicamente si recuperar información adicional durante la generación, mejorando coherencia y trazabilidad

## Para recordar

Elegir el nivel de complejidad del sistema RAG debe estar guiado por métricas de evaluación reales sobre el corpus y las queries objetivo, no por la disponibilidad de frameworks o la complejidad percibida de las técnicas.
