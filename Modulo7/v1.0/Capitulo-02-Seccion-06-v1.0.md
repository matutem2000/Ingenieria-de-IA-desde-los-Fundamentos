# Módulo 7 – Capítulo 02 – Sección 06

## Cierre: la calidad del razonamiento determina la calidad de las acciones del agente

El capítulo de razonamiento y planificación establece una verdad operativa central: en sistemas agénticos, el LLM no es solo el motor de generación de texto sino el módulo de toma de decisiones que determina qué acción ejecutar, en qué orden y con qué parámetros. La calidad de esas decisiones —y por tanto la calidad de los resultados del agente— está directamente limitada por la calidad del razonamiento que las precede. Un agente cuyo razonamiento es opaco, implícito o apresurado producirá acciones incorrectas con mayor frecuencia, y esos errores se amplificarán en cadenas largas hasta hacer la tarea fallida.

Las cuatro técnicas cubiertas en este capítulo —CoT, ReAct, ToT y planificación jerárquica— no son alternativas entre sí sino herramientas con diferentes perfiles de costo-beneficio que se aplican a diferentes tipos de problemas. El error más común es elegir entre ellas basándose en popularidad o en lo que se usó en el último proyecto: la elección correcta depende de la estructura del problema, el perfil de latencia requerido, y el presupuesto de tokens disponible. La tabla siguiente proporciona una guía de referencia rápida para esa decisión.

### Tabla comparativa de técnicas de razonamiento agéntico

| Técnica | Overhead de tokens | Latencia relativa | Caso de uso ideal | Limitación principal | Frameworks con soporte nativo |
|---|---|---|---|---|---|
| **Chain-of-Thought (CoT)** | Bajo (+50-200 tokens por paso) | Mínima (~0ms adicional) | Razonamiento sobre información ya disponible en el contexto; decisiones de qué herramienta usar | No puede corregir errores con información nueva; faithfulness del razonamiento no garantizada | Cualquier LLM con system prompt |
| **ReAct** | Medio (+100-500 tokens por iteración incluyendo observaciones) | Igual a CoT + latencia de herramientas | Tareas que requieren información externa en tiempo real; verificación factual; búsqueda iterativa | Overhead de tokens por observación; latencia acumulada en cadenas largas | LangGraph, LangChain AgentExecutor, AutoGen, API nativa de Anthropic/OpenAI |
| **Tree of Thoughts (ToT)** | Alto (k×d llamadas adicionales al LLM, donde k=candidatos y d=profundidad) | Alta (5-20x respecto a CoT) | Planificación inicial de tareas con fuertes dependencias entre decisiones; problemas donde un error temprano invalida el resto | Prohibitivo para uso en cada iteración del ciclo; requiere un evaluador de calidad para ser útil | Implementación manual; no nativo en frameworks estándar |
| **Planificación jerárquica** | Medio-Alto (una llamada de planificación adicional al inicio) | Media (overhead de planificación al inicio, ganancia de paralelismo en ejecución) | Tareas decomponibles en subtareas independientes; workflows donde se requiere aprobación del plan antes de ejecutar | Requiere re-planificación cuando los supuestos del plan original no se cumplen | LangGraph (nodos paralelos), CrewAI (Process.hierarchical), LLM Compiler |
| **Verificación y autocorrección** | Variable (0 para verificación programática; +1 llamada LLM para reflexión o judge) | Variable | Pasos críticos donde el error tiene alto impacto; outputs que deben cumplir contratos de formato | Fallos ante sesgos sistemáticos del modelo; costo prohibitivo si se aplica a cada paso | LangGraph (nodo de evaluación), LangSmith (evaluación automatizada) |

### Cuándo usar cada técnica: guía de decisión práctica

**CoT** es el default razonable para cualquier agente nuevo. Siempre actívalo, ya sea como Zero-Shot CoT ("piensa paso a paso") o como Few-Shot CoT con ejemplos del dominio. El costo es mínimo y el beneficio es consistente.

**ReAct** es la extensión natural de CoT cuando la tarea requiere información externa. Si el agente necesita buscar, leer, ejecutar o verificar datos del mundo real, ReAct es el patrón base a usar. Casi todos los frameworks agénticos modernos lo implementan nativamente.

**ToT** se justifica cuando la tarea tiene características específicas: múltiples caminos de solución con diferentes quality levels, donde la elección temprana entre ellos tiene consecuencias irrecuperables en los pasos posteriores. El caso de uso más frecuente en ingeniería es la planificación inicial de una arquitectura de software o de una estrategia de investigación compleja. Fuera de ese caso de uso, el costo en tokens y latencia raramente justifica el beneficio.

**Planificación jerárquica** se justifica cuando la tarea tiene más de 5-7 pasos y las subtareas son suficientemente independientes como para paralelizarse o para asignarse a agentes especializados. Si la tarea es inherentemente secuencial y sin paralelismo natural, la planificación jerárquica añade overhead sin beneficio proporcional.

**Autocorrección** siempre que los pasos críticos del ciclo produzcan outputs formalizables (código, JSON, URLs). Para outputs semánticos, usar LLM-judge selectivamente en los pasos de mayor impacto, no en cada paso del ciclo.

Invertir en mejorar la calidad del razonamiento —a través de prompts más estructurados, técnicas de reflexión, y evaluación de pasos intermedios— tiene mayor retorno que agregar más herramientas o aumentar el límite de iteraciones. La diferencia entre un agente que completa el 60% de las tareas y uno que completa el 90% rara vez está en las herramientas disponibles; está en la calidad del razonamiento que guía cuándo y cómo usarlas.

## Principio rector

La diferencia entre un agente que completa el 60% de las tareas y uno que completa el 90% rara vez está en las herramientas disponibles; está en la calidad del razonamiento que guía cuándo y cómo usarlas. Invertir en razonamiento antes de invertir en herramientas.

El capítulo siguiente completa el análisis del lado de las herramientas: si el razonamiento determina qué hacer, las herramientas determinan qué es posible hacer. Diseñarlas correctamente —con la misma precisión con la que se diseñan los prompts de razonamiento— es el próximo desafío de la ingeniería agéntica.

*"Thinking is the hardest work there is, which is probably the reason why so few engage in it."* — sentencia habitualmente atribuida a Henry Ford; independientemente de su autoría original, el principio se aplica literalmente a los sistemas agénticos: forzar al modelo a generar pensamiento explícito en tokens produce consistentemente mejores decisiones que permitirle responder de forma inmediata y sin articulación del razonamiento.
