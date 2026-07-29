# Módulo 10 – Capítulo 10 – Sección 03

# Deprecación de componentes: ciclo de vida de las APIs y abstracciones de plataforma

La deprecación de componentes en una plataforma de IA sigue el mismo principio que la deprecación de APIs en software: una vez que un componente (API endpoint, SDK version, abstracciones de pipeline, modelo de datos del registry) es expuesto a los consumidores, eliminarlo unilateralmente es equivalente a introducir un breaking change sin previo aviso, con el agravante de que en una plataforma interna los consumidores son colegas que esperan un nivel de soporte que en una API pública no siempre es posible. El proceso de deprecación en una plataforma de IA se estructura en fases: anuncio de deprecación con al menos 90 días de antelación (comunicado en el developer portal, notificación en Slack, y warning en los headers HTTP de las respuestas del componente deprecado `Deprecation: true`, `Sunset: 2025-03-01`), período de migración asistida donde el equipo de plataforma ofrece soporte activo para que los consumidores migren, período de read-only (el componente aún funciona pero no acepta nuevas registraciones), y finalmente eliminación con periodo de cortesía de 30 días donde las llamadas retornan un error con mensaje de migración. La documentación del ciclo de vida de los componentes en el developer portal (Backstage) incluye el estado actual de cada componente (Active, Deprecated, Sunset) con las fechas de cada transición, reduciendo la incertidumbre de los consumidores sobre cuándo deben actuar.

## Fases del proceso de deprecación de componentes

- Anuncio formal: notificación con mínimo 90 días de antelación vía developer portal, email a propietarios técnicos de equipos consumidores, y deprecation warning en los responses del componente vía headers HTTP estándar
- Migración asistida: el equipo de plataforma ofrece pairing sessions, guías de migración detalladas con ejemplos de código, y un canal de Slack dedicado para soporte durante el período de transición
- Read-only phase: el componente deprecado funciona para operaciones de lectura pero rechaza nuevas escrituras o registraciones; permite a los equipos completar la migración de sus datos históricos sin urgencia
- Sunset enforcement: después de la fecha de sunset, el endpoint retorna HTTP 410 Gone con un body JSON que incluye la URL del componente de reemplazo y la guía de migración; nunca eliminar silenciosamente (HTTP 404)
- Post-mortem de adopción: análisis de cuántos equipos migraron antes de la fecha de deprecación, cuántos requirieron extensión, y qué barreras de migración se encontraron; retroalimenta el diseño de la siguiente versión para minimizar la necesidad de deprecaciones

## Para recordar

Una deprecación bien gestionada fortalece la confianza de los equipos en la plataforma; una deprecación abrupta o mal comunicada puede generar desconfianza permanente y llevar a que los equipos eviten adoptar nuevas abstracciones por miedo a quedar bloqueados en el futuro.
