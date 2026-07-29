# Módulo 12 – Capítulo 06 – Sección 06

## Cierre: del sistema funcional al sistema operacional

El Capítulo 6 construyó el puente entre el sistema que funciona en un entorno de desarrollo y el sistema que opera en producción de forma reproducible, segura y con calidad garantizada en cada deploy. Los cinco componentes de este capítulo — containerización, CI/CD con gate de evaluación, infraestructura como código, estrategia canary y gestión de configuraciones — son colectivamente lo que distingue a un AI Engineer de un prototipador de IA. El prototipador puede hacer funcionar el LLM en un notebook; el AI Engineer puede garantizar que ese sistema sigue funcionando con calidad medible seis meses después del primer despliegue, con cada cambio validado automáticamente antes de llegar a los usuarios.

La práctica más transformadora del capítulo para equipos que vienen de proyectos de IA sin MLOps es el gate de evaluación en el CI/CD. La primera semana en la que el gate bloquea un deploy porque faithfulness cayó de 0.87 a 0.77 — causado por un cambio aparentemente inocuo en el system prompt del agente — demuestra de forma concreta que los LLMs tienen comportamientos no lineales frente a cambios pequeños en el contexto, y que la evaluación automática es el único mecanismo confiable para detectar esas regresiones antes de que afecten a los usuarios. Sin el gate, ese cambio habría llegado a producción y la degradación de calidad habría sido detectada días después por quejas de usuarios — o nunca, si los usuarios simplemente dejaron de confiar en el sistema sin reportarlo.

La ingeniería de costos como práctica operativa — el monitoreo continuo del costo por petición, la atribución por equipo y las alertas de presupuesto — cierra el loop entre el constraint de diseño (0.02 USD/petición definido en el Capítulo 1) y la realidad operativa. Sin ese monitoreo, el constraint de costo es una intención documentada en el ADR pero sin verificación en producción. Con el monitoreo activo y las alertas configuradas, el constraint es un SLA operativo que el equipo puede comprometerse a cumplir y que el sistema señala automáticamente cuando se aproxima al límite.

El Capítulo 7 comienza con la evaluación end-to-end del sistema desplegado: el framework de métricas en tres capas (RAG, agéntica y de sistema) que convierte el sistema operacional en un sistema mejorable con evidencia continua.

## Lo que el Capítulo 6 implementó

- **Dockerfile multi-stage**: usuario no-root, hash verification de dependencias, health check integrado, configuración uvicorn de producción — imagen reproducible e inmutable para cada deploy.
- **Pipeline CI/CD**: build (multi-stage + Trivy scan) + test (ruff + mypy + pytest 80% + integration + smoke) + evaluate (RAGAS gate sobre 20 muestras del golden dataset) + deploy (kubectl rollout status) — calidad verificada en cada deploy.
- **Infraestructura Terraform**: S3 backend + DynamoDB locking, módulos networking/compute/services, workspaces por entorno, EKS + RDS Multi-AZ + ElastiCache + Qdrant Cloud.
- **Canary deployment con Argo Rollouts**: steps 5% → 25% → 50% → 100% con AnalysisTemplate en Prometheus (error_rate, p95_latency, faithfulness_ragas); rollback automático sub-2-minutos.
- **Ingeniería de costos**: costo por petición desagregado por componente (embedding + reranking + LLM + infraestructura), atribución por equipo, alertas de "costo_hora > 1.5x promedio" y AWS Budgets.
- **Gestión de configuraciones**: AWS Secrets Manager + External Secrets Operator con rotación automática; ConfigMaps versionados en el repositorio; Pydantic Settings con validación al startup; detect-secrets en pre-commit hook.

> **Nota del Arquitecto**: El conjunto de prácticas de este capítulo tiene un costo de implementación real — estimo entre 3 y 5 días de trabajo de un ingeniero senior para configurar el pipeline CI/CD completo con gate de evaluación, el Terraform de infraestructura y la gestión de secrets con ESO. Ese costo se recupera en el primer incidente que el sistema previene: un deploy que degrada faithfulness de 0.87 a 0.74 y es bloqueado por el gate antes de llegar a los usuarios, o una API key que rota automáticamente sin downtime, o una instancia RDS que falla y el Multi-AZ hace failover en 60 segundos sin que el equipo tenga que intervenir. La pregunta no es "¿vale la pena el costo de implementación?" sino "¿cuántos incidentes de producción necesitamos para amortizarlo?". La respuesta habitual es uno.

El deploy automatizado no es una característica opcional — es la condición necesaria para poder iterar sobre el sistema con confianza, sabiendo que cada cambio pasa por las mismas puertas de calidad y seguridad.

**Para recordar**: El deploy automatizado no es una característica opcional — es la condición necesaria para poder iterar sobre el sistema con confianza, sabiendo que cada cambio pasa por las mismas puertas de calidad y seguridad.

*"Infrastructure as code is the practice of managing and provisioning infrastructure through machine-readable configuration files rather than manual processes." — Kief Morris, Infrastructure as Code*
