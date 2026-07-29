# Módulo 6 – Capítulo 02 – Sección 04

# Dimensionalidad, normalización y similitud coseno

La dimensionalidad de un vector de embedding tiene implicaciones directas en el costo de almacenamiento, la latencia de búsqueda ANN y la calidad de la recuperación, formando un triángulo de trade-offs que el ingeniero debe calibrar para cada caso de uso. Un vector de 1536 dimensiones (float32) ocupa 6KB; indexar 10 millones de chunks en Pinecone requiere aproximadamente 60GB de memoria VRAM, lo que impacta directamente el costo de la instancia; reducir a 256 dimensiones con MRL (Matryoshka Representation Learning) disminuye el uso de memoria a 10GB con una caída de calidad en MTEB de apenas 2–3 puntos. La normalización L2 de los vectores es una operación estándar que transforma la similitud coseno en un producto punto entre vectores unitarios, simplificando el cómputo a una multiplicación matricial optimizable con BLAS o cuBLAS en GPU; la mayoría de las bases vectoriales asumen vectores normalizados y producen resultados incorrectos si los vectores se insertan sin normalizar. La similitud coseno mide el coseno del ángulo entre dos vectores y es invariante a la magnitud, lo que la hace adecuada para comparar textos de longitudes muy diferentes; su complemento, la distancia coseno = 1 - similitud coseno, convierte la similitud en una métrica de distancia usable en índices de búsqueda.

## Aspectos técnicos de dimensionalidad y métricas

- Matryoshka Representation Learning (MRL): técnica de entrenamiento que permite truncar el vector a dimensiones menores (3072 → 256) manteniendo la mayor parte de la información semántica; implementado en text-embedding-3 de OpenAI y nomic-embed-v1.5
- Normalización L2: operación v_norm = v / ||v||_2 que convierte el vector a longitud unitaria; transforma similitud coseno en producto punto, habilitando optimizaciones SIMD y BLAS de alto rendimiento en tiempo de búsqueda
- Producto punto (dot product) vs similitud coseno: equivalentes para vectores L2-normalizados; el producto punto es preferible en implementación porque es más eficiente computacionalmente; sin normalización, el producto punto favorece vectores de mayor magnitud independientemente del ángulo
- Distancia euclidiana (L2): alternativa a similitud coseno para ciertos modelos de imagen o audio; generalmente inferior a similitud coseno para texto porque la magnitud del vector de embedding depende de la longitud del texto, introduciendo un sesgo no deseado
- Curse of dimensionality en ANN: a medida que la dimensionalidad aumenta, la diferencia entre la distancia al vecino más cercano y al más lejano tiende a cero, degradando la calidad de los índices ANN; modelos con dimensiones >2048 pueden mostrar peor Recall@K en índices HNSW que modelos de 768 dimensiones
- Análisis PCA de embeddings: herramienta de diagnóstico que proyecta los vectores del índice a 2D o 3D para visualizar clustering y detectar problemas como vectores colapsados (baja varianza), clusters espurios o distribuciones anómalas

## Para recordar

Normalizar los embeddings antes de insertarlos en la base vectorial y usar similitud coseno (o producto punto con vectores normalizados) como métrica de distancia son requisitos no negociables para obtener resultados de recuperación correctos y reproducibles.
