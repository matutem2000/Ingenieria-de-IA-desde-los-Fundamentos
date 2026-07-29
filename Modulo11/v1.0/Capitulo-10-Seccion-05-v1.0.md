# Módulo 11 – Capítulo 10 – Sección 05

## Checklist de madurez técnica antes de escalar: los 6 dominios de preparación para producción enterprise

Escalar un sistema de IA que no está listo para producción enterprise es uno de los errores más costosos que puede cometer un equipo de AI Engineering: los problemas que existen a baja escala se amplifican de manera no lineal a alta escala, y resolverlos con el sistema en producción activa con tráfico real es significativamente más difícil, más riesgoso, y más costoso que resolverlos antes de escalar. El checklist de madurez técnica es la herramienta que previene este error: una verificación sistemática de los 6 dominios de preparación para producción enterprise que debe completarse antes de aumentar el tráfico, antes de incorporar nuevos equipos consumidores a la plataforma, y antes de integrar el sistema con sistemas core del negocio.

Los 6 dominios del checklist no son independientes — tienen dependencias explícitas que determinan la secuencia de verificación. El dominio de **infraestructura y despliegue** es la base: sin un pipeline de CI/CD funcional, sin entornos separados, y sin capacidad de rollback automatizado, ningún otro dominio puede verificarse de manera confiable porque cualquier problema detectado en los otros dominios no puede resolverse de manera segura. El dominio de **evaluación y calidad** es el segundo: sin evaluación formal, el sistema puede escalar pero el equipo no tendrá visibilidad sobre si la calidad se degrada bajo carga. El dominio de **seguridad y cumplimiento** es crítico para entornos regulados: escalar un sistema que procesa datos regulados sin haber completado las verificaciones de cumplimiento puede producir obligaciones legales que requieren descomisionar el sistema o aplicar cambios urgentes bajo presión.

El primer dominio — **infraestructura y despliegue** — verifica que el sistema puede desplegarse de manera reproducible y revertirse de manera segura. Los criterios concretos son: pipeline de CI/CD con ejecución automática de tests antes de cada despliegue a producción; entorno de staging que recibe el 100% de los cambios antes de producción con datos que representan la distribución de producción; Dockerfile o definición de IaC que hace el entorno completamente reproducible; proceso de rollback que puede completarse en menos de 15 minutos sin intervención manual en el código; y proceso de canary deployment que permite dirigir el 5-10% del tráfico al nuevo deployment antes de la promoción completa.

El segundo dominio — **evaluación y calidad** — verifica que el equipo puede detectar degradaciones de calidad de manera automática. Los criterios son: golden dataset con al menos 100 casos curados que representa la distribución de inputs de producción; evaluación automática ejecutándose como gate en el CI/CD con threshold de calidad explícito; evaluación continua sobre el tráfico de producción (al menos el 5% del tráfico evaluado con LLM-as-a-judge); alertas automáticas cuando el quality score cae más del 5% respecto a la media histórica; y runbook documentado para el proceso de diagnóstico y resolución de una degradación de calidad detectada.

El tercer dominio — **seguridad y cumplimiento** — verifica que el sistema cumple los requisitos de seguridad y regulatorios del entorno enterprise. Los criterios son: revisión de seguridad aprobada por el equipo de seguridad de la organización; clasificación de los datos que el sistema procesa (si incluye datos PII o datos regulados, los controles correspondientes están implementados y documentados); logs de auditoría para todas las peticiones con retención definida por el marco regulatorio aplicable; controles de acceso (RBAC o ABAC) que garantizan que solo los usuarios autorizados pueden acceder al sistema; y proceso documentado para gestionar una solicitud de datos de un regulador o de un usuario (derecho de acceso, derecho de eliminación).

El cuarto dominio — **observabilidad** — verifica que el equipo puede detectar, diagnosticar, y resolver incidentes en producción de manera eficiente. Los criterios son: logging de trazas completas (input, output, latencia, costo de tokens) para todas las peticiones de producción con retención de al menos 30 días; dashboards con las métricas clave (latencia p50/p95/p99, error rate, quality score, costo diario) visibles en tiempo real; alertas configuradas con thresholds basados en los SLOs definidos para el sistema; runbooks actualizados para los tipos de incidentes más frecuentes; y proceso de on-call definido con responsables y escalation path para incidentes de producción fuera del horario laboral.

El quinto dominio — **gestión de costos** — verifica que el equipo tiene visibilidad y control sobre el costo del sistema antes de escalar el tráfico. Los criterios son: presupuesto mensual definido con alertas automáticas al 70% y al 90% del presupuesto; costo por tipo de petición desagregado (tokens de entrada, tokens de salida, embeddings, almacenamiento vectorial); proyección de costo bajo el volumen de tráfico post-escalado con escenario optimista, base, y pesimista; estrategias de optimización de costo implementadas en orden de impacto (prompt caching, semantic caching, model routing según el Capítulo 07); y proceso de aprobación para cambios que incrementan el costo mensual más del 20%.

El sexto dominio — **operaciones** — verifica que el sistema puede operar en producción sin dependencia constante de los ingenieros que lo construyeron. Los criterios son: documentación de operaciones que permite a alguien sin conocimiento previo del sistema diagnosticar los problemas más frecuentes; proceso de actualización del golden dataset y de los prompts que puede completarse por el equipo de operaciones sin modificar el código; plan de contingencia para fallo del proveedor de LLM (modelo alternativo o proceso manual de fallback); proceso de comunicación de incidentes a los stakeholders y usuarios afectados; y revisión trimestral del sistema que incluye análisis de los incidentes del período y actualización del roadmap de mejoras.

## Checklist consolidado de los 6 dominios

**Infraestructura y Despliegue**
- [ ] Pipeline de CI/CD con tests automáticos antes de cada despliegue a producción
- [ ] Entorno de staging separado de producción con datos representativos
- [ ] Proceso de rollback completable en < 15 minutos sin modificación de código
- [ ] Definición de IaC o Dockerfile que garantiza reproducibilidad del entorno
- [ ] Proceso de canary deployment para validar cambios con tráfico real parcial

**Evaluación y Calidad**
- [ ] Golden dataset con >= 100 casos curados con criterios de calidad acordados con el negocio
- [ ] Evaluación automática como gate en CI/CD con threshold explícito (ej. quality score >= 0.85)
- [ ] Evaluación continua sobre >= 5% del tráfico de producción con LLM-as-a-judge
- [ ] Alertas automáticas ante degradación de calidad (quality score cae > 5% vs. media histórica)
- [ ] Runbook para diagnóstico y resolución de una degradación de calidad detectada

**Seguridad y Cumplimiento**
- [ ] Revisión de seguridad aprobada por el equipo de seguridad de la organización
- [ ] Clasificación de datos procesados por el sistema con controles correspondientes implementados
- [ ] Logs de auditoría para todas las peticiones con retención definida por el marco regulatorio
- [ ] RBAC o ABAC implementado con principio de mínimo privilegio para acceso al sistema
- [ ] Proceso documentado para gestionar solicitudes de datos (acceso, eliminación) de usuarios o reguladores

**Observabilidad**
- [ ] Logging de trazas completas (input, output, latencia, costo) con retención >= 30 días
- [ ] Dashboards en tiempo real con métricas clave (latencia p50/p95/p99, error rate, quality score, costo)
- [ ] Alertas basadas en SLOs definidos para el sistema (latencia, error rate, quality score)
- [ ] Runbooks actualizados para los tipos de incidentes más frecuentes del sistema
- [ ] Proceso de on-call definido con responsables y escalation path para incidentes fuera de horario

**Gestión de Costos**
- [ ] Presupuesto mensual definido con alertas automáticas al 70% y 90% del presupuesto
- [ ] Costo por tipo de petición desagregado y visible en el dashboard de costos
- [ ] Proyección de costo bajo el volumen post-escalado (optimista/base/pesimista)
- [ ] Estrategias de optimización implementadas en orden de impacto (prompt caching primero)
- [ ] Proceso de aprobación para cambios que incrementan el costo mensual > 20%

**Operaciones**
- [ ] Documentación de operaciones para diagnóstico de problemas sin conocimiento previo del sistema
- [ ] Proceso de actualización de golden dataset y prompts sin modificación de código
- [ ] Plan de contingencia para fallo del proveedor de LLM (modelo alternativo o fallback manual)
- [ ] Proceso de comunicación de incidentes a stakeholders y usuarios afectados documentado
- [ ] Revisión trimestral planificada con análisis de incidentes y actualización del roadmap

---

**Nota del Arquitecto:** Este checklist no es una lista de requisitos perfectos sino una herramienta de diagnóstico de brechas. Un sistema puede tener un 70% de los ítems completados y estar en condiciones de escalar si las brechas restantes corresponden a los dominios de menor riesgo para el caso de uso específico. La decisión de escalar con brechas existentes debe tomarse de manera explícita y documentada — con el riesgo de cada brecha identificado, la mitigación en lugar de la solución formal aceptada, y la fecha comprometida para la resolución. Lo que nunca es aceptable es escalar sin conocer las brechas.

La sección de cierre del módulo articula la perspectiva que unifica todos los principios cubiertos: la gestión de la complejidad como el trabajo central del AI Engineer enterprise, y cómo la descomposición sistemática de esa complejidad en partes comprensibles es la competencia que distingue los sistemas que escalan de los que colapsan.
