# Módulo 10 – Capítulo 10 – Sección 04

# Feedback loop con los equipos: cómo incorporar las necesidades de los usuarios de la plataforma

El feedback loop entre el equipo de plataforma y los equipos consumidores es el mecanismo que garantiza que la plataforma evoluciona en la dirección correcta: sin feedback sistemático, el equipo de plataforma puede pasar meses construyendo capacidades que nadie necesita mientras los problemas más dolorosos de los usuarios quedan sin resolver. Los canales de feedback se implementan en múltiples frecuencias y formatos: feedback de alta frecuencia y bajo esfuerzo (canal de Slack `#platform-feedback` donde cualquier ingeniero puede reportar un pain point en cualquier momento, con respuesta de reconocimiento garantizada en menos de 24 horas), feedback de mediana frecuencia y estructura media (encuesta trimestral de DevEx con 5-10 preguntas sobre satisfacción con cada componente de la plataforma, NPS de la plataforma, y preguntas abiertas sobre los pain points más importantes), y feedback de baja frecuencia y alta profundidad (user research sessions trimestrales con 2-3 equipos consumidores que incluyen observación directa de cómo usan la plataforma, identificando friction points que los usuarios no articulan en la encuesta porque asumen que son parte normal del trabajo). El cierre del loop es tan importante como la recolección: cada pain point reportado debe recibir una respuesta visible (ej. "lo incluimos en el backlog del Q3", "ya lo arreglamos en v2.3", "es un diseño intencional porque X"), y las encuestas de DevEx deben ir seguidas de un summary publicado con los resultados y el plan de respuesta.

## Mecanismos de feedback loop para plataformas de IA

- Canal de Slack dedicado: `#platform-feedback` o `#ai-platform` con acuerdo de SLA de respuesta del equipo de plataforma (ej. acknowledgment en <24h, respuesta en <72h para issues que no son bugs)
- Encuesta trimestral de DevEx: 5-10 preguntas con escala Likert sobre satisfacción con componentes individuales (training cluster, model registry, serving, LLM gateway) y NPS global de la plataforma; resultados publicados en el developer portal
- Office hours semanales: sesión de 30-60 minutos donde cualquier equipo puede llevar preguntas, demos de problemas, o solicitudes de features al equipo de plataforma; mejora la calidad del feedback y la relación entre equipos
- GitHub/GitLab issues públicos: el repositorio de la plataforma acepta issues de feature requests y bug reports de todos los equipos consumidores, con proceso visible de triage y priorización en el backlog
- Adoption analytics: instrumentación que mide qué comandos del CLI se usan más, qué APIs se llaman con mayor frecuencia, y qué flujos generan más errores de usuario (ej. mensajes de "invalid parameter" frecuentes); feedback sin fricción basado en el uso real

## Para recordar

El feedback loop no es un proceso de "escuchar y no actuar": debe resultar en cambios visibles en el producto que los equipos consumidores puedan atribuir directamente a su input, creando un ciclo de confianza que aumenta la calidad del feedback futuro.
