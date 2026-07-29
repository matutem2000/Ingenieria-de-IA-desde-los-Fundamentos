# Módulo 11 – Capítulo 07 – Sección 01

# El costo de IA a escala: cómo un sistema eficiente a pequeña escala puede ser insostenible en enterprise

Un sistema de IA que procesa 1.000 peticiones diarias con un costo de 0,05 USD por petición tiene un costo mensual de 1.500 USD — razonable para un piloto o un MVP. El mismo sistema escalado a 1.000.000 de peticiones diarias (un escenario enterprise modesto para una organización de 10.000 empleados con uso frecuente) genera un costo mensual de 1.500.000 USD, que raramente está en el presupuesto operacional de ningún departamento y que convierte la eficiencia de costos de un desiderátum en una restricción de supervivencia del proyecto. El costo de IA a escala enterprise se distribuye entre tres categorías principales: el costo de inferencia (tokens consumidos en llamadas a APIs de LLM de proveedores externos, o costo de GPU para modelos self-hosted), el costo de recuperación (operaciones vectoriales en la base de datos vectorial para el pipeline de RAG, medidas en read units o en segundos de GPU para reranking), y el costo de almacenamiento e indexación (vectores almacenados en la base de datos vectorial, documentos en el data lake, y logs de trazas en los sistemas de observabilidad). La mayoría de los equipos que escalan por primera vez descubren que el costo de inferencia domina el total (típicamente el 70-80%), y que dentro del costo de inferencia, el prompt (el contexto del sistema, el historial de conversación, y los documentos RAG recuperados) puede representar el 80-90% de los tokens consumidos — haciendo de la optimización del prompt la palanca de reducción de costos más poderosa.

## Componentes del costo de IA a escala

- Costo de tokens de entrada: en GPT-4o (2,50 USD/1M tokens de entrada en 2025), un prompt con 4.000 tokens de contexto cuesta 0,01 USD por petición; a 1M peticiones/día, ese costo es 10.000 USD/día
- Costo de tokens de salida: los tokens de salida cuestan típicamente 3-5x más que los de entrada (10 USD/1M tokens de salida en GPT-4o); una respuesta de 500 tokens cuesta 0,005 USD; a 1M peticiones/día, 5.000 USD/día adicionales
- Costo de embeddings: text-embedding-3-large cuesta 0,13 USD/1M tokens; indexar 1M documentos de 1.000 tokens cada uno cuesta 130 USD — un costo único que parece bajo hasta que se recalcula con actualizaciones frecuentes
- Costo de almacenamiento vectorial: Pinecone Serverless cobra por storage y operaciones; a 10M vectores de 1.536 dimensiones, el costo de almacenamiento puede superar los 1.000 USD/mes antes de contar las operaciones de query
- Costo de observabilidad: LangSmith, Langfuse, o sistemas propios de logging de trazas de LLM pueden costar el 5-15% del costo de inferencia si se registran todas las peticiones sin sampling

## Para recordar

Calcular el costo unitario por petición en el piloto y proyectarlo al volumen enterprise estimado debe ser un ejercicio obligatorio antes de comprometer arquitectura de diseño — no después de tener el primer factura sorpresa del proveedor de LLM.
