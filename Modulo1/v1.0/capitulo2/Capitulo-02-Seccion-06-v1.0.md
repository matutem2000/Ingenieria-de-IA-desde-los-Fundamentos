# Capítulo 2 --- Sección 06 de 10

# Redes neuronales, atención y el nacimiento de los Transformers

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Los grandes modelos de lenguaje no aparecieron por un incremento
> gradual de potencia de cómputo. Surgieron gracias a un cambio de
> arquitectura."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender la evolución desde las redes neuronales clásicas hacia
    los Transformers.
-   Entender el concepto de atención (*Attention*) desde una perspectiva
    ingenieril.
-   Identificar por qué esta arquitectura permitió construir los Large
    Language Models.
-   Relacionar estos conceptos con las decisiones arquitectónicas que
    veremos más adelante.

------------------------------------------------------------------------

# Introducción

Hasta aquí vimos cómo un modelo aprende a partir de datos y cómo ese
aprendizaje queda distribuido entre millones de parámetros.

La siguiente pregunta es inevitable.

¿Cómo puede un modelo procesar textos completos, establecer relaciones
entre palabras separadas por cientos de posiciones y generar respuestas
coherentes?

Durante muchos años esa fue una de las principales limitaciones de las
arquitecturas existentes.

La solución llegó con un cambio conceptual que modificó el rumbo de la
Inteligencia Artificial.

------------------------------------------------------------------------

# Antes de los Transformers

Las primeras redes neuronales aplicadas al procesamiento de lenguaje
trabajaban de manera secuencial.

Procesaban una palabra tras otra.

Este enfoque presentaba dos problemas importantes.

El primero era el rendimiento.

La naturaleza secuencial impedía aprovechar completamente el
procesamiento paralelo del hardware moderno.

El segundo era la memoria.

A medida que los textos crecían, el modelo tenía dificultades para
mantener información relevante sobre elementos que habían aparecido
muchas posiciones antes.

En consecuencia, comprender documentos extensos resultaba complejo.

------------------------------------------------------------------------

# La idea de atención

La innovación consistió en permitir que el modelo evaluara qué partes
del texto resultaban relevantes para interpretar cada palabra.

En lugar de recordar únicamente el elemento inmediatamente anterior, el
modelo podía asignar distintos niveles de importancia a múltiples
posiciones del contexto.

Ese mecanismo recibió el nombre de **atención** (*Attention*).

No implica conciencia ni comprensión.

Representa un procedimiento matemático para ponderar relaciones entre
los elementos de una secuencia.

------------------------------------------------------------------------

# Una analogía

Imaginemos una reunión con veinte participantes.

Mientras una persona habla, no prestamos la misma atención a todos los
presentes.

Según el tema, algunas intervenciones adquieren mayor relevancia que
otras.

Nuestro foco cambia continuamente.

El mecanismo de atención persigue un objetivo similar.

Permite que el modelo determine qué información merece mayor peso para
resolver la tarea actual.

La analogía describe la idea general, aunque el cálculo real sea
completamente matemático.

------------------------------------------------------------------------

# Los Transformers

La arquitectura conocida como **Transformer** incorporó el mecanismo de
atención como componente central.

Esto permitió procesar secuencias completas de forma paralela, mejorar
el aprovechamiento del hardware y capturar relaciones complejas entre
palabras alejadas dentro de un mismo texto.

A partir de este cambio comenzaron a entrenarse modelos con cantidades
de datos y parámetros impensadas pocos años antes.

Los Large Language Models modernos descienden directamente de esta
arquitectura.

------------------------------------------------------------------------

``` mermaid
flowchart LR
A[Texto de entrada] --> B[Mecanismo de Atención]
B --> C[Representaciones enriquecidas]
C --> D[Capas Transformer]
D --> E[Predicción]
```

------------------------------------------------------------------------

# ¿Por qué esto cambió la industria?

La arquitectura Transformer no mejoró únicamente el procesamiento del
lenguaje.

También demostró ser efectiva para imágenes, audio, código fuente y
otros dominios.

Esto impulsó el desarrollo de modelos fundacionales reutilizables para
múltiples tareas.

El foco dejó de estar en construir un modelo para cada problema y pasó a
adaptarlos mediante diferentes estrategias.

------------------------------------------------------------------------

# Ideas clave

-   Los Transformers sustituyeron limitaciones de arquitecturas
    anteriores.
-   La atención permite ponderar relaciones entre distintos elementos
    del contexto.
-   Los LLM modernos se basan en esta arquitectura.
-   Comprender estos principios resulta más importante que memorizar
    implementaciones específicas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos cómo un Transformer entrenado
termina convirtiéndose en un **Large Language Model** y por qué estos
modelos son capaces de realizar tareas que nunca fueron programadas
explícitamente.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
