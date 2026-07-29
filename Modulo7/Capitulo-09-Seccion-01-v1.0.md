# Módulo 7 – Capítulo 09 – Sección 01

# Arquitectura de despliegue: stateless vs stateful, sincrónico vs asincrónico

El despliegue de agentes en producción requiere decisiones arquitectónicas que determinan el comportamiento bajo carga, la recuperación ante fallos y la experiencia del usuario. El primer eje es el modelo de estado: agentes stateless delegan toda la persistencia de estado al cliente o a una capa de almacenamiento externa, lo que facilita el escalado horizontal (cualquier instancia puede manejar cualquier request) pero requiere que el estado completo sea transmitido o recuperado en cada request; agentes stateful mantienen el estado internamente (en memoria o en un almacenamiento local), lo que simplifica la lógica del agente pero complica el escalado y la recuperación ante fallos de la instancia. El segundo eje es el modelo de ejecución: síncrono (el cliente espera la respuesta del agente antes de continuar, apropiado para tareas de <30 segundos) vs asíncrono (el cliente recibe inmediatamente un job_id y consulta o recibe notificación cuando la tarea termina, necesario para tareas largas de minutos u horas). La mayoría de los sistemas de producción usan un modelo híbrido: stateless con persistencia externa + asíncrono con streaming de pasos intermedios.

## Aspectos técnicos

- **Stateless + external state**: el agente recibe el estado completo en cada request (historial, contexto, configuración) desde un almacenamiento externo (Redis para estado de sesión, PostgreSQL para historial persistente); permite escalado horizontal sin sticky sessions
- **Stateful (no recomendado para escala)**: el agente mantiene estado en memoria de la instancia; requiere sticky routing (el mismo cliente siempre llega a la misma instancia) lo que complica el balanceo de carga y la recuperación ante crashes
- **Síncrono con streaming**: el servidor envía events via Server-Sent Events (SSE) o WebSocket mientras el agente ejecuta; el cliente recibe cada paso del agente (tool call, observation, reasoning) en tiempo real sin esperar el resultado final; mejora la UX en tareas de 10-60 segundos
- **Asíncrono con job queue**: el request del cliente encola la tarea en un sistema de cola (Celery + Redis, Bull + Redis, SQS); un worker independiente ejecuta el agente y almacena el resultado; el cliente hace polling al endpoint de estado o recibe un webhook cuando termina; obligatorio para tareas de >60 segundos
- **Timeout boundaries**: en modo síncrono, definir un timeout del servidor (p.ej. 120s para FastAPI/uvicorn) y un timeout del agente (max_steps * estimated_step_latency); en modo asíncrono, los timeouts son del worker y del total de la tarea (p.ej. 10 minutos máximo)

## Principio rector

La arquitectura de despliegue de un agente debe decidirse en función del perfil de latencia de la tarea: tareas de <30s son candidatas a síncrono con streaming; tareas de 30s-10min requieren asíncrono con job queue; tareas de >10min requieren arquitecturas de long-running jobs con checkpointing.
