# Módulo 2 — Prompt Engineering Profesional

# Capítulo 22 — Proyecto Integrador del Módulo 2

## Sección 02 — Análisis del Problema

> "Todo proyecto exitoso comienza comprendiendo el problema antes de elegir la tecnología."

### Objetivos de aprendizaje

- Realizar el análisis inicial de un proyecto de AI Engineering.
- Identificar actores, objetivos y restricciones.
- Traducir necesidades de negocio en requerimientos técnicos.
- Definir el alcance de una primera versión viable.

---

### Introducción

Antes de escribir un prompt, seleccionar un modelo o definir una arquitectura, un AI Engineer necesita comprender el problema que intenta resolver.

Las decisiones tomadas durante esta etapa condicionarán el resto del proyecto. Un análisis incompleto suele producir soluciones técnicamente interesantes, pero alejadas de las necesidades reales del negocio.

Esta sección desarrolla el primer entregable del proyecto integrador: el análisis del problema.

---

### Paso 1: Comprender el problema

El análisis inicial debe responder preguntas como:

- ¿Qué proceso desea mejorar la organización?
- ¿Quién utilizará el sistema?
- ¿Qué tareas serán asistidas por el Large Language Model (LLM)?
- ¿Qué tareas seguirán siendo responsabilidad de las personas?
- ¿Cómo se medirá el éxito del proyecto?

Estas respuestas constituyen la base del diseño posterior.

---

### Identificación de actores

| Actor | Responsabilidad |
|---|---|
| Usuario final | Interactúa con el asistente. |
| Responsable funcional | Define reglas de negocio. |
| Equipo de IA | Diseña la solución. |
| Equipo de IT | Integra la plataforma. |
| Administrador | Supervisa operación y métricas. |

Cada actor posee expectativas y necesidades diferentes. Identificarlos desde el inicio evita que el diseño técnico responda a supuestos incorrectos sobre quién usa el sistema y con qué propósito.

---

### Del problema a los requisitos

```mermaid
flowchart LR
  A[Necesidad del negocio] --> B[Objetivos] --> C[Requisitos funcionales] --> D[Requisitos no funcionales] --> E[Arquitectura]
```

El objetivo no consiste únicamente en automatizar tareas, sino en construir una solución sostenible. Cada paso del diagrama transforma una necesidad expresada en lenguaje de negocio en un elemento técnico concreto y verificable.

---

### Caso de estudio

Una empresa desea implementar un asistente para su mesa de ayuda.

Tras las primeras reuniones, el equipo observa que los agentes invierten más tiempo clasificando y registrando cada incidente que respondiendo la consulta en sí. Al revisar los registros existentes y preguntar a los agentes sobre su carga de trabajo diaria, el equipo comprende que el cuello de botella no está en la calidad de las respuestas sino en la fricción del proceso administrativo.

Esta conclusión modifica completamente el alcance del proyecto: la prioridad deja de ser la conversación y pasa a ser la automatización del proceso de atención. El caso ilustra un principio central del análisis: lo que la organización cree que necesita y lo que realmente necesita no siempre coinciden. La diferencia solo se revela al explorar el problema con profundidad.

---

### Actividades propuestas

1. Describir el problema de negocio en términos concretos, evitando referencias a tecnologías específicas.
2. Identificar actores y responsabilidades, y documentar el resultado como un activo verificable del proyecto.
3. Definir objetivos medibles que permitan evaluar el éxito al finalizar la primera versión.
4. Delimitar el alcance de la primera versión: qué queda dentro y qué queda fuera.
5. Registrar supuestos, riesgos y restricciones conocidas como documentación base para las etapas siguientes.

---

### Buenas prácticas

- Comprender el negocio antes de diseñar la solución técnica.
- Validar el alcance con los interesados antes de avanzar.
- Documentar supuestos y restricciones específicos del problema que se está analizando.
- Priorizar objetivos medibles sobre objetivos cualitativos.

---

### Errores frecuentes

- Comenzar escribiendo prompts sin haber completado el análisis previo.
- Confundir deseos con requisitos.
- Intentar resolver todos los problemas en la primera versión.
- No definir criterios de éxito antes de comenzar el desarrollo.

---

### Ideas clave

- Todo proyecto comienza con el análisis del problema, no con la elección de la tecnología.
- La tecnología debe responder a objetivos del negocio, no al revés.
- Un buen análisis reduce riesgos durante el desarrollo y evita rediseños costosos.

---

Con el problema comprendido, los actores identificados y el alcance delimitado, el siguiente paso es traducir ese análisis en una arquitectura concreta. En la próxima sección diseñaremos la arquitectura de referencia del proyecto, definiendo componentes, responsabilidades y flujos de interacción entre ellos.
