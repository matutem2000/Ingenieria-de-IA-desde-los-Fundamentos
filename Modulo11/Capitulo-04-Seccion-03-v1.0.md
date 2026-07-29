# Módulo 11 – Capítulo 04 – Sección 03

# Rate limiting y fairness por tenant: evitar que un tenant afecte a otros

El problema del "noisy neighbor" en plataformas multi-tenant de IA se manifiesta cuando un tenant ejecuta una carga de trabajo intensiva — por ejemplo, un job de indexación masiva de 100.000 documentos o un pico de 500 consultas simultáneas de usuarios — que satura los recursos compartidos de la plataforma y degrada la latencia de respuesta para todos los demás tenants activos en ese momento. El rate limiting por tenant en sistemas de IA debe operar en múltiples dimensiones simultáneamente: tokens por minuto (TPM) para controlar el consumo de contexto del LLM, requests por segundo (RPS) para controlar la frecuencia de consultas a la API, y unidades de vectorización por hora para controlar la carga de indexación en la base de datos vectorial. La implementación técnica del rate limiting distribuido — necesario porque la plataforma opera con múltiples instancias del servicio de orquestación — requiere un almacén de estado compartido (Redis con el algoritmo Token Bucket o Sliding Window implementado con scripts Lua atómicos) que garantiza que el límite se aplica globalmente al tenant y no por instancia individual del servicio. El fairness entre tenants va más allá del rate limiting: requiere implementar schedulers con fair queueing (Weighted Fair Queueing) que garantizan que un tenant que consume poco en condiciones normales recibe prioridad sobre un tenant que está saturando el sistema, evitando que los tenants de alto volumen monopolicen los recursos en momentos de alta demanda.

## Aspectos técnicos del rate limiting en IA multi-tenant

- Token bucket distribuido en Redis: implementado con RedisLimiter o redis-cell, permite burst de corta duración mientras aplica límites de largo plazo, con configuración por tenant_id y por tipo de operación (inferencia vs indexación)
- Límites en múltiples dimensiones: TPM (tokens per minute) para controlar el costo de LLM, RPM (requests per minute) para controlar la frecuencia de API, y concurrent_requests para controlar la saturación de conexiones simultáneas
- Priority queues por tier de servicio: colas de procesamiento con prioridad alta (tenants Enterprise), media (tenants Pro), y baja (tenants Free), procesadas con Weighted Fair Queueing para garantizar que los tenants de menor tier reciben respuesta incluso durante picos
- Adaptive rate limiting: ajuste dinámico de los límites por tenant basado en el consumo histórico y la capacidad disponible del sistema, usando métricas de Prometheus como señal de ajuste
- Respuestas de rate limit apropiadas: HTTP 429 con headers Retry-After y X-RateLimit-Reset para que los clientes implementen backoff exponencial; mensajes de error con información sobre el límite aplicable y cómo aumentarlo (upgrade de plan)

## Buena práctica

Los límites de rate limiting deben ser visibles para los tenants desde el primer día — publicarlos en el portal de desarrolladores con las métricas de consumo actual evita que los tenants descubran los límites en producción durante picos críticos de negocio.
