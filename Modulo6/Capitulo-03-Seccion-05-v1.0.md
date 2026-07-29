# Módulo 6 – Capítulo 03 – Sección 05

# Operaciones de producción: actualizaciones, eliminaciones y gestión del índice

Operar una base de datos vectorial en producción implica manejar el ciclo completo de vida del índice más allá de la inserción inicial: actualización de documentos modificados, eliminación de contenido obsoleto o con errores, monitoreo de la degradación del índice por fragmentación, y planificación de la reconstrucción periódica cuando el drift entre el índice y el corpus activo supera umbrales de calidad. La actualización de un documento en un índice vectorial no es una operación in-place como en una base de datos relacional: implica eliminar todos los vectores asociados al documento (identificados por doc_id en los metadatos) e insertar los nuevos vectores generados del documento actualizado; esta operación two-step debe ser atómica desde la perspectiva del sistema o puede producir un estado inconsistente donde coexisten versiones antigua y nueva del mismo documento. Qdrant soporta `upsert` por ID que actualiza o inserta sin duplicados, y `delete` por filtro de payload que elimina todos los vectores donde `doc_id = "valor"` en una sola llamada. La fragmentación del índice HNSW ocurre gradualmente por eliminaciones frecuentes que dejan "huecos" en el grafo; en Qdrant, la operación de `optimize` compacta el índice periódicamente; en Pinecone, el proceso es transparente y gestionado por la plataforma.

## Aspectos operativos críticos del índice

- Estrategia de actualización atómica: implementar un campo `version` o `updated_at` en los metadatos de cada chunk y usar `delete_by_filter({doc_id: X})` seguido de `upsert` de nuevos chunks; garantizar que durante la ventana de actualización el sistema sirva una versión consistente del documento
- Soft delete con campo `is_deleted`: alternativa a la eliminación física que marca chunks como eliminados en metadatos y los excluye mediante filtros en tiempo de búsqueda; permite recuperación en caso de errores pero incrementa el tamaño efectivo del índice con vectores "muertos"
- Optimización periódica del índice: en Qdrant, configurar `optimizer_config` con thresholds de `indexing_threshold` y `memmap_threshold` para balance entre rendimiento de escritura e índice optimizado; reconstrucción completa del índice recomendada mensualmente para corpus con alta tasa de actualizaciones (>20% del corpus mensual)
- Monitoreo de salud del índice: métricas a monitorear incluyen: número de vectores activos vs. eliminados (fragmentation ratio), tiempo de búsqueda p99 en función del tiempo (deterioro indica fragmentación), tasa de error en inserciones (indica problemas de capacidad), y coherencia de metadatos (orphaned chunks sin documento padre)
- Reindexado sin downtime: patrón blue-green para el índice: construir un índice nuevo en paralelo con el índice de producción, redirigir el tráfico de lectura al nuevo índice una vez validado y eliminar el índice antiguo; requiere doble capacidad de almacenamiento temporalmente
- Backups del índice vectorial: Qdrant soporta snapshots nativos de colecciones exportables a S3; pgvector usa el sistema de backup estándar de PostgreSQL (pg_dump, WAL archiving); Pinecone no expone backups directos pero mantiene replicación interna transparente

## Para recordar

El índice vectorial de producción debe tratarse como un sistema de datos con operaciones CRUD completas, políticas de backup, monitoreo de fragmentación y procedimientos documentados de recuperación ante fallos, no como un artefacto estático construido una vez.
