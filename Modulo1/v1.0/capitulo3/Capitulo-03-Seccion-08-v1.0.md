# Capítulo 3 --- Sección 08 de 10

# Evaluación de sistemas RAG: medir antes de confiar

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"No se puede mejorar aquello que no se mide. En un sistema RAG,
> evaluar es tan importante como recuperar y generar."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué evaluar un sistema RAG requiere métricas
    específicas.
-   Diferenciar métricas de recuperación y métricas de generación.
-   Conocer indicadores como Recall@K, Precision@K, MRR y nDCG.
-   Diseñar una estrategia de evaluación continua para entornos
    productivos.

------------------------------------------------------------------------

# Introducción

Un error frecuente consiste en evaluar un sistema RAG únicamente
preguntando si "la respuesta parece correcta".

Ese criterio resulta insuficiente.

Una respuesta correcta puede haberse obtenido por casualidad.

Una respuesta incorrecta puede deberse a un problema de recuperación y
no del LLM.

Para mejorar un sistema es necesario identificar qué componente está
fallando.

Por ello la evaluación debe analizar el pipeline completo.

------------------------------------------------------------------------

# Dos niveles de evaluación

En términos generales conviene separar la evaluación en dos grandes
etapas.

**Recuperación**

Determina si el sistema encontró los documentos adecuados.

**Generación**

Determina si el modelo utilizó correctamente esos documentos para
construir la respuesta.

Confundir ambos niveles suele conducir a diagnósticos incorrectos.

------------------------------------------------------------------------

# Métricas de recuperación

## Recall@K

Indica si los documentos relevantes aparecen entre los primeros **K**
resultados recuperados.

Un Recall@10 elevado significa que el sistema encuentra la información
necesaria dentro de los diez primeros documentos.

------------------------------------------------------------------------

## Precision@K

Mide qué proporción de los documentos recuperados realmente resulta
relevante.

Una precisión baja implica que el LLM recibirá mucho contexto
innecesario.

------------------------------------------------------------------------

## Mean Reciprocal Rank (MRR)

Evalúa la posición del primer documento relevante.

Mientras más arriba aparezca, mayor será el valor de la métrica.

------------------------------------------------------------------------

## nDCG

La métrica **Normalized Discounted Cumulative Gain** considera tanto la
relevancia como el orden de los documentos recuperados.

Resulta especialmente útil cuando existen distintos niveles de
relevancia.

------------------------------------------------------------------------

# Evaluando la generación

Una recuperación excelente no garantiza una buena respuesta.

También es necesario analizar si el modelo:

-   responde la pregunta planteada;
-   utiliza correctamente el contexto recuperado;
-   evita inventar información;
-   cita las fuentes cuando corresponde;
-   mantiene coherencia y completitud.

Estas evaluaciones pueden realizarse mediante expertos humanos,
conjuntos de referencia o modelos utilizados como evaluadores.

------------------------------------------------------------------------

# Construyendo un conjunto de pruebas

Una buena evaluación requiere consultas representativas.

Conviene incluir:

-   preguntas frecuentes;
-   consultas ambiguas;
-   casos límite;
-   preguntas sin respuesta;
-   documentos desactualizados;
-   terminología específica del dominio.

Cuanto más representativo sea el conjunto de pruebas, mayor confianza
ofrecerán los resultados.

------------------------------------------------------------------------

# Evaluación continua

Los sistemas RAG evolucionan constantemente.

Cambian los documentos.

Cambian los modelos.

Cambian las consultas de los usuarios.

Por ello la evaluación no debe ejecutarse una sola vez antes del
despliegue.

Debe incorporarse al ciclo de vida del sistema.

Una estrategia habitual consiste en medir automáticamente los
indicadores después de cada actualización importante del repositorio
documental o del pipeline de recuperación.

------------------------------------------------------------------------

# Caso de estudio

Un equipo reemplaza su modelo de embeddings esperando mejorar la calidad
de las respuestas.

Las pruebas muestran que el LLM produce respuestas similares a las
anteriores.

Sin embargo, las métricas revelan que el Recall@10 aumentó un 18 % y el
MRR mejoró significativamente.

El cambio todavía no resulta evidente para los usuarios, pero la
arquitectura recupera mejor la información y ofrece una base más sólida
para futuras optimizaciones.

Sin mediciones objetivas, esta mejora habría pasado inadvertida.

------------------------------------------------------------------------

# Ideas clave

-   Recuperación y generación deben evaluarse por separado.
-   Las métricas permiten localizar el origen de los problemas.
-   La evaluación debe utilizar consultas representativas del negocio.
-   Medir continuamente forma parte del mantenimiento de un sistema RAG.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos los principales patrones
arquitectónicos para desplegar sistemas RAG en producción, incluyendo
escalabilidad, cachés, actualización documental y observabilidad.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
