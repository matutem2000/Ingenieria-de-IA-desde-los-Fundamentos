# Capitulo-01-Seccion-03-v1.0

# ¿Qué es realmente el contexto?

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Cuando un usuario escribe un mensaje en ChatGPT, Claude o Gemini, suele imaginar que el modelo responde únicamente a ese texto. En realidad, el modelo recibe un conjunto mucho más amplio de información. Ese conjunto constituye el **contexto**.

Comprender qué integra el contexto es el primer paso para diseñar soluciones profesionales de IA.

---

# Una definición práctica

Podemos definir el contexto como:

> **Toda la información disponible para el modelo en el instante en que debe generar una respuesta.**

Esta definición incluye mucho más que el mensaje del usuario.

El contexto puede contener:

- instrucciones del sistema;
- mensajes anteriores;
- memoria persistente;
- documentos recuperados mediante RAG;
- resultados de herramientas;
- datos del usuario;
- fecha y hora;
- restricciones del dominio;
- políticas de seguridad.

---

# El contexto como una arquitectura

Una forma útil de visualizarlo es pensar en el contexto como una pila de capas.

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

En la siguiente sección analizaremos cómo interactúan estas capas y qué principios permiten construir arquitecturas de contexto eficientes, escalables y mantenibles.
