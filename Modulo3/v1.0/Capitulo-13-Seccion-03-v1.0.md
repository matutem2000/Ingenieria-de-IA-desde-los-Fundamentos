# Capítulo 13 — Observabilidad, Evaluación y Optimización

## Sección 03: Evaluación automática y evaluación humana

Medir la calidad de las respuestas de un sistema de IA a escala es uno de los problemas más abiertos de la ingeniería de IA aplicada. Un sistema de producción puede recibir diez mil solicitudes por día. Revisar cada respuesta manualmente no es factible. Pero delegar toda la evaluación a un algoritmo automático introduce sesgos y limitaciones que pueden ocultar problemas reales.

La solución práctica no es elegir entre evaluación automática y evaluación humana; es diseñar un pipeline que usa cada tipo de evaluación donde tiene más valor y las combina de manera inteligente.

### Evaluación automática: LLM-as-judge

La técnica más adoptada para la evaluación automática de respuestas de sistemas de IA es el LLM-as-judge: usar un modelo de lenguaje como evaluador de las respuestas de otro modelo. La idea es directa. Si se tiene una consulta, el contexto que recibió el sistema y la respuesta que generó, un segundo modelo puede evaluar si esa respuesta es relevante, está fundamentada en el contexto y es factualmente correcta.

La implementación básica tiene tres componentes:

**El prompt de evaluación.** Define el criterio que el modelo evaluador debe aplicar. Por ejemplo:

```
Eres un evaluador de calidad para un sistema de soporte técnico.
Dada la consulta del usuario, el contexto disponible y la respuesta generada,
evalúa la respuesta en tres dimensiones:

1. RELEVANCIA (0-1): ¿La respuesta aborda directamente la consulta del usuario?
2. FUNDAMENTACIÓN (0-1): ¿Cada afirmación de la respuesta puede verificarse en el contexto?
3. COMPLETITUD (0-1): ¿La respuesta incluye toda la información del contexto que es relevante?

Proporciona un score numérico para cada dimensión y una justificación breve.

CONSULTA: {consulta}
CONTEXTO: {contexto_recuperado}
RESPUESTA: {respuesta_del_sistema}
```

**El modelo evaluador.** Puede ser el mismo modelo que produce las respuestas o un modelo diferente. En general, usar un modelo más capaz o diferente como evaluador reduce el riesgo de que el evaluador favorezca sistemáticamente el estilo de respuesta del modelo evaluado.

**El pipeline de ejecución.** El proceso automatizado que toma una muestra de las solicitudes de producción, construye el prompt de evaluación para cada una y ejecuta el modelo evaluador. Los scores resultantes alimentan las métricas de calidad del sistema.

### Limitaciones conocidas del LLM-as-judge

El LLM-as-judge es una herramienta útil pero tiene limitaciones bien documentadas que el AI Engineer debe conocer antes de confiar en los scores que produce.

**Sesgo de autopreferencia.** Los modelos tienden a puntuar más alto las respuestas que se parecen al estilo que ellos mismos generarían. Si el evaluador y el sistema evaluado son del mismo modelo o de la misma familia de modelos, el evaluador puede calificar bien respuestas que otro evaluador —humano o de otra familia— calificaría peor.

**Sesgo de posición.** En evaluaciones donde se comparan dos respuestas (A/B), los modelos tienden a favorecer la respuesta que aparece primero, independientemente de su calidad real. Para mitigar este sesgo, las comparaciones deben ejecutarse en ambos órdenes y promediar los resultados.

**Sensibilidad al formato del prompt de evaluación.** Cambios menores en la redacción del prompt de evaluación pueden producir scores significativamente diferentes. Un prompt que pide "evalúa si la respuesta es correcta" produce resultados distintos a uno que pide "evalúa si cada afirmación de la respuesta está soportada por el contexto". El equipo debe validar que el prompt de evaluación captura el criterio de calidad correcto para el caso de uso.

**Incapacidad para detectar alucinaciones sutiles.** Un modelo evaluador que recibe el mismo contexto que el sistema evaluado puede confirmar que la respuesta es consistente con ese contexto —lo que es la definición de groundedness— sin detectar si el contexto mismo contiene información desactualizada. La evaluación de la exactitud factual respecto al mundo real, no respecto al contexto local, requiere una fuente de verdad externa.

**Costo adicional.** Ejecutar un modelo evaluador por cada respuesta de producción duplica o triplica el costo por solicitud si se evalúa el 100% del tráfico. En la práctica, el LLM-as-judge se ejecuta sobre una muestra del tráfico —típicamente el 5-20%— con muestreo estratificado para asegurar representatividad.

### Evaluación humana: cuándo es indispensable

La evaluación humana no puede reemplazarse en tres situaciones.

**Primera: calibración del evaluador automático.** Antes de confiar en los scores del LLM-as-judge, el equipo debe calibrarlo contra evaluaciones humanas. Si evaluadores humanos expertos puntúan una muestra de respuestas con consistencia, y los scores del modelo evaluador correlacionan fuertemente con esos scores humanos, el evaluador automático es confiable para esa distribución de casos. Si la correlación es baja, el evaluador automático tiene un sesgo sistemático que debe corregirse.

**Segunda: casos de alta consecuencia.** En dominios donde una respuesta incorrecta tiene consecuencias graves —diagnósticos médicos, asesoría legal, decisiones financieras—, la evaluación humana de una fracción representativa de las respuestas es una salvaguarda no negociable. Los modelos evaluadores no asumen responsabilidad por los errores que no detectan.

**Tercera: nuevos patrones de falla.** Cuando el sistema se enfrenta a un tipo de consulta que no estaba presente en los datos de calibración del evaluador automático, los scores del modelo evaluador pueden ser no confiables para ese nuevo patrón. El equipo de operaciones debe revisar manualmente los casos en que el evaluador automático produce scores extremos —muy altos o muy bajos— para detectar si hay un nuevo modo de falla que el evaluador no está capturando correctamente.

### El proceso de evaluación humana estructurado

Cuando se conduce evaluación humana, la estructura del proceso determina la calidad de los resultados. La evaluación informal —"alguien en el equipo revisa algunas respuestas"— produce datos que son difíciles de agregar y comparar en el tiempo.

Un proceso estructurado de evaluación humana tiene cuatro elementos:

**Protocolo de evaluación.** Un documento que define qué criterios se evalúan, cómo se escalan (qué significa un 3/5 en relevancia versus un 4/5), qué ejemplos de cada nivel sirven de referencia para los evaluadores.

**Selección de la muestra.** Las respuestas a evaluar deben seleccionarse de forma que sean representativas del tráfico real. Una muestra sesgada hacia los casos fáciles produce una estimación de calidad optimista; una muestra sesgada hacia los casos difíciles produce el efecto contrario.

**Múltiples evaluadores por caso.** Para medir la consistencia humana —y por tanto la confiabilidad de las evaluaciones—, al menos un subconjunto de los casos debe ser evaluado por dos o más personas. Si hay desacuerdo frecuente entre evaluadores, el protocolo de evaluación no es suficientemente preciso o el criterio de calidad es intrínsecamente subjetivo.

**Medición de acuerdo entre evaluadores (inter-rater reliability).** Una métrica como el coeficiente kappa de Cohen cuantifica en qué medida los evaluadores humanos están de acuerdo entre sí. Un kappa mayor de 0.7 indica acuerdo sustancial; por debajo de 0.5, el proceso de evaluación produce datos poco confiables.

### Datasets de evaluación: el golden set

Una práctica fundamental en sistemas de IA maduros es el mantenimiento de un golden set: un conjunto de casos de referencia con respuestas de calidad conocida, construido y validado por expertos del dominio.

El golden set sirve para dos propósitos distintos.

Primero, permite evaluar el sistema de forma repetible a lo largo del tiempo. Si el sistema pasa los casos del golden set con calidad alta hoy y con calidad más baja en tres meses, hay un deterioro detectable que puede investigarse.

Segundo, permite comparar versiones del sistema. Cuando se cambia el system prompt, se actualiza la base vectorial o se cambia el modelo, ejecutar el golden set sobre la nueva versión y comparar los resultados con la versión anterior produce evidencia objetiva de si el cambio mejoró o deterioró la calidad del sistema.

Un golden set efectivo incluye:

- Casos representativos del uso normal del sistema
- Casos borde conocidos: consultas que en el pasado produjeron respuestas incorrectas o insatisfactorias
- Casos adversariales: consultas diseñadas para detectar comportamientos problemáticos (instrucciones que contradicen el system prompt, preguntas fuera del dominio, consultas con información incorrecta en la premisa)
- Casos que verifican restricciones críticas: el sistema nunca debe revelar información confidencial, nunca debe contradecir una política corporativa específica, nunca debe responder fuera de su dominio declarado

### El pipeline de evaluación combinado

El pipeline de evaluación que funciona en producción combina las evaluaciones automáticas y humanas en un sistema cohesivo:

```
PIPELINE DE EVALUACIÓN — Operación continua

[PRODUCCIÓN] → 100% del tráfico
     |
     ├─→ [MÉTRICAS OPERACIONALES] → Latencia, tokens, errores
     |         (recolección automática, tiempo real)
     |
     ├─→ [LLM-AS-JUDGE] → Relevancia, groundedness, coherencia
     |         (muestra 10-20%, ejecución asíncrona)
     |
     └─→ [GOLDEN SET] → Evaluación periódica (semanal/quincenal)
              (todos los casos, con comparación de versiones)

[EVALUACIÓN HUMANA] → Flujo paralelo
     |
     ├─→ Calibración del LLM-as-judge (mensual)
     ├─→ Revisión de casos extremos (continua)
     └─→ Análisis de casos de alta consecuencia (por incidente)

[AGREGACIÓN] → Scorecard semanal
     Métricas operacionales + scores de calidad + tendencias
```

### Nota del arquitecto

La evaluación de sistemas de IA es un campo en evolución activa. Las técnicas que se describen aquí representan el estado práctico consolidado, pero no son definitivas. Investigaciones recientes muestran que los evaluadores automáticos basados en modelos de lenguaje tienen sesgos sistemáticos que pueden conducir a conclusiones erróneas sobre la calidad del sistema. La calibración periódica contra evaluadores humanos no es opcional; es la única forma de saber si los números que el pipeline automático produce son confiables.

Un equipo que confía ciegamente en los scores del LLM-as-judge sin calibración humana regular corre el riesgo de optimizar el sistema para satisfacer al evaluador —un fenómeno análogo a Goodhart's Law: cuando una métrica se convierte en el objetivo, deja de ser una buena métrica—.

La siguiente sección introduce la trazabilidad de prompts y contexto: cómo registrar no solo la respuesta del sistema sino el contexto completo que el modelo recibió, para poder diagnosticar respuestas incorrectas con precisión quirúrgica.
