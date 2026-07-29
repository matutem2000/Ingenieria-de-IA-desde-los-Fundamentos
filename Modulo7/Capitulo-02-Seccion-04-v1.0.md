# Módulo 7 – Capítulo 02 – Sección 04

# Planificación jerárquica: descomposición de tareas complejas en subtareas

La planificación jerárquica es el proceso mediante el cual un agente descompone un objetivo de alto nivel en un árbol de subtareas más manejables, donde cada subtarea puede ser asignada a un sub-agente especializado, ejecutada con herramientas específicas o resuelta con una llamada LLM independiente. Este patrón —implementado en sistemas como LLM Compiler (Khattab et al., 2023), AutoGen con agentes anidados y en el `plan-and-execute` agent de LangChain— separa explícitamente la fase de planificación (generación del plan estructurado) de la fase de ejecución (ejecución paso a paso del plan), permitiendo mayor control, paralelización y revisión del plan antes de comprometer recursos. La descomposición jerárquica reduce el riesgo de desviación del objetivo (goal drift) en tareas largas, ya que el agente siempre puede referenciar el plan original para verificar que sus acciones actuales contribuyen al objetivo de nivel superior.

## Aspectos técnicos

- **Planner-Executor split**: el planner (LLM con prompt de planificación) genera un plan estructurado (JSON, lista numerada o grafo de dependencias) que el executor sigue; separa las responsabilidades de estrategia y ejecución
- **Descomposición recursiva**: subtareas complejas pueden descomponerse a su vez en sub-subtareas; la profundidad máxima del árbol debe limitarse para evitar over-decomposition que añade latencia sin valor
- **Paralelización de subtareas**: subtareas independientes (sin dependencias entre sí) pueden ejecutarse en paralelo usando async/await o workers concurrentes; LangGraph implementa esto con nodos paralelos en el grafo de estado
- **Re-planificación dinámica**: cuando una subtarea falla o produce resultados inesperados, el agente debe poder actualizar el plan en lugar de continuar ciegamente; requiere un nodo de evaluación de plan en el grafo de estado
- **Granularidad de subtareas**: subtareas demasiado granulares generan overhead de coordinación; subtareas demasiado grandes recrean el problema original; el tamaño óptimo es aquel que puede ser resuelto con 2-5 acciones de herramienta

## Principio rector

La planificación jerárquica no elimina la incertidumbre de la ejecución, pero la hace manejable: al dividir el problema antes de actuar, el agente puede detectar y corregir desviaciones localmente sin perder el objetivo global.
