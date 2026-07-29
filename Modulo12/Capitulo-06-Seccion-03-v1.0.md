# Módulo 12 – Capítulo 06 – Sección 03

# Infraestructura como código: Terraform o Pulumi para provisionar el entorno de producción

La infraestructura del sistema integrador se provisiona con Terraform usando el provider de AWS, con el estado almacenado en un S3 bucket con DynamoDB para locking distribuido. Los recursos principales son: un cluster EKS (Elastic Kubernetes Service) con node groups de instancias c5.xlarge para las cargas de trabajo compute-intensive, una instancia RDS PostgreSQL para el almacenamiento del estado del agente (LangGraph persistence) y los audit logs, y un deployment de Qdrant Cloud como servicio administrado para la base vectorial en producción. La organización de los módulos Terraform sigue una estructura de tres capas: networking (VPC, subnets, security groups), compute (EKS, node groups, IAM roles) y services (RDS, Qdrant Cloud, ElastiCache Redis). Los módulos se parametrizan por entorno (dev/staging/prod) usando workspaces de Terraform, con archivos `.tfvars` por entorno que definen tamaños de instancia, número de réplicas y configuración de autoscaling.

## Componentes de infraestructura como código

- State backend: S3 bucket con versionado + DynamoDB table para state locking y prevención de conflictos concurrentes
- Módulo networking: VPC con subnets públicas y privadas en 3 AZs, NAT Gateway y security groups por capa
- Módulo compute: EKS v1.30 con managed node groups c5.xlarge, cluster autoscaler y IRSA para permisos IAM por pod
- Módulo services: RDS PostgreSQL 16 multi-AZ para persistencia, ElastiCache Redis para colas Celery
- Parametrización por entorno: workspaces Terraform con .tfvars que definen instance_type, min_nodes, max_nodes por entorno

## Para recordar

La infraestructura como código no es solo documentación ejecutable — es el control de versiones de la infraestructura, que permite auditar qué cambió, cuándo y por quién, y revertir a un estado anterior si un cambio causa un incidente.
