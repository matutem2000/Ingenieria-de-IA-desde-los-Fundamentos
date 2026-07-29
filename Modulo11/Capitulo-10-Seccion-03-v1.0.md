# Módulo 11 – Capítulo 10 – Sección 03

# Construcción de plataforma incremental: comenzar simple y añadir componentes según la demanda

La trampa más frecuente en la construcción de plataformas de IA enterprise es el diseño Big Bang: planificar la plataforma completa en el nivel 5 de madurez desde el inicio, con feature stores, bases de datos vectoriales distribuidas, pipelines de reentrenamiento automático, y portales de self-service — y no llegar a producción en 12-18 meses porque la complejidad del sistema excede la capacidad del equipo de construirlo y operarlo simultáneamente mientras atiende las demandas de los equipos de negocio que esperan resultados. La alternativa correcta es la construcción incremental guiada por la demanda: comenzar con la infraestructura mínima que soporte el primer caso de uso real en producción, añadir cada nuevo componente de plataforma solo cuando un segundo o tercer caso de uso lo demanda, y refactorizar la plataforma hacia mayor sofisticación de manera iterativa. La secuencia técnica de construcción incremental parte de tres decisiones mínimas: el proveedor de LLM (OpenAI, Anthropic, o modelo open-source self-hosted), el almacenamiento vectorial para el primer caso de RAG (pgvector sobre PostgreSQL existente para empezar, migrable a Pinecone o Weaviate cuando el volumen lo justifique), y el sistema de versionado de prompts (un directorio en Git con naming convention explícita es suficiente para el primer caso de uso, antes de invertir en un prompt registry completo). Los siguientes componentes se añaden a medida que los casos de uso los demandan: el pipeline de evaluación automatizada cuando el equipo tiene el primer golden dataset con 100 casos, el sistema de observabilidad LLM cuando los equipos necesitan debuggear problemas de calidad en producción, y el portal de self-service cuando el tercer equipo quiere usar la plataforma y el equipo de plataforma se convierte en cuello de botella.

## Secuencia de construcción incremental de plataforma

- Fase 0 (semanas 1-4): LLM API key + Python wrapper + logging básico + deployment en Docker — suficiente para el primer experimento de producción con un equipo piloto
- Fase 1 (meses 1-3): pgvector para RAG + prompts en Git con naming convention + evaluación manual con golden set de 50 casos + CI/CD básico con GitHub Actions que ejecuta los tests de evaluación
- Fase 2 (meses 3-6): OpenTelemetry para traces de LLM + prompt registry en PostgreSQL + base de datos vectorial dedicada (Pinecone o Weaviate) cuando el volumen supera los 100.000 vectores + cost allocation básico por tag
- Fase 3 (meses 6-12): Internal Developer Portal con Backstage + golden dataset de 200+ casos con evaluación automática + A/B testing de modelos + feature store compartido para los primeros 3 equipos
- Fase 4 (12+ meses): detección automática de drift + model routing dinámico + portal de self-service completo + reentrenamiento continuo para los casos de uso con suficientes datos de feedback

## Principio rector

Cada componente de plataforma se añade cuando existe un caso de uso real que lo demanda — no cuando el equipo tiene tiempo disponible para construirlo, ni cuando aparece en la arquitectura de referencia ideal.
