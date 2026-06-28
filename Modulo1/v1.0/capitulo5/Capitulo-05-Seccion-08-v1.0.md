# Capítulo 5 --- Sección 08 de 10

# Escalabilidad y resiliencia en plataformas de IA

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Una plataforma empresarial no se diseña para el promedio de carga.
> Se diseña para seguir funcionando cuando las condiciones dejan de ser
> normales."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los principios de escalabilidad aplicados a plataformas
    de IA.
-   Diseñar arquitecturas resilientes para modelos, agentes y servicios
    RAG.
-   Conocer estrategias para optimizar rendimiento y costos.
-   Identificar patrones para alta disponibilidad y recuperación ante
    fallos.

------------------------------------------------------------------------

# Introducción

Un prototipo puede atender a unos pocos usuarios utilizando un único
modelo.

Una plataforma empresarial debe soportar crecimiento, picos de demanda,
mantenimiento programado y fallos de infraestructura sin degradar
significativamente el servicio.

La escalabilidad y la resiliencia dejan de ser optimizaciones para
convertirse en requisitos arquitectónicos.

------------------------------------------------------------------------

# Escalabilidad vertical y horizontal

La escalabilidad vertical incrementa la capacidad de un nodo existente
mediante más CPU, memoria o GPU.

La escalabilidad horizontal agrega nuevas instancias que trabajan de
forma coordinada.

En plataformas de IA ambas estrategias suelen combinarse.

La elección depende del tipo de carga, del costo y de las
características del modelo utilizado.

------------------------------------------------------------------------

# Balanceo de carga

Cuando existen múltiples instancias de inferencia, resulta necesario
distribuir las solicitudes.

Un balanceador puede:

-   repartir tráfico;
-   detectar instancias no saludables;
-   evitar sobrecarga;
-   facilitar despliegues graduales.

El balanceo también puede considerar capacidades específicas, como
modelos especializados o disponibilidad de GPU.

------------------------------------------------------------------------

# Colas y procesamiento asíncrono

No todas las solicitudes requieren una respuesta inmediata.

Tareas como:

-   indexación documental;
-   generación de embeddings;
-   análisis masivos;
-   entrenamiento;
-   creación de informes complejos;

pueden ejecutarse mediante colas.

Este enfoque desacopla productores y consumidores, mejora la utilización
de recursos y reduce el impacto de los picos de demanda.

------------------------------------------------------------------------

# Cachés

Muchas consultas son repetitivas.

Una estrategia de caché puede reducir:

-   latencia;
-   consumo de tokens;
-   llamadas a proveedores externos;
-   costo operativo.

La plataforma debe definir políticas claras de expiración e invalidación
para evitar respuestas desactualizadas.

------------------------------------------------------------------------

# Tolerancia a fallos

Los componentes fallarán en algún momento.

Una arquitectura resiliente incorpora mecanismos como:

-   reintentos controlados;
-   circuit breakers;
-   timeouts;
-   degradación funcional;
-   redundancia;
-   recuperación automática.

El objetivo no es eliminar los errores, sino impedir que un fallo
localizado afecte a toda la plataforma.

------------------------------------------------------------------------

# Observabilidad para escalar

La escalabilidad depende de información objetiva.

Conviene monitorear:

-   utilización de CPU y GPU;
-   memoria;
-   latencia por servicio;
-   longitud de colas;
-   tiempo de inferencia;
-   consumo de tokens;
-   errores por componente.

Estas métricas permiten anticipar cuellos de botella antes de que
afecten a los usuarios.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR

U[Usuarios]
--> LB[Balanceador]

LB --> I1[Inferencia 1]
LB --> I2[Inferencia 2]
LB --> I3[Inferencia 3]

I1 --> RAG[RAG]
I2 --> RAG
I3 --> RAG

RAG --> VDB[Base Vectorial]

LB --> Q[Colas]
Q --> W[Workers]

I1 --> OBS[Observabilidad]
I2 --> OBS
I3 --> OBS
W --> OBS
```

------------------------------------------------------------------------

# Caso de estudio

Una organización lanza un asistente interno que inicialmente atiende a
cincuenta usuarios.

Tras integrarlo con el portal corporativo, el número de consultas se
multiplica por veinte.

Gracias al uso de balanceadores, inferencia distribuida y procesamiento
asíncrono para tareas pesadas, la plataforma mantiene tiempos de
respuesta estables sin rediseñar la aplicación.

La arquitectura absorbió el crecimiento.

------------------------------------------------------------------------

# Buenas prácticas

-   Diseñar componentes sin estado cuando sea posible.
-   Escalar servicios de forma independiente.
-   Utilizar colas para procesos extensos.
-   Implementar cachés con políticas de expiración.
-   Automatizar recuperación ante fallos.
-   Monitorear continuamente capacidad y costos.
-   Probar escenarios de alta carga antes de producción.

------------------------------------------------------------------------

# Ideas clave

-   Escalabilidad y resiliencia son capacidades arquitectónicas.
-   Balanceo, colas y cachés permiten optimizar rendimiento.
-   La tolerancia a fallos debe diseñarse desde el inicio.
-   Las decisiones de escalado deben apoyarse en métricas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección integraremos gobierno, observabilidad,
seguridad, automatización y operación continua para construir una
plataforma de IA preparada para múltiples equipos y cientos de
aplicaciones.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
