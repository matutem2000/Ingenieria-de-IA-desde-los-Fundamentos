# Módulo 12 – Capítulo 08 – Sección 04

# Alertas: configuración de umbrales y runbooks para los incidentes más probables

Las alertas del sistema integrador se configuran en Grafana Alerting con reglas que evalúan métricas de Prometheus y Loki cada 60 segundos, con un periodo de pending de 3 minutos para evitar falsos positivos por picos transitorios. Las alertas críticas (que despiertan al ingeniero de guardia) son: error_rate > 5% durante 3 minutos, latencia_P95 > 5000ms durante 3 minutos, y Qdrant/OpenAI API unavailable (health check falla 3 veces consecutivas). Las alertas de advertencia (notifican en Slack sin despertar a nadie) son: faithfulness_ragas < 0.80 (posible drift de calidad), latencia_P95 > 3500ms (degradación de rendimiento no crítica), y costo_por_hora > 1.5x el promedio de las últimas 24h. Cada alerta tiene un runbook asociado en la documentación técnica que describe: cómo confirmar el problema, las primeras acciones de mitigación (con comandos concretos), las causas más probables y el escalation path si las acciones iniciales no resuelven el incidente.

## Configuración de alertas por severidad

- CRITICAL: error_rate > 5% por 3 min, P95 > 5s por 3 min, dependency unavailable — PagerDuty + Slack #incidents
- WARNING: faithfulness < 0.80, P95 > 3.5s, costo_hora > 1.5x promedio — Slack #ai-ops sin notificación urgente
- INFO: tasa de rechazo por injection > 10 req/min, colección Qdrant > 80% capacidad — Slack #ai-ops log
- Runbook links: cada alerta incluye URL al runbook específico con comandos kubectl y consultas de diagnóstico
- Silencing: procedimiento de silenciado de alertas durante mantenimiento programado con duración máxima de 4 horas

## Para recordar

Una alerta sin runbook es ruido — el ingeniero que la recibe a las 3am necesita saber exactamente qué comandos ejecutar para diagnosticar y mitigar el problema, sin tener que reconstruir el procedimiento desde cero bajo presión.
