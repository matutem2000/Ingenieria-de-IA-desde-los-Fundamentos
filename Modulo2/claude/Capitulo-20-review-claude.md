# Informe Editorial — Capítulo 20

**Capítulo:** 20 — Arquitecturas Basadas en Prompts  
**Módulo:** 2 — Prompt Engineering Profesional  
**Versión revisada:** 0.1  
**Fecha de revisión:** 2026-07-01  
**Rol:** Director Pedagógico y Revisor Editorial

---

## 1. Fortalezas

### Progresión conceptual coherente

El capítulo construye una escalera conceptual bien diseñada: parte del prompt como unidad aislada (Sección 01), avanza hacia la composición (Sección 02), introduce la jerarquía y la orquestación (Sección 03), diferencia cadenas de grafos (Sección 04), integra capacidades externas como RAG y Tool Calling (Sección 05), sistematiza en patrones reutilizables (Sección 06) y cierra con un catálogo evolutivo (Sección 07). El recorrido tiene lógica interna sólida.

### Diagramas mermaid como andamiaje visual

El uso sistemático de diagramas `mermaid` en todas las secciones es una fortaleza clara. En un capítulo que trata de flujos y relaciones entre componentes, el apoyo visual reduce la carga cognitiva y hace tangibles conceptos abstractos. Destacan los diagramas de las Secciones 03, 04 y 07, que muestran bien la diferencia entre jerarquía plana y bifurcaciones.

### Casos de estudio aplicados a contextos reconocibles

Los casos de estudio están bien elegidos (asistente de expedientes en Sección 01, gestión de siniestros en Sección 02, asistente corporativo multi-dominio en Sección 03, atención ciudadana en Secciones 04 y 06, soporte técnico en Sección 05). Todos están dentro del mundo empresarial real, lo que facilita la identificación del lector con los problemas descritos.

### Consistencia estructural entre secciones

Cada sección sigue el mismo esquema: epígrafe, objetivos, introducción, desarrollo con tabla y diagrama, caso de estudio, buenas prácticas, errores frecuentes, ideas clave y transición. Esta consistencia reduce la fricción cognitiva: el lector sabe siempre qué esperar en cada bloque.

### Transiciones entre secciones

Las frases de cierre de cada sección anticipan con precisión el contenido siguiente. Esto genera sensación de continuidad narrativa y orienta la lectura hacia adelante.

### Estilo claro y directo

El estilo de escritura es conciso, sin ornamentos innecesarios. La prosa es breve, los párrafos son cortos y las oraciones directas. Esto es apropiado para un texto técnico de nivel profesional.

### Epígrafes con criterio temático

Los epígrafes de apertura varían por sección y están bien elegidos: cada uno anticipa el núcleo conceptual de la sección desde una perspectiva de diseño. El epígrafe de cierre compartido ("Un arquitecto no memoriza respuestas...") funciona como ancla temática del capítulo completo.

---

## 2. Debilidades

### Ausencia de definición explícita del término "arquitectura" (Sección 01)

La Sección 01 introduce el concepto de "arquitectura basada en prompts" sin definir qué se entiende por arquitectura en este contexto. El lector que viene de capítulos anteriores sobre diseño de prompts puede no tener clara la distinción entre una colección de prompts y una arquitectura propiamente dicha. El salto conceptual se asume sin andamiaje.

### La tabla de "Características" en Sección 01 y la tabla de "Beneficios" en Sección 02 son casi redundantes

La tabla de Sección 01 lista: modularidad, reutilización, bajo acoplamiento, versionado independiente y observabilidad. La tabla de Sección 02 lista: reutilización, mantenibilidad, escalabilidad, observabilidad y pruebas independientes. Hay solapamiento alto entre ambas. Desde una perspectiva editorial, estas dos tablas compiten entre sí en lugar de sumar capas de comprensión distintas.

### El orquestador no se diferencia claramente del grafo de decisiones (Secciones 03 y 04)

La Sección 03 presenta el orquestador como un componente coordinador central. La Sección 04 introduce los grafos de prompts como flujos con bifurcaciones dinámicas. Sin embargo, el diagrama de la Sección 03 (flujo TD con un nodo B que se ramifica hacia C, D, E, F) es visualmente casi idéntico al diagrama de grafo de la Sección 04. El lector puede confundir ambos conceptos porque no se explicita qué es lo que los hace genuinamente distintos: uno es un componente (el orquestador), el otro es una topología (el grafo).

### El papel del "constructor de respuesta" en Sección 05 no se explica

El diagrama de arquitectura integrada de la Sección 05 incluye un nodo llamado "Constructor de respuesta" (nodo G) que recibe salidas del Prompt, el RAG, el Tool Calling y el Agente Especializado. Sin embargo, este componente no aparece ni en la tabla de responsabilidades ni en el texto narrativo. Es un elemento central del diagrama que queda sin descripción.

### El catálogo de patrones en Sección 06 introduce términos sin desarrollo

La tabla de patrones frecuentes de la Sección 06 lista "Workflow" y "Multiagente" como patrones, pero ninguno de los dos se desarrolla en el capítulo. Se mencionan de pasada en el caso de estudio pero no se explica qué distingue un patrón Workflow de un Orquestador o un Grafo. El lector queda con nombres en la tabla sin contenido detrás.

### La Sección 07 no agrega nuevo contenido conceptual

La Sección 07 cumple una función de cierre y síntesis, lo cual es válido, pero el catálogo de referencia que presenta no añade ninguna idea que no haya sido mencionada previamente. El diagrama de "Evolución arquitectónica" (Prompt único → Pipeline → Modular → Orquestador → Integración → Herramientas → Agentes → Plataforma) es útil, pero la tabla que lo acompaña repite categorías ya vistas. Esta sección aporta estructura pero no densidad conceptual nueva.

### Falta de criterios de decisión concretos entre patrones (Sección 06)

La sección sobre patrones señala que "la elección no depende únicamente de la tecnología disponible" y lista seis criterios de análisis, pero no ofrece ningún ejemplo de cómo aplicar esos criterios para elegir entre, por ejemplo, un Pipeline y un Grafo. El lector sabe que debe analizar la "naturaleza del problema" pero no sabe qué características de un problema orientan hacia un patrón u otro.

---

## 3. Conceptos que conviene ampliar

### Definición de "contrato funcional" o "contrato de entrada y salida" (Secciones 01, 02 y 03)

Las buenas prácticas de las Secciones 01, 02 y 03 mencionan "definir contratos claros entre componentes" como principio fundamental. Sin embargo, nunca se explica qué es un contrato en este contexto: ¿es un schema JSON? ¿una especificación del formato de entrada y salida? ¿un documento de texto? ¿un test automatizado? Este concepto se repite en múltiples secciones sin nunca materializarse en algo concreto. Es uno de los vacíos pedagógicos más relevantes del capítulo.

### Latencia y consumo de tokens como restricciones arquitectónicas (Sección 02)

La Sección 02 menciona en "Errores frecuentes" el "impacto acumulado sobre latencia y consumo de tokens" como un riesgo de encadenar prompts sin estrategia. Sin embargo, este tema no se desarrolla en ninguna sección. Para un lector que deba tomar decisiones de diseño reales, la cuestión del costo operativo y la latencia de las arquitecturas multi-prompt es crítica y merece al menos un bloque propio.

### Gestión de errores en arquitecturas jerárquicas (Sección 03)

La tabla de responsabilidades del orquestador en la Sección 03 incluye "Gestionar errores" como una responsabilidad. Pero no hay ningún desarrollo de qué implica gestionar errores en este contexto: ¿qué pasa cuando un componente especializado falla? ¿hay reintentos? ¿hay fallbacks? ¿quién notifica al usuario? Este es un aspecto central del diseño de sistemas robustos y merece una subsección específica.

### El patrón Multiagente (Sección 06)

El patrón "Multiagente" aparece en la tabla de la Sección 06 como uno de los patrones frecuentes, pero no tiene ni una sección propia ni un desarrollo dentro de la sección. Dado que el libro parece incluir módulos posteriores sobre agentes, una breve descripción de en qué se diferencia arquitectónicamente este patrón de un Orquestador sería muy útil aquí como puente conceptual.

### Criterios para decidir cuándo usar un componente RAG versus incluir información en el contexto (Sección 05)

La Sección 05 integra RAG como componente de recuperación de conocimiento externo, pero no ofrece criterios para decidir cuándo es preferible RAG versus contexto estático. Para un ingeniero que está diseñando una arquitectura, esta es una decisión concreta que el texto evita.

### El concepto de "estado" en arquitecturas de grafos y workflows (Secciones 04 y 06)

La Sección 04 menciona que los grafos permiten decisiones dinámicas en tiempo de ejecución y la Sección 06 menciona el patrón "Workflow" como modelado de "procesos con estados". Sin embargo, la gestión del estado entre nodos —cómo se almacena, cómo se transmite, qué ocurre si el estado se corrompe— no se aborda en ningún momento. Es un concepto técnico crítico para implementar cualquier arquitectura no trivial.

---

## 4. Conceptos que pueden resumirse

### Buenas prácticas y errores frecuentes de las Secciones 01, 02 y 03

Las listas de "Buenas prácticas" y "Errores frecuentes" de las Secciones 01, 02 y 03 son prácticamente intercambiables. Las tres mencionan: responsabilidad única, contratos claros, reutilización, desacoplamiento, no concentrar lógica en un único prompt. Esta repetición acumulada no añade conocimiento nuevo en cada sección. Podría consolidarse en una única lista de principios generales en la Sección 01 y en las secciones siguientes solo señalarse las particularidades propias de cada patrón.

### Los casos de estudio de las Secciones 04 y 06 se solapan temáticamente

Ambos casos describen una "plataforma de atención ciudadana" que clasifica consultas y las deriva a componentes especializados. Aunque los casos tienen énfasis distintos (grafos dinámicos en Sección 04, evolución de patrones en Sección 06), el escenario base es tan similar que el lector puede confundirlos o percibir repetición innecesaria.

### Las "Ideas clave" de las Secciones 02 y 03 son redundantes entre sí

Las ideas clave de la Sección 02 (composición, modularidad, diseño que reduce complejidad) y las de la Sección 03 (jerarquía, orquestador coordina/especializados ejecutan, desacoplamiento) comparten el eje central de "modularidad y desacoplamiento" al punto de que podrían unificarse sin pérdida de información.

### La Sección 07 puede comprimirse

La Sección 07 tiene valor como cierre sintético pero actualmente ocupa el mismo espacio que el resto de las secciones. El catálogo de referencia podría reducirse a la tabla evolutiva, los indicadores de cuándo evolucionar y el caso de estudio final, eliminando las "Buenas prácticas" y "Errores frecuentes" que son ya conocidos por el lector en ese punto del capítulo.

---

## 5. Recomendaciones editoriales

### 5.1 Agregar una definición operativa de "arquitectura basada en prompts" al inicio de la Sección 01

La Sección 01 abre con la transición del prompt al componente, pero el término "arquitectura" se usa desde el título sin ser definido. Convendría incluir una definición de una o dos oraciones antes del diagrama mermaid, que establezca explícitamente qué separa una "arquitectura" de un conjunto de prompts encadenados. Esto elimina la ambigüedad desde el primer contacto.

### 5.2 Diferenciar visualmente el orquestador del grafo en Secciones 03 y 04

Los diagramas de ambas secciones son topológicamente similares. Se recomienda que el diagrama de la Sección 03 enfatice al orquestador como nodo con lógica propia (por ejemplo, con una etiqueta que indique "decide" o "evalúa") y que el diagrama de la Sección 04 enfatice las condiciones en las transiciones (ya presente pero podría hacerse más explícito con etiquetas en las flechas). Esto haría visualmente clara la distinción conceptual entre "componente de coordinación" y "topología de flujo".

### 5.3 Desarrollar el concepto de "contrato" con un ejemplo mínimo en Sección 02

Dado que el concepto de "contrato entre componentes" es central y se repite en tres secciones (01, 02 y 03), conviene materializarlo en la Sección 02 con un ejemplo concreto: un esquema de entrada y salida de un prompt de clasificación, aunque sea en pseudocódigo o texto estructurado. Esto le da peso técnico a un principio que actualmente es solo una declaración.

### 5.4 Describir el "Constructor de respuesta" en Sección 05

El nodo "Constructor de respuesta" del diagrama de la Sección 05 debe aparecer en la tabla de responsabilidades y recibir al menos un párrafo de descripción. Sin esto, hay una inconsistencia directa entre el diagrama y el texto que puede desconcertar al lector.

### 5.5 Consolidar buenas prácticas genéricas en Sección 01 y diferenciar las específicas en cada sección posterior

Para reducir la repetición de las listas de buenas prácticas y errores frecuentes, se recomienda que la Sección 01 establezca el conjunto de principios generales (responsabilidad única, contratos, reutilización, desacoplamiento, versionado) y que las secciones siguientes solo listen las consideraciones propias de cada patrón. Esto elimina la sensación de que cada sección está repitiendo el mismo contenido con palabras ligeramente distintas.

### 5.6 Agregar al menos un párrafo sobre latencia y costo en Sección 02 o Sección 04

La Sección 02 menciona el impacto sobre latencia y tokens como un error frecuente, pero no lo desarrolla. La Sección 04, que trata sobre grafos con ejecuciones condicionales, es un lugar natural para tratar este tema: cuántos nodos se activan en cada ejecución tiene consecuencias directas sobre el costo y la latencia del sistema. Un párrafo corto en esa sección con una orientación práctica daría sustancia a una advertencia que hoy queda en el aire.

### 5.7 Diferenciar los casos de estudio de Secciones 04 y 06

Dado que ambos casos usan el mismo escenario base (plataforma de atención ciudadana), se recomienda cambiar uno de ellos por un contexto diferente —por ejemplo, un sistema de onboarding de clientes, un asistente de auditoría interna o una plataforma de análisis financiero— para que el lector pueda apreciar que los patrones se aplican a problemas de distinta naturaleza.

### 5.8 Agregar una nota al pie o recuadro sobre el patrón Multiagente en Sección 06

Dado que el patrón "Multiagente" aparece en la tabla pero no se desarrolla, una nota breve que lo diferencie del patrón Orquestador y lo vincule con el módulo posterior del libro sería suficiente para no dejar al lector con una entrada de tabla sin contenido. No es necesario un desarrollo extenso, pero sí una referencia al módulo donde se tratará en profundidad.

### 5.9 Revisar el diagrama de evolución de Sección 07

El diagrama de "Evolución arquitectónica" de la Sección 07 incluye "Herramientas" y "Agentes" como niveles separados. Sin embargo, en la Sección 05 ya se presentan integrados dentro de la misma arquitectura. Convendría revisar si la separación en el diagrama de la Sección 07 es intencional o genera una inconsistencia con lo presentado previamente.

### 5.10 Considerar un glosario de términos al final del capítulo

El capítulo introduce términos como orquestador, pipeline, grafo, Router, Workflow, contrato, desacoplamiento y observabilidad sin una referencia consolidada. Un glosario breve al final de la Sección 07 —o como apéndice del capítulo— mejoraría la navegabilidad para el lector que quiera consultar definiciones durante el estudio.

---

*Fin del informe editorial. Este documento analiza el manuscrito v0.1 sin alterar ni reescribir el contenido original.*
