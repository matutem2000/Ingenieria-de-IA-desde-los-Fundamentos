# Módulo 11 – Capítulo 08 – Sección 02

# HIPAA para IA en salud: requisitos de BAA, cifrado y auditoría para datos de pacientes

La Health Insurance Portability and Accountability Act (HIPAA) regula el manejo de Protected Health Information (PHI) en los Estados Unidos, e impone requisitos técnicos específicos que todo sistema de IA que procesa datos de pacientes debe cumplir: cifrado de PHI en reposo con AES-256 y en tránsito con TLS 1.3, controles de acceso basados en roles con autenticación multifactor, audit logs de cada acceso a PHI que deben retenerse por 6 años, y la firma de Business Associate Agreements (BAA) con todos los proveedores tecnológicos que procesan PHI — incluyendo los proveedores de LLM externos. El BAA es el requisito contractual y técnico más crítico antes de implementar cualquier sistema de IA en salud que envíe PHI a APIs externas: OpenAI ofrece BAA solo para clientes de Enterprise, Anthropic tiene programa equivalente, y Microsoft Azure OpenAI Service ofrece BAA como parte de su oferta enterprise — sin BAA firmado, enviar PHI a una API de LLM es una violación de HIPAA con multas que van desde 100 USD hasta 50.000 USD por violación, con un techo de 1,9 millones USD por categoría por año. Las técnicas de de-identification conforme a HIPAA (Safe Harbor: eliminar 18 tipos específicos de identificadores; Expert Determination: demostrar estadísticamente que el riesgo de re-identificación es muy bajo) permiten procesar datos de pacientes de-identificados con proveedores de LLM sin BAA, pero requieren un proceso riguroso de validación de la de-identificación que debe ser aprobado por un experto en privacidad.

## Requisitos técnicos de HIPAA para sistemas de IA

- Cifrado de PHI: AES-256 para datos en reposo en S3, bases de datos (Transparent Data Encryption en PostgreSQL/RDS), y bases de datos vectoriales; TLS 1.3 para todos los datos en tránsito entre componentes del sistema
- Access Controls y autenticación: RBAC con roles de mínimo privilegio para el acceso a PHI, MFA obligatorio para todos los usuarios con acceso a PHI, y tiempo de sesión máximo configurado (típicamente 15-30 minutos de inactividad)
- Audit logs de HIPAA: registro inmutable de quién accedió a qué PHI, cuándo, desde dónde, y con qué propósito, implementado en un sistema de logging separado (CloudTrail + S3 con Object Lock WORM) con retención de 6 años
- BAA con proveedores cloud y LLM: AWS y GCP ofrecen BAA de cobertura total para sus servicios HIPAA-eligible; para LLMs de terceros, usar solo proveedores con BAA disponible o implementar de-identification antes del envío
- Minimum Necessary PHI en prompts: solo incluir los campos de PHI estrictamente necesarios para la tarea de IA en el prompt — no enviar el historial clínico completo si solo se necesita la lista de diagnósticos activos

## Buena práctica

Crear un registro explícito de todos los lugares del código donde se procesa PHI (código anotado con comentarios # PHI_FIELD y revisado en cada code review), porque la HIPAA aplica a cualquier dato que identifica a un paciente — no solo a los campos marcados como "sensibles" en el esquema.
