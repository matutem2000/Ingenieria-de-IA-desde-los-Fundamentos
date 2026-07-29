# Módulo 12 – Capítulo 01 – Sección 02

# El problema a resolver: definición del caso de uso, alcance y restricciones técnicas

El proyecto final construye un asistente técnico inteligente para ingenieros de software, capaz de responder preguntas sobre la base de conocimiento interna de una organización usando documentación técnica, ADRs, runbooks y tickets históricos como fuentes. El sistema debe operar dentro de restricciones concretas: latencia de respuesta inferior a 3 segundos para el percentil P95, costo máximo de 0.02 USD por petición, y capacidad de manejar hasta 50 consultas concurrentes sin degradación visible. El alcance técnico incluye ingesta de documentos PDF y Markdown, chunking semántico, búsqueda híbrida con Qdrant, un agente ReAct con acceso a herramientas externas, y una API REST expuesta con FastAPI. El caso de uso excluye explícitamente la generación de código arbitrario y la ejecución de comandos en sistemas externos, limitando la autonomía del agente a consultas de lectura.

## Restricciones técnicas definidas

- Latencia P95 < 3 segundos para el pipeline completo: retrieval + reranking + generación LLM
- Costo por petición < 0.02 USD contabilizando tokens de prompt y completion con el modelo seleccionado
- Concurrencia mínima de 50 peticiones simultáneas con throughput sostenido sin memory leaks detectables
- Superficie de ataque limitada: el agente no ejecuta código arbitrario ni accede a sistemas externos en escritura
- SLA de disponibilidad del 99.5% con health checks activos y restart automático mediante Kubernetes liveness probes

## Principio rector

Definir explícitamente qué queda fuera del alcance técnico es tan importante como definir qué está dentro — las restricciones son las que hacen posible comprometerse con métricas medibles y verificables.
