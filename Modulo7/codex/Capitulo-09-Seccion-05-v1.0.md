# Módulo 7 – Capítulo 09 – Sección 05

# Escalabilidad horizontal de agentes: workers, colas y balanceo de carga

Los agentes en producción de alto volumen no pueden ejecutarse en una sola instancia: el tiempo de ejecución por tarea (segundos a minutos) y la intensidad computacional (múltiples llamadas a LLM + herramientas por tarea) limitan el throughput de una sola instancia a pocas tareas concurrentes. La escalabilidad horizontal requiere descomponer el sistema en productores (los clientes que envían tareas), colas de mensajes (Redis, RabbitMQ, SQS, Kafka) que actúan como buffers entre productores y workers, y workers (instancias del agente que consumen tareas de la cola y las ejecutan). Este patrón desacopla la recepción de requests de su procesamiento, permite escalar el número de workers dinámicamente según la carga (auto-scaling basado en profundidad de cola), y proporciona resistencia natural ante fallos de workers individuales (la tarea vuelve a la cola si el worker falla antes de confirmar su completitud). Celery con Redis/RabbitMQ, Dramatiq, Bull.js, y AWS SQS + ECS son stacks comunes para este patrón en producción.

## Aspectos técnicos

- **Queue-based worker pool**: los requests de tareas del agente se encolan en Redis/SQS con un mensaje que contiene: task_id, input del usuario, configuración del agente, y timestamp de encole; los workers consumen y procesan tareas concurrentemente hasta su límite de concurrencia configurado
- **Worker concurrency**: cada worker puede ejecutar N agentes concurrentemente usando asyncio (I/O-bound tasks) o threads/procesos (CPU-bound tasks); para agentes que hacen múltiples llamadas HTTP concurrentes, asyncio con concurrencia de 5-20 tareas por worker es típico
- **Auto-scaling basado en métricas de cola**: cuando la profundidad de la cola (número de tareas pendientes) supera un umbral, escalar horizontalmente añadiendo workers; cuando cae por debajo de otro umbral, escalar hacia abajo; implementado con Kubernetes HPA + KEDA (escalado basado en métricas de colas externas)
- **Dead letter queue (DLQ)**: tareas que fallan repetidamente (superan max_retries) se mueven a una DLQ para revisión manual; la DLQ previene que tareas irrecuperables bloqueen la cola principal o consuman recursos infinitamente en retries
- **Prioridad de tareas**: en colas con prioridad (Redis Sorted Sets, SQS FIFO con grupos de mensajes), asignar mayor prioridad a tareas interactivas de usuario (esperan respuesta en tiempo real) sobre tareas batch (se ejecutan en background); garantiza que las tareas interactivas no sean bloqueadas por cargas de trabajo batch

## Buena práctica

Monitorear la profundidad de la cola y la latencia de procesamiento como SLIs primarios del sistema de agentes: un aumento sostenido en la profundidad de la cola sin aumento proporcional en el número de workers es la señal más temprana de degradación de capacidad antes de que los usuarios experimenten latencias inaceptables.
