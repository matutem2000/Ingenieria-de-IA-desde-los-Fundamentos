# Módulo 8 – Capítulo 06 – Sección 01

## Por qué hacer fine-tuning: casos donde el prompting no es suficiente

El fine-tuning es la técnica de mayor costo de ingeniería en el flujo de trabajo de modelos locales, y por esa razón debe ser la última opción en la secuencia de decisiones, no la primera. La secuencia correcta es: primero, prompt engineering con el modelo base; segundo, few-shot prompting con ejemplos en el contexto; tercero, RAG para inyectar conocimiento externo; y solo cuando todos estos han demostrado empíricamente alcanzar un plateau de rendimiento insuficiente, fine-tuning. Esta secuencia no es dogma sino economía: cada paso previo al fine-tuning es más rápido de implementar, más fácil de iterar y menos costoso de operar.

¿Qué evidencia indica que el prompting ha alcanzado su límite? La señal más clara es una curva de aprendizaje flat en el golden dataset: añadir más ejemplos al few-shot prompt ya no mejora el score de calidad en el golden set. La segunda señal es inconsistencia estructural: el modelo produce la respuesta correcta en el 85-90% de los casos pero falla en el 10-15% restante de una forma que no puede corregirse con instrucciones adicionales en el prompt. La tercera señal es el costo del contexto: cuando el few-shot prompting requiere 1.000-2.000 tokens de ejemplos en cada petición, el costo de tokens de entrada en producción puede superar el presupuesto proyectado, y un modelo fine-tuneado que "sabe" el comportamiento esperado sin necesitar esos ejemplos en cada petición es más económico.

Los escenarios concretos donde el fine-tuning aporta valor medible incluyen formatos de salida altamente específicos que el few-shot prompting no produce con consistencia suficiente para producción. Por ejemplo, un sistema de extracción de información médica que debe producir JSON con un schema de 40 campos específicos del dominio clínico: con few-shot prompting sobre un modelo general de 7B, la tasa de conformidad al schema puede estar entre el 82-88%; con fine-tuning sobre 2.000 ejemplos anotados, puede elevarse al 97-99%. Esta diferencia de tasa de error del 2-15% puede significar la diferencia entre un sistema usable y uno que requiere revisión manual constante.

El conocimiento de dominio muy especializado es otro escenario clásico: terminología médica interna de un hospital, el lenguaje de APIs propietarias de una empresa, los estilos de redacción de un medio de comunicación específico. Un modelo general "inventa" términos cuando no conoce la terminología exacta o produce respuestas plausibles pero incorrectas en el dominio especializado. El fine-tuning sobre documentación real del dominio internaliza ese vocabulario en los pesos del modelo, eliminando las alucinaciones de terminología que el prompting no puede resolver.

La eficiencia en inferencia es el caso de uso económico más convincente: un modelo de 7B fine-tuneado en una tarea específica puede igualar o superar a un modelo de 70B con few-shot prompting en esa tarea, con un costo de inferencia 10x menor. Para aplicaciones de alto volumen (millones de peticiones al mes), esta diferencia de costo puede financiar varios ciclos de fine-tuning con los ahorros generados en el primer mes de producción.

## Casos de uso donde el fine-tuning supera al prompting

- **Formato de salida estricto y consistente:** cuando se requiere que >98% de las respuestas sigan un schema JSON o un formato específico que el few-shot produce con 85-90% de consistencia; el fine-tuning puede elevar esto al 97-99%.
- **Dominio con terminología no en los datos de preentrenamiento:** sistemas legacy, APIs propietarias, jerga interna de la empresa; el modelo base "inventa" terminología; el fine-tuning sobre documentación real resuelve el problema.
- **Eficiencia en inferencia:** un modelo de 7B fine-tuneado puede igualar a un modelo de 70B con few-shot en la tarea específica; el costo de inferencia 10x menor justifica el costo único de fine-tuning.
- **Reducción de longitud del prompt:** una capacidad que requiere 500-1.000 tokens de contexto en few-shot puede reducirse a un system prompt de 50 tokens post fine-tuning, multiplicando el contexto efectivo disponible para datos de usuario.
- **Comportamiento ante edge cases:** el few-shot no garantiza comportamiento correcto en inputs que difieren del patrón de los ejemplos; el fine-tuning sobre un dataset diverso mejora la robustez ante entradas inesperadas.

> **Nota del Arquitecto:** La pregunta que siempre hago antes de aprobar un proyecto de fine-tuning es: "¿Has medido el rendimiento de GPT-4o con few-shot prompting en el golden dataset?" Si la respuesta es no, no estamos listos para fine-tuning. El modelo de frontera con few-shot es el upper bound de calidad alcanzable con prompting; si ese upper bound ya supera el umbral del producto, el camino más rápido es fine-tuning de un modelo más pequeño. Si no lo supera, el problema está en el diseño de la tarea o los datos, no en la técnica de adaptación.

El fine-tuning es la herramienta correcta en los escenarios identificados. Las secciones siguientes presentan las técnicas específicas de fine-tuning eficiente —LoRA, QLoRA y DPO— que permiten ejecutar este proceso en hardware de consumo sin los recursos de un laboratorio de investigación.

---
