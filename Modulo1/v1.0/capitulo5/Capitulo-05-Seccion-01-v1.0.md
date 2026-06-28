# Capítulo 5 --- Sección 01 de 10

# Plataformas de IA: del prototipo a la capacidad organizacional

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Entrenar un modelo puede llevar semanas. Construir una plataforma
> capaz de operar cientos de modelos durante años constituye un desafío
> de ingeniería completamente diferente."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es una plataforma de IA desde una perspectiva
    arquitectónica.
-   Diferenciar un experimento, un producto y una plataforma.
-   Entender el propósito de LLMOps y MLOps.
-   Identificar los componentes fundamentales de una plataforma
    empresarial de IA.

------------------------------------------------------------------------

# Introducción

Hasta este punto del libro analizamos los fundamentos de los modelos de
lenguaje, las arquitecturas RAG y los sistemas basados en agentes.

Todos esos conceptos responden a una pregunta importante:

> ¿Cómo construir una aplicación inteligente?

Sin embargo, las organizaciones rara vez desarrollan una única
aplicación.

Con el tiempo aparecen nuevos asistentes, agentes especializados,
modelos, bases de conocimiento y equipos de desarrollo.

Administrar ese ecosistema exige un enfoque diferente.

Aquí comienza el dominio de las plataformas de IA.

------------------------------------------------------------------------

# Del proyecto a la plataforma

Un prototipo suele construirse con rapidez.

Puede utilizar un único modelo, un repositorio documental reducido y un
conjunto limitado de herramientas.

Cuando el éxito del proyecto impulsa nuevas iniciativas, comienzan a
surgir preguntas diferentes.

-   ¿Cómo desplegar nuevos modelos sin interrumpir el servicio?
-   ¿Cómo controlar costos?
-   ¿Cómo versionar prompts y configuraciones?
-   ¿Cómo auditar cambios?
-   ¿Cómo reutilizar componentes entre proyectos?
-   ¿Cómo garantizar seguridad y cumplimiento normativo?

Responder estas preguntas requiere pensar en capacidades compartidas y
no únicamente en aplicaciones individuales.

------------------------------------------------------------------------

# ¿Qué es una plataforma de IA?

Una plataforma de IA es un conjunto de servicios, procesos y
herramientas que permite desarrollar, desplegar, operar y gobernar
soluciones basadas en inteligencia artificial de forma repetible y
escalable.

El objetivo no consiste únicamente en ejecutar modelos.

Consiste en proporcionar un entorno donde múltiples equipos puedan
construir soluciones con criterios comunes de calidad, seguridad y
operación.

------------------------------------------------------------------------

# Componentes fundamentales

Aunque cada organización adapta la arquitectura a sus necesidades, una
plataforma suele incluir:

-   catálogo de modelos;
-   infraestructura de inferencia;
-   gestión de prompts;
-   repositorios de conocimiento;
-   pipelines de datos;
-   monitoreo y observabilidad;
-   autenticación y autorización;
-   registro de auditoría;
-   herramientas de evaluación;
-   automatización de despliegues.

Cada componente representa una capacidad reutilizable por distintas
aplicaciones.

------------------------------------------------------------------------

# Una analogía

Pensemos en una ciudad.

Construir una casa resuelve una necesidad puntual.

Construir calles, redes eléctricas, agua potable y transporte permite
que miles de personas construyan sus propias viviendas sobre una
infraestructura común.

Las plataformas cumplen un papel similar.

No resuelven un caso de uso específico.

Crean las condiciones para desarrollar muchos casos de uso de manera
consistente.

------------------------------------------------------------------------

# Arquitectura conceptual

``` mermaid
flowchart LR

DEV[Equipos de desarrollo] --> API[Plataforma de IA]

API --> MODELS[Catálogo de modelos]
API --> RAG[Servicios RAG]
API --> AGENTS[Servicios de agentes]
API --> OBS[Observabilidad]
API --> SEC[Seguridad]
API --> CICD[Automatización]

MODELS --> INF[Infraestructura de inferencia]
```

La plataforma abstrae la complejidad y ofrece capacidades compartidas a
toda la organización.

------------------------------------------------------------------------

# ¿Dónde aparecen LLMOps y MLOps?

A medida que la plataforma crece surge la necesidad de administrar su
ciclo de vida.

Aquí aparecen dos disciplinas complementarias.

**MLOps** se centra en el ciclo de vida de modelos de aprendizaje
automático.

**LLMOps** adapta esos principios al ecosistema de modelos
fundacionales, agentes, RAG, prompts y evaluación continua.

Ambas buscan transformar experimentos en servicios confiables.

------------------------------------------------------------------------

# Caso de estudio

Una empresa comienza con un único asistente documental.

Dos años después dispone de quince asistentes especializados, varios
agentes, tres modelos locales, proveedores externos, múltiples bases
vectoriales y distintos equipos de desarrollo.

Sin una plataforma compartida, cada proyecto implementa autenticación,
monitoreo, despliegues y evaluación de forma diferente.

Los costos aumentan y el mantenimiento se vuelve complejo.

La creación de una plataforma unificada permite estandarizar
capacidades, reducir duplicaciones y acelerar nuevos desarrollos.

------------------------------------------------------------------------

# Ideas clave

-   Una plataforma de IA proporciona capacidades reutilizables para
    múltiples proyectos.
-   El objetivo no es ejecutar un modelo, sino gobernar un ecosistema
    completo.
-   LLMOps y MLOps permiten operar soluciones de IA de manera
    profesional.
-   La plataforma constituye un activo estratégico para la organización.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos el ciclo de vida completo de una
solución de IA y veremos cómo LLMOps adapta los principios de DevOps
para operar modelos, prompts, agentes y sistemas RAG en entornos de
producción.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
