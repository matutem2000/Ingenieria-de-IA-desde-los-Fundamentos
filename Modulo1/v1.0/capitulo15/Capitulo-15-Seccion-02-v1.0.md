# Capitulo-15-Seccion-02-v1.0

# Capítulo 15 --- Evaluación Final y Proyecto Integrador

**Versión:** 1.0\
**Estado:** Aprobado

> *"Los proyectos integradores no ponen a prueba la memoria. Ponen a
> prueba la capacidad de diseñar soluciones frente a restricciones
> reales."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Presentar el proyecto integrador del libro.
-   Definir el contexto, alcance y restricciones del ejercicio.
-   Integrar conocimientos de arquitectura, LLM, RAG, agentes y
    operación.
-   Establecer los criterios de éxito de una solución empresarial.

------------------------------------------------------------------------

# Proyecto integrador

## Contexto

Una organización multinacional desea incorporar una plataforma de
Inteligencia Artificial para asistir a sus colaboradores en la consulta
de procedimientos, políticas internas, documentación técnica y
conocimiento corporativo.

Actualmente la información se encuentra distribuida entre documentos
PDF, manuales, bases de conocimiento, sistemas internos y aplicaciones
de gestión.

Los tiempos de búsqueda son elevados y existen respuestas inconsistentes
entre distintas áreas.

La dirección decide iniciar un proyecto para construir un asistente
corporativo basado en IA.

------------------------------------------------------------------------

# Objetivo del proyecto

Diseñar una solución empresarial que permita responder consultas
utilizando exclusivamente información autorizada por la organización.

La solución deberá priorizar:

-   precisión;
-   trazabilidad;
-   seguridad;
-   mantenibilidad;
-   escalabilidad;
-   observabilidad.

La implementación tecnológica constituye únicamente una parte del
desafío.

La mayor responsabilidad recae sobre el diseño arquitectónico.

------------------------------------------------------------------------

# Restricciones

La solución deberá contemplar las siguientes condiciones:

  Restricción      Descripción
  ---------------- ---------------------------------------------------
  Privacidad       Los documentos contienen información confidencial
  Escalabilidad    Miles de usuarios concurrentes
  Auditoría        Toda respuesta debe poder justificarse
  Disponibilidad   Servicio continuo
  Evolución        Incorporación permanente de nueva documentación

``` mermaid
flowchart LR
A[Usuarios] --> B[Portal Corporativo]
B --> C[Autenticación]
C --> D[Motor RAG]
D --> E[Índice Vectorial]
D --> F[LLM]
F --> G[Respuesta]
G --> H[Observabilidad]
```

------------------------------------------------------------------------

# Entregables esperados

El proyecto deberá incluir como mínimo:

-   arquitectura lógica;
-   arquitectura física;
-   justificación de componentes;
-   estrategia de evaluación;
-   criterios de seguridad;
-   plan de operación;
-   propuesta de mejora continua.

No existe una única solución correcta.

La calidad del proyecto dependerá de la capacidad para justificar cada
decisión tomada.

------------------------------------------------------------------------

# Ideas clave

-   Un proyecto integrador evalúa competencias, no herramientas.
-   Las restricciones del negocio condicionan la arquitectura.
-   Toda decisión debe estar respaldada por argumentos técnicos.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección se definirán los criterios de evaluación que
permitirán valorar objetivamente el proyecto integrador.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
