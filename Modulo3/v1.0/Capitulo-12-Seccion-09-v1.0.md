# Capítulo 12 — Context Engineering Empresarial

## Sección 09: Patrones y anti-patrones empresariales

Los patrones que funcionan en producción corporativa no son los mismos que funcionan en un prototipo de laboratorio. En el laboratorio, las condiciones son controladas: el conocimiento está bien curado, los usuarios son técnicamente sofisticados, los volúmenes son pequeños y el equipo está disponible para intervenir cuando algo falla. En producción corporativa, las condiciones son las del mundo real: el conocimiento es heterogéneo, los usuarios tienen expectativas variables, los volúmenes son impredecibles y el equipo no puede intervenir manualmente en cada incidente.

Esta sección cataloga los patrones que han demostrado funcionar en ese contexto real, y los anti-patrones que producen problemas recurrentes independientemente de la calidad técnica del equipo que los implementa.

---

### Patrones que funcionan

**Patrón 1: Contexto mínimo suficiente**

El principio es construir el contexto más pequeño que produce la calidad de respuesta requerida, y no más.

La tentación habitual es agregar más contexto para cubrir más casos: más instrucciones en el system prompt para manejar más situaciones, más documentos en la base vectorial para tener más cobertura, más historia de conversación para que el modelo no "olvide". Cada uno de esos agregados tiene un costo: más tokens, más latencia, más costo de inferencia y frecuentemente peor calidad de recuperación porque la señal se diluye entre más fragmentos.

El contexto mínimo suficiente requiere un proceso iterativo: comenzar con el contexto mínimo plausible, medir la calidad de las respuestas, identificar los casos donde la calidad es insuficiente, agregar el contexto necesario para esos casos específicos, y repetir. El objetivo no es maximizar el contexto; es encontrar el mínimo que satisface los requisitos de calidad definidos.

**Patrón 2: Separación entre conocimiento estático y dinámico**

El conocimiento que cambia raramente —políticas, manuales, especificaciones de productos— se indexa en la base vectorial. El conocimiento que cambia frecuentemente —estado de pedidos, disponibilidad de inventario, datos de la sesión del cliente— se recupera dinámicamente como herramienta en el momento de la consulta.

Mezclar conocimiento estático y dinámico en la misma base vectorial produce problemas de vigencia difíciles de detectar y corregir. La separación permite aplicar estrategias de actualización apropiadas para cada tipo: reindexación periódica para el conocimiento estático, recuperación en tiempo real para el dinámico.

**Patrón 3: Degradación controlada**

El sistema define explícitamente cómo se comporta cuando alguno de sus componentes de contexto falla o no está disponible.

Si la base vectorial tiene una interrupción, el sistema puede continuar funcionando con el contexto estático de las instrucciones del sistema, informando al usuario que el conocimiento especializado no está temporalmente disponible. Si la integración con el CRM falla, el sistema puede responder preguntas que no requieren datos del cliente sin información personalizada. Si la historia de conversación no puede recuperarse, el sistema puede comenzar la conversación desde cero con una notificación apropiada.

Definir estos modos de degradación antes de que ocurran —como parte del diseño del sistema— permite que el sistema permanezca útil incluso durante incidentes parciales, en lugar de fallar completamente cuando cualquier componente tiene un problema.

**Patrón 4: Gobierno ligero y proceso explícito**

Un proceso de gobierno que existe en un documento pero que nadie sigue no es un proceso de gobierno; es un artefacto burocrático. El gobierno del conocimiento que funciona en la práctica es aquel que los propietarios del conocimiento pueden seguir sin que les tome más tiempo del que justifica el beneficio.

Un proceso de incorporación de documentos que requiere cinco aprobaciones y tres semanas no será seguido; los responsables buscarán formas de evitarlo. Un proceso que requiere una revisión por el propietario del área y un paso de verificación técnica es razonable y será seguido. La simplicidad del proceso es una variable de diseño del gobierno, no un detalle de implementación.

---

### Anti-patrones recurrentes

**Anti-patrón 1: La base de conocimiento acumulativa sin curación**

La base vectorial crece de forma acumulativa —se agregan documentos pero raramente se eliminan— sin un proceso de curación periódica. Con el tiempo, la base contiene una mezcla de documentos vigentes, documentos desactualizados, documentos duplicados con versiones contradictorias y documentos de baja calidad que nunca deberían haberse indexado.

El sistema de recuperación no distingue la calidad de los documentos; los recupera por similitud semántica. El resultado es que la calidad de las respuestas se degrada progresivamente a medida que la base crece de forma no curada. Los usuarios no ven esta degradación en la arquitectura; la ven en respuestas cada vez más inconsistentes que no pueden explicar.

La solución es tratar la base de conocimiento como un activo que requiere mantenimiento activo, con auditorías periódicas y un proceso de retiro de documentos obsoletos tan definido como el proceso de incorporación.

**Anti-patrón 2: Instrucciones del sistema como especificación de requisitos**

El system prompt de producción crece de forma orgánica cada vez que el sistema produce una respuesta inesperada: alguien agrega una instrucción para corregir ese comportamiento específico. Con el tiempo, el system prompt se convierte en un documento de centenares de reglas, muchas de las cuales contradicen parcialmente a otras o abordan casos que nunca volvieron a ocurrir.

Un system prompt inflado de esta forma tiene varias consecuencias negativas: el modelo tiene dificultades para priorizar instrucciones que se contradicen, el costo de tokens por llamada crece, y nadie entiende completamente qué hace el sistema cuando recibe una consulta nueva.

La solución es gestionar las instrucciones del sistema como código: con control de versiones, con revisiones de refactorización periódicas que eliminan reglas obsoletas o contradictorias, y con pruebas que verifican que el conjunto de instrucciones produce el comportamiento correcto para el conjunto de casos de referencia.

**Anti-patrón 3: El sistema de IA como fuente de verdad**

Los usuarios comienzan a tratar al sistema de IA como la fuente de verdad sobre las políticas y datos de la organización, en lugar de como una interfaz para acceder a las fuentes de verdad reales. Cuando el conocimiento en la base vectorial está desactualizado, el sistema produce respuestas incorrectas que los usuarios aceptan como oficiales porque "el sistema lo dijo".

Este anti-patrón es especialmente peligroso porque el sistema puede estar técnicamente funcionando —recuperando fragmentos con alta similitud, generando respuestas fluidas— mientras que las respuestas son factualmente incorrectas.

La solución tiene dos componentes: técnico —incluir en las respuestas del sistema la referencia a la fuente y la fecha del conocimiento que está usando, para que el usuario pueda verificar si la información es reciente— y de gobierno —establecer un proceso riguroso de actualización del conocimiento indexado que evite que la base vectorial quede significativamente detrás de las fuentes autorizadas—.

**Anti-patrón 4: El prototipo que nunca deja de serlo**

Un prototipo que empieza siendo usado por cinco usuarios del equipo de IA termina siendo adoptado por cincuenta usuarios de negocio sin que el sistema haya pasado por ningún proceso de productización: sin controles de acceso formales, sin monitoreo de calidad, sin proceso de actualización del conocimiento, sin documentation de usuario, sin proceso de soporte para cuando el sistema produce respuestas incorrectas.

Este anti-patrón es especialmente frecuente porque el prototipo funciona bien para los cinco usuarios iniciales, que son técnicamente sofisticados y saben compensar sus limitaciones. Cuando los cincuenta usuarios de negocio empiezan a usarlo, encuentran un sistema que no tiene la robustez que esperan de un sistema corporativo.

La solución es tener criterios explícitos de producción que deben satisfacerse antes de abrir el acceso a usuarios de negocio: proceso de gobierno definido, monitoreo implementado, soporte diseñado, documentación de usuario disponible.

### La tabla diagnóstica

| Síntoma observable | Causa más probable | Patrón a aplicar |
|---|---|---|
| Respuestas inconsistentes entre sesiones | Base de conocimiento desactualizada o conflictiva | Curación periódica + patrón de vigencia |
| Latencia creciente sin aumento de carga | Contexto inflado acumulativamente | Contexto mínimo suficiente |
| Usuarios que evitan el sistema | Respuestas incorrectas repetidas | Diagnóstico de recuperación + actualización |
| Comportamiento inesperado ante consultas nuevas | System prompt contradictorio | Refactorización de instrucciones |
| Diferentes respuestas de distintos asistentes | Silos de contexto sin coordinación | Contexto compartido entre equipos |

### Nota del arquitecto

Los anti-patrones descritos en esta sección no son el resultado de equipos poco capaces. Son el resultado de que los problemas de producción corporativa no son evidentes cuando se diseña el sistema desde la perspectiva del caso feliz: el documento que siempre está actualizado, el usuario que siempre formula sus preguntas claramente, el sistema corporativo que nunca tiene una interrupción. La diferencia entre un arquitecto experimentado y uno novato no está en la elegancia de los casos felices; está en el diseño de la respuesta correcta ante los casos que inevitablemente no son felices.

La siguiente sección aplica todos estos conceptos en un caso de estudio completo: una organización de mediana escala implementando Context Engineering a nivel corporativo, con todos los problemas reales que ese proceso involucra.
