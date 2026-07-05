# Módulo 2 — Prompt Engineering Profesional

# Capítulo 16 — Ingeniería del Prompt

## Sección 2 — Anatomía de un prompt profesional

> *"Todo prompt profesional posee una estructura. La diferencia entre un resultado consistente y uno impredecible suele comenzar allí."*

---

## Objetivos de aprendizaje

- Comprender la anatomía de un prompt profesional.
- Diferenciar los distintos bloques que conforman un prompt de producción.
- Relacionar cada componente con un requisito de negocio.
- Introducir el concepto de diseño modular de prompts.

---

## Introducción

En una conversación cotidiana es habitual escribir una única instrucción y esperar una respuesta. En una aplicación empresarial ese enfoque rara vez resulta suficiente.

A medida que las soluciones basadas en Large Language Models (LLM) crecieron en complejidad, los prompts evolucionaron desde simples instrucciones hasta convertirse en especificaciones estructuradas con responsabilidades claramente definidas.

Diseñar un prompt implica organizar información de manera que el modelo pueda interpretar correctamente el objetivo, las restricciones y el formato esperado de la respuesta.

---

## Anatomía de un prompt

Un prompt de ingeniería suele estar compuesto por bloques independientes, cada uno con una función precisa.

| Componente | Propósito |
|------------|-----------|
| Rol | Define el comportamiento esperado del modelo. |
| Objetivo | Explica la tarea que debe resolver. |
| Contexto | Proporciona información relevante para la tarea. |
| Restricciones | Limita comportamientos no deseados. |
| Criterios de calidad | Establece cómo evaluar si la respuesta es correcta. |
| Formato de salida | Define la estructura esperada de la respuesta. |

El **Objetivo** merece atención especial. Un objetivo bien formulado describe con precisión qué se espera del modelo: no "analiza este documento", sino "identifica los riesgos contractuales y clasifícalos por severidad". La diferencia entre un objetivo ambiguo y uno bien especificado determina en gran medida el nivel de consistencia de las respuestas.

Los **Criterios de calidad** cumplen dos funciones complementarias. Dentro del prompt le indican al modelo qué estándares debe alcanzar la respuesta. Fuera del prompt, durante la etapa de evaluación, permiten al equipo de ingeniería comprobar si el modelo efectivamente los cumplió. Esta distinción —criterios como instrucción interna versus criterios como métrica externa— se profundizará en las Secciones 6 y 8.

```mermaid
flowchart TD
A[Rol]
B[Objetivo]
C[Contexto]
D[Restricciones]
E[Criterios]
F[Formato]

A --> G[Prompt Profesional]
B --> G
C --> G
D --> G
E --> G
F --> G
G --> H[LLM]
H --> I[Respuesta consistente]
```

---

## Modularidad

Cada bloque cumple una responsabilidad específica.

Esta separación facilita el mantenimiento, el versionado y la reutilización. Una modificación en el formato de salida no debería requerir reescribir el contexto ni alterar el rol asignado al modelo.

Desde la perspectiva del AI Engineering, esta modularidad permite tratar los prompts como artefactos versionables dentro del ciclo de vida de una aplicación. Cada bloque puede evolucionar de manera independiente sin afectar a los demás, siempre que no se introduzcan instrucciones contradictorias entre ellos.

---

## Caso de estudio

Un equipo desarrolla un asistente jurídico para analizar contratos. Inicialmente cada prompt contiene instrucciones mezcladas, ejemplos y reglas de formato en un único bloque de texto.

Tras separar el prompt en componentes reutilizables, el equipo consigue:

- disminuir el esfuerzo de mantenimiento;
- reutilizar bloques entre distintos asistentes;
- simplificar las revisiones;
- controlar mejor los cambios entre versiones.

---

## Buenas prácticas

- Separar responsabilidades dentro del prompt; cada bloque debe tener una función única.
- Documentar el propósito de cada bloque.
- Evitar instrucciones contradictorias entre bloques.
- Mantener un formato consistente entre versiones.

---

## Errores frecuentes

- Mezclar contexto con restricciones en un mismo bloque.
- Duplicar instrucciones en distintos bloques.
- Cambiar múltiples bloques simultáneamente sin evaluación intermedia.
- Diseñar prompts difíciles de mantener porque no tienen estructura visible.

---

## Ideas clave

- Un prompt profesional posee una estructura deliberada compuesta por bloques con funciones diferenciadas.
- La modularidad mejora la mantenibilidad y facilita el versionado.
- Cada componente responde a un objetivo concreto de ingeniería.

---

## Transición hacia la siguiente sección

En la próxima sección estudiaremos el primero de estos bloques en profundidad: el concepto de rol (*role prompting*) y cómo influye en el comportamiento de un modelo dentro de soluciones empresariales.
