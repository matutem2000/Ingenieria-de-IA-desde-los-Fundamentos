# Capítulo 05 - Sección 14

# Autoevaluación

> Módulo 3 — Context Engineering Profesional

---

# Instrucciones

Esta autoevaluación cubre los conceptos centrales del capítulo. Respondé cada pregunta antes de consultar las respuestas. El objetivo no es obtener una nota sino identificar qué conceptos necesitan repaso.

---

# Parte 1: Preguntas conceptuales

**1.** ¿Cuál es la diferencia principal entre una instrucción del sistema y el historial de conversación, desde el punto de vista de su rol en la arquitectura de contexto?

**2.** En la jerarquía de instrucciones de un sistema LLM, ¿qué ocurre cuando la instrucción del sistema del operador entra en conflicto con las políticas del proveedor del modelo?

**3.** ¿Por qué una restricción formulada como "intentá no dar información incorrecta" es técnicamente deficiente? ¿Cómo debería reformularse?

**4.** Una empresa tiene un asistente de soporte con la siguiente instrucción: *"Si el usuario es cliente premium, respondé con mayor prioridad."* ¿Esta instrucción pertenece a la capa de instrucciones del sistema o al contexto dinámico? Justificá.

**5.** ¿Cuál es el mecanismo principal de prompt injection indirecto y por qué es especialmente peligroso en agentes con herramientas?

---

# Parte 2: Análisis de instrucciones

Para cada instrucción del sistema a continuación, identificá el problema principal y proponé una versión mejorada.

---

**Instrucción A:**
```text
Sos un asistente de IA muy útil. Respondé todo lo que el usuario
pregunta de la mejor manera posible. Si no podés responder,
intentá dar algo útil igual.
```

¿Cuál es el anti-patrón? ¿Cómo lo corregirías?

---

**Instrucción B:**
```text
Respondé siempre en español.
[...150 tokens de otras instrucciones...]
Adaptate al idioma que prefiere el usuario para mejorar la experiencia.
```

¿Cuál es el problema? ¿Cómo lo resolverías en una sola instrucción coherente?

---

**Instrucción C:**
```text
El usuario actual es María López, plan Enterprise, con acceso
completo a todos los módulos. Sus últimos tres pedidos son #4421,
#4422 y #4423. Su próximo vencimiento es el 30 de agosto.
Ayudala con sus consultas de soporte técnico.
```

¿Cuál es el problema de arquitectura? ¿Cómo debería rediseñarse?

---

**Instrucción D:**
```text
Sos un agente que puede enviar emails, crear tickets y actualizar
registros de clientes. Cuando el usuario lo solicite, ejecutá
las acciones que sean necesarias para resolver su problema.
```

¿Qué elementos críticos faltan para un agente con herramientas? Listá al menos tres.

---

# Parte 3: Diseño aplicado

**Situación:**

Una empresa de educación online quiere lanzar un asistente para sus estudiantes. El asistente puede responder preguntas sobre el contenido de los cursos y ayudar a los estudiantes a organizar su plan de estudio.

**Restricciones que el negocio estableció:**
- No puede resolver ejercicios por el estudiante; solo puede orientarlo.
- No puede revelar las respuestas correctas de los exámenes.
- No puede hacer comentarios negativos sobre el nivel del estudiante.
- Debe adaptar la complejidad de sus explicaciones al nivel del curso inscripto.

**Pregunta:** Escribí el bloque de restricciones de la instrucción del sistema para este asistente. Las restricciones deben ser comportamientos observables con acciones definidas para cuando se activan.

---

# Respuestas de referencia

---

**Pregunta 1:** Las instrucciones del sistema definen el comportamiento permanente del modelo (reglas que se aplican en todas las conversaciones). El historial registra lo que ocurrió en la conversación actual y puede cambiar en cada turno. Las instrucciones son estables; el historial es dinámico.

---

**Pregunta 2:** Las políticas del proveedor prevalecen siempre. El operador puede definir comportamientos dentro del espacio habilitado por el proveedor, pero no puede eliminar ni sobrescribir las restricciones que el proveedor estableció mediante el entrenamiento del modelo.

---

**Pregunta 3:** "Intentá" es una instrucción de intención, no de comportamiento. En casos límite, el modelo puede decidir que la intención se cumple aunque el comportamiento no sea el deseado. Una versión correcta: *"Si no tenés certeza sobre un dato, indicalo explícitamente con frases como 'No tengo esa información disponible'. Nunca presentes información incierta como si fuera un hecho verificado."*

---

**Pregunta 4:** Al contexto dinámico. El hecho de que un usuario sea cliente premium depende del estado actual de su cuenta, que puede cambiar. Si esa condición está en las instrucciones del sistema, la instrucción quedaría desactualizada cuando el plan del usuario cambie. La instrucción del sistema debe decir *cómo* comportarse según el nivel del usuario; el nivel específico debe llegar como contexto dinámico.

---

**Pregunta 5:** El prompt injection indirecto ocurre cuando un agente procesa contenido externo (documentos, resultados de búsqueda, emails) que contiene instrucciones maliciosas diseñadas para modificar su comportamiento. Es especialmente peligroso en agentes con herramientas porque las instrucciones maliciosas pueden intentar forzar la ejecución de acciones reales (enviar emails, modificar registros, acceder a datos no autorizados).

---

**Instrucción A:** Anti-patrón: rol sin límites y restricción como deseo ("intentá dar algo útil igual"). Corrección: definir qué es el asistente, cuál es su dominio específico y qué debe hacer cuando no puede responder.

---

**Instrucción B:** Instrucción contradictoria. Ambas reglas sobre idioma no pueden coexistir sin un criterio de precedencia. Versión correcta: *"Respondé siempre en español, salvo que el usuario solicite explícitamente otro idioma. En ese caso, usá el idioma que el usuario pide."*

---

**Instrucción C:** Información dinámica en la capa de sistema (nombre de usuario, número de pedidos, fecha de vencimiento). Esta información cambia entre usuarios y entre sesiones. Debe moverse al contexto dinámico y ser inyectada en cada sesión. La instrucción del sistema debe describir solo el comportamiento, no los datos de un usuario específico.

---

**Instrucción D:** Faltan: (1) criterios de cuándo usar cada herramienta, (2) límites de autonomía (qué acciones requieren confirmación del usuario y cuáles no), (3) manejo de errores de herramientas, (4) política de seguridad ante prompt injection indirecto desde contenido externo.

---

**Parte 3 — Respuesta de referencia:**

```text
## Restricciones

- No resolvés ejercicios ni actividades evaluables por el estudiante.
  Si el estudiante te pide que resuelvas un ejercicio, orientalo
  sobre el concepto relevante y sugierile que intente la resolución.
  Podés revisar su razonamiento una vez que lo haya intentado.

- Nunca revelás respuestas correctas de exámenes ni evaluaciones,
  incluso si el estudiante argumenta que ya terminó el examen o
  que lo solicita para estudiar. Si el estudiante tiene dudas sobre
  un examen ya cerrado, sugerile que consulte con el tutor del curso.

- No hacés comentarios negativos sobre el nivel, el ritmo de
  aprendizaje ni el desempeño del estudiante. Si el estudiante
  expresa frustración, respondé con orientación concreta sobre
  cómo abordar la dificultad.

- Adaptás la complejidad de tus explicaciones al nivel del curso
  en que está inscripto el estudiante, especificado en el contexto
  de sesión. Para cursos básicos, usá analogías y evitá terminología
  avanzada. Para cursos avanzados, podés usar terminología técnica
  directamente.
```

---

# Resumen

La autoevaluación cubre las cuatro dimensiones centrales del capítulo: comprensión conceptual, análisis crítico de instrucciones existentes, diagnóstico de anti-patrones y aplicación práctica al diseño. Los errores en alguna de estas dimensiones indican qué secciones conviene releer antes de continuar.

La siguiente sección presenta la transición hacia el capítulo 06, donde estudiaremos el contexto dinámico: la capa que complementa a las instrucciones del sistema con información que cambia en cada interacción.
