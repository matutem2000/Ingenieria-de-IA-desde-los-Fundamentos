# Módulo 10 – Capítulo 07 – Sección 05

# Auditoría centralizada: logging de todas las llamadas a modelos con metadatos de negocio

La auditoría centralizada en un LLM Gateway significa que cada request a un modelo de lenguaje es registrado con suficiente contexto para responder tres preguntas críticas en cualquier momento posterior: ¿qué se envió al modelo? (prompt, sistema, parámetros), ¿quién lo envió? (equipo, proyecto, usuario de la aplicación si está disponible), y ¿qué respondió el modelo? (respuesta completa, tokens usados, latencia, costo, proveedor usado). Este registro es imprescindible para múltiples propósitos: debugging de comportamientos incorrectos (reproducir exactamente qué prompt produjo una respuesta problemática), atribución de costos (asignar el costo exacto de inferencia al equipo y proyecto que lo generó), compliance y auditoría (demostrar a auditores qué datos fueron procesados por qué modelo y cuándo), y análisis de uso para identificar patrones y optimizaciones. La implementación del audit log debe considerar la privacidad de datos: en muchos casos los prompts contienen PII o información confidencial, por lo que el log puede almacenar el hash del prompt (para deduplicación y búsqueda exacta) en lugar del prompt completo, o almacenarlo encriptado con una clave que requiere autorización especial para descifrar. La retención del log debe definirse por política: logs de metadatos (sin prompts) por período indefinido, logs completos (con prompts) por 90 días, con eliminación automática conforme a la política de retención de datos de la organización.

## Componentes del sistema de auditoría centralizada

- Registro inmutable: cada evento se escribe en append-only storage (S3 con Object Lock, Kafka con retención configurable, o un sistema de audit logging como Immuta) que previene modificación o eliminación posterior
- Metadatos de negocio: campos obligatorios en cada log entry: `team_id`, `project_id`, `application_name`, `environment`, `model_used`, `provider`, `input_tokens`, `output_tokens`, `cost_usd`, `latency_ms`, `request_id`
- Gestión de PII en logs: opción de redacción automática de PII en prompts usando detectores (presidio, regex-based) antes de escribir al log; política configurable por equipo según sensibilidad de sus datos
- Query de logs: interfaz para buscar logs por `request_id` (para debugging de reportes de incidentes), por `team_id` y rango de tiempo (para reportes de uso), y por patrones de prompt (para identificar uso de prompts problemáticos)
- Integración con SIEM: exportación de eventos de auditoría a sistemas de seguridad corporativos (Splunk, Elasticsearch/ELK, Microsoft Sentinel) para correlación con otros eventos de seguridad de la organización

## Para recordar

El audit log de un LLM Gateway es la primera línea de investigación cuando ocurre un incidente de AI: "el modelo respondió algo inapropiado" solo puede investigarse con el prompt exacto que lo causó, y ese prompt solo existe en el log si el gateway lo registró.
