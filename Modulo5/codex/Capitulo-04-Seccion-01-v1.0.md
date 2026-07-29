# Módulo 5 – Capítulo 04 – Sección 01

# Patrones de integración: síncrono, asíncrono, event-driven y por lotes

Integrar capacidades de IA en una aplicación existente puede seguir cuatro patrones arquitectónicos según los requisitos de latencia, throughput y complejidad del flujo: síncrono (request-response), asíncrono (polling o webhooks), event-driven (mensajería) y por lotes (batch processing). El patrón síncrono es el más simple: el cliente llama a un endpoint que internamente llama al LLM y devuelve la respuesta en la misma conexión HTTP; adecuado para interacciones conversacionales con latencia tolerable de 2-10 segundos y volumen bajo-medio (<100 RPS). El patrón asíncrono desacopla la solicitud de la respuesta: el cliente recibe un `job_id` inmediatamente, y consulta el estado vía polling o recibe un webhook cuando el proceso termina; adecuado para tareas de análisis de documentos que toman 30+ segundos donde mantener la conexión abierta es costoso. El patrón event-driven con brokers de mensajes (Kafka, RabbitMQ, AWS SQS) permite escalar horizontalmente el procesamiento de IA distribuyendo trabajo entre múltiples workers consumidores, con control de backpressure y dead letter queues para manejo robusto de fallos.

## Aspectos técnicos de los patrones de integración

- Síncrono con streaming: combina la simplicidad del patrón síncrono con streaming SSE para reducir la latencia percibida; FastAPI + `StreamingResponse` o Django con `StreamingHttpResponse` permiten transmitir tokens del LLM al cliente en tiempo real
- Asíncrono con Celery o ARQ: workers Python consumen tareas de una cola Redis o RabbitMQ, llaman al LLM y actualizan el estado en la base de datos; el cliente consulta el estado vía polling sobre un endpoint REST de status
- Event-driven con AWS SQS + Lambda: mensajes en SQS disparan funciones Lambda que procesan con el LLM y publican el resultado en otro topic SNS o actualizan DynamoDB; ideal para pipelines de enriquecimiento de datos a escala
- Batch processing nocturno: scripts que leen registros de una base de datos, los procesan en paralelo con `asyncio.gather()` sobre el SDK async del LLM, y escriben los resultados de vuelta; throughput optimizable con semáforos para controlar la concurrencia y respetar el rate limit de la API
- Elección del patrón: latencia <5s y UX conversacional → síncrono con streaming; análisis de documento único por usuario → asíncrono con webhook; enriquecimiento de millones de registros → batch; pipeline de eventos en tiempo real → event-driven

## Principio rector

El patrón de integración determina el diseño del sistema completo —autenticación, manejo de errores, escalabilidad y experiencia del usuario—; elegirlo correctamente desde el inicio es más importante que la elección del modelo de IA específico.
