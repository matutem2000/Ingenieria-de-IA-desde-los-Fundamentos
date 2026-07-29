# Módulo 11 – Capítulo 03 – Sección 04

# APIs de integración: REST, SOAP, gRPC y message queues para conectar el legado

Los sistemas enterprise legacy exponen datos e interfaces mediante protocolos y estilos arquitectónicos que reflejan la época en que fueron construidos: un sistema de los años 90 típicamente habla mediante procedimientos almacenados o archivos batch, uno de los 2000 habla SOAP/XML con WSDLs elaborados, uno de los 2010 expone REST/JSON, y los sistemas modernos pueden ofrecer gRPC o APIs GraphQL. El ingenieros de IA enterprise debe ser capaz de integrar con todos estos protocolos, eligiendo el mecanismo de integración más apropiado para cada caso en función de los requisitos de latencia, volumen de datos, y disponibilidad del sistema fuente. gRPC es el protocolo preferido para comunicación entre servicios internos de IA de alta frecuencia: el uso de Protocol Buffers garantiza serialización eficiente con tipado fuerte, el soporte de streaming bidireccional permite enviar resultados de inferencia en tiempo real, y el rendimiento supera en 5-10x a REST/JSON para el mismo payload en benchmarks típicos de microservicios. Los message queues (RabbitMQ, Apache Kafka, AWS SQS) son la integración adecuada cuando el sistema legacy no puede ser consultado de manera sincrónica: el sistema de IA actúa como consumidor de mensajes que el legacy publica cuando ocurren eventos de negocio relevantes (nueva factura creada, contrato firmado, ticket de soporte abierto), procesándolos de manera asíncrona sin imponer carga adicional al sistema fuente.

## Aspectos técnicos de cada protocolo

- REST/JSON: protocolo de integración por defecto para sistemas modernos, con OpenAPI 3.0 para documentación, HTTP/2 para multiplexing, y compresión gzip para reducir el tamaño de payloads con textos largos en contextos de RAG
- SOAP/XML: consumido mediante generadores de clientes WSDL (zeep en Python, JAX-WS en Java) o mediante herramientas de API mediation (Apache Camel, MuleSoft) que convierten SOAP a REST transparentemente
- gRPC con Protocol Buffers: protocolo preferido para alta frecuencia intra-cluster, con .proto schemas versionados en un schema registry, generación de código automática para múltiples lenguajes, y soporte de streaming para respuestas de LLM en tiempo real
- Apache Kafka como integration backbone: topics particionados por dominio de negocio, consumidores de IA que procesan eventos en paralelo, y schemas Avro que garantizan compatibilidad backward entre versiones del productor y el consumidor
- File-based integration para mainframes: SFTP con PGP encryption para transferencia segura de archivos fijos generados por COBOL, procesados por pipelines de Spark o Pandas con detección de cambios por checksum

## Idea central

La selección del protocolo de integración debe basarse en las capacidades del sistema legacy, no en las preferencias tecnológicas del equipo de IA: integrar bien un sistema SOAP es más valioso que insistir en que adopte REST antes de que el sistema de IA pueda usarlo.
