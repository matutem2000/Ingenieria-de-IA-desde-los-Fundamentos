# Módulo 6 – Capítulo 03 – Sección 01

# Fundamentos: índices HNSW, IVF y búsqueda aproximada de vecinos más cercanos (ANN)

La búsqueda exacta del vecino más cercano (exact kNN) en un corpus de millones de vectores requiere comparar el vector de consulta contra todos los vectores del índice, lo que escala como O(N×D) y es inviable a escala de producción: encontrar los 10 vecinos más cercanos en 10 millones de vectores de 1536 dimensiones requeriría aproximadamente 30 segundos en CPU, y menos de 1 segundo con GPU de alta gama pero a un costo prohibitivo. Los algoritmos de Approximate Nearest Neighbor (ANN) resuelven este problema sacrificando una fracción de exactitud (recall) a cambio de latencia y costo drásticamente menores. HNSW (Hierarchical Navigable Small World), el algoritmo dominante en producción, construye un grafo multi-capa donde cada capa superior es una versión submuestreada del nivel inferior, permitiendo navegar desde nodos de alta conectividad en capas superiores hasta los vecinos más precisos en la capa base; su complejidad de búsqueda es O(log N) con un recall@10 típico del 95–99%. IVF (Inverted File Index) particiona el espacio vectorial en clusters mediante k-means y en tiempo de búsqueda solo examina los ncentros más cercanos al vector de consulta, acelerando la búsqueda a costa de mayor fragmentación de memoria y menor recall en particiones pequeñas.

## Conceptos técnicos de índices ANN

- HNSW (Hierarchical Navigable Small World): índice de grafo multi-capa; parámetros clave son M (número de conexiones por nodo, típicamente 16–64) y ef_construction (tamaño de la cola de búsqueda durante construcción, 100–400); construido en RAM, búsqueda en microsegundos con recall >96%
- IVF (Inverted File Index): divide el espacio en nlist clusters (típicamente sqrt(N)); en búsqueda examina nprobe clusters (nprobe=nlist da búsqueda exacta); compresión IVF+PQ (Product Quantization) reduce memoria 8–32x a costa de 3–8% de recall
- SCANN (Scalable Nearest Neighbors, Google): algoritmo que combina particionamiento anisótropo con compresión asimétrica; superior a HNSW en recall/latencia para corpus de >100M vectores; disponible en Google Vertex AI Vector Search
- NSW (Navigable Small World): base teórica de HNSW; grafo plano de mundo pequeño donde cada nodo conecta con sus M vecinos más cercanos durante la inserción; HNSW agrega la jerarquía de capas para mejorar la fase de entrada al grafo
- Recall vs. latencia trade-off: en HNSW, aumentar ef_search (tamaño de la cola durante la búsqueda) mejora recall a costa de latencia; ef_search=50 da ~95% recall en <5ms, ef_search=400 da >99% recall en ~15ms para corpus de 1M vectores en CPU moderno
- Flat index: índice exacto que examina todos los vectores; útil como baseline de evaluación o para corpus menores a 100K vectores donde la latencia exacta es aceptable

## Para recordar

HNSW es el algoritmo de ANN de referencia para producción debido a su alto recall, latencia predecible y buen comportamiento incremental (permite insertar nuevos vectores sin reconstruir el índice completo); IVF+PQ es preferible cuando las restricciones de memoria son críticas a escala de cientos de millones de vectores.
