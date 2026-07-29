# Módulo 6 – Capítulo 06 – Sección 05

# Evaluación continua en producción: detecting drift y degradaciones

La evaluación continua en producción es la práctica de monitorear sistemáticamente la calidad del sistema RAG sobre tráfico real, detectando degradaciones antes de que los usuarios las reporten. Los sistemas RAG degradan en producción por múltiples causas: el corpus cambia (documentos actualizados, nuevos documentos sobre temas no cubiertos, eliminación de documentos clave), la distribución de queries cambia (nuevas categorías de preguntas, cambios en la terminología de los usuarios), el modelo de embedding puede quedar obsoleto o dejar de estar disponible por decisión de su proveedor, lo que puede exigir una reindexación, o el LLM generador actualiza su comportamiento entre versiones. El monitoring de producción para RAG requiere trazar cada solicitud con su query, los chunks recuperados (con sus scores de similitud), la respuesta generada y, opcionalmente, el feedback del usuario (thumbs up/down, clic en la fuente citada, reformulación de la query como señal implícita de insatisfacción). Herramientas como LangSmith (LangChain), Phoenix (Arize), TruLens y Langfuse implementan observabilidad específica para pipelines LLM con trazabilidad completa de cada componente y dashboards de métricas agregadas.

## Componentes del monitoring de calidad en producción

- Tracing completo del pipeline: instrumentar cada etapa del pipeline RAG (query embedding, búsqueda vectorial, reranking, generación) con spans de trazabilidad compatible con OpenTelemetry; registrar latencia, tokens consumidos, IDs de chunks recuperados y scores para cada solicitud
- Feedback implícito como proxy de calidad: monitorear señales de insatisfacción: queries seguidas de reformulación en <30 segundos (señal de respuesta incorrecta), sesiones que terminan sin interacción posterior (posible respuesta inaceptable), clic en fuentes citadas (señal positiva de utilidad del RAG)
- Evaluación asíncrona con LLM-as-judge: para un sample aleatorio del 1–5% de las consultas de producción, ejecutar automáticamente una evaluación de faithfulness y answer relevancy usando un LLM evaluador; agregar los scores diariamente y alertar si caen más de 10 puntos porcentuales vs. baseline
- Embedding drift detection: calcular la distribución de scores de similitud coseno de las búsquedas diarias y monitorear cambios en la distribución (desplazamiento de la media, aumento de varianza); un shift significativo puede indicar que el corpus del índice está desalineado con las queries actuales de los usuarios
- Concept drift en queries: usar clustering de embeddings de queries de producción para detectar aparición de nuevos clusters de temas no cubiertos por el corpus; alertar cuando más del X% de las queries caen en un cluster con Recall@5 bajo estimado
- Alertas y SLOs de calidad: definir SLOs de calidad (faithfulness >0.75, answer relevancy >0.70) y configurar alertas cuando los valores caigan por debajo del umbral durante más de 24 horas; integrar con sistemas de on-call (PagerDuty, OpsGenie) para degradaciones severas

## Buena práctica

Implementar tracing completo de producción desde el primer despliegue, aunque el sistema sea un MVP; los datos de producción son irreemplazables para entender el comportamiento real del sistema y detectar problemas que no aparecen en los datasets de evaluación sintéticos.
