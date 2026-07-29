# Módulo 11 – Capítulo 01 – Sección 02

## De proyectos piloto a producción: las brechas que impiden la escala

El 85% de los proyectos de IA no llegan a producción, según reportes de Gartner y McKinsey. La causa rara vez es la calidad del modelo: la mayoría de los pilotos funcionan razonablemente bien en las condiciones controladas en que fueron construidos. El problema es la infraestructura de soporte que necesitan para sobrevivir al contacto con la realidad operacional de un enterprise: usuarios reales con comportamientos imprevistos, datos de producción con inconsistencias que los datos de prueba no tenían, y equipos de operaciones que no participaron en el desarrollo y que reciben el sistema sin runbooks ni SLOs definidos.

Un piloto exitoso en un Jupyter Notebook con datos de muestra enfrenta en el camino a producción una brecha técnica compuesta por cinco dimensiones acumulativas. La primera es la reproducibilidad: cuando el entorno de desarrollo no está encapsulado de forma explícita — sin gestión de dependencias con Poetry o Conda lockfiles, sin Dockerfiles versionados, sin IaC para la infraestructura de staging — la transferencia del sistema a otro equipo o a otro entorno produce el clásico "funciona en mi máquina". La segunda es la observabilidad: sin trazas distribuidas (OpenTelemetry), sin métricas de latencia por percentil (p50, p95, p99), y sin logs estructurados con correlation IDs, el equipo de operaciones no puede diagnosticar un incidente de producción en un tiempo razonable.

La tercera brecha es la de datos. Los pipelines de preparación de datos en pilotos suelen ser scripts ejecutados manualmente que el Data Scientist corre localmente antes de cada experimento. En producción, esos datos necesitan actualizarse automáticamente, con validaciones de calidad que detecten degradaciones antes de que los datos corruptos contaminen el índice vectorial o los features del modelo. Herramientas como Apache Airflow, Prefect, o dbt con sus suites de testing integradas (not_null, unique, accepted_values) son el paso obligatorio de esta transición.

La cuarta brecha es la evaluación. Un piloto que se evalúa manualmente — el equipo mira los outputs y decide si "se ven bien" — no puede escalar a producción. Un sistema enterprise necesita un golden set de 100 a 500 pares input/output curados, evaluadores automáticos que se ejecuten en el pipeline de CI/CD, y thresholds de calidad que bloqueen el despliegue cuando la calidad cae por debajo del nivel aceptable. Sin esto, cada cambio de prompt o de modelo es un riesgo no cuantificado.

La quinta brecha — y la más costosa en tiempo — es la de seguridad y acceso. La ausencia de gestión de secretos con HashiCorp Vault o AWS Secrets Manager, y de políticas IAM que restrinjan el acceso al modelo en producción, no es solo un problema de cumplimiento: es el bloqueo más frecuente en la aprobación de despliegues por parte del equipo de seguridad corporativo, que puede detener un proyecto por semanas en espera de remediaciones que deberían haberse implementado desde el inicio.

> **Nota del Arquitecto:** La brecha de confianza operacional es la menos documentada pero la más real. Los equipos de infraestructura que van a operar el sistema en producción necesitan runbooks claros, alertas calibradas con thresholds verificados en staging, y SLOs definidos y acordados antes de aceptar la transferencia. Sin ese material, el equipo de IA retiene la operación del sistema indefinidamente, lo que no escala.

## Brechas técnicas que bloquean la escala

- **Brecha de reproducibilidad:** entornos de desarrollo sin gestión de dependencias explícitas (Poetry, Conda lockfiles) producen fallos en la transición a staging que son costosos de diagnosticar porque el sistema "funcionaba" en desarrollo.
- **Brecha de observabilidad:** ausencia de trazas distribuidas (OpenTelemetry), métricas de latencia de inferencia por percentil (p50, p95, p99), y logs estructurados con correlation IDs que permitan correlacionar una queja de usuario con la inferencia específica que la produjo.
- **Brecha de datos:** pipelines manuales de preparación de datos que no están automatizados ni validados, haciendo imposible el reentrenamiento o la actualización continua sin intervención humana en cada ciclo.
- **Brecha de evaluación:** falta de un test suite de evaluación automática con datasets dorados que validen la calidad del modelo antes de cada despliegue; sin él, la detección de regresiones depende de que un usuario reporte el problema.
- **Brecha de seguridad y acceso:** ausencia de gestión de secretos con Vault o AWS Secrets Manager, y de políticas IAM que restrinjan el acceso al modelo en producción con principio de mínimo privilegio.

---

**Para recordar:** La transición de piloto a producción no es un problema de ajuste fino del modelo, sino de construcción de la infraestructura de soporte que lo rodea. Invertir tiempo en identificar y cerrar cada brecha antes del despliegue es siempre más barato que remediarlas bajo presión de un incidente de producción.

La sección siguiente describe la arquitectura que sirve como solución estructural a estas brechas: el stack en cuatro capas que organiza los componentes del sistema enterprise de IA de manera que cada dimensión pueda evolucionar de forma independiente.
