# Capítulo 05 - Sección 06

# Separación entre instrucciones y contexto dinámico

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Uno de los errores de arquitectura más frecuentes en aplicaciones de IA en producción es colocar en la capa de instrucciones del sistema información que debería estar en el contexto dinámico. Este error parece inofensivo al principio, pero genera problemas crecientes a medida que la aplicación escala.

Esta sección explica por qué la separación importa, cómo identificar cuándo se está violando y cómo refactorizar una instrucción del sistema que mezcla ambas capas.

---

# Objetivos de esta sección

Al finalizar esta sección el lector podrá:

- Distinguir con precisión qué pertenece a las instrucciones del sistema y qué al contexto dinámico.
- Identificar los síntomas de una instrucción del sistema con mezcla de capas.
- Refactorizar instrucciones que incluyen información dinámica en la capa de sistema.
- Diseñar arquitecturas donde las capas estática y dinámica del contexto estén claramente separadas.

---

# La regla de la permanencia

Una pregunta útil para decidir si algo pertenece a las instrucciones del sistema o al contexto dinámico es:

> ¿Cambiaría esta información si el mismo asistente atendiese a otro usuario, en otro momento, con otro estado de la aplicación?

Si la respuesta es sí, esa información es dinámica y no pertenece a las instrucciones del sistema.

| Información | ¿Pertenece al sistema? |
|---|---|
| El rol del asistente | Sí |
| El idioma de respuesta | Sí (si es fijo) |
| Las restricciones de seguridad | Sí |
| El nombre del usuario actual | No |
| El saldo de cuenta del usuario | No |
| Los últimos tickets del usuario | No |
| Los resultados de una consulta a la API | No |
| La fecha y hora actual | No |
| Los documentos relevantes recuperados por RAG | No |

---

# Anti-patrón: información dinámica en la capa de sistema

El siguiente es un ejemplo real del tipo de instrucción del sistema que aparece con frecuencia en aplicaciones construidas sin esta distinción:

```text
Sos el asistente de Ana García, cliente premium de DataFlux.
Ana tiene una cuenta con 5 usuarios activos y 3 proyectos.
Sus últimos tickets fueron: TK-2341 (resuelto), TK-2398 (pendiente).
Tiene pendiente renovar su suscripción el 15 de agosto de 2026.
No puede acceder al módulo de exportación porque su plan no lo incluye.
El sistema está actualmente en mantenimiento programado los martes
entre las 22:00 y las 00:00.

Respondé a sus consultas de soporte con acceso a esta información.
```

Esta instrucción parece razonable en una demostración. En producción genera los siguientes problemas:

---

## Problema 1: La instrucción envejece

La fecha de vencimiento del 15 de agosto, el estado de los tickets, el mantenimiento programado: toda esta información cambia. Cada cambio requiere actualizar la instrucción del sistema. En una aplicación con miles de usuarios, eso significa instrucciones distintas por usuario y actualizaciones constantes.

---

## Problema 2: Mayor costo en cada conversación

Cada invocación al modelo incluye la instrucción del sistema completa. Si esa instrucción contiene datos del usuario, datos de tickets, estados de cuenta y otras informaciones dinámicas, el costo en tokens aumenta incluso cuando esa información no es relevante para la consulta específica.

---

## Problema 3: Dificultad para evolucionar la aplicación

Cuando las instrucciones del sistema mezclan reglas permanentes con datos dinámicos, cualquier cambio en las reglas requiere re-ensamblar y verificar toda la instrucción. El mantenimiento se vuelve propenso a errores.

---

## Problema 4: Riesgo de datos obsoletos

Si la instrucción se construyó al inicio de la sesión y la sesión dura tiempo, la información puede quedar desactualizada. El modelo podría decirle a un usuario que su ticket TK-2398 está pendiente cuando ya fue resuelto treinta minutos antes.

---

# Refactorización: la versión correcta

La misma funcionalidad puede lograrse de manera limpia separando las capas:

**Instrucción del sistema (estática):**
```text
Sos el asistente de soporte de DataFlux. Tu función es ayudar a
los usuarios a resolver consultas técnicas, revisar el estado de
sus tickets y entender las capacidades de su plan.

El contexto del usuario (nombre, plan, tickets activos, estado de
su cuenta) te será proporcionado al inicio de cada conversación.
Usá esa información para personalizar tus respuestas, pero no la
memorices más allá de la conversación actual.

Si el usuario pregunta por información que no está en el contexto
proporcionado, indicale que no tenés esa información disponible
y sugerile que revise su panel de usuario o contacte al equipo
de soporte.
```

**Contexto dinámico (inyectado en cada llamada):**
```text
[CONTEXTO DEL USUARIO]
Nombre: Ana García
Plan: Premium
Usuarios activos: 5
Proyectos: 3
Tickets activos: TK-2398 (Pendiente - Problema de exportación)
Vencimiento de suscripción: 2026-08-15
Restricciones del plan: Sin acceso al módulo de exportación avanzada.
Mantenimiento programado: Martes 22:00 - 00:00 ART.
[FIN DEL CONTEXTO]
```

Esta separación logra lo mismo pero con una diferencia fundamental: la instrucción del sistema no cambia entre usuarios ni entre sesiones. Solo el bloque de contexto dinámico se actualiza.

---

# Dónde va el contexto dinámico

La información dinámica puede inyectarse en varios lugares del contexto, dependiendo de la arquitectura:

- **En el mensaje del sistema**, como un bloque separado claramente marcado (como en el ejemplo anterior).
- **En el primer mensaje de usuario**, como parte del turno de apertura de la conversación.
- **Como mensajes de herramienta**, cuando la información proviene de una consulta a una API o base de datos.

La elección depende del modelo, del proveedor y de los límites de la interfaz de programación disponible. Lo que no debe cambiar es el principio: las reglas permanentes y los datos temporales van en capas separadas.

---

# Un caso más sutil: instrucciones que parecen estables pero no lo son

Algunas instrucciones parecen estables pero dependen de información que cambia:

```text
El asistente puede ayudar con los módulos A, B y C.
```

Si los módulos disponibles dependen del plan del usuario o de la versión del producto, esta instrucción no es estable. Hoy puede ser A, B y C; mañana puede ser A, B, C y D; o puede ser solo A para usuarios con plan básico.

La instrucción correcta en este caso:

```text
El asistente puede ayudar con los módulos que se listan en el
contexto del usuario proporcionado al inicio de la conversación.
```

---

# Nota del arquitecto

Una manera práctica de verificar si la separación es correcta es preguntarse: ¿puedo reutilizar exactamente la misma instrucción del sistema para usuarios diferentes con planes diferentes y estados diferentes?

Si la respuesta es sí, la separación está bien lograda. Si la respuesta es no, hay información dinámica en la capa de sistema.

---

# Resumen

La separación entre instrucciones permanentes y contexto dinámico es uno de los principios de arquitectura más importantes del diseño de sistemas de IA. Las instrucciones del sistema deben contener solo aquello que es verdadero para todos los usuarios, en todos los momentos y en todos los estados de la aplicación. Todo lo demás es contexto dinámico.

En la siguiente sección estudiaremos el caso particular de los agentes con acceso a herramientas, donde el diseño de instrucciones del sistema requiere considerar dimensiones adicionales de complejidad y riesgo.
