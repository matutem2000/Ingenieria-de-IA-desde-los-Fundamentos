# Capítulo 09 — Arquitecturas Multiagente

## Sección 01 — Introducción a las arquitecturas multiagente

Un agente único, bien diseñado, puede resolver una clase sorprendentemente amplia de problemas. Puede razonar, consultar herramientas, mantener memoria episódica y ejecutar planes de múltiples pasos. Los capítulos anteriores de este módulo construyeron ese agente capa por capa: primero el contexto, luego la memoria, después las herramientas, finalmente los patrones de coordinación. Ese agente es poderoso.

Pero hay una categoría de problemas que un agente único no puede resolver bien, no porque le falte capacidad de razonamiento, sino porque la naturaleza del problema excede los límites estructurales de un sistema secuencial con una sola ventana de contexto y un único hilo de ejecución.

¿Cuáles son esos problemas? Son exactamente cuatro tipos:

**Problemas que requieren paralelismo real.** Cuando una tarea puede descomponerse en subtareas independientes que deben completarse simultáneamente para que el resultado sea oportuno, un agente único actúa en serie donde el sistema necesita actuar en paralelo. Analizar veinte documentos de forma concurrente, ejecutar tres búsquedas independientes al mismo tiempo, generar variantes alternativas de una propuesta simultáneamente: estos son casos donde la arquitectura secuencial impone una latencia innecesaria.

**Problemas que requieren especialización profunda.** Un agente generalista que intenta hacer bien muchas cosas distintas necesita un prompt de sistema extenso, herramientas diversas y un contexto que mezcla instrucciones de naturaleza muy diferente. La calidad de sus outputs en cada dominio es inevitablemente menor que la de un agente cuyo único propósito es ese dominio específico, con un prompt ajustado a esa tarea y herramientas seleccionadas para ese trabajo. Un agente especializado en análisis jurídico con acceso a bases de datos legales produce outputs más precisos que un agente generalista que también hace análisis jurídico entre otras cosas.

**Problemas que requieren verificación independiente.** Cuando la corrección de un output es crítica —un diagnóstico médico, un contrato legal, una recomendación financiera—, un único agente que genera y valida su propio trabajo tiene un conflicto de interés estructural: tiende a confirmar lo que produjo. Un segundo agente que recibe el output del primero como input a evaluar, sin haber participado en su generación, aplica una perspectiva genuinamente independiente. Este es el patrón de Reflexión a escala de sistema.

**Problemas cuya escala excede la ventana de contexto de un único agente.** Cuando el volumen de información que una tarea requiere procesar supera lo que puede mantenerse en una sola ventana de contexto, la única solución que no implica compresión con pérdida es distribuir la tarea entre múltiples agentes, cada uno operando sobre un fragmento manejable del problema total.

Cuando uno o más de estos cuatro factores están presentes, la arquitectura de múltiples agentes no es una complejidad opcional: es la respuesta correcta al problema.

### Qué es un sistema multiagente

Un sistema multiagente es una arquitectura en la que dos o más agentes de IA coordinan su trabajo para completar una tarea que ninguno de ellos podría completar de forma óptima en solitario. Cada agente tiene su propio contexto, su propia instrucción de sistema, su propio conjunto de herramientas y, potencialmente, su propia memoria. Lo que los conecta es un mecanismo de comunicación —un protocolo, un almacén de estado compartido, o ambos— y una lógica de coordinación que determina quién hace qué y en qué orden.

Esto no es lo mismo que llamar a un modelo de lenguaje varias veces en un pipeline. En un pipeline secuencial, el output de una llamada es el input de la siguiente, pero no hay agentes en el sentido estricto: hay funciones que se encadenan. Un sistema multiagente implica agentes con autonomía propia —capaces de tomar decisiones, usar herramientas, manejar errores y reportar resultados— coordinados por una lógica que puede ser tan simple como un orquestador central o tan compleja como un protocolo de negociación entre pares.

### La progresión natural desde el agente único

El Capítulo 08 construyó el agente individual: la unidad mínima de comportamiento autónomo en un sistema de IA. Este capítulo escala esa unidad hacia sistemas compuestos.

La progresión no es arbitraria. Es la misma que ocurre en ingeniería de software cuando un monolito bien diseñado alcanza los límites de lo que una única unidad de despliegue puede manejar: no se abandona el monolito porque sea mal código, sino porque la escala del problema cambió. El agente multiagente es al agente único lo que los microservicios son al monolito bien estructurado: una respuesta arquitectónica a la complejidad del problema, no una señal de que el diseño anterior era incorrecto.

### Lo que este capítulo cubre

Las quince secciones de este capítulo construyen el marco completo para diseñar, coordinar y operar sistemas multiagente:

- La sección 02 establece los criterios de decisión para saber cuándo una arquitectura multiagente es la respuesta correcta y cuándo es sobreingeniería.
- Las secciones 03 y 04 desarrollan cómo se diseñan los agentes individuales dentro del sistema y cómo colaboran entre sí.
- Las secciones 05 y 06 abordan los mecanismos de comunicación y la arquitectura de orquestación.
- Las secciones 07 y 08 tratan los problemas de ingeniería más desafiantes: la consistencia del estado compartido y la tolerancia a fallos.
- La sección 09 sistematiza los patrones que funcionan y los anti-patrones que deben evitarse.
- La sección 10 aplica todo lo anterior a un caso empresarial completo.
- Las secciones 11 a 15 proveen el laboratorio práctico, la checklist operativa, el resumen, la autoevaluación y la transición al capítulo siguiente.

Al completar este capítulo, el lector podrá identificar con precisión qué tipo de problema justifica una arquitectura multiagente, diseñar la topología apropiada para ese problema, definir los roles y mecanismos de comunicación de los agentes, anticipar los puntos de fallo del sistema y aplicar estrategias concretas para hacerlo resiliente.

---

*La sección 02 comienza por la decisión más importante del capítulo: ¿cuándo realmente necesitamos más de un agente? La respuesta correcta a esa pregunta evita la complejidad innecesaria que convierte un sistema potencialmente elegante en un sistema difícil de mantener.*
