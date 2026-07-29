# Módulo 11 – Capítulo 08 – Sección 05

# Compliance as code: automatizar la verificación de cumplimiento en el pipeline de CI/CD

Compliance as code es el enfoque de implementar las verificaciones de cumplimiento regulatorio como código ejecutable en el pipeline de CI/CD, en lugar de como procesos manuales periódicos de auditoría interna — transformando el cumplimiento de un evento puntual en una verificación continua que detecta desviaciones en minutos en lugar de en meses. Las verificaciones de cumplimiento codificables incluyen: análisis estático de código (SAST con Semgrep o Bandit) para detectar patrones prohibidos como credenciales hardcodeadas, logging de datos personales sin enmascarar, o uso de funciones criptográficas deprecadas; análisis de dependencias (SCA con Snyk o OWASP Dependency Check) para identificar librerías con CVEs conocidas que violan la política de vulnerabilidades; análisis de infraestructura como código (IaC scanning con Checkov, tfsec, o AWS CloudFormation Guard) para detectar configuraciones que violan las políticas de seguridad (buckets S3 públicos, grupos de seguridad con puertos abiertos a 0.0.0.0/0, instancias sin cifrado de disco); y policy-as-code con herramientas como Open Policy Agent (OPA) o Kyverno para Kubernetes que evalúan en tiempo real si los pods desplegados cumplen con las políticas de seguridad del cluster (no privileged, read-only filesystem, resource limits definidos). La integración de estas verificaciones como gates en el pipeline de CI/CD (usando GitHub Actions, GitLab CI, o Jenkins) garantiza que ningún código que viole las políticas de cumplimiento puede llegar a producción sin la aprobación explícita de una excepción.

## Componentes del compliance as code pipeline

- SAST para PII y seguridad: Semgrep con rulesets para GDPR (detección de logging de datos personales), HIPAA (detección de PHI hardcodeada), y seguridad general (inyección SQL, XSS, use de eval()), ejecutado en cada PR antes del merge
- SCA para vulnerabilidades de dependencias: Snyk o Dependabot en el pipeline de CI que falla el build si se detectan CVEs de severidad alta o crítica sin patch disponible, con revisión semanal automatizada de nuevas vulnerabilidades en dependencias existentes
- IaC scanning con Checkov: análisis de todos los archivos Terraform, CloudFormation, y Kubernetes YAML en el pipeline para detectar misconfigurations de seguridad, con umbral de "fail on HIGH" configurado y proceso de excepción documentado
- Open Policy Agent (OPA) como admission controller: políticas Rego que verifican cada objeto Kubernetes antes de admitirlo al cluster, rechazando pods sin resource limits, con imágenes no escaneadas, o con permisos excesivos
- Compliance dashboard automatizado: generación automática de evidencia de cumplimiento a partir de los logs del pipeline de CI/CD (qué verificaciones pasaron, cuándo, con qué versión de código), exportable para auditorías SOC 2 o ISO 27001 sin trabajo manual adicional

## Idea central

Cuando el cumplimiento se verifica automáticamente en cada commit, los desarrolladores reciben feedback inmediato sobre las violaciones y las corrigen en el mismo contexto de trabajo — a diferencia de las auditorías periódicas donde las violaciones se descubren semanas después de que el código ya está en producción.
