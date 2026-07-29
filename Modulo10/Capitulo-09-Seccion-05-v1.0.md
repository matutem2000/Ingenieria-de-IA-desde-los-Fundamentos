# Módulo 10 – Capítulo 09 – Sección 05

# Presupuestos y alertas: controles de gasto antes de que los costos escalen

Los controles de presupuesto en una plataforma de IA deben implementarse como guardrails técnicos que previenen que el gasto escale descontroladamente, no solo como reportes que informan del daño después de que ocurrió. La diferencia es crítica: un modelo de IA que empieza a ser llamado en un loop infinito por un bug en la aplicación cliente puede generar miles de dólares de costos en minutos; sin un control de hard stop cuando se alcanza el presupuesto diario del equipo, el incidente se detecta solo en la factura mensual. Los controles de gasto se implementan en múltiples capas: el LLM Gateway puede tener un disyuntor de gasto por equipo que rechaza peticiones (HTTP 429) cuando el gasto acumulado del día supera el presupuesto diario configurado; los cloud providers ofrecen Budget Alerts (AWS Budgets, GCP Budget Alerts) que notifican y pueden detener recursos cuando se alcanzan umbrales; y los sistemas de orquestación de pipelines pueden ser configurados para no lanzar training jobs cuando el gasto mensual del equipo ha superado su cuota. Las alertas de presupuesto son útiles pero insuficientes si no van acompañadas de acción automática: la buena práctica es definir tres niveles de respuesta automatizada: alerta informativa al 80% del presupuesto (Slack notification), reducción de tráfico al modelo más barato al 100% (automatic model downgrade), y bloqueo completo de nuevas llamadas al 110% (hard stop con HTTP 429).

## Controles técnicos de presupuesto para plataformas de IA

- Daily spend limits en LLM Gateway: presupuesto diario configurable por equipo en USD; el gateway lleva un contador en Redis del gasto acumulado del día y rechaza peticiones cuando se supera el límite, retornando HTTP 429 con header `Retry-After`
- AWS Budgets / GCP Budget Alerts: alertas nativas del cloud provider a 50%, 80%, 100% del presupuesto mensual; configurables para enviar notificaciones a SNS/Pub-Sub y disparar acciones automáticas (detener instancias EC2 si el presupuesto se supera)
- Training job cost estimation: antes de lanzar un training job, el sistema estima el costo basándose en la configuración (instance type, número de instancias, duración estimada) y requiere aprobación explícita si el costo supera un umbral configurable
- Anomaly detection de gasto: alertas cuando el gasto diario supera mean + 2*std del gasto histórico de los últimos 30 días; indicativo de un bug de producción (loop infinito) o de un cambio no planificado en el volumen de uso
- Cost circuit breaker: mecanismo automático que detiene el autoescaling de los pods de serving cuando el costo proyectado del día supera el presupuesto, manteniendo el número de réplicas actual hasta revisión manual

## Principio rector

Un presupuesto de IA sin controles técnicos de enforcement es una expectativa, no un límite: la diferencia entre una expectativa y un límite real se evidencia en el primer incidente de costo inesperado.
