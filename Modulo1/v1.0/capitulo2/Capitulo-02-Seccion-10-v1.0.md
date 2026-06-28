# Capítulo 2 --- Sección 10 de 10

# Integrando los conceptos: cómo piensa un Large Language Model

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Comprender un modelo no significa conocer cada una de sus
> ecuaciones. Significa entender cómo interactúan sus componentes para
> producir un comportamiento útil."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Integrar los conceptos desarrollados a lo largo del capítulo.
-   Explicar, a alto nivel, el recorrido completo desde un texto de
    entrada hasta una respuesta generada.
-   Comprender qué elementos pertenecen al modelo y cuáles a la
    arquitectura que lo rodea.
-   Prepararte para estudiar Retrieval-Augmented Generation (RAG) en el
    próximo capítulo.

------------------------------------------------------------------------

# Introducción

En este capítulo recorrimos el funcionamiento interno de un modelo
moderno de lenguaje.

Cada concepto estudiado constituye una pieza de un sistema mucho mayor.

Analizados de forma aislada pueden parecer independientes.

Sin embargo, cuando se integran describen el flujo completo de
funcionamiento de un Large Language Model.

------------------------------------------------------------------------

# El recorrido de una consulta

Cuando un usuario envía una pregunta, el proceso puede resumirse de la
siguiente manera:

1.  El texto se tokeniza.
2.  Cada token se transforma en una representación numérica.
3.  Esa representación se convierte en embeddings.
4.  El Transformer procesa la secuencia utilizando mecanismos de
    atención.
5.  Los parámetros aprendidos durante el entrenamiento permiten estimar
    el siguiente token más probable.
6.  El proceso se repite hasta construir la respuesta completa.

Aunque internamente intervienen miles de millones de operaciones
matemáticas, esta secuencia resume el comportamiento general del
sistema.

``` mermaid
flowchart LR
A[Texto] --> B[Tokens]
B --> C[Embeddings]
C --> D[Transformer]
D --> E[Predicción del siguiente token]
E --> F[Respuesta]
```

------------------------------------------------------------------------

# Lo que el modelo sabe y lo que no sabe

A lo largo del capítulo diferenciamos claramente dos fuentes de
conocimiento.

Por un lado, el conocimiento adquirido durante el entrenamiento y
almacenado en los parámetros del modelo.

Por otro, el contexto suministrado durante cada interacción.

Esta diferencia resulta fundamental.

Un modelo no consulta Internet por sí mismo.

No accede automáticamente a la base documental de una empresa.

Solo puede utilizar la información presente en sus parámetros y en el
contexto recibido durante la inferencia.

Cuando esto no alcanza, es necesario incorporar componentes externos.

Aquí comienza el terreno de la arquitectura.

------------------------------------------------------------------------

# Del modelo al sistema

Uno de los errores más frecuentes consiste en identificar un producto
basado en IA únicamente con el modelo de lenguaje.

En realidad, el modelo representa solo uno de sus componentes.

Un sistema preparado para producción suele incluir además:

-   autenticación;
-   bases de datos;
-   almacenamiento documental;
-   observabilidad;
-   monitoreo;
-   registro de auditoría;
-   mecanismos de recuperación de información;
-   validaciones de negocio;
-   integración con APIs.

La calidad final depende de la interacción entre todos estos elementos.

------------------------------------------------------------------------

# Lo que aprenderemos a continuación

Hasta ahora analizamos el funcionamiento interno del modelo.

Sin embargo, la mayoría de las aplicaciones empresariales necesita
trabajar con información que no formó parte del entrenamiento.

Normativa interna.

Procedimientos.

Contratos.

Historias clínicas.

Expedientes.

Catálogos.

Bases de conocimiento.

¿Cómo puede un modelo responder utilizando esa información sin volver a
entrenarse?

La respuesta conduce directamente al siguiente gran concepto del libro:
**Retrieval-Augmented Generation (RAG)**.

------------------------------------------------------------------------

# Resumen del capítulo

Durante este capítulo aprendimos que:

-   un modelo aprende ajustando parámetros;
-   los datos constituyen la base del aprendizaje;
-   la información debe transformarse en vectores;
-   los embeddings representan significado;
-   los Transformers permiten modelar relaciones complejas mediante
    atención;
-   los LLM son el resultado de entrenar esas arquitecturas a gran
    escala;
-   los modelos procesan tokens dentro de una ventana de contexto
    limitada.

Estos conceptos serán reutilizados constantemente en el resto del libro.

------------------------------------------------------------------------

# Mensaje final

Comprender cómo funciona un Large Language Model permite abandonar la
visión de "caja negra".

A partir de ahora podremos analizar arquitecturas completas y justificar
técnicamente decisiones que van mucho más allá de elegir un proveedor o
escribir un prompt.

Ese es el verdadero objetivo de la Ingeniería de IA.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
