# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 05: Monitoreo de agentes y flujos

El monitoreo de una llamada individual al modelo es relativamente directo: hay una entrada, una salida, una latencia medible y un costo calculable. El monitoreo de un sistema agentivo es cualitativamente más complejo porque el agente no produce una respuesta en un solo paso. Produce un flujo de acciones —planificación, ejecución de herramientas, observación de resultados, replaneación— que puede tener decenas de pasos, durar minutos, y fallar de maneras que ningún paso individual indica de forma aislada.

Esta sección describe cómo extender la observabilidad a los sistemas agentivos: qué métricas adicionales se necesitan, cómo detectar los modos de falla específicos de los agentes y cómo visualizar flujos de múltiples etapas de manera que el equipo de operaciones pueda entender qué está ocurriendo.

### Los modos de falla específicos de los agentes

Un agente bien implementado tiene mecanismos para hacer las preguntas correctas, usar las herramientas disponibles y llegar a una respuesta útil. Pero tiene también modos de falla que no aparecen en sistemas de inferencia directa.

**El bucle infinito.** El agente entra en un ciclo donde repite las mismas acciones sin progresar hacia una respuesta. Puede ocurrir cuando el agente interpreta los resultados de una herramienta como evidencia de que debe ejecutar la misma herramienta nuevamente, o cuando el criterio de terminación del ciclo agentivo no está bien definido. Sin monitoreo, un bucle infinito consume tokens y costo de forma indefinida hasta que el sistema alcanza un timeout externo o agota el presupuesto.

**La explosión de herramientas.** El agente llama a muchas más herramientas de las necesarias para responder la consulta. En lugar de responder una pregunta con dos o tres herramientas relevantes, llama a diez o quince herramientas en búsqueda de certeza adicional. Esto aumenta la latencia, el costo y a veces produce respuestas peores porque el contexto acumulado de múltiples herramientas es más difícil de sintetizar que el de pocas herramientas precisas.

**El abandono prematuro.** El agente decide que no puede responder la consulta y se detiene antes de haber explorado las herramientas que habrían permitido una respuesta correcta. Puede ocurrir cuando el primer intento de recuperación no produce resultados relevantes y el agente interpreta eso como una señal de que el sistema no tiene la información, cuando en realidad una estrategia de búsqueda diferente habría encontrado la información.

**La propagación de errores.** Una herramienta del pipeline produce un resultado incorrecto o ambiguo, y el agente lo incorpora en su razonamiento sin cuestionar su validez. Los pasos posteriores se construyen sobre una base incorrecta, produciendo una respuesta final que es incorrecta de forma no obvia —el razonamiento parece coherente pero parte de una premisa falsa—.

**La divergencia de objetivos.** El agente pierde de vista el objetivo original de la consulta a medida que avanza en el proceso de razonamiento. Las herramientas que ejecuta en los pasos finales responden una pregunta diferente a la que se hizo al inicio. Esto ocurre con mayor frecuencia en agentes con muchos pasos de razonamiento donde el contexto de la consulta original se diluye.

### Métricas específicas para sistemas agentivos

Además de las métricas operacionales estándar, los sistemas agentivos requieren métricas adicionales que capturan la dinámica de los flujos multi-etapa.

**Número de pasos por solicitud.** Cuántas iteraciones del ciclo agentivo (planificación → acción → observación) se ejecutaron para resolver la consulta. Una distribución estable con un máximo razonable indica un agente bien controlado. Una distribución con cola larga o con solicitudes que alcanzan el máximo configurado indica que el agente está entrando en bucles o tomando caminos demasiado indirectos.

**Número de herramientas llamadas por solicitud.** Cuántas herramientas distintas ejecutó el agente, y cuántas veces llamó a la misma herramienta. Si el agente llama a la misma herramienta con parámetros similares tres veces seguidas, es señal de un bucle o de un criterio de terminación mal definido.

**Tasa de éxito por herramienta.** El porcentaje de llamadas a cada herramienta que producen un resultado útil (no un error, no un resultado vacío). Una herramienta con alta tasa de fallos es un punto de fragilidad del sistema que debe ser reforzado o reemplazado.

**Latencia por etapa del pipeline.** Cuánto tiempo consume cada etapa: planificación inicial, cada llamada a herramienta, cada paso de razonamiento, síntesis de la respuesta final. Esta descomposición permite identificar dónde están los cuellos de botella: si el 80% de la latencia está en una herramienta específica, ese es el lugar donde optimizar.

**Costo acumulado por flujo.** El costo total de un flujo agentivo completo, que puede ser significativamente mayor que el costo de una llamada individual. En sistemas con costos por token, un agente que da diez pasos tiene un costo de inferencia diez veces mayor que uno que da un paso. Si el costo promedio por solicitud de un agente está creciendo, significa que los flujos se están volviendo más complejos con el tiempo —lo que puede ser esperado o puede ser una degradación que requiere investigación—.

**Tasa de terminación exitosa.** El porcentaje de flujos agentivos que terminan con una respuesta (éxito) versus los que terminan por timeout, por error técnico, o porque el agente declaró que no podía responder. Una tasa de terminación exitosa que cae indica que el agente está encontrando más situaciones en las que no puede operar, lo que puede señalar cambios en el tipo de consultas que recibe o deterioro en las herramientas disponibles.

### Visualización de flujos agentivos

El formato de log plano no es adecuado para sistemas agentivos. Una secuencia lineal de eventos no comunica la estructura de árbol del razonamiento. El formato correcto es el árbol de spans descrito en la sección anterior, con la adición de visualizaciones que muestren el flujo como un grafo de decisiones.

```
FLUJO AGENTIVO — Solicitud de análisis de inventario (ID: agent-3d7f)

[PLANIFICACIÓN INICIAL]
  Objetivo: "¿Qué productos del catálogo tienen stock bajo para la campaña de verano?"
  Plan inicial: 1) consultar inventario → 2) filtrar productos de temporada → 3) comparar con predicción de demanda

[PASO 1] → tool: query_inventory_db
  Parámetros: {categoria: "verano", umbral_stock: null}
  Resultado: 847 productos devueltos
  Latencia: 420ms
  Decisión: demasiados resultados, refinar búsqueda

[PASO 2] → tool: query_inventory_db (segunda llamada)
  Parámetros: {categoria: "verano", umbral_stock: 50}
  Resultado: 23 productos con stock <= 50 unidades
  Latencia: 380ms
  Decisión: obtener predicción de demanda para estos 23 productos

[PASO 3] → tool: get_demand_forecast
  Parámetros: {product_ids: [23 IDs], periodo: "verano-2026"}
  Resultado: predicción por producto con intervalos de confianza
  Latencia: 1,240ms
  Decisión: suficiente información, sintetizar respuesta

[SÍNTESIS FINAL]
  Duración total: 2,980ms
  Pasos ejecutados: 3
  Herramientas usadas: 2 (query_inventory_db × 2, get_demand_forecast × 1)
  Tokens totales: 8,450
  Resultado: respuesta con 8 productos en riesgo de desabastecimiento
```

Esta representación permite que el equipo de operaciones vea de un vistazo si el flujo fue directo o estuvo exploración innecesaria, cuánto tiempo tardó cada herramienta y cuál fue la secuencia de decisiones del agente.

### Detección de bucles y comportamientos anómalos

Para detectar bucles y comportamientos anómalos en tiempo real, el sistema de monitoreo debe implementar alertas específicas:

**Alerta de pasos excesivos.** Si un flujo agentivo supera un umbral configurado de pasos —por ejemplo, 15 pasos en un agente diseñado para operar en 3-7— la alerta se dispara automáticamente. La solicitud puede continuar mientras se investiga, o puede interrumpirse si el costo proyectado es inaceptable.

**Alerta de herramienta repetida.** Si el agente llama a la misma herramienta con los mismos parámetros más de una vez en el mismo flujo, es señal de un bucle potencial. El sistema puede alertar al equipo y opcionalmente interrumpir el flujo.

**Alerta de costo proyectado.** Si el costo acumulado de un flujo supera el percentil 95 del costo histórico de solicitudes similares, la alerta indica que este flujo es anómalamente costoso y merece inspección.

**Detección de ciclos en el grafo de decisiones.** Un análisis automático del árbol de spans puede detectar si el agente visitó el mismo estado (herramienta + parámetros similares) más de una vez, lo que es evidencia de un ciclo en la lógica de planificación.

### Monitoreo de sistemas multi-agente

Los sistemas de múltiples agentes coordinados —donde un agente orquestador delega tareas a agentes especializados— presentan un nivel adicional de complejidad. Cada agente tiene su propio ciclo de vida y su propia traza, pero las trazas deben vincularse para poder entender el flujo completo de una solicitud.

El mecanismo correcto es propagar el identificador de traza desde el orquestador a cada subagente. Cuando el subagente genera su traza, la registra como hija de la traza del orquestador. El resultado es un árbol de trazas anidadas que muestra el flujo completo del sistema, desde la solicitud del usuario hasta la respuesta final, pasando por todas las delegaciones y subagentes involucrados.

Sin esta propagación de identificadores, las trazas de los subagentes quedan huérfanas: existen como registros independientes, pero no pueden vincularse con la solicitud que los originó.

### Nota del arquitecto

El monitoreo de sistemas agentivos requiere herramientas diseñadas para ese propósito. Las herramientas de monitoreo de software tradicional pueden capturar las métricas operacionales, pero no pueden visualizar árboles de razonamiento, detectar bucles en flujos agentivos o mostrar la secuencia de herramientas ejecutadas de manera comprensible. Plataformas especializadas como Langfuse, LangSmith, Phoenix y Weights & Biases ofrecen visualizaciones adaptadas a sistemas de IA. La elección de plataforma es secundaria al principio: el sistema debe instrumentarse para producir los datos que esas plataformas necesitan —identificadores de traza, spans jerárquicos, atributos de contexto—. Una vez que el sistema produce esos datos, migrar de plataforma es relativamente sencillo. Un sistema que no los produce no puede beneficiarse de ninguna plataforma.

La siguiente sección examina cómo usar los datos de observabilidad para optimizar las arquitecturas de contexto en producción: el ciclo de experimentación que permite mejorar el sistema basándose en evidencia de uso real.
