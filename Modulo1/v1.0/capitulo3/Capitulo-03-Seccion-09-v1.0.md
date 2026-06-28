# Capítulo 3 --- Sección 09 de 10

# RAG en producción: patrones arquitectónicos para sistemas empresariales

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un prototipo demuestra una idea. Una arquitectura preparada para
> producción demuestra que esa idea puede sostener un negocio."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los principales desafíos de desplegar un sistema RAG en
    producción.
-   Conocer patrones arquitectónicos utilizados en entornos
    empresariales.
-   Entender el papel de la observabilidad, las cachés y la
    actualización documental.
-   Incorporar criterios de diseño orientados a escalabilidad y
    mantenibilidad.

------------------------------------------------------------------------

# Introducción

Construir un prototipo de RAG suele requerir pocos componentes.

Construir un servicio utilizado por cientos o miles de personas es un
desafío completamente distinto.

A medida que aumenta el uso aparecen nuevos requisitos:

-   mayor volumen documental;
-   usuarios concurrentes;
-   restricciones de tiempo de respuesta;
-   control de costos;
-   auditoría;
-   alta disponibilidad;
-   seguridad.

La arquitectura debe evolucionar para responder a estas necesidades.

------------------------------------------------------------------------

# Separación por responsabilidades

Una buena práctica consiste en desacoplar los componentes principales
del sistema.

En una arquitectura típica encontramos:

-   servicio de ingestión documental;
-   servicio de generación de embeddings;
-   base vectorial;
-   servicio de recuperación;
-   orquestador RAG;
-   Large Language Model;
-   servicios de monitoreo y observabilidad.

Cada componente puede escalar y evolucionar de manera independiente.

------------------------------------------------------------------------

# Actualización del conocimiento

El conocimiento corporativo cambia continuamente.

Nuevos procedimientos reemplazan versiones anteriores.

Se incorporan documentos.

Otros dejan de estar vigentes.

Una arquitectura madura debe permitir:

-   indexación incremental;
-   reindexación completa cuando sea necesario;
-   versionado documental;
-   eliminación segura de información obsoleta;
-   trazabilidad de cada actualización.

Actualizar un repositorio documental no debería requerir detener todo el
sistema.

------------------------------------------------------------------------

# Estrategias de caché

Muchas consultas se repiten.

Volver a ejecutar todo el pipeline para cada solicitud puede incrementar
costos y latencia.

Dependiendo del dominio pueden incorporarse distintos niveles de caché:

-   resultados de búsqueda;
-   embeddings de consultas frecuentes;
-   respuestas previamente validadas;
-   documentos recientemente recuperados.

La caché no reemplaza al RAG.

Complementa su funcionamiento.

------------------------------------------------------------------------

# Observabilidad

Cuando una respuesta resulta incorrecta, el arquitecto necesita saber
por qué.

Para ello conviene registrar información como:

-   consulta original;
-   documentos recuperados;
-   puntuaciones de recuperación;
-   tiempo consumido en cada etapa;
-   modelo utilizado;
-   cantidad de tokens;
-   costo estimado;
-   respuesta final.

Estos registros permiten diagnosticar problemas y mejorar el sistema de
forma continua.

------------------------------------------------------------------------

# Escalabilidad

No todos los componentes crecen al mismo ritmo.

La base vectorial puede requerir más memoria.

El servicio de embeddings puede necesitar aceleración mediante GPU.

El LLM puede ejecutarse localmente o consumirse como servicio externo.

Diseñar componentes independientes facilita escalar únicamente aquello
que realmente constituye un cuello de botella.

------------------------------------------------------------------------

# Seguridad y gobierno

Los sistemas empresariales deben respetar las mismas políticas que el
resto de la organización.

Algunas consideraciones habituales incluyen:

-   autenticación y autorización;
-   control de acceso por documento;
-   cifrado en tránsito y en reposo;
-   auditoría de consultas;
-   protección de información confidencial;
-   cumplimiento normativo.

La búsqueda semántica nunca debe ignorar las reglas de seguridad
existentes.

Un usuario solo debería recuperar documentos para los cuales posee
autorización.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR
A[Repositorio documental] --> B[Pipeline de ingestión]
B --> C[Embeddings]
C --> D[Base vectorial]

U[Usuario] --> O[Orquestador RAG]
O --> D
D --> O
O --> L[LLM]
L --> O
O --> R[Respuesta]

O --> M[Logs y Métricas]
```

Este diagrama resume una arquitectura desacoplada, donde cada componente
posee una responsabilidad claramente definida.

------------------------------------------------------------------------

# Caso de estudio

Una empresa implementa un asistente interno para más de dos mil
empleados.

Durante las primeras semanas el sistema responde correctamente.

Con el tiempo, la incorporación diaria de nuevos procedimientos comienza
a degradar la experiencia porque la indexación solo se ejecuta una vez
por semana.

El problema no reside en el LLM ni en la base vectorial.

La arquitectura de ingestión ya no acompaña el ritmo de actualización
del negocio.

La solución consiste en incorporar un pipeline incremental que procese
únicamente los documentos modificados.

------------------------------------------------------------------------

# Ideas clave

-   Un sistema RAG en producción requiere mucho más que un LLM y una
    base vectorial.
-   La observabilidad es indispensable para diagnosticar problemas.
-   La actualización documental debe formar parte del diseño
    arquitectónico.
-   Escalabilidad, seguridad y mantenibilidad son requisitos de primer
    nivel.

------------------------------------------------------------------------

## Próxima sección

En la última sección del capítulo integraremos todos los conceptos
desarrollados y construiremos una visión completa de una arquitectura
RAG moderna, preparando el camino para el estudio de agentes de IA y
sistemas compuestos.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
