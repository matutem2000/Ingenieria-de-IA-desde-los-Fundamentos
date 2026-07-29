# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 06: Optimización continua de prompts y contexto

El Módulo 2 de este libro enseñó a construir prompts efectivos antes del despliegue: cómo estructurar las instrucciones del sistema, cómo usar few-shot examples, cómo diseñar el contexto para maximizar la calidad de la respuesta en condiciones de laboratorio. Esta sección aborda un problema diferente: cómo mejorar un sistema que ya está en producción, usando los datos reales que el sistema genera, para decisiones de optimización que ningún experimento de laboratorio puede replicar.

La diferencia es fundamental. En laboratorio, el ingeniero controla la distribución de consultas. En producción, los usuarios hacen las preguntas que tienen, no las que el ingeniero esperaba. Las consultas reales revelan áreas débiles del sistema que los conjuntos de prueba no cubren, patrones de uso no anticipados que la arquitectura original no optimizó, y oportunidades de mejora que solo son visibles cuando hay suficiente volumen de datos.

### El ciclo de optimización continua

La optimización continua de un sistema de IA en producción sigue un ciclo de cuatro etapas que se repiten indefinidamente.

**Etapa 1: Observar.** Recolectar las métricas de las cuatro dimensiones de observabilidad. Identificar los patrones anómalos: qué tipos de consultas producen scores de calidad más bajos, qué fragmentos de documentos se recuperan con mayor frecuencia y producen respuestas incorrectas, qué categorías de preguntas el agente resuelve con más pasos de los esperados, qué parte del día o de la semana concentra los picos de insatisfacción del usuario.

**Etapa 2: Formular hipótesis.** Traducir la observación en una hipótesis de causa y en una propuesta de intervención. La observación puede ser "las consultas sobre políticas de devolución tienen groundedness de 0.65, 20 puntos por debajo del promedio". La hipótesis es "el fragmento de documentos de política de devoluciones que se indexó está desactualizado y el sistema recupera información incorrecta". La intervención propuesta es "reindexar el documento de política de devoluciones actualizado y verificar si hay otros documentos de política con el mismo problema".

**Etapa 3: Intervenir y medir.** Implementar la intervención en el sistema —puede ser una actualización de la base vectorial, un cambio en el system prompt, un ajuste en el algoritmo de recuperación, o un cambio en el modelo— y medir su impacto usando las métricas de la etapa 1. Para que la medición sea rigurosa, la intervención debe compararse contra una base: el comportamiento del sistema antes del cambio.

**Etapa 4: Decidir y documentar.** Si la intervención mejoró las métricas objetivo sin degradar otras métricas, se consolida en producción. Si no mejoró, o mejoró una métrica a costa de otra, se evalúa si el trade-off es aceptable o si se necesita una hipótesis diferente. En cualquier caso, se documenta qué se hizo, con qué resultado, para construir una base de conocimiento institucional sobre el comportamiento del sistema.

### A/B testing para arquitecturas de contexto

El instrumento más riguroso para comparar dos versiones de una arquitectura de contexto es el A/B testing: exponer una fracción del tráfico de producción a la versión A del sistema (control) y la fracción restante a la versión B (variante), y comparar las métricas entre ambos grupos.

El A/B testing para sistemas de IA tiene particularidades que lo diferencian del A/B testing de interfaces de usuario.

**Las métricas de éxito son más ruidosas.** Un botón tiene una tasa de clic que se mide directamente. La calidad de una respuesta de IA requiere evaluación —automática o humana— que introduce ruido. Esto significa que los A/B tests de sistemas de IA necesitan muestras más grandes y duraciones más largas para producir resultados estadísticamente significativos.

**Los efectos de interferencia son posibles.** Si un usuario interactúa con el sistema múltiples veces y es asignado a versiones diferentes en distintas sesiones, su experiencia se contamina. El diseño correcto asigna usuarios —no solicitudes— a los grupos de forma consistente a lo largo del tiempo.

**Las métricas secundarias pueden divergir.** Una variante que mejora la relevancia puede aumentar la latencia porque el sistema de recuperación más sofisticado es más lento. Las decisiones deben considerar el conjunto de métricas, no solo la métrica primaria del experimento.

**Los efectos de aprendizaje del usuario existen.** Los usuarios aprenden a usar el sistema de cierta manera. Si la versión B requiere consultas formuladas de forma diferente para obtener mejores resultados, los usuarios de la versión B pueden tardar en adaptar su comportamiento, produciendo una ventaja inicial de la versión A que desaparece con el tiempo.

### Qué puede optimizarse con A/B testing

Las dimensiones de la arquitectura de contexto que pueden compararse mediante A/B testing son múltiples:

**Estrategias de recuperación.** Recuperar los K documentos más relevantes por score versus usar un umbral de score mínimo. Usar solo búsqueda semántica versus combinar búsqueda semántica con búsqueda léxica (BM25). Aplicar re-ranking posterior a la recuperación versus usar el ranking original del buscador vectorial.

**Configuración del contexto.** Incluir historial de conversación de 3 turnos versus 5 turnos. Incluir un preamble de orientación al modelo antes de los documentos versus no incluirlo. Comprimir el historial de conversación mediante resumen versus truncación directa.

**System prompt.** Versiones alternativas de las instrucciones del sistema que enfatizan diferentes aspectos de la respuesta esperada. Adición de few-shot examples versus system prompt sin ejemplos. Diferentes niveles de restricción sobre el dominio del asistente.

**Modelo.** Comparar el mismo sistema con modelos de diferente tamaño o familia. Esto es especialmente relevante para encontrar el punto donde el modelo más pequeño produce calidad suficiente a menor costo.

### El problema de la significancia estadística

Un error frecuente en la optimización de sistemas de IA es tomar decisiones basadas en diferencias de métricas que no son estadísticamente significativas. Si la versión A tiene groundedness de 0.83 y la versión B tiene groundedness de 0.85, la diferencia parece favorable a B. Pero si el intervalo de confianza del 95% de ambas métricas se superpone, esa diferencia puede deberse al azar y no a una diferencia real en el sistema.

El principio básico: no consolidar una intervención en producción hasta que la diferencia en las métricas primarias sea estadísticamente significativa. En la práctica, esto significa definir antes del experimento el tamaño de muestra necesario para detectar la diferencia mínima que se considera relevante para el negocio (el "effect size" mínimo detectable), y no evaluar el experimento hasta que ese tamaño de muestra se alcance.

Para sistemas de IA donde las métricas de calidad son ruidosas, los experimentos necesitan típicamente entre 500 y 2,000 solicitudes evaluadas por variante para producir resultados confiables. Los sistemas de bajo volumen de tráfico pueden requerir semanas para alcanzar ese tamaño de muestra.

### Optimización sin experimentación controlada: el análisis de subgrupos

En sistemas con volumen de tráfico insuficiente para A/B testing, o cuando la intervención es urgente y no puede esperar un experimento, el análisis de subgrupos puede guiar la optimización.

El análisis de subgrupos examina las métricas de los distintos tipos de consultas que el sistema recibe. Si las consultas del tipo "¿cuánto cuesta X?" tienen groundedness de 0.91, mientras que las consultas del tipo "¿cuál es la diferencia entre X e Y?" tienen groundedness de 0.69, el análisis de subgrupos indica que el problema de calidad está concentrado en las consultas comparativas, no en el sistema en general.

Este hallazgo puede guiar una intervención específica —por ejemplo, agregar documentos de comparación de productos a la base vectorial o modificar el system prompt para que el sistema solicite más contexto antes de responder consultas comparativas— sin necesitar un A/B test formal.

### Nota del arquitecto

La optimización continua no es una actividad que ocurre de vez en cuando cuando el sistema da problemas. Es un proceso regular, con cadencia definida —por ejemplo, una revisión semanal de métricas y una intervención mensual como mínimo— que convierte los datos de observabilidad en mejoras concretas del sistema. Los equipos que no tienen esta cadencia tienden a reaccionar solo cuando los problemas son graves, en lugar de detectarlos y corregirlos cuando son menores.

La optimización continua también requiere una cultura de experimentación honesta: estar dispuesto a concluir que una hipótesis no funcionó y documentar ese resultado sin sesgarlo para que parezca que funcionó. Los resultados negativos son tan informativos como los positivos. Un equipo que solo documenta los éxitos tiene un sesgo de confirmación que lo lleva a optimizar el sistema en la dirección equivocada.

La siguiente sección aborda el problema que aparece cuando la optimización no basta: cómo detectar que el sistema está degradándose de forma sistemática y qué tipos de respuesta corresponden a distintos niveles de severidad de degradación.
