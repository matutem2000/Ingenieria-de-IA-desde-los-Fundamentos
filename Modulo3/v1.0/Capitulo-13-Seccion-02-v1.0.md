# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 02: Métricas de calidad y desempeño

Una métrica es útil solo si está vinculada a una decisión. Una colección de números sin un criterio de interpretación no es observabilidad; es ruido con formato de dashboard. Antes de instrumentar un sistema de IA, el AI Engineer debe responder dos preguntas para cada métrica que planea recolectar: ¿qué indica esta métrica cuando es alta? ¿qué acción se toma cuando cruza un umbral?

Esta sección cataloga las métricas de los sistemas de IA en dos categorías: métricas operacionales, que miden el comportamiento técnico del sistema, y métricas de calidad, que miden el valor que el sistema entrega. Ambas categorías son necesarias. Ninguna es suficiente por sí sola.

### Métricas operacionales

Las métricas operacionales describen cómo se comporta el sistema como infraestructura técnica. Son análogas a las métricas de cualquier sistema distribuido y, en su mayoría, pueden recolectarse con herramientas de observabilidad estándar.

**Tiempo al primer token (TTFT, Time To First Token).** El tiempo que transcurre desde que la solicitud llega al sistema hasta que el modelo comienza a generar su respuesta. Es la métrica de latencia percibida más relevante para el usuario en sistemas con streaming. Un TTFT alto —típicamente por encima de 2-3 segundos en aplicaciones interactivas— produce la percepción de sistema lento aunque el total de tokens se genere rápidamente. El TTFT depende de la latencia de red, el tiempo de procesamiento previo a la inferencia (recuperación RAG, ensamblado del contexto) y la carga del proveedor del modelo.

**Tokens por segundo (TPS, Tokens Per Second).** La velocidad de generación de tokens una vez iniciada la respuesta. Determina si el streaming de la respuesta se percibe fluido o interrumpido. Los modelos grandes son inherentemente más lentos que los modelos pequeños; la elección del modelo tiene un efecto directo en esta métrica.

**Latencia de extremo a extremo (p50, p95, p99).** El tiempo total desde la solicitud hasta la respuesta completa, en percentiles. El p50 describe el caso típico; el p95 y p99 describen los casos lentos que, aunque infrecuentes, determinan la experiencia de los usuarios más afectados. En sistemas de IA, la cola de distribución de latencia tiende a ser más larga que en sistemas tradicionales porque las solicitudes largas o los contextos complejos generan respuestas mucho más largas que la mediana.

**Tokens por solicitud (input y output).** Cuántos tokens consume el contexto de entrada (system prompt, historial, documentos recuperados, consulta del usuario) y cuántos produce la respuesta. Esta métrica tiene dos usos: calcular el costo por solicitud y detectar anomalías. Un pico inusual en los tokens de entrada puede indicar que el sistema RAG está recuperando demasiados documentos, que el historial de conversación creció sin control, o que se inyectó contenido inesperado en el contexto.

**Costo por solicitud y costo por usuario activo.** El costo en dólares de cada llamada al modelo, calculado a partir del número de tokens y el precio del proveedor. En sistemas de IA de producción, el costo es una restricción operativa real. Un sistema que aumenta su volumen diez veces sin que el costo escale proporcionalmente indica eficiencias en el uso del contexto. Un sistema cuyo costo escala más que el volumen indica un problema de context bloat que debe investigarse.

**Tasa de errores técnicos.** El porcentaje de solicitudes que fallan por razones técnicas: límites de la API del proveedor (rate limits), errores de red, timeouts, contextos que superan la ventana máxima del modelo. Distinguir el tipo de error es importante: un pico de errores por rate limit indica que el sistema necesita implementar backoff o distribuir la carga; un pico de errores por contexto demasiado largo indica que la estrategia de construcción del contexto está generando prompts que exceden la capacidad del modelo.

### Métricas de calidad

Las métricas de calidad miden si las respuestas del sistema son buenas, no solo si el sistema responde. Son más difíciles de recolectar que las métricas operacionales porque la calidad de una respuesta de lenguaje natural no puede calcularse con una fórmula aritmética. Sin embargo, existen aproximaciones prácticas que permiten estimar la calidad a escala.

**Relevancia de la respuesta.** En qué medida la respuesta del sistema aborda la consulta del usuario. Una respuesta relevante responde lo que se preguntó. Una respuesta irrelevante puede ser factualmente correcta sobre un tema diferente al que se preguntó. La relevancia puede estimarse automáticamente usando modelos de scoring o mediante evaluación humana.

**Fundamentación en el contexto (groundedness).** En qué medida la respuesta está soportada por el conocimiento disponible en el contexto que recibió el modelo. Una respuesta groundada extrae información del contexto; una respuesta no groundada introduce información que no estaba en el contexto —lo que en el dominio de IA se denomina alucinación—. Esta métrica es especialmente crítica en sistemas RAG: si el sistema recupera documentos correctos pero el modelo genera respuestas que no se derivan de esos documentos, hay un problema de groundedness.

**Exactitud factual.** En qué medida las afirmaciones de la respuesta son correctas respecto al conocimiento real. La exactitud factual es la métrica más difícil de medir automáticamente porque requiere una referencia de verdad de la que muchas veces no se dispone. En sistemas con un dominio acotado y bien documentado —manuales de productos, políticas corporativas, bases de conocimiento técnico— la exactitud puede evaluarse comparando la respuesta contra las fuentes autorizadas.

**Coherencia y completitud.** Si la respuesta es internamente consistente (no se contradice entre sí), si tiene el nivel de detalle apropiado para la consulta (ni demasiado escueta ni innecesariamente extensa), y si respeta las restricciones de formato y tono definidas en el system prompt.

**Satisfacción del usuario.** La métrica de calidad más directa es si el usuario quedó satisfecho con la respuesta. Esta puede aproximarse de varias formas: la tasa de conversaciones que terminan sin que el usuario reformule o escale, las calificaciones explícitas si el sistema las solicita (thumbs up/thumbs down), el ratio de sesiones que continúan después de la primera respuesta como señal de engagement.

### El problema de las métricas universales de calidad

Una advertencia importante: las métricas de calidad no son universales. La calidad correcta para un asistente de atención al cliente no es la misma que para un asistente de análisis legal ni para un generador de código. El criterio de "relevancia" en un sistema de soporte técnico exige respuestas directas y accionables; en un sistema de análisis de contratos, exige exhaustividad y matices.

El AI Engineer no puede tomar prestado un conjunto de métricas de otro proyecto y aplicarlo sin adaptación. El proceso correcto es:

1. Definir con el equipo de negocio qué significa "una buena respuesta" para este caso de uso específico.
2. Traducir esa definición en criterios observables.
3. Diseñar las métricas que operacionalizan esos criterios.
4. Establecer los umbrales de alerta en función de los datos reales del sistema en producción, no de valores abstractos.

### Tabla de métricas de referencia

| Métrica | Categoría | Cómo se mide | Umbral de alerta típico |
|---|---|---|---|
| TTFT | Operacional | Timestamp primera respuesta - timestamp solicitud | > 3 segundos en aplicaciones interactivas |
| Latencia p95 | Operacional | Percentil 95 del tiempo de respuesta completo | Varía por caso de uso; establecer en baseline |
| Tokens de entrada p95 | Operacional | Tokens del prompt en percentil 95 | > 80% de la ventana de contexto del modelo |
| Tasa de errores técnicos | Operacional | Errores / solicitudes totales | > 1% en producción |
| Costo por solicitud | Operacional | Tokens × precio del proveedor | Desviación > 20% del baseline |
| Relevancia | Calidad | Evaluación automática o humana (0-1) | < 0.80 en promedio semanal |
| Groundedness | Calidad | Evaluación automática (0-1) | < 0.85 en promedio semanal |
| Satisfacción del usuario | Calidad | Rating explícito o señal implícita | Caída > 10 puntos desde el baseline |

Los valores de la columna "Umbral de alerta típico" son puntos de partida, no verdades absolutas. El equipo debe calibrarlos contra el comportamiento observado del sistema en las primeras semanas de producción.

### El scorecard operativo de un sistema de IA

La forma más práctica de gestionar estas métricas en un equipo de operaciones es un scorecard: una vista condensada que muestra el estado del sistema en cada dimensión, con un indicador de tendencia (mejorando, estable, deteriorando) y un flag de alerta cuando alguna métrica cruza su umbral.

```
SCORECARD SEMANAL — Sistema RAG de Soporte al Cliente

DIMENSIÓN OPERACIONAL
  Latencia p50:     820ms  ↔ (estable)
  Latencia p95:    2,150ms ↑ (subiendo — revisar)
  Tasa de errores:  0.3%   ↔ (estable)
  Costo/solicitud:  $0.004 ↔ (estable)

DIMENSIÓN DE CALIDAD
  Relevancia:       0.83   ↔ (estable)
  Groundedness:     0.78   ↓ (ALERTA — cayó 0.08 pts)
  Satisfacción:     72%    ↓ (cayó 5 pts — investigar)

INCIDENTES ESTA SEMANA
  Martes 14:30 — Pico de errores rate limit (6 minutos)
  Jueves 09:00 — 3 respuestas con groundedness < 0.50 detectadas
```

Este formato permite que el equipo de operaciones identifique en segundos qué está funcionando y qué requiere atención. Las secciones siguientes describen cómo se producen los valores de calidad de este scorecard: a través de pipelines de evaluación automática y humana.

### Nota del arquitecto

El error más común en la definición de métricas no es elegir las métricas incorrectas —eso se puede corregir con el tiempo—. Es no conectar las métricas con acciones. Si el equipo define "groundedness < 0.80" como umbral de alerta pero no tiene un proceso definido de respuesta para cuando ese umbral se cruce, la alerta es ruido. Cada umbral de alerta debe tener asociada una acción: quién investiga, con qué prioridad, qué playbook sigue.

El diseño de las métricas y el diseño de los procesos de respuesta son inseparables. Un scorecard sin procesos de respuesta es un tablero decorativo.

La siguiente sección describe cómo producir los valores de las métricas de calidad: las técnicas de evaluación automática y humana que permiten medir, a escala, si las respuestas del sistema son buenas.
