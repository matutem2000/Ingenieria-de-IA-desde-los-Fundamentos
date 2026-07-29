# Capítulo 10 — Planificación y Razonamiento

## Sección 14: Autoevaluación

Las siguientes preguntas evalúan la comprensión de los conceptos fundamentales del capítulo. Algunas tienen una respuesta correcta precisa; otras son preguntas de diseño con múltiples respuestas válidas. Para estas últimas, lo que importa es la calidad del razonamiento que las sustenta.

---

### Preguntas de comprensión conceptual

**1.** Un colega afirma: "Nuestro agente usa GPT-4, así que razona mejor que los humanos en tareas analíticas." ¿Qué aspectos de esta afirmación son imprecisos? ¿Cómo describirías de forma más precisa lo que el modelo hace cuando produce un análisis?

**2.** Explica, en tus propias palabras, por qué la calidad del razonamiento de un LLM depende principalmente del diseño del contexto y no solo de la capacidad del modelo.

**3.** ¿Cuál es la diferencia fundamental entre la reflexión interna (el agente evalúa su propio output) y la verificación externa (el sistema verifica el output contra una fuente de verdad)? ¿Qué clases de errores detecta cada una que la otra no puede?

**4.** Un sistema usa Tree of Thoughts con 3 niveles y factor de ramificación 3 en todos los niveles, evaluando todas las ramas antes de podar. Estima el número de llamadas al modelo necesarias. ¿En qué condiciones justificarías ese costo en un sistema de producción?

**5.** El anti-patrón "verificación circular" implica usar el mismo modelo con el mismo prompt para generar y evaluar un output. ¿Por qué el uso de un prompt de evaluación significativamente diferente (aunque sea el mismo modelo) mejora la situación? ¿Qué limitación fundamental persiste?

---

### Preguntas de diseño

**6.** Eres el AI Engineer responsable de un sistema que genera respuestas a preguntas frecuentes de clientes sobre una política de devoluciones. Las respuestas incorrectas tienen un costo bajo (el cliente puede contactar soporte para aclarar). Diseña la arquitectura de razonamiento más apropiada para este sistema, justificando cada decisión.

**7.** El mismo caso del punto 6, pero ahora el sistema genera respuestas sobre el estado de reclamaciones de seguros de salud. Una respuesta incorrecta puede resultar en que el paciente no reciba atención médica necesaria. ¿Cómo cambia la arquitectura? ¿Qué mecanismos adicionales añades?

**8.** Un agente que planifica la compra de materias primas para una empresa manufacturera generó el siguiente plan:

```
Paso 1: Consultar inventario actual de materias primas.
Paso 2: Determinar necesidades de producción para las próximas 4 semanas.
Paso 3: Calcular la diferencia entre inventario y necesidades.
Paso 4: Emitir órdenes de compra para cubrir la diferencia.
```

Identifica los problemas de este plan desde la perspectiva del capítulo. ¿Qué pasos faltan? ¿Qué verificaciones son necesarias? ¿Qué escaladas deben definirse?

**9.** Un sistema de planificación tiene la siguiente tasa de error en producción: 2% de las tareas producen un output incorrecto que llega al usuario. El equipo propone agregar un paso de reflexión (una iteración de evaluación y revisión) que, según sus pruebas, reduciría la tasa de error al 0.8%. Cada reflexión añade 3 segundos de latencia y 0.05 USD de costo por tarea. El sistema procesa 10.000 tareas por día. El costo de un output incorrecto es de 5 USD en gestión del reclamo. ¿Vale la pena añadir la reflexión? Muestra el análisis económico.

**10.** Diseña el mecanismo de escalada para el sistema de análisis de solicitudes de préstamo del caso de estudio (sección 10). Define: (a) las condiciones específicas que desencadenan escalada, (b) la información que debe incluir la notificación al analista, (c) qué hace el sistema mientras espera la respuesta del analista, (d) qué ocurre si el analista no responde en el plazo definido.

---

### Preguntas de análisis de casos

**11.** Un sistema de generación de informes financieros produce informes de 20 páginas a partir de datos de múltiples fuentes. El equipo detecta que el 15% de los informes contienen al menos un dato incorrecto. ¿Cuál de los anti-patrones del capítulo es más probable que esté causando este problema? ¿Cómo lo diagnosticarías y cómo lo corregirías?

**12.** Un agente de soporte técnico usa planificación iterativa con un límite de 20 iteraciones. En producción, el 8% de las sesiones alcanzan el límite de iteraciones sin resolver el problema del usuario. El equipo quiere aumentar el límite a 40 para darle más oportunidades al agente de resolver. ¿Cuál es el problema con esta solución? ¿Qué analizarías antes de decidir si aumentar el límite es la respuesta correcta?

---

### Respuestas orientativas para preguntas seleccionadas

**Respuesta orientativa — Pregunta 4:**

Nivel 1: 3 generaciones + 1 evaluación = 4 llamadas.
Nivel 2: 3 × 3 = 9 generaciones + 1 evaluación = 10 llamadas (si se expanden todas las ramas del nivel 1).
Nivel 3: 9 × 3 = 27 generaciones + 1 evaluación = 28 llamadas (si se expanden todas las ramas del nivel 2).
Total: 4 + 10 + 28 = 42 llamadas al modelo.

Este costo se justifica cuando: (a) el valor del output es suficientemente alto (decisiones estratégicas de alto impacto), (b) el primer enfoque intuitivo del modelo es frecuentemente subóptimo en este dominio específico, (c) la latencia adicional es aceptable para el caso de uso (análisis que se realiza overnight, no en tiempo real).

**Respuesta orientativa — Pregunta 9:**

Costo diario actual de errores: 10.000 × 0.02 × 5 = 1.000 USD/día.
Costo diario con reflexión — errores: 10.000 × 0.008 × 5 = 400 USD/día.
Ahorro en errores: 600 USD/día.

Costo adicional de la reflexión: 10.000 × 0.05 = 500 USD/día.

Resultado: el ahorro en errores (600 USD) supera el costo de la reflexión (500 USD). El balance neto es positivo en 100 USD/día. La reflexión se justifica económicamente. Consideración adicional: el impacto de 3 segundos adicionales de latencia en la experiencia del usuario debe evaluarse separadamente — puede ser un factor determinante si el sistema requiere respuesta en tiempo real.
