# Capítulo 4 --- Sección 07 de 10

# Planning: cómo un agente transforma objetivos en planes ejecutables

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Resolver un problema complejo rara vez consiste en ejecutar una
> única acción. La clave está en construir un plan capaz de adaptarse al
> contexto."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender el papel de la planificación dentro de un agente.
-   Diferenciar un objetivo de un plan de ejecución.
-   Conocer estrategias para descomponer tareas complejas.
-   Incorporar criterios arquitectónicos para diseñar agentes capaces de
    planificar.

------------------------------------------------------------------------

# Introducción

En una aplicación tradicional, el flujo de ejecución suele estar
definido por el desarrollador.

El sistema conoce de antemano qué pasos debe seguir.

Los agentes modifican este paradigma.

Reciben un objetivo de alto nivel y deben decidir por sí mismos qué
acciones ejecutar, en qué orden y con qué herramientas.

La planificación se convierte así en una capacidad fundamental.

------------------------------------------------------------------------

# Del objetivo al plan

Los usuarios rara vez describen todos los pasos necesarios para
completar una tarea.

Una solicitud como:

> "Prepará la documentación para incorporar un nuevo empleado."

encierra múltiples actividades implícitas.

El agente debe identificar dichas actividades y organizarlas en una
secuencia coherente.

Entre ellas podrían encontrarse:

-   validar la identidad;
-   crear cuentas de acceso;
-   asignar permisos;
-   generar documentación;
-   notificar a las áreas involucradas.

La planificación traduce una intención general en acciones concretas.

------------------------------------------------------------------------

# Descomposición de tareas

Uno de los principios más importantes consiste en dividir problemas
complejos en subtareas manejables.

Este enfoque ofrece varias ventajas:

-   facilita la reutilización de herramientas;
-   simplifica la recuperación ante errores;
-   permite ejecutar tareas en paralelo cuando corresponda;
-   mejora la observabilidad;
-   reduce el riesgo de decisiones incorrectas.

La descomposición también favorece la colaboración entre agentes
especializados.

------------------------------------------------------------------------

# Planes dinámicos

No todos los planes permanecen estables.

Durante la ejecución pueden surgir eventos inesperados.

Por ejemplo:

-   una API deja de responder;
-   un documento no existe;
-   un usuario carece de permisos;
-   una herramienta devuelve información incompleta.

Un agente maduro no continúa ejecutando el plan original sin
modificaciones.

Reevalúa la situación y genera un nuevo plan teniendo en cuenta el
estado actual del sistema.

Esta capacidad convierte la planificación en un proceso continuo y no en
una etapa aislada.

------------------------------------------------------------------------

# Dependencias

Las tareas rara vez son independientes.

Algunas requieren que otras hayan finalizado previamente.

Por ejemplo, no es posible asignar permisos a una cuenta que todavía no
fue creada.

El planificador debe identificar estas relaciones para evitar errores de
ejecución.

Desde una perspectiva arquitectónica, esto implica modelar dependencias
explícitas entre acciones.

------------------------------------------------------------------------

# Priorización

Cuando existen múltiples tareas posibles, el agente necesita establecer
prioridades.

Algunos criterios habituales incluyen:

-   criticidad para el negocio;
-   disponibilidad de recursos;
-   tiempo estimado de ejecución;
-   impacto sobre el usuario;
-   riesgo asociado.

La priorización permite optimizar tanto el rendimiento como la
experiencia final.

------------------------------------------------------------------------

# Flujo de planificación

``` mermaid
flowchart TD

A[Objetivo]
A --> B[Análisis]

B --> C[Descomposición]

C --> D[Priorización]

D --> E[Ejecución]

E --> F[Evaluación]

F -->|Objetivo alcanzado| G[Finalizar]

F -->|Cambios en el entorno| B
```

El ciclo refleja que la planificación no finaliza cuando comienza la
ejecución.

Ambos procesos evolucionan conjuntamente.

------------------------------------------------------------------------

# Caso de estudio

Una empresa solicita al agente:

> "Migrá el sistema de desarrollo al nuevo entorno."

Durante el análisis inicial el agente identifica decenas de tareas.

Al comenzar la ejecución descubre que uno de los servidores no se
encuentra disponible.

En lugar de cancelar toda la operación, reorganiza el plan.

Ejecuta las tareas independientes, registra la incidencia y pospone
aquellas que dependen del servidor afectado.

La capacidad de replantear el plan evita interrupciones innecesarias y
mejora la resiliencia del proceso.

------------------------------------------------------------------------

# Buenas prácticas

-   Diseñar tareas pequeñas y reutilizables.
-   Expresar dependencias de forma explícita.
-   Permitir replanificación durante la ejecución.
-   Registrar cada decisión tomada por el planificador.
-   Establecer límites para evitar ciclos infinitos.
-   Medir el desempeño del plan y no solo el resultado final.

------------------------------------------------------------------------

# Ideas clave

-   Un objetivo no constituye un plan.
-   La planificación transforma intenciones en acciones concretas.
-   Los planes deben adaptarse a los cambios del entorno.
-   La calidad del planificador influye directamente sobre la eficacia
    del agente.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la observabilidad y el gobierno de
agentes de IA, analizando cómo auditar decisiones, controlar costos,
registrar ejecuciones y garantizar un funcionamiento seguro en entornos
empresariales.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
