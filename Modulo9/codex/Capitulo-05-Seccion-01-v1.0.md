# Módulo 9 – Capítulo 05 – Sección 01

# RAG poisoning: inyección de documentos maliciosos en el índice vectorial

RAG poisoning es el ataque en el que un adversario introduce documentos maliciosos en el corpus del sistema RAG (Retrieval-Augmented Generation) con el objetivo de que esos documentos sean recuperados como contexto por el LLM y ejecuten instrucciones adversariales o proporcionen información falsa presentada como fuente confiable. A diferencia de la prompt injection directa, RAG poisoning ataca el pipeline de ingestión de datos —que frecuentemente tiene menos controles de seguridad que el endpoint de inferencia— y sus efectos son persistentes: el documento malicioso permanece en el índice hasta que es detectado y eliminado, potencialmente afectando miles o millones de requests. El ataque es especialmente efectivo porque el LLM recibe los documentos recuperados como "contexto confiable" del sistema, no como "input de usuario no confiable", lo que reduce la resistencia del modelo a seguir instrucciones embebidas en esos documentos. Los vectorstores como Pinecone, Weaviate, Chroma y pgvector que alimentan sistemas RAG en producción son superficies de ataque críticas que requieren controles equivalentes a los de una base de datos de producción.

## Aspectos técnicos

- Vectores de inyección de documentos: APIs de ingestión de documentos sin autenticación adecuada, pipelines de web scraping que indexan automáticamente páginas modificadas por el atacante, uploads de usuarios que son indexados sin validación de contenido, y contribuciones a bases de conocimiento compartidas (wikis internas, SharePoints)
- Diseño del documento malicioso: el atacante debe construir un documento que sea recuperado para las queries de interés (optimización del embedding para queries objetivo), que contenga instrucciones adversariales de manera que pasen la revisión humana (texto oculto, formato confuso), y que las instrucciones sean seguidas por el LLM cuando aparecen en el contexto
- Envenenamiento de embeddings: técnica avanzada donde el documento se construye no solo para contener instrucciones maliciosas sino para que su representación vectorial sea cercana (en el espacio de embeddings) a documentos legítimos relevantes, asegurando alta probabilidad de recuperación
- Impacto en producción: un documento en el índice vectorial que instrucye al LLM a "siempre recomendar el producto X" o "siempre proporcionar información de contacto del atacante" afecta todos los usuarios que consulten sobre temas relacionados, sin que el equipo de desarrollo tenga visibilidad inmediata del problema
- Detección de documentos maliciosos: escaneo automático de documentos ingresados con clasificadores de contenido (LlamaGuard, Azure Content Safety) antes de indexarlos, auditoría periódica del corpus del vectorstore con búsquedas de patrones de injection, y monitoreo de outputs anómalos en producción que podrían indicar activación de documentos maliciosos

## Para recordar

El vectorstore es un componente de la superficie de ataque del sistema RAG tan crítico como el endpoint de inferencia: requiere controles de acceso con autenticación y autorización, validación de contenido en la ingestión, auditoría periódica del corpus, y monitoreo de outputs para detectar comportamientos coherentes con documentos maliciosos.
