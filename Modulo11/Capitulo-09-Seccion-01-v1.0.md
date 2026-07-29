# Módulo 11 – Capítulo 09 – Sección 01

# AI maturity model técnico: 5 niveles desde experimentos ad-hoc hasta IA industrializada

El AI maturity model técnico es un marco de evaluación que permite a los equipos de ingeniería medir objetivamente el nivel de sofisticación de sus prácticas de desarrollo, despliegue, y operación de sistemas de IA, proporcionando un roadmap estructurado de mejora con criterios verificables para cada transición de nivel. A diferencia de los modelos de madurez centrados en la capacidad organizacional (como CMMI), este modelo técnico se enfoca en los artefactos, las herramientas, y los procesos de ingeniería concretos: la existencia o ausencia de CI/CD para modelos, la cobertura de evaluaciones automatizadas, el nivel de self-service de la plataforma, y la capacidad de detectar y responder a degradaciones de calidad en producción. El Nivel 1 (Ad-hoc) describe equipos donde los modelos se desarrollan en notebooks sin versionado, se despliegan manualmente subiendo archivos a un servidor, y se monitoran reactivamente cuando un usuario reporta un problema — el estado más común en organizaciones que están comenzando con IA y que típicamente tienen entre 1 y 3 proyectos de IA en producción. El Nivel 5 (Industrializado) describe organizaciones como Google, Meta, o Amazon que tienen plataformas de ML/LLM completamente automatizadas con reentrenamiento continuo activado por señales de drift, experimentación concurrente con decenas de A/B tests en producción, y optimización automática de costos mediante model routing dinámico — un estado alcanzable por las mejores organizaciones enterprise después de 3-5 años de inversión sostenida.

## Los 5 niveles del modelo de madurez técnica de IA

- Nivel 1 — Ad-hoc: notebooks sin versionado de código, datos sin gobernanza formal, despliegues manuales sin CI/CD, monitoreo inexistente o manual, conocimiento concentrado en individuos específicos
- Nivel 2 — Reproducible: código en Git, entornos reproducibles con Docker y requirements.txt/Poetry, pipeline de datos automatizado con Airflow, staging separado de producción, métricas básicas de disponibilidad
- Nivel 3 — Definido: MLflow o similar para tracking de experimentos, evaluaciones automatizadas con golden sets, CI/CD con tests de calidad del modelo como gate, observabilidad con OpenTelemetry, prompt registry versionado
- Nivel 4 — Gestionado: A/B testing de modelos en producción, feature store compartido entre equipos, detección automática de drift con alertas, cost allocation por equipo y caso de uso, self-service de nuevos casos de uso mediante templates
- Nivel 5 — Optimizado: reentrenamiento continuo activado automáticamente por señales de calidad o drift, model routing dinámico con bandit algorithms, retroalimentación del negocio integrada automáticamente en el ciclo de mejora, plataforma con SLA de 99.9%

## Para recordar

La evaluación de madurez debe hacerse con evidencia técnica verificable — logs, dashboards, pipelines ejecutados, métricas reales — no con declaraciones del equipo sobre lo que podría hacerse si fuera necesario.
