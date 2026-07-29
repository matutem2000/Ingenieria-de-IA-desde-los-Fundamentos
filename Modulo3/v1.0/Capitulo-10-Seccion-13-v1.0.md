# Capítulo 10 — Planificación y Razonamiento

## Sección 13: Resumen del capítulo

### Lo que el capítulo estableció

El capítulo 10 estudió los mecanismos internos que habilitan la planificación y el razonamiento en sistemas de IA. El punto de partida fue conceptual y fue deliberado: antes de diseñar un sistema de razonamiento, el AI Engineer necesita entender con precisión qué es lo que el LLM hace cuando razona.

**El razonamiento en un LLM es predicción estadística de tokens, no inferencia lógica formal.** Esta distinción tiene tres consecuencias prácticas que deben guiar cada decisión de diseño: el modelo puede equivocarse con plena confianza, el contexto determina la calidad del razonamiento, y el modelo no tiene acceso introspectivo privilegiado a sus propios procesos. El arquitecto del sistema es quien debe estructurar el contexto, añadir verificación externa y gestionar la corrección donde el modelo solo no es suficiente.

---

### Los cuatro patrones de planificación

El capítulo presentó una taxonomía de cuatro patrones que cubren el espacio de diseño de sistemas de razonamiento:

**Patrón simple:** Una llamada produce el output completo. Correcto para tareas de baja complejidad donde el modelo tiene alta precisión sin razonamiento multi-paso.

**Patrón secuencial:** Una cadena de llamadas donde cada output alimenta el input siguiente. Correcto para tareas con estructura de pipeline donde los pasos intermedios son verificables de forma independiente.

**Patrón iterativo (con reflexión):** El output se evalúa y revisa en ciclos. Correcto para tareas de alta calidad requerida donde los errores son detectables con una segunda revisión. Requiere criterio de convergencia y límite de iteraciones.

**Patrón ramificado (Tree of Thoughts):** Múltiples ramas de razonamiento se generan, evalúan y podan. Correcto para problemas de optimización donde el primer enfoque intuitivo es frecuentemente subóptimo. Costo computacional alto; se justifica cuando el valor del output es suficientemente alto.

---

### Las técnicas fundamentales

**Chain of Thought arquitectónico:** Más que una instrucción de prompting, es la decisión de materializar los pasos de razonamiento como outputs separados, incorporados al contexto de las llamadas siguientes. Hace el razonamiento auditable, mejora la precisión en tareas multi-paso y permite intervención en puntos específicos del proceso.

**Tree of Thoughts:** Una arquitectura de búsqueda sobre un árbol de estados de razonamiento. Requiere generación de múltiples pensamientos, evaluación de cada uno y selección del más prometedor. El costo real en llamadas al modelo crece con el factor de ramificación y la profundidad; en práctica se usa con árboles poco profundos y poda agresiva.

**Planificación iterativa y Plan-and-Execute:** La planificación dinámica decide el siguiente paso en cada iteración. Plan-and-Execute separa la planificación de la ejecución, haciendo el plan inspeccionable antes de ejecutarse. La replanificación dinámica combina ambos enfoques cuando el entorno es suficientemente incierto.

**Reflexión:** El ciclo de generación-evaluación-revisión mejora la coherencia y completitud. Puede detectar omisiones, inconsistencias internas y brechas de cobertura. No puede detectar errores factuales donde el evaluador comparte los puntos ciegos del generador.

---

### Las estrategias de verificación

La verificación externa es el complemento necesario de la reflexión interna. La estrategia correcta depende del tipo de output:

- **Código:** verificación sintáctica, ejecución en sandbox, suite de tests.
- **Respuestas factuales:** contraste contra fuente de verdad externa; marcado explícito de afirmaciones no verificadas.
- **Planes de acción:** verificación de disponibilidad de herramientas, coherencia de dependencias, completitud de cobertura.
- **Outputs estructurados:** validación contra esquema JSON/XSD antes de pasar a sistemas downstream.

El LLM-as-judge es una herramienta válida cuando la verificación automática no es posible, con la limitación de que el evaluador hereda los puntos ciegos del modelo generador.

---

### Las cuatro dimensiones empresariales

Más allá de la calidad técnica del razonamiento, los sistemas empresariales deben atender cuatro dimensiones simultáneamente:

1. **Calidad:** calibrada al nivel que el caso de uso requiere, no al máximo que la técnica permite.
2. **Latencia:** diseñada dentro del presupuesto de tiempo del caso de uso, con paralelización y caching donde sea posible.
3. **Auditabilidad:** trazas completas de cada llamada, herramienta y verificación, disponibles para auditoría regulatoria y depuración operacional.
4. **Control humano:** escalada predefinida, separación entre recomendación y decisión, capacidad de intervención en cualquier punto del ciclo.

---

### Los cinco anti-patrones críticos

El capítulo identificó los patrones de diseño que más frecuentemente producen fallos en producción:

1. El optimista de una sola llamada, que funciona en demos y falla en producción.
2. La reflexión infinita, que degrada el output en lugar de mejorarlo más allá de 2-3 iteraciones.
3. El plan que no puede fallar, donde los errores de pasos tempranos se propagan invisiblemente.
4. El agente sin herramientas, que planifica acciones que no puede ejecutar.
5. La verificación circular, que da falsa seguridad sin agregar garantías reales.

---

### El principio unificador

El principio que unifica todo el capítulo es este: el razonamiento de un LLM es el resultado del contexto que el arquitecto diseña, no una propiedad intrínseca del modelo. El AI Engineer que entiende esto diseña el contexto con precisión, añade verificación donde el modelo no es confiable, implementa reflexión donde la calidad lo justifica, y construye mecanismos de control donde el sistema opera sobre decisiones de alto impacto.

El capítulo 11 aplica estos principios a un dominio concreto: el desarrollo de software asistido por IA, donde la planificación y el razonamiento se despliegan sobre el problema de entender, generar y mantener código.
