# Módulo 7 – Capítulo 01 – Sección 02

# De los chatbots a los agentes: el salto del turno único a la autonomía

Un chatbot tradicional opera en un esquema de un turno por ciclo: recibe un mensaje, genera una respuesta y espera al siguiente input humano; su estado entre turnos depende exclusivamente del historial de conversación que el desarrollador decide pasar en cada llamada. Un agente rompe ese esquema: dado un objetivo de alto nivel, el sistema ejecuta múltiples pasos de forma autónoma —llamadas a herramientas, análisis de resultados, iteraciones de corrección— hasta alcanzar una condición de terminación sin requerir intervención humana en cada paso intermedio. Frameworks como LangChain ReAct o LangGraph implementan este salto mediante bucles explícitos donde el LLM actúa como controlador de flujo, decidiendo en cada iteración si debe invocar otra herramienta, continuar razonando o entregar el resultado final. Este cambio de paradigma implica que el comportamiento del sistema emergente no puede predecirse leyendo solo el prompt inicial; hay que analizar el grafo de estados completo.

## Aspectos técnicos

- **Single-turn vs multi-step**: en chatbots el flujo es `user → LLM → response`; en agentes es `user_goal → [tool_call → observation → reasoning]^n → final_answer`
- **Condición de terminación**: los agentes necesitan criterios explícitos de parada —respuesta al usuario, fallo irrecuperable, límite de iteraciones (max_steps=25 en LangGraph)— para evitar bucles infinitos
- **Estado compartido**: a diferencia del chatbot sin estado, el agente mantiene un `AgentState` mutable que acumula observaciones, resultados de herramientas y decisiones a lo largo del ciclo
- **Latencia acumulada**: cada paso añade al menos una llamada de inferencia (100-500ms por paso) más la latencia de la herramienta invocada; tareas de 10 pasos pueden tardar 5-30 segundos end-to-end
- **Control de flujo por el modelo**: el LLM elige cuándo llamar a qué herramienta a través de function calling estructurado, no a través de lógica imperativa codificada por el desarrollador

## Idea central

El salto de chatbot a agente no es de complejidad de prompt sino de arquitectura: exige un bucle de ejecución explícito, gestión de estado persistente y criterios claros de terminación.
