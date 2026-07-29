# Módulo 8 – Capítulo 09 – Sección 06

# Cierre: los modelos son artefactos de software y requieren el mismo gobierno

Los modelos de lenguaje son artefactos de ingeniería con ciclo de vida, dependencias, vulnerabilidades y requisitos de governance análogos a los del software de producción, y los equipos que los tratan como cajas negras inmutables sin procesos de versionado, validación, despliegue controlado y auditoría experimentan los mismos tipos de incidentes que el software sin prácticas de ingeniería: regresiones no detectadas, rollbacks costosos, pérdida de trazabilidad y violaciones de compliance. La madurez del ecosistema de herramientas (Hugging Face Hub para registry, MLflow para tracking, vLLM para serving, Argo Rollouts para despliegue progresivo) permite aplicar las mejores prácticas de DevOps a los modelos con relativamente poco esfuerzo adicional, adaptando conceptos de CI/CD como golden test suites, canary deployments y runbooks de rollback al contexto específico de los LLMs. El gobierno de modelos también incluye la dimensión de compliance: documentar las fuentes de datos de entrenamiento, los criterios de exclusión de datos, las métricas de sesgo evaluadas y las restricciones de uso es un requisito que la regulación emergente (AI Act en la UE, Executive Order de IA en EEUU) está convirtiendo en obligatorio para modelos de alto riesgo. El AI Engineer que implementa estos procesos de governance no solo reduce el riesgo operativo sino que habilita la confianza institucional necesaria para que los productos de IA escalen dentro de las organizaciones sin fricciones de compliance o gobernanza.

## Idea central

La diferencia entre un proyecto de ML experimental y un sistema de ML en producción es precisamente el governance: versionado, validación, despliegue controlado y auditoría no son burocracia sino la ingeniería que permite operar modelos con confianza a escala.

---

*"Software engineering is what happens to programming when you add time and other programmers."* — Russ Cox, ingeniero en Google y contribuidor principal a Go, recordando que la gestión del ciclo de vida de modelos ML requiere exactamente las mismas disciplinas de ingeniería de software que cualquier otro sistema de producción que evoluciona en el tiempo.
