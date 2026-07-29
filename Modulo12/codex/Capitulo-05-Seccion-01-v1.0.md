# Módulo 12 – Capítulo 05 – Sección 01

# Threat model del sistema integrador: identificación de amenazas específicas del caso de uso

El threat model del proyecto aplica el marco STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) a los componentes específicos del sistema RAG agéntico. Para un asistente técnico que accede a documentación interna, las amenazas de mayor riesgo son: prompt injection directa (un usuario autenticado intenta manipular el comportamiento del agente mediante instrucciones embebidas en la query), prompt injection indirecta (un documento en la base de conocimiento contiene instrucciones maliciosas que el agente ejecuta al recuperarlo), y divulgación no autorizada de información (el agente devuelve documentos a los que el usuario no debería tener acceso por su rol). El threat model también identifica amenazas de DoS específicas de LLMs: token flooding (queries diseñadas para maximizar el uso de tokens del modelo) y retrieval amplification (queries que generan búsquedas repetidas en Qdrant). Cada amenaza se documenta con probabilidad estimada, impacto y control mitigante seleccionado.

## Amenazas identificadas por categoría STRIDE

- Spoofing: suplantación de identidad mediante tokens JWT expirados o robados; mitigación: validación de token en cada petición
- Tampering: inyección de instrucciones maliciosas en documentos de la base de conocimiento (prompt injection indirecta)
- Repudiation: ausencia de audit log que vincule cada respuesta al usuario y query que la generó
- Information Disclosure: retrieval de documentos con clasificación superior a los permisos del usuario autenticado
- DoS: token flooding con queries de 2000 caracteres que maximizan uso de context window del modelo
- Elevation of Privilege: tool chaining donde el agente es manipulado para encadenar herramientas en formas no previstas

## Para recordar

El threat model de un sistema de IA no es una formalidad de seguridad — es el documento que determina cuáles controles son no negociables y cuáles son mejoras opcionales, permitiendo priorizar el trabajo de hardening.
