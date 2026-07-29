# Módulo 7 – Capítulo 02 – Sección 03

# Tree of Thoughts: exploración de múltiples caminos de razonamiento

Tree of Thoughts (ToT), propuesto por Yao et al. (2023) en "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", extiende CoT de un proceso lineal a una búsqueda en árbol: el modelo genera múltiples "pensamientos" candidatos en cada paso, evalúa el valor de cada nodo (ya sea con un evaluador heurístico o mediante el propio LLM) y expande los más prometedores usando estrategias de búsqueda como BFS (Breadth-First Search) o DFS (Depth-First Search). Este enfoque permite al agente retroceder ante caminos de razonamiento incorrectos y explorar alternativas, algo imposible en la generación lineal de CoT. En la práctica, ToT tiene un costo computacional significativamente mayor que CoT —puede requerir 5-20 llamadas al LLM por decisión— pero produce mejoras notables en puzzles, planificación y problemas matemáticos donde los errores de un paso temprano invalidan todos los pasos posteriores.

## Aspectos técnicos

- **Generación de pensamientos candidatos**: en cada nodo del árbol, el LLM genera k pensamientos alternativos (típicamente k=3-5) que representan diferentes formas de avanzar desde el estado actual
- **Evaluador de nodos**: función que asigna un score a cada pensamiento candidato; puede ser el propio LLM (usando un prompt de evaluación separado), una función heurística programática o una red de valor entrenada
- **Estrategia de búsqueda BFS**: expande todos los nodos del nivel actual antes de avanzar; garantiza encontrar la solución óptima si existe pero requiere mantener múltiples ramas activas simultáneamente en memoria
- **Estrategia de búsqueda DFS con backtracking**: sigue un camino hasta el fallo y retrocede; más eficiente en memoria pero puede atascarse en mínimos locales sin un límite de profundidad adecuado
- **Aplicabilidad en agentes**: ToT es más adecuado para la fase de planificación inicial de una tarea compleja que para el bucle de ejecución paso a paso; usar ToT en cada iteración agéntica es prohibitivo en costo y latencia

## Principio rector

Tree of Thoughts intercambia latencia y costo por calidad de razonamiento: es la técnica correcta para tareas donde un error de planificación temprano es más costoso que el tiempo adicional de exploración.
