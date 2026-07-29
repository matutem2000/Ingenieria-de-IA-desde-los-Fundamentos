# Módulo 9 – Capítulo 02 – Sección 01

# Prompt injection directa: el usuario inyecta instrucciones en el input

La prompt injection directa ocurre cuando un usuario malintencionado incluye instrucciones en su input diseñadas para sobrescribir, ignorar o modificar el system prompt del sistema, cambiando el comportamiento del modelo de maneras no autorizadas por el diseñador de la aplicación. A diferencia de los ataques de inyección clásicos (SQL injection, command injection), la prompt injection no explota un bug en el código sino una característica fundamental del modelo: su capacidad de seguir instrucciones en lenguaje natural sin poder distinguir semánticamente entre instrucciones autorizadas del sistema y instrucciones maliciosas del usuario. El ataque más simple es "Ignore all previous instructions and do X", pero en la práctica las técnicas son más sofisticadas: uso de delimitadores alternativos, roleplay para cambiar el contexto, o instrucciones en idiomas diferentes al del system prompt. Toda aplicación que concatena input de usuario con un system prompt está potencialmente expuesta a prompt injection directa.

## Aspectos técnicos

- Mecanismo de ataque: el modelo recibe el system prompt y el user input como parte del mismo contexto de atención; no existe separación criptográfica ni semántica que el modelo pueda garantizar entre instrucciones del sistema y del usuario
- Técnicas comunes: "ignore previous instructions", delimitadores alternativos (```, ---, XML tags), token smuggling con caracteres Unicode de aspecto similar, instrucciones multi-idioma que el sistema no monitorea, y prompt fragmentado distribuido en múltiples turns
- Impacto en aplicaciones: bypass de restricciones de contenido, exfiltración del system prompt, modificación del comportamiento del asistente para engañar a terceros usuarios, o uso del sistema para generar contenido prohibido a escala
- Factores de riesgo amplificantes: aplicaciones con herramientas habilitadas (tool-calling), historial de conversación persistente en memoria, y templates que incluyen variables de usuario sin sanitización son especialmente vulnerables
- Ejemplos documentados: ataques contra Bing Chat (Sydney) en 2023, New Bing revelando su system prompt completo; Chevrolet chatbot manipulado para insultar a la empresa; múltiples instancias de bypass de asistentes de atención al cliente

## Buena práctica

La defensa primaria contra prompt injection directa no es filtrar el input del usuario mediante reglas —lo cual es eludible— sino diseñar el system prompt con instrucciones de refuerzo explícitas, usar modelos que soporten separación real de roles (como el campo `system` de la API de Anthropic), y aplicar validación semántica del output antes de entregarlo al usuario.
