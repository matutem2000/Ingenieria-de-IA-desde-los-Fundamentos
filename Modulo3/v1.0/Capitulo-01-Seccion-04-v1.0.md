# Cómo procesa un LLM el contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Hasta aquí vimos qué es el contexto y cómo organizarlo en capas. Sin embargo, todavía falta responder una pregunta fundamental:

**¿Qué hace realmente un modelo de lenguaje con toda esa información?**

Responder esta pregunta permite comprender por qué algunas arquitecturas producen resultados consistentes mientras que otras fallan incluso utilizando el mismo modelo.

---

# El contexto como espacio de trabajo

Un LLM no "consulta una base de datos interna" cada vez que responde. En cada interacción construye un espacio de trabajo temporal compuesto por todos los tokens que recibe.

En ese espacio conviven simultáneamente:

- las instrucciones del sistema;
- el historial de la conversación;
- el mensaje del usuario;
- la memoria incorporada;
- los documentos recuperados;
- los resultados de herramientas.

La respuesta se genera utilizando únicamente la información disponible en ese instante.

---

# Un modelo no distingue el origen de los datos

Desde el punto de vista del modelo, toda la información llega convertida en tokens.

Eso significa que una regla del sistema, un párrafo recuperado mediante RAG o el mensaje escrito por el usuario terminan formando parte de la misma secuencia de entrada.

La responsabilidad de priorizar y estructurar esa información recae en el diseñador de la solución.

---

# El orden importa

Aunque los modelos modernos son muy potentes, el orden en que se presenta la información influye en el resultado. Los mecanismos de atención que sustentan a los transformadores asignan mayor peso a la información más cercana al final de la secuencia; por eso las instrucciones críticas y la consulta del usuario tienden a posicionarse en las últimas posiciones.

Una organización habitual es:

1. Instrucciones del sistema.
2. Información permanente.
3. Memoria.
4. Historial.
5. Conocimiento recuperado.
6. Consulta del usuario.

Este orden facilita que el modelo interprete correctamente las prioridades.

---

# Señales contradictorias

Uno de los problemas más comunes ocurre cuando distintas partes del contexto contienen instrucciones incompatibles.

Ejemplo:

- El sistema indica responder siempre en español.
- Un documento recuperado contiene instrucciones para responder en inglés.
- El usuario solicita un resumen en francés.

Sin una jerarquía clara, el comportamiento puede ser impredecible.

Las arquitecturas modernas resuelven este problema estableciendo reglas explícitas de precedencia. Una jerarquía de referencia sencilla y efectiva es la siguiente:

1. **Instrucciones del sistema** (máxima prioridad). Definen el comportamiento base de la aplicación.
2. **Políticas y restricciones** (prioridad alta). Reglas de negocio, seguridad y cumplimiento que no pueden ser sobrescritas por el usuario.
3. **Solicitud del usuario** (prioridad normal). La instrucción del usuario rige en todo lo que no entre en conflicto con los niveles superiores.

Volviendo al ejemplo anterior: el sistema indica español, el documento recuperado incluye texto en inglés (que el modelo puede usar como fuente pero no como instrucción de idioma) y el usuario pide francés. Aplicando la jerarquía, el modelo responde en español porque la instrucción del sistema tiene precedencia sobre la solicitud del usuario. El diseñador puede optar por permitir excepciones de idioma si así lo especifica explícitamente en la capa de sistema.

---

# Caso práctico

Supongamos un asistente jurídico.

Antes de responder una consulta podría recibir:

- políticas institucionales;
- normativa vigente;
- fallos judiciales relevantes;
- historial del expediente;
- perfil del abogado que realiza la consulta;
- pregunta del usuario.

El valor del sistema no depende únicamente del modelo utilizado, sino de cómo se construyó ese contexto.

---

# Error frecuente

Agregar más información no siempre mejora la respuesta.

Un contexto excesivamente grande puede introducir ruido, aumentar el costo y dificultar que el modelo identifique los elementos realmente importantes.

En Context Engineering, **calidad** suele ser más importante que **cantidad**.

---

# Resumen

Un LLM procesa el contexto como una única secuencia de información disponible durante la inferencia. El diseñador de la solución debe decidir qué datos incluir, en qué orden presentarlos y cuáles descartar. Establecer jerarquías de precedencia entre capas es la herramienta clave para resolver conflictos y garantizar un comportamiento predecible.

En la siguiente sección estudiaremos los principios de diseño que utilizan las arquitecturas modernas para construir contextos robustos y eficientes.
