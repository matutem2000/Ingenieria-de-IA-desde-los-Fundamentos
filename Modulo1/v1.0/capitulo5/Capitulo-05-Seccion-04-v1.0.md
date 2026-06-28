# Capítulo 5 --- Sección 04 de 10

# Ingeniería de Prompts: de texto improvisado a activo estratégico

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"Un prompt en producción deja de ser una instrucción escrita por una
> persona. Se convierte en un componente de software que debe
> evolucionar con el mismo rigor que el resto de la plataforma."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender por qué los prompts forman parte de la arquitectura.
-   Tratar los prompts como artefactos versionables.
-   Diseñar catálogos reutilizables de prompts.
-   Incorporar estrategias de evaluación y mantenimiento continuo.

------------------------------------------------------------------------

# Introducción

En los primeros experimentos con modelos de lenguaje es habitual
escribir un prompt directamente en la interfaz del proveedor.

Este enfoque resulta adecuado para aprender.

Sin embargo, una organización que opera decenas de asistentes, agentes y
procesos automatizados necesita un enfoque completamente distinto.

Los prompts pasan a ser activos tecnológicos.

Deben mantenerse, versionarse, probarse y auditarse.

La Ingeniería de Prompts deja de ser una habilidad individual para
convertirse en una disciplina de plataforma.

------------------------------------------------------------------------

# El problema del prompt "invisible"

Una situación frecuente consiste en encontrar instrucciones distribuidas
en múltiples lugares:

-   código fuente;
-   variables de entorno;
-   archivos de configuración;
-   bases de datos;
-   aplicaciones cliente.

Cuando surge un problema nadie sabe con certeza cuál es la versión
utilizada por producción.

Esto dificulta reproducir errores, comparar resultados y realizar
auditorías.

Centralizar la gestión de prompts elimina gran parte de estos
inconvenientes.

------------------------------------------------------------------------

# Un prompt es un artefacto de software

Desde una perspectiva de ingeniería, un prompt posee características
similares a cualquier otro componente del sistema.

Debe contar con:

-   identificador único;
-   versión;
-   autor o responsable;
-   fecha de creación;
-   historial de cambios;
-   propósito funcional;
-   métricas de calidad;
-   estado (experimental, aprobado, retirado).

Esta información permite administrar su evolución de forma controlada.

------------------------------------------------------------------------

# Catálogo de prompts

Una plataforma madura suele disponer de un repositorio centralizado.

Cada prompt puede clasificarse según:

-   dominio de negocio;
-   aplicación consumidora;
-   idioma;
-   modelo compatible;
-   nivel de criticidad;
-   agente asociado.

El catálogo facilita reutilización y evita duplicar instrucciones
similares en distintos proyectos.

------------------------------------------------------------------------

# Versionado

Modificar un prompt puede alterar significativamente el comportamiento
de un sistema.

Por ello conviene aplicar principios similares a los utilizados con el
código fuente.

Una nueva versión debería:

-   conservar el historial;
-   documentar el motivo del cambio;
-   permitir comparaciones;
-   facilitar el retorno a una versión anterior.

Versionar no significa únicamente guardar copias.

Significa administrar la evolución.

------------------------------------------------------------------------

# Evaluación antes del despliegue

Toda modificación importante debería validarse mediante un conjunto
representativo de pruebas.

Entre los aspectos evaluados pueden encontrarse:

-   calidad de las respuestas;
-   cumplimiento de instrucciones;
-   consumo de tokens;
-   tiempo de respuesta;
-   uso correcto de herramientas;
-   estabilidad frente a consultas ambiguas.

La aprobación no debería depender exclusivamente de una revisión manual.

------------------------------------------------------------------------

# Plantillas y parametrización

Muchos prompts comparten una estructura común.

En lugar de duplicarlos conviene utilizar plantillas parametrizadas.

Por ejemplo:

-   rol del asistente;
-   idioma;
-   nivel de detalle;
-   políticas de seguridad;
-   contexto recuperado mediante RAG.

Este enfoque reduce mantenimiento y favorece la consistencia entre
aplicaciones.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR

DEV[Equipo de desarrollo]
--> CAT[Catálogo de Prompts]

CAT --> TEST[Evaluación]

TEST --> VER[Versionado]

VER --> DEPLOY[Despliegue]

DEPLOY --> PROD[Aplicaciones y Agentes]

PROD --> MET[Observabilidad]

MET --> CAT
```

El ciclo de vida del prompt forma parte del ciclo de vida completo de la
plataforma.

------------------------------------------------------------------------

# Caso de estudio

Un agente jurídico comienza a responder con menor precisión después de
una actualización.

El análisis muestra que el modelo no cambió.

Tampoco cambió el repositorio RAG.

La diferencia proviene de una modificación menor en el prompt del
sistema realizada semanas atrás.

Gracias al versionado y al registro de cambios, el equipo identifica
rápidamente la causa, compara ambas versiones y restaura la
configuración anterior mientras prepara una mejora definitiva.

------------------------------------------------------------------------

# Buenas prácticas

-   Centralizar todos los prompts.
-   Aplicar control de versiones.
-   Automatizar pruebas antes del despliegue.
-   Reutilizar plantillas parametrizadas.
-   Registrar métricas de calidad.
-   Documentar el propósito de cada prompt.
-   Asociar cada versión con el modelo para el cual fue validada.

------------------------------------------------------------------------

# Ideas clave

-   Un prompt de producción es un activo de ingeniería.
-   El versionado facilita auditoría y reproducibilidad.
-   Los catálogos favorecen reutilización y consistencia.
-   La evaluación continua reduce el riesgo de regresiones.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la evaluación continua de
plataformas de IA, analizando cómo medir calidad, costos, seguridad y
rendimiento mediante pipelines automatizados de validación.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
