# Módulo 10 – Capítulo 05 – Sección 04

# Alertas inteligentes: umbrales adaptativos vs estáticos para sistemas de IA

Los sistemas de alerta basados en umbrales estáticos (alertar cuando la latencia p99 supera 2000ms) son insuficientes para modelos de IA en producción porque las métricas de estos sistemas tienen estacionalidad y varianza natural significativa: la latencia puede ser sistemáticamente más alta los lunes por la mañana por patrones de uso, y un umbral fijo calibrado para evitar alertas en horas pico generará false negatives durante las horas normales. Los umbrales adaptativos calculan dinámicamente el umbral de alerta basándose en el comportamiento histórico reciente de la métrica: Grafana Alerting soporta alertas basadas en percentiles de una ventana temporal (`alert if current_value > percentile_95(metric[-7d])`), y Prophet (de Meta) puede modelar la estacionalidad semanal y diaria de las métricas para generar umbrales que se ajustan automáticamente al contexto temporal. Para las métricas de calidad de modelo (drift score, LLM-as-a-judge score), los umbrales adaptativos son aún más importantes: el nivel "normal" de drift de un modelo puede cambiar después de un reentrenamiento, y el umbral de alerta debe recalibrarse automáticamente en lugar de requerir ajuste manual. La estrategia de alertas efectiva para sistemas de IA combina alertas de síntoma (latencia alta, error rate elevado) que disparan inmediatamente, con alertas de causa raíz (drift de features, degradación de calidad de modelo) que disparan con mayor tolerancia temporal pero avisan antes de que el problema llegue a los usuarios.

## Aspectos técnicos de alertas inteligentes

- Alertas de síntoma: latencia p99, error rate, throughput; umbrales estáticos son aceptables para estos porque tienen rangos operativos bien definidos e impacto inmediato en usuarios
- Alertas de calidad de modelo: drift score (KS statistic, PSI), LLM judge score, factual accuracy; requieren umbrales adaptativos porque el baseline cambia con cada reentrenamiento del modelo
- Detección de anomalías con Z-score: alertar cuando una métrica supera mean ± 3*std calculados sobre una ventana deslizante de 7-30 días; efectivo para métricas con distribución aproximadamente normal
- CUSUM (Cumulative Sum Control Chart): detecta cambios sutiles y sostenidos que no disparan alertas de Z-score; especialmente útil para concept drift gradual en métricas de calidad de modelo
- Alert fatigue management: usar dead man's switch para alertas de data freshness, agregación de alertas correlacionadas (PagerDuty Grouping o Alertmanager), y silenciamiento automático durante despliegues planificados

## Principio rector

Una alerta que se ignora habitualmente es peor que ninguna alerta: la calibración de umbrales para minimizar false positives es tan importante como la sensibilidad para detectar problemas reales.
