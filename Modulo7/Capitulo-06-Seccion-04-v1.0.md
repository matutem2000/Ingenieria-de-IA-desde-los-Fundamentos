# Módulo 7 – Capítulo 06 – Sección 04

# Agente orquestador vs agentes especializados: roles y responsabilidades

En un sistema multiagente con patrón jerárquico, el agente orquestador y los agentes especializados tienen responsabilidades fundamentalmente distintas que deben estar claramente delimitadas para evitar solapamiento de funciones y degradación del sistema. El orquestador es responsable de la planificación de alto nivel (descomponer la tarea en subtareas y decidir qué agente ejecuta qué), la delegación (invocar a los agentes correctos con el contexto apropiado), el monitoreo de resultados intermedios (verificar que cada subtarea se completó correctamente), y la síntesis del resultado final. Los agentes especializados son responsables exclusivamente de ejecutar la subtarea asignada dentro de su dominio de expertise, sin necesidad de conocer el objetivo global ni el estado del sistema más allá de su tarea inmediata. Esta separación de responsabilidades permite reemplazar, actualizar o escalar agentes especializados sin modificar el orquestador, siempre que se respete el contrato de interfaz.

## Aspectos técnicos

- **Capacidades del orquestador**: razonamiento de planificación (qué hacer y en qué orden), routing de tareas (a qué agente especializado delegar cada subtarea), consolidación de resultados (combinar outputs de múltiples agentes en un resultado cohesivo), y manejo de fallos (qué hacer cuando un agente especializado falla)
- **Modelo de LLM para el orquestador**: el orquestador requiere el modelo con mejor capacidad de razonamiento y planificación disponible (GPT-4o, Claude 3.5 Sonnet), ya que sus errores de planificación se propagan a todos los agentes subordinados; los agentes especializados pueden usar modelos más ligeros y rápidos para sus tareas específicas
- **Stateless workers**: los agentes especializados idealmente son stateless entre invocaciones del orquestador; todo el estado necesario para ejecutar la subtarea se les provee en cada llamada, y su output se devuelve al orquestador sin mantener estado propio
- **Capacidades del agente especializado**: herramientas acotadas a su dominio, system prompt específico de su rol, knowledge base especializada (RAG sobre documentación técnica específica), y criterios de éxito bien definidos para su tipo de tarea
- **Delegación vs ejecución directa**: el orquestador debe poder decidir si ejecutar una subtarea directamente (sin delegar) o delegarla a un especialista; tareas triviales que no justifican el overhead de comunicación pueden ser ejecutadas por el propio orquestador

## Para recordar

El orquestador es el estratega y coordinador del sistema; los agentes especializados son los ejecutores expertos en su dominio: confundir estos roles —un orquestador que ejecuta tareas operativas o un especialista que intenta planificar el workflow global— es una causa frecuente de ineficiencia y errores en sistemas multiagente.
