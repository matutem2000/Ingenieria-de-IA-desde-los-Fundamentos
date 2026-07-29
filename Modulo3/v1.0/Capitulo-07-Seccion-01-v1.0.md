# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 01 — Introducción a las herramientas (Tools) en IA

Un modelo de lenguaje sin herramientas es un sistema que conoce el mundo hasta la fecha de su entrenamiento y que solo puede operar sobre texto. Sabe que una ciudad tiene clima cálido en verano, pero no puede consultar la temperatura actual. Puede describir cómo se registra un cliente en un CRM, pero no puede ejecutar esa acción. Puede razonar sobre el estado de un pedido, pero no puede leer la base de datos de la empresa.

Las herramientas rompen esa limitación. Una herramienta, en el contexto de los sistemas de IA que construimos en este libro, es cualquier función, API o servicio externo que el modelo puede invocar durante una interacción para obtener información dinámica o ejecutar una acción real. El modelo no ejecuta la herramienta por sí mismo — genera una solicitud de invocación estructurada, la aplicación que lo rodea ejecuta la herramienta, y el resultado vuelve al contexto del modelo para que continúe razonando.

Esta distinción es central: el modelo razona, la aplicación actúa.

### Qué es una herramienta en este capítulo

A lo largo de este capítulo usamos el término herramienta para referirnos a un mecanismo de integración que opera dentro del alcance de una interacción. El modelo recibe una solicitud del usuario, razona sobre qué información o acción necesita, solicita una o varias herramientas, recibe los resultados y produce una respuesta final. Todo ocurre en el marco de un único ciclo de conversación.

Lo que no cubrimos aquí son los ciclos de planificación multi-turno, en los que un agente ejecuta decenas o cientos de pasos a lo largo del tiempo antes de entregar un resultado. Ese territorio pertenece al capítulo 08 (Sistemas Multi-Agente) y al capítulo 10 (Planificación y Razonamiento). La distinción importa porque las decisiones de diseño — seguridad, control, manejo de errores — son diferentes según la autonomía que se le otorga al sistema.

### Por qué las herramientas cambian el diseño de los sistemas

Antes de que existiera el mecanismo de herramientas, los desarrolladores que querían dar acceso a datos externos a un modelo tenían que inyectar esa información directamente en el prompt. Si el usuario preguntaba por el estado de su pedido, el sistema consultaba la base de datos primero, construía un texto con el resultado y lo incluía en el prompt. El modelo respondía como si "supiera" la respuesta.

Ese patrón funciona para casos simples. Cuando la complejidad crece — cuando el modelo necesita consultar múltiples fuentes según el contenido de la pregunta, o cuando necesita ejecutar acciones cuyo alcance no se puede predecir de antemano — el patrón de inyección previa en el prompt se rompe.

Las herramientas permiten que el modelo decida en tiempo de ejecución qué información necesita y cuándo la necesita. Eso cambia el diseño de los sistemas porque el flujo de control ya no es enteramente lineal: la aplicación le cede al modelo la decisión de qué herramienta invocar, y el modelo puede invocar herramientas en secuencia o en paralelo según lo que va descubriendo.

### Tipos de herramientas

Las herramientas se clasifican de manera natural según sus efectos:

**Herramientas de consulta.** Recuperan información sin modificar el estado del sistema. Son idempotentes: llamarlas diez veces produce el mismo resultado. Ejemplos: consultar el precio de un producto, buscar un cliente por su identificador, obtener el historial de una transacción, leer el estado de un ticket de soporte.

**Herramientas de acción.** Modifican el estado del sistema. Tienen efectos secundarios que pueden ser irreversibles. Ejemplos: crear un registro, enviar un correo electrónico, procesar un pago, actualizar el estado de un pedido, eliminar un archivo.

Esta clasificación no es solo conceptual. Determina qué nivel de control necesita el sistema sobre la invocación: las herramientas de consulta pueden ejecutarse automáticamente con menos riesgos; las herramientas de acción, especialmente las irreversibles, requieren controles de autorización y en muchos casos confirmación explícita del usuario. La sección 07 desarrolla este punto con detalle.

### La posición del modelo frente a las herramientas

El modelo no sabe directamente cómo funciona una herramienta ni qué código ejecuta. Lo que recibe es una descripción en texto de qué hace la herramienta y qué parámetros espera. Con esa descripción, el modelo decide si la herramienta es relevante para responder la solicitud actual y, si lo es, genera los valores de los parámetros necesarios para invocarla.

Esta dependencia de la descripción tiene una consecuencia directa para el diseño: el texto que describe una herramienta es parte del contrato técnico del sistema, no documentación auxiliar. Si la descripción es ambigua, el modelo invocará la herramienta en situaciones incorrectas o pasará parámetros mal formados. La sección 05 desarrolla los principios de diseño de herramientas robustas.

### El ciclo fundamental

El ciclo de una interacción con herramientas tiene la siguiente estructura:

1. El usuario envía una solicitud.
2. El modelo recibe la solicitud junto con las descripciones de las herramientas disponibles.
3. El modelo razona y determina que necesita invocar una herramienta.
4. El modelo genera una solicitud de invocación estructurada con los parámetros correspondientes.
5. La aplicación intercepta esa solicitud y ejecuta la herramienta real.
6. El resultado de la herramienta se incorpora al contexto del modelo.
7. El modelo continúa razonando. Si necesita otra herramienta, repite los pasos 3 a 6.
8. Cuando el modelo tiene suficiente información, genera la respuesta final al usuario.

Este ciclo puede iterarse varias veces en una sola interacción. El capítulo 03 de este módulo muestra cómo cada resultado de herramienta se incorpora al contexto de forma acumulativa. La sección 03 de este capítulo detalla los mecanismos técnicos de invocación con ejemplos concretos.

### Lo que este capítulo cubre

Las quince secciones de este capítulo construyen un marco completo para diseñar, implementar y operar sistemas basados en herramientas:

- Las secciones 01 a 03 establecen el marco conceptual y los mecanismos técnicos de invocación.
- Las secciones 04 a 06 abordan la arquitectura de integración y la orquestación dentro de una interacción.
- La sección 07 desarrolla seguridad y control de ejecución.
- La sección 08 aplica todo lo anterior al contexto empresarial concreto.
- Las secciones 09 a 11 presentan patrones, un caso de estudio completo y un laboratorio práctico.
- Las secciones 12 a 15 cierran con una checklist operativa, un resumen, autoevaluación y la transición al capítulo 08.

Al terminar este capítulo, el lector podrá diseñar herramientas correctamente definidas, integrarlas en flujos de contexto reales, gestionar errores y errores, aplicar controles de seguridad apropiados y distinguir con precisión entre lo que le compete a las herramientas y lo que le compete a los agentes del capítulo siguiente.
