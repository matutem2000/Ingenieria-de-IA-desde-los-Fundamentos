# Módulo 11 – Capítulo 01 – Sección 04

# Madurez de IA empresarial: modelo de madurez en 5 niveles para evaluar el estado actual

Un modelo de madurez de IA empresarial proporciona un marco de referencia objetivo para diagnosticar el estado actual de la organización e identificar las acciones técnicas necesarias para avanzar al siguiente nivel, evitando la trampa de implementar capacidades avanzadas sin haber consolidado las fundacionales. Inspirado en el CMMI y adaptado a las particularidades de los sistemas de IA, el modelo distingue cinco niveles que van desde experimentos aislados hasta IA industrializada con mejora continua autónoma: cada nivel tiene prerequisitos técnicos específicos que deben verificarse antes de intentar avanzar. La evaluación de madurez se realiza sobre dimensiones concretas: automatización de pipelines, cobertura de observabilidad, existencia de datasets de evaluación, nivel de self-service para equipos de producto, y tiempo medio de despliegue de un nuevo caso de uso. Sin este mapa, las organizaciones tienden a invertir en componentes del nivel 4 (por ejemplo, fine-tuning automatizado) mientras operan en el nivel 1 (sin CI/CD para modelos), creando deuda técnica que bloquea el progreso.

## Los 5 niveles de madurez técnica

- Nivel 1 — Ad hoc: experimentos en notebooks sin versionado, datos sin gobernanza, despliegues manuales, sin métricas de calidad, dependencia de individuos específicos
- Nivel 2 — Reproducible: pipelines de datos automatizados con Airflow/Prefect, modelos en MLflow, CI/CD básico, entornos de staging separados de producción
- Nivel 3 — Definido: plataforma compartida de ML/LLM, evaluaciones automatizadas con golden sets, observabilidad con OpenTelemetry, gestión de prompts versionada, SLOs definidos
- Nivel 4 — Gestionado: A/B testing de modelos en producción, feature store compartido, cost allocation por equipo, auto-scaling reactivo, reentrenamiento automatizado con detección de drift
- Nivel 5 — Optimizado: experimentación continua con bandit algorithms, optimización automática de costos mediante model routing dinámico, retroalimentación de negocio integrada en el ciclo de mejora

## Buena práctica

Realizar la evaluación de madurez como una auditoría técnica con checklist verificable — no como una encuesta de percepción — es el único modo de obtener un diagnóstico accionable.
