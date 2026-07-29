# Capítulo 12 — Context Engineering Empresarial

## Sección 02: Contexto organizacional y conocimiento corporativo

El conocimiento de una organización no es una base de datos ordenada esperando ser indexada. Es un ecosistema desordenado, parcialmente documentado, distribuido en decenas de sistemas distintos, actualizado por cientos de personas con criterios heterogéneos y acumulado durante años o décadas. Esa realidad define el problema de contexto más complejo que enfrenta el AI Engineer en un entorno corporativo.

Esta sección no repite lo que el capítulo de RAG ya enseñó sobre cómo funciona la recuperación vectorial técnicamente. Parte de ese conocimiento y agrega la dimensión que solo aparece en el contexto organizacional: cómo el conocimiento corporativo es cualitativamente diferente del conocimiento individual, y qué consecuencias tiene esa diferencia para el diseño del contexto.

### Las dimensiones del conocimiento corporativo

El conocimiento que una organización produce y acumula puede clasificarse en tres dimensiones que son relevantes para el AI Engineer.

**La dimensión de la estructura.** Parte del conocimiento corporativo está explícitamente documentado: manuales de productos, políticas aprobadas, contratos firmados, procedimientos operativos estándar, especificaciones técnicas. Este conocimiento existe en documentos, es recuperable y puede indexarse para RAG. Pero otra parte del conocimiento corporativo es tácito: las convenciones informales que el equipo de ventas usa para calificar un cliente, los criterios implícitos con los que el equipo de diseño aprueba una interfaz, el historial de decisiones que nunca se documentó pero que explica por qué el sistema está estructurado como está. Ese conocimiento tácito es el que los nuevos empleados tardan meses en adquirir y el que los sistemas de IA nunca tendrán acceso a menos que alguien tome la decisión deliberada de documentarlo.

**La dimensión de la vigencia.** Un documento corporativo tiene una vida útil que varía radicalmente según su tipo. Una política de precios puede cambiar trimestralmente. Un manual de usuario puede actualizarse con cada versión del producto. Un contrato puede estar vigente durante cinco años sin modificaciones. Una nota interna puede quedar obsoleta a las 48 horas de su creación. Un sistema de IA que indexa conocimiento corporativo sin distinguir la vigencia de sus fuentes producirá respuestas que mezclan información actual con información desactualizada, sin que el usuario pueda distinguir cuál es cuál. La gestión de la vigencia del conocimiento no es un problema técnico de embeddings: es un problema de proceso organizacional que el arquitecto debe resolver antes de que el sistema entre en producción.

**La dimensión de la autoridad.** No toda la información que circula en una organización tiene el mismo nivel de autoridad. Una presentación de estrategia del CEO tiene mayor autoridad que una nota informal de un analista. Un procedimiento aprobado por el comité de riesgo tiene mayor autoridad que una práctica de trabajo que nunca fue oficializada. Un contrato firmado por la dirección legal tiene mayor autoridad que un borrador preparado por un pasante. Cuando un sistema de IA recupera información para responder una pregunta, no distingue automáticamente entre fuentes de alta autoridad y fuentes de baja autoridad. El arquitecto debe diseñar esa distinción en la arquitectura del contexto.

### El problema de la calidad del conocimiento corporativo

La realidad en la mayoría de las organizaciones medianas y grandes es que la calidad del conocimiento acumulado es heterogénea. Esto tiene causas estructurales bien conocidas.

Las organizaciones no documentan en tiempo real. La documentación se produce cuando hay tiempo —que frecuentemente es después de que el proyecto terminó, la situación cambió o el responsable se fue—. El resultado es documentación que describe cómo se pensó que iba a funcionar algo, no cómo funciona realmente.

Las organizaciones no eliminan conocimiento obsoleto sistemáticamente. Los servidores corporativos acumulan documentos de todos los años sin un proceso riguroso de archivo o eliminación. Un sistema de RAG que indexa esa base sin filtros puede recuperar, con igual probabilidad, el manual vigente y el manual de tres versiones anteriores, sin que el usuario sepa cuál es cuál.

Las organizaciones tienen silos de información. El equipo legal tiene documentos que el equipo técnico no puede ver. El equipo comercial tiene datos de clientes que el equipo de producto no puede acceder directamente. Las restricciones de acceso no son arbitrarias —protegen información sensible y gestionan riesgos de confidencialidad— pero son una realidad que el diseño del contexto debe respetar.

### Qué significa Context Engineering en este escenario

Construir un sistema de IA sobre conocimiento corporativo desordenado requiere resolver cuatro decisiones de diseño que no aparecen en el proyecto individual.

**Primera decisión: qué conocimiento se indexa.** No todo el conocimiento corporativo debe entrar en la base vectorial. El AI Engineer debe definir, en coordinación con los responsables del negocio, qué fuentes se indexan, con qué criterio de inclusión y con qué proceso de curación previa. Esta decisión tiene consecuencias directas sobre la calidad de las respuestas: una base vectorial construida con fuentes de alta calidad y alta autoridad producirá respuestas más precisas que una base construida con todo lo disponible sin criterio de selección.

**Segunda decisión: con qué granularidad se fragmenta.** La fragmentación de documentos para indexación en bases vectoriales es una decisión técnica con consecuencias semánticas importantes. Un fragmento demasiado pequeño pierde el contexto necesario para que la respuesta tenga sentido. Un fragmento demasiado grande incluye información irrelevante que diluye la señal. El tamaño óptimo de fragmento depende del tipo de documento: un párrafo de un manual técnico tiene diferente densidad semántica que un párrafo de un contrato legal o que un artículo de una base de conocimiento de soporte.

**Tercera decisión: cómo gestionar la vigencia.** El sistema debe saber si el conocimiento que recupera está vigente. Esto requiere que los documentos indexados tengan metadatos de fecha de creación y fecha de última modificación, y que el sistema use esos metadatos en la recuperación —priorizando fuentes recientes cuando hay varias opciones— y en la respuesta, indicando al usuario la fecha del conocimiento que está usando.

**Cuarta decisión: cómo respetar las restricciones de acceso.** Los sistemas de IA empresariales no pueden ignorar los controles de acceso existentes. Si un empleado no tiene acceso al contrato de un cliente específico, el sistema de IA tampoco debe incluir ese contrato en su contexto cuando responde preguntas de ese empleado. Implementar controles de acceso en un sistema de RAG requiere un diseño que vincule los metadatos de autorización de cada documento con los permisos del usuario que hace la consulta.

### Diagrama: capas del conocimiento corporativo para Context Engineering

```
CAPA 1 — CONOCIMIENTO CORPORATIVO UNIVERSAL
  Políticas aprobadas | Valores y misión | Marco regulatorio
  Acceso: todos los sistemas y usuarios
  Actualización: proceso formal de aprobación

CAPA 2 — CONOCIMIENTO DEPARTAMENTAL
  Procedimientos del área | Documentación de proyectos | Guías de trabajo
  Acceso: equipo responsable + sistemas del área
  Actualización: responsable del área con revisión periódica

CAPA 3 — CONOCIMIENTO OPERATIVO
  Datos de clientes | Contratos activos | Historiales de caso
  Acceso: roles con permiso explícito
  Actualización: continua, con procesos de validación

CAPA 4 — CONOCIMIENTO TÁCITO (a documentar)
  Convenciones informales | Criterios implícitos | Decisiones sin registrar
  Acceso: requiere proceso de captura y formalización
  Actualización: requiere programa de gestión del conocimiento
```

### La diferencia que hace la perspectiva empresarial

En el capítulo de RAG se aprendió cómo construir un índice vectorial y recuperar fragmentos relevantes para enriquecer el contexto del modelo. Eso resuelve el problema técnico. La perspectiva empresarial agrega las preguntas que el capítulo de RAG no respondió: ¿quién es responsable de mantener actualizado ese índice? ¿con qué frecuencia se revisa? ¿cómo sabe el sistema —y el usuario— que la información que recuperó es la versión vigente? ¿qué pasa cuando un empleado abandona la organización y era el único responsable de mantener cierta documentación?

Estas preguntas no tienen respuestas técnicas. Tienen respuestas organizacionales. El AI Engineer que solo sabe responder las preguntas técnicas construirá sistemas que funcionan bien en el día de la entrega y se degradan silenciosamente durante los meses siguientes, sin que nadie lo note hasta que el sistema empieza a dar respuestas incorrectas con confianza.

### Nota del arquitecto

El proceso de inventariar el conocimiento corporativo antes de diseñar el sistema de IA es el equivalente empresarial del análisis de datos antes de entrenar un modelo: inevitablemente revela que la situación es peor de lo que se pensaba. La documentación está más desactualizada de lo esperado. Las fuentes autorizadas son más difíciles de identificar de lo previsto. Los controles de acceso son más complejos de mapear de lo que se asumió. Esta revelación no debe tratarse como un obstáculo; es información de diseño. Un arquitecto que sabe cómo está realmente el conocimiento corporativo puede diseñar un sistema que funciona en esa realidad. Un arquitecto que asume que el conocimiento está bien organizado diseñará un sistema que falla en producción.

La siguiente sección examina qué arquitecturas permiten gestionar ese conocimiento complejo a escala: cómo estructurar la infraestructura de contexto de una organización para que múltiples equipos y múltiples sistemas puedan compartir y especializar el conocimiento de forma coherente.
