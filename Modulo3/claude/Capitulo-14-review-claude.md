# Informe Pedagógico — Capítulo 14: Seguridad, Gobernanza y Compliance

**Revisado por:** Director Pedagógico / Claude
**Fecha:** 2026-07-25

---

## NOTA EDITORIAL PRIORITARIA

**El capítulo está en estado de esqueleto estructural. No existe contenido desarrollado en ninguna de sus 15 secciones.** Cada sección contiene únicamente: título, nota editorial de contexto, lista de objetivos genéricos, lista de elementos "previstos" y una frase de transición estándar.

**El capítulo no puede publicarse ni revisarse pedagógicamente en profundidad hasta que el contenido sea desarrollado.**

---

## 1. Fortalezas

**La decisión de incluir un capítulo dedicado a seguridad en un módulo de Context Engineering es correcta y diferenciadora.** La seguridad de sistemas de IA no es un tema solo de infraestructura: el diseño del contexto es la primera línea de defensa. Que esto aparezca como capítulo de cierre técnico (antes del proyecto integrador) le da el peso editorial que merece.

**La sección 03 ("Prompt Injection y ataques al contexto")** es el tema de seguridad más específico y relevante para este módulo. Prompt injection —cuando un usuario malintencionado intenta que el contenido del contexto modifique el comportamiento del modelo— es el ataque que el AI Engineer debe conocer y diseñar para prevenir.

**La sección 04 ("Gobernanza de modelos y datos")** extiende el capítulo más allá de la seguridad técnica hacia el gobierno organizacional: quién puede desplegar un modelo, quién aprueba cambios en el sistema prompt, qué datos pueden incluirse en el contexto. Este es el puente entre seguridad y compliance.

**La sección 08 ("Arquitecturas seguras para IA empresarial")** cierra el circuito de todo el módulo: las arquitecturas del Context Engineering no solo deben ser efectivas y escalables, sino también seguras por diseño. "Secure by design" aplicado a sistemas de IA.

**La sección 07 ("Cumplimiento normativo y auditoría")** es de alta relevancia en 2026, con regulaciones de IA emergentes en Europa (AI Act), Estados Unidos y múltiples jurisdicciones. El AI Engineer que no entiende los requerimientos de compliance difícilmente podrá trabajar en sectores regulados.

---

## 2. Debilidades

**La totalidad del contenido está ausente.** No hay análisis de amenazas, ejemplos de prompt injection, marcos de gobernanza ni referencias normativas desarrolladas.

**La sección 02 ("Amenazas específicas para LLM y agentes")** tiene el riesgo de quedarse incompleta o imprecisa.** El panorama de amenazas a LLMs es extenso: prompt injection (directo e indirecto), jailbreaking, data extraction, model inversion, adversarial inputs, supply chain attacks. El autor debe seleccionar las amenazas más relevantes para el contexto del Context Engineering y no intentar cubrirlas todas.

**La sección 05 ("Privacidad y protección de información")** requiere conocimiento legal específico que puede variar por jurisdicción (GDPR en Europa, HIPAA en salud en EEUU, protección de datos en Latinoamérica). El autor debe optar por principios de privacidad por diseño ("privacy by design") en lugar de especificidad legal, que envejece rápidamente.

**La sección 07 ("Cumplimiento normativo")** es de alta volatilidad regulatoria.** Las normativas de IA están en proceso de definición en 2026. El autor debe presentar principios de compliance que se mantengan válidos independientemente de la normativa específica, con referencias a regulaciones actuales en notas al pie.

**El capítulo podría presentarse como una reflexión final independiente**, sin conexión clara con los mecanismos técnicos del módulo. Para evitar esto, cada sección de seguridad debe estar ancla en elementos concretos del Context Engineering: prompt injection afecta las instrucciones del sistema, la privacidad afecta qué datos incluir en la memoria, el gobierno afecta quién controla el RAG.

---

## 3. Conceptos a ampliar (recomendaciones para el desarrollo)

**Prompt Injection directo vs. indirecto:** El directo ocurre cuando el usuario incluye instrucciones maliciosas en su mensaje. El indirecto ocurre cuando un documento recuperado por RAG o un resultado de herramienta contiene instrucciones maliciosas. El segundo es más peligroso y menos intuitivo; merece desarrollo específico.

**El principio del mínimo privilegio aplicado al contexto:** El capítulo 02 lo mencionó brevemente. Este capítulo debe desarrollarlo en profundidad: qué información no debe incluirse en el contexto aunque esté disponible, qué herramientas no deben exponerse aunque el modelo podría usarlas.

**Sandboxing de herramientas:** Cómo aislar la ejecución de herramientas para que un agente comprometido no pueda tomar acciones irreversibles (eliminar datos, enviar correos masivos, realizar transacciones). Cuándo usar ejecución en sandbox versus ejecución directa.

**Auditoría del contexto:** Cómo registrar qué información recibió el modelo, qué herramientas ejecutó y qué respuesta generó, para poder reproducir un incidente y cumplir con requerimientos de auditoría. Conecta con el capítulo 13 (observabilidad).

**AI Act y requerimientos de transparencia:** En Europa, el AI Act establece requerimientos de transparencia y documentación para sistemas de IA de alto riesgo. El capítulo debe al menos introducir qué implica esto para el diseñador de sistemas de Context Engineering.

---

## 4. Conceptos a resumir o eliminar

En el estado actual no hay contenido para resumir o eliminar.

Como advertencia preventiva: el capítulo tiene riesgo de intentar cubrir toda la seguridad de IA (que es un campo extenso) cuando su foco debe ser exclusivamente la seguridad específica del Context Engineering. Las amenazas genéricas de infraestructura (ataques de red, SQL injection en bases de datos) no pertenecen a este capítulo; las amenazas específicas del contexto (prompt injection, datos sensibles en RAG, herramientas sin control) sí.

---

## 5. Recomendaciones editoriales

1. **Desarrollar las 15 secciones** antes de cualquier revisión pedagógica posterior.

2. **Enmarcar el capítulo desde la primera sección** como "seguridad del Context Engineering", no como seguridad de IA en general. Cada amenaza y cada control debe estar vinculado a un componente específico del contexto estudiado en capítulos anteriores.

3. **Desarrollar la sección 03 ("Prompt Injection")** como el contenido técnico más profundo del capítulo: (a) definir directo e indirecto, (b) mostrar ejemplos concretos de cada tipo, (c) explicar por qué es difícil de mitigar completamente, (d) proporcionar controles de diseño: validación de entrada, separación de instrucciones y datos, instrucciones de contexto resistentes.

4. **Incluir en la sección 05 ("Privacidad")** un flujo de decisión: ¿este dato debe incluirse en el contexto? Si la respuesta es no (PII innecesaria, datos de otros usuarios, secretos corporativos), qué alternativa existe (dato anonimizado, dato resumido, referencia a registro seguro).

5. **Desarrollar la sección 08 ("Arquitecturas seguras")** con un conjunto de principios de diseño: secure by default (los controles de seguridad deben ser la configuración predeterminada, no una opción), defense in depth (múltiples capas de control), fail closed (en caso de error, el sistema debe denegar el acceso, no concederlo).

6. **Diseñar el laboratorio (sección 11)** como un ejercicio de threat modeling: dado un sistema de Context Engineering diseñado en el capítulo anterior, el estudiante identifica las tres principales amenazas de seguridad y propone controles para cada una.

7. **La sección 15 ("Transición al Capítulo 15")** debe establecer que todos los conceptos del módulo —arquitectura, memoria, RAG, herramientas, agentes, observabilidad y seguridad— convergen en el proyecto integrador, donde el estudiante diseña una solución completa de extremo a extremo.
