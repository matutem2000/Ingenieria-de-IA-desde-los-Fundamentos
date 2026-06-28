# Capitulo-12-Seccion-03-v1.0

# Capítulo 12 --- Mitos sobre la Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"La confianza en una respuesta nunca debe reemplazar la validación de
> la información."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Comprender por qué un modelo puede generar información incorrecta
    con aparente seguridad.
-   Diferenciar precisión lingüística de veracidad.
-   Analizar el fenómeno de las alucinaciones desde una perspectiva de
    ingeniería.
-   Incorporar estrategias para reducir este riesgo en soluciones
    empresariales.

------------------------------------------------------------------------

# El mito: "La IA siempre dice la verdad"

Una respuesta bien redactada suele transmitir confianza. En los modelos
generativos, esa percepción puede inducir a un error frecuente: asumir
que toda respuesta correcta desde el punto de vista gramatical también
es correcta desde el punto de vista factual.

Los Large Language Models (LLM) no verifican automáticamente la
veracidad de cada afirmación. Su objetivo consiste en producir la
secuencia de tokens más probable dadas las entradas y el conocimiento
adquirido durante el entrenamiento.

Por ese motivo pueden construir respuestas coherentes que contengan
datos inexistentes, referencias incorrectas o conclusiones
injustificadas.

------------------------------------------------------------------------

# ¿Qué es una alucinación?

En ingeniería de IA se denomina *alucinación* a la generación de
contenido plausible pero incorrecto.

No implica un fallo del software en el sentido tradicional.

Es una consecuencia esperable de un sistema probabilístico que debe
responder incluso cuando no dispone de información suficiente.

``` mermaid
flowchart TD
A[Consulta del usuario] --> B{Existe evidencia suficiente?}
B -->|Sí| C[Respuesta fundamentada]
B -->|No| D[Estimación probabilística]
D --> E[Posible alucinación]
```

------------------------------------------------------------------------

# Caso de estudio

Una empresa integra un asistente para responder preguntas sobre
contratos históricos.

Durante una auditoría, el sistema cita una cláusula contractual que
nunca existió.

El texto era convincente, incluía numeración y lenguaje jurídico
apropiado, pero la referencia había sido completamente inventada.

La causa no fue un error de programación, sino la ausencia de un
mecanismo de recuperación documental que limitara las respuestas al
contenido realmente disponible.

------------------------------------------------------------------------

# Buenas prácticas

-   Incorporar Retrieval-Augmented Generation (RAG) cuando la exactitud
    sea prioritaria.
-   Mostrar las fuentes utilizadas para construir la respuesta.
-   Establecer umbrales de confianza cuando sea posible.
-   Permitir que el usuario solicite evidencia documental.

------------------------------------------------------------------------

# Errores frecuentes

  -----------------------------------------------------------------------
  Error                             Impacto
  --------------------------------- -------------------------------------
  Confiar ciegamente en la          Información incorrecta en producción
  respuesta                         

  No exigir fuentes                 Difícil auditoría

  Utilizar IA sin validación en     Riesgos legales y operativos
  dominios críticos                 
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Ideas clave

-   Fluidez no implica veracidad.
-   Las alucinaciones forman parte del comportamiento esperado de un
    modelo generativo.
-   La arquitectura debe incorporar mecanismos para reducir y detectar
    este riesgo.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos otro mito ampliamente difundido: la
idea de que la Inteligencia Artificial reemplazará completamente a los
desarrolladores y arquitectos de software.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
