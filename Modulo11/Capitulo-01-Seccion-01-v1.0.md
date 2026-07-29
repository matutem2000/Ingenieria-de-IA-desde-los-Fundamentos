# Módulo 11 – Capítulo 01 – Sección 01

# Los desafíos únicos del enterprise: escala, heterogeneidad, cumplimiento y legado

Desplegar IA en contextos enterprise no es simplemente escalar un prototipo: implica operar sobre infraestructuras que combinan mainframes IBM z/OS, bases de datos Oracle de décadas de antigüedad, APIs SOAP que solo viven en intranets, y sistemas modernos de Kubernetes en la nube, todo bajo requisitos estrictos de GDPR, SOC 2 e ISO 27001. La escala introduce problemas que no existen en pilotos: latencia de red entre zonas de disponibilidad, contención de recursos bajo carga concurrente de miles de usuarios simultáneos, y costos de inferencia que pueden superar los presupuestos de infraestructura si no se gestionan con modelos de cost allocation por unidad de negocio. La heterogeneidad tecnológica obliga al AI Engineer a diseñar capas de abstracción que normalicen fuentes de datos con formatos incompatibles: JSON, XML, COBOL copybooks, EDI, y Parquet coexisten en el mismo pipeline. El cumplimiento normativo no es una capa que se agrega al final, sino una restricción de diseño que afecta desde el esquema del modelo de datos hasta el contrato de retención de logs de auditoría.

## Dimensiones críticas del contexto enterprise

- Escala de usuarios concurrentes: sistemas enterprise manejan picos de 10.000 a 100.000 RPM que requieren auto-scaling reactivo con Kubernetes HPA y KEDA
- Heterogeneidad de datos: pipelines que deben consumir fuentes OLTP (PostgreSQL, Oracle), data warehouses (Snowflake, BigQuery) y data lakes (S3, ADLS) en un mismo contexto de inferencia
- Cumplimiento regulatorio activo: requisitos de GDPR Art. 25 (privacy by design), HIPAA Security Rule, y PCI-DSS afectan el diseño de cada componente del sistema
- Integración con sistemas legacy: conectores hacia SAP R/3, Salesforce SFDC, y APIs SOAP/XML que no soportan cambios sin ventanas de mantenimiento planificadas
- Restricciones de gobernanza interna: modelos de aprobación de despliegues con Change Advisory Boards (CAB) que introducen lead times de semanas entre el desarrollo y la producción

## Principio rector

Los desafíos enterprise no son variantes de los desafíos de startup — son problemas de una categoría distinta que exigen disciplina de ingeniería de sistemas por encima de la sofisticación del modelo.
