# Capítulo 4 --- Sección 05 de 10

# La memoria de los agentes: recordar para actuar mejor

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un agente sin memoria debe redescubrir el mundo en cada interacción.
> Un agente con memoria puede construir experiencia."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué la memoria es un componente esencial de un
    agente.
-   Diferenciar memoria de trabajo, memoria a largo plazo, memoria
    semántica y memoria episódica.
-   Entender cómo se implementan estos conceptos en arquitecturas
    empresariales.
-   Diseñar estrategias de memoria escalables y seguras.

------------------------------------------------------------------------

# Introducción

Hasta este punto analizamos cómo un agente razona, planifica y utiliza
herramientas.

Sin embargo, existe una capacidad adicional que determina gran parte de
su utilidad: la memoria.

Sin memoria, cada solicitud constituye un problema completamente nuevo.

El agente olvida conversaciones anteriores, decisiones tomadas y
resultados obtenidos.

En aplicaciones reales esto resulta inaceptable.

Los usuarios esperan continuidad, personalización y aprendizaje a lo
largo del tiempo.

La memoria permite construir esa continuidad.

------------------------------------------------------------------------

# ¿Qué entendemos por memoria?

En el contexto de la Ingeniería de IA, la memoria es el conjunto de
mecanismos que permiten conservar información útil para tareas presentes
o futuras.

No toda la información merece el mismo tratamiento.

Por ello, la mayoría de las arquitecturas distingue distintos tipos de
memoria según su duración, propósito y forma de recuperación.

------------------------------------------------------------------------

# Memoria de trabajo

La memoria de trabajo contiene únicamente la información necesaria para
resolver la tarea actual.

Incluye elementos como:

-   el objetivo solicitado;
-   el contexto de la conversación;
-   resultados intermedios;
-   estado de las herramientas utilizadas.

Su vida útil suele finalizar cuando termina la ejecución.

Mantener esta memoria pequeña mejora el rendimiento y reduce el consumo
de contexto del LLM.

------------------------------------------------------------------------

# Memoria a largo plazo

La memoria a largo plazo conserva información entre distintas sesiones.

Puede almacenar:

-   preferencias del usuario;
-   configuraciones habituales;
-   historial de decisiones;
-   conocimiento específico del dominio;
-   resultados previamente validados.

En la práctica, esta memoria suele implementarse mediante bases de
datos, repositorios documentales o sistemas RAG.

El LLM no almacena directamente esta información.

La recupera cuando resulta necesaria.

------------------------------------------------------------------------

# Memoria semántica

La memoria semántica representa conocimiento relativamente estable.

Por ejemplo:

-   documentación técnica;
-   políticas corporativas;
-   manuales;
-   procedimientos;
-   glosarios;
-   normas de negocio.

Generalmente se implementa mediante repositorios indexados y búsqueda
semántica.

Cuando el agente necesita responder una consulta, recupera únicamente
los fragmentos relevantes.

------------------------------------------------------------------------

# Memoria episódica

La memoria episódica registra experiencias concretas.

Algunos ejemplos incluyen:

-   tareas ejecutadas anteriormente;
-   errores detectados;
-   decisiones tomadas;
-   resultados obtenidos;
-   conversaciones relevantes.

Esta información permite evitar repetir errores y facilita auditorías
posteriores.

En ciertos escenarios también puede utilizarse para mejorar futuras
planificaciones.

------------------------------------------------------------------------

# Arquitectura de memoria

Una implementación típica puede representarse de la siguiente manera:

``` mermaid
flowchart LR

U[Usuario] --> O[Orquestador]

O --> W[Memoria de trabajo]
O --> S[Memoria semántica]
O --> E[Memoria episódica]

S --> RAG[RAG]
E --> DB[Base de datos]

W --> LLM
RAG --> LLM
DB --> LLM

LLM --> O
O --> R[Respuesta]
```

Cada tipo de memoria cumple una función diferente.

No existe una única memoria universal.

------------------------------------------------------------------------

# ¿Debe recordarse todo?

No.

Recordar indiscriminadamente produce problemas.

Entre ellos:

-   crecimiento innecesario del contexto;
-   incremento de costos;
-   información obsoleta;
-   riesgos de privacidad;
-   respuestas inconsistentes.

Un arquitecto debe definir políticas claras sobre:

-   qué recordar;
-   durante cuánto tiempo;
-   quién puede acceder;
-   cuándo eliminar la información.

La memoria también forma parte del gobierno de datos.

------------------------------------------------------------------------

# Caso de estudio

Una mesa de ayuda incorpora un agente para asistir a los técnicos.

Durante la primera versión, cada conversación comenzaba desde cero.

Los usuarios debían repetir constantemente información sobre el sistema
afectado, el historial del incidente y las acciones ya realizadas.

En una segunda versión se añadió memoria episódica.

El agente recuperaba automáticamente los eventos relacionados con el
ticket actual y utilizaba esa información para continuar el diagnóstico.

El cambio no mejoró el modelo.

Mejoró la arquitectura de memoria.

------------------------------------------------------------------------

# Buenas prácticas

-   Separar memoria temporal de memoria persistente.
-   No almacenar información sensible sin controles adecuados.
-   Aplicar políticas de expiración y versionado.
-   Recuperar únicamente la memoria relevante para cada tarea.
-   Auditar el acceso a la información persistente.
-   Diseñar la memoria como un servicio independiente del LLM.

------------------------------------------------------------------------

# Ideas clave

-   La memoria permite continuidad entre interacciones.
-   Existen distintos tipos de memoria con responsabilidades diferentes.
-   La memoria persistente suele implementarse fuera del modelo.
-   Gestionar correctamente la memoria mejora precisión, costos y
    experiencia del usuario.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos los sistemas multiagente,
comprendiendo cómo varios agentes especializados pueden colaborar para
resolver problemas que exceden las capacidades de un único agente.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
