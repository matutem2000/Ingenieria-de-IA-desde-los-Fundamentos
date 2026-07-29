# Módulo 8 – Capítulo 09 – Sección 06

## Cierre: los modelos son artefactos de software y requieren el mismo gobierno

La analogía más útil para comunicar el gobierno de modelos a una organización que viene del mundo del software es directa: los modelos de lenguaje son artefactos de ingeniería con ciclo de vida, dependencias, vulnerabilidades y requisitos de governance análogos a los del software de producción. Un modelo sin versionado es como código sin git: funciona hasta que necesitas entender qué cambió entre dos versiones y no tienes forma de saberlo. Un modelo sin validación pre-despliegue es como código sin tests: funciona hasta que no funciona, y entonces no sabes por qué. Un modelo sin proceso de rollback es como código sin capacidad de revertir commits: cada despliegue es un punto de no retorno.

La madurez del ecosistema de herramientas de gobierno de modelos ha reducido el costo de implementar estas prácticas a un nivel accesible para cualquier equipo. Hugging Face Hub o MLflow para el registry de modelos, un golden dataset mantenido en el repositorio Git del proyecto, GitHub Actions o Jenkins para ejecutar la validación automatizada, Argo Rollouts para el despliegue progresivo canary, y `kubectl rollout undo` para el rollback: estas son herramientas ampliamente disponibles y bien documentadas que, combinadas con los procesos presentados en este capítulo, constituyen el mínimo viable de gobierno de modelos para un sistema de producción.

El gobierno de modelos también tiene dimensiones de compliance que están siendo codificadas en regulación: el EU AI Act para sistemas de alto riesgo requiere documentación del proceso de entrenamiento, de las métricas de evaluación de sesgos y de las restricciones de uso; el Executive Order de IA de EEUU establece requisitos de transparencia para modelos de gran capacidad. Los equipos que implementan el governance desde el principio —model cards documentados, linaje de datos trazable, evaluaciones de sesgo en el golden dataset, restricciones de uso documentadas— estarán mejor posicionados cuando estos requisitos regulatorios se apliquen a sus sistemas. Los que los implementen como afterthought tendrán que documentar retroactivamente sistemas opcos que han operado durante meses sin trazabilidad.

El CI/CD para modelos —automatizar el pipeline desde el commit del código de entrenamiento hasta el despliegue en producción pasando por todos los gates de validación— es el estado del arte del MLOps que los equipos más maduros están implementando en 2025. Un pipeline típico integra: validación del dataset al hacer PR del script de preparación de datos, entrenamiento automático con Axolotl en una instancia cloud Spot al fusionar al main branch del adaptador, evaluación con lm-evaluation-harness en el golden set como CI step, push al Hugging Face Hub solo si se superan los umbrales de calidad, y trigger automático del canary deployment en Kubernetes al publicar una nueva versión en el registry. Este pipeline convierte el fine-tuning de una operación manual en un proceso de ingeniería reproducible y auditable.

## Idea central

La diferencia entre un proyecto de ML experimental y un sistema de ML en producción es precisamente el governance: versionado, validación, despliegue controlado y auditoría no son burocracia sino la ingeniería que permite operar modelos con confianza a escala.

---

*"Software engineering is what happens to programming when you add time and other programmers."* — Russ Cox, ingeniero en Google y contribuidor principal a Go, recordando que la gestión del ciclo de vida de modelos ML requiere exactamente las mismas disciplinas de ingeniería de software que cualquier otro sistema de producción que evoluciona en el tiempo.
