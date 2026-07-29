# Módulo 11 – Capítulo 01 – Sección 04

## Madurez de IA empresarial: modelo de madurez en 5 niveles para evaluar el estado actual

Toda organización enterprise que adopta IA opera en algún punto de un espectro que va desde los primeros experimentos no coordinados hasta la industrialización completa con mejora continua autónoma. El problema es que sin un marco de referencia explícito, las organizaciones no saben dónde están en ese espectro, y sin saber dónde están no pueden planificar de manera coherente dónde quieren llegar. Invierten en capacidades avanzadas — fine-tuning automatizado, model routing dinámico — sin haber consolidado las fundacionales, y producen deuda técnica que bloquea el progreso en lugar de acelerarlo.

Un modelo de madurez de IA empresarial resuelve este problema proporcionando un marco de diagnóstico objetivo. Inspirado en el CMMI y adaptado a las particularidades de los sistemas de IA, distingue cinco niveles que tienen prerequisitos técnicos específicos y verificables. El énfasis en verificabilidad es central: la evaluación de madurez debe realizarse como una auditoría técnica con checklist concreto — qué artefactos existen, qué pipelines se ejecutan en producción, qué métricas son visibles en dashboards reales — no como una encuesta de percepción donde cada equipo declara el nivel que aspira a tener.

Las dimensiones de evaluación del modelo son cinco: la automatización de pipelines (¿los datos fluyen automáticamente desde las fuentes hasta el modelo, o hay pasos manuales?), la cobertura de observabilidad (¿el equipo puede ver en tiempo real qué está haciendo el sistema en producción?), la existencia y ejecución de evaluaciones (¿hay un golden set y se ejecuta en CI/CD?), el nivel de self-service para equipos de producto (¿los equipos pueden desplegar nuevos casos de uso sin asistencia del equipo de plataforma?), y el tiempo medio de despliegue de un nuevo caso de uso (¿semanas o días?).

El uso práctico del modelo es el diagnóstico de brechas: una organización puede estar en el Nivel 3 en términos de versionado y CI/CD, pero en el Nivel 1 en evaluación porque nunca construyó el golden set. Ese diagnóstico de brecha identifica exactamente dónde está la inversión más urgente. El Capítulo 09 de este módulo retoma este marco y lo operacionaliza con criterios de evidencia verificable por dimensión: qué artefacto concreto prueba que el equipo está en el Nivel 2 versus el Nivel 3 en cada dimensión.

> **Nota del Arquitecto:** En mi experiencia, la brecha más frecuente y más costosa es la de evaluación. Los equipos suelen construir el CI/CD (Nivel 2) y el prompt registry (Nivel 3) antes de construir el golden set, porque el golden set requiere tiempo de los stakeholders de negocio para curar los casos de referencia. El resultado es que tienen la infraestructura de despliegue controlado sin la capacidad de medir si lo que despliegan es mejor o peor que lo anterior. El golden set debe construirse en paralelo al primer caso de uso, no después.

## Los 5 niveles de madurez técnica

- **Nivel 1 — Ad hoc:** experimentos en notebooks sin versionado, datos sin gobernanza, despliegues manuales, sin métricas de calidad, dependencia de individuos específicos que concentran el conocimiento del sistema.
- **Nivel 2 — Reproducible:** pipelines de datos automatizados con Airflow/Prefect, modelos en MLflow con versionado, CI/CD básico, entornos de staging separados de producción con datos de prueba representativos.
- **Nivel 3 — Definido:** plataforma compartida de ML/LLM, evaluaciones automatizadas con golden sets ejecutados en CI/CD como gate de despliegue, observabilidad con OpenTelemetry, gestión de prompts versionada en un prompt registry, SLOs definidos y documentados.
- **Nivel 4 — Gestionado:** A/B testing de modelos en producción con asignación estadísticamente válida, feature store compartido entre equipos, cost allocation por equipo y caso de uso con dashboards de FinOps, auto-scaling reactivo con KEDA, detección automática de drift con alertas.
- **Nivel 5 — Optimizado:** experimentación continua con bandit algorithms, optimización automática de costos mediante model routing dinámico, retroalimentación de negocio integrada automáticamente en el ciclo de mejora, plataforma con SLA de 99.9% y portal de self-service completo para equipos consumidores.

---

**Buena práctica:** Realizar la evaluación de madurez como una auditoría técnica con checklist verificable — no como una encuesta de percepción — es el único modo de obtener un diagnóstico accionable. El Capítulo 09 provee el checklist completo con los criterios de evidencia por nivel y por dimensión de evaluación.

La siguiente sección completa el marco introductorio del módulo describiendo el perfil del AI Engineer que opera en este entorno enterprise: sus responsabilidades técnicas, sus stakeholders, y las capacidades que lo diferencian del Data Scientist o del ML Engineer convencional.
