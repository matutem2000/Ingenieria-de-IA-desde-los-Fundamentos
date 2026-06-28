# Capítulo 3 --- Sección 05 de 10

# Bases de datos vectoriales: donde vive el conocimiento recuperable

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un sistema RAG no busca documentos. Busca proximidad matemática
> entre representaciones semánticas."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es una base de datos vectorial.
-   Entender por qué una base relacional tradicional no resuelve
    eficientemente este problema.
-   Conocer los principios de búsqueda aproximada por vecinos más
    cercanos (ANN).
-   Incorporar criterios arquitectónicos para seleccionar una tecnología
    vectorial.

------------------------------------------------------------------------

# Introducción

Una vez preparados los documentos y generados sus embeddings, surge una
nueva pregunta.

¿Dónde almacenarlos?

Podríamos guardar cada vector en una tabla relacional.

Sin embargo, cuando el repositorio contiene cientos de miles o millones
de documentos, buscar el vector más parecido deja de ser un problema de
almacenamiento y pasa a ser un problema de geometría computacional.

Las bases de datos vectoriales nacieron para resolver precisamente ese
desafío.

------------------------------------------------------------------------

# Del SQL a la similitud

Las bases de datos relacionales fueron diseñadas para responder
preguntas como:

-   ¿Cuál es el cliente con este identificador?
-   ¿Qué facturas pertenecen a este período?
-   ¿Qué pedidos superan determinado importe?

Todas ellas pueden responderse mediante igualdad, rangos o índices
clásicos.

En cambio, un sistema RAG necesita responder otra pregunta:

> ¿Qué documentos son semánticamente más parecidos a esta consulta?

Aquí ya no buscamos igualdad.

Buscamos cercanía en un espacio vectorial.

------------------------------------------------------------------------

# ¿Qué almacena una base vectorial?

Cada registro suele contener:

-   el embedding;
-   el identificador del documento;
-   el texto o referencia al contenido;
-   metadatos;
-   información necesaria para indexación.

El embedding constituye el elemento central.

Los demás datos permiten recuperar y contextualizar el contenido
original.

------------------------------------------------------------------------

# Búsqueda por similitud

Comparar un vector contra millones de registros calculando todas las
distancias sería demasiado costoso.

Por ello la mayoría de las bases vectoriales implementa algoritmos de
**Approximate Nearest Neighbor (ANN)**.

Estos algoritmos sacrifican una pequeña cantidad de precisión para
obtener mejoras muy significativas en tiempo de respuesta.

En aplicaciones empresariales este intercambio suele resultar aceptable.

------------------------------------------------------------------------

# Índices especializados

Al igual que una base relacional utiliza índices B-Tree o Hash, las
bases vectoriales emplean estructuras específicas para espacios de alta
dimensión.

Entre las más utilizadas se encuentran:

-   HNSW (Hierarchical Navigable Small World);
-   IVF (Inverted File Index);
-   PQ (Product Quantization).

Como arquitecto no es imprescindible memorizar cada algoritmo, pero sí
comprender que la estrategia de indexación influye directamente sobre:

-   latencia;
-   consumo de memoria;
-   precisión de la recuperación;
-   costo operativo.

------------------------------------------------------------------------

# Tecnologías disponibles

Actualmente existen múltiples alternativas.

Algunas de las más utilizadas son:

-   **FAISS**, biblioteca optimizada para búsquedas vectoriales locales.
-   **Qdrant**, base vectorial orientada a aplicaciones modernas.
-   **Milvus**, diseñada para grandes volúmenes de datos.
-   **Weaviate**, con capacidades adicionales de búsqueda híbrida.
-   **pgvector**, extensión para PostgreSQL que incorpora almacenamiento
    y búsqueda vectorial.

La decisión depende del contexto del proyecto.

No existe una opción universalmente superior.

------------------------------------------------------------------------

# Criterios de selección

Antes de elegir una tecnología conviene analizar:

-   volumen esperado de documentos;
-   frecuencia de actualización;
-   necesidad de alta disponibilidad;
-   integración con la infraestructura existente;
-   costos de operación;
-   experiencia del equipo;
-   requerimientos regulatorios.

En muchos proyectos pequeños, una base relacional con soporte vectorial
puede ser suficiente.

En plataformas corporativas de gran escala suele justificarse una
solución especializada.

------------------------------------------------------------------------

# Caso de estudio

Una organización comienza con cincuenta mil documentos utilizando
PostgreSQL y una extensión vectorial.

Dos años después supera los treinta millones de fragmentos indexados.

Las búsquedas siguen siendo correctas, pero la latencia deja de cumplir
los objetivos del negocio.

El problema no radica en el modelo de IA.

La arquitectura de almacenamiento ya no resulta adecuada para la nueva
escala.

La migración hacia una base vectorial especializada se convierte en una
decisión arquitectónica, no funcional.

------------------------------------------------------------------------

# Ideas clave

-   Una base vectorial almacena representaciones semánticas, no
    únicamente texto.
-   La búsqueda por similitud requiere algoritmos diferentes a los
    utilizados por SQL tradicional.
-   La estrategia de indexación influye en rendimiento y precisión.
-   La tecnología elegida debe responder a los requerimientos del
    proyecto y no a tendencias del mercado.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la búsqueda híbrida, combinando
recuperación semántica y búsqueda léxica para mejorar la precisión de
sistemas RAG en escenarios empresariales.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
