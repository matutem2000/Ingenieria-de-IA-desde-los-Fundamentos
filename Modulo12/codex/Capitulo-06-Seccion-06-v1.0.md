# Módulo 12 – Capítulo 06 – Sección 06

# Cierre: el despliegue automatizado es lo que distingue un experimento de un sistema operacional

El capítulo de MLOps del proyecto final cierra el ciclo entre el desarrollo y la operación: la containerización con Docker multi-stage produce imágenes reproducibles; el pipeline CI/CD con gate de evaluación garantiza que solo las versiones que mantienen la calidad llegan a producción; la infraestructura como código en Terraform permite provisionar entornos idénticos en minutos; el canary deployment con Argo Rollouts minimiza el riesgo de cada despliegue; y la gestión de secrets con AWS Secrets Manager garantiza que las credenciales nunca toquen el código. Este conjunto de prácticas convierte el sistema integrador de un prototipo funcional en un producto operacional que puede desplegarse, monitorearse, revertirse y auditarse. La diferencia entre un ingeniero que construye prototipos y un ingenieros de IA que opera sistemas en producción es precisamente este conjunto de capacidades: no solo hacer funcionar el modelo, sino garantizar que siga funcionando, con calidad medible, después del primer despliegue.

## Aspectos técnicos que integra este capítulo

- Dockerfile multi-stage: usuario no-root, hash verification de dependencias, health check integrado
- Pipeline CI/CD: build + test + evaluate (gate RAGAS) + deploy con kubectl rollout status
- Terraform: S3 backend, EKS cluster, RDS PostgreSQL, parametrización por entorno con workspaces
- Canary deployment: Argo Rollouts con análisis automático de métricas y rollback automático sub-2-minutos
- Secrets management: AWS Secrets Manager + External Secrets Operator con rotación automática sin downtime

## Para recordar

El deploy automatizado no es una característica opcional — es la condición necesaria para poder iterar sobre el sistema con confianza, sabiendo que cada cambio pasa por las mismas puertas de calidad y seguridad.

*"Infrastructure as code is the practice of managing and provisioning infrastructure through machine-readable configuration files rather than manual processes." — Kief Morris, Infrastructure as Code*
