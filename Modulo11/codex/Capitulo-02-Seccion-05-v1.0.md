# Módulo 11 – Capítulo 02 – Sección 05

# Landing zones de IA: entornos isolados para desarrollo, staging y producción

Una landing zone de IA enterprise es un entorno cloud pre-configurado y pre-aprobado que provee la infraestructura base necesaria para desplegar sistemas de IA de manera segura y conforme a las políticas corporativas, eliminando el tiempo de aprovisionamiento ad hoc que cada equipo dedicaría a configurar VPCs, roles IAM, buckets de S3, y políticas de red desde cero. La arquitectura de landing zones para IA define al menos tres entornos con separación explícita: desarrollo (donde los Data Scientists e ingenieros de IA experimentan con datos anonimizados o sintéticos, sin acceso a datos de producción), staging (réplica de producción con datos de prueba reales bajo las mismas políticas de seguridad, donde se validan los cambios antes del despliegue final), y producción (entorno con datos reales de negocio, acceso restringido, audit logging activo, y cambios gestionados mediante change management formal). La separación no es solo lógica mediante namespaces de Kubernetes: debe ser física a nivel de cuentas de AWS/subscripciones de Azure/proyectos de GCP, con políticas de Service Control Policies (AWS SCP) o Azure Policy que impidan, por ejemplo, que desde una cuenta de desarrollo se acceda a datos de producción aunque el desarrollador tenga las credenciales necesarias. El aprovisionamiento de nuevas landing zones se automatiza con Infrastructure as Code (Terraform, Pulumi, o AWS CDK) ejecutado desde pipelines de CI/CD con aprobación de un equipo de plataforma.

## Componentes de una landing zone de IA

- Aislamiento de red: VPC dedicada por entorno con subnets privadas para los servicios de IA, NAT Gateway para salida controlada a internet, y Private Link para acceso a APIs de LLM sin tráfico público
- Gestión de identidad y acceso: roles IAM por función (ingenieros de IA, Data Scientist, Operator) con principio de mínimo privilegio, MFA obligatorio, y acceso Just-In-Time para operaciones privilegiadas
- Almacenamiento de datos: buckets S3/GCS/ADLS con cifrado SSE-KMS, versionado activado, políticas de retención según clasificación de datos, y acceso bloqueado a datos de producción desde entornos inferiores
- Registro y auditoría: CloudTrail/Cloud Audit Logs habilitado en todos los servicios, logs retenidos mínimo 12 meses, y alertas automáticas para acciones de alto riesgo (borrado de datos, cambios de política IAM)
- Guardrails automatizados: AWS Config Rules, Azure Policy, o GCP Organization Policies que verifican continuamente el cumplimiento de las políticas de seguridad y generan alertas o bloqueos automáticos

## Buena práctica

La landing zone de IA debe ser el camino de menor resistencia para los equipos: si configurarla por fuera es más fácil que usarla, los equipos la evitarán y con ello eludirán los controles de seguridad y cumplimiento.
