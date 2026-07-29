# Módulo 6 – Capítulo 10 – Sección 06

# Cierre: los patrones avanzados de RAG son respuestas a limitaciones concretas del sistema

Self-RAG, Adaptive RAG, Corrective RAG, FLARE y Agentic RAG no son innovaciones académicas desconectadas de la práctica sino respuestas ingenieriles a problemas concretos y frecuentes que los equipos de producción encuentran en sus sistemas RAG: el RAG estándar recupera siempre aunque a veces el modelo ya tiene la respuesta (Self-RAG lo soluciona); el mismo pipeline de recuperación es ineficiente para todos los tipos de queries (Adaptive RAG lo soluciona); el retriever a veces devuelve chunks irrelevantes que producen hallucinations (Corrective RAG lo soluciona); el modelo a veces necesita recuperar información específica en mitad de la generación (FLARE lo soluciona); algunas queries requieren múltiples ciclos de recuperación secuenciales (Agentic RAG lo soluciona). El criterio de adopción de cada patrón debe ser empírico: identificar el tipo de error más frecuente en el sistema mediante análisis de logs y métricas de evaluación, y adoptar el patrón que específicamente resuelve ese tipo de error. Adoptar Agentic RAG sin haber identificado que las queries multi-step son frecuentes en el sistema es sobreingeniería; ignorar Corrective RAG cuando el análisis muestra que el 20% de las respuestas incluyen hallucinations por retrieval fallido es negligencia de ingeniería.

*"The art of making systems simple again is harder than making complex ones. It takes more skill, more insight, and more courage."* — Leslie Lamport, Premio Turing 2013, sobre el diseño de sistemas distribuidos correctos y simples

## Principio rector

Adoptar patrones avanzados de RAG únicamente cuando el análisis de métricas y errores identifica el problema que resuelven como causa de degradación medible en el sistema; la complejidad adicional de cada patrón tiene un costo operativo que debe ser justificado por la mejora de calidad que aporta.
