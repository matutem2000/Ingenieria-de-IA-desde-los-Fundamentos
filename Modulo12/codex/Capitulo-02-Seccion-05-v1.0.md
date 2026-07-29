# Módulo 12 – Capítulo 02 – Sección 05

# ADR 004: estrategia de seguridad — controles seleccionados y modelo de amenazas

El ADR-004 documenta la estrategia de seguridad del sistema, incluyendo el modelo de amenazas STRIDE aplicado, los controles seleccionados y los riesgos residuales aceptados. El modelo de amenazas identifica como amenazas de alta prioridad para sistemas RAG agénticos: prompt injection directa (usuario inyecta instrucciones en la query), prompt injection indirecta (documentos en la base de conocimiento contienen instrucciones maliciosas), y escalación de privilegios mediante tool chaining (el agente es manipulado para encadenar herramientas en formas no previstas). Los controles implementados incluyen: validación de inputs con Pydantic y rechazo de payloads con patrones de injection conocidos, output filtering con detección de PII antes de devolver respuestas al usuario, y separación explícita de instrucciones de sistema y datos de usuario mediante delimitadores XML que reducen la eficacia de injection indirecta.

## Controles de seguridad seleccionados

- Input validation: Pydantic schema con longitud máxima de 2000 caracteres y detección de patrones de injection vía lista negra
- Instrucción de sistema hardeneada: uso de delimitadores XML (<user_query></user_query>) para separar instrucciones de datos
- Output filtering: detección de PII (emails, números de teléfono, tokens) con regex + NER antes de devolver respuesta al usuario
- Rate limiting: 10 peticiones por minuto por usuario autenticado, 100 por hora, con respuesta 429 y Retry-After header
- Audit logging: registro de cada petición con user_id, timestamp, query hasheada y tool calls ejecutadas para trazabilidad

## Principio rector

El ADR-004 no enumera todos los controles de seguridad posibles — documenta los seleccionados, los descartados y los riesgos residuales que el equipo acepta conscientemente tras el análisis de amenazas.
