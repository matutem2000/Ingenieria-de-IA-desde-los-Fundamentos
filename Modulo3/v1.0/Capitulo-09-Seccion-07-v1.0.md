# Capítulo 09 — Arquitecturas Multiagente

## Sección 07 — Memoria compartida y contexto distribuido

Cuando un sistema multiagente trabaja en una tarea común, los agentes necesitan compartir información. El agente investigador necesita que el agente analista vea los documentos que recuperó. El agente analista necesita que el agente redactor vea las conclusiones que produjo. El agente supervisor necesita ver el output del agente que supervisa. Sin un mecanismo de compartición de información, los agentes trabajan en silos y el sistema no puede funcionar.

El mecanismo natural para resolver este problema es el estado compartido: un almacén de información al que todos los agentes pueden leer y escribir. Pero el estado compartido introduce uno de los problemas de ingeniería más clásicos de los sistemas distribuidos: ¿qué ocurre cuando dos agentes intentan modificar el mismo dato al mismo tiempo? ¿Cómo sabe un agente que la información que está leyendo sigue siendo válida y no fue modificada por otro agente después de que la leyó?

Estos no son problemas teóricos. En un sistema multiagente que opera en paralelo, son situaciones que ocurren regularmente. El diseño del mecanismo de memoria compartida determina si esas situaciones producen errores silenciosos, errores detectables o comportamiento correcto.

### El problema de la concurrencia en el estado compartido

Considera un sistema multiagente que mantiene un objeto de estado con el contexto acumulado de la tarea. El estado incluye, entre otras cosas, una lista de conclusiones a las que los agentes han llegado durante el proceso.

El agente A lee la lista de conclusiones (tiene cuatro elementos), añade su conclusión y escribe la lista de vuelta al estado (ahora tiene cinco elementos). Simultáneamente, el agente B leyó la misma lista cuando tenía cuatro elementos (antes de que A la modificara), añadió su conclusión y escribió la lista de vuelta. El resultado es que la lista tiene cinco elementos: las cuatro originales más la de B, pero la conclusión de A se perdió porque B sobreescribió con la versión que leyó antes de la modificación de A.

Esto es una condición de carrera clásica. En sistemas de software tradicionales se resuelve con bloqueos (locks): antes de modificar un dato compartido, el proceso adquiere un bloqueo exclusivo sobre ese dato y lo libera cuando termina. Otros procesos que quieren modificar el mismo dato deben esperar a que el bloqueo sea liberado.

Los bloqueos funcionan pero tienen costos: en un sistema multiagente donde los agentes pueden tardar segundos o decenas de segundos en completar una tarea, un bloqueo mantenido durante toda la ejecución de un agente puede bloquear a otros agentes por períodos inaceptablemente largos.

### Tres estrategias de memoria compartida

**Estrategia 1: Almacén de estado centralizado con escrituras atómicas**

El almacén de estado centralizado serializa todas las escrituras. Cuando un agente quiere escribir al estado, su escritura se ejecuta de forma atómica: se aplica completamente o no se aplica. Si dos escrituras llegan simultáneamente, se ejecutan en serie, una después de la otra, sin posibilidad de solapamiento parcial.

Esta estrategia elimina las condiciones de carrera pero introduce un cuello de botella: el almacén de estado centralizado procesa las escrituras en serie. En sistemas con pocos agentes y escrituras infrecuentes, esto no es un problema. En sistemas con muchos agentes y alto volumen de escrituras, puede convertirse en el limitante de rendimiento del sistema.

**Estrategia 2: Estado versionado con control optimista**

Cada objeto en el estado tiene un número de versión. Cuando un agente quiere modificar un objeto, lee el objeto y toma nota de su versión actual. Produce su modificación. Cuando intenta escribir, el sistema verifica que la versión del objeto no cambió desde que el agente lo leyó. Si la versión es la misma, la escritura se acepta y la versión se incrementa. Si la versión cambió (otro agente modificó el objeto en el intervalo), la escritura se rechaza y el agente debe leer la versión actualizada y reintentar.

Este mecanismo de control de concurrencia optimista es el modelo correcto cuando los conflictos son poco frecuentes. Cuando son frecuentes —cuando muchos agentes intentan modificar el mismo objeto al mismo tiempo— el costo de los reintentos puede ser mayor que el de los bloqueos. La elección depende del patrón de acceso específico del sistema.

**Estrategia 3: Estado distribuido mediante paso de mensajes**

En lugar de un almacén centralizado, cada agente mantiene su propio estado local. La sincronización entre agentes ocurre mediante mensajes: cuando un agente produce información relevante para otros agentes, la publica como un mensaje. Los agentes que necesitan esa información la reciben y actualizan su estado local.

Este modelo elimina el problema de concurrencia sobre un estado centralizado porque no hay estado centralizado. Cada agente tiene su propia copia de la información que necesita. El costo es la consistencia eventual: en el momento en que un agente publica una actualización, otros agentes pueden no haberla recibido todavía. Hay un período durante el cual diferentes agentes tienen visiones distintas del estado del sistema. Para sistemas donde la consistencia inmediata es crítica, este modelo no es apropiado. Para sistemas donde cada agente trabaja principalmente con su propio contexto y solo necesita sincronización periódica, el modelo es muy eficiente.

### Qué guardar en la memoria compartida

No toda la información que un agente produce debe ir al estado compartido. Parte de la información es interna al agente y no necesita ser visible para otros. Parte es relevante solo para el próximo agente en la cadena. Parte es relevante para todo el sistema durante toda la duración de la tarea.

Un criterio útil para decidir qué va al estado compartido:

**Compartido y persistente:** información que múltiples agentes necesitan consultar, y que debe estar disponible durante toda la duración de la tarea. El resultado de investigaciones, conclusiones validadas por el supervisor, el estado de progreso del plan. Esta información va al estado compartido.

**Compartido y efímero:** información que un agente necesita transferir a otro agente específico, pero que no es relevante para el sistema en general. Este tipo de información se transmite mejor como un mensaje directo entre agentes que como estado compartido.

**Local y efímero:** el razonamiento interno del agente durante la ejecución de su tarea, los resultados intermedios que descarta, los intentos fallidos antes del output final. Esta información no debe ir al estado compartido. Incluirla añade ruido y costo sin valor.

### El contexto que cada agente recibe

Una pregunta práctica frecuente es: cuando un agente comienza a trabajar en su subtarea, ¿qué información del estado compartido debe recibir?

La respuesta correcta no es "todo el estado": un agente que recibe todo el contexto acumulado del sistema puede estar procesando información irrelevante para su subtarea específica, lo que añade costo de tokens y puede distraer su razonamiento. La respuesta correcta es: el agente recibe el contexto mínimo necesario para ejecutar su subtarea más los resultados de las subtareas de las cuales la suya depende.

El orquestador o planificador que asigna la subtarea al agente es responsable de construir este contexto mínimo necesario. No delega al agente la responsabilidad de decidir qué del estado global necesita: lo construye explícitamente como parte del mensaje de tarea que le envía al agente.

### Privacidad y aislamiento en la memoria compartida

En sistemas multiagente empresariales, el estado compartido puede contener información sensible. Una arquitectura que permite que cualquier agente lea cualquier parte del estado es un riesgo de privacidad: un agente comprometido, o un agente con un error de razonamiento que lo lleva a incluir información inapropiada en su output, puede exponer información a la que no debería tener acceso.

El principio de mínimo privilegio aplica también al acceso al estado: cada agente debe tener acceso de lectura solo a las partes del estado que su función requiere, y acceso de escritura solo a las partes del estado que su función produce. El control de acceso al estado compartido no es una funcionalidad opcional en producción: es una condición necesaria para que el sistema sea seguro.

---

*La sección 08 amplía la perspectiva desde el estado interno del sistema hacia sus propiedades operacionales: cómo se escala cuando la demanda crece, y cómo se comporta cuando uno o más agentes fallan. La tolerancia a fallos en sistemas multiagente no es un tema de mantenimiento: es un tema de diseño que debe resolverse antes de la primera línea de código de producción.*
