# Módulo 6 – Capítulo 04 – Sección 06

# Cierre: el chunking es la decisión de ingeniería más impactante en RAG

La investigación empírica y la experiencia de producción coinciden en que el chunking y la preparación de documentos tienen mayor impacto en la calidad final de un sistema RAG que la elección del modelo de embedding o del LLM generador. Un sistema con chunking bien diseñado, metadatos ricos y estrategia de enriquecimiento apropiada puede compensar parcialmente un modelo de embedding de segunda línea, mientras que el mejor modelo de embedding del mercado no puede recuperar información que fue destruida por un chunking que cortó las unidades semánticas en el lugar equivocado. El chunking es además la etapa del pipeline que más varía entre dominios: el chunking óptimo para contratos legales (por cláusula, con identificador de artículo como metadato) es completamente distinto al óptimo para documentación técnica de software (por función o endpoint, preservando la firma como metadato), o para artículos periodísticos (por párrafo, con el lead de la noticia como contexto prepended). Esta especificidad de dominio implica que el chunking debe ser diseñado y validado por alguien con conocimiento del corpus y de cómo los usuarios formulan sus queries, no elegido por defecto del framework.

*"Garbage in, garbage out. En ningún sistema de recuperación de información esto es más verdad que en la calidad del preprocesamiento: cualquier pérdida de información en la transformación del documento original al fragmento indexado es irrecuperable en tiempo de consulta."* — Karen Spärck Jones, pionera de la recuperación de información y del cálculo de TF-IDF

## Principio rector

Invertir tiempo en el diseño y la evaluación experimental del chunking antes de optimizar cualquier otro componente del sistema RAG: la calidad del índice determina el techo de calidad de toda la cadena de recuperación y generación.
