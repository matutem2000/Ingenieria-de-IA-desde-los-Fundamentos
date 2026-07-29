# Módulo 11 – Capítulo 01 – Sección 02

# De proyectos piloto a producción: las brechas que impiden la escala

El 85% de los proyectos de IA no llegan a producción según reportes de Gartner y McKinsey, y la causa rara vez es la calidad del modelo: es la ausencia de infraestructura de soporte para operarlo en condiciones reales. Un piloto exitoso en un Jupyter Notebook con datos de muestra enfrenta en el camino a producción una brecha técnica compuesta por cinco dimensiones acumulativas: gobernanza de datos, observabilidad, integración con sistemas existentes, gestión del ciclo de vida del modelo, y seguridad. La infraestructura de un piloto suele ser ad hoc — un contenedor Docker lanzado manualmente, prompts hardcodeados en el código fuente, y evaluaciones manuales —, mientras que producción enterprise exige pipelines de CI/CD, feature stores versionados con herramientas como Feast o Tecton, y sistemas de evaluación automatizada con métricas de negocio cuantificables. La brecha más crítica y menos evidente es la de confianza operacional: los equipos de operaciones e infraestructura necesitan runbooks, alertas calibradas, y SLOs definidos antes de aceptar la transferencia de un sistema de IA a su responsabilidad.

## Brechas técnicas que bloquean la escala

- Brecha de reproducibilidad: entornos de desarrollo sin gestión de dependencias explícitas (Poetry, Conda lockfiles) producen "funciona en mi máquina" en la transición a staging
- Brecha de observabilidad: ausencia de trazas distribuidas (OpenTelemetry), métricas de latencia de inferencia por percentil (p50, p95, p99), y logs estructurados con correlation IDs
- Brecha de datos: pipelines manuales de preparación de datos que no están automatizados con Airflow, Prefect o dbt, haciendo imposible el reentrenamiento o la actualización continua
- Brecha de evaluación: falta de un test suite de evaluación automática con datasets dorados (golden sets) que validen la calidad del modelo antes de cada despliegue
- Brecha de seguridad y acceso: ausencia de gestión de secretos con Vault o AWS Secrets Manager, y de políticas IAM que restrinjan el acceso al modelo en producción

## Para recordar

La transición de piloto a producción no es un problema de ajuste fino del modelo, sino de construcción de la infraestructura de soporte que lo rodea.
