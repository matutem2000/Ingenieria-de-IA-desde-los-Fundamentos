# Módulo 11 – Capítulo 01 – Sección 01

## Los desafíos únicos del enterprise: escala, heterogeneidad, cumplimiento y legado

El Módulo 10 de este libro construyó la plataforma de IA: el feature store, el model registry, el serving infrastructure, y los fundamentos de gobernanza y MLOps que permiten a un equipo operar sistemas de machine learning con disciplina técnica. Ese módulo respondió la pregunta de cómo construir la base. Este módulo responde una pregunta distinta: cómo operar esa base cuando el contexto es un enterprise con decenas de miles de empleados, décadas de sistemas heredados, requisitos regulatorios no negociables, y una organización donde el cambio técnico requiere aprobación de comités. La diferencia no es de grado sino de naturaleza. Lo que aquí empieza no es la continuación del Módulo 10, sino su aplicación bajo condiciones de fricción máxima.

Desplegar IA en contextos enterprise no es simplemente escalar un prototipo: es operar sobre infraestructuras que combinan mainframes IBM z/OS, bases de datos Oracle de décadas de antigüedad, APIs SOAP que solo viven en intranets corporativas, y sistemas modernos de Kubernetes en la nube, todo bajo requisitos estrictos de GDPR, SOC 2 e ISO 27001. Estas restricciones no son obstáculos administrativos que desaparecen con el tiempo: son propiedades estructurales del entorno en el que el sistema de IA debe funcionar, y deben incorporarse al diseño desde el primer día.

La escala introduce problemas que no existen en pilotos. La latencia de red entre zonas de disponibilidad, la contención de recursos bajo carga concurrente de miles de usuarios simultáneos, y los costos de inferencia que pueden superar los presupuestos operacionales si no se gestionan con modelos de cost allocation por unidad de negocio son fenómenos que solo emergen cuando el tráfico deja de ser sintético. Un sistema que procesa 50 peticiones por minuto en staging puede colapsar ante 5.000 peticiones concurrentes en producción no porque el modelo sea incorrecto, sino porque la capa de orquestación no fue diseñada para ese nivel de paralelismo.

La heterogeneidad tecnológica obliga al AI Engineer a diseñar capas de abstracción que normalicen fuentes de datos con formatos incompatibles. JSON, XML, COBOL copybooks, EDI X12, y Parquet coexisten en el mismo pipeline de datos. Cada formato refleja la era en que fue creado el sistema que lo genera, y la integración de todos ellos en un contexto unificado que pueda alimentar un LLM es, por sí misma, un proyecto de ingeniería de meses. El cumplimiento normativo completa el cuadro: no es una capa que se agrega al final del desarrollo, sino una restricción de diseño que afecta desde el esquema del modelo de datos hasta el contrato de retención de logs de auditoría.

> **Nota del Arquitecto:** El error más frecuente al entrar a un proyecto de IA enterprise es subestimar el tiempo de integración con los sistemas existentes. En proyectos con los que he trabajado, la integración con el legado consumió entre el 40% y el 60% del tiempo total de desarrollo, mientras que la lógica de IA propiamente dicha consumió el 20%. Planificar inversamente produce proyectos que llegan al plazo con el modelo perfeccionado y sin la integración funcional.

## Dimensiones críticas del contexto enterprise

- **Escala de usuarios concurrentes:** sistemas enterprise manejan picos de 10.000 a 100.000 RPM que requieren auto-scaling reactivo con Kubernetes HPA y KEDA, con señales de escalado basadas en consumer lag de Kafka o longitud de cola de inferencia, no solo en CPU utilization.
- **Heterogeneidad de datos:** pipelines que deben consumir fuentes OLTP (PostgreSQL, Oracle), data warehouses (Snowflake, BigQuery) y data lakes (S3, ADLS) en un mismo contexto de inferencia, con capas de normalización que garantizan que el LLM recibe datos en un formato coherente independientemente de su origen.
- **Cumplimiento regulatorio activo:** requisitos de GDPR Art. 25 (privacy by design), HIPAA Security Rule, y PCI-DSS afectan el diseño de cada componente del sistema; no son verificaciones de fin de proyecto sino restricciones de arquitectura.
- **Integración con sistemas legacy:** conectores hacia SAP R/3, Salesforce SFDC, y APIs SOAP/XML que no soportan cambios sin ventanas de mantenimiento planificadas y aprobaciones formales del equipo de TI corporativo.
- **Restricciones de gobernanza interna:** modelos de aprobación de despliegues con Change Advisory Boards (CAB) que introducen lead times de semanas entre el desarrollo y la producción, y que requieren documentación técnica de change requests con análisis de impacto y plan de rollback verificable.

---

**Principio rector:** Los desafíos enterprise no son variantes de los desafíos de startup — son problemas de una categoría distinta que exigen disciplina de ingeniería de sistemas por encima de la sofisticación del modelo.

Este capítulo establece el mapa del territorio. Las secciones siguientes recorren cada dimensión del stack enterprise en detalle: la arquitectura de referencia que organiza las cuatro capas del sistema, el modelo de madurez que permite diagnosticar el estado actual de la organización, y el rol del AI Engineer que debe navegar la complejidad técnica y la complejidad organizacional con la misma destreza.
