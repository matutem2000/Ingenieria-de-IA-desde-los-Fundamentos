# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 14: Autoevaluación

Las siguientes preguntas permiten verificar la comprensión de los conceptos centrales del capítulo. Las respuestas no son de memorización sino de aplicación: cada pregunta plantea un escenario y requiere razonar a partir de los principios estudiados.

---

**1.** Un desarrollador pega el siguiente prompt en su asistente de IA:

> "Escribe una función en Python que valide un número de tarjeta de crédito usando el algoritmo de Luhn."

El modelo genera una función correcta que implementa el algoritmo de Luhn. El desarrollador la integra directamente al módulo de pagos del proyecto. ¿Qué problemas puede haber en el código integrado, y qué contexto habría reducido esos problemas?

---

**2.** Un equipo tiene el siguiente workflow: el pipeline de CI/CD ejecuta una revisión automática de IA de cada PR. Si la IA no encuentra problemas, el PR se mergea automáticamente sin revisión humana. Si la IA encuentra problemas, un humano revisa.

Identifica los problemas de diseño de este workflow y propón un diseño alternativo.

---

**3.** Un AI Engineer diseña un sistema de debugging asistido para un equipo. El sistema recupera automáticamente el error de los logs de producción y se lo envía al modelo como prompt. Los desarrolladores reportan que el diagnóstico es "casi siempre superficial e inútil". Sin cambiar el modelo, ¿qué haría el AI Engineer para mejorar el sistema?

---

**4.** Un equipo tiene el siguiente archivo de instrucciones del proyecto:

```markdown
# Proyecto Backend
- Usamos Python
- El código debe ser limpio y legible
- Seguimos las mejores prácticas de programación
```

Evalúa la calidad de este archivo como contexto y reescríbelo para un proyecto de e-commerce ficticio con las características que consideres representativas.

---

**5.** Un desarrollador tiene la especificación de una función: "Calcular el precio de envío de un pedido según el peso y la zona de destino, aplicando tarifas de una tabla de precios del courier." El desarrollador quiere usar IA para generar la función. Lista en orden los elementos de contexto que incluirías en el prompt, justificando por qué cada uno es necesario.

---

**6.** Un equipo con 8 desarrolladores quiere implementar Context Engineering en su proyecto. El proyecto tiene 5 años de antigüedad, 220.000 líneas de código y documentación desactualizada. El AI Engineer tiene presupuesto para dedicar 2 semanas a la implementación inicial. ¿Qué haría en esas 2 semanas para maximizar el impacto?

---

**7.** Diferencia, con un ejemplo concreto para cada caso, entre:
- Un uso de IA en diseño de arquitectura donde el modelo amplifica el trabajo del arquitecto
- Un uso de IA en diseño de arquitectura donde el modelo está siendo usado como árbitro de la decisión

¿Cuál es el problema del segundo caso?

---

**8.** El laboratorio de la sección 11 demostró que el diagnóstico de un bug se volvió más preciso a medida que se agregaban capas de contexto. ¿En qué orden se deben agregar esas capas, y por qué ese orden específico?

---

**9.** Un equipo reporta la siguiente experiencia: "Cuando usamos la IA para generar tests de una función nueva, los tests siempre pasan. Pero cuando hay bugs en producción, los tests no los detectan." ¿Cuál es la causa más probable de este problema, y cómo lo corregirías desde el Context Engineering?

---

**10.** ¿Por qué el capítulo recomienda que las revisiones automáticas de IA en el pipeline de CI/CD sean informativas (generan comentarios) y no bloqueantes (detienen el pipeline hasta aprobación del modelo)?

---

### Respuestas orientativas

**1.** La función puede ser correcta en abstracto pero incorrectamente integrada al proyecto: usa tipos de datos incorrectos (str en lugar del tipo personalizado CardNumber del proyecto), no usa las excepciones del dominio de pagos, no incluye logging, no sigue las convenciones de naming del proyecto. El contexto que habría reducido estos problemas: el módulo de pagos existente, las clases del dominio de pagos, las excepciones custom, el archivo de instrucciones del proyecto.

**2.** Problemas: falsos negativos del modelo (no detecta problemas que existen) llevan a merges sin revisión; el modelo no tiene suficiente contexto del sistema para detectar todos los problemas. Diseño alternativo: la revisión de IA genera comentarios en el PR para el revisor humano; la aprobación final siempre requiere un humano con conocimiento del sistema; el modelo es una capa de asistencia al revisor, no un árbitro.

**3.** El sistema envía solo el error — el contexto mínimo. El AI Engineer agregaría: el stack trace completo, el código de las funciones del stack trace, el historial de commits recientes de esos archivos, los tests que fallan. El sistema podría automatizar este ensamblaje mediante un script que, dado el error de los logs, recupera automáticamente esos elementos del repositorio.

**4.** El archivo original es demasiado genérico para ser útil al modelo. Un archivo efectivo especifica el stack con versiones, las convenciones concretas (no "código limpio" sino "type hints obligatorios, Decimal para valores monetarios"), los patrones de diseño adoptados y las instrucciones específicas para el asistente.

**5.** En orden: (1) el módulo donde se insertará el código — orienta al modelo sobre el dominio; (2) la tabla de precios del courier y cómo está representada en el sistema — el modelo necesita la estructura de datos real; (3) la clase Order o los parámetros de entrada — el modelo necesita los tipos que recibirá la función; (4) funciones similares existentes en el módulo — el modelo puede seguir el mismo patrón; (5) los tests que debe pasar — si existen; (6) las convenciones del proyecto — vía archivo de instrucciones.

**6.** La inversión de mayor impacto con 2 semanas: (1) Crear el archivo de instrucciones del proyecto a partir de la documentación existente, el código y entrevistas breves con los desarrolladores sénior (1 semana); (2) Estandarizar los flujos de trabajo de debugging y revisión de PR, con el archivo de instrucciones como base (3 días); (3) Capacitar al equipo con un workshop práctico sobre cómo usar el contexto correctamente (2 días). No es recomendable invertir esas 2 semanas en infraestructura técnica compleja (sistemas de RAG, indexación avanzada) hasta que los fundamentos estén funcionando.

**7.** Amplificación: el arquitecto propone un diseño y le pide al modelo que identifique riesgos no considerados y alternativas que no evaluó. El arquitecto usa ese output para revisar su decisión. Árbitro: el arquitecto presenta dos alternativas y le pregunta al modelo "¿cuál es mejor?", y adopta la respuesta como la decisión. El problema del segundo caso: el modelo puede no tener el contexto organizacional, las capacidades del equipo y las restricciones tácitas que hacen que una alternativa sea superior en ese proyecto específico.

**8.** El orden correcto es el que agrega valor diagnóstico con cada capa: primero el síntoma (reporte + test fallido), que define qué se está buscando; después el código, que revela el mecanismo potencial; después el historial de cambios, que revela cuándo se introdujo el problema; después el diff específico, que permite verificar la hipótesis. El orden importa porque cada capa informa qué buscar en la siguiente.

**9.** La causa más probable: los tests se generaron con solo el código en el contexto, sin la especificación funcional. Los tests verifican el comportamiento del código actual (que puede tener bugs) en lugar de verificar el comportamiento esperado según la especificación. La corrección: generar tests con la especificación funcional en el contexto, no solo el código. Los tests deben describir el comportamiento esperado; si el código tiene bugs, los tests los detectarán porque difieren de la especificación.

**10.** El modelo puede tener falsos negativos — aprobar código con problemas porque el contexto disponible no incluía la información necesaria para detectarlos. Si la revisión es bloqueante y el modelo aprueba, el código llega a producción sin revisión. Si la revisión es informativa, el humano puede identificar problemas que el modelo no detectó. La revisión automática es una capa de asistencia adicional al proceso de revisión, no un reemplazo de él.

---

La siguiente y última sección del capítulo establece el puente hacia el capítulo 12 y el territorio que espera al lector.
