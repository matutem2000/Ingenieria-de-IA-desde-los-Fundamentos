# Módulo 5 – Capítulo 04 – Sección 02

## APIs REST para exponer capacidades de IA a otras aplicaciones

La forma más efectiva de hacer que las capacidades de IA estén disponibles para otros sistemas —frontends web, aplicaciones móviles, microservicios internos, herramientas de terceros— es encapsularlas detrás de una API REST con contratos bien definidos. Este encapsulamiento oculta los detalles de implementación: qué proveedor de LLM usa el sistema, qué versión de modelo, qué estructura de prompt, qué framework de orquestación. Los sistemas consumidores solo conocen el contrato de la API —el schema de entrada y salida, los códigos de error, las garantías de versionado— y pueden adaptarse a cambios de implementación interna sin modificación.

FastAPI es el framework Python dominante para este propósito por tres razones concretas. Los modelos Pydantic se traducen automáticamente en schemas de validación de request, documentación OpenAPI/Swagger generada en `/docs`, y serialización tipada de responses, sin ningún código adicional. El soporte nativo de async/await hace que los endpoints puedan llamar a las APIs de LLM de forma no bloqueante, manejando múltiples requests concurrentes sin hilos adicionales. Y `StreamingResponse` permite transmitir tokens al cliente con tres líneas de código, lo que en otros frameworks requiere configuración significativa.

El diseño del contrato de la API de IA tiene consideraciones específicas que no aplican a APIs convencionales. El schema de request debe incluir los campos de contenido (el texto o pregunta del usuario, los documentos a procesar, el historial conversacional) más campos de configuración opcionales que dan flexibilidad sin exponer complejidad interna: `tone` para aplicaciones de redacción, `format` para aplicaciones de análisis, `language` para sistemas multilingues. El schema de response debe incluir siempre los datos de resultado más un campo `metadata` con información de operación: `model_used`, `input_tokens`, `output_tokens`, `latency_ms`, `request_id`. Esta metadata es invaluable para debugging, facturación interna y análisis de comportamiento, y añadir estos campos al contrato desde el inicio es mucho más simple que hacerlo retroactivamente cuando múltiples sistemas ya consumen la API.

La autenticación de la API interna de IA debe implementarse con JWT o API keys propias —no las del proveedor de LLM, que son credenciales de infraestructura— con scopes que definen qué capacidades puede usar cada cliente interno. Un servicio de frontend puede tener scope `chat:send` pero no `analysis:batch`; un servicio de procesamiento interno puede tener `analysis:batch` sin necesidad de `chat:send`. Esta granularidad de permisos aplica el principio de mínimo privilegio al nivel de la API de IA, independientemente de los permisos que cada servicio tenga hacia el proveedor externo.

El versionado de endpoints con prefijo `/v1/` desde el inicio establece la política explícita de que el contrato de la versión activa se mantiene estable durante al menos doce meses tras publicar la siguiente. Esta garantía permite que los sistemas consumidores migren a nuevas versiones sin urgencia, y que el equipo de IA evolucione la implementación interna —cambiando el modelo, el prompt, el framework— sin romper integraciones existentes.

## Componentes principales de una API REST de IA

- **Schema de request con Pydantic:** modelos de entrada con validación de campos obligatorios (`user_message: str = Field(min_length=1, max_length=4096)`), tipos enumerados para parámetros opcionales, y documentación de campo que se propaga a la documentación OpenAPI.
- **Middleware de autenticación:** `Depends(verify_jwt_token)` en FastAPI que valida el token antes de ejecutar el endpoint, extrae los scopes del payload JWT, y verifica que el scope requerido esté presente; rate limiting por API key usando Redis.
- **Schema de response estandarizado:** estructura `{"data": {...}, "metadata": {"model": "...", "input_tokens": N, "output_tokens": N, "latency_ms": N, "request_id": "..."}, "error": null}` consistente para éxito y fallo, con el mismo envelope en ambos casos.
- **Versionado semántico de endpoints:** prefijo `/v1/` en todos los endpoints con política explícita de backward compatibility; nuevas capacidades se añaden en `/v2/` mientras `/v1/` permanece operativa durante el período de migración.
- **Health checks:** endpoint `/health` que verifica la conectividad con el proveedor de LLM haciendo una llamada de prueba y devuelve la latencia; `/readiness` que incluye además la conectividad con bases de datos y caches; usados por Kubernetes para routing de tráfico.

La API REST de IA es el contrato entre las capacidades de IA y el resto del sistema; su estabilidad, documentación y versionado determina la autonomía con que el equipo de IA puede evolucionar la implementación interna sin coordinar con todos los equipos consumidores en cada cambio. La siguiente sección aborda la integración de IA con las fuentes de datos que el sistema ya tiene: bases de datos relacionales, documentales, y vectoriales.

---

**Para recordar:** La API REST de IA es el contrato con el resto del sistema; estabilizarla con versionado explícito, schema de metadata estandarizado y documentación OpenAPI actualizada protege a los equipos consumidores de los cambios internos de implementación del modelo o el prompt.
