# Capítulo 5 --- Sección 02 de 10

# LLMOps: el ciclo de vida de una solución de IA

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Construir un modelo útil es un logro. Mantenerlo operativo, seguro y
> evolucionando durante años es una disciplina de ingeniería."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender el concepto de LLMOps.
-   Diferenciar DevOps, MLOps y LLMOps.
-   Entender el ciclo de vida de una solución basada en modelos
    fundacionales.
-   Identificar las capacidades necesarias para operar IA en producción.

------------------------------------------------------------------------

# Introducción

Durante muchos años las organizaciones desarrollaron software siguiendo
principios de ingeniería consolidados.

Con la llegada del aprendizaje automático apareció un nuevo desafío: los
modelos también evolucionan.

Ya no basta con versionar código.

Es necesario administrar datasets, modelos, métricas y procesos de
entrenamiento.

La aparición de los Large Language Models incorporó una nueva capa de
complejidad.

Prompts, bases vectoriales, agentes, herramientas, evaluaciones
automáticas y múltiples proveedores pasan a formar parte del ciclo de
vida del producto.

En este contexto surge **LLMOps**.

------------------------------------------------------------------------

# De DevOps a LLMOps

Cada disciplina responde a un problema distinto.

  -----------------------------------------------------------------------
  Disciplina                 Objetivo principal
  -------------------------- --------------------------------------------
  DevOps                     Construir y operar aplicaciones de software.

  MLOps                      Gestionar el ciclo de vida de modelos de
                             Machine Learning.

  LLMOps                     Operar soluciones basadas en modelos
                             fundacionales, RAG y agentes.
  -----------------------------------------------------------------------

LLMOps no reemplaza a DevOps ni a MLOps.

Los complementa incorporando capacidades específicas del ecosistema de
IA generativa.

------------------------------------------------------------------------

# El ciclo de vida

Una solución moderna suele atravesar las siguientes etapas:

1.  Definición del caso de uso.
2.  Selección del modelo.
3.  Diseño de prompts y arquitectura.
4.  Construcción del pipeline RAG o de agentes.
5.  Evaluación funcional y técnica.
6.  Despliegue.
7.  Observabilidad.
8.  Mejora continua.

Cada etapa produce información que debe conservarse y versionarse.

------------------------------------------------------------------------

# ¿Qué debe versionarse?

En una aplicación tradicional el repositorio contiene principalmente
código.

En una plataforma de IA también conviene versionar:

-   prompts;
-   configuraciones del modelo;
-   modelos de embeddings;
-   pipelines de ingestión;
-   evaluaciones;
-   datasets de prueba;
-   herramientas disponibles;
-   políticas de seguridad.

Versionar estos elementos permite reproducir resultados y comprender el
impacto de cada cambio.

------------------------------------------------------------------------

# Despliegue continuo

El despliegue de una solución de IA no debería depender de tareas
manuales.

Las organizaciones maduras automatizan procesos como:

-   construcción de imágenes;
-   ejecución de pruebas;
-   despliegue por ambientes;
-   validación de métricas;
-   rollback;
-   actualización de configuraciones.

La automatización reduce errores y acelera la entrega de nuevas
capacidades.

------------------------------------------------------------------------

# Observabilidad durante la operación

Una vez desplegado el sistema comienza una nueva etapa.

Es necesario responder preguntas como:

-   ¿Qué modelo está respondiendo?
-   ¿Cuántos tokens consume?
-   ¿Cuál es el costo diario?
-   ¿Qué prompts generan mejores resultados?
-   ¿Qué herramientas producen más errores?
-   ¿Cómo evoluciona la calidad del sistema?

Sin observabilidad no existe mejora continua.

------------------------------------------------------------------------

# Arquitectura conceptual

``` mermaid
flowchart LR

DEV[Desarrollo]
--> TEST[Evaluación]

TEST --> BUILD[Construcción]

BUILD --> DEPLOY[Despliegue]

DEPLOY --> PROD[Producción]

PROD --> OBS[Observabilidad]

OBS --> IMP[Mejora continua]

IMP --> DEV
```

Este ciclo se repite continuamente durante toda la vida útil de la
plataforma.

------------------------------------------------------------------------

# Caso de estudio

Una organización modifica un prompt para mejorar la calidad de un
asistente jurídico.

Las respuestas parecen mejores durante las pruebas iniciales.

Sin embargo, al analizar las métricas en producción se observa un
incremento significativo en el consumo de tokens y un aumento del costo
operativo.

Gracias al versionado y a la observabilidad, el equipo identifica el
cambio responsable, compara resultados y ajusta el diseño sin afectar al
resto de la plataforma.

------------------------------------------------------------------------

# Buenas prácticas

-   Automatizar el ciclo de despliegue.
-   Versionar todos los artefactos relevantes.
-   Medir calidad y costos de forma continua.
-   Mantener ambientes separados para desarrollo, pruebas y producción.
-   Registrar el historial de cambios.
-   Incorporar evaluación automática antes de cada despliegue.

------------------------------------------------------------------------

# Ideas clave

-   LLMOps extiende los principios de DevOps al ecosistema de IA
    generativa.
-   Los prompts y las configuraciones forman parte del ciclo de vida del
    producto.
-   La operación continua requiere automatización y observabilidad.
-   La mejora permanente depende de métricas objetivas.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la gestión de modelos,
comprendiendo cómo seleccionar, versionar, actualizar y reemplazar
modelos fundacionales sin comprometer la estabilidad de una plataforma
empresarial.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
