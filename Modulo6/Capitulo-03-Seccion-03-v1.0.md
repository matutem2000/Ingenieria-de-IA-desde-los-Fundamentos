# Módulo 6 – Capítulo 03 – Sección 03

# Criterios de selección: escala, latencia, consistencia y gestión de metadatos

Seleccionar la base de datos vectorial adecuada requiere definir primero los requisitos operativos concretos del sistema: el volumen de vectores a indexar (1K, 1M, 1B), la latencia objetivo en el percentil 99 (p99 <50ms, <200ms), el throughput de escritura esperado durante la ingesta (100 docs/s, 10K docs/s), el modelo de consistencia requerido (consistencia eventual vs. strong consistency) y la complejidad de los filtros de metadatos que el sistema necesita aplicar en tiempo de búsqueda. La latencia p99 es la métrica operativa más relevante para sistemas RAG de producción porque las búsquedas de percentil 99 determinan la peor experiencia de usuario; Qdrant en Rust con HNSW alcanza típicamente p99 <10ms para corpus de 1M vectores en memoria, mientras que Pinecone serverless puede tener p99 de 100–300ms por cold start de pods. La gestión de metadatos es crítica cuando el sistema necesita combinar búsqueda semántica con filtros de negocio (fecha_documento > 2024-01-01 AND categoria = "legal" AND usuario_id IN [...]), porque no todas las bases vectoriales tienen soporte eficiente para filtros de alta cardinalidad sin degradar el recall del índice ANN.

## Criterios técnicos de selección

- Escala de vectores: Chroma y Redis VSS para <1M vectores (prototipado, desarrollo); pgvector y Qdrant para 1M–100M vectores con infraestructura propia; Pinecone serverless y Weaviate Cloud para >100M vectores con escalado automático
- Latencia p99: Qdrant (Rust, gRPC) y Milvus son los benchmarks de menor latencia para búsqueda local; Pinecone managed tiene latencia variable por cold start; pgvector tiene p99 comparable a Qdrant para corpus en memoria pero se degrada con corpus que no caben en RAM
- Consistencia de escritura: Pinecone tiene consistencia eventual en escritura (nuevo vector visible en búsqueda en 1–5 segundos); Qdrant y pgvector tienen consistencia sincrónica; crítico para casos de uso donde la respuesta debe reflejar documentos recién ingresados
- Filtrado de metadatos: Qdrant implementa filtrado pre-ANN (calcula el subgrafo de vectores que pasan el filtro antes de buscar), evitando el problema de recall degradado del filtrado post-ANN; Weaviate tiene filtrado nativo integrado en su motor de búsqueda híbrida
- Modelo de despliegue: para equipos con restricciones de soberanía de datos (documentos confidenciales que no pueden salir de la infraestructura propia), Qdrant, Weaviate y pgvector son las únicas opciones; Pinecone y Weaviate Cloud requieren enviar vectores a infraestructura del proveedor
- Operaciones multi-tenant: escenarios donde cada cliente tiene su propia colección aislada; Qdrant soporta namespaces y colecciones dinámicas eficientemente; Pinecone soporta namespaces dentro de un índice con aislamiento lógico pero no físico

## Para recordar

Definir los SLOs (latencia p99, throughput de ingesta, consistencia) antes de evaluar opciones de bases de datos vectoriales; los trade-offs técnicos entre las opciones solo son evaluables en el contexto de los requisitos operativos concretos del sistema.
