# Módulo 11 – Capítulo 09 – Sección 02

# Métricas de productividad del equipo: time-to-deploy, cycle time y defect rate en proyectos de IA

La productividad de los equipos de AI Engineering enterprise se mide con métricas adaptadas de las DORA (DevOps Research and Assessment) metrics — deployment frequency, lead time for changes, change failure rate, y time to restore service — a las particularidades de los proyectos de IA, donde el ciclo de entrega incluye no solo el desarrollo del código sino también la evaluación del modelo, la construcción del dataset de evaluación, y el proceso de validación de calidad. El time-to-deploy de nuevos casos de uso es la métrica más reveladora de la madurez de la plataforma: en organizaciones en el Nivel 1-2 de madurez, implementar un nuevo caso de uso de IA tarda típicamente 6-12 semanas (configurar la infraestructura, integrar con las fuentes de datos, construir el pipeline de evaluación desde cero); en organizaciones en el Nivel 4-5, el mismo nuevo caso de uso tarda 1-2 semanas gracias a los templates de la plataforma, el feature store compartido, y el pipeline de evaluación reutilizable. El cycle time — el tiempo desde que un cambio (nuevo prompt, nuevo modelo, nueva fuente de datos para RAG) entra al backlog hasta que está en producción — es la métrica de eficiencia del proceso de desarrollo: en sistemas de IA bien instrumentados con CI/CD y evaluación automatizada, los ciclos de mejora de prompts pueden ejecutarse en horas en lugar de días. El defect rate en proyectos de IA debe separarse entre defectos de software (bugs en el código de infraestructura) y defectos de comportamiento del modelo (respuestas incorrectas, alucinaciones, violaciones de las restricciones configuradas), porque tienen causas raíz distintas y procesos de remediación diferentes.

## Métricas de productividad específicas para equipos de AI Engineering

- Deployment frequency: número de deploys exitosos por semana a producción (incluyendo cambios de prompts, modelos, y configuración de RAG); organizaciones de alta madurez realizan múltiples deploys diarios
- Lead time for LLM changes: tiempo medio desde el commit de un cambio de prompt o modelo hasta que está sirviendo el 100% del tráfico en producción, medido con timestamps de Git y del sistema de despliegue
- Change failure rate para IA: porcentaje de cambios (prompts, modelos, configuración) que requieren rollback dentro de las 24 horas del despliegue, calculado como incidentes de calidad / total de cambios
- Time-to-detect de regresiones: tiempo medio entre el despliegue de un cambio que introduce una regresión de calidad y la detección automática de esa regresión por el sistema de monitoreo, con objetivo de menos de 15 minutos
- Evaluation coverage: porcentaje de los cambios desplegados a producción que fueron evaluados con el golden set antes del despliegue; el objetivo es el 100% de los cambios que tocan el path crítico de inferencia

## Buena práctica

Publicar las métricas de productividad del equipo en un dashboard visible para todos los stakeholders — incluyendo product managers y líderes de negocio — crea alineación sobre el estado real del equipo y facilita la justificación de inversiones en infraestructura de plataforma.
