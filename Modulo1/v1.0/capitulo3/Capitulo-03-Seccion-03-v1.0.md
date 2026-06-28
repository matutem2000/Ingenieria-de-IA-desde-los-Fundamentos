# Capítulo 3 --- Sección 03 de 10

# Preparación de documentos: la base de un RAG de calidad

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La calidad de un sistema RAG comienza mucho antes de la primera
> consulta. Comienza en la preparación del conocimiento."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué la preparación documental es una etapa crítica.
-   Entender el concepto de *chunking* y su impacto en la recuperación.
-   Conocer el rol de los metadatos dentro de una arquitectura RAG.
-   Identificar buenas prácticas para construir una base documental
    escalable.

------------------------------------------------------------------------

# Introducción

Cuando se observa un sistema RAG funcionando, suele parecer que todo
comienza con la pregunta del usuario.

En realidad, una parte sustancial del trabajo ocurre mucho antes.

Antes de responder una sola consulta es necesario transformar el
conocimiento de la organización en un formato que pueda ser recuperado
eficientemente.

Esta etapa recibe distintos nombres según la herramienta utilizada, pero
conceptualmente constituye el proceso de **ingestión y preparación
documental**.

La calidad de este proceso condiciona directamente la calidad de las
respuestas futuras.

------------------------------------------------------------------------

# La diversidad de las fuentes

En un entorno empresarial la información rara vez se encuentra
organizada de manera uniforme.

Es habitual encontrar:

-   documentos PDF;
-   manuales técnicos;
-   archivos de Office;
-   páginas wiki;
-   correos electrónicos;
-   bases de conocimiento;
-   registros de sistemas;
-   documentación en Markdown;
-   código fuente;
-   procedimientos internos.

Cada formato requiere mecanismos específicos de extracción y
normalización.

Antes de pensar en modelos, el arquitecto debe garantizar que el
contenido pueda ser procesado de forma consistente.

------------------------------------------------------------------------

# Normalización

La normalización consiste en convertir documentos heterogéneos en una
representación uniforme.

Dependiendo del proyecto, esto puede implicar:

-   eliminar encabezados y pies de página repetitivos;
-   corregir errores de codificación;
-   unificar formatos de fecha;
-   preservar tablas relevantes;
-   eliminar contenido duplicado;
-   extraer texto de documentos escaneados mediante OCR.

No se trata de "limpiar texto".

Se trata de preservar el conocimiento realmente útil para el sistema.

------------------------------------------------------------------------

# El problema del tamaño

Una vez normalizados los documentos aparece un nuevo desafío.

Los modelos de lenguaje trabajan con ventanas de contexto limitadas.

Enviar documentos completos rara vez constituye una buena estrategia.

Por ello surge el concepto de **chunking**.

------------------------------------------------------------------------

# ¿Qué es el chunking?

El *chunking* consiste en dividir un documento en fragmentos más
pequeños denominados **chunks**.

Cada fragmento debe conservar suficiente contexto para mantener su
significado, pero también debe ser lo bastante compacto como para
recuperarse eficientemente.

El objetivo no es partir un archivo cada determinada cantidad de
caracteres.

El objetivo es preservar unidades de conocimiento coherentes.

Por ejemplo:

-   una sección de un manual;
-   un procedimiento completo;
-   un artículo de una normativa;
-   una función documentada;
-   un apartado de una política interna.

------------------------------------------------------------------------

# ¿Por qué el chunking es tan importante?

Supongamos un procedimiento compuesto por diez pasos.

Si el algoritmo divide el texto exactamente en la mitad, es posible que
los primeros cinco pasos queden en un fragmento y los restantes en otro.

Una consulta relacionada con el procedimiento podría recuperar
únicamente la primera mitad.

La respuesta sería técnicamente correcta, pero estaría incompleta.

Este ejemplo muestra que el chunking no es un problema de longitud.

Es un problema de diseño del conocimiento.

------------------------------------------------------------------------

# El papel de los metadatos

Cada fragmento puede enriquecerse con información adicional.

Estos datos reciben el nombre de **metadatos**.

Algunos ejemplos son:

-   autor;
-   fecha de creación;
-   versión;
-   área responsable;
-   tipo de documento;
-   clasificación de seguridad;
-   idioma;
-   sistema de origen.

Los metadatos permiten aplicar filtros antes o después de la búsqueda
semántica.

Por ejemplo:

-   recuperar únicamente documentos vigentes;
-   limitar resultados a una determinada unidad organizativa;
-   excluir versiones obsoletas;
-   restringir información confidencial.

Un sistema RAG empresarial rara vez funciona únicamente con similitud
vectorial.

Los metadatos forman parte de la estrategia de recuperación.

------------------------------------------------------------------------

# Pipeline de preparación documental

Una arquitectura típica de ingestión puede representarse de la siguiente
manera:

``` mermaid
flowchart LR
A[Repositorio documental] --> B[Extracción]
B --> C[Normalización]
C --> D[Chunking]
D --> E[Metadatos]
E --> F[Embeddings]
F --> G[Base vectorial]
```

Obsérvese que el modelo de lenguaje todavía no participa.

Todo este trabajo ocurre antes de la primera consulta.

------------------------------------------------------------------------

# Caso de estudio

Una empresa incorpora diez años de documentación técnica a su plataforma
RAG.

Durante las pruebas iniciales las respuestas son inconsistentes.

El problema no reside en el modelo ni en la base vectorial.

Los documentos fueron divididos cada mil caracteres sin respetar
títulos, subtítulos ni límites de sección.

Al redefinir el chunking utilizando la estructura lógica de los
documentos y agregando metadatos sobre versión y área responsable, la
precisión mejora de forma significativa sin modificar el LLM.

La mejora provino de la arquitectura de ingestión.

------------------------------------------------------------------------

# Buenas prácticas

Al diseñar el proceso de preparación documental conviene considerar los
siguientes principios:

-   preservar el significado de cada fragmento;
-   evitar duplicados innecesarios;
-   mantener trazabilidad hacia el documento original;
-   enriquecer los chunks con metadatos útiles;
-   automatizar la actualización del repositorio;
-   versionar el conocimiento cuando corresponda.

Estas prácticas facilitan el mantenimiento del sistema y mejoran la
calidad de la recuperación.

------------------------------------------------------------------------

# Ideas clave

-   Un sistema RAG comienza con la preparación del conocimiento.
-   El chunking determina qué información podrá recuperarse
    posteriormente.
-   Los metadatos complementan la búsqueda semántica.
-   La calidad de la ingestión condiciona la calidad de todo el sistema.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos cómo se generan los embeddings para
cada fragmento y por qué la elección del modelo de embeddings puede
tener tanto impacto como la elección del propio LLM.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
