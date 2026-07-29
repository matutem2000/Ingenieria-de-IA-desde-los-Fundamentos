# Módulo 9 – Capítulo 08 – Sección 06

# Cierre: sin trazabilidad no hay auditoría posible ni aprendizaje de incidentes

La trazabilidad y la auditoría en sistemas de IA no son capacidades que se añaden por compliance sino herramientas de ingeniería que mejoran activamente la seguridad del sistema: los logs bien diseñados permiten detectar ataques que de otro modo serían invisibles, los análisis forenses post-incidente producen mejoras concretas en los controles, y la integración con SIEM convierte los eventos aislados del sistema de IA en parte del programa de seguridad corporativo con correlación cross-system. Un sistema de IA sin trazabilidad es operado con los ojos cerrados: no se sabe si está siendo atacado ahora mismo, no se puede saber qué ocurrió cuando algo sale mal, y no se puede aprender de los incidentes para mejorar. La inversión en un sistema de logging e auditoría robusto —schema bien diseñado, almacenamiento inmutable, integración con SIEM, playbooks de IR— tiene un ROI claramente positivo medido en tiempo de detección de incidentes reducido, tiempo de respuesta reducido, y capacidad de demostrar compliance regulatorio cuando es auditado.

*"Logging is not just for debugging — it is the historical record of your system's behavior, and without it you are flying blind into the past."* — Kelsey Hightower, Staff Developer Advocate en Google Cloud y uno de los ingenieros más influyentes en cloud-native architecture, sobre el rol fundamental del logging en sistemas de producción.

## Conceptos clave del capítulo

- Schema de security events: user_id + session_id + model_id + system_prompt_hash + retrieved_document_ids + tool_calls + safety_scores — mínimo vital para análisis forense y compliance GDPR/HIPAA
- Inmutabilidad de logs: S3 Object Lock COMPLIANCE mode, Azure Immutable Blob, firma criptográfica HMAC-SHA256 con cadena de hashes, forwarding a SIEM en cuenta independiente como copia inmutable secundaria
- Trazabilidad de decisiones: CoT logging para razonamiento del modelo, citation generation para atribución de fuentes RAG, versioning del system prompt, model card y version tracking por request
- SIEM integration: formato CEF/OCSF, alertas por correlación (rate limit + IP nueva = extracción; safety triggers repetidos = jailbreak sistemático), dashboards de seguridad específicos para IA
- Incident response: playbooks específicos por tipo de incidente (jailbreak, RAG poisoning, data leakage), IoCs de IA definidos como umbrales de alerta, opciones de contención escalonadas, análisis forense post-incidente con mejoras documentadas

## Idea central

La trazabilidad es el prerequisito para la seguridad operacional de sistemas de IA: sin logs completos, inmutables e integrados con el SIEM corporativo, un sistema de IA en producción es una caja negra desde la cual no es posible detectar, contener ni aprender de los incidentes de seguridad.
