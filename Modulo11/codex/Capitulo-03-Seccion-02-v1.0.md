# Módulo 11 – Capítulo 03 – Sección 02

# Patrones de integración: adapter, facade y anti-corruption layer para sistemas legacy

Los patrones de diseño de integración con sistemas legacy provienen del Domain-Driven Design (DDD) y de los patrones de integración de enterprise (EIP), y su aplicación a sistemas de IA enterprise permite encapsular la complejidad y la inconsistencia de los sistemas legacy detrás de interfaces modernas que los sistemas de IA pueden consumir sin acoplarse a los detalles de implementación del sistema legacy. El patrón Adapter traduce la interfaz de un sistema legacy a una interfaz que el sistema de IA puede consumir: un Adapter SOAP-to-REST convierte las llamadas SOAP/XML de un sistema SAP en endpoints RESTful con payloads JSON, absorbiendo la conversión de formato y el manejo de errores específicos de SOAP sin que el sistema de IA necesite conocer que el sistema subyacente habla SOAP. El patrón Facade agrega múltiples sistemas legacy detrás de una interfaz unificada: en lugar de que el sistema de RAG tenga que consultar por separado el ERP, el CRM, y el sistema de gestión documental, la Facade presenta una API única que internamente orquesta las consultas a los tres sistemas y devuelve una respuesta consolidada. El Anti-Corruption Layer (ACL) es el patrón más crítico para sistemas de IA: actúa como una capa de traducción bidireccional que impide que el modelo de dominio corrupto del sistema legacy (con sus nombres de campo crípticos, sus reglas de negocio implícitas, y sus inconsistencias históricas) contamine el modelo de dominio limpio del sistema de IA.

## Aspectos técnicos de los patrones de integración

- Adapter SOAP-to-REST: implementado con Apache Camel, MuleSoft, o AWS API Gateway con mapping templates, convierte WSDLs en OpenAPI specs automáticamente con herramientas como soap2rest
- Facade de agregación: microservicio que implementa el patrón Backend-for-Frontend (BFF) específico para IA, consolidando datos de múltiples fuentes legacy en el formato óptimo para el contexto de un LLM
- Anti-Corruption Layer: capa de traducción con mappers explícitos (MapStruct en Java, Pydantic validators en Python) que valida, limpia, y transforma los datos del legacy antes de que entren al pipeline de IA
- Change Data Capture (CDC): Debezium sobre MySQL/PostgreSQL o Oracle LogMiner para capturar cambios en las bases de datos legacy en tiempo real y publicarlos en Kafka sin acceso directo a las tablas
- Circuit breaker para legado: implementar Resilience4j o Polly con timeouts agresivos (2-3 segundos máximo) y fallbacks a datos cacheados cuando el sistema legacy no responde dentro del SLA esperado

## Principio rector

Aislar la complejidad del legado en capas de integración explícitas permite que el sistema de IA evolucione independientemente de los cambios —o la falta de cambios— en los sistemas legacy subyacentes.
