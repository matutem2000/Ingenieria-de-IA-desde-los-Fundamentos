# Módulo 11 – Capítulo 06 – Sección 02

# Document-level permissions: que el sistema RAG respete el control de acceso de los documentos fuente

La implementación de document-level permissions en sistemas RAG enterprise requiere que el pipeline de recuperación vectorial sea permission-aware desde el nivel del índice, no solo a nivel de la interfaz de usuario: filtrar los resultados en la capa de presentación después de que el LLM ha generado una respuesta usando documentos no autorizados es inútil porque el daño (la información ya fue procesada y potencialmente incluida en la respuesta) ya se produjo. El mecanismo técnico más robusto es el pre-filtering en la capa de retrieval: antes de ejecutar la búsqueda por similitud vectorial, el sistema resuelve los grupos de permisos del usuario autenticado consultando al Identity Provider (Okta, Azure AD, o el LDAP corporativo) y construye un filtro de metadata que restricta la búsqueda vectorial solo a los documentos donde el usuario tiene permiso de lectura. En Pinecone, esto se implementa mediante filtros de metadata en la query vectorial ($in con la lista de grupos autorizados del usuario); en Weaviate mediante where filters; en pgvector mediante cláusulas WHERE en la query SQL. El desafío de rendimiento de este enfoque es que la lista de grupos de permisos del usuario puede ser larga (un ejecutivo puede pertenecer a 50-100 grupos de seguridad) y los filtros de metadata en bases de datos vectoriales tienen un overhead de rendimiento proporcional a la complejidad del filtro. La solución típica es cachear la lista de permisos del usuario en Redis con un TTL de 5-10 minutos, y usar técnicas de permission set hashing para reducir la complejidad de los filtros.

## Aspectos técnicos de document-level permissions

- Permission metadata en embeddings: cada documento se vectoriza con metadata que incluye document_acl (lista de grupos con acceso de lectura), classification_level, y owner_department, almacenada junto al vector en el índice
- Pre-filtering vs post-filtering: pre-filtering (aplicar permisos antes de la búsqueda vectorial) es más seguro que post-filtering (filtrar resultados después de la búsqueda) porque evita que documentos no autorizados entren en el contexto del LLM
- Resolución de permisos con caché: servicio de permissions-resolver que consulta Azure AD Graph API o LDAP, cachea el resultado por user_id en Redis con TTL de 5 minutos, y expone el permission set como lista de group_ids para construir el filtro vectorial
- Herencia de permisos: cuando un directorio tiene permisos, los documentos dentro heredan esos permisos a menos que se configuren permisos explícitos en el documento — la lógica de herencia debe replicarse exactamente en el pipeline de indexación de RAG
- Revocación inmediata: cuando el IAM revoca un permiso, el TTL del caché de permisos determina el tiempo máximo de exposición residual — TTL de 5 minutos implica que en el peor caso un usuario retiene acceso 5 minutos después de la revocación

## Buena práctica

Documentar explícitamente en el contrato de seguridad del sistema RAG el tiempo máximo de revocación de acceso (equivalente al TTL del caché de permisos) y obtener aprobación del CISO sobre ese tiempo como parte del diseño de seguridad.
