# Módulo 12 – Capítulo 05 – Sección 03

# Autenticación y autorización: control de acceso al sistema y a las herramientas del agente

La autenticación del sistema usa JWT (JSON Web Tokens) con algoritmo RS256, donde el token incluye claims estándar (sub, exp, iat) más claims personalizados: `roles` (lista de roles del usuario) y `allowed_document_types` (tipos de documentos a los que el usuario tiene acceso). Cada petición a la API pasa por un middleware FastAPI que verifica la firma del JWT con la clave pública del identity provider, valida la expiración y extrae los claims de autorización. La autorización a nivel de herramientas del agente implementa RBAC: los filtros de metadatos de la herramienta `search_knowledge_base` incluyen automáticamente el claim `allowed_document_types` del usuario, de modo que un usuario sin acceso a ADRs confidenciales no puede recuperarlos aunque los solicite explícitamente en su query. El refresh de tokens usa un endpoint dedicado con tokens de corta duración (15 minutos) y refresh tokens con rotación automática, almacenados en httpOnly cookies.

## Controles de autenticación y autorización

- JWT RS256: tokens firmados con clave privada del IdP, verificados con clave pública en cada petición al middleware FastAPI
- Claims de autorización: allowed_document_types y roles incluidos en el JWT y validados antes de cada llamada a herramienta
- Filtros automáticos: search_knowledge_base aplica allowed_document_types como filtro mandatory en cada query a Qdrant
- Token lifecycle: access token 15 minutos, refresh token 24 horas con rotación automática en cada uso
- Audit trail: cada petición autenticada registra user_id, timestamp, endpoint y resultado en tabla de audit logs de PostgreSQL

## Para recordar

La autorización a nivel de herramientas del agente es el control más efectivo contra divulgación no autorizada — si el retrieval filtra automáticamente por los permisos del usuario, el agente no puede devolver documentos a los que el usuario no tiene acceso, independientemente de cómo formule su query.
