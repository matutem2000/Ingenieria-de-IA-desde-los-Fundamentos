# Módulo 6 – Capítulo 04 – Sección 05

# Indexación incremental: actualizaciones sin reindexar toda la colección

Los corpus de producción no son estáticos: los documentos se actualizan, se añaden nuevos contenidos y se eliminan materiales obsoletos de forma continua; la capacidad de procesar estos cambios de forma incremental, sin reconstruir el índice completo, es una propiedad crítica para la operabilidad del sistema. La reindexación completa de un corpus de 1 millón de documentos puede tardar horas o días dependiendo del volumen de texto, el costo de las llamadas al modelo de embedding y el throughput de escritura de la base vectorial; hacerlo en cada actualización es operativamente inviable. La indexación incremental requiere un mecanismo de detección de cambios: la estrategia más común es mantener un hash (SHA-256 o MD5) del contenido de cada documento y compararlo con el hash almacenado en la base de datos de tracking cada vez que se ejecuta el pipeline de ingesta; solo los documentos cuyo hash difiere requieren reindexación. Este change detection pipeline puede ejecutarse como un proceso batch programado (cada hora, cada noche) o en tiempo real mediante event streams (Kafka, SNS, webhooks de sistemas de gestión documental como SharePoint o Confluence).

## Componentes de la indexación incremental

- Change detection: comparación de hash SHA-256 del contenido de cada documento con el hash almacenado en una tabla de tracking (PostgreSQL, DynamoDB); los documentos con hash diferente se marcan para reindexación; los documentos nuevos (sin hash previo) se marcan para indexación inicial
- Document tracking store: base de datos relacional o KV que almacena doc_id, hash_content, indexed_at, chunk_ids[] para cada documento indexado; permite reconstruir qué chunks están asociados a qué documento y coordinar eliminaciones atómicas durante actualizaciones
- Eliminación de chunks obsoletos: al reindexar un documento actualizado, eliminar primero todos los chunks con `doc_id = X` en la base vectorial, luego insertar los nuevos chunks del documento actualizado; el orden garantiza que no coexistan versiones antiguas y nuevas durante la actualización
- Pipeline de ingesta streaming: integración con sistemas de eventos (Kafka, AWS SQS, webhooks de SharePoint/Confluence/Notion) que disparan la reindexación del documento modificado en tiempo real con latencia de segundos; adecuado para casos de uso donde la frescura del índice es crítica
- Pipeline de ingesta batch: proceso programado (cron o Apache Airflow) que escanea el corpus, detecta cambios mediante hash comparison, procesa en lotes (batches de 100–1000 documentos) y actualiza el índice; adecuado cuando la latencia de actualización de minutos u horas es aceptable
- Manejo de dependencias entre chunks: en corpus con documentos que se referencian entre sí (wikis con links internos, bases de código con imports), el cambio de un documento puede requerir reindexar los chunks de los documentos dependientes que incluyen el contexto del documento modificado

## Buena práctica

Diseñar el pipeline de indexación con soporte incremental desde el inicio, antes de que el corpus sea demasiado grande para reindexación completa; añadir capacidad incremental a un sistema que nació como reindexación completa periódica es una refactorización costosa.
