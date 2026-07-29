# Módulo 5 – Capítulo 03 – Sección 05

## Comparación y decisión: LangChain, LlamaIndex, DSPy o implementación directa

Elegir entre LangChain, LlamaIndex, DSPy o llamadas directas al SDK del proveedor no es una decisión de preferencia personal ni de popularidad relativa en GitHub: es una decisión de ingeniería basada en el análisis objetivo de los requisitos del caso de uso, la complejidad del flujo, el perfil del equipo, y el costo de mantenimiento de la abstracción a lo largo del ciclo de vida del sistema. El error más frecuente es adoptar prematuramente el framework más popular sin evaluar si las abstracciones que ofrece resuelven los problemas específicos del proyecto, resultando en código que usa el 5% de las capacidades del framework mientras carga con el 100% de sus dependencias y complejidad.

La implementación directa con el SDK puro del proveedor es el punto de referencia contra el cual medir cualquier framework. Para flujos simples —una llamada al LLM por request, respuesta devuelta sin transformación compleja—, el SDK directo es la solución más controlable, predecible y debuggeable: el stack de llamadas completo está en código propio, los errores tienen trazas directas sin indirecciones de framework, y cualquier desarrollador Python puede leer y modificar el código sin conocer abstracciones específicas. El criterio cuantitativo es claro: si el flujo completo cabe en menos de 100 líneas limpias con el SDK puro, incluyendo el manejo de errores y el logging, la implementación directa es preferible.

LangChain es la opción cuando la complejidad del flujo supera ese umbral y el problema dominante es la orquestación: múltiples herramientas que el agente puede invocar, composición de llamadas al LLM con recuperación de datos y transformaciones intermedias, o flujos con ramificación condicional basada en el resultado de pasos anteriores. LangGraph, como extensión de LangChain, es específicamente la herramienta correcta cuando el flujo necesita ciclos —un agente que llama al LLM, evalúa si la respuesta es suficiente, y vuelve a llamar con información adicional— o cuando el estado debe persistir entre sesiones del usuario. La fortaleza de LangChain reside en su ecosistema: 200+ integraciones disponibles, documentación extensa y LangSmith para observabilidad nativa.

LlamaIndex es la opción dominante cuando el problema central es la gestión de datos: múltiples fuentes heterogéneas (PDFs, bases de datos, APIs), chunking semánticamente correcto, y pipelines de recuperación avanzados como `RouterQueryEngine` o `SubQuestionQueryEngine`. Su ecosistema de 150+ conectores de datos elimina semanas de trabajo de integración que la implementación directa requeriría. Para sistemas RAG sobre más de 10.000 documentos con múltiples fuentes, LlamaIndex ahorra un mes de desarrollo de la capa de ingesta, indexación y recuperación.

DSPy es la opción cuando el prompt ideal no puede determinarse por ingeniería manual y la tarea tiene un dataset de entrenamiento suficiente con una función de evaluación bien definida. La condición práctica para adoptar DSPy es que el equipo tenga disponibles más de 50 ejemplos de entrenamiento anotados y una función de evaluación que correlacione con la calidad real —exactamente los activos que el sistema de evaluación del capítulo 7 produce. DSPy no reemplaza a LangChain ni a LlamaIndex en la capa de orquestación; puede combinarse con ambos, usando DSPy para optimizar los prompts de módulos dentro de una cadena LangChain o de un query engine de LlamaIndex.

## Tabla de decisión por criterio

La siguiente tabla cruza los factores más determinantes con la recomendación de cada alternativa:

| Criterio | Implementación directa | LangChain / LangGraph | LlamaIndex | DSPy |
|---|---|---|---|---|
| Pasos en el pipeline | 1-2 pasos | 3+ con ramificación o ciclos | Recuperación + síntesis | Cualquier flujo con evaluación |
| Fuentes de datos | Una fuente simple | No determinante | Múltiples fuentes | No determinante |
| Agentes con estado | No aplica | LangGraph | No aplica | No aplica |
| Prompt óptimo conocido | Sí | Sí | Sí | No |
| Dataset de entrenamiento | No necesario | No necesario | No necesario | Necesario (>50 ejemplos) |
| Debuggabilidad | Máxima | Media (mejorada con LangSmith) | Media | Baja durante optimización |
| Overhead de dependencias | Mínimo | Alto (100-200 deps transitivas) | Alto | Medio |

## Señales de que un framework no está justificado

- **Flujo de un solo paso:** una sola llamada al LLM por request sin ramificación ni composición hace que cualquier framework sea overhead puro.
- **Equipo pequeño sin experiencia previa:** en equipos de 1-2 personas el costo de aprendizaje del framework puede superar su beneficio durante los primeros tres a seis meses del proyecto.
- **Alta necesidad de debuggabilidad:** cuando los bugs son costosos de reproducir, tener el stack completo en código propio es la ventaja más valiosa frente a cualquier framework.
- **Flujo estable y bien entendido:** si el flujo no cambiará significativamente en los próximos seis a doce meses, la implementación directa bien estructurada es más mantenible que una cadena de componentes de terceros.

El criterio de decisión más práctico en la industria es el "test de la implementación directa": antes de adoptar un framework, intentar implementar el flujo con el SDK puro y estimar cuántas líneas requiere. Si el resultado es manejable, la implementación directa es preferible. Si la complejidad que emerge —manejo del historial, múltiples fuentes de datos, ciclos de agente— genera código difícil de mantener, el framework está justificado.

---

**Idea central:** La decisión de adoptar un framework debe evaluarse con la misma rigurosidad que cualquier dependencia de terceros: ¿qué problema específico resuelve que no se puede resolver en menos código propio? La respuesta honesta a esa pregunta determina si el framework aporta o añade complejidad accidental.
