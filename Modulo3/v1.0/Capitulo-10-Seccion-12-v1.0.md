# Capítulo 10 — Planificación y Razonamiento

## Sección 12: Checklist del AI Engineer

Esta checklist cubre las decisiones de diseño críticas para sistemas de planificación y razonamiento en producción. No es una lista de verificación de implementación — es una lista de decisiones de arquitectura que deben estar resueltas antes de que el sistema entre en producción.

---

### Bloque A: Diseño del razonamiento

**A1. ¿Está definido el patrón de planificación para cada tipo de tarea?**
- Para cada tipo de solicitud que el sistema procesará, ¿hay una decisión explícita de qué patrón usar (simple / secuencial / iterativo / ramificado)?
- ¿Esa decisión está documentada y es auditable?

**A2. ¿El contexto de planificación es completo?**
- ¿El prompt de planificación incluye el catálogo completo de herramientas disponibles con sus inputs, outputs y limitaciones?
- ¿El prompt incluye los criterios de éxito de la tarea?
- ¿El prompt incluye las restricciones de dominio relevantes (límites regulatorios, umbrales del negocio, restricciones de acceso a datos)?

**A3. ¿El razonamiento es visible?**
- ¿El sistema produce los pasos de razonamiento como texto explícito que puede ser auditado?
- ¿Esos pasos se registran junto con el output final?
- ¿Un analista humano puede seguir la cadena de razonamiento del agente hasta el output?

**A4. ¿Las herramientas deterministas se usan para cálculos?**
- ¿Los cálculos numéricos, la validación de esquemas y las consultas a bases de datos son herramientas deterministas, no llamadas al modelo?
- ¿El modelo se reserva para las tareas que requieren razonamiento sobre lenguaje natural: análisis, síntesis, evaluación?

---

### Bloque B: Reflexión y evaluación

**B1. ¿Está definida la política de reflexión?**
- ¿Para qué pasos del sistema se activa la reflexión?
- ¿Cuántas iteraciones máximas de reflexión están permitidas?
- ¿Cuál es el criterio de convergencia que determina cuándo la reflexión es suficiente?

**B2. ¿El evaluador es suficientemente independiente del generador?**
- ¿El prompt del evaluador es significativamente diferente al prompt del generador?
- Si se usa el mismo modelo para generar y evaluar, ¿hay mecanismos adicionales para compensar los puntos ciegos compartidos?
- ¿El evaluador tiene una lista explícita de tipos de problemas que debe buscar, en lugar de una instrucción genérica de "evaluar la calidad"?

**B3. ¿La reflexión tiene criterio de activación?**
- ¿La reflexión se activa siempre, o solo en los pasos de alto impacto donde el valor de la iteración justifica el costo?
- ¿Hay una clasificación de pasos por nivel de riesgo que determine cuándo se aplica reflexión y cuándo no?

---

### Bloque C: Verificación de outputs

**C1. ¿Hay una estrategia de verificación por tipo de output?**
- Para cada tipo de output que produce el sistema (código, texto estructurado, plan, respuesta factual), ¿hay una estrategia de verificación específica?
- ¿Esa estrategia está implementada y se activa automáticamente?

**C2. ¿La verificación de código incluye ejecución?**
- Para outputs de código, ¿el sistema ejecuta el código en un sandbox antes de entregarlo?
- ¿El resultado de la ejecución se usa para retroalimentar al agente si el código falla?

**C3. ¿La verificación factual usa fuentes externas?**
- Para outputs con afirmaciones factuales, ¿hay una fuente de verdad externa que el sistema consulta?
- ¿Las afirmaciones no verificadas están marcadas como tales en el output?

**C4. ¿Los outputs estructurados se validan contra un esquema?**
- ¿El sistema valida JSON/XML contra el esquema esperado antes de pasarlo a sistemas downstream?
- ¿Un fallo de validación desencadena retroalimentación automática al modelo?

---

### Bloque D: Control de recursos y fallos

**D1. ¿Hay límites explícitos de recursos?**
- ¿Está definido el número máximo de iteraciones del ciclo de planificación?
- ¿Está definido el número máximo de llamadas al modelo por tarea?
- ¿Hay un timeout absoluto por tarea?
- ¿Hay un límite de costo por tarea (en términos de tokens o de costo de API)?

**D2. ¿Hay comportamiento de degradación graceful?**
- ¿Está definido qué hace el sistema cuando una herramienta no está disponible?
- ¿Está definido qué hace el sistema cuando una fuente de datos externa no responde?
- ¿El sistema puede producir un output de menor calidad (con indicación explícita de la degradación) en lugar de fallar completamente?

**D3. ¿Hay detección de estancamiento?**
- ¿El sistema detecta cuando el agente ejecuta la misma acción repetidamente sin avanzar?
- ¿Esa detección desencadena un mecanismo de salida (escalada o aborto)?

---

### Bloque E: Auditabilidad y control humano

**E1. ¿El sistema registra trazas completas?**
- ¿Se registra el input y output de cada llamada al modelo?
- ¿Se registra el input y output de cada llamada a herramientas?
- ¿Se registra el resultado de cada verificación?
- ¿La traza completa está disponible para auditoría post-hoc?

**E2. ¿Está definida la política de escalada?**
- ¿Hay una lista explícita de condiciones que desencadenan escalada al operador humano?
- ¿La notificación de escalada incluye la información que el operador necesita para tomar una decisión?
- ¿El sistema puede detenerse y esperar la respuesta del operador sin perder el estado?

**E3. ¿Hay separación clara entre recomendación y decisión?**
- ¿El sistema produce recomendaciones, no decisiones autónomas, para las operaciones de alto impacto?
- ¿El analista humano tiene toda la información necesaria para aceptar, modificar o rechazar la recomendación?
- ¿Los criterios que determinan qué es "alto impacto" están documentados y son revisables?

---

### Señales de alerta

Un sistema de planificación que no puede responder afirmativamente a las siguientes preguntas debe ser revisado antes de pasar a producción:

- ¿Puede el equipo explicar, paso a paso, cómo el agente llegó a cualquier output específico?
- ¿El sistema tiene un mecanismo de parada de emergencia que un operador humano puede activar?
- ¿El sistema ha sido probado con inputs que producen fallos en las herramientas y en los pasos de verificación?
- ¿El costo máximo posible por tarea está acotado y dentro de los parámetros económicos del servicio?
- ¿Hay un proceso definido para revisar y actualizar el sistema cuando los modelos subyacentes cambian?
