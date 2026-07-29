# Capítulo 15 — Proyecto Integrador

## Sección 01: Introducción al proyecto integrador

A lo largo del Módulo 3 construiste las piezas de un rompecabezas: instrucciones del sistema, ventanas de contexto, memoria persistente, recuperación aumentada por recuperación, herramientas externas, agentes, observabilidad y seguridad. Cada capítulo desarrolló esas piezas por separado, con casos enfocados y ejercicios acotados. Este capítulo las ensambla.

El proyecto integrador no es un repaso ni un resumen. Es una instancia de síntesis activa: diseñarás una solución de IA de extremo a extremo, tomarás decisiones de arquitectura reales con restricciones reales, y documentarás el razonamiento detrás de cada elección. Al final del capítulo tendrás un artefacto completo: una arquitectura de referencia con sus decisiones justificadas, un laboratorio para verificar tu comprensión, y un checklist profesional que podrás aplicar a cualquier proyecto propio.

### Qué cubre este capítulo

El capítulo se organiza en cuatro bloques:

**Bloque 1 — Marco del proyecto (secciones 01–03).** Define el problema de negocio que servirá como hilo conductor, establece los requisitos que la solución debe satisfacer y produce el diagrama de arquitectura completa que integra todos los componentes del módulo.

**Bloque 2 — Diseño dimensional (secciones 04–08).** Examina cada dimensión técnica por separado: cómo se diseñan el contexto y la memoria, cómo se integran RAG y herramientas, cómo se incorporan los agentes, cómo se instrumenta la observabilidad y la seguridad, y cómo se planifica el despliegue.

**Bloque 3 — Revisión crítica y laboratorio (secciones 09–11).** Identifica los errores que emergen cuando se integran componentes (distintos de los errores que aparecen en componentes aislados), presenta el caso completo de implementación como referencia, y propone el laboratorio guiado en tres niveles de profundidad.

**Bloque 4 — Cierre del módulo (secciones 12–15).** Entrega el checklist profesional definitivo, resume los principios fundamentales del Context Engineering, propone criterios de autoevaluación y establece el puente hacia el Módulo 4.

### El caso de referencia

Para que el proyecto sea concreto, trabajarás a lo largo de todo el capítulo con un único caso de negocio: el asistente empresarial interno de TechCore S.A., una organización de doscientas personas con departamentos de TI, Legal, Recursos Humanos y Finanzas. Ese caso fue seleccionado porque obliga a usar todos los componentes del módulo: instrucciones del sistema diferenciadas por departamento, memoria de usuario, RAG sobre documentación interna, herramientas de sistemas corporativos, un agente de análisis de incidentes, observabilidad operacional y controles de acceso por rol.

La selección de un caso de complejidad intermedia es deliberada. Un caso trivial —un chatbot de preguntas frecuentes— no requiere agentes ni memoria persistente y no ejercita la arquitectura completa. Un caso de máxima complejidad —un sistema multiagente distribuido globalmente— introduce dificultades de infraestructura que oscurecen las decisiones de Context Engineering. TechCore ocupa el punto medio: suficientemente ambiguo para que las decisiones de diseño no sean únicas ni obvias, suficientemente concreto para que el análisis sea preciso.

### Cómo trabajar este capítulo

Cada sección introduce un aspecto del diseño y lo aplica al caso TechCore. El objetivo no es que memorices la arquitectura resultante sino que entiendas el razonamiento que la produce. Cuando leas las justificaciones de cada decisión, pregúntate si en tu propio contexto profesional ese razonamiento cambiaría y por qué. La arquitectura de TechCore es una referencia, no un modelo universal.

El laboratorio integrador (sección 11) está diseñado para que puedas completarlo sin infraestructura de producción. Requiere diagramas, documentación de decisiones y análisis de riesgos, no despliegues en la nube ni acceso a APIs empresariales. Lo que se evalúa es la capacidad de diseñar y justificar, no la de ejecutar.

---

Con ese marco establecido, la siguiente sección define el problema de negocio con precisión suficiente para que las decisiones de arquitectura tengan base concreta.
