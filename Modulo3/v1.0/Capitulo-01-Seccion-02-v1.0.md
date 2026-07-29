# Los componentes del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Cuando un usuario escribe un mensaje en ChatGPT, Claude o Gemini, suele imaginar que el modelo responde únicamente a ese texto. En realidad, el modelo recibe un conjunto mucho más amplio de información.

En la sección anterior definimos el contexto como toda la información disponible para el modelo en el instante en que debe generar una respuesta. En esta sección exploraremos su estructura interna: qué elementos lo componen y cómo se relacionan entre sí.

Comprender estos componentes es el primer paso para diseñar soluciones profesionales de IA.

---

# El contexto como una arquitectura

Una forma útil de visualizar el contexto es pensarlo como una pila de capas apiladas sobre el modelo.

```text
┌──────────────────────────────────────┐
│ Respuesta del modelo                 │
├──────────────────────────────────────┤
│ Herramientas y resultados            │
├──────────────────────────────────────┤
│ Información recuperada (RAG)         │
├──────────────────────────────────────┤
│ Memoria                              │
├──────────────────────────────────────┤
│ Historial conversacional             │
├──────────────────────────────────────┤
│ Prompt del usuario                   │
├──────────────────────────────────────┤
│ Instrucciones del sistema            │
└──────────────────────────────────────┘
```

Cada una de estas capas aporta información que modifica la forma en que el modelo razona.

---

# Los componentes principales

## 1. Instrucciones del sistema

Definen el comportamiento esperado del modelo.

Ejemplos:

- rol profesional;
- idioma;
- formato de respuesta;
- restricciones;
- objetivos.

---

## 2. Mensaje del usuario

Representa la necesidad inmediata que debe resolverse.

No suele contener toda la información necesaria para producir la mejor respuesta.

---

## 3. Historial

Permite mantener continuidad entre distintas interacciones.

Gracias al historial el modelo puede interpretar referencias como:

> "Hacé lo mismo que antes."

Sin historial esa instrucción carecería de significado.

---

## 4. Memoria

La memoria conserva información que debe sobrevivir a una conversación específica.

Por ejemplo:

- preferencias del usuario;
- proyectos activos;
- estilo de comunicación;
- configuraciones frecuentes.

La diferencia entre memoria e historial es fundamental: el historial describe lo que ocurrió en la conversación actual; la memoria preserva lo que el sistema sabe del usuario más allá de esa conversación. Una sesión puede terminar y la memoria continúa existiendo, lista para enriquecer la siguiente interacción.

---

## 5. Conocimiento recuperado

Muchas aplicaciones incorporan documentación obtenida dinámicamente mediante RAG.

Esto permite responder utilizando información reciente sin necesidad de reentrenar el modelo.

---

## 6. Herramientas

Los modelos modernos pueden consultar APIs, ejecutar funciones o acceder a bases de datos.

El resultado de esas operaciones también pasa a formar parte del contexto.

---

# Error frecuente

Uno de los errores más comunes consiste en invertir todo el esfuerzo en escribir un prompt perfecto mientras se descuida el resto del contexto.

En aplicaciones empresariales suele ocurrir exactamente lo contrario: un prompt sencillo acompañado por un contexto bien diseñado produce mejores resultados que un prompt extremadamente elaborado pero aislado.

---

# Nota del arquitecto

Antes de optimizar un prompt, pregúntese:

- ¿El modelo tiene toda la información necesaria?
- ¿Existe información irrelevante ocupando tokens?
- ¿Hay datos desactualizados?
- ¿Qué podría recuperarse dinámicamente en lugar de enviarse siempre?

Estas preguntas suelen tener un impacto mucho mayor que modificar unas pocas palabras del prompt.

---

# Resumen

El contexto constituye el verdadero espacio de trabajo de un modelo de lenguaje. El prompt del usuario representa solo uno de sus componentes.

En la siguiente sección analizaremos cómo organizar estos componentes en una arquitectura de capas y qué principios permiten construir contextos eficientes, escalables y mantenibles.
