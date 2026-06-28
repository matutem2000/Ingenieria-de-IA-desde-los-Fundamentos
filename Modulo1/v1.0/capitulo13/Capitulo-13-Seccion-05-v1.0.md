# Capitulo-13-Seccion-05-v1.0

# Capítulo 13 --- Laboratorios de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"Un modelo aislado responde con lo que conoce; un modelo conectado al
> conocimiento correcto responde con lo que la organización necesita."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Comprender el valor de incorporar contexto externo a un Large
    Language Model (LLM).
-   Observar las diferencias entre responder con conocimiento propio y
    responder utilizando información recuperada.
-   Introducir los principios fundamentales de Retrieval-Augmented
    Generation (RAG) mediante una práctica controlada.
-   Analizar cómo el contexto modifica la calidad de las respuestas.

------------------------------------------------------------------------

# Laboratorio 3 --- Incorporando contexto mediante RAG

## Objetivo

Comparar el comportamiento de un modelo respondiendo una consulta con y
sin acceso a documentación específica de una organización.

## Nivel

Intermedio.

## Tiempo estimado

60 minutos.

## Prerrequisitos

-   Laboratorios anteriores completados.
-   Modelo local operativo.
-   Conjunto de documentos de prueba.
-   Herramienta para construir un índice vectorial o un mecanismo simple
    de recuperación.

------------------------------------------------------------------------

# Escenario

Una empresa dispone de un manual interno de procedimientos.

El objetivo consiste en responder consultas de los empleados utilizando
únicamente la información oficial disponible.

Se realizará una comparación entre dos escenarios:

1.  El modelo responde utilizando únicamente el conocimiento adquirido
    durante el entrenamiento.
2.  El modelo responde utilizando información recuperada desde la
    documentación corporativa.

``` mermaid
flowchart LR
A[Consulta] --> B{¿Existe RAG?}
B -->|No| C[LLM]
B -->|Sí| D[Recuperación documental]
D --> E[Contexto]
E --> C
C --> F[Respuesta]
```

------------------------------------------------------------------------

# Desarrollo

1.  Seleccionar un conjunto reducido de documentos.
2.  Construir el mecanismo de recuperación.
3.  Formular una consulta cuya respuesta se encuentre en los documentos.
4.  Ejecutar la consulta sin contexto adicional.
5.  Repetir la misma consulta utilizando RAG.
6.  Comparar precisión, referencias y nivel de detalle.
7.  Registrar las diferencias observadas.

------------------------------------------------------------------------

# Validación

El laboratorio se considera satisfactorio cuando el lector puede
demostrar que la incorporación de contexto mejora la calidad de la
respuesta y reduce la probabilidad de alucinaciones.

------------------------------------------------------------------------

# Preguntas para reflexionar

-   ¿Qué información pudo responder correctamente únicamente gracias al
    contexto?
-   ¿Cómo cambió el nivel de precisión?
-   ¿Qué ocurriría si los documentos estuvieran desactualizados?
-   ¿Qué impacto tendría la calidad de los embeddings sobre la
    recuperación?

------------------------------------------------------------------------

# Desafíos opcionales

-   Repetir la prueba utilizando distintos tamaños de contexto.
-   Comparar diferentes estrategias de recuperación.
-   Medir el impacto sobre el tiempo de respuesta.
-   Incorporar documentos contradictorios y analizar el comportamiento
    del modelo.

------------------------------------------------------------------------

# Ideas clave

-   El contexto constituye uno de los factores que mayor influencia
    ejerce sobre la calidad de una respuesta.
-   RAG no reemplaza al modelo; amplía la información disponible durante
    la inferencia.
-   La calidad documental resulta tan importante como la calidad del
    modelo.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima práctica analizaremos cómo evaluar objetivamente las
respuestas generadas por un modelo mediante métricas y criterios
reproducibles, evitando depender únicamente de apreciaciones subjetivas.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
