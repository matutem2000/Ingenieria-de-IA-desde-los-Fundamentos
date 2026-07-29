# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 13: Resumen del capítulo

Este capítulo cerró el ciclo técnico del módulo de Context Engineering. Los capítulos anteriores construyeron los componentes de los sistemas de IA: el contexto, la memoria, el RAG, las herramientas, los agentes, la observabilidad. Este capítulo completó ese cuadro con la pregunta que los capítulos técnicos no responden: ¿cómo garantizar que esos sistemas funcionan de manera segura, dentro de los límites autorizados y de acuerdo con las obligaciones de la organización?

A continuación, los conceptos centrales de cada sección.

---

### Fundamentos de seguridad en Context Engineering (secciones 01 a 03)

**La seguridad del contexto es un problema propio.** Los sistemas de IA no tienen una separación rígida entre instrucciones y datos; el modelo procesa ambos como texto unificado. Esta propiedad crea una superficie de ataque que no existe en el software tradicional y que requiere controles específicos.

**Las tres capas de la seguridad en CE** son la seguridad técnica del contexto, la gobernanza organizacional y el compliance. Las tres son necesarias y se refuerzan mutuamente.

**La superficie de ataque del Context Engineering** abarca: prompt injection (directo e indirecto), extracción del system prompt, jailbreaking, extracción de datos a través del contexto, uso excesivo de herramientas, ataques a la cadena de suministro del contexto y degradación adversarial.

**El prompt injection** es la amenaza más característica. El prompt injection directo proviene del usuario; el indirecto, de documentos maliciosos que el sistema RAG recupera e incluye en el contexto. Los controles clave incluyen: separación estructural de instrucciones y datos en el system prompt, validación de entradas, inspección del contexto recuperado, y principio del mínimo privilegio en herramientas.

---

### Controles técnicos y organizacionales (secciones 04 a 06)

**La gobernanza del system prompt** requiere tratarlo como un activo crítico: control de versiones, proceso de aprobación para cambios en producción, entornos de staging separados, registro de despliegues.

**La gobernanza de datos** establece qué puede entrar al contexto: el catálogo de fuentes autorizadas, los niveles de clasificación, el principio de minimización de datos y el proceso de aprobación para nuevas fuentes.

**Privacidad por diseño** aplicada al contexto: incluir solo los datos que el modelo necesita para la tarea, aplicar anonimización o pseudonimización cuando sea posible, definir políticas de retención explícitas para cada tipo de dato. El flujo de decisión "¿este dato debe estar en el contexto?" es la herramienta práctica central.

**La gestión de identidades** en CE abarca tres tipos de identidad (usuario final, sistema, componentes), la propagación de identidad del usuario a los componentes del backend, el RBAC para roles de usuario y los permisos de herramientas como el punto más crítico del control de acceso.

**El sandboxing de herramientas** aísla la ejecución de herramientas para limitar el daño que un agente comprometido puede causar. Las herramientas de ejecución de código corren en contenedores aislados. Las herramientas de impacto alto requieren confirmación antes de ejecutarse.

---

### Compliance y arquitectura (secciones 07 y 08)

**El entorno regulatorio de IA** incluye el AI Act europeo (con su clasificación de riesgo: inaceptable, alto, limitado, mínimo), los marcos norteamericanos del NIST y regulaciones sectoriales existentes. Los principios de diseño orientados a compliance —trazabilidad, supervisión humana, documentación, transparencia— se mantienen válidos independientemente de la regulación específica.

**La auditoría del contexto** es la extensión de la observabilidad hacia los requisitos de compliance: registros de inferencias, cambios de configuración, accesos a datos sensibles, incidentes y decisiones de alto impacto, con formatos auditables, integridad garantizada y retención alineada a los requisitos legales.

**Los principios de arquitectura segura** son cinco: secure by default (la configuración predeterminada es la más segura), defense in depth (múltiples capas de control), fail closed (los fallos técnicos producen denegación, no acceso), aislamiento de tenants y superficie de ataque mínima.

---

### Síntesis práctica (secciones 09 a 12)

**Los patrones de seguridad** validados son: aislamiento de contexto por usuario, separación estructural de instrucciones y datos, validación de doble capa, confirmación antes de acción de alto impacto y degradación controlada ante errores de seguridad.

**Los anti-patrones** más frecuentes son: confiar en todo el contenido del contexto por igual, usar el secreto del system prompt como mecanismo de seguridad, otorgar permisos de herramientas por conveniencia, carecer de aislamiento entre sesiones de usuario, omitir el logging por "proteger la privacidad" y incluir información de infraestructura en el system prompt.

**El caso de estudio** (auditoría del asistente financiero) ilustró cuatro problemas típicos de sistemas construidos sin seguridad por diseño: sistema RAG sin filtros de acceso, system prompt con información de infraestructura, herramientas sin límite de alcance y memoria sin aislamiento de sesión.

**El threat modeling** es la práctica de seguridad proactiva que el AI Engineer debe aplicar antes del despliegue: identificar activos, catalogar amenazas usando el marco STRIDE, evaluar el riesgo de cada amenaza, diseñar controles específicos y verificarlos con casos de prueba.

---

### La conexión con el módulo

Este capítulo demostró que la seguridad no es una capa independiente añadida encima del sistema, sino una propiedad que atraviesa todas las decisiones de diseño del Context Engineering:

- El diseño del **system prompt** afecta la resistencia al prompt injection y la superficie de ataque de extracción de información.
- La arquitectura del **sistema RAG** determina si se pueden aplicar filtros de acceso por usuario y si los documentos recuperados pueden contener instrucciones maliciosas.
- El diseño de la **memoria del agente** determina si la información de un usuario puede filtrarse a las sesiones de otro.
- El alcance de las **herramientas** determina el daño máximo que puede causar un agente comprometido.
- La **observabilidad** del capítulo anterior es la base de la auditoría y la detección de incidentes.

El AI Engineer que comprende esas conexiones construye sistemas donde la seguridad es consecuencia del diseño, no un parche posterior.

La siguiente sección propone ejercicios de autoevaluación para consolidar los conceptos de este capítulo.
