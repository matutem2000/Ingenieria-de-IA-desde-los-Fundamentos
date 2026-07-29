# Principios de diseño del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Diseñar el contexto de una aplicación basada en LLM no consiste en agregar toda la información disponible. El objetivo es proporcionar **la información correcta, en el momento correcto y con la estructura adecuada**.

En esta sección analizaremos los principios que sirven como guía para construir arquitecturas de contexto eficientes.

---

# Principio 1 — Relevancia

Todo elemento incorporado al contexto debe contribuir a resolver la tarea.

Antes de agregar información, pregúntese:

- ¿Es necesaria para responder?
- ¿Aporta valor?
- ¿Puede recuperarse bajo demanda?

La información irrelevante incrementa el consumo de tokens y dificulta el razonamiento.

---

# Principio 2 — Jerarquía

No toda la información tiene la misma importancia.

Una jerarquía habitual es:

1. Instrucciones del sistema.
2. Políticas y restricciones.
3. Memoria persistente.
4. Historial.
5. Información recuperada.
6. Consulta del usuario.

Cuando existen conflictos, esta jerarquía permite resolverlos de manera consistente.

---

# Principio 3 — Modularidad

Cada componente del contexto debería mantenerse de forma independiente.

Ejemplos:

- perfil del usuario;
- memoria;
- documentos RAG;
- herramientas;
- historial.

La modularidad simplifica el mantenimiento y favorece la reutilización. Si cambiar el idioma del usuario exige modificar el prompt principal, la modularidad está comprometida.

---

# Principio 4 — Actualización

El contexto debe reflejar el estado actual del sistema.

Es recomendable:

- eliminar información obsoleta;
- refrescar datos dinámicos;
- invalidar memorias incorrectas;
- volver a consultar fuentes cuando sea necesario.

---

# Principio 5 — Economía de tokens

Los modelos tienen un límite de contexto y cada token tiene un costo.

Una arquitectura eficiente:

- resume información repetitiva;
- evita duplicados;
- utiliza RAG para recuperar únicamente lo necesario;
- elimina contenido que ya no aporta valor.

---

# Ejemplo

Un asistente de soporte recibe la solicitud:

> "¿Cuál es el estado del incidente 1542?"

En lugar de enviar toda la base de tickets al modelo, el sistema:

1. identifica el incidente;
2. recupera únicamente su información;
3. incorpora el perfil del usuario;
4. agrega las políticas de respuesta;
5. envía el contexto al LLM.

El resultado es una respuesta más rápida, económica y precisa.

---

# Checklist de diseño

Antes de poner en producción una solución, verifique:

- ¿Cada bloque del contexto tiene un propósito?
- ¿Existe información redundante?
- ¿Las prioridades están definidas?
- ¿La memoria puede actualizarse?
- ¿El conocimiento recuperado está vigente?
- ¿El modelo tiene toda la información necesaria para responder?
- ¿Hay datos desactualizados que podrían inducir a error?
- ¿Existe información que podría recuperarse bajo demanda en lugar de enviarse siempre?

---

# Resumen

El Context Engineering combina principios de arquitectura de software con técnicas específicas para modelos de lenguaje. La calidad del contexto depende menos de su tamaño que de su organización.

En la próxima sección pondremos en práctica estos principios mediante un laboratorio rápido de diseño de arquitectura de contexto.
