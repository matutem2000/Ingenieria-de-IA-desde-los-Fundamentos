# Módulo 6 – Capítulo 03 – Sección 04

# Filtrado híbrido: combinar búsqueda vectorial con filtros de metadatos

El filtrado híbrido es la capacidad de ejecutar búsquedas que combinan similitud semántica vectorial con predicados booleanos sobre metadatos estructurados (fecha, categoría, autor, permisos de acceso) en una sola operación eficiente. En sistemas de producción, prácticamente toda consulta real requiere algún filtro de metadatos: un asistente legal solo debe recuperar documentos de un cliente específico, un chatbot de soporte solo debe consultar documentos de la versión de producto relevante, un sistema de cumplimiento solo debe mostrar regulaciones vigentes después de cierta fecha. La implementación naive del filtrado vectorial realiza primero la búsqueda ANN y luego filtra por metadatos los resultados (post-filtering), lo que produce un recall degradado cuando el filtro elimina una fracción grande del corpus; Qdrant resuelve esto con pre-filtering, construyendo dinámicamente un subgrafo del índice HNSW restringido a los vectores que pasan el filtro y ejecutando la búsqueda ANN sobre ese subgrafo. Weaviate implementa una variante similar con su motor de inverted index integrado que combina BM25 sobre texto plano con filtros de propiedades y búsqueda vectorial en un solo pipeline.

## Aspectos técnicos del filtrado híbrido

- Post-filtering: recuperar los top-K*N vectores más cercanos y filtrar por metadatos; simple de implementar pero requiere sobrerecuperar (K*N) para compensar los documentos que no pasan el filtro, degradando latencia y recall cuando el filtro es selectivo (elimina >70% del corpus)
- Pre-filtering (Qdrant): construir dinámicamente una vista filtrada del índice HNSW y ejecutar la búsqueda ANN sobre esa vista; mantiene recall@K incluso con filtros muy selectivos; más complejo de implementar pero indispensable en producción con filtros de alta selectividad
- Índice invertido acoplado: Pinecone y Weaviate mantienen un índice invertido separado sobre los metadatos, ejecutando primero la búsqueda en el índice invertido para obtener el conjunto de IDs elegibles y luego la búsqueda ANN restringida a ese conjunto
- Filtros de payload en Qdrant: soporte para tipos de filtro ricos: Match (equality), Range (numérico y datetime), GeoRadius (coordenadas geográficas), IsNull, IsEmpty, HasId; anidables con operadores must, should, must_not equivalentes a AND, OR, NOT
- Cardinalidad del filtro como variable crítica: filtros de baja selectividad (category = "legal" retiene el 30% del corpus) son manejables con post-filtering; filtros de alta selectividad (user_id = "uuid-específico" retiene el 0.01% del corpus) requieren pre-filtering obligatoriamente
- Namespaces y particionamiento: estrategia alternativa al filtrado donde el corpus se divide en colecciones o namespaces separados por tenant o categoría; elimina la necesidad de filtrado pero incrementa la complejidad operativa de gestión del índice

## Buena práctica

Diseñar el esquema de metadatos del índice vectorial al mismo tiempo que la estrategia de chunking, identificando los filtros que el sistema necesitará aplicar en producción y eligiendo una base vectorial cuyo modelo de filtrado sea compatible con esos patrones de acceso.
