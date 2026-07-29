# Capítulo 09 — Arquitecturas Multiagente

## Sección 14 — Autoevaluación

Las preguntas de esta sección no tienen respuestas de una palabra. Son preguntas de razonamiento: requieren aplicar los marcos del capítulo a situaciones que no aparecieron exactamente en el texto. Si puedes responderlas con precisión, has construido el modelo mental correcto. Si alguna revela una laguna, esa laguna señala exactamente la sección del capítulo que vale la pena releer.

---

**Pregunta 1**

Un equipo propone un sistema multiagente con doce agentes para automatizar la generación de informes de ventas semanales. Los informes tienen siempre la misma estructura, se basan en datos que el sistema puede consultar directamente desde la base de datos de ventas, y no requieren análisis subjetivo ni síntesis de múltiples fuentes heterogéneas.

¿Qué le dirías al equipo? Aplica el árbol de decisión de la sección 02 al caso y justifica tu recomendación.

---

**Pregunta 2**

Estás diseñando un sistema multiagente para analizar contratos legales. El sistema tiene un agente extractor (identifica las cláusulas relevantes), un agente analista (evalúa las cláusulas contra los criterios de la empresa) y un agente redactor (produce el resumen ejecutivo).

El agente analista necesita, para algunos contratos, consultar precedentes de contratos anteriores de la empresa. Esos precedentes están en la memoria compartida del sistema.

¿Qué consideraciones de diseño aplicas para que el agente analista acceda a los precedentes de forma correcta y segura? Incluye consideraciones de consistencia, aislamiento y privacidad.

---

**Pregunta 3**

Tu sistema multiagente lleva tres semanas en producción. El costo de tokens es un 40% mayor de lo esperado en la estimación inicial. El output de calidad es el esperado. ¿Cuáles son las causas más probables de esa desviación y cómo la investigarías? ¿Qué cambios de diseño evaluarías?

---

**Pregunta 4**

Tienes un sistema con la siguiente topología: un agente orquestador que distribuye tareas entre cuatro agentes especializados, que devuelven sus resultados al orquestador, que luego los envía a un agente redactor. Es una topología jerárquica clásica.

En producción, el sistema falla con frecuencia en el paso de síntesis del orquestador: los cuatro resultados de los agentes especializados son correctos individualmente, pero el orquestador tiene dificultades para integrarlos de forma coherente porque los formatos de output de los cuatro agentes son distintos entre sí.

Diagnostica el problema y propón dos alternativas de solución con sus compromisos.

---

**Pregunta 5**

Un colega propone añadir al sistema del caso de estudio de la sección 10 (evaluación de propuestas de proveedores) un agente de negociación que, después de producir el borrador de evaluación, genere automáticamente una contraoferta al proveedor si las condiciones comerciales no cumplen los parámetros de la empresa.

Evalúa esta propuesta. ¿Qué dimensiones del diseño cambian? ¿Qué consideraciones nuevas aparecen que no estaban presentes en el diseño original?

---

**Pregunta 6**

Describe la diferencia entre el anti-patrón del Agente Dios y un agente orquestador legítimo. ¿Qué características tiene el orquestador que lo distinguen del Agente Dios? ¿Cómo sabrías cuándo un orquestador está convirtiéndose en un Agente Dios?

---

**Pregunta 7**

Tu sistema multiagente tiene un agente supervisor que evalúa el output del agente redactor antes de entregarlo al usuario. La tasa de rechazo del supervisor es del 35%: rechaza un tercio de los borradores que recibe y los devuelve al redactor para corrección.

Esa tasa te parece alta. ¿Significa que el sistema está funcionando mal? ¿O podría ser una señal de que el sistema está funcionando correctamente? ¿Qué información adicional necesitarías para distinguir entre ambos casos?

---

**Pregunta 8**

Diseña brevemente la estrategia de resiliencia para el siguiente escenario: un sistema de pipeline en el que cinco agentes actúan en secuencia (A → B → C → D → E) para transformar un documento desde su forma original hasta su forma final. El proceso completo toma en promedio ocho minutos.

¿Qué ocurre si el agente C falla a los cuatro minutos de procesamiento? ¿Cómo diseñas el sistema para que no sea necesario reiniciar desde A?

---

### Criterios de autodiagnóstico

Si respondiste las preguntas 1, 2 y 6 con claridad y precisión: tienes sólida comprensión de los conceptos fundamentales del capítulo (cuándo usar multiagente, diseño de agentes, patrones y anti-patrones).

Si también respondiste las preguntas 3, 4 y 8: tienes comprensión operacional del capítulo (costo, debugging, resiliencia).

Si también respondiste las preguntas 5 y 7: tienes comprensión de las dimensiones de diseño más sutiles del capítulo (cambios de alcance, interpretación de métricas de sistema).

Si alguna pregunta quedó sin respuesta satisfactoria, ese es el punto de entrada para releer el capítulo con un objetivo específico, no una relectura completa.

---

*La sección 15 establece el puente entre los sistemas multiagente de este capítulo y el problema del razonamiento y la planificación que define el capítulo 10.*
