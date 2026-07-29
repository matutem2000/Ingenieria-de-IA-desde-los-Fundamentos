# Módulo 11 – Capítulo 09 – Sección 05

# Roadmap de madurez: cómo pasar del nivel actual al siguiente con acciones técnicas concretas

El roadmap de madurez técnica de IA enterprise no es un plan de transformación abstracto sino una secuencia de inversiones de ingeniería específicas que, ejecutadas en orden de prioridad, permiten avanzar un nivel en el modelo de madurez en un horizonte de 3-6 meses por nivel. La transición del Nivel 1 al Nivel 2 (el paso más crítico porque desbloquea todos los demás) requiere tres inversiones concretas: mover todos los notebooks a repositorios Git con revisión de código obligatoria, dockerizar los servicios de inferencia para garantizar la reproducibilidad del entorno, y crear un entorno de staging separado de producción con un pipeline básico de CI/CD que ejecute tests antes de cada despliegue. La transición del Nivel 2 al Nivel 3 (donde el equipo gana control sobre la calidad del sistema) requiere: construir el dataset de evaluación con 100-200 casos de referencia curados por el equipo y los stakeholders de negocio, integrar la evaluación automatizada como gate en el pipeline de CI/CD, y desplegar el prompt registry versionado con la capacidad de hacer rollback de prompts en menos de 5 minutos. La transición del Nivel 3 al Nivel 4 (donde la plataforma se convierte en un activo compartido) requiere: construir el Internal Developer Portal con Backstage para el self-service de nuevos casos de uso, implementar cost allocation por equipo con dashboards de FinOps de IA, y desplegar la detección automática de drift con alertas configuradas. Cada transición de nivel debe planificarse como un proyecto de ingeniería con objetivos medibles, responsables definidos, y criterios de éxito verificables — no como una aspiración de mejora continua sin métricas de progreso.

## Acciones técnicas concretas por transición de nivel

- L1 → L2: repositorios Git para todos los proyectos de IA (1 semana), Dockerfile para cada servicio de inferencia (2-3 semanas), pipeline de CI/CD básico con GitHub Actions (1-2 semanas), entorno de staging separado de producción (2-4 semanas)
- L2 → L3: golden dataset con 200 casos curados (4-6 semanas), integración de evaluación como gate en CI/CD (2-3 semanas), prompt registry con versionado (2-3 semanas), OpenTelemetry para traces de LLM (2-4 semanas)
- L3 → L4: Internal Developer Portal con templates de nuevos casos de uso (8-12 semanas), feature store compartido entre equipos (6-10 semanas), sistema de cost allocation con dashboards (4-6 semanas), detección automática de drift (4-6 semanas)
- L4 → L5: bandit algorithms para model routing dinámico (8-12 semanas), pipeline de reentrenamiento automático activado por drift (10-16 semanas), integración de feedback de negocio en el ciclo de mejora (6-10 semanas)
- Priorización del roadmap: priorizar las inversiones con mayor impacto en las métricas de madurez más rezagadas (la dimensión de evaluación si cobertura < 50%, la dimensión de CI/CD si change failure rate > 20%)

## Idea central

El roadmap de madurez es más efectivo cuando se ancla en las métricas actuales del equipo: la inversión más valiosa es siempre la que mejora la dimensión más rezagada, no la que extiende la dimensión ya más avanzada.
