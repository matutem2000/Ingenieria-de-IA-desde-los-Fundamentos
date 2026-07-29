# Módulo 6 – Capítulo 07 – Sección 03

# Versionado de índices y estrategias de actualización en caliente

El versionado de índices es la práctica de mantener múltiples versiones del índice vectorial de forma simultánea, permitiendo actualizar la configuración del sistema (modelo de embedding, estrategia de chunking, parámetros del índice ANN) sin interrumpir el servicio ni degradar la experiencia del usuario durante la transición. La necesidad surge cuando se cambia el modelo de embedding: todos los vectores del índice actual fueron generados con la versión anterior del modelo y son incompatibles con el nuevo modelo; no es posible comparar vectores generados por modelos distintos porque habitan espacios latentes distintos aunque tengan la misma dimensionalidad. La estrategia estándar es el patrón blue-green para índices: construir el nuevo índice (green) en paralelo con el índice de producción (blue) sin interrumpir el serving; una vez que el green index está completo y validado con el golden dataset de evaluación, cambiar el tráfico de lectura del retriever de blue a green mediante una actualización de configuración o un feature flag; finalmente, eliminar el blue index una vez que el green ha demostrado estabilidad en producción durante un período de observación (24–72 horas). Este patrón requiere el doble de la capacidad de almacenamiento durante la transición pero garantiza rollback inmediato si el nuevo índice produce resultados inesperados.

## Estrategias de versionado y actualización

- Blue-green index deployment: construir nuevo índice (green) en paralelo, validar con evaluación automatizada, redirigir tráfico gradualmente (canary: 5% → 20% → 50% → 100%), rollback inmediato si las métricas degradan; requiere doble capacidad de almacenamiento vectorial durante la transición
- Índice canary: dirigir un porcentaje pequeño del tráfico (1–5%) al nuevo índice mientras el resto sigue en el índice estable; comparar métricas de calidad (faithfulness, answer relevancy via LLM-judge) y latencia entre ambos índices en tiempo real antes de completar la migración
- Metadata versioning: adjuntar a cada chunk el campo `embedding_model_version` como metadato; permite identificar qué chunks fueron generados con qué versión del modelo y ejecutar reindexación incremental por versión sin reconstruir el índice completo si el modelo cambia solo parcialmente
- Compatibilidad hacia atrás del esquema de metadatos: cambios en los campos de metadatos (añadir un campo nuevo, cambiar el tipo de un campo existente) deben ser retrocompatibles; los chunks del índice con el esquema antiguo deben seguir siendo consultables después de un cambio de esquema
- Zero-downtime reindex con sharding temporal: dividir el corpus en shards y reindexar shard por shard; cada shard completamente reindexado pasa al nuevo índice; el serving consulta ambos índices (old y new) y combina los resultados hasta que la migración completa está finalizada
- Registro de versiones del índice: mantener un registro de versiones del índice con: versión del modelo de embedding usado, timestamp de inicio y fin de construcción, número de vectores indexados, parámetros de chunking y resultados de la evaluación automatizada; permite auditoría completa de qué índice estaba activo en cada momento

## Para recordar

Implementar el versionado de índices antes de realizar el primer cambio de modelo de embedding en producción; migrar un índice sin esta infraestructura implica un período de downtime o de calidad degradada que puede ser evitado con el patrón blue-green.
