# Módulo 10 – Capítulo 06 – Sección 05

# GitOps para MLOps: infraestructura como código y despliegue declarativo

GitOps aplica el principio de que el estado deseado de toda la infraestructura y configuración del sistema se describe declarativamente en un repositorio Git, y un operador automático (ArgoCD, Flux) se encarga de reconciliar continuamente el estado real del cluster con el estado declarado en Git. En el contexto de MLOps, GitOps cubre tres dimensiones: la infraestructura de la plataforma (definición de namespaces de Kubernetes, ResourceQuotas, NetworkPolicies, IngressRoutes mediante Helm charts o Kustomize manifestados en Git), la configuración de los modelos en producción (los InferenceService de KServe con la versión del modelo, los parámetros de scaling y los recursos de CPU/GPU se definen en YAML en Git, no se modifican con kubectl directo), y los pipelines de MLOps (las definiciones de los DAGs de Airflow o los Prefect Deployments se versionan en Git y se despliegan automáticamente al mergearse). El beneficio de GitOps para MLOps es la auditabilidad completa: toda modificación al sistema pasa por un pull request con revisión, el historial de Git contiene cuándo, quién y qué cambió en la configuración de cualquier modelo en producción, y `git revert` es el mecanismo de rollback de infraestructura. ArgoCD sincroniza automáticamente cuando se mergea un cambio al repositorio de configuración, ejecutando `kubectl apply` o `helm upgrade` y reportando el estado de la sincronización en su UI y vía webhooks.

## Aspectos técnicos de GitOps para MLOps

- Repository structure: separar el repo de código de entrenamiento del repo de configuración de despliegue (config-as-code); el pipeline de CI actualiza automáticamente el config repo cuando un nuevo modelo pasa los gates de calidad
- ArgoCD Application: recurso de Kubernetes que define qué directorio del repositorio Git mapea a qué namespace del cluster, con sync policy (manual o automático) y configuración de pruning de recursos eliminados
- Helm charts para modelos: un chart parametrizado que acepta `model_uri`, `replicas`, `cpu_limit`, `memory_limit` como values; el CI actualiza el `values.yaml` con la nueva versión del modelo y ArgoCD aplica el cambio
- Promotion workflow: el pipeline de entrenamiento crea un PR automático al config repo con la nueva versión del modelo; un humano aprueba el PR para promover a producción, creando un audit trail completo
- Secret management: los secretos (API keys, credenciales) no se almacenan en Git sino en HashiCorp Vault o AWS Secrets Manager; las referencias a secretos (External Secrets Operator) sí se almacenan en Git de forma segura

## Buena práctica

El repositorio de configuración de GitOps para MLOps debe ser el único origen de verdad sobre qué versión de qué modelo está en producción: cualquier cambio manual con kubectl que no pase por Git debe ser considerado una violación de proceso y un riesgo de auditoría.
