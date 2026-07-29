# Módulo 11 – Capítulo 09 – Sección 01

## Cómo medir objetivamente el nivel de madurez actual: criterios de evidencia verificable

El Capítulo 01 de este módulo introdujo el modelo de madurez en 5 niveles como marco conceptual para organizar el estado de los sistemas de IA enterprise. Este capítulo retoma ese marco con un propósito distinto: no describir qué caracteriza cada nivel en abstracto, sino definir **qué evidencia técnica concreta** prueba que un equipo está en un nivel específico y no en otro. La diferencia es significativa. Cualquier equipo puede declarar que está en el Nivel 3 basándose en su percepción de sus propias prácticas. Solo un equipo que puede mostrar los artefactos requeridos por el Nivel 3 ha demostrado objetivamente que lo está.

Esta distinción importa porque la evaluación de madurez basada en percepción produce diagnósticos incorrectos que llevan a inversiones incorrectas. Un equipo que se percibe en el Nivel 3 pero no tiene un golden dataset ejecutándose en CI/CD (el artefacto definitorio del Nivel 3) va a invertir en capacidades del Nivel 4 (A/B testing, feature store compartido) sobre una fundación del Nivel 2. Esas inversiones no producen el valor esperado porque la fundación no está consolidada.

### Criterios de evidencia por nivel y por dimensión

Para diagnosticar el nivel de madurez de manera rigurosa, se evalúan cinco dimensiones con criterios de evidencia específicos:

**Dimensión 1 — Automatización del ciclo de vida del sistema:**
- Nivel 2: existe un Dockerfile para el servicio de inferencia; el servicio se puede reproducir en cualquier entorno con `docker build && docker run` sin intervención manual.
- Nivel 3: existe un pipeline de CI/CD en GitHub Actions, GitLab CI, o Jenkins que se ejecuta automáticamente en cada PR; el pipeline incluye tests unitarios y de integración como gate de merge.
- Nivel 4: el pipeline de CI/CD incluye la suite de evaluación de LLM como gate; ningún cambio de prompt o de modelo puede desplegarse sin pasar la evaluación automatizada.

**Dimensión 2 — Evaluación y calidad:**
- Nivel 2: existe un conjunto de casos de prueba manuales (aunque sea un Google Sheet) que el equipo usa antes de desplegar.
- Nivel 3: existe un golden dataset con mínimo 100 casos curados en Git, con un script ejecutable que produce un score de evaluación reproducible. El artefacto definitorio del Nivel 3 es este script siendo ejecutado automáticamente en el CI/CD.
- Nivel 4: la evaluación se ejecuta sobre el tráfico de producción (sampling del 1-5%), con alertas automáticas cuando la calidad degrada más del threshold configurado.

**Dimensión 3 — Observabilidad:**
- Nivel 2: existen logs básicos del servicio de inferencia accesibles en la plataforma de logging (CloudWatch, Datadog, ELK).
- Nivel 3: el servicio está instrumentado con OpenTelemetry y produce trazas de LLM en Langfuse o LangSmith con el par (prompt, completion) trazable por conversation_id; la latencia p50/p95/p99 es visible en un dashboard en tiempo real.
- Nivel 4: existe un dashboard de métricas de calidad de producción (quality score rolling average, drift rate, hallucination rate) actualizado en tiempo real con alertas configuradas.

**Dimensión 4 — Gestión de prompts:**
- Nivel 2: los prompts están en archivos de texto en el repositorio Git (no hardcodeados en el código fuente), con naming convention explícita.
- Nivel 3: existe un prompt registry con versionado semántico, API de consulta, y capacidad de rollback a la versión anterior en menos de 5 minutos sin despliegue de código.
- Nivel 4: el prompt registry soporta canary deployments, A/B testing, y audit trail completo de qué versión de prompt generó cada respuesta en producción.

**Dimensión 5 — Gestión de costos:**
- Nivel 2: existe algún mecanismo para ver el costo total mensual del sistema (la factura del proveedor de LLM).
- Nivel 3: el costo está desagregado por caso de uso y puede calcularse el costo por petición por tipo de operación.
- Nivel 4: existe un sistema de cost allocation por equipo o tenant con dashboard de FinOps de IA y alertas de gasto configuradas.

## Criterios de evidencia por transición de nivel

- **Nivel 1 → Nivel 2:** el sistema puede reproducirse en staging con un solo comando (Docker); existe un repositorio Git con el historial completo del código del sistema; staging está separado de producción con datos de prueba distintos.
- **Nivel 2 → Nivel 3:** el golden dataset existe en Git con mínimo 100 casos curados; el script de evaluación se ejecuta automáticamente en CI/CD como gate; el prompt registry tiene API funcional; OpenTelemetry está instrumentado con trazas visibles en un dashboard.
- **Nivel 3 → Nivel 4:** la evaluación se ejecuta sobre tráfico de producción con alertas automáticas; el A/B testing de prompts o modelos tiene evidencia de haber sido ejecutado al menos una vez con resultados documentados; el cost allocation por equipo tiene dashboard visible para los stakeholders de negocio.
- **Nivel 4 → Nivel 5:** el model routing dinámico está operativo con clasificador de complejidad; el portal de self-service tiene evidencia de haber sido usado por al menos 3 equipos distintos para desplegar sus propios casos de uso sin asistencia del equipo de plataforma.

---

**Para recordar:** La evaluación de madurez debe realizarse con evidencia técnica verificable — artefactos que existen y pueden demostrarse — no con declaraciones del equipo sobre sus prácticas. La diferencia entre "tenemos CI/CD" (declaración) y "aquí está el pipeline que se ejecutó ayer con estos logs" (evidencia) es la diferencia entre una auto-evaluación y una auditoría.

La sección siguiente aplica los criterios de evidencia al seguimiento de la productividad del equipo con métricas específicas adaptadas al contexto de AI Engineering.
