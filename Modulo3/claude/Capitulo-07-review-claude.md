# Informe Pedagógico — Capítulo 07: Herramientas, MCP e Integración con Sistemas Externos

**Revisado por:** Director Pedagógico / Claude
**Fecha:** 2026-07-25

---

## NOTA EDITORIAL PRIORITARIA

**El capítulo está en estado de esqueleto estructural. No existe contenido desarrollado en ninguna de sus 15 secciones.** Cada sección contiene únicamente: título, nota editorial de contexto, lista de objetivos genéricos, lista de elementos "previstos" y una frase de transición estándar.

**El capítulo no puede publicarse ni revisarse pedagógicamente en profundidad hasta que el contenido sea desarrollado.**

---

## 1. Fortalezas

**La inclusión de MCP (Model Context Protocol) como sección dedicada (sección 02)** es una decisión editorial acertada y diferenciadora. MCP es un estándar relativamente reciente que está ganando adopción rápida y que aún no aparece en la mayoría de los libros del área. Su tratamiento en profundidad dará actualidad al módulo.

**La distinción entre Function Calling y Tool Calling (sección 03)** responde a una confusión real que existe en el mercado entre la terminología de diferentes proveedores. El capítulo 02 (sección 08) introdujo "herramientas" de manera conceptual; aquí se diferencia entre los mecanismos concretos de invocación, lo que agrega profundidad técnica progresiva.

**La sección 07 ("Seguridad y control de ejecución")** anticipa una de las decisiones de diseño más críticas en sistemas con herramientas: cuándo ejecutar automáticamente y cuándo requerir confirmación humana ("human in the loop"). Esta sección, bien desarrollada, puede ser uno de los aportes más valiosos del capítulo.

**La posición del capítulo en el módulo es correcta.** Las herramientas son el complemento lógico de RAG: RAG recupera conocimiento estático, las herramientas acceden a información dinámica y ejecutan acciones. Vienen en secciones consecutivas, lo que refuerza la distinción establecida en capítulos anteriores.

**La sección 08 ("Integración con sistemas empresariales")** cubre el contexto de aplicación real más frecuente: ERP, CRM, bases de datos internas, sistemas de ticketing, calendarios. Para el AI Engineer corporativo, este es el contenido directamente aplicable.

**La secuencia planificada es progresiva:**
- Secciones 01-03: marco conceptual y mecanismos
- Secciones 04-06: arquitectura e integración
- Sección 07: seguridad
- Sección 08: aplicación empresarial
- Secciones 09-15: patrones, caso de estudio, laboratorio, cierre

---

## 2. Debilidades

**La totalidad del contenido está ausente.** No hay definiciones de Tool Calling, ejemplos de definiciones de herramientas (JSON Schema), diagramas de flujo de ejecución ni casos de uso desarrollados.

**La sección 06 ("Orquestación y planificación de herramientas")** es un tema que también se abordará en el capítulo 08 (Agentes) y en el capítulo 10 (Planificación y Razonamiento). El autor deberá delimitar cuidadosamente qué cubre aquí (selección y ejecución de herramientas dentro de una interacción) y qué reserva para los capítulos de agentes (ciclos de planificación multi-paso).

**El alcance del capítulo puede ser demasiado amplio para 15 secciones.** Herramientas, MCP, Function Calling, Tool Calling, orquestación, seguridad e integración empresarial son temas que en conjunto podrían justificar un módulo completo. El autor debe decidir el nivel de profundidad apropiado para cada uno.

**La sección 05 ("Diseño de herramientas robustas")** es un tema técnico que requiere conocimiento de diseño de APIs (contratos claros, manejo de errores, idempotencia, timeouts). El capítulo no ha establecido si el lector tiene esos conocimientos previos.

---

## 3. Conceptos a ampliar (recomendaciones para el desarrollo)

**Definición de herramientas en JSON Schema:** El lector necesita ver cómo se define una herramienta concretamente (nombre, descripción, parámetros, tipos, validaciones) porque eso determina qué información el modelo recibe para decidir cuándo y cómo invocarla. Al menos tres ejemplos completos de definición de herramienta son necesarios.

**El ciclo completo de Tool Calling:** El diagrama del capítulo 02 (sección 08) mostró el flujo a alto nivel. Este capítulo debe mostrar el ciclo técnico completo: el modelo genera una tool call → la aplicación la ejecuta → el resultado se incorpora al contexto → el modelo continúa o genera la respuesta final. Este ciclo puede repetirse varias veces en una sola interacción.

**Manejo de errores de herramientas:** Qué ocurre cuando una herramienta falla, devuelve un timeout, retorna datos inesperados o excede su límite de uso. Cómo instruir al modelo para manejar estos casos y cómo diseñar respuestas de error que el modelo pueda interpretar.

**Model Context Protocol (MCP) en profundidad:** Qué es MCP, qué problema resuelve respecto a las integraciones directas, cómo se implementa un servidor MCP básico y cuáles son sus limitaciones actuales. Esta sección puede convertirse en el diferenciador del capítulo.

**Límites de autonomía y confirmación humana:** En qué casos el modelo debe ejecutar una herramienta automáticamente y en qué casos debe solicitar confirmación al usuario antes de ejecutar (especialmente en acciones irreversibles como enviar un correo, eliminar un registro o realizar una transacción).

---

## 4. Conceptos a resumir o eliminar

En el estado actual no hay contenido para resumir o eliminar.

Como advertencia preventiva: si la sección 06 ("Orquestación y planificación de herramientas") se desarrolla con ciclos de razonamiento multi-paso, entrará en conflicto con los capítulos 08 y 10. El autor debe reservar la orquestación de herramientas para el contexto de una sola interacción (selección de qué herramienta usar y en qué orden en una sola solicitud) y dejar la planificación multi-turno para los capítulos de agentes.

---

## 5. Recomendaciones editoriales

1. **Desarrollar las 15 secciones** antes de cualquier revisión pedagógica posterior.

2. **Delimitar el alcance desde la sección 01:** establecer explícitamente qué se entiende por "herramienta" en este capítulo (mecanismo de integración en una sola interacción) y qué temas se reservan para los capítulos de agentes y planificación.

3. **Incluir en la sección 03 ejemplos completos de definición de herramienta** en JSON Schema para al menos dos casos: una herramienta de consulta (GET, sin efectos secundarios) y una herramienta de acción (POST, con efectos secundarios). Las implicancias de diseño son diferentes para cada tipo.

4. **Desarrollar MCP en la sección 02** con: (a) qué problema resuelve que no resuelven las integraciones directas, (b) cómo funciona el protocolo, (c) ejemplo de servidor MCP mínimo. Incluir una nota del arquitecto sobre cuándo MCP justifica su complejidad adicional.

5. **La sección 07 ("Seguridad y control de ejecución")** debe abordar el principio del mínimo privilegio aplicado a herramientas: qué permisos reales necesita cada herramienta, cómo evitar que el modelo solicite herramientas que el usuario no está autorizado a usar, y cómo implementar confirmación humana para acciones de alto impacto.

6. **Diseñar el laboratorio (sección 11)** para que el estudiante defina dos herramientas (una de consulta y una de acción), las integre en un flujo de contexto y observe cómo el modelo las invoca para responder una consulta. El ejercicio debe incluir el manejo de un error deliberado de la herramienta.

7. **La sección 15 ("Transición al Capítulo 8")** debe establecer que las herramientas son el mecanismo de ejecución y que los agentes (capítulo 08) son los sistemas que coordinan múltiples herramientas en ciclos de planificación y acción. Esta distinción es esencial para que el lector llegue al capítulo 08 con el marco correcto.
