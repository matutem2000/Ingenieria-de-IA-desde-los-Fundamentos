# Módulo 6 – Capítulo 04 – Sección 01

# Por qué el chunking determina la calidad de la recuperación

El chunking es el proceso de dividir los documentos del corpus en fragmentos indexables y es, posiblemente, la decisión de ingeniería con mayor impacto en la calidad final de un sistema RAG: un chunking deficiente produce chunks que o bien cortan contexto semántico crítico en el punto medio de una idea, o bien son tan grandes que diluyen la señal semántica hasta hacer imposible que el embedding capture la información relevante del fragmento. El problema fundamental es que el modelo de embedding produce un único vector que representa todo el contenido del chunk: si el chunk contiene información sobre tres temas distintos, el vector estará en algún punto promediado del espacio semántico que no captura bien ninguno de los tres temas, reduciendo el score de similitud coseno con queries específicas de cualquiera de ellos. Investigaciones empíricas sobre benchmarks de recuperación como BEIR muestran que la variación en la estrategia y los parámetros de chunking puede producir diferencias de hasta 15–20 puntos porcentuales en Recall@5, mayor que el impacto de cambiar el modelo de embedding de una versión a otra del mismo proveedor. El chunking no es solo un problema de tamaño sino de granularidad semántica: el chunk ideal contiene exactamente la información necesaria para responder un tipo específico de query sin incluir información irrelevante que dilute el vector.

## Puntos críticos del chunking

- Granularidad semántica: el chunk ideal contiene una unidad de información coherente (un procedimiento, una definición, un argumento) que puede ser recuperada de forma independiente sin perder su significado por falta de contexto circundante
- Impacto del chunk en el vector embedding: chunks de más de 512 tokens tienden a producir vectores promediados que capturan temas múltiples y tienen menor similitud coseno con queries específicas; chunks de menos de 50 tokens tienen insuficiente contexto semántico para el embedding
- Context bleeding: fenómeno donde información de un tema al final del chunk se mezcla con información de otro tema al inicio, produciendo vectores de baja calidad que no representan bien ninguno de los dos temas adyacentes
- Dependencia del dominio: el chunking óptimo varía según el tipo de contenido; documentos legales con artículos y subarticulos se benefician de chunking por estructura jerárquica; artículos científicos, de chunking por sección; FAQs, de chunking por par pregunta-respuesta
- Impacto en el generador: chunks demasiado cortos proporcionan contexto insuficiente al LLM generador que puede necesitar información del párrafo anterior para responder; chunks demasiado largos consumen tokens de contexto innecesarios y elevan el costo de inferencia
- Evaluación empírica del chunking: la única forma de validar una estrategia de chunking es medir Recall@K en un dataset de evaluación representativo; no existe un tamaño universal óptimo; 512 tokens con 10% overlap es un punto de partida razonable que raramente es el óptimo

## Para recordar

El chunking es la decisión de preprocessing más impactante en RAG y debe evaluarse experimentalmente con el corpus y las queries reales del caso de uso, no elegirse arbitrariamente basándose en valores por defecto de los frameworks.
