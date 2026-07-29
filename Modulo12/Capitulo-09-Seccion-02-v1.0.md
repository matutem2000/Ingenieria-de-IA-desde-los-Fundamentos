# Módulo 12 – Capítulo 09 – Sección 02

# Documentación de API: endpoints, contratos y ejemplos de uso

La documentación de API del sistema integrador sigue el estándar OpenAPI 3.1, generada automáticamente por FastAPI desde los schemas Pydantic de los endpoints y enriquecida con ejemplos de request/response y descripciones de campos. El endpoint principal `/query` se documenta con el schema de request `QueryRequest` (campos `query: str`, `filters: Optional[QueryFilters]`, `session_id: Optional[str]`), el schema de response `QueryResponse` (campos `answer: str`, `sources: list[Source]`, `metadata: ResponseMetadata`), los códigos de error posibles (400 validation error, 401 unauthorized, 429 rate limit, 503 service unavailable) y tres ejemplos de request/response: pregunta simple, pregunta con filtros de metadata y pregunta fuera del dominio. El endpoint `/ingest` se documenta con el schema de request para ingesta de documentos individuales y por batch, incluyendo los campos de metadata obligatorios y opcionales. La documentación de API se expone en `/docs` (Swagger UI) y `/redoc` (ReDoc) en los entornos de desarrollo y staging, pero se deshabilita en producción por razones de seguridad.

## Elementos de la documentación de API

- OpenAPI 3.1 spec: generado automáticamente por FastAPI con enriquecimiento manual de descriptions y ejemplos
- Endpoint /query: request schema, response schema, ejemplos de petición simple, con filtros y fuera del dominio
- Endpoint /ingest: schema de documento individual y batch, campos de metadata obligatorios y opcionales
- Códigos de error: 400 (validation), 401 (auth), 403 (authorization), 429 (rate limit), 503 (dependency unavailable)
- Autenticación: documentación del flujo JWT con ejemplo de header Authorization: Bearer <token> y expiración de tokens

## Para recordar

La documentación de API no es un comentario — es un contrato entre el sistema y sus consumidores, y debe tratarse con el mismo rigor que el código: versionada, mantenida y testeada automáticamente contra la implementación real.
