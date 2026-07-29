# Capítulo 04 — Sección 10

# Anti-patrones

Los anti-patrones son soluciones que parecen razonables —o que son consecuencia natural de tomar el camino de menor resistencia— pero que producen problemas predecibles en producción. Esta sección describe los anti-patrones más frecuentes en sistemas de memoria de IA, sus síntomas y las correcciones que los resuelven.

## Anti-patrón 1: La memoria esponja (guardar todo)

**Descripción:** el sistema guarda cada mensaje, cada dato mencionado en cada conversación, sin ningún criterio de selectividad. La premisa implícita es "más memoria es mejor".

**Por qué ocurre:** es la implementación de menor esfuerzo. Si no hay criterio de qué guardar, guardar todo evita el problema de decidir.

**Síntomas en producción:**
- La base de datos de memoria crece sin control.
- La recuperación semántica devuelve memorias irrelevantes que contaminan el contexto.
- El sistema recuerda detalles triviales ("el usuario preguntó qué temperatura hace en Madrid") con la misma prominencia que información crítica.
- Las respuestas del modelo se vuelven ruidosas porque el contexto inyectado contiene memorias irrelevantes mezcladas con las relevantes.
- El costo operativo (almacenamiento + computación de embeddings) crece de forma no sostenible.

**Corrección:** implementar un componente de captura selectiva (Memory Extractor, patrón de la sección anterior) con criterios explícitos de qué merece ser persistido. El criterio mínimo: ¿esta información tiene valor en una sesión futura? Si la respuesta no es claramente sí, no persiste.

---

## Anti-patrón 2: El contexto desbordado (memory dumping)

**Descripción:** el sistema recupera toda la memoria disponible sobre el usuario y la inyecta en el contexto al inicio de cada sesión, sin importar su relevancia para la consulta actual.

**Por qué ocurre:** es el equivalente de "mejor que sobre que no falte". El sistema no tiene un componente de Context Assembly, así que vuelca todo lo que encuentra.

**Síntomas en producción:**
- El costo de tokens por sesión es alto incluso para consultas simples.
- Las respuestas del modelo muestran referencias a memorias irrelevantes ("ya sé que preferís Python, aunque tu pregunta sea sobre una hoja de cálculo").
- El fenómeno "lost in the middle": el modelo pierde el foco en la consulta real porque está enterrada bajo demasiado contexto de memoria.
- En conversaciones largas, se alcanza el límite de contexto prematuramente porque la memoria inyectada ocupa demasiado espacio.

**Corrección:** implementar un Context Assembler que seleccione y priorice la memoria según su relevancia para la consulta actual. La memoria inyectada debe ser suficiente para contextualizar, no exhaustiva.

---

## Anti-patrón 3: La memoria muerta (nunca se actualiza)

**Descripción:** el sistema guarda información la primera vez que la captura pero nunca la actualiza, incluso cuando el usuario provee información más reciente o contradictoria.

**Por qué ocurre:** el sistema tiene mecanismo de escritura pero no de actualización. Cada hecho nuevo se guarda como registro nuevo, sin verificar si existe un registro anterior sobre el mismo tema.

**Síntomas en producción:**
- La memoria contiene versiones contradictorias del mismo hecho: "el usuario trabaja en empresa A" y "el usuario trabaja en empresa B".
- El modelo recibe ambas versiones en el contexto y produce respuestas ambiguas o elige arbitrariamente una de las dos.
- El usuario corrije al sistema ("te dije que ahora trabajo en X") pero el sistema sigue usando la información anterior en sesiones futuras.
- La confianza del usuario en el sistema se degrada.

**Corrección:** implementar el patrón Upsert Semántico (sección 09). Antes de guardar cualquier hecho nuevo, verificar si existe un registro con alta similitud semántica. Si existe, actualizar en lugar de insertar.

---

## Anti-patrón 4: La memoria fantasma (sin TTL ni expiración)

**Descripción:** toda la memoria persiste indefinidamente. No hay mecanismo de expiración, archivado ni eliminación por caducidad.

**Por qué ocurre:** el equipo se concentró en el diseño de captura y recuperación, y no pensó en el ciclo de vida de la memoria.

**Síntomas en producción:**
- El sistema usa información desactualizada con plena confianza: menciona proyectos que cerraron, habla de restricciones que ya no aplican, asume un contexto organizacional que cambió.
- Los usuarios experimentan que el sistema "está viviendo en el pasado".
- A medida que pasa el tiempo, la proporción de memorias desactualizadas crece, degradando la calidad general del sistema.

**Corrección:** implementar TTL diferenciado por tipo de información (como se describió en la sección 07). Los hechos volátiles expiran rápido; los hechos estables expiran lentamente o cuando son explícitamente contradichos.

---

## Anti-patrón 5: La memoria opaca (sin visibilidad para el usuario)

**Descripción:** el sistema tiene memoria persistente pero el usuario no sabe qué recuerda sobre él, no puede consultarla y no puede corregirla.

**Por qué ocurre:** el equipo implementó la memoria como un componente interno sin interfaz de usuario. La transparencia no se consideró un requisito de diseño.

**Síntomas en producción:**
- El usuario percibe que el sistema "inventó" preferencias que nunca expresó.
- El usuario no puede corregir una memoria incorrecta excepto repitiendo la corrección hasta que el sistema la captura.
- El usuario no sabe si sus datos están siendo guardados, qué datos son o durante cuánto tiempo.
- En contextos empresariales, esto puede generar desconfianza o directamente violar regulaciones de privacidad.

**Corrección:** diseñar una interfaz de gestión de memoria —aunque sea mínima— que permita al usuario ver qué recuerda el sistema sobre él y eliminar o corregir entradas específicas. Esta interfaz puede ser tan simple como un comando `/memoria` dentro del chat, o tan elaborada como una pantalla de configuración de perfil.

---

## Anti-patrón 6: La memoria centralizada en el prompt de sistema (hardcoding de contexto)

**Descripción:** en lugar de diseñar memoria dinámica, el equipo escribe la información del usuario directamente en el system prompt de forma estática. El "diseño de memoria" consiste en un texto fijo que dice "eres un asistente para el equipo de finanzas de empresa X".

**Por qué ocurre:** es la solución de prototipo que escala mal. Funciona para un sistema de un solo cliente y un solo contexto, pero no escala a múltiples usuarios con contextos distintos.

**Síntomas en producción:**
- El sistema funciona bien para el caso de uso para el que fue configurado y falla para cualquier variación.
- Todos los usuarios reciben exactamente el mismo contexto, sin personalización.
- Actualizar el contexto requiere modificar y redesplegar el system prompt.
- Es imposible adaptar el sistema a nuevos usuarios sin intervención de ingeniería.

**Corrección:** separar el system prompt estático (instrucciones de comportamiento) de la memoria dinámica (contexto del usuario). El system prompt define cómo debe comportarse el sistema; la memoria dinámica provee el contexto específico de cada usuario, recuperado en tiempo de ejecución.

---

## Tabla resumen de anti-patrones

| Anti-patrón | Síntoma principal | Corrección |
|---|---|---|
| Memoria esponja | Ruido en recuperación, costo descontrolado | Captura selectiva con criterios explícitos |
| Context dumping | Context saturado, respuestas ruidosas | Context Assembler por relevancia |
| Memoria muerta | Contradicciones, información desactualizada | Upsert semántico con detección de conflictos |
| Memoria fantasma | "Viviendo en el pasado" | TTL diferenciado por tipo de dato |
| Memoria opaca | Desconfianza, incapacidad de corregir | Interfaz de gestión de memoria para el usuario |
| Hardcoding de contexto | Sin personalización, no escala | Memoria dinámica separada del system prompt |

---

*La siguiente sección presenta un caso de estudio empresarial concreto que integra los patrones vistos y muestra las decisiones de diseño tomadas en un sistema real de producción.*
