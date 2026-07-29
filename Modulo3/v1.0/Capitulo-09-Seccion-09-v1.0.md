# Capítulo 09 — Arquitecturas Multiagente

## Sección 09 — Patrones y anti-patrones multiagente

Los patrones de diseño en ingeniería de software son soluciones probadas a problemas recurrentes. No son recetas que se aplican mecánicamente: son marcos que nombran una solución conocida para que los equipos puedan reconocerla, comunicarla y aplicarla con conciencia de sus compromisos. Los anti-patrones son su inverso: configuraciones que parecen soluciones pero que producen problemas específicos y conocidos.

En el diseño de sistemas multiagente, el vocabulario de patrones y anti-patrones está consolidándose a medida que más equipos ponen estos sistemas en producción. Esta sección presenta los patrones y anti-patrones más relevantes, no como categorías exhaustivas sino como el conjunto que un AI Engineer debe reconocer antes de diseñar su primer sistema multiagente.

### Patrones que funcionan

**Patrón: Reflexión (Reflection)**

Un agente generador produce un output. Ese output es enviado a un agente crítico que lo evalúa contra criterios explícitos y produce una evaluación. Si la evaluación identifica problemas, el output vuelve al agente generador con el feedback específico para que produzca una versión mejorada. El ciclo puede repetirse hasta que el output pase la evaluación o hasta que se alcance el límite de iteraciones.

El patrón de Reflexión es especialmente valioso para tareas donde la precisión del output es alta y donde un agente único tiene dificultades para detectar sus propios errores. En código generado por IA, la Reflexión puede detectar errores que el agente generador validó como correctos. En análisis complejos, puede identificar saltos lógicos que el agente analista no advirtió.

El costo del patrón es la latencia adicional y el costo de tokens del agente crítico. El beneficio es una tasa de error significativamente menor en el output final. La decisión de aplicarlo depende de si la criticidad de la tarea justifica ese costo adicional.

**Patrón: Ejecución paralela con síntesis (Parallel Fanout with Synthesis)**

Un agente orquestador descompone una tarea en subtareas independientes, las distribuye simultáneamente a múltiples agentes especializados y espera a que todos completen su trabajo. Una vez que todos los agentes han reportado sus resultados, el orquestador (o un agente síntesis dedicado) integra esos resultados en un output unificado.

Este patrón es el más directo para aprovechar la arquitectura multiagente: la latencia total es la del agente más lento, no la suma de todas las latencias. Es el patrón correcto cuando las subtareas son genuinamente independientes y el resultado final requiere la integración de todos los outputs parciales.

El riesgo más frecuente es asumir independencia entre subtareas cuando en realidad hay dependencias sutiles. Un sistema que analiza en paralelo los aspectos financieros y legales de una empresa puede producir conclusiones que se contradicen si los datos que cada agente analiza no son consistentes entre sí. La independencia de las subtareas es una condición que debe verificarse, no asumirse.

**Patrón: Escalada supervisada (Supervised Escalation)**

El sistema tiene un agente de nivel básico que maneja la mayoría de los casos, y un agente de nivel superior —más capaz, más costoso— que recibe los casos que el agente básico no pudo resolver con confianza. La decisión de escalar puede basarse en una métrica de confianza del agente básico, en la detección de características del caso que lo clasifican como complejo, o en la intervención del supervisor.

Este patrón reduce el costo promedio del sistema porque la mayoría de los casos son resueltos por el agente de menor costo. El agente de nivel superior solo se activa cuando es genuinamente necesario. La eficiencia del patrón depende de la capacidad del sistema para identificar correctamente qué casos requieren escalada: si muchos casos se escalan innecesariamente, el beneficio de costo se pierde.

**Patrón: Verificación cruzada (Cross-Validation)**

Dos o más agentes resuelven independientemente el mismo problema, y un agente árbitro compara sus resultados. Si los resultados coinciden, el consenso se acepta como la respuesta del sistema. Si hay discrepancias significativas, el árbitro puede intentar resolver el conflicto mediante análisis adicional o escalar a revisión humana.

Este patrón duplica o triplica el costo de la generación pero ofrece el nivel más alto de confianza en el output para tareas de máxima criticidad. Es la arquitectura correcta cuando el costo de un error en el output supera con creces el costo adicional de la generación redundante.

### Anti-patrones que se deben evitar

**Anti-patrón: El agente dios (God Agent)**

Un único agente que intenta hacer todo: buscar información, analizarla, redactar el output, verificarlo, ejecutar acciones y coordinar a otros agentes. El resultado es un agente con un prompt de sistema extremadamente largo, herramientas de naturaleza muy distinta y un comportamiento difícil de predecir porque está intentando equilibrar demasiadas responsabilidades simultáneamente.

El síntoma más claro del anti-patrón del agente dios es el prompt de sistema que empieza con "Eres un asistente inteligente capaz de..." seguido de una lista de decenas de capacidades heterogéneas. La solución es la descomposición: identificar las responsabilidades del agente dios y redistribuirlas entre agentes especializados con roles bien delimitados.

**Anti-patrón: Red de charlas (Chatty Network)**

Los agentes se comunican entre sí con una frecuencia mucho mayor de lo necesario. En lugar de que un agente complete una subtarea completa y reporte el resultado, el agente A envía al agente B un resultado parcial, B responde con una consulta, A responde a la consulta, B envía un resultado parcial a C, C responde a B... El sistema produce un volumen de comunicación que excede con creces la complejidad del trabajo real que está haciendo.

Este anti-patrón generalmente emerge cuando los roles de los agentes no están bien definidos (cada agente necesita consultar constantemente a otros porque no tiene claro qué información necesita para completar su tarea) o cuando el sistema fue diseñado con demasiado acoplamiento entre agentes (el output del agente A tiene demasiadas dependencias del estado del agente B).

La solución es revisar la definición de roles y asegurarse de que cada agente recibe, al inicio de su tarea, toda la información que necesita para completarla sin consultas adicionales.

**Anti-patrón: Confianza no verificada entre agentes (Unverified Trust)**

Un agente acepta el output de otro agente como verdadero sin verificación. Si el agente upstream produce un error —ya sea por un fallo de razonamiento o por manipulación externa— ese error se propaga a través del sistema sin ningún punto de detección.

En sistemas multiagente, los agentes deben tratar el output de otros agentes con el mismo escepticismo que aplicarían a datos de fuentes externas. La validación del esquema del output (¿el formato es el esperado?), la verificación de rangos plausibles (¿los valores están en rangos razonables?) y la detección de inconsistencias internas (¿las partes del output son coherentes entre sí?) son controles que deben estar presentes aunque el origen del dato sea otro agente del mismo sistema.

**Anti-patrón: Multiagente innecesario (Accidental Complexity)**

El sistema implementa una arquitectura multiagente para resolver un problema que un agente único bien diseñado podría resolver con mejor calidad, menor costo y mayor simplicidad. Este anti-patrón no tiene un síntoma técnico inmediato: el sistema funciona. El síntoma es la dificultad desproporcionada para mantener, depurar y mejorar el sistema en comparación con el valor que produce.

La prueba de diagnóstico es la pregunta de las cuatro condiciones de la sección 02: si ninguna de ellas está presente (paralelismo genuinamente necesario, especialización fundamentalmente distinta, criticidad que requiere verificación independiente, volumen que excede la ventana de contexto), la arquitectura multiagente es accidental, no necesaria.

**Anti-patrón: Plan sin supervisión (Unmonitored Plan)**

El planificador genera un plan, los agentes lo ejecutan, y el resultado final se entrega al usuario sin que ningún punto del proceso incluya verificación de calidad. El sistema puede operar durante días entregando outputs incorrectos sin que nadie lo detecte, porque no hay ningún mecanismo de detección.

Este anti-patrón suele emerger en la transición del prototipo a la producción: en el prototipo, el desarrollador revisa manualmente cada output. En producción, esa revisión manual ya no es posible a escala, pero tampoco se implementó ningún sustituto automatizado. La observabilidad de la sección 08 y el patrón de supervisión de la sección 06 son las respuestas a este anti-patrón.

---

*La sección 10 aplica los patrones y principios de este capítulo a un caso de estudio concreto. El salto de la teoría a la práctica requiere ver un sistema real diseñado paso a paso, con las decisiones que se tomaron y las alternativas que se descartaron.*
