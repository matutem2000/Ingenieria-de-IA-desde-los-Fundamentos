# Capítulo 2 --- Sección 09 de 10

# La ventana de contexto: el límite de la memoria inmediata

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un modelo puede haber aprendido sobre millones de documentos y, sin
> embargo, ser incapaz de utilizar un documento que no entra en su
> ventana de contexto."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es la ventana de contexto (*Context Window*).
-   Diferenciar conocimiento entrenado de contexto suministrado durante
    la inferencia.
-   Entender cómo el tamaño del contexto afecta la calidad, el
    rendimiento y el costo.
-   Comprender por qué esta limitación impulsó el desarrollo de
    arquitecturas como RAG.

------------------------------------------------------------------------

# Introducción

Una de las preguntas más frecuentes al comenzar a trabajar con modelos
de lenguaje es:

> "¿Por qué no puedo enviar toda la documentación de mi empresa en una
> única consulta?"

La respuesta está relacionada con uno de los conceptos más importantes
de los Large Language Models: la **ventana de contexto**.

Aunque un modelo haya sido entrenado con enormes cantidades de
información, durante cada interacción solo puede procesar una cantidad
limitada de tokens.

Comprender esta restricción resulta esencial para diseñar aplicaciones
eficientes.

------------------------------------------------------------------------

# ¿Qué es la ventana de contexto?

La ventana de contexto representa la cantidad máxima de información que
un modelo puede considerar simultáneamente para generar una respuesta.

Dentro de esa ventana conviven distintos elementos:

-   las instrucciones del sistema;
-   el historial de la conversación;
-   la consulta del usuario;
-   documentos adicionales;
-   herramientas utilizadas por el modelo;
-   la respuesta que está generando.

Todos ellos compiten por el mismo espacio.

------------------------------------------------------------------------

# Conocimiento permanente versus memoria temporal

Es importante distinguir dos conceptos.

El **conocimiento entrenado** forma parte de los parámetros del modelo y
permanece constante durante la inferencia.

El **contexto**, en cambio, existe únicamente durante la conversación
actual.

Una analogía útil consiste en comparar un profesional con una reunión de
trabajo.

La experiencia acumulada durante años representa su conocimiento
permanente.

Los documentos distribuidos al comienzo de la reunión constituyen el
contexto temporal utilizado para resolver una tarea específica.

Cuando la reunión termina, esos documentos dejan de formar parte del
contexto inmediato.

------------------------------------------------------------------------

# ¿Qué ocurre cuando el contexto es demasiado grande?

Cuando la información supera el tamaño permitido aparecen distintas
alternativas:

-   eliminar parte del historial;
-   resumir conversaciones anteriores;
-   dividir documentos en fragmentos;
-   recuperar únicamente la información relevante.

Las últimas dos estrategias dieron origen a arquitecturas modernas como
**Retrieval-Augmented Generation (RAG)**.

En lugar de enviar toda la base documental, el sistema recupera solo los
fragmentos más relacionados con la consulta.

------------------------------------------------------------------------

# Arquitectura versus modelo

En muchos proyectos el problema no consiste en disponer de un modelo más
grande.

Consiste en enviar información innecesaria.

Un diseño arquitectónico adecuado suele producir mejores resultados que
incrementar indiscriminadamente el tamaño del contexto.

Esto explica por qué sistemas relativamente pequeños pueden superar a
soluciones mucho más costosas cuando la recuperación de información está
correctamente diseñada.

------------------------------------------------------------------------

# Caso real

Una empresa desea consultar un repositorio con veinte mil procedimientos
internos.

La primera propuesta consiste en incluir todos los documentos en cada
consulta.

Los costos y la latencia resultan inaceptables.

La solución finalmente implementada utiliza embeddings para localizar
los cinco documentos más relevantes y solo esos fragmentos se incorporan
al contexto del modelo.

El resultado mejora simultáneamente la precisión, el rendimiento y el
costo operativo.

------------------------------------------------------------------------

# Ideas clave

-   La ventana de contexto limita la cantidad de información procesable
    en una interacción.
-   El conocimiento entrenado y el contexto son conceptos diferentes.
-   Un mayor contexto no siempre implica mejores respuestas.
-   La arquitectura determina qué información debe enviarse realmente al
    modelo.

------------------------------------------------------------------------

## Próxima sección

En la última sección del capítulo integraremos todos los conceptos
estudiados y construiremos una visión completa del funcionamiento
interno de un Large Language Model, preparando el terreno para los
capítulos dedicados a RAG y arquitectura de sistemas inteligentes.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
