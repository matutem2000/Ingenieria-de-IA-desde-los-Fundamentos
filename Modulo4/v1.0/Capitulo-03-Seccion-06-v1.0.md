# Módulo 4 – Capítulo 03 – Sección 06

## Resumen

Este capítulo desarrolló la arquitectura RAG como un ecosistema de cuatro dominios interdependientes, cada uno con sus propias decisiones técnicas, herramientas y criterios de calidad. La comprensión de ese ecosistema completo es lo que diferencia a un AI Architect que puede diseñar un sistema RAG productivo de un desarrollador que conecta una API de LLM a una base vectorial.

El pipeline de ingesta establece la calidad del conocimiento disponible. Las decisiones de extracción, limpieza y chunking son las de mayor impacto en la calidad final del sistema, y frecuentemente son subestimadas a favor de la experimentación con modelos de lenguaje. El chunking no es un parámetro técnico menor: la estrategia correcta depende del tipo de documento, de la distribución de consultas esperadas y de la ventana de contexto del modelo receptor. Cambiar la estrategia de chunking en producción requiere re-indexar toda la base de conocimiento, lo que lo convierte en una decisión de alto costo de reversión.

La recuperación inteligente determina qué fracción del conocimiento disponible llega a cada consulta. La búsqueda híbrida (BM25 + embeddings) con reranking cross-encoder es el estándar de producción actual para sistemas que requieren alta precisión. La selección de la base vectorial — Pinecone, Weaviate, Qdrant, pgvector — debe realizarse con criterios de escala, latencia, modelo operativo del equipo y costo, no por preferencia tecnológica. La evaluación con métricas RAGAS (context recall, context precision, faithfulness, answer relevancy) transforma la calidad de recuperación de una impresión subjetiva en un indicador medible.

La generación de respuestas controla cómo el modelo de lenguaje utiliza el contexto recuperado. El grounding, las citas estructuradas y la escalada a humano cuando la confianza es baja son mecanismos que protegen la confiabilidad del sistema. La trazabilidad de cada respuesta — qué documentos la produjeron, qué prompt fue enviado — es un requisito no funcional de primera categoría en contextos empresariales.

La operación y monitoreo cierra el ciclo. Latencia por etapa, calidad de recuperación periódica, costo por consulta, actualización del conocimiento y auditoría de consultas son las dimensiones que determinan si el sistema mantiene su calidad y viabilidad económica a lo largo del tiempo. Plataformas como LangSmith, Langfuse y Phoenix de Arize convierten estos datos en observabilidad accionable.

La conclusión central de este capítulo es que un sistema RAG productivo es tan robusto como su componente más débil. Un pipeline de ingesta excelente no compensa una recuperación de baja precisión. Una recuperación precisa no compensa un proceso de generación que mezcla el contexto con el conocimiento paramétrico del modelo. Y ninguno de los dos compensa la ausencia de operación sistemática. El modelo de lenguaje es el componente más visible del sistema, pero raramente es el más determinante para su calidad en producción.

El Capítulo 04 eleva la complejidad arquitectónica un nivel: en lugar de sistemas que recuperan y generan, exploraremos sistemas que planifican, deciden y ejecutan acciones en el mundo real. Las arquitecturas de agentes son la siguiente frontera para el AI Architect.

---

*"Antes de optimizar el modelo, optimice la calidad de los datos y del proceso de recuperación. En la mayoría de los proyectos, esa decisión produce un mayor impacto que cambiar de LLM."*
— Principio del Arquitecto de RAG, adoptado de la experiencia operativa en sistemas de recuperación a escala
