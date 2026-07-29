# Módulo 12 – Capítulo 09 – Sección 03

# Runbook operativo: procedimientos para los incidentes más frecuentes

El runbook operativo del sistema integrador documenta los cinco incidentes más frecuentes en producción con procedimientos step-by-step que incluyen comandos concretos, consultas de diagnóstico y criterios de resolución. Cada entrada del runbook sigue la misma estructura: título del incidente, síntomas observables (alerta disparada + comportamiento del usuario), diagnóstico (comandos kubectl, consultas Prometheus/Loki para confirmar la causa raíz), acciones de mitigación inmediata (pasos con comandos completos, no descripción de alto nivel), escalation (cuándo y a quién escalar si la mitigación no funciona en 15 minutos), y cierre (verificación de que el sistema volvió a estado normal y post-mortem si aplica). Los cinco incidentes cubiertos son: alta latencia P95 (cuello de botella en LLM o reranker), error_rate > 5% (dependency failure de OpenAI o Qdrant), degradación de faithfulness (drift de datos o modelo), pod OOM (memory leak en pipeline de ingesta), y alerta de rate limiting agresivo (posible abuso o bug del cliente).

## Incidentes documentados en el runbook

- Alta latencia P95: diagnóstico con spans de Grafana Tempo, comandos kubectl top pods, acciones de escalado horizontal
- Error rate > 5%: verificación de health de OpenAI/Qdrant/Cohere, activación de circuit breaker y fallback degradado
- Degradación de faithfulness: comparación con baseline en Prometheus, diagnóstico de drift de datos o cambio de modelo LLM
- Pod OOM: kubectl describe pod para evento OOM, análisis de memory profile, ajuste de resource limits y requests
- Rate limiting agresivo: análisis de logs Loki por user_id, bloqueo temporal de usuario si es abuso, fix de bug si es cliente legítimo

## Para recordar

Un runbook es efectivo cuando permite a un ingeniero con conocimiento general del sistema (no el que lo diseñó) resolver el incidente en su turno de guardia — si el procedimiento asume conocimiento implícito, necesita más detalle.
