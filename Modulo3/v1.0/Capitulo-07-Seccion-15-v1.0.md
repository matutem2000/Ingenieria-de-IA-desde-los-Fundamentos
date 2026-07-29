# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 15 — Transición al Capítulo 08

Las herramientas le dan al modelo la capacidad de actuar en el mundo. Consultar una base de datos, cancelar un pedido, enviar una notificación: con las herramientas correctamente diseñadas, el modelo puede resolver en segundos lo que antes requería intervención humana. Este capítulo construyó el marco completo para diseñar ese nivel de integración — desde la definición de herramientas individuales hasta la arquitectura de sistemas con docenas de herramientas en entornos empresariales.

Pero hay una categoría de problemas que el modelo-con-herramientas no puede resolver eficientemente: los problemas que requieren múltiples ciclos de razonamiento a lo largo del tiempo, con estado persistente entre sesiones, con capacidad de revisar y corregir el propio trabajo, o con la coordinación de múltiples agentes especializados trabajando en paralelo.

Un asistente de atención al cliente que responde un ticket es un sistema de herramientas. Un sistema que analiza cientos de tickets, identifica patrones, redacta un informe de tendencias, propone cambios en los procesos de la empresa, y los implementa coordinando con múltiples sistemas — ese es un sistema de agentes.

### La distinción que importa

La diferencia no es de grado sino de arquitectura:

**Sistema con herramientas** (este capítulo):
- Un ciclo de razonamiento por interacción con el usuario.
- El modelo decide qué herramientas invocar para responder una solicitud específica.
- El estado existe solo dentro del contexto de la interacción.
- La autonomía es limitada: el modelo invoca herramientas, pero el usuario inicia y cierra cada interacción.
- El control humano es frecuente (confirmaciones, intervenciones en acciones de alto impacto).

**Sistema de agentes** (capítulo 08):
- Múltiples ciclos de razonamiento que se extienden en el tiempo.
- El agente planifica, ejecuta, evalúa resultados y decide si continuar, revisar o abandonar.
- El estado persiste entre sesiones y puede ser compartido entre múltiples agentes.
- La autonomía es mayor: el sistema puede actuar sin intervención humana durante períodos extendidos.
- El control humano se diseña en puntos específicos del flujo, no en cada acción.

Las herramientas son el mecanismo de ejecución de los agentes. Un agente sin herramientas puede razonar pero no puede actuar. Lo que diferencia al capítulo siguiente no son las herramientas en sí — los principios de diseño de herramientas desarrollados en este capítulo se aplican directamente a los sistemas de agentes — sino la arquitectura que coordina múltiples instancias de razonamiento y acción a lo largo del tiempo.

### Lo que el capítulo 08 agrega

El capítulo 08 — Sistemas Multi-Agente y Orquestación — desarrolla:

**El ciclo ReAct.** El patrón Razonamiento-Acción-Observación que estructura cómo un agente decide qué hacer, ejecuta una acción, observa el resultado y decide el siguiente paso. Este ciclo puede repetirse decenas o cientos de veces antes de que el agente llegue a un resultado.

**La memoria del agente.** Cómo el agente mantiene estado entre ciclos y entre sesiones: memoria a corto plazo en el contexto, memoria a largo plazo en sistemas de almacenamiento externo, y cómo diseñar qué información persiste y qué se descarta.

**La arquitectura multi-agente.** Cómo múltiples agentes especializados se coordinan para resolver problemas que ningún agente individual puede resolver solo: un agente orquestador que delega tareas a agentes especializados (agente de investigación, agente de redacción, agente de verificación), con comunicación entre ellos y consolidación de resultados.

**El control de autonomía.** Cómo decidir en qué puntos del flujo un agente necesita intervención humana, cómo implementar "checkpoints" de aprobación, y cómo diseñar sistemas que fallen de forma segura cuando el agente se desvía del comportamiento esperado.

### El marco que llevas contigo

Las herramientas bien diseñadas son la base de los sistemas de agentes. Un agente que invoca herramientas mal definidas tendrá el mismo comportamiento impredecible que cualquier sistema de herramientas mal diseñado — solo que con mayor autonomía, lo que amplifica el impacto de cada error.

Los principios de esta parte del libro se construyen en capas:

- El capítulo 05 y 06 establecieron cómo gestionar el contexto — la información que el sistema mantiene para razonar.
- El capítulo 07 estableció cómo integrar el mundo externo — las herramientas que el sistema puede invocar para actuar.
- El capítulo 08 establece cómo coordinar múltiples ciclos de razonamiento y acción — la arquitectura que convierte herramientas en agentes.

Cada capa asume que la anterior está bien construida. Un agente que opera sobre un contexto mal gestionado o con herramientas mal diseñadas es un sistema frágil, independientemente de la sofisticación de su arquitectura de orquestación.

El trabajo del capítulo 07 — definir herramientas con contratos claros, descripciones operativas precisas, manejo de errores robusto y controles de seguridad apropiados — es la inversión que el capítulo 08 rentabiliza.
