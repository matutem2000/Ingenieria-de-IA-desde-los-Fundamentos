# Módulo 7 – Capítulo 02 – Sección 02

# ReAct (Reason + Act): intercalar razonamiento con acciones externas

ReAct, presentado por Yao et al. (2022) en "ReAct: Synergizing Reasoning and Acting in Language Models", es el patrón de agente que alterna explícitamente entre generación de razonamiento (Thought) e invocación de acciones externas (Act), incorporando las observaciones de esas acciones (Observation) en el contexto antes del siguiente ciclo de razonamiento. A diferencia de CoT puro —donde el razonamiento es auto-contenido—, ReAct cierra el bucle entre pensamiento y mundo real: el agente puede buscar información en tiempo real, ejecutar código, leer archivos o consultar APIs, y usar esos resultados para refinar su razonamiento en el paso siguiente. Este patrón es la base arquitectónica de la mayoría de frameworks agénticos modernos: LangChain AgentExecutor, LangGraph con nodos de herramientas, y el `tool_use` workflow de Anthropic implementan variantes de ReAct. La calidad del Thought en cada paso determina directamente si la Action invocada será la correcta.

## Aspectos técnicos

- **Formato Thought-Action-Observation**: cada iteración del bucle genera texto en formato `Thought: [razonamiento] → Action: [tool_name(params)] → Observation: [resultado]`, que se acumula en el contexto
- **Grounding externo**: a diferencia de CoT puro, ReAct puede corregir errores de razonamiento basándose en evidencia real obtenida de herramientas, reduciendo alucinaciones en tareas que requieren información factual actualizada
- **Action space definition**: el conjunto de acciones disponibles (herramientas con nombre, descripción y schema) se inyecta en el system prompt; definiciones ambiguas degradan la calidad de las decisiones de acción
- **Interleaving obligatorio**: el razonamiento y la acción deben alternarse en el mismo hilo de generación del LLM; separar ambas fases en llamadas distintas al modelo rompe la coherencia del razonamiento
- **Overhead de tokens**: cada iteración ReAct añade al contexto el Thought (50-200 tokens), la Action (20-100 tokens) y la Observation (variable); tareas de 10 pasos pueden consumir 5K-15K tokens solo en trazas de razonamiento

## Para recordar

ReAct transforma al LLM de un sistema que razona en el vacío a uno que razona sobre evidencia real: cada observación de herramienta es información nueva que puede confirmar, refutar o redirigir el plan del agente.
