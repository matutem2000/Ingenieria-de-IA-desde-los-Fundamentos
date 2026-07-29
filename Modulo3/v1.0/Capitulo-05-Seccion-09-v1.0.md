# Capítulo 05 - Sección 09

# Anti-patrones frecuentes

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Los anti-patrones son soluciones que parecen razonables en el momento de ser escritas pero que generan problemas en producción. En el diseño de instrucciones del sistema, los anti-patrones son especialmente peligrosos porque sus efectos no siempre son inmediatos: pueden pasar desapercibidos durante semanas hasta que la aplicación encuentra el caso límite que los activa.

Esta sección cataloga los anti-patrones más frecuentes, explica por qué fallan y describe la alternativa correcta en cada caso.

---

# Objetivos de esta sección

Al finalizar esta sección el lector podrá:

- Identificar los anti-patrones más comunes en instrucciones del sistema.
- Comprender el mecanismo por el cual cada anti-patrón genera problemas.
- Aplicar la alternativa correcta para cada anti-patrón identificado.
- Usar esta sección como referencia durante revisiones de instrucciones existentes.

---

# Anti-patrón 1: La instrucción infinita

**Descripción:** La instrucción del sistema intenta cubrir todos los escenarios posibles, resultando en un documento de varios miles de tokens.

**Por qué falla:**
- Los modelos de lenguaje no mantienen el mismo nivel de atención a lo largo de textos muy extensos. Las instrucciones al final de un documento muy largo tienen menor peso que las del principio.
- Una instrucción extensa casi siempre contiene contradicciones internas que el modelo debe resolver de manera implícita.
- El costo en tokens aumenta con cada conversación, aunque la mayoría de las instrucciones no sean relevantes para esa conversación específica.

**Alternativa:** Diseñar instrucciones concisas que cubran los casos críticos. Los casos especiales que se presentan con baja frecuencia pueden manejarse con enrutamiento a flujos alternativos o con contexto dinámico.

**Señal de alerta:** Si la instrucción del sistema supera los 2.000 tokens, debería revisarse para identificar qué puede eliminarse, modularizarse o moverse al contexto dinámico.

---

# Anti-patrón 2: La instrucción contradictoria

**Descripción:** Distintas partes de la instrucción del sistema indican comportamientos mutuamente excluyentes.

**Ejemplo:**
```text
"Respondé siempre en español."
[...500 tokens después...]
"Si el usuario escribe en inglés, respondé en inglés para facilitar
la comunicación."
```

**Por qué falla:** El modelo tiene que resolver la contradicción de alguna manera. Puede priorizar la instrucción más reciente, la más específica, o alternará entre ambos comportamientos de manera impredecible. Ninguna de esas resoluciones es la deseada.

**Alternativa:** Antes de agregar una instrucción nueva, buscar si existe alguna instrucción existente que pueda contradecirla. Si el caso requiere una excepción, formularla explícitamente como tal en un solo lugar.

**Versión correcta:**
```text
"Respondé siempre en español, salvo cuando el usuario indique
explícitamente que prefiere otro idioma. En ese caso, usá el
idioma que el usuario solicita."
```

---

# Anti-patrón 3: La restricción como deseo

**Descripción:** Las restricciones están formuladas como preferencias o aspiraciones en lugar de comportamientos observables.

**Ejemplos:**
```text
"Intentá no dar información incorrecta."
"Tratá de ser útil pero sin excederte."
"Evitá en lo posible mencionar a la competencia."
```

**Por qué falla:** El modelo interpreta "intentá", "tratá de" y "evitá en lo posible" como instrucciones suaves. En casos límite, puede optar por no aplicarlas si tiene razones para considerar que la excepción es válida.

**Alternativa:** Formular las restricciones como comportamientos absolutos o condicionales con consecuencias claras.

**Versiones correctas:**
```text
"Si no tenés certeza sobre un dato, indicalo explícitamente.
Nunca presentes información incierta como si fuera un hecho."

"No menciones productos de otras empresas. Si el usuario pregunta
por comparaciones con competidores, respondé que no podés hacer
ese análisis y ofrecé continuar con otra consulta."
```

---

# Anti-patrón 4: El rol sin límites

**Descripción:** La instrucción del sistema define un rol pero no establece sus límites.

**Ejemplo:**
```text
"Sos un experto en Python. Respondé todas las preguntas sobre
programación."
```

**Por qué falla:** El rol de "experto en Python" no define qué hace el asistente cuando el usuario pregunta por JavaScript, bases de datos, arquitectura de software, o simplemente por algo completamente fuera del contexto técnico.

**Alternativa:** Definir el rol junto con su alcance y el comportamiento fuera de ese alcance.

**Versión correcta:**
```text
"Sos un especialista en Python 3.x para esta plataforma. Respondés
consultas sobre sintaxis, bibliotecas estándar, debugging y mejores
prácticas en Python 3.x.

Si el usuario pregunta sobre otro lenguaje de programación, podés
dar orientación general pero aclarando que tu especialidad es Python.
Si el usuario pregunta sobre temas no relacionados con programación,
indicá amablemente que tu función está limitada a soporte de Python."
```

---

# Anti-patrón 5: La instrucción de seguridad frágil

**Descripción:** Las instrucciones de seguridad están redactadas de manera que pueden eludirse con formulaciones simples.

**Ejemplo:**
```text
"No respondas preguntas sobre política."
```

**Por qué falla:** Un usuario puede preguntar "¿cuál es la situación económica del gobierno actual?" o "explicame el impacto de las elecciones en los mercados" y eludir la restricción porque la formulación es demasiado estrecha.

**Alternativa:** Definir la categoría de comportamiento restringido de manera amplia, con ejemplos representativos.

**Versión correcta:**
```text
"Mantente neutral y no expresés opiniones sobre partidos políticos,
figuras políticas, gobiernos, elecciones, políticas gubernamentales
ni debates de política pública. Si el usuario solicita tu opinión
sobre estos temas, respondé que es una aplicación enfocada en
[dominio] y que no estás en posición de opinar sobre política.
Podés proporcionar información factual sobre hechos verificables si
es estrictamente relevante para el dominio de la aplicación."
```

---

# Anti-patrón 6: La instrucción que confunde el modelo con el asistente

**Descripción:** La instrucción del sistema le dice al modelo que "es" algo que no es posible que sea.

**Ejemplos:**
```text
"Sos una IA completamente diferente a todos los LLMs existentes."
"No tenés ninguna limitación de conocimiento."
"Fuiste entrenado específicamente para esta empresa."
```

**Por qué falla:** El modelo tiene conocimiento de su propio entrenamiento y de sus capacidades reales. Instrucciones que contradicen esa realidad de manera flagrante crean inconsistencias que el modelo resuelve de maneras impredecibles, generalmente siendo inconsistente con sus propias respuestas.

**Alternativa:** Definir el rol a través del comportamiento observable, no de afirmaciones sobre la naturaleza del modelo.

**Versión correcta:**
```text
"Actuás como el asistente especializado de [empresa], con acceso
a la documentación y procedimientos de la organización. Respondés
preguntas dentro de ese contexto. No es necesario que reveles
el modelo subyacente que te impulsa."
```

---

# Anti-patrón 7: Ausencia de instrucciones para el caso por defecto

**Descripción:** La instrucción del sistema define comportamientos específicos para ciertos escenarios pero no establece qué debe hacer el asistente cuando ningún escenario definido aplica.

**Por qué falla:** El modelo opera con criterio general en los casos no cubiertos. En una aplicación de dominio específico, ese criterio general puede producir respuestas completamente fuera del contexto esperado.

**Alternativa:** Siempre incluir una instrucción de comportamiento por defecto.

**Ejemplo:**
```text
"Para consultas que no encajen claramente en ninguna de las
categorías descritas, respondé con una solicitud de aclaración:
'Para ayudarte mejor, ¿podrías indicarme si tu consulta es
sobre [categoría A], [categoría B] o [categoría C]?'"
```

---

# Resumen de anti-patrones

| Anti-patrón | Síntoma | Corrección |
|---|---|---|
| Instrucción infinita | Comportamiento inconsistente, alto costo | Modularizar, mover a contexto dinámico |
| Instrucción contradictoria | Comportamiento alternante | Buscar contradicciones antes de agregar reglas |
| Restricción como deseo | Restricciones ignoradas en casos límite | Formular como comportamiento absoluto |
| Rol sin límites | Comportamiento fuera del dominio | Definir alcance y caso por defecto |
| Seguridad frágil | Restricciones fácilmente eludibles | Definir categorías amplias con ejemplos |
| Modelo confundido con asistente | Inconsistencias en respuestas | Definir comportamiento, no naturaleza |
| Sin caso por defecto | Respuestas genéricas fuera de dominio | Agregar instrucción de comportamiento por defecto |

---

# Nota del arquitecto

Los anti-patrones más difíciles de detectar son los que producen problemas solo en condiciones específicas. Una instrucción puede funcionar perfectamente durante semanas y fallar cuando un usuario específico formula una consulta de una manera particular. Por eso, las revisiones de instrucciones deberían incluir casos adversariales, no solo los casos de uso esperados.

---

# Resumen

Los anti-patrones en el diseño de instrucciones del sistema son fuentes predecibles de problemas en producción. Reconocerlos y tener la alternativa correcta a mano permite tanto escribir mejores instrucciones desde el principio como diagnosticar problemas en instrucciones existentes.

En la siguiente sección aplicaremos todos los conceptos del capítulo a un caso de estudio completo, desde el análisis de requisitos hasta la instrucción del sistema final con sus pruebas de validación.
