# Capítulo 4 --- Sección 06 de 10

# Sistemas Multiagente: inteligencia distribuida

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un agente puede resolver muchas tareas. Un conjunto de agentes
> especializados puede resolver problemas cuya complejidad supera las
> capacidades de un único componente."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender qué es un sistema multiagente.
-   Diferenciar un agente generalista de un conjunto de agentes
    especializados.
-   Entender los patrones de coordinación más utilizados.
-   Identificar cuándo conviene adoptar una arquitectura multiagente.

------------------------------------------------------------------------

# Introducción

A medida que las aplicaciones de IA crecen, también aumenta la
complejidad de las tareas que deben resolver.

Un único agente puede transformarse rápidamente en un cuello de botella.

Debe conocer demasiados procesos, utilizar numerosas herramientas y
tomar decisiones sobre dominios muy diferentes.

Una alternativa consiste en distribuir esas responsabilidades.

En lugar de construir un agente capaz de hacerlo todo, se diseñan varios
agentes especializados que colaboran entre sí.

Este enfoque da origen a los **Sistemas Multiagente (Multi-Agent
Systems, MAS)**.

------------------------------------------------------------------------

# ¿Por qué varios agentes?

La división de responsabilidades aporta ventajas similares a las
observadas en la ingeniería de software.

Cada agente puede especializarse en un dominio concreto.

Por ejemplo:

-   agente de búsqueda documental;
-   agente financiero;
-   agente legal;
-   agente de soporte técnico;
-   agente de planificación;
-   agente de auditoría.

Esta especialización simplifica la evolución del sistema y mejora la
calidad de las decisiones dentro de cada dominio.

------------------------------------------------------------------------

# Patrones de coordinación

Existen múltiples estrategias para coordinar agentes.

## Orquestación

Un agente coordinador recibe la solicitud, divide el trabajo y
distribuye tareas entre los agentes especializados.

Este patrón facilita el control, la auditoría y la aplicación de
políticas.

## Coreografía

Los agentes colaboran directamente entre sí mediante eventos o mensajes,
sin depender de un coordinador central.

Este enfoque favorece el desacoplamiento, aunque incrementa la
complejidad de diseño.

La elección depende de los requisitos de cada organización.

------------------------------------------------------------------------

# Comunicación entre agentes

La colaboración requiere un lenguaje común.

En la práctica, los agentes intercambian información mediante:

-   mensajes estructurados;
-   APIs;
-   colas de eventos;
-   llamadas a herramientas;
-   documentos compartidos.

Es recomendable que la comunicación utilice contratos explícitos y
formatos bien definidos para facilitar la interoperabilidad.

------------------------------------------------------------------------

# Evitando duplicación de responsabilidades

Un error frecuente consiste en crear múltiples agentes con funciones
similares.

Esto genera:

-   decisiones inconsistentes;
-   mayor consumo de recursos;
-   mantenimiento complejo;
-   dificultades para el gobierno del sistema.

Cada agente debe poseer un propósito claramente delimitado y
responsabilidades bien definidas.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR

U[Usuario] --> O[Agente Orquestador]

O --> A1[Agente RAG]
O --> A2[Agente ERP]
O --> A3[Agente Analítico]
O --> A4[Agente Auditor]

A1 --> O
A2 --> O
A3 --> O
A4 --> O

O --> R[Respuesta integrada]
```

El usuario interactúa con un único punto de entrada, mientras que la
complejidad interna permanece encapsulada.

------------------------------------------------------------------------

# Caso de estudio

Una empresa desea automatizar el proceso de incorporación de nuevos
empleados.

El agente orquestador recibe la solicitud y distribuye tareas.

-   El agente de RR. HH. valida la información del colaborador.
-   El agente de infraestructura crea las cuentas necesarias.
-   El agente de seguridad asigna permisos.
-   El agente documental genera contratos y formularios.
-   El agente de auditoría registra todas las acciones realizadas.

Cada componente trabaja sobre su propio dominio, mientras el orquestador
consolida el resultado final.

------------------------------------------------------------------------

# Desafíos

Las arquitecturas multiagente introducen nuevos problemas.

-   Coordinación entre agentes.
-   Gestión de estados compartidos.
-   Resolución de conflictos.
-   Tolerancia a fallos.
-   Observabilidad distribuida.
-   Control de costos.
-   Latencia acumulada.

Por este motivo, no toda aplicación requiere múltiples agentes.

La complejidad debe justificarse mediante necesidades reales del
negocio.

------------------------------------------------------------------------

# Buenas prácticas

-   Definir responsabilidades claras.
-   Mantener interfaces estables entre agentes.
-   Evitar dependencias circulares.
-   Centralizar observabilidad y auditoría.
-   Medir el valor aportado por cada agente.
-   Incorporar mecanismos de recuperación ante fallos.

------------------------------------------------------------------------

# Ideas clave

-   Un sistema multiagente distribuye responsabilidades entre
    componentes especializados.
-   La coordinación puede realizarse mediante orquestación o
    coreografía.
-   La especialización mejora mantenibilidad y escalabilidad.
-   La complejidad adicional debe responder a una necesidad
    arquitectónica concreta.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos la planificación avanzada
(*Planning*), la descomposición automática de objetivos y las
estrategias utilizadas por los agentes para resolver tareas complejas de
múltiples pasos.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
