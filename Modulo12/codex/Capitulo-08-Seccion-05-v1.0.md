# Módulo 12 – Capítulo 08 – Sección 05

# Monitoreo de drift: detección de degradación de calidad en producción

El monitoreo de drift en el sistema integrador detecta dos tipos de degradación: drift de datos (los documentos en la base de conocimiento se vuelven obsoletos o el perfil de queries de los usuarios cambia) y drift de calidad del modelo (el LLM subyacente recibe una actualización del proveedor que cambia su comportamiento). Para detectar drift de datos, el sistema ejecuta diariamente un análisis de distribución de los scores de relevancia retornados por Cohere Rerank: una caída sostenida en el score medio de reranking indica que las queries de los usuarios están divergiendo del contenido de la base de conocimiento. Para detectar drift de modelo, el sistema ejecuta el golden dataset completo de 200 pares cada 7 días y alerta si faithfulness cae más de 0.05 puntos respecto al baseline establecido en el último deploy. El análisis de distribución de query types (mediante clustering de embeddings de queries de producción) detecta nuevos patrones de uso no cubiertos por el golden dataset, señalando la necesidad de expandir la base de conocimiento o el dataset de evaluación.

## Mecanismos de detección de drift

- Drift de datos: análisis diario de distribución de reranking scores; alerta si score_medio cae > 0.1 en ventana de 7 días
- Drift de modelo: evaluación semanal del golden dataset completo; alerta si faithfulness cae > 0.05 vs baseline del último deploy
- Query distribution drift: clustering semanal de embeddings de queries de producción para detectar nuevos tipos no cubiertos
- Knowledge staleness: análisis de documentos con fecha de modificación > 90 días sin actualización en la base de conocimiento
- Baseline tracking: registro en PostgreSQL de métricas RAGAS por deploy para calcular deltas y detectar regresiones graduales

## Para recordar

El drift de calidad en sistemas de IA es gradual e invisible sin monitoreo activo — la calidad puede degradarse semana a semana sin que ningún indicador de error rate o latencia dispare una alerta, hasta que el usuario finalmente reporta que el sistema "ya no funciona bien".
