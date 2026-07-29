# Módulo 7 – Capítulo 08 – Sección 02

# Privilege escalation: un agente que obtiene más permisos de los necesarios

El privilege escalation en sistemas agénticos ocurre cuando un agente logra ejercer permisos o capacidades que superan los que le fueron explícitamente concedidos, ya sea por diseño deficiente de las herramientas (una herramienta de lectura que también puede escribir), por encadenamiento de herramientas que combinan permisos individuales para lograr efectos no previstos (leer un archivo de configuración + ejecutar código = acceso a credenciales + ejecución arbitraria), o por prompt injection que induce al agente a invocar herramientas de formas no contempladas por el diseñador. Un patrón específico de escalación es el "confused deputy problem": el agente actúa como intermediario entre el usuario y sistemas externos, y un atacante puede instruirlo para que use sus permisos legítimos en beneficio del atacante. Las mitigaciones incluyen el principio de mínimo privilegio (cada herramienta tiene exactamente los permisos necesarios para su función), la validación pre-ejecución (verificar que la acción solicitada está dentro del scope autorizado antes de ejecutarla), y el sandboxing de herramientas.

## Puntos críticos

- **Confused deputy problem**: el agente tiene permisos legítimos que un atacante puede aprovecharse mediante prompt injection; mitigado con confirmación humana para acciones de alto impacto y con validación de que la acción solicitada es coherente con el objetivo declarado de la tarea
- **Tool chaining risks**: la combinación de herramientas legítimas puede producir efectos no previstos; p.ej. `read_env_vars` + `execute_code` + `make_http_request` permite exfiltrar credenciales aunque ninguna herramienta individual lo permita; requiere análisis de flujo de información entre herramientas
- **Credenciales en contexto**: nunca inyectar credenciales (API keys, tokens, contraseñas) directamente en el contexto del agente; usar variables de entorno o secret managers (AWS Secrets Manager, Vault) accesibles solo por las herramientas que los necesitan, no por el LLM
- **RBAC para herramientas**: implementar control de acceso basado en roles a nivel de herramientas; diferentes usuarios o diferentes tareas pueden tener acceso a diferentes subsets de herramientas, con las restricciones validadas a nivel de infraestructura, no solo a nivel de prompt
- **Audit log de invocaciones**: registrar cada invocación de herramienta con usuario, timestamp, parámetros y resultado; los logs inmutables permiten detectar escalaciones y proveen evidencia forense post-incidente

## Para recordar

El privilege escalation en agentes es más insidioso que en sistemas tradicionales porque el agente puede ser manipulado para escalar sus propios permisos mediante razonamiento —no mediante un exploit técnico— lo que requiere defensas en profundidad tanto en el modelo de permisos como en la detección de comportamiento anómalo.
