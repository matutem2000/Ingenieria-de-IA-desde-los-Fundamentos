# Módulo 4 – Capítulo 09 – Sección 01

## Gobierno de Plataformas de IA

Los capítulos anteriores de este módulo describieron cómo construir, operar, proteger y escalar sistemas de IA individuales. El gobierno de plataformas de IA aborda una escala diferente: no la operación de un sistema específico, sino la gestión de múltiples sistemas de IA dentro de una organización, con políticas coherentes, procesos estandarizados, y estructuras de responsabilidad que permitan que la organización no solo despliegue IA sino que la opere con confianza a lo largo del tiempo.

La diferencia entre una organización que experimenta con IA y una que la ha institucionalizado es exactamente el gobierno. La organización que experimenta tiene proyectos de IA aislados que dependen de personas específicas, sin políticas de uso, sin estándares de calidad, sin procedimientos de actualización de modelos, y sin métricas de madurez. Cuando esa persona clave abandona el equipo, el proyecto entra en riesgo. Cuando el modelo del proveedor cambia de comportamiento, nadie detecta la degradación. Cuando la regulación de IA entra en vigor, la organización no puede demostrar que sus sistemas cumplen. El gobierno convierte esos proyectos aislados en capacidades organizacionales: repetibles, auditables, mejorables y sostenibles independientemente de las personas que los operan en un momento dado.

El gobierno de plataformas de IA se organiza en cinco dimensiones interdependientes:

**Políticas y estándares:** las reglas que definen cómo se construyen, documentan y despliegan los sistemas de IA en la organización. Cubren desde los estándares técnicos (qué modelos están aprobados para uso, cómo se versionan los prompts, qué métricas de evaluación son obligatorias) hasta las políticas de uso (qué tipos de datos pueden procesarse con IA, qué tipos de decisiones pueden automatizarse completamente, qué siempre requiere supervisión humana).

**Gestión del ciclo de vida de modelos:** los procesos que gobiernan el modelo desde su incorporación hasta su retiro. Incluye la evaluación inicial, el versionado, el monitoreo continuo de calidad, los procedimientos de actualización y migración, y el retiro planificado cuando el modelo ya no cumple los requisitos de calidad o de cumplimiento.

**Evaluación continua como práctica de gobierno:** la institucionalización de la evaluación de sistemas de IA como proceso periódico y sistemático. Cubre los frameworks de evaluación (RAGAS, LLM-as-judge, eval harnesses), los datasets de evaluación mantenidos por el equipo, las regresiones automáticas ante cambios de modelo o prompt, y las políticas que definen cuándo un resultado de evaluación requiere acción.

**Gestión de riesgos regulatorios:** la identificación, evaluación y mitigación de los riesgos legales, éticos y regulatorios de los sistemas de IA de la organización. Incluye el análisis de aplicabilidad del EU AI Act, la evaluación de impacto sobre derechos fundamentales, los procedimientos de notificación ante incidentes, y las responsabilidades legales asociadas a los outputs del sistema.

**Indicadores de madurez:** el sistema de medición que permite a la organización evaluar su progreso en la adopción responsable de IA y compararse con estándares externos.

> **Nota del Arquitecto:** El gobierno de IA en las organizaciones que conozco que lo hacen bien tiene una característica en común: empezaron a construirlo antes de que lo necesitaran urgentemente. El momento de diseñar las políticas de uso de IA no es cuando un incidente regula atorio obliga a hacerlo. Es cuando los primeros sistemas están en producción, cuando todavía es posible diseñar el gobierno para que facilite la innovación en lugar de frenarla. El gobierno diseñado en respuesta a una crisis tiende a ser burocrático y restrictivo; el gobierno diseñado proactivamente tiende a ser un habilitador.

Una buena gobernanza no limita la innovación; crea el marco necesario para que la innovación pueda escalar de forma segura y sostenible. Las secciones siguientes desarrollan cada dimensión del gobierno con los procesos, herramientas y criterios de madurez que la hacen operativa.
