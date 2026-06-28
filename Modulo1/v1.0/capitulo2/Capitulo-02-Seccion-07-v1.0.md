# Capítulo 2 --- Sección 07 de 10

# Del Transformer al Large Language Model

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un Transformer es una arquitectura. Un Large Language Model es el
> resultado de entrenar esa arquitectura con enormes cantidades de
> datos."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Diferenciar arquitectura de modelo entrenado.
-   Comprender qué es el preentrenamiento (*pretraining*).
-   Entender el propósito del ajuste fino (*fine-tuning*).
-   Explicar por qué un LLM puede resolver tareas para las que nunca fue
    programado explícitamente.

------------------------------------------------------------------------

# Introducción

En la sección anterior estudiamos la arquitectura Transformer.

Sin embargo, disponer de una buena arquitectura no basta para construir
un modelo útil.

Un Transformer recién comienza a adquirir capacidades cuando atraviesa
un largo proceso de entrenamiento utilizando cantidades masivas de
información.

Ese proceso es el que da origen a un **Large Language Model (LLM)**.

------------------------------------------------------------------------

# ¿Qué significa "Large"?

El término *Large* no hace referencia únicamente a la cantidad de
parámetros.

También involucra:

-   enormes volúmenes de datos de entrenamiento;
-   grandes capacidades de cómputo;
-   extensos tiempos de entrenamiento;
-   una capacidad creciente para generalizar conocimientos.

El objetivo no es memorizar documentos, sino aprender patrones
estadísticos del lenguaje.

------------------------------------------------------------------------

# El preentrenamiento

Durante el preentrenamiento el modelo procesa cantidades gigantescas de
texto.

Su tarea principal suele consistir en predecir cuál debería ser el
siguiente token de una secuencia.

Aunque esta tarea parezca simple, obliga al modelo a capturar relaciones
gramaticales, semánticas y contextuales.

Con el tiempo desarrolla representaciones internas que luego podrán
reutilizarse para una enorme variedad de aplicaciones.

------------------------------------------------------------------------

# El ajuste fino

Una vez finalizado el preentrenamiento, el modelo puede adaptarse a
necesidades concretas.

Este proceso recibe el nombre de **fine-tuning**.

Por ejemplo:

-   responder consultas médicas;
-   analizar contratos;
-   asistir a desarrolladores;
-   clasificar documentos legales.

El objetivo ya no es aprender lenguaje general, sino especializar el
comportamiento para un dominio determinado.

------------------------------------------------------------------------

# Capacidades emergentes

Uno de los fenómenos más interesantes de los LLM modernos es la
aparición de capacidades que no fueron programadas explícitamente.

Un modelo entrenado para predecir el siguiente token puede:

-   resumir textos;
-   traducir idiomas;
-   generar código;
-   responder preguntas;
-   explicar conceptos.

Estas capacidades emergen como consecuencia del entrenamiento y de la
escala del modelo.

No corresponden a módulos independientes desarrollados por un equipo de
ingeniería.

------------------------------------------------------------------------

# Caso real

Una organización adopta un modelo fundacional para asistir a sus
analistas.

Sin modificar la arquitectura, el mismo modelo se utiliza para resumir
expedientes, redactar correos, responder preguntas sobre normativa y
colaborar con desarrolladores.

La diferencia no reside únicamente en el modelo.

Reside en el contexto, los datos y la forma en que se integra dentro de
la arquitectura empresarial.

------------------------------------------------------------------------

# Ideas clave

-   Transformer y LLM no son sinónimos.
-   El preentrenamiento construye conocimiento general.
-   El ajuste fino adapta ese conocimiento a un dominio específico.
-   Muchas capacidades aparecen como resultado de la escala del
    entrenamiento.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos la **tokenización**, comprenderemos
qué es un token y por qué este concepto resulta esencial para entender
costos, ventanas de contexto y rendimiento de los modelos modernos.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
