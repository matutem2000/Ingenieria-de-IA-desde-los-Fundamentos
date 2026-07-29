# Capítulo 09 — Arquitecturas Multiagente

## Sección 02 — ¿Cuándo utilizar múltiples agentes?

La arquitectura multiagente es una herramienta poderosa. También es una fuente frecuente de sobreingeniería. La distinción entre ambos usos no está en la tecnología sino en el problema: algunos problemas exigen múltiples agentes, la mayoría no. Un AI Engineer que no puede hacer esa distinción construye sistemas innecesariamente complejos cuando el problema pedía un agente simple, o sistemas inevitablemente frágiles cuando el problema pedía un sistema distribuido.

Esta sección establece los criterios de decisión. No como reglas rígidas, sino como un árbol de preguntas que, respondidas honestamente, señalan la arquitectura correcta.

### El punto de partida: empieza siempre con el agente único

Antes de cualquier análisis, la regla de base es esta: **diseña primero con un agente único**. No porque sea siempre suficiente, sino porque es siempre más simple, más barato, más fácil de depurar y más rápido de iterar. Si el agente único puede resolver el problema con calidad aceptable, ese es el sistema correcto. La complejidad adicional de una arquitectura multiagente tiene un costo real: en latencia, en costo de tokens, en superficie de errores, en dificultad operativa.

El multiagente se justifica cuando el agente único encuentra límites que no puede superar estructuralmente. No cuando "sería más elegante", no cuando "escalaría mejor en teoría", sino cuando el problema real impone restricciones que el agente único no puede satisfacer.

### Las cuatro preguntas de decisión

**Primera pregunta: ¿puede la tarea descomponerse en subtareas independientes que se beneficiarían de ejecución simultánea?**

Si la respuesta es sí, el paralelismo de agentes reduce la latencia total del sistema. Considera un sistema de due diligence empresarial que debe analizar estados financieros, reputación legal, historial de clientes y cobertura mediática de una compañía. Cada análisis es independiente de los demás. Un agente único los haría en secuencia: primero financiero, luego legal, luego clientes, luego medios. Cuatro agentes especializados los hacen en paralelo. La latencia total pasa de ser la suma de las cuatro duraciones a ser la duración del análisis más lento. Cuando la tarea tiene esta estructura —subtareas independientes cuyo resultado no depende entre sí—, el paralelismo de agentes es directamente útil.

Si las subtareas son secuenciales (el output de A es el input de B), el paralelismo no ayuda. Un pipeline secuencial entre dos llamadas al modelo suele ser suficiente.

**Segunda pregunta: ¿requieren distintas partes de la tarea conocimiento especializado, herramientas o instrucciones de sistema fundamentalmente distintas?**

Un agente generalista que analiza código en Python, redacta contratos legales y responde consultas médicas necesita un prompt de sistema que intente cubrir todos esos dominios simultáneamente. El resultado es predecible: el agente es mediocre en todos ellos porque ninguno recibe el tratamiento especializado que merece.

La especialización de agentes es la respuesta correcta cuando los dominios de trabajo son suficientemente distintos como para que un único prompt de sistema no pueda servir a todos con la misma precisión. Un agente cuya única función es analizar código Python, con herramientas de ejecución de código y acceso a documentación técnica, produce análisis fundamentalmente mejores que el agente generalista. Si el problema tiene esa estructura —múltiples dominios que requieren especialización real—, la arquitectura multiagente con agentes especializados es la elección correcta.

**Tercera pregunta: ¿la corrección del output es suficientemente crítica como para requerir verificación independiente?**

Un agente que genera una conclusión y la valida por sí mismo tiene un sesgo estructural hacia confirmar lo que produjo. Para tareas de baja criticidad, este sesgo es aceptable. Para tareas donde un error tiene consecuencias significativas —una recomendación de inversión, un diagnóstico diferencial, la verificación de código de seguridad—, la verificación independiente por un segundo agente que no participó en la generación añade una capa de robustez real.

El patrón de Reflexión en arquitectura multiagente es precisamente esto: un agente generador y un agente crítico que evalúa el output del primero contra criterios explícitos antes de que ese output sea aceptado. La criticidad de la tarea es el factor decisivo: si el costo de un error justifica la latencia y el costo adicional de la verificación, la arquitectura dual es correcta.

**Cuarta pregunta: ¿el volumen de información que la tarea requiere procesar excede lo que puede mantenerse en una sola ventana de contexto sin compresión con pérdida inaceptable?**

Cuando la respuesta es sí, la distribución entre agentes es la única solución que preserva la fidelidad de la información. Un análisis que requiere procesar doscientos documentos densos no puede hacerse con calidad en una única ventana de contexto de cien mil tokens. Dos agentes procesando cien documentos cada uno, con un agente síntesis que combina sus outputs, distribuyen la carga sin sacrificar fidelidad. Este criterio es objetivo y medible: si el contenido de la tarea cabe en la ventana de contexto con margen para el razonamiento, el agente único es suficiente; si no cabe, el multiagente es necesario.

### El árbol de decisión

```
¿La tarea tiene subtareas independientes paralelizables? 
  → SÍ: considerar agentes paralelos
  → NO ↓

¿Los dominios de la tarea requieren especialización radicalmente distinta?
  → SÍ: considerar agentes especializados
  → NO ↓

¿La criticidad del output justifica verificación independiente?
  → SÍ: considerar patrón generador + crítico
  → NO ↓

¿El volumen de información excede la ventana de contexto sin pérdida aceptable?
  → SÍ: considerar agentes distribuidores + síntesis
  → NO → Agente único es la arquitectura correcta
```

Si ninguna de las cuatro preguntas produce un "sí", la arquitectura de agente único es la respuesta correcta. No como segunda opción: como la mejor opción para ese problema.

### Anti-patrón: multiagente por aspiración arquitectónica

El anti-patrón más frecuente en este campo no es técnico sino motivacional: equipos que adoptan arquitecturas multiagente porque son más sofisticadas, porque los demos se ven más impresionantes, o porque "ya que estamos construyendo con IA, hagámoslo bien". Ninguna de estas razones es una razón válida para añadir la complejidad de un sistema multiagente.

El síntoma más claro de este anti-patrón es la dificultad para responder concretamente cuál de las cuatro preguntas anteriores justificó la arquitectura. Si la respuesta es "porque es más escalable" o "porque es la arquitectura moderna", el sistema probablemente debería ser más simple.

### El costo real del multiagente

Antes de decidir implementar una arquitectura multiagente, el AI Engineer debe estimar con honestidad:

- **Latencia:** cada agente adicional añade tiempo de procesamiento. Los sistemas paralelos reducen la latencia del caso crítico, pero añaden overhead de coordinación. Los sistemas secuenciales con múltiples agentes acumulan latencia en cada paso.
- **Costo de tokens:** cada agente consume tokens de input y output. Un sistema de cuatro agentes que procesan el mismo contexto base multiplica ese costo base por cuatro.
- **Superficie de errores:** cada agente es un punto de fallo potencial. Cada canal de comunicación entre agentes es otro. La complejidad del sistema de manejo de errores crece con el número de agentes.
- **Dificultad de depuración:** cuando un sistema multiagente produce un output incorrecto, identificar cuál agente introdujo el error y en qué momento requiere trazabilidad completa. Sin ella, el sistema es una caja negra difícil de mantener.

Estos costos no son razones para evitar el multiagente cuando el problema lo requiere. Son razones para no adoptarlo cuando el problema no lo requiere.

---

*La sección 03 asume que la decisión ya fue tomada: el problema justifica una arquitectura multiagente. El siguiente paso es diseñar los agentes individuales que componen ese sistema, comenzando por la pregunta de cómo definir roles y especialización de forma que el sistema sea más que la suma de sus partes.*
