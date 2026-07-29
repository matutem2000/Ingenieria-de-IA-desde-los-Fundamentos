# Capítulo 10 — Planificación y Razonamiento

## Sección 02: Qué significa razonar en un LLM

Antes de diseñar un sistema de razonamiento, es necesario entender con precisión qué ocurre cuando un LLM produce lo que parece ser una cadena de razonamiento. Esta distinción conceptual no es un ejercicio filosófico: tiene consecuencias directas sobre las decisiones de arquitectura y sobre lo que el ingeniero puede esperar del sistema.

### Razonamiento simbólico versus predicción de tokens

El razonamiento simbólico formal — el de la lógica deductiva, la demostración matemática o el planificador clásico de IA — opera sobre símbolos con semántica fija. Dado un conjunto de premisas y reglas de inferencia, el sistema produce conclusiones que son necesariamente correctas si las premisas son correctas. El proceso es determinista, verificable y explicable paso a paso.

Un LLM no opera de esa manera. Un modelo de lenguaje es, en su núcleo, una función de probabilidad condicional: dado el texto que precede al siguiente token, el modelo asigna una distribución de probabilidad sobre todos los tokens posibles y selecciona uno (o muestrea uno, según la temperatura configurada). Este proceso se repite token a token hasta que el modelo genera la secuencia completa de la respuesta.

No hay inferencia formal. No hay motor de reglas. No hay manipulación de símbolos con semántica garantizada. Lo que hay es una función estadística extremadamente compleja, entrenada sobre cantidades masivas de texto humano, que aprendió a producir secuencias de tokens que son consistentes con el contexto dado.

Cuando ese contexto incluye problemas con soluciones correctas — matemáticas, programación, razonamiento lógico — el modelo produce secuencias de tokens que, estadísticamente, se asemejan a las soluciones correctas que aparecían en sus datos de entrenamiento y en el contexto inmediato. El output parece razonado porque el razonamiento humano tiene patrones lingüísticos reconocibles, y el modelo los reproduce.

### Por qué esto importa para el diseño

Esta distinción tiene tres consecuencias prácticas inmediatas:

**Primera consecuencia: el modelo puede equivocarse con plena confianza.** Cuando un LLM afirma algo incorrecto, no está mintiendo ni fallando deliberadamente. Está produciendo la secuencia de tokens más probable dado su contexto, y esa secuencia puede ser factualmente incorrecta. No existe, en el modelo, un mecanismo que detecte la contradicción entre lo que afirma y la verdad del mundo. El arquitecto del sistema es quien debe añadir ese mecanismo externamente.

**Segunda consecuencia: el contexto determina la calidad del razonamiento.** Dado que el modelo predice tokens condicionado al contexto, la calidad del razonamiento que produce depende directamente de cómo se estructura ese contexto. Un prompt que incluye pasos de razonamiento intermedios induce al modelo a continuar con pasos similares. Un prompt que pregunta directamente por la respuesta final induce al modelo a saltar a ella, potencialmente omitiendo verificaciones necesarias. El diseño del contexto es el principal lever de control que tiene el AI Engineer sobre la calidad del razonamiento.

**Tercera consecuencia: el razonamiento no es introspección.** Cuando un modelo explica cómo llegó a una conclusión, esa explicación es una secuencia de tokens que el modelo genera después (o simultáneamente con) la conclusión. No es una descripción fiel del proceso computacional que produjo la respuesta. El modelo no tiene acceso privilegiado a sus propios pesos. La explicación es, también, predicción estadística. Esto tiene implicaciones importantes para los sistemas de verificación: no se puede confiar en que el modelo detecte sus propios errores simplemente pidiéndole que los explique.

### El razonamiento emergente y cómo aprovecharlo

Si el razonamiento de un LLM es predicción estadística, ¿qué lo hace útil en la práctica?

Lo que ocurre es que ciertos patrones de razonamiento son lo suficientemente frecuentes y consistentes en el texto humano que el modelo los reproduce con alta fidelidad. La lógica deductiva básica, la descomposición de problemas en subproblemas, la identificación de contradicciones, el reconocimiento de patrones en código — todo esto aparece repetidamente en el corpus de entrenamiento, y el modelo aprende a reproducir esos patrones de forma confiable.

Esto significa que el razonamiento de un LLM es robusto en los dominios donde el modelo tiene buena cobertura de entrenamiento y donde el razonamiento tiene patrones lingüísticos reconocibles. Y es frágil en problemas novedosos, en razonamiento numérico preciso sin herramientas de apoyo, o en cualquier dominio donde el modelo no tuvo exposición suficiente durante el entrenamiento.

La clave para el AI Engineer es no tratar al modelo como una caja de razonamiento general, sino como un sistema que, bajo las condiciones correctas de contexto, produce outputs de calidad razonable en dominios donde ha sido bien entrenado. El diseño del sistema debe complementar las capacidades del modelo con mecanismos externos — herramientas, verificación, reflexión — donde el modelo solo no es suficientemente confiable.

### Diagrama conceptual

```
RAZONAMIENTO SIMBÓLICO FORMAL
  Premisas → Reglas de inferencia → Conclusión (garantizada)
  Determinista | Verificable | Explicable

RAZONAMIENTO EN LLM
  Contexto → Predicción token-a-token → Secuencia de output
  Probabilístico | Estadístico | Emergente del entrenamiento

LO QUE EL ARQUITECTO CONTROLA:
  - El contenido y estructura del contexto
  - Los pasos intermedios que el modelo debe producir
  - La verificación externa del output
  - Las herramientas disponibles para complementar al modelo
```

### Nota del arquitecto

El error más costoso en la práctica no es sobreestimar las capacidades del modelo — los ingenieros con experiencia aprenden rápido a desconfiar de respuestas no verificadas. El error más costoso es infrautilizar el contexto: tratar al modelo como un oráculo que solo necesita la pregunta, cuando en realidad es un sistema que requiere que el contexto estructure el proceso de razonamiento. Un modelo mediocre con un contexto bien diseñado supera consistentemente a un modelo superior con un contexto pobre.

La siguiente sección presenta la taxonomía de patrones de planificación que el arquitecto puede usar para estructurar ese contexto de forma efectiva.
