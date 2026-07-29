# Módulo 12 – Capítulo 05 – Sección 05

# Red teaming del sistema: ejecución de casos de ataque y documentación de resultados

El red teaming del proyecto final ejecuta una sesión estructurada de 50 ataques documentados en cuatro categorías: prompt injection directa (15 casos), prompt injection indirecta mediante documentos maliciosos (15 casos), evasión de filtros de autorización (10 casos) y DoS agéntico mediante queries de alta complejidad (10 casos). Cada ataque se documenta con: descripción del payload, comportamiento observado del sistema, clasificación del resultado (bypass exitoso / bypass parcial / mitigado) y control que bloqueó el ataque o recomendación de mejora si fue exitoso. Los ataques de prompt injection directa incluyen variantes clásicas: "ignore previous instructions", roleplay con personas alternativas, instrucciones en idiomas distintos al inglés para evadir la lista negra, y codificación Base64 de instrucciones maliciosas. La tasa objetivo de bypass es inferior al 5% (máximo 2-3 ataques exitosos de los 50 ejecutados), con los bypasses exitosos convertidos en casos de test de regresión.

## Categorías de ataques del red teaming

- Prompt injection directa: 15 variantes incluyendo roleplay, idiomas alternativos y instrucciones codificadas en Base64
- Prompt injection indirecta: 15 documentos con instrucciones maliciosas embebidas en contenido técnico aparentemente legítimo
- Evasión de autorización: 10 casos de queries que intentan acceder a document_types fuera del allowed_document_types del usuario
- DoS agéntico: 10 queries diseñadas para maximizar iteraciones del agente y consumo de tokens sin respuesta útil
- Documentación de resultados: reporte con payload, comportamiento observado, clasificación y acción correctiva si hubo bypass

## Para recordar

Los bypasses exitosos del red teaming son el input más valioso para mejorar los controles de seguridad — cada ataque que funciona se convierte en un test de regresión que el sistema debe pasar antes del siguiente deploy.
