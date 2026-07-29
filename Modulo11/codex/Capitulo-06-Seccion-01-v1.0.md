# Módulo 11 – Capítulo 06 – Sección 01

# RAG empresarial: desafíos de seguridad, autorización y segmentación de conocimiento

El RAG (Retrieval-Augmented Generation) en contexto enterprise no es simplemente un sistema de búsqueda semántica conectado a un LLM: es un sistema de acceso a información corporativa que debe respetar estrictamente los mismos controles de acceso que el sistema de gestión documental del que provienen los documentos, porque la capacidad del LLM de sintetizar información de múltiples fragmentos de documentos puede revelar información confidencial a usuarios que tendrían acceso a cada fragmento individual pero no deberían poder combinarlos. El desafío de la segmentación de conocimiento emerge cuando el sistema RAG indexa documentos de diferentes niveles de clasificación — documentos públicos, internos, confidenciales, y restringidos — en el mismo índice vectorial: una búsqueda semántica sin filtros de autorización puede recuperar fragmentos de documentos restringidos en el contexto de un usuario que solo tiene acceso a documentos internos, y el LLM generará una respuesta que sintetiza información a la que el usuario no debería tener acceso. Los desafíos de autorización en RAG enterprise incluyen además la temporalidad del acceso: cuando un usuario pierde el acceso a un documento (porque cambió de rol, porque el documento fue reclasificado, o porque venció su autorización temporal), el índice vectorial debe reflejar ese cambio de acceso inmediatamente sin requerir una reindexación completa del corpus. La segmentación de conocimiento por dominio (cada departamento ve solo los documentos de su dominio, con excepciones gestionadas por el sistema de gestión de permisos del DMS) es la dimensión más crítica para el cumplimiento en sectores regulados como el financiero, legal, y farmacéutico.

## Desafíos técnicos del RAG empresarial

- Permission-aware retrieval: el pipeline de recuperación debe filtrar los documentos candidatos por los permisos del usuario autenticado antes de ejecutar la búsqueda vectorial de similitud, no después
- Clasificación de documentos en el índice: cada chunk vectorizado debe llevar metadata de su nivel de clasificación (public, internal, confidential, restricted) y los permisos del documento fuente (lista de grupos autorizados)
- Acumulación de contexto y information leakage: el LLM recibe múltiples chunks de documentos distintos en el mismo contexto; si alguno de esos chunks proviene de un documento al que el usuario no debería acceder, hay un fallo de control de acceso que el LLM no puede detectar
- Revocación de acceso en tiempo real: cuando el sistema de IAM revoca el acceso de un usuario a un documento, el pipeline de RAG debe reflejar ese cambio sin reindexar — implementado mediante filtros dinámicos basados en permisos actualizados en caché con TTL corto (5-60 segundos)
- Audit logging de retrieval: registrar en cada búsqueda vectorial los document IDs recuperados, los permisos del usuario solicitante, y los chunks incluidos en el contexto del LLM, para auditoría de acceso a información sensible

## Para recordar

Un sistema RAG enterprise que no implementa autorización a nivel de documento es un sistema que potencialmente exfiltra información confidencial a cualquier usuario autenticado que formule la pregunta correcta.
