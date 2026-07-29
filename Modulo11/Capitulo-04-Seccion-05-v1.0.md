# Módulo 11 – Capítulo 04 – Sección 05

# Escalabilidad y cost allocation: crecer con nuevos tenants sin degradación de servicio

Una plataforma multi-tenant de IA debe escalar tanto en el eje vertical (más recursos por tenant existente cuando aumenta su uso) como en el eje horizontal (más tenants sin degradar la experiencia de los tenants actuales), y el diseño para esta escalabilidad bifurcada requiere decisiones arquitectónicas explícitas desde el primer día que no pueden agregarse retroactivamente sin costo significativo de refactorización. El auto-scaling en plataformas multi-tenant de IA opera con señales más complejas que el CPU utilization típico: el KEDA (Kubernetes Event-Driven Autoscaling) puede escalar el número de pods de inferencia basándose en el largo de la cola de mensajes de Kafka por tenant, el número de requests pendientes en Redis, o métricas de negocio personalizadas como el número de usuarios activos por tenant en los últimos 5 minutos. El cost allocation por tenant es crítico para el modelo de negocio de la plataforma y para el showback/chargeback interno en plataformas privadas: cada petición de inferencia debe registrar el tenant_id, el modelo utilizado, el número de tokens de entrada y salida (para calcular el costo exacto de la llamada al LLM), los recursos de cómputo consumidos (GPU seconds para inferencia self-hosted), y el número de operaciones vectoriales ejecutadas. Con estos datos disponibles en un sistema de métricas (ClickHouse, BigQuery, o Prometheus con Thanos para retención larga), el equipo de plataforma puede generar facturas por tenant con granularidad diaria o mensual, y los líderes de negocio pueden ver el costo de IA desagregado por unidad de negocio.

## Componentes de escalabilidad y cost allocation

- KEDA para auto-scaling reactivo: escalado horizontal de pods de inferencia y orquestación basado en métricas de Kafka consumer lag, Redis queue length, o métricas de Prometheus expuestas por la aplicación
- Horizontal Pod Autoscaler (HPA) con métricas personalizadas: escalar basándose en tokens_per_second_in_flight por modelo, ajustando el número de réplicas del servicio de inferencia según la demanda real
- Chargeback por token consumido: registro en ClickHouse de cada inferencia con tenant_id, model_id, input_tokens, output_tokens, latency_ms, y costo calculado (precio_por_token × tokens_consumidos)
- Resource quotas por tenant en Kubernetes: LimitRanges y ResourceQuotas por namespace de tenant que garantizan que un tenant no puede consumir más de su cuota asignada de CPU y memoria del cluster
- Dashboard de costos por tenant: Grafana conectado a ClickHouse mostrando costo diario, tendencia mensual, desglose por modelo y operación, y alerta cuando el gasto proyectado supera el presupuesto asignado al tenant

## Para recordar

El cost allocation por tenant no es una feature a implementar cuando haya tiempo: sin él, es imposible tomar decisiones de precio del producto, identificar tenants no rentables, o justificar la inversión en la plataforma ante el liderazgo.
