# Módulo 10 – Capítulo 02 – Sección 05

# Evolución de la plataforma: de scripts ad-hoc a plataforma gobernada

La evolución de una plataforma de IA sigue un patrón predecible documentado por múltiples organizaciones: primero aparecen scripts de bash o Python que automatiza un ingeniero para resolver su propio problema de infraestructura (Nivel 0), luego esos scripts se comparten informalmente entre equipos hasta que se vuelven un punto de dolor cuando fallan en entornos distintos (Nivel 1), después alguien los convierte en un proyecto interno con documentación básica (Nivel 2), y finalmente la organización invierte en construir una plataforma real con SLOs, equipo dedicado y roadmap (Nivel 3). El paso más crítico en esta evolución es la transición del Nivel 1 al Nivel 2: en ese momento es necesario refactorizar los scripts ad-hoc en APIs con contratos explícitos, añadir tests automatizados, establecer un proceso de pull request y revisión, y crucialmente, asignar ownership claro a alguien responsable de mantener el sistema. Google clasifica esta evolución en su MLOps maturity model en tres niveles: MLOps Level 0 (entrenamiento manual), MLOps Level 1 (pipelines automatizados), y MLOps Level 2 (CI/CD completo para pipelines de ML); la plataforma es la infraestructura que hace posible escalar desde el nivel 0 al nivel 2.

## Etapas de evolución técnica

- Nivel 0 – Scripts ad-hoc: entrenamiento manual con notebooks de Jupyter, despliegue manual vía SCP o rsync, sin tracking de experimentos ni versionado de modelos
- Nivel 1 – Automatización básica: scripts de Python en repos de Git, CI/CD básico con GitHub Actions, MLflow para tracking de experimentos, Docker para reproducibilidad de environments
- Nivel 2 – Plataforma naciente: Kubernetes para scheduling de jobs, APIs internas con versiones, model registry compartido, feature store inicial, observabilidad básica con Prometheus
- Nivel 3 – Plataforma gobernada: IDP completo con self-service, multi-tenancy, SLOs contractuales, chargeback automatizado, equipo dedicado con roadmap público y feedback loop activo
- Señales de regresión: crecimiento en el número de repos privados con herramientas de infraestructura duplicadas, aumento en el tiempo medio de despliegue, o incremento en incidentes causados por diferencias de configuración entre equipos

## Buena práctica

La evolución de la plataforma debe ser incremental y guiada por el dolor real de los equipos, no por un roadmap aspiracional: el mejor indicador de que es momento de invertir en el siguiente nivel es que el costo de no hacerlo supera el costo de construirlo.
