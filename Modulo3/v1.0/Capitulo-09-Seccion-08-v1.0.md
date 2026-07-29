# Capítulo 09 — Arquitecturas Multiagente

## Sección 08 — Escalabilidad y tolerancia a fallos

Un sistema multiagente que funciona perfectamente en un entorno de desarrollo controlado y falla en producción bajo carga real no es un sistema terminado. Es un prototipo. La diferencia entre ambos no está en la lógica del negocio ni en la calidad del razonamiento de los agentes: está en la ingeniería de las propiedades operacionales del sistema. La escalabilidad define qué ocurre cuando la demanda crece. La tolerancia a fallos define qué ocurre cuando algo sale mal.

Ambas propiedades deben diseñarse antes de la primera línea de código de producción. Añadirlas como correcciones posteriores a un sistema ya en producción es costoso, lento y frecuentemente incompleto.

### Escalabilidad horizontal de agentes

La forma natural de escalar un sistema multiagente es la escalabilidad horizontal: añadir más instancias de los agentes que constituyen el cuello de botella. Si el sistema procesa cien solicitudes por hora y el agente analista tarda treinta segundos por solicitud, ese agente es el limitante. Añadir una segunda instancia del agente analista duplica la capacidad de ese paso sin modificar ninguna otra parte del sistema.

Esta escalabilidad horizontal funciona cuando los agentes son stateless: cuando su comportamiento depende únicamente del mensaje que recibieron, no de ningún estado interno acumulado de interacciones anteriores. Un agente stateless puede escalar a cualquier número de instancias porque todas las instancias son equivalentes entre sí.

Cuando los agentes tienen estado interno —cuando una instancia del agente analista necesita recordar el contexto de solicitudes anteriores para funcionar correctamente—, la escalabilidad horizontal se complica. Las solicitudes relacionadas deben dirigirse a la misma instancia del agente (afinidad de sesión), lo que limita la flexibilidad de la distribución de carga.

El principio de diseño que emerge: diseña los agentes como stateless siempre que sea posible. Si el agente necesita estado, externaliza ese estado al almacén compartido que la sección 07 describió. La instancia del agente lee el estado del almacén al inicio de cada tarea y escribe sus resultados al almacén al finalizar. El agente en sí mismo no guarda nada entre tareas.

### Costo y latencia del paralelismo

El paralelismo de agentes no es gratis. Cada agente en ejecución simultánea consume tokens de input y output en paralelo. Un sistema que ejecuta diez agentes en paralelo puede consumir diez veces el costo de tokens de un agente único ejecutando en serie, incluso si la latencia total es menor.

Esta relación entre paralelismo, costo y latencia tiene implicaciones concretas para el diseño:

**El paralelismo reduce la latencia pero aumenta el costo.** Cuando la latencia es la variable crítica —el usuario está esperando una respuesta en tiempo real—, el paralelismo es la herramienta correcta. Cuando el costo es la variable crítica —el sistema procesa miles de solicitudes por hora en un presupuesto definido—, el paralelismo excesivo puede no estar justificado.

**El grado óptimo de paralelismo depende del problema.** No todas las subtareas de un sistema se benefician de la misma cantidad de paralelismo. Las subtareas largas y costosas son las mejores candidatas para el paralelismo. Las subtareas cortas pueden no justificar el overhead de coordinación.

**El costo de los agentes de coordinación se suma.** El orquestador, el planificador y el supervisor también consumen tokens. En un sistema con muchos niveles de coordinación, el costo de los agentes de coordinación puede ser una fracción significativa del costo total. Este costo debe estar en el modelo de costo del sistema desde el diseño.

### Modos de fallo en sistemas multiagente

Los fallos en sistemas multiagente pueden clasificarse en cuatro categorías según su naturaleza y sus implicaciones:

**Fallo de un agente ejecutor.** El agente que debía completar una subtarea no puede hacerlo: el servicio de IA no está disponible, el timeout se agotó, el agente produjo un error irrecuperable. Este es el fallo más común y el que el sistema debe manejar con más frecuencia.

**Fallo del orquestador o planificador.** El agente de coordinación del sistema falla. Este es el fallo más severo en una topología jerárquica: sin el orquestador, el sistema no puede coordinar trabajo. En una topología entre pares, el fallo de un agente individual tiene un impacto más localizado.

**Fallo silencioso.** El agente completa la tarea sin errores técnicos pero produce un output incorrecto o de baja calidad que el sistema acepta como válido. Este tipo de fallo es el más peligroso porque no genera alertas: el sistema funciona correctamente desde el punto de vista técnico, pero el resultado entregado al usuario es incorrecto. El supervisor de la sección 06 es la defensa principal contra este tipo de fallo.

**Fallo de la memoria compartida.** El almacén de estado no está disponible o devuelve datos corruptos. Los agentes que dependen de ese estado no pueden completar su trabajo. Este fallo es transversal a todo el sistema: no afecta a un agente sino a todos.

### Estrategias de resiliencia

**Reintentos con backoff exponencial.** Cuando un agente ejecutor falla en una subtarea, el sistema reintenta la subtarea después de un intervalo de espera. Si el segundo intento también falla, el intervalo se duplica antes del siguiente reintento. Este patrón da tiempo al sistema de IA subyacente para recuperarse de condiciones transitorias sin generar una cascada de solicitudes que puede empeorar el problema.

El límite de reintentos es un parámetro de diseño importante. Un límite demasiado bajo puede abandonar prematuramente una tarea que se habría recuperado. Un límite demasiado alto puede mantener bloqueado a un agente esperando la recuperación de un servicio que no va a recuperarse a tiempo.

**Agente de respaldo (fallback agent).** Para subtareas críticas, se puede designar un agente alternativo que recibe la tarea si el agente primario no puede completarla. El agente de respaldo puede ser una instancia del mismo tipo de agente en un entorno diferente, un agente con capacidades reducidas pero disponibilidad más alta, o un comportamiento degradado que produce un resultado parcial en lugar de ningún resultado.

**Circuit breaker.** Si un agente falla repetidamente dentro de un período definido, el sistema lo marca como no disponible y deja de enviarle solicitudes por un tiempo determinado. Este patrón evita que el sistema continúe enviando solicitudes a un componente que claramente no puede procesarlas, permitiendo que el componente se recupere sin estar inundado de solicitudes nuevas.

**Punto de verificación y recuperación (checkpoint and recovery).** En tareas de larga duración, el sistema guarda el estado del progreso en puntos intermedios. Si el sistema falla después del tercer paso de un plan de ocho, la recuperación puede retomar desde el tercer paso en lugar de reiniciar desde el primero. Esta estrategia es especialmente valiosa en sistemas donde el costo de reiniciar desde cero es alto, ya sea en tiempo, en tokens o en acceso a recursos externos que no son gratuitos.

### Observabilidad como condición de operación

Un sistema multiagente sin observabilidad es un sistema que no se puede operar. Cuando algo falla —o cuando algo funciona peor de lo esperado—, la capacidad de determinar qué falló, cuándo y por qué depende de la instrumentación del sistema.

La observabilidad mínima en un sistema multiagente incluye:

- Trazas de cada mensaje enviado y recibido entre agentes, con marcas temporales.
- Logs de cada subtarea: cuándo comenzó, qué input recibió, qué output produjo, cuánto tiempo tomó, si requirió reintentos.
- Métricas de costo por agente y por tarea, para detectar desviaciones respecto a los valores esperados.
- Alertas sobre fallos recurrentes de agentes específicos o sobre tasas de error que exceden umbrales predefinidos.

Sin esta instrumentación, un sistema en producción es una caja negra. Con ella, el comportamiento del sistema es visible y las anomalías son detectables antes de que se conviertan en problemas que los usuarios reportan.

---

*La sección 09 toma todo lo desarrollado en las secciones anteriores y lo organiza en el lenguaje de los patrones: qué configuraciones de diseño funcionan de forma consistente en sistemas multiagente reales, y qué configuraciones producen problemas igualmente consistentes. Conocer los patrones y los anti-patrones es lo que permite reconocerlos en un sistema propio.*
