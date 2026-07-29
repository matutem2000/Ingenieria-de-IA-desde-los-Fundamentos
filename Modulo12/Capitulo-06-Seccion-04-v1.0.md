# Módulo 12 – Capítulo 06 – Sección 04

# Estrategia de despliegue: blue-green o canary para el modelo y el sistema completo

El proyecto implementa una estrategia de despliegue canary para el sistema completo, donde cada nueva versión recibe inicialmente el 5% del tráfico de producción durante 30 minutos, luego el 25%, luego el 50%, y finalmente el 100% si las métricas de calidad y error rate se mantienen dentro de los umbrales. El canary se implementa con Argo Rollouts, que maneja el balanceo de tráfico entre las versiones stable y canary mediante VirtualService de Istio; el análisis automático de métricas en cada step evalúa: error rate < 1%, latencia P95 < 3500ms y faithfulness RAGAS >= 0.82 medida sobre queries muestreadas en tiempo real. Si cualquier métrica viola su umbral durante el análisis, Argo Rollouts ejecuta un rollback automático en menos de 2 minutos sin intervención manual. Para cambios en el pipeline RAG que requieren re-indexación (cambio de modelo de embedding o parámetros de chunking), se usa una estrategia blue-green: se provisiona una colección paralela en Qdrant, se re-indexa, se valida con el golden dataset y se hace el cutover atómico con zero downtime.

## Configuración de la estrategia canary

- Argo Rollouts: canary steps al 5%, 25%, 50%, 100% con pausa entre steps y análisis automático de métricas
- Análisis de métricas: AnalysisTemplate con queries a Prometheus para error_rate, p95_latency y métricas custom de RAGAS
- Rollback automático: triggered cuando error_rate > 1% o p95_latency > 3500ms durante el periodo de análisis
- Blue-green para RAG: colección paralela en Qdrant con re-indexación completa antes del cutover atómico
- Notificaciones: hooks de Argo Rollouts a Slack con step actual, métricas de análisis y estado del rollout

## Para recordar

El canary deployment con análisis automático de métricas es la estrategia óptima para sistemas de IA en producción — detecta degradaciones de calidad antes de que afecten al 100% de los usuarios, con rollback automático que no requiere intervención manual.
