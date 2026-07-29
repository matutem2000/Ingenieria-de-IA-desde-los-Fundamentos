# Módulo 5 – Capítulo 09 – Sección 05

# Monitoreo y alertas de costos: dashboards y umbrales de gasto

El monitoreo de costos en sistemas de IA debe operar en tres horizontes temporales: tiempo real (alertas ante spikes anómalos de gasto en los últimos 15-60 minutos), diario (costo total y breakdown por feature/usuario/modelo del día anterior), y mensual (tendencias, proyecciones y comparación vs presupuesto). Los proveedores ofrecen dashboards de costos propios (OpenAI Usage Dashboard, Anthropic Console) con granularidad por día y por API key, pero carecen de la dimensión de negocio: no saben qué feature interno generó cada request. La solución es construir la dimensión de negocio en el sistema de logging propio: cada llamada al LLM se loggea con `feature`, `user_segment`, `prompt_version`, y el costo calculado localmente (`(input_tokens * price_in + output_tokens * price_out)`); este log alimenta un data warehouse o una herramienta de análisis (Grafana, Metabase, DataDog) que permite queries como "¿cuánto costó el feature de resumen de emails en la última semana y cuál fue el top 10 de usuarios por gasto?". Las alertas de costo deben configurarse en dos niveles: alertas del proveedor (OpenAI y Anthropic permiten configurar email alerts ante umbral mensual) y alertas propias basadas en el gasto calculado en el sistema de logging (alerta inmediata si el gasto en 15 minutos supera N veces el promedio histórico de 15 minutos).

## Aspectos técnicos del monitoreo de costos

- Cálculo local del costo en cada request: tabla de precios como config (`PRICING = {"claude-3-5-sonnet-20241022": {"input": 3.0, "output": 15.0, "cache_read": 0.30, "cache_write": 3.75}}`) y `cost = (in_tok * p["input"] + out_tok * p["output"]) / 1_000_000` loggueado como `cost_usd` en cada request
- Dashboard de costos en Grafana: panel de "Costo por hora (rolling 24h)" con alerta si supera el percentil 95 histórico, panel de "Top features por costo (last 7d)" con breakdown por `feature` y `model`, y panel de "Proyección mensual" que extrapola el gasto diario promedio al mes
- Alertas de anomalía: CloudWatch Anomaly Detection o Grafana Alerting con modelo de predicción de gasto basado en el histórico detecta spikes anómalos automáticamente sin requerir definir un umbral estático; útil para sistemas con variabilidad de uso alta
- Budget alerts del proveedor: configurar en el OpenAI Dashboard o Anthropic Console alertas al 50%, 80% y 100% del presupuesto mensual asignado por proyecto/API key; estas alertas son el respaldo contra bugs de loop infinito o ataques de prompt injection que generan llamadas masivas no deseadas
- Atribución de costos por equipo: en organizaciones con múltiples equipos usando el mismo proyecto de API, usar diferentes API keys por equipo o por ambiente, o bien añadir un campo `team` en el logging de costos, para que la atribución de gastos sea precisa en las reuniones de revisión de presupuesto

## Buena práctica

El costo de construir el sistema de monitoreo de costos en las primeras semanas del proyecto es invariablemente menor que el costo de descubrir un bug de loop infinito o un prompt mal diseñado que multiplicó el gasto por 100x en la primera factura mensual.
