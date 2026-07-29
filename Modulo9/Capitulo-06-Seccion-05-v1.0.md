# Módulo 9 – Capítulo 06 – Sección 05

# Auditoría de acceso a datos: logs de qué datos fueron procesados por el modelo

La auditoría de acceso a datos en sistemas de IA responde a una pregunta crítica para compliance regulatorio (GDPR, HIPAA, CCPA): ¿qué datos de qué usuarios fueron procesados por qué modelo en qué momento? Esta pregunta, trivial en sistemas de base de datos relacionales con logs de queries, se vuelve compleja en sistemas de IA donde el "procesamiento" de un dato es difuso: ¿un dato fue procesado cuando fue incluido en el contexto del modelo? ¿cuando fue parte del corpus de fine-tuning? ¿cuando fue recuperado por RAG pero el modelo no lo utilizó directamente en su respuesta? Un sistema de auditoría robusto para IA debe registrar no solo los inputs y outputs de cada request, sino también qué documentos fueron recuperados del vectorstore (con sus identificadores), qué herramientas fueron invocadas por el agente, y qué modelo y versión procesó cada request. Esta granularidad es necesaria para responder a las solicitudes de acceso a datos del GDPR (DSAR - Data Subject Access Requests) y para el análisis forense de incidentes de seguridad.

## Aspectos técnicos

- Estructura del audit log para sistemas de IA: cada evento de inferencia debe registrar: user_id, session_id, timestamp, model_id + version, system_prompt_hash (no el contenido), user_input (completo o resumido según políticas de retención), retrieved_document_ids (IDs de documentos del vectorstore), tool_calls (herramienta + argumentos), model_output_hash o output completo, y latency + token_count
- Inmutabilidad del audit log: los logs de auditoría deben ser inmutables (write-once) para ser válidos como evidencia regulatoria; opciones técnicas: Amazon S3 Object Lock con COMPLIANCE mode, Azure Immutable Blob Storage, o sistemas de log con firma criptográfica (syslog-ng con TLS client certificates a un SIEM centralizado)
- Granularidad de tracking de documentos RAG: cada documento recuperado debe registrarse con su ID único en el vectorstore, el score de similitud, y si fue efectivamente incluido en el contexto enviado al modelo — este tracking permite responder DSAR de GDPR ("¿qué documentos míos fueron usados para generar respuestas para otros usuarios?")
- Retention y borrado de logs: el derecho al olvido del GDPR (Art. 17) aplica a los datos del usuario en los logs; el sistema debe implementar borrado selectivo de eventos que contienen datos de un usuario específico sin borrar el registro completo del sistema — técnicamente implementado mediante cifrado de logs por usuario con posterior descarte de la clave de descifrado
- DSAR compliance automation: sistemas que procesan datos de usuarios sujetos a GDPR deben ser capaces de responder automáticamente a una DSAR dentro de 30 días; esto requiere que el audit log sea consultable por user_id y que los datos relacionados puedan exportarse en formato legible

## Para recordar

El audit log de un sistema de IA es el registro legal del procesamiento de datos: sin él, es imposible responder a requisitos regulatorios de GDPR, HIPAA o CCPA, ni realizar análisis forense de incidentes de seguridad; y un audit log incompleto o mutable es equivalente a no tener audit log desde el punto de vista de compliance.
