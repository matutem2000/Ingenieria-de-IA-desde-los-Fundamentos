# Módulo 6 – Capítulo 03 – Sección 06

# Cierre: la base de datos vectorial como componente crítico de infraestructura

La base de datos vectorial no es un detalle de implementación intercambiable en un sistema RAG: es el componente que determina el techo de rendimiento del retriever, la latencia observable por el usuario, la capacidad de filtrar por permisos y metadatos de negocio, y el costo operativo a escala. Los equipos que tratan la base vectorial como un "detail de bajo nivel" que siempre puede cambiarse más tarde pagan el costo de migraciones costosas cuando los requisitos de producción superan las capacidades del sistema inicial; Chroma es excelente para prototipos pero escala mal a corpus de millones de documentos, y migrar de Chroma a Qdrant implica reindexar todo el corpus y adaptar el código de integración. La base de datos vectorial debe considerarse al mismo nivel de criticidad que cualquier base de datos transaccional: requiere planificación de capacidad, estrategia de backup y recuperación, monitoreo de latencia y disponibilidad, runbooks de operación y ownership claro en el equipo de plataforma. Los sistemas RAG más robustos de producción, como el de Elastic o el de Cohere, tratan la infraestructura vectorial como una capa de servicio independiente con su propio SLA, separada del pipeline de recuperación que la consume.

*"La arquitectura de un sistema es las decisiones que son difíciles de cambiar. Todo lo demás son detalles."* — Martin Fowler, arquitecto de software y autor de Patterns of Enterprise Application Architecture

## Principio rector

Elegir la base de datos vectorial como una decisión de infraestructura de largo plazo, evaluando no solo el rendimiento actual sino la capacidad de la plataforma para crecer con el sistema y la solidez operativa de su ecosistema de herramientas de gestión.
