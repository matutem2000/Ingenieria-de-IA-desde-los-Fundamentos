# Módulo 9 – Capítulo 05 – Sección 04

# Sandboxing de herramientas de agentes: contención de ejecución de código y acceso a sistemas

El sandboxing en sistemas agénticos es el conjunto de mecanismos técnicos que limitan el alcance del daño potencial cuando un agente es comprometido: si el agente ejecuta código malicioso o es inducido a realizar acciones no autorizadas, el sandbox garantiza que esas acciones no pueden propagarse más allá del entorno controlado. En el contexto de ejecución de código (el caso más crítico), el sandboxing debe aislar el proceso de ejecución del sistema de archivos del host, la red, las credenciales del sistema y otros procesos. OpenAI implementa Code Interpreter (la herramienta de análisis de código de ChatGPT) en containers Docker con restricciones de red estrictas; AWS Lambda proporciona entornos de ejecución aislados con tiempo de vida limitado; y tecnologías como gVisor, Firecracker (AWS) y WebAssembly (WASM) proporcionan diferentes capas de aislamiento con diferentes trade-offs de performance y seguridad.

## Aspectos técnicos

- Sandboxing de ejecución de código: ejecutar el código generado por el agente en un container Docker sin acceso a red, con filesystem de solo lectura excepto en directorios temporales, con límites de CPU/memoria (cgroups), y con tiempo máximo de ejecución; tecnologías como gVisor (Google) añaden una capa adicional de aislamiento del kernel
- Control de acceso a herramientas en el nivel de runtime: cada llamada a una herramienta debe pasar por un proxy de autorización que verifica que la operación específica (lectura vs. escritura, directorio específico, API endpoint específico) está dentro del scope autorizado para el agente en el contexto de la request actual
- Network sandboxing: los agentes con acceso a internet deben operar a través de un proxy HTTP egress que filtra destinos permitidos (allowlist de dominios) y rechaza conexiones a IPs privadas (169.254.0.0/16, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) para prevenir SSRF vía herramientas del agente
- Secrets management en agentes: las credenciales que el agente usa para llamar APIs externas nunca deben estar en el contexto del modelo (en el system prompt o en el historial); deben ser inyectadas en el entorno del agente mediante variables de entorno gestionadas por un vault (HashiCorp Vault, AWS Secrets Manager) e inaccessibles para el LLM
- Ephemeral environments: para tareas de alta sensibilidad, el agente debe ejecutarse en un entorno efímero que se destruye completamente al finalizar la tarea, incluyendo todos los artefactos temporales, variables de entorno y estado de ejecución — sin persistencia que el atacante pueda explotar en requests posteriores

## Para recordar

El sandboxing de herramientas agénticas debe diseñarse asumiendo que el LLM puede ser comprometido: el sandbox debe garantizar que incluso un agente completamente bajo control del atacante no puede acceder a credenciales, modificar sistemas fuera de su scope, o comunicarse con hosts no autorizados.
