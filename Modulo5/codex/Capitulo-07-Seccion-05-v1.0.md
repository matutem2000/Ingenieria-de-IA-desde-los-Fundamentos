# Módulo 5 – Capítulo 07 – Sección 05

# Evaluación offline vs evaluación online en producción

La evaluación offline ejecuta el sistema de evaluación sobre un dataset estático curado antes del despliegue, con la ventaja de ser controlada, reproducible y de bajo riesgo; la evaluación online ejecuta el sistema de evaluación sobre el tráfico real de producción, con la ventaja de capturar la distribución real de queries y detectar degradaciones que los datasets offline no anticipan. Ambas son necesarias y se complementan: la evaluación offline es el gate de calidad del despliegue y la evaluación online es el sistema de alerta temprana de la operación. La evaluación online puede ser exhaustiva (evaluar el 100% del tráfico con métricas automáticas ligeras como score de longitud, detección de alucinaciones o clasificador de calidad), o por muestreo (evaluar el 1-5% del tráfico con métricas más costosas como LLM-as-judge que requieren llamadas adicionales al modelo). Las señales de feedback implícito del usuario —conversación que termina abruptamente, consulta reformulada inmediatamente, botón de regeneración presionado, feedback negativo explícito— son métricas de evaluación online gratuitas que no requieren una llamada adicional al LLM evaluador.

## Aspectos técnicos de la evaluación online

- Muestreo de tráfico para evaluación: seleccionar aleatoriamente el X% de los requests (stratified sampling por categoría de consulta si el tráfico tiene distribución heterogénea) para evaluación con LLM-as-judge, balanceando profundidad de evaluación vs costo incremental
- Pipeline de evaluación asíncrono: la evaluación online no debe añadir latencia al request del usuario; ejecutarla en un job asíncrono que consume los requests loggueados desde una cola (SQS, Pub/Sub) o directamente desde los logs estructurados en S3
- Señales de feedback implícito: loggear `session_id`, `turn_number`, `time_to_next_message`, `message_length` y `thumbs_up/down` para construir métricas de calidad sin costo de API; la tasa de "edit and resend" es una señal potente de respuesta insatisfactoria
- Dashboard de evaluación online: tabla de métricas en tiempo real (rolling 24h, rolling 7d) con degradación coloreada (rojo si cae >X% respecto al baseline), visible en el canal de operaciones del equipo y consultable vía Grafana o DataDog
- Feedback loop offline: los casos evaluados negativamente en producción (score bajo o feedback negativo del usuario) se añaden semiautomáticamente al dataset offline de evaluación para que los futuros runs de CI detecten regresiones similares

## Principio rector

La evaluación offline sin evaluación online es una ilusión de calidad: el dataset offline siempre es una aproximación de la distribución real del tráfico de producción, y los casos donde el sistema falla en producción son sistemáticamente distintos de los casos del dataset curado.
