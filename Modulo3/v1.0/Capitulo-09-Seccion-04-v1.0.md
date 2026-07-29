# Capítulo 09 — Arquitecturas Multiagente

## Sección 04 — Patrones de colaboración entre agentes

La especialización de cada agente responde a la pregunta de qué hace cada unidad del sistema. La topología responde a la pregunta de cómo se relacionan entre sí. Estas dos preguntas son independientes: se pueden tener agentes perfectamente especializados organizados en una topología inadecuada para el problema, y el sistema fallará por la desconexión entre diseño de unidades y diseño de sistema.

Hay cuatro topologías fundamentales en los sistemas multiagente. No son mutuamente excluyentes —los sistemas reales con frecuencia combinan varias— pero cada una tiene una lógica propia y un conjunto de casos de uso donde es la elección natural.

### Topología jerárquica

En la topología jerárquica existe un agente en el nivel superior —el orquestador— que tiene autoridad sobre todos los demás. El orquestador recibe la tarea del sistema, la descompone en subtareas, asigna cada subtarea al agente especializado correspondiente, recibe los resultados y produce la síntesis final. Los agentes del nivel inferior no se comunican entre sí directamente: toda comunicación pasa por el orquestador.

Esta topología es la arquitectura de referencia para sistemas multiagente empresariales porque tiene propiedades que facilitan su operación: la responsabilidad está centralizada (el orquestador es el único punto de coordinación), el flujo de datos es predecible (todo pasa por el orquestador), y el debug es relativamente directo (se puede examinar qué recibió y qué envió el orquestador en cada paso).

Sus compromisos son igualmente claros: el orquestador es un cuello de botella potencial. Si el orquestador falla, el sistema completo falla. Si el orquestador toma decisiones de descomposición incorrectas, los agentes especializados las ejecutan perfectamente pero producen el resultado incorrecto. La calidad del orquestador determina la calidad del sistema.

**Casos de uso óptimos:** sistemas con tareas bien estructurables en subtareas, donde la coordinación centralizada es una ventaja de control más que una limitación de rendimiento. Procesamiento de documentos, generación de informes complejos, pipelines de análisis multidimensional.

### Topología en pipeline

En el pipeline, los agentes se organizan en secuencia lineal. El agente A procesa el input inicial y produce un output que el agente B consume como input, produciendo a su vez un output que el agente C consume, y así sucesivamente. No hay un orquestador central: la coordinación está implícita en la secuencia y en los contratos de input/output entre agentes consecutivos.

El pipeline es la topología más simple de implementar y razonar sobre ella. Cuando la tarea tiene una estructura naturalmente secuencial —donde la fase B genuinamente no puede comenzar hasta que la fase A termine— el pipeline no es solo simple sino correcto. Intentar paralelizar un proceso inherentemente secuencial solo añade complejidad sin reducir la latencia total.

Sus limitaciones son simétricas a su simpleza: no hay paralelismo posible dentro de la topología pura. Si el agente C falla, el pipeline completo se detiene. Y si el error fue introducido en el agente A, el agente B lo amplifica y el agente C lo amplifica aún más: los errores se propagan hacia adelante sin oportunidad de corrección.

**Casos de uso óptimos:** transformaciones secuenciales donde cada etapa agrega valor sobre el output de la anterior sin posibilidad de paralelismo. Extracción → normalización → análisis → reporte. Transcripción → traducción → resumen → indexación.

### Topología entre pares (peer-to-peer)

En la topología entre pares, los agentes pueden comunicarse directamente entre sí sin un coordinador central. Cada agente conoce la existencia de otros agentes y puede iniciar comunicación con cualquiera de ellos cuando lo necesita. La coordinación emerge de la interacción descentralizada más que de una autoridad central.

Esta topología tiene capacidades que las anteriores no pueden replicar: permite que un agente solicite ayuda a otro sin que el orquestador deba anticipar esa necesidad. Un agente analista que descubre que necesita información adicional puede solicitarla directamente al agente investigador, sin esperar que el orquestador detecte esa necesidad y la gestione. Esto produce sistemas más adaptativos y capaces de manejar casos que no fueron completamente anticipados en el diseño.

El costo es la complejidad: los sistemas entre pares son notablemente más difíciles de depurar, de razonar sobre su comportamiento y de garantizar su terminación. Pueden surgir ciclos de comunicación, deadlocks donde dos agentes esperan mutuamente una respuesta y estados del sistema difíciles de predecir. La trazabilidad de quién le dijo qué a quién y en qué orden requiere instrumentación cuidadosa.

**Casos de uso óptimos:** sistemas de investigación abierta donde los agentes necesitan consultar a otros en función de lo que descubren, sistemas de deliberación colaborativa y cualquier caso donde la rigidez de un orquestador central impide la adaptación necesaria.

### Topología basada en mercado

En la topología de mercado, los agentes compiten o cooperan por recursos: tareas, datos o capacidad de procesamiento. Un agente "publicador" anuncia que tiene una tarea disponible. Los agentes "suscriptores" que tienen la capacidad apropiada postulan para ejecutarla. El sistema asigna la tarea al agente más disponible o más calificado según algún criterio de selección.

Esta topología es la más compleja pero también la más escalable. Es el modelo correcto cuando el volumen de trabajo es variable e impredecible, cuando hay múltiples instancias de agentes del mismo tipo que pueden ejecutar la misma clase de tarea, y cuando se quiere distribuir la carga dinámicamente en función de la disponibilidad real del sistema.

Es también la más difícil de implementar correctamente: requiere un mecanismo de descubrimiento de agentes, un protocolo de postulación, un mecanismo de asignación y un sistema de confirmación y reporte de resultados. Para la mayoría de sistemas empresariales de tamaño mediano, esta complejidad no está justificada.

**Casos de uso óptimos:** sistemas de alta escala con trabajo altamente variable, múltiples instancias de agentes especializados y necesidad de distribución dinámica de carga.

### Patrones híbridos: la práctica real

Los sistemas reales rara vez implementan una topología pura. La combinación más común es una topología jerárquica que incorpora elementos de pipeline en el nivel de los agentes ejecutores: el orquestador coordina en el nivel superior, y los agentes especializados ejecutan flujos secuenciales internamente.

Otra combinación frecuente es la topología jerárquica con un sub-grafo de pares: el orquestador coordina los macro-pasos del sistema, pero dentro de un micro-sistema de análisis colaborativo, un conjunto de agentes especializados se consulta mutuamente para producir un análisis más completo.

El criterio para combinar topologías es el mismo que para elegir entre ellas: cada nivel del sistema debe tener la topología que mejor responde a su naturaleza. La coordinación de alto nivel tiende a beneficiarse de la jerarquía; la ejecución de tareas específicas puede beneficiarse del pipeline; los sistemas de exploración o deliberación se benefician de la topología entre pares.

### Documentar la topología antes de implementarla

Una práctica indispensable antes de comenzar la implementación de cualquier sistema multiagente es dibujar el diagrama de la topología con el nivel de detalle que incluya: cada agente con su rol, las direcciones de comunicación entre ellos, y los formatos de los mensajes que transitan cada conexión. Este diagrama no es documentación posterior a la implementación: es el artefacto de diseño previo a la primera línea de código.

El diagrama de topología cumple dos funciones. La primera es la verificación de coherencia: si el diagrama muestra que el agente A necesita información que produce el agente C pero C es posterior a A en el pipeline, hay un error de diseño que el diagrama hace visible antes de que sea un error de código. La segunda función es la comunicación: un equipo que trabaja sobre el mismo sistema necesita un modelo compartido de cómo funciona, y ese modelo es el diagrama.

---

*Con los agentes diseñados y la topología elegida, la siguiente pregunta es mecánica pero crucial: ¿cómo se comunican concretamente los agentes entre sí? La sección 05 desarrolla los protocolos y mecanismos de comunicación que hacen que la topología funcione en la práctica.*
