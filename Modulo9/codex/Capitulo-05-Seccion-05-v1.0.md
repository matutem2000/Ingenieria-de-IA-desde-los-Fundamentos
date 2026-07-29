# Módulo 9 – Capítulo 05 – Sección 05

# Authorization en herramientas: validar que el agente tiene permiso para cada acción

La autorización en sistemas agénticos es el control que verifica que el agente tiene permiso explícito para ejecutar una acción específica en nombre del usuario específico que originó la request, distinguiéndola del modelo de "el agente tiene permiso para usar todas las herramientas" que es la implementación más común y menos segura. La arquitectura correcta separa el plano de datos (lo que el agente procesa como LLM) del plano de control (qué acciones puede ejecutar y bajo qué condiciones), y todas las acciones pasan por el plano de control para verificación de autorización antes de ser ejecutadas. Esto es análogo al principio de separation of privilege en seguridad informática clásica: el agente que procesa documentos no debe tener los mismos privilegios de ejecución que el agente que modifica registros en producción. Los frameworks agénticos modernos como LangGraph y CrewAI están implementando patrones de authorization más granulares, pero en la mayoría de los deployments de producción actuales la autorización es binaria ("el agente puede o no puede usar la herramienta") sin granularidad a nivel de operación o recurso.

## Aspectos técnicos

- Authorization granular por operación: en lugar de "el agente puede usar la herramienta de base de datos", el control debe ser "el agente puede ejecutar SELECT en la tabla customers para el user_id del usuario actual, pero no UPDATE, DELETE, ni acceder a otras tablas" — autorización a nivel de operación y recurso específico
- Human-in-the-loop para acciones críticas: acciones irreversibles o de alto impacto (enviar emails, borrar archivos, confirmar transacciones financieras, publicar contenido) deben requerir confirmación explícita del usuario en cada ejecución — no es suficiente con la autorización inicial de "el agente puede enviar emails"
- Contextual authorization: la autorización puede variar según el contexto de la request; un agente puede estar autorizado a leer datos del cliente actual pero no de otros clientes, o a modificar solo documentos creados por el usuario actual — el plano de control debe evaluar el contexto completo de cada acción, no solo el tipo de herramienta
- Audit trail de acciones: cada acción ejecutada por el agente debe registrarse con: el usuario que originó la request, el timestamp, la herramienta invocada, los argumentos completos de la invocación, el resultado, y el estado de autorización (aprobada/denegada) — este log es la base para auditoría y análisis forense de incidentes
- Revocación dinámica de permisos: si se detecta comportamiento anómalo del agente (múltiples llamadas a herramientas sensibles en tiempo corto, acceso a recursos fuera del pattern habitual), el plano de control debe poder revocar permisos en tiempo real sin terminar la sesión completa

## Para recordar

La autorización en sistemas agénticos debe ser tan granular como el impacto de las acciones que el agente puede ejecutar: el modelo "el agente tiene acceso a todas las herramientas" es equivalente a dar al agente privilegios de administrador del sistema, y cualquier compromiso del agente se convierte inmediatamente en el peor escenario posible.
