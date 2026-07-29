# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 01: Introducción a la seguridad en sistemas de IA

El capítulo anterior construyó las herramientas para saber cuándo un sistema de Context Engineering está fallando: métricas, trazas, evaluadores automáticos, dashboards de producción. Sin esa visibilidad, un sistema puede degradarse durante semanas sin que nadie lo detecte. Con esa visibilidad, el equipo puede diagnosticar problemas, medir mejoras y mantener la calidad en el tiempo.

Pero la observabilidad no protege al sistema de algo que no es una falla técnica: alguien que usa el sistema de manera deliberadamente maliciosa, o un sistema que, sin ningún atacante externo, expone información que no debería exponer, ejecuta acciones que no debería ejecutar o actúa fuera de los límites que la organización estableció. Ese es el dominio de la seguridad.

La seguridad de sistemas de IA es un campo nuevo. Las amenazas son distintas a las del software tradicional, los controles son distintos y los marcos de referencia todavía están madurando. Este capítulo no cubre seguridad de infraestructura general —ataques de red, gestión de secretos de servidor, autenticación de bases de datos— sino la seguridad específica del Context Engineering: las formas en que el diseño del contexto puede ser explotado, y los principios para construir sistemas que resistan esa explotación.

### Por qué la seguridad del contexto es un problema propio

En el software tradicional, el código y los datos están claramente separados. Un servidor web ejecuta código Python; los datos que recibe del usuario son cadenas de texto que el código procesa. Si el usuario envía texto malicioso intentando ejecutar código —una inyección SQL, un ataque de cross-site scripting—, el desarrollador aplica controles en la frontera entre datos y código: escapado, validación, consultas parametrizadas.

Los modelos de lenguaje borran esa frontera. El modelo recibe texto en el contexto y ese texto influye directamente en su comportamiento. No hay separación estricta entre "dato" e "instrucción": un fragmento de texto en el contexto puede ser una instrucción del sistema, el historial de una conversación, un documento recuperado del sistema RAG, el resultado de una herramienta, o un mensaje del usuario. El modelo procesa todo ese texto junto, y el texto malicioso puede confundirse con instrucciones legítimas.

Esta propiedad fundamental hace que la seguridad del Context Engineering sea un problema distinto. Los controles de seguridad de aplicaciones web tradicionales no son suficientes —y en algunos casos no aplican— porque el vector de ataque es el propio contexto que el sistema construye y entrega al modelo.

### Las tres capas de la seguridad en Context Engineering

La seguridad de un sistema de Context Engineering opera en tres capas que corresponden a los tres niveles de preocupación del AI Engineer.

**Primera capa: seguridad técnica del contexto.** Los mecanismos que protegen el contenido del contexto de ser manipulado por atacantes, de exponer información que no debería exponer, y de ejecutar acciones más allá de los límites autorizados. Abarca el diseño de instrucciones resistentes, la validación de entradas, el filtrado de salidas, el sandboxing de herramientas y el control de qué información puede incluirse en el contexto.

**Segunda capa: gobernanza del sistema.** Los procesos organizacionales que definen quién tiene autoridad para cambiar el sistema, qué cambios requieren aprobación, qué datos pueden procesarse y qué herramientas pueden exponerse al modelo. La gobernanza transforma la seguridad de un problema técnico individual en una disciplina organizacional sostenible.

**Tercera capa: compliance.** El conjunto de requisitos externos —regulaciones, normas industriales, obligaciones contractuales— con los que el sistema debe cumplir. El compliance no reemplaza a la seguridad técnica ni a la gobernanza, pero establece el piso mínimo de controles que la organización debe demostrar ante auditores y reguladores.

Las tres capas son necesarias y se refuerzan mutuamente. Un sistema técnicamente seguro sin gobernanza puede ser comprometido por un cambio no revisado en el system prompt. Un sistema bien gobernado sin controles técnicos puede ser explotado directamente por un usuario. Un sistema seguro y gobernado que no cumpla con las regulaciones aplicables puede enfrentar consecuencias legales aunque nunca haya ocurrido un incidente.

### Seguridad desde el diseño, no como parche posterior

El error más frecuente en la primera generación de sistemas de IA empresariales fue tratar la seguridad como una tarea de cierre: "añadimos los controles de seguridad antes del lanzamiento". En la práctica, esto significaba filtros de contenido añadidos a último momento, políticas de acceso definidas apresuradamente y una revisión superficial del system prompt horas antes del despliegue.

El problema de ese enfoque es estructural. Un sistema de Context Engineering que no fue diseñado con seguridad desde el comienzo tiene propiedades que son difíciles de cambiar retroactivamente: el sistema prompt puede estar estructurado de manera que facilita la extracción de sus instrucciones, las herramientas pueden tener permisos más amplios de lo necesario, la memoria del agente puede acumular información de distintos usuarios sin aislamiento, el pipeline de RAG puede mezclar documentos con distintos niveles de confidencialidad.

Corregir esas propiedades después del despliegue no es imposible, pero es costoso y arriesgado. Cada cambio en el diseño del contexto puede alterar el comportamiento del sistema de maneras difíciles de anticipar. El AI Engineer que trata la seguridad como un elemento de diseño desde el comienzo evita esa deuda técnica.

El principio rector es simple: **secure by design** —los controles de seguridad son parte de la arquitectura del sistema, no una capa añadida encima.

### La estructura del capítulo

El capítulo construye la capacidad de diseñar, implementar y operar sistemas de Context Engineering seguros, organizando los contenidos en bloques progresivos.

**Bloque de amenazas** (secciones 01 a 03): los fundamentos de la seguridad en CE, las amenazas específicas para LLMs y agentes, y el análisis en profundidad del prompt injection como la amenaza más relevante para este módulo.

**Bloque de controles** (secciones 04 a 06): la gobernanza de modelos y datos, los principios de privacidad aplicados al contexto, y la gestión de identidades y permisos en sistemas de IA.

**Bloque de compliance y arquitectura** (secciones 07 y 08): el cumplimiento normativo y los requisitos de auditoría, y las arquitecturas seguras para IA empresarial.

**Bloque de síntesis** (secciones 09 a 15): patrones y anti-patrones, caso de estudio, laboratorio de threat modeling, checklist del AI Engineer, resumen, autoevaluación y transición al proyecto integrador.

### Nota del arquitecto

La seguridad de sistemas de IA no es responsabilidad exclusiva del equipo de seguridad. Es responsabilidad compartida del AI Engineer que diseña el sistema, del equipo de plataforma que gestiona la infraestructura, del equipo de datos que decide qué información puede procesarse y del área legal que establece los requisitos de compliance. Este capítulo está escrito desde la perspectiva del AI Engineer: qué decisiones de diseño afectan la seguridad, qué controles puede implementar directamente y qué problemas debe escalar a otros equipos.

La siguiente sección cataloga las amenazas específicas que enfrentan los sistemas basados en LLMs y agentes, y establece cuáles son más relevantes para el Context Engineering.
