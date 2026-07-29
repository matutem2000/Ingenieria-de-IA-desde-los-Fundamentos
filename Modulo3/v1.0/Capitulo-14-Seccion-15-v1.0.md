# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 15: Transición al Capítulo 15

El módulo de Context Engineering se construyó por capas. Cada capa añadió capacidades y, con ellas, complejidad y responsabilidades adicionales.

El módulo comenzó con la arquitectura del contexto: qué es el contexto, cómo se construye, qué límites tiene y por qué el diseño del contexto determina la calidad del sistema. Construyó sobre eso los mecanismos de memoria: cómo el sistema puede recordar información relevante entre turnos y entre sesiones, y qué formas de memoria sirven para qué propósitos. Desarrolló el Retrieval-Augmented Generation: cómo conectar el modelo con conocimiento externo actualizable, cómo recuperar los fragmentos más relevantes y cómo integrarlos eficientemente en el contexto. Extendió el sistema con herramientas: cómo el agente puede actuar sobre el mundo, no solo generar texto. Integró múltiples agentes con distintas especialidades coordinadas por un orquestador. Construyó la observabilidad: cómo saber si el sistema está funcionando correctamente, qué medir, cómo detectar la degradación. Y finalmente, este capítulo añadió la seguridad: cómo garantizar que todo eso funciona dentro de los límites autorizados, protege la privacidad, resiste los ataques y puede demostrarlo.

Esas siete capacidades —arquitectura de contexto, memoria, RAG, herramientas, agentes, observabilidad y seguridad— son los componentes del AI Engineer. El capítulo 15 es la síntesis.

### El proyecto integrador

El capítulo 15 propone un proyecto integrador: el diseño y la implementación de un sistema de Context Engineering completo, de extremo a extremo, que combine los siete componentes del módulo.

El proyecto no es un ejercicio aislado de ningún capítulo. Es la demostración de que el AI Engineer puede integrar todos los conceptos del módulo en un sistema coherente, funcional, observable y seguro.

El enunciado del proyecto integrador tiene la forma de un brief empresarial: una organización, un problema concreto, un conjunto de requisitos funcionales y no funcionales, y restricciones de diseño. El AI Engineer produce: un documento de arquitectura (qué componentes usa el sistema, cómo están conectados, qué decisiones de diseño se tomaron y por qué), el código del sistema (implementado y funcionando), un análisis de observabilidad (qué métricas se definen, qué alertas se configuran, cómo se evalúa la calidad), y un análisis de seguridad (threat model, controles implementados, gaps identificados).

### Lo que el proyecto integrador evalúa

El proyecto evalúa si el AI Engineer puede razonar sobre el sistema completo, no solo sobre sus partes individuales. Las preguntas que el proyecto debe responder son preguntas de síntesis:

**Sobre la arquitectura:** ¿Por qué se eligió esta combinación de componentes y no otra? ¿Qué compensaciones implica cada decisión? ¿Qué haría diferente si el caso de uso fuera distinto?

**Sobre el contexto:** ¿Cómo se construye el contexto en cada solicitud? ¿Qué información se incluye y qué se excluye? ¿Cómo se gestiona el límite de tokens? ¿Cómo se garantiza que el contexto sea relevante para la consulta?

**Sobre la memoria y el RAG:** ¿Cómo interactúan la memoria del agente y el sistema RAG? ¿Qué ocurre cuando hay información contradictoria en ambas fuentes? ¿Cómo se actualiza el conocimiento del sistema sin comprometer la consistencia?

**Sobre los agentes y las herramientas:** ¿Qué herramientas tienen los agentes y por qué exactamente esas y no otras? ¿Qué ocurre cuando una herramienta falla? ¿Cómo se coordina la toma de decisiones en sistemas con múltiples agentes?

**Sobre la observabilidad:** ¿Cómo sabría el equipo si el sistema empieza a degradarse sin que nadie lo reporte? ¿Qué métricas son las más importantes para este sistema específico? ¿Cómo se distingue una falla del sistema de un cambio en el comportamiento del usuario?

**Sobre la seguridad:** ¿Cuáles son las tres amenazas más importantes para este sistema específico? ¿Cómo se mitigan? ¿Qué ocurre si la mitigación falla? ¿Qué logs se generan para poder investigar un incidente?

### De los componentes al sistema

Hay una diferencia entre conocer los componentes del Context Engineering y saber construir un sistema que los integre. Los componentes se pueden aprender por separado: la mecánica del RAG, los tipos de memoria, la estructura de un sistema multiagente. Pero en un sistema real, esos componentes interactúan de maneras no lineales. La decisión sobre la memoria afecta el diseño del RAG. El diseño del RAG afecta la superficie de ataque de seguridad. Los controles de seguridad afectan la latencia del sistema. La latencia afecta la experiencia del usuario. La experiencia del usuario afecta las métricas de observabilidad.

El proyecto integrador es el espacio donde esas interacciones se vuelven visibles y el AI Engineer aprende a navegar el sistema como un todo.

### La perspectiva del módulo

El Context Engineering no es un conjunto de técnicas: es una disciplina de diseño. El AI Engineer que domina esa disciplina no solo sabe implementar un sistema RAG o diseñar un agente multiherramienta; sabe preguntar: ¿qué información necesita el modelo para completar esta tarea, de dónde viene esa información, cuánto debe durar, cómo se protege, cómo se actualiza y cómo sabemos que el sistema sigue funcionando bien?

Esas preguntas son el núcleo del módulo. El capítulo 15 es la oportunidad de demostrar que se pueden responder en un sistema real.

---

*El Capítulo 15 presenta el proyecto integrador del módulo de Context Engineering.*
