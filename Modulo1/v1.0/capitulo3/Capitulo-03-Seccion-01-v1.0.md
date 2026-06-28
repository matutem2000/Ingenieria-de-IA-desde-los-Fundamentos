# Capítulo 3 --- Sección 01 de 10

# Retrieval-Augmented Generation: cuando el conocimiento del modelo no alcanza

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La pregunta más importante no es cuánto sabe un modelo, sino cómo
> accede al conocimiento que necesita en el momento adecuado."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender el problema que dio origen a Retrieval-Augmented
    Generation (RAG).
-   Diferenciar conocimiento entrenado de conocimiento externo.
-   Identificar las limitaciones de un LLM trabajando de forma aislada.
-   Entender por qué RAG representa una decisión arquitectónica y no un
    nuevo modelo.

------------------------------------------------------------------------

# Introducción

En los capítulos anteriores analizamos cómo aprende un modelo de
lenguaje, cómo representa la información y cómo genera respuestas.

También vimos que un LLM posee una limitación fundamental.

Su conocimiento está determinado por dos elementos:

-   los parámetros obtenidos durante el entrenamiento;
-   el contexto disponible durante la inferencia.

Esto plantea un desafío inmediato para cualquier organización.

¿Cómo responder preguntas sobre información que nunca formó parte del
entrenamiento del modelo?

------------------------------------------------------------------------

# Un problema cotidiano

Imaginemos una empresa que desea construir un asistente para responder
consultas sobre:

-   procedimientos internos;
-   contratos;
-   manuales técnicos;
-   expedientes;
-   políticas de seguridad;
-   documentación de proyectos.

Ninguno de esos documentos fue utilizado durante el entrenamiento del
modelo.

Aunque el LLM sea extremadamente capaz, simplemente no puede conocer
información privada que nunca estuvo disponible públicamente.

Entrenar nuevamente el modelo completo tampoco resulta una alternativa
razonable.

El costo económico, el tiempo requerido y la complejidad técnica hacen
que esta estrategia sea inviable para la mayoría de las organizaciones.

------------------------------------------------------------------------

# Las alternativas tradicionales

Antes de la aparición de RAG existían dos caminos habituales.

El primero consistía en confiar únicamente en el conocimiento general
del modelo.

Esto producía respuestas fluidas, pero incapaces de incorporar
información específica de la organización.

El segundo consistía en volver a entrenar el modelo con documentación
propia.

Aunque posible en determinados escenarios, esta estrategia presenta
importantes desventajas:

-   alto costo computacional;
-   largos tiempos de entrenamiento;
-   dificultad para actualizar información;
-   necesidad de infraestructura especializada;
-   riesgo de degradar capacidades previamente adquiridas.

Era evidente que hacía falta un enfoque diferente.

------------------------------------------------------------------------

# Una idea sencilla con enorme impacto

La propuesta detrás de Retrieval-Augmented Generation puede resumirse en
una frase.

> En lugar de enseñar permanentemente toda la información al modelo,
> recuperemos únicamente la información necesaria para responder la
> consulta actual.

Esta idea cambia completamente la arquitectura.

El conocimiento deja de almacenarse exclusivamente dentro de los
parámetros del modelo.

Parte del conocimiento permanece en repositorios externos y solo se
incorpora cuando resulta necesario.

------------------------------------------------------------------------

# Un cambio de paradigma

Con RAG el modelo deja de ser la única fuente de conocimiento.

La arquitectura pasa a estar formada por varios componentes que
colaboran entre sí.

El modelo continúa siendo responsable de comprender la consulta y
generar la respuesta.

Sin embargo, la recuperación de información queda delegada a un
mecanismo especializado.

Esta separación de responsabilidades aporta múltiples beneficios:

-   actualización inmediata de documentos;
-   reducción de costos;
-   mayor trazabilidad;
-   respuestas fundamentadas en fuentes concretas;
-   menor necesidad de reentrenamiento.

------------------------------------------------------------------------

# Caso real

Una organización pública mantiene miles de resoluciones administrativas
que cambian periódicamente.

Cada semana se incorporan nuevas versiones y se derogan procedimientos
anteriores.

Entrenar un modelo completo después de cada modificación sería
impracticable.

Con una arquitectura RAG, las resoluciones permanecen en un repositorio
documental.

Cuando un usuario realiza una consulta, el sistema recupera únicamente
los documentos relevantes y los incorpora al contexto del modelo.

La actualización ocurre sobre los documentos, no sobre el LLM.

------------------------------------------------------------------------

# Ideas clave

-   Un LLM no conoce automáticamente la información privada de una
    organización.
-   Reentrenar un modelo rara vez es la mejor solución.
-   RAG separa el conocimiento del modelo del conocimiento documental.
-   Retrieval-Augmented Generation es una arquitectura, no un modelo
    nuevo.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección analizaremos la arquitectura completa de un
sistema RAG y seguiremos el recorrido de una consulta desde que el
usuario formula una pregunta hasta que el modelo genera una respuesta
respaldada por información recuperada.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
