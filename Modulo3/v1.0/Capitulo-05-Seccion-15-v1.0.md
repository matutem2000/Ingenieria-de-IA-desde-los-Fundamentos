# Capítulo 05 - Sección 15

# Transición al siguiente capítulo

> Módulo 3 — Context Engineering Profesional

---

# Lo que construimos en este capítulo

Este capítulo transformó las instrucciones del sistema de un elemento difuso —ese "texto que se pone al principio"— en un componente de arquitectura con estructura, patrones, restricciones y ciclo de vida propios.

Aprendimos a diseñar instrucciones que:

- operan correctamente dentro de la jerarquía de autoridad del proveedor y el usuario;
- tienen una anatomía de seis bloques con funciones diferenciadas;
- expresan restricciones como comportamientos observables, no como intenciones;
- separan las reglas permanentes del contexto dinámico;
- cubren el caso especial de los agentes con herramientas;
- se mantienen y evolucionan en producción con criterio de ingeniería.

---

# La pregunta que dejamos abierta

La sección 06 de este capítulo identificó uno de los principios arquitectónicos más importantes del módulo: la separación entre las instrucciones del sistema y el contexto dinámico.

Esa separación responde la pregunta de qué no debe estar en las instrucciones del sistema. Pero no responde qué sí debe estar en el contexto dinámico, cómo se construye ese contexto, cuándo se ensambla, cómo se actualiza y cómo se evita que llegue información inoportuna o desactualizada al modelo.

Esa es exactamente la pregunta que abre el capítulo 06.

---

# El capítulo 06: Contexto dinámico

Si las instrucciones del sistema son la capa estable del contexto —las reglas que no cambian entre conversaciones—, el contexto dinámico es la capa viva: la información que llega al modelo en tiempo de ejecución y que hace posible que el mismo asistente responda de manera diferente según el usuario, el momento y el estado de la aplicación.

El capítulo 06 estudia:

- **El estado de la aplicación y de la tarea:** qué información sobre el contexto operativo actual necesita el modelo para razonar correctamente.
- **El perfil, preferencias y permisos del usuario:** cómo incorporar información del usuario actual sin violar la separación de capas.
- **Tiempo, ubicación y vigencia de los datos:** cómo manejar información sensible al tiempo y cómo detectar cuándo un dato se ha vuelto obsoleto.
- **Variables, eventos y señales externas:** cómo el estado del mundo exterior llega al contexto del modelo.
- **Ensamblado de contexto en tiempo de ejecución:** el proceso técnico de construir el contexto completo antes de cada invocación al modelo.
- **Separación entre datos, instrucciones y contenido no confiable:** cómo evitar que diferentes tipos de información se contaminen entre sí.
- **Trazabilidad y depuración:** cómo hacer que el razonamiento del modelo sea auditable.

---

# La continuidad arquitectónica

Si miramos el módulo como un todo, la arquitectura de contexto que estamos construyendo tiene capas que se superponen de manera ordenada:

```text
┌─────────────────────────────────────────────┐
│ Respuesta del modelo                        │
├─────────────────────────────────────────────┤
│ Herramientas y resultados (Cap. 07)         │
├─────────────────────────────────────────────┤
│ Conocimiento recuperado - RAG (Cap. 07)     │
├─────────────────────────────────────────────┤
│ Contexto dinámico (Cap. 06) ← próximo       │
├─────────────────────────────────────────────┤
│ Historial y memoria (Cap. 04)               │
├─────────────────────────────────────────────┤
│ Instrucciones del sistema (Cap. 05) ← aquí  │
└─────────────────────────────────────────────┘
```

Cada capítulo del módulo agrega una capa a esa arquitectura. Las instrucciones del sistema, que estudiamos aquí, son el fundamento sobre el cual se apoyan todas las demás capas.

---

# Una reflexión práctica antes de continuar

Antes de pasar al capítulo 06, vale la pena detenerse en una observación que aparece frecuentemente en equipos que comienzan a implementar estas prácticas.

La tentación más común en ese momento es la siguiente: una vez que se aprende a diseñar bien las instrucciones del sistema, se tiende a querer resolver todo desde esa capa. Cuando el asistente no se comporta como se espera, el primer reflejo suele ser agregar más texto a las instrucciones del sistema.

Ese reflejo produce el anti-patrón de la instrucción infinita.

La respuesta correcta, en la mayoría de los casos, no es agregar más instrucciones. Es identificar si el problema es de instrucciones (en cuyo caso, refinarlas con precisión) o de contexto dinámico (en cuyo caso, enriquecer la información que llega al modelo en tiempo de ejecución).

El capítulo 06 entrega las herramientas para hacer esa distinción de manera informada.

---

# Resumen

Este capítulo completó el estudio de las instrucciones del sistema como disciplina de ingeniería. El siguiente capítulo avanza hacia el contexto dinámico, la capa que convierte a un asistente genérico en una aplicación que conoce a su usuario, entiende su situación actual y tiene acceso a la información más relevante del momento en que ocurre la interacción.
