# Módulo 10 – Capítulo 08 – Sección 02

# Model governance: políticas de aprobación antes del despliegue a producción

El model governance es el conjunto de procesos y controles técnicos que garantizan que ningún modelo llega a producción sin haber pasado por los gates de evaluación y aprobación definidos por la organización, adaptando el concepto de "code review" y "deployment approval" al ciclo de vida de los modelos de ML. Un proceso de model governance robusto define para cada categoría de modelo (modelos de recomendación de bajo riesgo, modelos de scoring de crédito de alto riesgo, modelos de decisiones médicas de riesgo crítico) un checklist de aprobación diferenciado: los modelos de bajo riesgo pueden tener aprobación automática si pasan los gates de calidad técnica (métricas sobre umbral, tests de bias dentro de tolerancia, revisión de seguridad de la imagen Docker), mientras que los modelos de alto riesgo requieren revisión humana explícita de un Model Review Board con representación de ingeniería, producto, legal y (para ciertos dominios) compliance. La implementación técnica del model governance se integra directamente en el model registry: el registro de un modelo en el estado "Staging" dispara automáticamente una serie de evaluaciones (bias audit con Fairlearn o AIF360, security scan del artefacto, performance regression test), y solo cuando todas pasan puede iniciarse el proceso de solicitud de aprobación para pasar a "Production". El EU AI Act (en vigor desde 2024) hace que el model governance pase de ser una best practice a un requisito legal para sistemas de IA de alto riesgo, definiendo documentación obligatoria, trazabilidad de datos de entrenamiento, y reportes de evaluación de riesgo.

## Aspectos técnicos del model governance

- Automated gates: evaluaciones automáticas que el modelo debe pasar antes de poder solicitar aprobación: accuracy over threshold, fairness metrics within tolerance, no critical security vulnerabilities in model artifact, latency SLO met in load test
- Bias evaluation: tests automáticos con Fairlearn (`MetricFrame`) o IBM AIF360 que miden la disparidad de métricas (accuracy, precision, recall) entre subgrupos definidos (gender, age, geography); flag automático si la disparidad supera el umbral de política
- Model card generation: documento técnico generado automáticamente con los metadatos del modelo, métricas de evaluación, limitaciones conocidas, datos de entrenamiento usados, y resultados de bias evaluation; requerido antes de la solicitud de aprobación
- Approval workflow: integración con sistemas de ticketing (Jira, ServiceNow) o pull requests de Git para formalizar la solicitud de aprobación, adjuntar el model card, y mantener registro de quién aprobó qué y cuándo
- Audit trail: registro inmutable de cada decisión de aprobación (quién aprobó, en qué fecha, con qué justificación), requerido para demostrar compliance ante reguladores y para investigación de incidentes

## Buena práctica

El model governance efectivo no ralentiza el desarrollo: automatizar la mayor parte posible de los gates (bias evaluation, performance regression, security scan) y reservar la revisión humana solo para los modelos de mayor riesgo garantiza que el proceso agrega valor sin convertirse en cuello de botella.
