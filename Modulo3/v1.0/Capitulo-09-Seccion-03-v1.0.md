# Capítulo 09 — Arquitecturas Multiagente

## Sección 03 — Roles y especialización de agentes

Un sistema multiagente que distribuye trabajo entre agentes genéricos no es un sistema multiagente bien diseñado: es un sistema que añade la complejidad de la coordinación sin aprovechar la principal ventaja de la arquitectura, que es precisamente la especialización. La potencia del diseño multiagente está en que cada agente hace una cosa con precisión, no en que muchos agentes hagan muchas cosas con mediocridad distribuida.

Esta sección desarrolla cómo se definen los roles de los agentes dentro de un sistema, qué significa especializar un agente de forma efectiva y qué decisiones de diseño determinan la calidad de cada unidad dentro del sistema compuesto.

### Qué define el rol de un agente

El rol de un agente no es un nombre en un diagrama. Es la combinación de tres elementos que deben estar alineados de forma coherente:

**El alcance funcional:** qué hace el agente, en términos concretos y limitados. "Analiza el código Python enviado y detecta vulnerabilidades de seguridad según las categorías del OWASP Top 10" es un alcance funcional bien definido. "Ayuda con el desarrollo de software" no lo es.

**El conjunto de herramientas:** qué herramientas tiene disponibles. Un agente cuyo rol es analizar código necesita acceso a herramientas de ejecución de código, linters, bases de datos de vulnerabilidades conocidas. No necesita herramientas de búsqueda web general, acceso a calendarios ni capacidades de redacción de documentos. La disciplina de incluir solo las herramientas que el rol específicamente requiere evita que el agente las use de forma inapropiada y reduce la superficie de errores.

**La instrucción de sistema:** el prompt de sistema que define la identidad, los objetivos, las restricciones y el formato de output del agente. Esta instrucción debe ser específica para el rol, no una versión recortada de un prompt generalista. Un agente crítico tiene una instrucción de sistema fundamentalmente distinta a la de un agente generador, incluso si trabajan sobre el mismo dominio. El agente generador está orientado a producir; el agente crítico está orientado a evaluar. Sus instrucciones de sistema deben reflejar esa diferencia.

### Roles típicos en sistemas multiagente de producción

Los sistemas multiagente bien diseñados tienden a converger en un conjunto de roles arquetípicos que aparecen en distintas configuraciones según el dominio:

**El agente orquestador.** No produce contenido directamente. Descompone tareas complejas en subtareas, asigna esas subtareas a los agentes apropiados, recibe sus outputs y sintetiza el resultado final. Su instrucción de sistema lo orienta explícitamente hacia la coordinación, no hacia la ejecución. Es el director del sistema, no uno de sus instrumentistas.

**El agente investigador.** Su función es recuperar información: buscar en bases de conocimiento, consultar APIs externas, recuperar documentos relevantes. Está equipado con herramientas de búsqueda y recuperación. Su output es información estructurada para ser consumida por otros agentes, no una respuesta final para el usuario.

**El agente analista.** Recibe información —producida por el investigador u obtenida de otra fuente— y produce análisis: patrones, inferencias, evaluaciones, predicciones. Sus herramientas son de cómputo y razonamiento, no de búsqueda. No necesita saber cómo se recuperó la información que analiza.

**El agente redactor.** Transforma análisis o información estructurada en texto de alta calidad para el output final: informes, respuestas al usuario, documentos. Su instrucción de sistema está orientada a la claridad, el tono y el formato. No necesita acceso a bases de datos ni herramientas de cómputo.

**El agente crítico.** Recibe el output de otro agente —generalmente el redactor o el analista— y lo evalúa contra criterios explícitos. Detecta errores de razonamiento, inconsistencias, afirmaciones no respaldadas, problemas de tono o formato. Su output es una evaluación estructurada, no una versión mejorada del texto: la corrección es responsabilidad del agente que generó el output, no del crítico.

**El agente ejecutor.** Es el único agente del sistema que tiene permiso para realizar acciones con efectos en el mundo externo: enviar correos, actualizar registros, ejecutar código en producción. Esta concentración de capacidad de acción en un único agente especializado es una decisión de seguridad deliberada: facilita el control de autorización y la auditoría de todas las acciones del sistema.

### El principio de mínima capacidad

Un agente bien diseñado tiene las capacidades mínimas necesarias para cumplir su función. Este principio no es una restricción arbitraria: es la condición que permite que el sistema sea predecible, seguro y depurable.

Un agente investigador que también puede ejecutar código en producción es un punto de riesgo: si el agente es comprometido o produce un error de razonamiento, las consecuencias pueden ser irreversibles. Un agente investigador que solo puede buscar y leer información tiene un radio de daño acotado.

El principio de mínima capacidad también mejora la calidad del razonamiento. Un agente que tiene disponibles veinte herramientas diferentes dedica esfuerzo de razonamiento a decidir cuál usar. Un agente que tiene tres herramientas relevantes para su función específica utiliza ese mismo esfuerzo de razonamiento en hacer bien su trabajo.

### Diseñar el rol antes de implementar el agente

El error más común en el diseño de agentes especializados es comenzar por la implementación: "creo un agente, le doy herramientas, le pongo un prompt". El resultado es un agente cuyo rol emerge de forma ad hoc de las herramientas que se le dieron y del prompt que se le ocurrió al momento de escribirlo.

El proceso correcto es inverso: primero se define el rol con precisión (¿qué hace este agente? ¿qué no hace?), luego se seleccionan las herramientas que ese rol específicamente requiere, y finalmente se escribe la instrucción de sistema que expresa ese rol con precisión. El orden importa porque la claridad del rol determina la coherencia de las decisiones de implementación que le siguen.

Una prueba útil al diseñar el rol de un agente es la pregunta de la sustitución: si este agente fuera un ser humano contratado para ese rol específico, ¿qué haría en su primer día de trabajo? ¿Qué recursos necesitaría? ¿Qué haría y qué explícitamente no haría? Si esa descripción es clara, el rol está bien definido. Si la respuesta es vaga o incluye demasiadas responsabilidades heterogéneas, el rol necesita más delimitación.

### La frontera entre agentes y su impacto en la calidad

La calidad de un sistema multiagente depende tanto de lo que hace cada agente como de dónde termina la responsabilidad de uno y comienza la del siguiente. Las fronteras mal definidas producen solapamientos (dos agentes intentan hacer lo mismo con enfoques distintos) o vacíos (ningún agente es responsable de una tarea necesaria).

Las fronteras se definen por los contratos de input y output: qué formato produce el agente A como output y qué formato espera consumir el agente B como input. Cuando ambos formatos coinciden sin necesidad de transformación, la frontera está bien definida. Cuando el agente B necesita interpretar o transformar el output del agente A antes de poder trabajar con él, la frontera necesita revisión: o el formato de output del agente A debe ser más preciso, o la responsabilidad de transformación debe asignarse explícitamente a alguno de los dos.

---

*La sección 04 toma los agentes bien diseñados de esta sección y examina cómo se organizan entre sí. Las topologías de colaboración —jerárquica, en pipeline, entre pares, basada en mercado— no son variantes estéticas: cada una tiene casos de uso óptimos y compromisos específicos que el arquitecto debe evaluar antes de comprometerse con una.*
