# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 11: Laboratorio práctico

Este laboratorio tiene un objetivo específico: diseñar un framework de observabilidad completo para un caso de uso concreto, antes de que ese sistema entre en producción. El ejercicio no requiere código. Requiere tomar decisiones de diseño —qué se mide, cómo se mide, qué umbrales se usan, qué acciones corresponden a cada umbral— que son las decisiones que determinan si el sistema será operable o no.

### El caso de uso

Se va a diseñar la observabilidad para el siguiente sistema:

> **Asistente de soporte técnico para una empresa de software SaaS.** El asistente ayuda a los usuarios de la plataforma a resolver problemas de configuración, responder dudas sobre funcionalidades y guiar flujos de trabajo dentro del producto. Está basado en RAG con acceso a la documentación del producto, artículos de la base de conocimiento y guías de inicio rápido. Los usuarios interactúan mediante chat en la propia plataforma. El sistema recibe aproximadamente 3,000 consultas por día en horario laboral (8am-8pm). Una respuesta incorrecta o incompleta puede llevar al usuario a realizar configuraciones erróneas que afectan sus datos o flujos de trabajo.

### Parte 1: Definición de métricas

El primer paso es definir qué se mide y por qué. Para este caso de uso específico, el estudiante debe seleccionar y justificar cinco métricas de calidad y tres métricas operacionales.

**Tarea 1.1: Métricas operacionales (completar la tabla)**

| Métrica | Por qué es relevante para este caso | Cómo se calcula | Umbral de alerta propuesto |
|---|---|---|---|
| (métrica 1) | | | |
| (métrica 2) | | | |
| (métrica 3) | | | |

Consideraciones: el sistema opera en horario laboral con 3,000 consultas diarias, lo que equivale a aproximadamente 250 consultas por hora en pico. Los usuarios son profesionales que usan el producto para trabajo real. La latencia que consideran aceptable es diferente a la de un chatbot de entretenimiento.

**Tarea 1.2: Métricas de calidad (completar la tabla)**

| Métrica | Definición para este caso | Cómo se mide | Umbral de alerta propuesto |
|---|---|---|---|
| (métrica 1) | | | |
| (métrica 2) | | | |
| (métrica 3) | | | |
| (métrica 4) | | | |
| (métrica 5) | | | |

Consideraciones: una respuesta incorrecta sobre configuración puede llevar a errores que el usuario debe deshacer. El costo de una respuesta incorrecta es más alto que el de una respuesta incompleta que lleva al usuario a preguntar de nuevo.

### Parte 2: Diseño del golden set

El estudiante debe diseñar la estructura del golden set para este sistema: qué categorías de casos debe incluir, cuántos casos por categoría, y quiénes deben participar en su construcción.

**Tarea 2.1: Categorías del golden set**

Identifica al menos seis categorías de casos que el golden set debe cubrir para ser representativo del uso real del sistema:

1. (categoría 1 — descripción y ejemplos de consultas típicas)
2. (categoría 2)
3. (categoría 3)
4. (categoría 4)
5. (categoría 5)
6. (categoría 6)

**Tarea 2.2: Casos de borde y adversariales**

Identifica al menos tres tipos de casos de borde o adversariales que el golden set debe incluir:

1. (caso borde 1 — descripción y por qué es importante)
2. (caso borde 2)
3. (caso borde 3)

**Tarea 2.3: Proceso de construcción**

Describe brevemente:
- Quiénes deben participar en la construcción del golden set (¿solo el equipo técnico? ¿también miembros del equipo de soporte? ¿usuarios reales?)
- Con qué frecuencia debe actualizarse y bajo qué condiciones
- Cómo se determina que una respuesta en el golden set es "correcta"

### Parte 3: Framework de alertas

Diseña el framework de alertas para este sistema con tres niveles de severidad. Para cada nivel, define:

- Qué condiciones lo disparan (con los valores numéricos de los umbrales)
- Qué acción debe tomar el equipo
- En qué tiempo debe ocurrir la respuesta
- Quién es responsable de responder

**Nivel 1 — Logging:**
- Condiciones: (lista de métricas y umbrales)
- Acción: 
- Tiempo de respuesta:
- Responsable:

**Nivel 2 — Revisión activa:**
- Condiciones:
- Acción:
- Tiempo de respuesta:
- Responsable:

**Nivel 3 — Acción inmediata:**
- Condiciones:
- Acción:
- Tiempo de respuesta:
- Responsable:

### Parte 4: Playbook de un incidente específico

El equipo recibe el siguiente reporte del equipo de soporte:

> "Varios usuarios están reportando que el asistente les da instrucciones de configuración que no coinciden con lo que ven en la interfaz. Los pasos que describe el asistente no existen en la versión actual del producto."

Escribe el playbook de respuesta para este incidente específico, siguiendo la estructura:

1. **Primer paso: verificación** — ¿Qué datos verificas primero para confirmar el problema? ¿Qué herramienta o sistema usas?

2. **Identificación del alcance** — ¿Cómo determinas si el problema afecta a todas las consultas de configuración o solo a un tipo específico? ¿Qué datos necesitas?

3. **Diagnóstico de causa raíz** — ¿Cuáles son las tres hipótesis más probables para este tipo de problema? ¿Cómo descartarías o confirmarías cada una con los datos disponibles?

4. **Intervención** — Si la causa raíz es que la documentación en la base vectorial corresponde a una versión anterior del producto, ¿qué pasos concretos sigues para resolver el problema?

5. **Verificación de la solución** — ¿Cómo confirmas que el problema está resuelto? ¿Qué métricas monitorizas durante las siguientes 24 horas?

6. **Documentación** — ¿Qué escribes en el post-mortem? ¿Qué cambios en el proceso propones para evitar la recurrencia?

### Parte 5: Diseño del pipeline de evaluación

Diseña el pipeline de evaluación completo para este sistema. El diseño debe responder:

**Evaluación automática:**
- ¿Qué porcentaje del tráfico se evalúa automáticamente?
- ¿Qué modelo se usa como juez y por qué?
- ¿Cuál es el prompt de evaluación para la dimensión de groundedness? (escribe el prompt completo)
- ¿Con qué frecuencia se ejecuta el golden set?

**Evaluación humana:**
- ¿Qué casos se envían a evaluación humana?
- ¿Quién evalúa (miembro del equipo técnico, miembro del equipo de soporte, usuario experto)?
- ¿Con qué criterio se determina si una respuesta es correcta para este dominio?
- ¿Con qué frecuencia se calibra el evaluador automático contra las evaluaciones humanas?

### Respuestas de referencia

Las siguientes respuestas no son la única solución correcta, pero ilustran el nivel de detalle y el razonamiento esperado.

**Métricas operacionales propuestas:**

| Métrica | Por qué es relevante | Cómo se calcula | Umbral de alerta |
|---|---|---|---|
| Latencia p95 | Los usuarios profesionales tienen baja tolerancia a esperas. P95 captura los casos lentos que afectan la experiencia | Tiempo entre solicitud y respuesta completa, percentil 95 | > 4 segundos (el doble del p50 esperado de ~2s) |
| Tasa de errores técnicos | Las interrupciones de servicio durante horario laboral tienen impacto directo en la productividad | Errores / total de solicitudes | > 0.5% (umbral bajo dado el impacto en trabajo real) |
| Tokens de contexto p95 | Un contexto que crece sin control indica problemas de compresión o documentos excesivamente largos recuperados | Tokens totales del prompt, percentil 95 | > 75% de la ventana de contexto del modelo |

**Métricas de calidad propuestas:**

| Métrica | Definición para este caso | Cómo se mide | Umbral de alerta |
|---|---|---|---|
| Groundedness | Cada instrucción de configuración debe poder rastrearse hasta la documentación actual | LLM-as-judge, muestra del 15% | < 0.85 (más estricto que el promedio; errores de config tienen alto costo) |
| Exactitud de versión | Las instrucciones corresponden a la versión actual del producto | Evaluación humana periódica + comparación con changelog | < 95% de exactitud en evaluación humana mensual |
| Relevancia | La respuesta aborda la consulta específica del usuario | LLM-as-judge, mismo 15% de muestra | < 0.82 en promedio semanal |
| Tasa de reformulación | El usuario reformuló su pregunta (señal de que la primera respuesta no satisfizo) | Análisis del historial de conversación | > 20% de conversaciones con reformulación en 48h |
| Tasa de escalación | El usuario solicitó hablar con un agente humano después de interactuar con el asistente | Log de eventos de escalación | > 15% del total de conversaciones |

### Nota al instructor

Este laboratorio puede adaptarse a cualquier caso de uso: un asistente de análisis financiero, un asistente legal, un sistema de recomendación de productos. La estructura del ejercicio —definir métricas, diseñar el golden set, crear el framework de alertas, escribir el playbook, diseñar el pipeline de evaluación— es transferible a cualquier sistema de IA en producción. El valor pedagógico está en forzar las decisiones de diseño antes de que el sistema exista, cuando es más fácil pensar con claridad que después de que el primer incidente de producción ocurre.
