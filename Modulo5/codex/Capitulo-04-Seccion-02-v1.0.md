# Módulo 5 – Capítulo 04 – Sección 02

# APIs REST para exponer capacidades de IA a otras aplicaciones

Exponer capacidades de IA como endpoints REST permite que cualquier aplicación —frontend web, aplicación móvil, microservicio interno— consuma la funcionalidad sin conocer los detalles de implementación del LLM, el prompt o el framework de orquestación subyacente. FastAPI es el framework Python dominante para este propósito: tipos de entrada y salida definidos con Pydantic se traducen automáticamente en OpenAPI/Swagger docs, validación de request y serialización de response sin código adicional. El diseño del contrato de la API es crítico: el schema de entrada debe ser lo suficientemente genérico para no romper compatibilidad ante cambios de prompt, y el schema de salida debe incluir campos de metadata como `model_used`, `tokens_consumed`, `latency_ms` y `request_id` que permitan debugging y facturación interna. La autenticación de la API interna de IA debe implementarse con JWT o API keys propias (no las del proveedor de LLM), con scopes que limiten qué capacidades puede usar cada cliente interno, aplicando el principio de mínimo privilegio a nivel de API.

## Componentes principales de una API REST de IA

- Schema de request con Pydantic: definir modelos de entrada (`ChatRequest`, `AnalysisRequest`) con validación de campos obligatorios, longitud máxima del input, y enumeraciones de parámetros opcionales como el `tone` o `format` de salida
- Middleware de autenticación: JWT validation middleware en FastAPI con `Depends()` que verifica el token antes de llegar al endpoint, con rate limiting por API key usando Redis para prevenir abuso interno
- Schema de response estandarizado: incluir siempre `data`, `metadata` (tokens, latencia, modelo), `request_id` y `error` en el mismo envelope para que los clientes tengan una interfaz predecible independientemente del éxito o fallo
- Versionado de endpoints: prefijo `/v1/` en todos los endpoints con la política de que una versión se mantiene activa durante al menos 12 meses tras publicar la siguiente, dando tiempo a los clientes para migrar sin urgencia
- Health checks y readiness: endpoint `/health` que verifica conectividad con el proveedor de LLM y devuelve latencia de la última llamada de prueba, permitiendo a Kubernetes excluir pods degradados del tráfico

## Para recordar

La API REST de IA es el contrato con el resto del sistema; estabilizarla con versiones claras y documentación OpenAPI actualizada protege a los equipos consumidores de los cambios internos de implementación del modelo o el prompt.
