# Módulo 10 – Capítulo 02 – Sección 03

# Multi-tenancy: aislamiento de recursos, costos y datos entre equipos

El multi-tenancy en una plataforma de IA es la capacidad de servir a múltiples equipos desde la misma infraestructura compartida garantizando que ningún equipo puede afectar el rendimiento de otro (noisy neighbor), acceder a los datos o modelos de otro (aislamiento de datos), o incurrir en costos que no se le atribuyan correctamente (accountability financiera). En Kubernetes, el aislamiento se implementa mediante namespaces con ResourceQuotas (límites de CPU, memoria y GPU por equipo), NetworkPolicies que restringen el tráfico entre namespaces, y RBAC con ServiceAccounts específicos por equipo. Para el aislamiento de datos, cada equipo recibe prefijos de S3 o buckets GCS propios con IAM policies que impiden el acceso cruzado, y el feature store (Feast) usa proyectos separados con entity ownership por equipo. La atribución de costos se implementa mediante labels de Kubernetes (`team=nlp-squad`, `project=search-ranking`) que se propagan a las métricas de AWS Cost Explorer o GCP Billing, y mediante un servicio de chargeback interno que asigna el costo de cada Pod-hour de GPU al equipo propietario.

## Puntos críticos del multi-tenancy

- Aislamiento de cómputo: Kubernetes LimitRanges y ResourceQuotas por namespace, con PriorityClasses para garantizar que los jobs de producción no sean desalojados por jobs de experimentación
- Aislamiento de red: NetworkPolicies que permiten solo el tráfico explícitamente autorizado; los servicios de plataforma (registry, feature store) tienen egress permitido desde todos los namespaces bajo autenticación
- Aislamiento de datos: object storage con prefijos por equipo y IAM conditions que impiden acceso cruzado; encriptación por equipo con KMS keys distintas para datos sensibles
- Chargeback técnico: etiquetado obligatorio de recursos (team, project, environment) validado por webhook de admisión; reportes automáticos de costo por equipo generados semanalmente
- Aislamiento de modelos en el registry: MLflow usa experiments con permisos por usuario/equipo; SageMaker Model Registry usa model groups con política de IAM que restringe acceso por equipo

## Idea central

El multi-tenancy exitoso hace invisible la compartición de recursos: cada equipo percibe que tiene su propia infraestructura, sin saber que está compartiendo el mismo cluster de A100s con otros diez equipos.
