# Módulo 12 – Capítulo 04 – Sección 01

# Diseño del agente: objetivos, herramientas y ciclo de razonamiento elegido

El agente del proyecto final implementa el patrón ReAct (Reasoning + Acting) usando LangGraph, donde cada paso del ciclo de razonamiento consiste en: observar el estado actual, razonar sobre qué herramienta usar y con qué argumentos, ejecutar la herramienta, observar el resultado y decidir si continuar o entregar la respuesta final. El objetivo del agente es responder preguntas técnicas complejas que pueden requerir múltiples búsquedas en la base de conocimiento, correlación de información de distintas fuentes y síntesis de respuestas con citación explícita. Las herramientas disponibles son: `search_knowledge_base(query: str, filters: dict, top_k: int) -> list[Document]`, `get_document_by_id(doc_id: str) -> Document`, y `list_available_sources(document_type: str) -> list[str]`; cada herramienta tiene un contrato de interfaz tipado con Pydantic que el LLM usa para generar llamadas correctas. El ciclo tiene un límite de max_iterations=5 para prevenir bucles, con un nodo de fallback que devuelve la respuesta parcial más informativa disponible.

## Componentes del diseño agéntico

- Grafo de estado LangGraph: nodos reason, act, observe y respond con edges condicionales basados en el output del LLM
- System prompt del agente: instrucciones de grounding, formato de citación obligatoria y criterios de parada explícitos
- Contrato de herramientas: esquemas Pydantic para inputs y outputs de cada tool, con validación antes de la ejecución
- Ciclo ReAct: secuencia Thought → Action → Observation con logging estructurado de cada paso para trazabilidad
- Condición de parada: el agente entrega respuesta cuando classifica que tiene suficiente información o alcanza max_iterations

## Para recordar

El diseño del ciclo de razonamiento del agente debe incluir condiciones de parada explícitas antes de la implementación — un agente sin límites claros puede entrar en bucles que consumen tokens y tiempo sin converger a una respuesta.
