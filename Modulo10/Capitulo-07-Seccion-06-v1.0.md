# Módulo 10 – Capítulo 07 – Sección 06

# Cierre: el LLM Gateway es el punto de control central de la plataforma de IA

El LLM Gateway cumple en una plataforma de IA el mismo rol que un API Gateway en una arquitectura de microservicios: es el punto donde la política se aplica, el tráfico se observa, y la experiencia del desarrollador se estandariza. Sin él, cada equipo gestiona individualmente sus API keys de OpenAI, implementa su propia lógica de retry y fallback, decide unilateralmente qué modelo usar y con qué parámetros, y genera costos que nadie puede atribuir con precisión; con él, toda esa complejidad se resuelve una vez a nivel de plataforma y los equipos consumen un endpoint interno estable que se comporta de forma consistente independientemente de qué proveedor está sirviendo la petición en ese momento. La adopción de un LLM Gateway requiere un cambio cultural en los equipos de desarrollo: en lugar de llamar directamente a `https://api.openai.com/v1/chat/completions`, se llama a `https://llm-gateway.internal/v1/chat/completions` con credenciales internas; el beneficio concreto para el equipo es que si OpenAI tiene una outage, el gateway los cambia automáticamente a Anthropic o Azure OpenAI sin que el equipo tenga que cambiar nada. La inversión en construir y operar un LLM Gateway se amortiza rápidamente a escala: en organizaciones con más de 20 equipos usando LLMs, la reducción de costos por caching semántico y routing optimizado, combinada con la visibilidad de costos para FinOps, justifica ampliamente el esfuerzo de construcción.

## Principio rector

El LLM Gateway convierte el caos de múltiples equipos llamando directamente a múltiples APIs de modelos en un sistema gobernado: un punto de entrada, múltiples salidas, y visibilidad completa sobre quién gasta qué en qué modelo.

---

*"Simplicity is prerequisite for reliability."*
— Edsger W. Dijkstra, pionero de la ciencia de la computación, cuya máxima sobre la relación entre simplicidad y confiabilidad aplica directamente al diseño de capas de abstracción como el LLM Gateway.
