# Capítulo 10 — Planificación y Razonamiento

## Sección 01: Introducción a la planificación y el razonamiento

Los capítulos anteriores de este módulo establecieron los bloques fundamentales del Context Engineering: cómo construir agentes, cómo coordinarlos y cómo gestionar la memoria que necesitan para operar con continuidad. Todo ese andamiaje, sin embargo, depende de una capacidad subyacente que aún no hemos examinado en profundidad: la capacidad del modelo de lenguaje para razonar sobre una tarea antes de actuar sobre ella.

Razonar, en el contexto de un LLM, no significa lo mismo que razonar en el sentido filosófico o matemático. Significa algo más específico y, para el AI Engineer, más útil: la capacidad de descomponer un problema en pasos intermedios, evaluar alternativas, detectar errores en la propia respuesta y revisar el plan antes de continuar. Estas capacidades no son propiedades intrínsecas del modelo; son propiedades que emergen cuando el arquitecto del sistema diseña el contexto correctamente.

Este capítulo estudia cómo funciona ese proceso desde adentro: qué ocurre cuando un LLM genera una cadena de pensamiento, qué arquitecturas de planificación existen y cuándo conviene usar cada una, cómo un agente puede reflexionar sobre su propio output y corregirlo, y cómo verificar los resultados de un sistema de razonamiento antes de que esos resultados lleguen al usuario o a otro sistema.

### Por qué este capítulo es diferente al capítulo 08

En el capítulo 08 se estudió el ciclo de vida del agente: percepción, planificación, acción y observación. La planificación aparecía allí como una etapa del ciclo, pero no se analizaba su estructura interna. El capítulo 10 entra en esa estructura. La pregunta no es qué hace el agente cuando planifica, sino cómo lo hace a nivel de llamadas al modelo, de diseño de prompt y de arquitectura de contexto.

La distinción es análoga a la diferencia entre describir que un motor de combustión produce movimiento (el ciclo del agente) y explicar cómo funciona el ciclo termodinámico interno (los mecanismos de razonamiento). Ambas perspectivas son necesarias. El capítulo 08 daba la primera; el capítulo 10 da la segunda.

### Qué va a encontrar el lector en este capítulo

El capítulo está organizado en cuatro bloques:

**Bloque conceptual** (secciones 01 a 03): qué significa razonar en un LLM, en qué se diferencia del razonamiento simbólico formal, y cuál es la taxonomía de patrones de planificación disponibles para el arquitecto de sistemas.

**Bloque de técnicas** (secciones 04 a 07): las técnicas concretas que implementan esos patrones — Chain of Thought, Tree of Thoughts, planificación iterativa, reflexión y verificación — con análisis de cuándo usar cada una, qué cuesta y qué riesgos presenta.

**Bloque de aplicación** (secciones 08 a 10): cómo estas técnicas se integran en arquitecturas empresariales reales, qué patrones funcionan y cuáles fallan en producción, y un caso de estudio completo que ilustra las decisiones de diseño en un contexto concreto.

**Bloque de cierre** (secciones 11 a 15): laboratorio práctico, checklist del AI Engineer, resumen, autoevaluación y transición al capítulo 11.

### Nivel de abstracción

Este capítulo trabaja al nivel de patrones de diseño, no de implementación de código. El objetivo es que el lector entienda la estructura de los mecanismos de razonamiento con suficiente profundidad para tomar decisiones de arquitectura correctas: cuándo un sistema necesita razonamiento multi-paso, cuándo la reflexión agrega valor y cuándo no, qué estrategia de verificación corresponde a cada tipo de output.

Los diagramas de flujo de llamadas al modelo reemplazan aquí a los fragmentos de código. Son más generalizables que cualquier SDK particular y capturan la lógica arquitectónica que permanece estable aunque las bibliotecas cambien.

La siguiente sección establece el fundamento conceptual imprescindible: qué significa, con precisión, que un LLM razone.
