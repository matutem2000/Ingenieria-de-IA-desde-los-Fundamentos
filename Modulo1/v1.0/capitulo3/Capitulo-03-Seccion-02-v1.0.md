# Capítulo 3 --- Sección 02 de 10

# Arquitectura de un sistema RAG

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"RAG no es una llamada a un modelo. Es una arquitectura compuesta por
> múltiples componentes especializados que colaboran para producir una
> respuesta confiable."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los componentes principales de una arquitectura RAG.
-   Seguir el recorrido completo de una consulta.
-   Diferenciar recuperación de información y generación de respuestas.
-   Identificar los puntos donde un arquitecto puede optimizar el
    sistema.

------------------------------------------------------------------------

# Introducción

Una vez comprendido el problema que intenta resolver RAG, el siguiente
paso consiste en analizar cómo funciona internamente.

A diferencia de un chatbot tradicional, un sistema RAG incorpora un
flujo adicional antes de invocar al modelo de lenguaje.

Ese flujo tiene un único objetivo: recuperar el conocimiento más
relevante para responder la consulta del usuario.

------------------------------------------------------------------------

# Componentes principales

Una arquitectura RAG típica está compuesta por los siguientes elementos:

-   Cliente o aplicación consumidora.
-   Motor de orquestación.
-   Modelo de embeddings.
-   Base de datos vectorial.
-   Repositorio documental.
-   Large Language Model.
-   Sistema de observabilidad y monitoreo.

Cada componente cumple una responsabilidad específica.

Separar responsabilidades facilita la evolución, el mantenimiento y la
escalabilidad.

------------------------------------------------------------------------

# Flujo de una consulta

Cuando un usuario realiza una pregunta, el proceso puede resumirse así:

1.  La aplicación recibe la consulta.
2.  La consulta se convierte en un embedding.
3.  Ese embedding se utiliza para buscar documentos similares en la base
    vectorial.
4.  Se recuperan únicamente los fragmentos más relevantes.
5.  Los fragmentos recuperados se incorporan al contexto del modelo.
6.  El LLM genera una respuesta fundamentada en ese contexto.
7.  La respuesta se devuelve al usuario.

``` mermaid
flowchart LR
A[Usuario] --> B[Aplicación]
B --> C[Embedding]
C --> D[Base Vectorial]
D --> E[Fragmentos relevantes]
E --> F[LLM]
F --> G[Respuesta]
```

------------------------------------------------------------------------

# ¿Por qué separar recuperación y generación?

Un error frecuente consiste en pensar que el modelo "busca" documentos.

En realidad, la búsqueda suele estar a cargo de un componente
independiente.

El modelo recibe únicamente el resultado de esa búsqueda.

Esta separación aporta varias ventajas:

-   permite cambiar el modelo sin modificar el repositorio documental;
-   facilita optimizar la recuperación de información;
-   reduce costos de inferencia;
-   mejora la trazabilidad de las respuestas.

Cada componente puede evolucionar de forma independiente.

------------------------------------------------------------------------

# Arquitectura antes que modelo

En proyectos reales es habitual obtener mayores mejoras optimizando la
recuperación que reemplazando el LLM.

Una mala estrategia de recuperación puede enviar contexto irrelevante.

Un contexto irrelevante conduce a respuestas incorrectas, incluso
utilizando un modelo de última generación.

Por el contrario, una recuperación precisa permite que modelos más
pequeños produzcan resultados sorprendentes.

Esta es una de las razones por las cuales RAG se considera un patrón
arquitectónico.

------------------------------------------------------------------------

# Caso de estudio

Dos organizaciones utilizan exactamente el mismo modelo fundacional.

La primera envía manuales completos al modelo en cada consulta.

La segunda recupera únicamente los cinco fragmentos más relacionados
mediante búsqueda semántica.

Aunque ambas utilizan el mismo LLM, la segunda obtiene menor latencia,
menor costo y respuestas más precisas.

La diferencia no reside en el modelo.

Reside en la arquitectura.

------------------------------------------------------------------------

# Ideas clave

-   RAG incorpora una etapa de recuperación previa a la generación.
-   La base vectorial y el LLM cumplen responsabilidades distintas.
-   La calidad de la recuperación condiciona la calidad de la respuesta.
-   La arquitectura completa determina el desempeño del sistema.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos cómo se preparan los documentos
antes de ingresar a una arquitectura RAG, incluyendo particionado
(*chunking*), normalización y generación de embeddings.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
