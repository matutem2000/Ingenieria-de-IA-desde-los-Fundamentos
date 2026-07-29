# Módulo 12 – Capítulo 04 – Sección 03

# Integración RAG-agente: el agente usa el RAG como herramienta de recuperación

La integración entre el agente y el pipeline RAG se realiza a través de la herramienta `search_knowledge_base`, que encapsula todo el pipeline de recuperación — embedding de query, búsqueda híbrida en Qdrant, reranking con Cohere y compresión de contexto — y devuelve al agente una lista de documentos relevantes ya procesados. Esta arquitectura desacopla el agente del pipeline RAG: el agente no sabe si el retrieval usa BM25 o embeddings densos, ni si hay reranking o no; solo sabe que la herramienta devuelve los chunks más relevantes para su query. El desacoplamiento permite actualizar el pipeline RAG (cambiar el modelo de embedding, ajustar los parámetros de chunking, agregar un step de compresión adicional) sin modificar el código del agente. La herramienta también implementa query reformulation: si la query original del usuario es ambigua o muy general, el agente puede generar una query más específica para el retrieval basándose en el contexto de la conversación.

## Puntos de integración RAG-agente

- Interfaz de herramienta: search_knowledge_base abstrae el pipeline RAG completo detrás de un contrato de función tipada
- Query reformulation: el agente puede llamar search_knowledge_base con queries refinadas distintas a la query original del usuario
- Multi-step retrieval: el agente puede llamar la herramienta múltiples veces con queries distintas y fusionar los resultados
- Filtros contextuales: el agente infiere filtros de metadatos (document_type, team) desde el contexto de la conversación
- Gestión de contexto: el agente lleva registro de los documentos ya recuperados para evitar búsquedas redundantes en el mismo turno

## Para recordar

Encapsular el pipeline RAG detrás de una herramienta con contrato tipado es el patrón de integración correcto — permite evolucionar el pipeline de forma independiente y testear el agente con mocks del retrieval sin dependencias externas.
