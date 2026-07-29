# Módulo 11 – Capítulo 02 – Sección 04

# API management para servicios de IA: versionado, contratos y retrocompatibilidad

Los servicios de IA enterprise exponen APIs que son consumidas por decenas de aplicaciones internas, y cada cambio en el comportamiento del modelo o en el esquema de respuesta puede romper integraciones en cascada si no se gestiona mediante un proceso formal de versionado y gestión de contratos de API. El versionado semántico aplicado a APIs de IA (v1, v2, v3 en el path, o versión en el header Accept) debe acompañarse de un período de deprecación explícito — mínimo 6 meses para APIs internas, 12 meses para APIs expuestas a clientes externos — durante el cual ambas versiones coexisten y el equipo productor provee soporte a los consumidores para migrar. El contrato de una API de IA incluye dimensiones que no existen en APIs convencionales: el modelo subyacente que se utiliza (y si puede cambiar sin previo aviso), los campos del esquema de respuesta que son estables versus los que son experimentales, los SLOs de latencia (p50, p95, p99), y las garantías o ausencia de garantías de determinismo en las respuestas. Las herramientas de API management enterprise (Kong Gateway, AWS API Gateway, Azure APIM, o Apigee) permiten gestionar estas APIs con rate limiting por cliente, logging centralizado para auditoría, y circuit breakers que protegen los sistemas upstream cuando el servicio de LLM tiene degradación de rendimiento.

## Aspectos técnicos de API management para IA

- Versionado de API: URI versioning (/v1/completions, /v2/chat) combinado con deprecation headers (Sunset, Deprecation) para notificar a los consumidores la fecha de fin de soporte
- Contratos OpenAPI/AsyncAPI: especificaciones Swagger que documentan todos los campos, tipos, ejemplos, y restricciones de la API, publicadas en el portal de desarrolladores interno
- Rate limiting inteligente: límites configurados a nivel de tenant, endpoint, y modelo, con headers de respuesta (X-RateLimit-Remaining, Retry-After) para que los clientes adapten su comportamiento
- Circuit breaker y fallback: patrón implementado con Resilience4j o Polly que devuelve respuestas de fallback predefinidas cuando el LLM upstream supera el tiempo de respuesta configurado
- API versioning governance: proceso de RFC interno para proponer cambios breaking, con período de review, aprobación por los principales consumidores, y release notes detalladas

## Principio rector

Un contrato de API es una promesa: en sistemas enterprise, romper esa promesa sin un proceso formal de deprecación genera confianza negativa que tarda meses en reconstruirse.
