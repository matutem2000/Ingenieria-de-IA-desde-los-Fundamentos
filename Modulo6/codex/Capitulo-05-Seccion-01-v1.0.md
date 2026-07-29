# Módulo 6 – Capítulo 05 – Sección 01

# Búsqueda semántica vs búsqueda léxica (BM25): fortalezas y limitaciones de cada una

La búsqueda semántica basada en embeddings vectoriales y la búsqueda léxica basada en BM25 (Best Match 25) son enfoques complementarios con perfiles de fortaleza y debilidad sistemáticamente opuestos, lo que explica por qué los sistemas de recuperación más robustos de producción combinan ambos. BM25 es un algoritmo de ranking probabilístico que extiende TF-IDF con normalización por longitud del documento y saturación de la frecuencia de términos; devuelve resultados de alta precisión cuando los términos de la query aparecen literalmente en el documento, y funciona especialmente bien para queries con términos específicos de dominio (nombres propios, identificadores, códigos, términos técnicos) que el modelo de embedding puede no representar bien porque aparecen raramente en el corpus de entrenamiento. La búsqueda semántica, en cambio, recupera documentos semánticamente relacionados con la query aunque no compartan ni una sola palabra, permitiendo encontrar "fármacos antiinflamatorios" cuando la query dice "medicamentos para el dolor" o "perros de servicio" cuando la query dice "animales de asistencia"; pero falla sistemáticamente con consultas que requieren matching exacto de identificadores, fechas, números o términos técnicos que el embedding no ha visto frecuentemente en entrenamiento.

## Fortalezas y limitaciones técnicas comparadas

- BM25 fortalezas: matching exacto de términos; invariante a la calidad del corpus de entrenamiento; funciona bien para nombres propios, IDs, números de serie, códigos de producto; sin overhead de modelo de embedding en tiempo de consulta; determinista y reproducible; implementado eficientemente con índices invertidos (Elasticsearch, OpenSearch, BM25S)
- BM25 limitaciones: sin comprensión semántica; no recupera sinónimos ni paráfrasis; sensible a vocabulario ("auto" vs. "coche" vs. "vehículo" son tratados como términos distintos); penaliza documentos que usan terminología diferente al de la query aunque el contenido sea idéntico
- Búsqueda semántica fortalezas: recuperación por similitud conceptual independiente del vocabulario; maneja sinónimos, paráfrasis, reformulaciones y consultas en idiomas diferentes al corpus con modelos multilingües; captura intención semántica de queries complejas
- Búsqueda semántica limitaciones: falla con términos OOV (out-of-vocabulary) del corpus de entrenamiento del embedding; número de modelo "GPT-4o-mini" puede tener un embedding similar al de "GPT-4 mini" aunque sean modelos distintos; más costosa computacionalmente que BM25 durante la indexación por las llamadas al modelo de embedding
- Queries que favorecen BM25: "contrato número 2024-LAT-0892", "error ECONNREFUSED", "ivermectina 6mg dosis adultos"; cualquier query con tokens específicos que deban aparecer literalmente en el resultado
- Queries que favorecen búsqueda semántica: "¿cuáles son los efectos secundarios del tratamiento?", "explícame cómo funciona el proceso de aprobación", "ventajas de esta tecnología sobre las alternativas"; queries conceptuales donde el vocabulario de la respuesta puede diferir del de la query

## Para recordar

Ni la búsqueda semántica ni BM25 dominan consistentemente en todos los tipos de queries; un sistema que solo implementa una de las dos tiene un techo de calidad sistemáticamente inferior al que implementa ambas.
