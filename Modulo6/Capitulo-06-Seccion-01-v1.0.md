# Módulo 6 – Capítulo 06 – Sección 01

# El problema de evaluar RAG: múltiples componentes y métricas en conflicto

Evaluar un sistema RAG es intrínsecamente más complejo que evaluar un modelo de clasificación o un LLM en aislamiento porque el sistema completo tiene al menos dos subsistemas con métricas propias y parcialmente en conflicto: el retriever (medido por Recall@K, MRR, NDCG) y el generador (medido por faithfulness, answer relevancy, coherencia). Un retriever que maximiza Recall@K recuperando muchos chunks puede degradar la calidad de la generación si introduce chunks no relevantes que confunden al LLM o superan el límite de su ventana de contexto; un generador que produce respuestas muy concisas puede tener alta faithfulness pero baja answer relevancy si omite aspectos importantes de la query. La evaluación end-to-end debe medir la calidad de la experiencia completa del usuario (¿la respuesta final es correcta y útil?) y la calidad de cada componente de forma aislada (¿el retriever recupera lo correcto? ¿el generador usa fielmente el contexto?), manteniendo la capacidad de diagnosticar en qué etapa se introduce la degradación cuando los resultados empeoran. Frameworks como RAGAS, DeepEval y TruLens implementan conjuntos de métricas que intentan cubrir todos los aspectos del sistema RAG en un pipeline de evaluación ejecutable automáticamente, reduciendo la dependencia de la evaluación humana manual para ciclos de iteración rápidos.

## Dimensiones del problema de evaluación

- Desacoplamiento de métricas de retriever y generador: evaluar el retriever con Recall@K requiere un ground truth de qué chunks son relevantes para cada query; evaluar el generador requiere un ground truth de qué respuesta es correcta; estos datasets de evaluación deben construirse por separado y pueden ser inconsistentes
- Faithfulness vs. answer completeness: un sistema que siempre responde "no tengo información suficiente" tiene faithfulness perfecta pero answer relevancy cero; optimizar una sola métrica puede degradar las otras; necesidad de métricas compuestas o umbrales mínimos en todas las dimensiones
- Evaluación con LLM como juez (LLM-as-judge): usar un LLM (GPT-4o, Claude 3 Opus) como evaluador automático de calidad de respuestas es el método más escalable pero introduce sesgos del modelo evaluador (preferencia por respuestas verbosas, sesgo de posición, consistencia variable); requiere calibración contra evaluación humana
- Golden dataset representativo: el dataset de evaluación debe cubrir la distribución real de queries de producción (factual, comparativo, multi-hop, temporal, ambiguo); un golden dataset sesgado hacia queries simples produce métricas infladas que no predicen la experiencia real del usuario
- Evaluación de componentes intermedios: además del retriever y el generador, evaluar la calidad del chunking (¿los chunks tienen cohesión semántica?), de los metadatos (¿son correctos y completos?) y de los embeddings (¿los vectores similares corresponden a contenidos semánticamente relacionados?)
- Ciclo de evaluación continua: la evaluación no es un evento único sino un proceso continuo que debe ejecutarse en cada cambio del pipeline (nuevo modelo de embedding, nueva estrategia de chunking, actualización del corpus) para detectar regresiones antes de que afecten a usuarios de producción

## Para recordar

Definir la suite de métricas de evaluación del sistema RAG antes de comenzar el desarrollo, no al final; los datos de evaluación son tan importantes como los datos del corpus y deben ser construidos con el mismo rigor de ingeniería.
