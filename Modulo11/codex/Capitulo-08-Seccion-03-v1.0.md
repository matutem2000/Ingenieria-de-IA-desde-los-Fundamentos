# Módulo 11 – Capítulo 08 – Sección 03

# SOC 2 Type II para plataformas de IA: controles técnicos requeridos para la certificación

SOC 2 Type II es el estándar de auditoría de seguridad más relevante para plataformas de IA B2B enterprise en el mercado norteamericano: los clientes enterprise exigen el reporte SOC 2 Type II como prerequisito para contratar, y obtenerlo requiere demostrar a un auditor externo (CPA firma especializada) que los controles de seguridad definidos en los cinco Trust Service Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy) han estado operando de manera efectiva durante un período mínimo de 6 meses (Type II, a diferencia de Type I que es solo una instantánea). Los controles técnicos requeridos para SOC 2 en plataformas de IA incluyen: gestión de acceso con revisiones de acceso trimestrales (demostrar que los usuarios que ya no necesitan acceso son desprovisionados), gestión de vulnerabilidades con escaneos semanales y remediación de vulnerabilidades críticas en menos de 30 días (usando herramientas como Snyk, Dependabot, o AWS Inspector), cifrado de datos con gestión documentada de claves (rotación anual mínima de KMS keys), y monitoreo de seguridad con alertas para comportamientos anómalos (GuardDuty en AWS, Security Center en Azure). La certificación SOC 2 Type II para plataformas de IA introduce controles adicionales específicos al dominio: procedimientos de revisión del comportamiento del modelo antes de cada despliegue a producción, documentación de los casos de entrenamiento y fine-tuning, y controles para detectar prompt injection y otros ataques específicos de sistemas LLM.

## Controles técnicos clave para SOC 2 en plataformas de IA

- Logical Access Controls: provisioning automático de acceso basado en roles (SCIM con Okta), revisión trimestral de accesos con evidencia exportable, y offboarding automatizado que revoca todos los accesos en menos de 24 horas tras la baja del empleado
- Change Management: proceso documentado de code review (mínimo 1 aprobación para PRs en ramas de staging, 2 aprobaciones para ramas de producción), pipeline de CI/CD con tests automatizados como gate obligatorio, y registro de todos los deploys en el log de cambios
- Encryption Management: inventario documentado de todos los datos en reposo y en tránsito con el tipo de cifrado aplicado, proceso de rotación de KMS keys con evidencia de última rotación, y prohibición de credenciales hardcodeadas verificada con herramientas de SAST (Semgrep, GitLeaks)
- Incident Response: plan de respuesta a incidentes documentado con RTO y RPO definidos, ejercicios de simulación de incidente al menos anuales con evidencia del resultado, y proceso de notificación a clientes afectados en menos de 72 horas
- Vulnerability Management: escaneos de dependencias en el pipeline de CI/CD (Snyk, Dependabot), escaneos de infraestructura semanales (AWS Inspector, Trivy para imágenes Docker), y SLA de remediación por severidad (crítico: 7 días, alto: 30 días)

## Principio rector

SOC 2 Type II no se obtiene en el mes previo a la auditoría: requiere 6 meses de controles operando y registrados — comenzar el programa de seguridad desde el primer día de la plataforma es la única manera de obtenerlo sin retrasos costosos.
