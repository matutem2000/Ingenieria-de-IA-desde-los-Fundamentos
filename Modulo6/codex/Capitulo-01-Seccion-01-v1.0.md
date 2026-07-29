# Módulo 6 – Capítulo 01 – Sección 01

# Qué es RAG y por qué existe: limitaciones de los LLM sin contexto externo

Los Large Language Models como GPT-4, Claude o Llama 3 son entrenados sobre snapshots estáticos de datos que tienen una fecha de corte fija; una vez desplegados, su conocimiento no se actualiza y no tienen acceso a documentos privados o sistemas internos de la organización. Esta limitación estructural genera dos clases de fallos críticos: la alucinación de hechos que el modelo no conoce pero sintetiza con confianza aparente, y la imposibilidad de responder sobre información post-entrenamiento o propietaria. Retrieval-Augmented Generation (RAG), introducido por Lewis et al. en 2020, resuelve este problema convirtiendo cada inferencia en una consulta activa a una base de conocimiento externa, inyectando los fragmentos relevantes en el contexto del prompt antes de la generación. El resultado es un sistema que combina la capacidad de razonamiento lingüístico del LLM con acceso dinámico a fuentes verificables y actualizables.

## Limitaciones fundamentales de los LLM sin recuperación externa

- Knowledge cutoff: los pesos del modelo encodifican conocimiento hasta la fecha de entrenamiento, haciendo imposible responder sobre eventos o documentos posteriores sin fine-tuning o retrieval
- Context window como único canal de conocimiento en inferencia: sin RAG, el único modo de inyectar información específica es incluirla manualmente en el prompt, lo cual no escala a corpora de millones de documentos
- Hallucination de hechos específicos: el modelo interpola entre patrones estadísticos y puede fabricar nombres, fechas, cifras o citas con alta fluidez pero baja fidelidad cuando no tiene evidencia en sus pesos
- Opacidad de fuentes: un LLM sin RAG no puede citar la fuente de una afirmación porque no la recupera; RAG hace el conocimiento trazable y auditable por diseño
- Costo prohibitivo de actualización por fine-tuning continuo: reentrenar o hacer fine-tuning del modelo para incorporar nuevos documentos tiene un costo computacional y operativo que RAG evita al externalizar el conocimiento al índice

## Para recordar

RAG existe porque la separación entre conocimiento paramétrico (pesos del modelo) y conocimiento no-paramétrico (índice externo) es la única arquitectura que permite actualizaciones de conocimiento a costo operativo razonable sin modificar el modelo.
