# Capitulo-15-Seccion-04-v1.0

# Capítulo 15 --- Evaluación Final y Proyecto Integrador

**Versión:** 1.0\
**Estado:** Aprobado

> *"Toda arquitectura sólida comienza comprendiendo el problema antes de
> seleccionar cualquier tecnología."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar el problema de negocio del proyecto integrador.
-   Identificar actores, necesidades y restricciones.
-   Traducir requerimientos funcionales y no funcionales en decisiones
    arquitectónicas.
-   Preparar el diseño de la solución.

------------------------------------------------------------------------

# Comprensión del problema

La organización necesita un asistente corporativo capaz de responder
consultas sobre información distribuida en múltiples fuentes
documentales.

Actualmente los usuarios deben consultar distintos sistemas,
repositorios y manuales para obtener una respuesta.

Esto genera:

-   pérdida de tiempo;
-   respuestas inconsistentes;
-   dependencia de especialistas;
-   duplicación de esfuerzos.

Antes de seleccionar un modelo o una plataforma, el arquitecto debe
comprender este contexto.

------------------------------------------------------------------------

# Actores involucrados

  Actor          Necesidad principal
  -------------- -------------------------------
  Empleado       Obtener respuestas rápidas
  Especialista   Reducir consultas repetitivas
  Área de TI     Administrar la plataforma
  Seguridad      Proteger la información
  Dirección      Medir el impacto del proyecto

------------------------------------------------------------------------

# Requerimientos

## Funcionales

-   Consultas en lenguaje natural.
-   Acceso a documentación autorizada.
-   Referencias documentales.
-   Historial de conversaciones.
-   Integración con autenticación corporativa.

## No funcionales

-   Alta disponibilidad.
-   Escalabilidad horizontal.
-   Baja latencia.
-   Observabilidad.
-   Seguridad.
-   Auditoría.

------------------------------------------------------------------------

# Análisis inicial

``` mermaid
flowchart LR
A[Problema de negocio]
A --> B[Usuarios]
A --> C[Documentación]
A --> D[Restricciones]
B --> E[Arquitectura]
C --> E
D --> E
```

La arquitectura comenzará a definirse únicamente después de comprender
estos elementos.

------------------------------------------------------------------------

# Riesgos iniciales

  Riesgo                         Impacto
  ------------------------------ -----------------------------
  Información desactualizada     Respuestas incorrectas
  Falta de gobierno documental   Baja confianza
  Escalabilidad insuficiente     Mala experiencia de usuario
  Accesos indebidos              Riesgo de seguridad

------------------------------------------------------------------------

# Buenas prácticas

-   Validar los requisitos con todas las áreas involucradas.
-   Diferenciar claramente problemas de negocio y problemas
    tecnológicos.
-   Documentar supuestos antes de diseñar la arquitectura.
-   Identificar restricciones desde el inicio.

------------------------------------------------------------------------

# Ideas clave

-   El análisis del problema determina el éxito del proyecto.
-   La arquitectura responde a necesidades del negocio.
-   Comprender el contexto reduce decisiones incorrectas durante el
    diseño.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección comenzaremos el diseño de la arquitectura lógica
del proyecto integrador, seleccionando los componentes principales y
justificando cada decisión.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
