# Módulo 11 – Capítulo 06 – Sección 03

# RAG sobre datos estructurados y no estructurados en el enterprise

Los datos enterprise se distribuyen entre dos grandes categorías con propiedades de retrieval fundamentalmente distintas: datos no estructurados (documentos PDF, presentaciones PowerPoint, correos electrónicos, tickets de soporte, transcripciones de reuniones, contratos en Word) que se indexan como texto mediante chunking y embedding para búsqueda vectorial, y datos estructurados (tablas de bases de datos relacionales, data warehouses, hojas de cálculo, APIs de sistemas ERP) que se consultan mediante SQL o APIs específicas y cuya integración con RAG requiere un enfoque diferente al del retrieval vectorial clásico. Para datos estructurados, el patrón Text-to-SQL — donde el LLM convierte la pregunta en lenguaje natural en una query SQL ejecutable sobre la base de datos — permite que el sistema RAG consulte dinámicamente el data warehouse sin requerir indexación previa, con la ventaja de que los datos están siempre actualizados y la desventaja de que el LLM puede generar SQL incorrecto o costoso si no se implementan guardrails específicos (validación de la query SQL antes de ejecutarla, límites de tiempo de ejecución, restricciones de tablas y columnas accesibles). El enfoque más robusto para datos enterprise mixtos es el RAG híbrido: un router que analiza la pregunta del usuario y determina si debe recuperar contexto del índice vectorial (para preguntas sobre política interna, contratos, documentación técnica), ejecutar Text-to-SQL (para preguntas sobre métricas, cifras, y datos transaccionales), o combinar ambos (para preguntas que requieren tanto información factual de documentos como datos cuantitativos de bases de datos).

## Componentes del RAG sobre datos heterogéneos

- Pipeline de chunking para no estructurados: estrategia de chunking semántico (LangChain SemanticChunker, LlamaIndex SentenceWindowNodeParser) que produce chunks de 512-1024 tokens con overlap de 20%, preservando el contexto entre chunks adyacentes
- Text-to-SQL con schema masking: el LLM recibe solo el schema relevante (tablas y columnas relacionadas con el dominio de la pregunta), no el schema completo de la base de datos, para reducir el riesgo de queries sobre tablas no autorizadas
- Validación de SQL generado: ejecución en modo EXPLAIN antes de la ejecución real, verificación de que la query solo accede a tablas en el whitelist configurado, y timeout de 5 segundos para prevenir queries costosas
- Reranker cross-encoder: modelo de reranking (ms-marco-MiniLM-L-12-v2, Cohere Rerank, Jina Rerank) que reordena los chunks recuperados por similitud vectorial usando una score de relevancia más precisa antes de incluirlos en el contexto del LLM
- Metadata filtering por tipo de fuente: permitir al usuario o al sistema especificar si la respuesta debe basarse en documentos de un tipo específico (solo políticas internas, solo contratos firmados en 2024, solo datos del Q3), usando los campos de metadata del índice vectorial

## Idea central

El RAG híbrido que combina retrieval vectorial para datos no estructurados con Text-to-SQL para datos estructurados es la arquitectura que cubre el espectro completo de necesidades de información de un enterprise, donde la mayoría de las preguntas de negocio requieren ambos tipos de contexto.
