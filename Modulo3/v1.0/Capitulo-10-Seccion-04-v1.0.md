# Capítulo 10 — Planificación y Razonamiento

## Sección 04: Chain of Thought, Tree of Thoughts y variantes

Las técnicas de esta sección son las implementaciones más influyentes de los patrones de planificación secuencial y ramificado. Aunque el Módulo 2 introdujo Chain of Thought como técnica de prompting, aquí se examina desde una perspectiva diferente y más relevante para el AI Engineer: no como técnica de prompting, sino como mecanismo de diseño del contexto en sistemas de agentes.

---

### Chain of Thought: del prompting a la arquitectura

**La perspectiva del Módulo 2** trató Chain of Thought (CoT) como una instrucción al modelo: incluir en el prompt la indicación de pensar paso a paso, o incluir ejemplos few-shot donde la respuesta mostraba el razonamiento intermedio. Eso es suficiente para un prompt individual.

**La perspectiva arquitectónica** va más allá. En un sistema de agentes, Chain of Thought no es una instrucción en un prompt: es la decisión de diseño de separar el razonamiento de la respuesta en llamadas distintas, de materializar los pasos intermedios como outputs que se incorporan al contexto de las llamadas siguientes.

Esta distinción importa porque tiene consecuencias en la observabilidad del sistema, en la capacidad de intervención y en la distribución de errores.

**Anatomía de un CoT arquitectónico:**

```
PASO 1 — LLAMADA DE RAZONAMIENTO
Prompt: "Eres un analista financiero. Aquí está el balance de una empresa:
[datos financieros]. Antes de emitir cualquier conclusión, identifica:
(a) los tres indicadores más relevantes para el sector,
(b) los valores de cada indicador en el periodo actual y anterior,
(c) la tendencia de cada indicador.
Responde solo con este análisis, sin conclusiones."

Output del modelo:
(a) Indicadores relevantes: ratio de liquidez, margen EBITDA, deuda/patrimonio.
(b) Ratio liquidez: 1.8 actual vs 2.3 anterior. Margen EBITDA: 12% vs 15%.
    Deuda/patrimonio: 0.65 vs 0.48.
(c) Tendencias: liquidez deteriorándose, margen comprimiéndose, apalancamiento aumentando.

PASO 2 — LLAMADA DE CONCLUSIÓN
Prompt: [sistema anterior] + [output del paso 1] + "Con base en el análisis
anterior, emite una evaluación de riesgo crediticio (bajo/medio/alto) y justifica
brevemente."

Output del modelo:
Evaluación: Riesgo medio-alto. La empresa muestra deterioro simultáneo en tres
indicadores clave durante el periodo. El aumento del apalancamiento combinado con
la compresión del margen reduce la capacidad de servicio de deuda.
```

**Qué ganó la separación en dos llamadas:**

1. El paso 1 es auditable de forma independiente. El equipo puede revisar si el análisis de indicadores es correcto sin revisar la conclusión.
2. Si el paso 1 comete un error, ese error es visible y puede corregirse antes de que llegue al paso 2.
3. El sistema puede configurarse para requerir aprobación humana entre los pasos, lo que es relevante en entornos con regulación o supervisión.
4. Los errores del paso 2 son más fáciles de diagnosticar porque el contexto que recibe es explícito y verificable.

**Cuándo Chain of Thought mejora la calidad y cuándo no:**

CoT mejora la calidad cuando la tarea tiene estructura de razonamiento multi-paso y el modelo tiende a saltar pasos intermedios en ausencia de instrucción explícita. Mejora la precisión en matemáticas aplicadas, análisis lógico, diagnóstico de problemas de código y análisis de múltiples factores.

CoT no mejora la calidad — y puede perjudicarla — en tareas de recuperación directa de información, en clasificación simple donde el modelo ya tiene alta precisión, o en tareas creativas donde la fluidez del razonamiento lineal inhibe la generación de ideas no convencionales. Un CoT mal diseñado puede también guiar al modelo por un camino de razonamiento incorrecto y hacer que llegue a una conclusión incorrecta con mayor confianza que si hubiera respondido directamente.

---

### Tree of Thoughts: razonamiento como búsqueda

Tree of Thoughts (ToT) es una arquitectura publicada en 2023 que formaliza el patrón de planificación ramificado. Su intuición central es que el razonamiento puede modelarse como un proceso de búsqueda sobre un árbol de estados, donde cada nodo es un pensamiento intermedio y los arcos son los pasos de razonamiento que conectan pensamientos.

**Los tres componentes del ToT:**

**1. Generación de pensamientos:** En cada nodo del árbol, el modelo genera múltiples pensamientos posibles. Un "pensamiento" es un fragmento coherente de razonamiento — una hipótesis, un enfoque, un paso de solución — que tiene sentido analizar de forma independiente.

**2. Evaluación de pensamientos:** Cada pensamiento generado se evalúa. La evaluación puede ser mediante una llamada separada al mismo modelo ("¿es este enfoque prometedor?"), mediante una función heurística diseñada para el dominio, o mediante ejecución directa (en el caso de código, verificar si compila y pasa tests básicos).

**3. Selección y continuación:** Los pensamientos con mejor evaluación se seleccionan para continuar. Los pensamientos descartados se podan. El proceso se repite hasta alcanzar una solución completa o un límite de profundidad.

**Ejemplo concreto — Diseño de una estrategia de migración de datos:**

```
NODO RAÍZ: "Diseñar estrategia para migrar 50 TB de datos de clientes de
sistema on-premise a cloud sin downtime."

NIVEL 1 — GENERACIÓN (3 pensamientos):
  A: "Migración por replicación continua: mantener ambos sistemas en sync
     durante la transición."
  B: "Migración por lotes nocturnos: procesar los datos fuera de horario pico
     durante 4 semanas."
  C: "Migración Blue-Green: crear entorno paralelo, migrar datos, hacer
     cutover atómico."

NIVEL 1 — EVALUACIÓN:
  A: Viable pero compleja de mantener; riesgo de divergencia de datos.
  B: Simple pero implica 28 días de datos en migración; riesgo acumulado.
  C: Más limpia para el cutover; requiere doble infraestructura durante transición.
  → Seleccionado: C (mejor balance riesgo/complejidad para el requisito de no downtime)

NIVEL 2 — GENERACIÓN (desde C, 2 variantes):
  C1: "Blue-Green con sincronización unidireccional (on-premise → cloud) durante
      el periodo de transición."
  C2: "Blue-Green con sincronización bidireccional para soporte de rollback completo."

NIVEL 2 — EVALUACIÓN:
  C1: Más simple; rollback requiere re-sincronizar en dirección inversa.
  C2: Rollback inmediato; pero doble la complejidad de sincronización.
  → Seleccionado: C2 si el requisito de rollback es crítico; C1 en caso contrario.

OUTPUT FINAL: Plan detallado para la variante seleccionada con estimación de
recursos, duración y criterios de cutover.
```

**El costo real del Tree of Thoughts:**

Para un árbol de profundidad 2 con factor de ramificación 3, el número de llamadas es:

- Nivel 1: 3 llamadas de generación + 1 llamada de evaluación = 4 llamadas
- Nivel 2: 2 llamadas de generación + 1 llamada de evaluación = 3 llamadas (continuando solo la rama seleccionada)
- Output final: 1 llamada
- Total: 8 llamadas

Si el factor de ramificación es 3 en todos los niveles y se evalúan todas las ramas en todos los niveles antes de podar:

- Nivel 1: 3 generaciones + 1 evaluación = 4
- Nivel 2: 9 generaciones + 1 evaluación = 10
- Total: 14+ llamadas

La latencia total es la suma de las latencias de todas las llamadas. Para sistemas de alto volumen o con requisitos de respuesta en tiempo real, ToT completo raramente es práctico. En la práctica, se usan versiones podadas agresivamente — 2 niveles máximo, 2-3 ramas, poda temprana.

---

### Variantes notables

**Self-Consistency:** Genera múltiples cadenas de razonamiento independientes para el mismo problema (varias llamadas paralelas con temperatura > 0) y selecciona la respuesta más frecuente entre ellas. Mejora la precisión en problemas con respuesta discreta (matemáticas, clasificación) sin la complejidad de la arquitectura ToT completa.

**ReAct (Reasoning + Acting):** Intercala pasos de razonamiento con acciones sobre herramientas. El modelo razona sobre qué herramienta usar, usa la herramienta, observa el resultado, razona sobre qué hacer a continuación. Es el patrón más común en agentes con herramientas porque combina razonamiento y ejecución en un ciclo natural.

**Plan-and-Execute:** Separa explícitamente la fase de planificación de la fase de ejecución. Una llamada inicial produce el plan completo; llamadas subsiguientes ejecutan cada paso del plan. La ventaja es que el plan puede ser revisado por un humano o por otro agente antes de ejecutarse.

### Nota del arquitecto

La elección entre CoT, ToT o sus variantes no es principalmente técnica: es económica. El AI Engineer debe estimar el valor del output (¿cuánto cuesta un error en producción?) y compararlo con el costo de la arquitectura de razonamiento (llamadas adicionales, latencia, complejidad de mantenimiento). Para la mayoría de los casos de uso empresariales, CoT arquitectónico con un paso de evaluación es el balance correcto. ToT completo se reserva para decisiones de alto valor donde el costo del error supera ampliamente el costo de las llamadas adicionales.

La siguiente sección examina cómo la planificación iterativa — el patrón 3 — implementa estos principios en un ciclo de ejecución continua.
