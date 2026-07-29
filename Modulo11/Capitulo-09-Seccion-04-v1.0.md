# Módulo 11 – Capítulo 09 – Sección 04

# Métricas de plataforma: adopción interna, self-service rate y incident rate

Las métricas de plataforma de IA enterprise miden la salud de la infraestructura compartida desde la perspectiva de los equipos que la consumen: no solo si la plataforma funciona técnicamente, sino si los equipos la usan voluntariamente (adopción), si pueden implementar sus casos de uso sin necesitar asistencia del equipo de plataforma (self-service rate), y con qué frecuencia la plataforma interrumpe el negocio de sus usuarios (incident rate). La adopción interna es la métrica que valida el éxito de la plataforma como producto interno: una plataforma de IA enterprise con capacidades avanzadas pero adoptada solo por el equipo que la construyó no ha generado valor organizacional. La adopción se mide como el número de equipos activos que han desplegado al menos un caso de uso en producción en los últimos 30 días, el número de casos de uso nuevos por mes, y la retención (equipos que usaron la plataforma el mes pasado y siguen usándola este mes). El self-service rate indica qué porcentaje de las tareas que los equipos consumidores necesitan realizar pueden completarse sin abrir un ticket al equipo de plataforma: en una plataforma madura, el 80% o más de las tareas (provisionar un nuevo índice RAG, actualizar un prompt, crear un nuevo endpoint de inferencia, ver los costos de su caso de uso) deben ser self-service mediante el portal de desarrolladores o las APIs de la plataforma. El incident rate de la plataforma (número de incidentes de severidad alta o crítica por mes que afectan a múltiples equipos consumidores) es la métrica de confiabilidad: un incident rate alto genera desconfianza en la plataforma y empuja a los equipos a construir sus propias soluciones ad-hoc, fragmentando la gobernanza.

## Métricas de plataforma en contexto enterprise

- Adopción activa: número de equipos con al menos 1 caso de uso en producción en los últimos 30 días, tiempo medio desde que un equipo empieza a explorar la plataforma hasta su primer despliegue en producción (time-to-first-deploy)
- Self-service rate: porcentaje de operaciones completadas por equipos consumidores sin ticket al equipo de plataforma, medido como (operaciones_total - tickets_recibidos) / operaciones_total por mes
- API uptime y latencia de plataforma: SLA de disponibilidad de 99.9% para las APIs core de la plataforma (embedding, inferencia, retrieval vectorial), con latencia p95 < 500ms para el endpoint de inferencia y < 100ms para el endpoint de embedding
- Incident rate y MTTR de plataforma: número de incidentes que afectan a más de 1 equipo consumidor por mes (objetivo: < 2 incidentes de severidad alta), MTTR (objetivo: < 2 horas para severidad alta, < 30 minutos para severidad crítica)
- Developer Experience (DX) score: encuesta trimestral a los equipos consumidores sobre la facilidad de uso de la plataforma, la calidad de la documentación, y la respuesta del equipo de soporte, con NPS específico de plataforma

## Buena práctica

Publicar un status page de la plataforma (similar a status.anthropic.com o status.openai.com) accesible para todos los equipos internos, con el historial de incidentes y los SLOs actuales — la transparencia sobre el estado de la plataforma construye confianza más que la promesa de alta disponibilidad sin evidencia.
