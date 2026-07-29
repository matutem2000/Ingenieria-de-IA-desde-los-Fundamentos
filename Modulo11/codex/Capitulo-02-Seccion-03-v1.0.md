# Módulo 11 – Capítulo 02 – Sección 03

# Arquitectura orientada a eventos para IA: procesamiento asíncrono a escala

Los sistemas de IA enterprise que dependen exclusivamente de procesamiento síncrono request-response enfrentan un límite de escala determinado por el tiempo de inferencia del modelo: si un LLM tarda 3 segundos en responder, un servicio con 1.000 usuarios concurrentes necesita 3.000 conexiones abiertas simultáneamente, agotando los recursos de red y generando timeouts en cascada. La arquitectura orientada a eventos desacopla el productor de la petición del consumidor de la inferencia mediante un message broker (Apache Kafka, AWS SQS/SNS, o Azure Service Bus), permitiendo que el procesamiento de IA ocurra de manera asíncrona y que los resultados se entreguen cuando estén disponibles — mediante webhooks, websockets, o polling de estado. Este patrón es especialmente crítico para workloads de procesamiento de documentos (análisis de contratos, extracción de información de PDFs, clasificación de correos electrónicos), donde un único job puede requerir procesar miles de documentos en batch y la latencia de cada llamada individual al LLM haría inviable un diseño síncrono. La implementación con Kafka permite además procesar el mismo evento por múltiples consumidores: el mismo documento puede ser vectorizado, clasificado, y enriquecido con metadata por tres servicios de IA distintos en paralelo, consumiendo el mismo mensaje del topic.

## Componentes del diseño orientado a eventos

- Message broker: Apache Kafka con topics particionados por tipo de evento y tenant, retención configurable, y esquemas Avro gestionados en Confluent Schema Registry
- Productores de eventos: aplicaciones que publican eventos de negocio (documento_subido, contrato_recibido, ticket_creado) sin conocer quién los va a procesar
- Workers de IA: consumidores Kafka (Faust, Kafka Streams) que procesan eventos y ejecutan las inferencias de IA, con dead letter queues para manejo de errores
- Entrega de resultados: webhooks para notificación push, Server-Sent Events (SSE) para streaming de respuestas largas, o actualización de estado en base de datos consultable por polling
- Backpressure y control de flujo: consumer lag monitoring con Grafana, auto-scaling de workers basado en el lag del consumer group, y throttling configurable por tenant

## Para recordar

El procesamiento asíncrono orientado a eventos es la arquitectura natural para workloads de IA enterprise que procesan volúmenes altos de documentos o peticiones batch con tiempos de respuesta tolerantes al diferido.
