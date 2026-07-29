# Capitulo-01-Seccion-05-v1.0

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

Aunque los modelos modernos son muy potentes, el orden en que se presenta la información influye en el resultado.

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

Por ese motivo, las arquitecturas modernas establecen reglas explícitas de precedencia.

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

# Buenas prácticas

- Enviar únicamente información relevante.
- Evitar duplicaciones.
- Eliminar datos obsoletos.
- Definir prioridades entre las distintas capas.
- Separar claramente instrucciones, conocimiento y memoria.

---

# Error frecuente

Agregar más información no siempre mejora la respuesta.

Un contexto excesivamente grande puede introducir ruido, aumentar el costo y dificultar que el modelo identifique los elementos realmente importantes.

En Context Engineering, **calidad** suele ser más importante que **cantidad**.

---

# Resumen

Un LLM procesa el contexto como una única secuencia de información disponible durante la inferencia. El diseñador de la solución debe decidir qué datos incluir, en qué orden presentarlos y cuáles descartar.

En la siguiente sección comenzaremos a estudiar los principios de diseño que utilizan las arquitecturas modernas para construir contextos robustos y eficientes.
