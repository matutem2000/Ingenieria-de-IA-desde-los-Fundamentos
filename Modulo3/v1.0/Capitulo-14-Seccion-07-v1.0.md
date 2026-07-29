# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 07: Cumplimiento normativo y auditoría

El compliance en sistemas de IA es un campo en construcción activa. Las regulaciones de IA están siendo desarrolladas, revisadas y actualizadas en múltiples jurisdicciones simultáneamente. Lo que es cierto en 2026 puede estar parcialmente desactualizado en 2028. Esta sección no pretende ser un manual legal: para eso existen los equipos jurídicos y los consultores especializados. Lo que desarrolla son los principios de diseño orientados a compliance —principios que se mantienen válidos independientemente de cuál sea la regulación específica aplicable— y las características de los sistemas de IA que hacen posible cumplir y demostrar el cumplimiento.

### El entorno regulatorio en 2026

La Unión Europea lidera la regulación formal de IA con el **AI Act** (Reglamento europeo de inteligencia artificial), que entró en vigor en 2024 y cuya aplicación plena avanza por etapas hasta 2026 y más allá. El AI Act establece un enfoque basado en riesgo: clasifica los sistemas de IA en niveles (inaceptable, alto, limitado, mínimo) y establece requisitos proporcionales al nivel de riesgo.

Para el AI Engineer que diseña sistemas de Context Engineering empresariales, las categorías más relevantes del AI Act son:

**Sistemas de alto riesgo:** sistemas que toman o apoyan decisiones en dominios críticos como salud, educación, empleo, justicia, infraestructuras críticas, biometría. Los sistemas de alto riesgo requieren documentación técnica exhaustiva, sistemas de gestión de riesgos, registro de actividad (logging), supervisión humana y, en algunos casos, certificación por terceros.

**Sistemas de riesgo limitado:** sistemas que interactúan con personas pero no toman decisiones de alto impacto. Requieren principalmente transparencia: el usuario debe saber que está interactuando con un sistema de IA (obligación de identificación).

**Sistemas de riesgo mínimo:** la mayoría de los asistentes de productividad, chatbots de atención al cliente y sistemas de recomendación sin impacto en decisiones críticas. Sin requisitos específicos, pero sujetos al marco general de protección de datos.

En Estados Unidos, la regulación de IA es más fragmentada: una combinación de directrices ejecutivas (el Executive Order on Safe, Secure and Trustworthy AI de 2023), marcos voluntarios (el AI Risk Management Framework del NIST) y regulaciones sectoriales existentes (HIPAA para salud, SOX para servicios financieros, FERPA para educación).

En Latinoamérica, varios países avanzan en marcos regulatorios propios, frecuentemente inspirados en el AI Act europeo o en los marcos del NIST.

### Principios de diseño orientados a compliance

Independientemente de cuál sea la regulación aplicable, los sistemas de IA que cumplen los siguientes principios de diseño están bien posicionados para satisfacer la mayoría de los requerimientos regulatorios existentes y emergentes:

**1. Trazabilidad completa.** El sistema puede reconstruir exactamente qué información recibió el modelo, qué decisión tomó y por qué, para cualquier solicitud histórica dentro del período de retención. Este principio es directamente requerido por el AI Act para sistemas de alto riesgo ("registro de actividad") y por marcos de auditoría en prácticamente todos los sectores.

**2. Supervisión humana por diseño.** El sistema está diseñado para que un ser humano pueda intervenir, corregir o anular sus decisiones. En el Context Engineering, esto se implementa mediante: puntos de aprobación humana en flujos de decisión de alto impacto, dashboards de monitoreo que permiten a operadores detectar anomalías, mecanismos de escalación cuando el sistema encuentra casos fuera de sus parámetros.

**3. Documentación técnica actualizada.** Existe documentación actualizada que describe el propósito del sistema, el modelo utilizado, los datos de entrenamiento (si aplica), las capacidades y limitaciones conocidas, las medidas de seguridad implementadas y los resultados de evaluaciones de riesgo. Esta documentación debe actualizarse cuando el sistema cambia significativamente.

**4. Evaluación de riesgos previa al despliegue.** Antes de desplegar el sistema o una actualización significativa, se realiza una evaluación de los riesgos potenciales: qué puede salir mal, qué tipos de usuarios puede afectar y cómo, cuál es el impacto máximo de una falla. Esta evaluación no elimina los riesgos, pero documenta que fueron considerados.

**5. Mecanismos de reporte y corrección.** Los usuarios afectados por errores del sistema tienen un canal para reportarlos. El equipo tiene un proceso para recibir ese reporte, investigarlo y corregir el sistema si es necesario. Esto aplica tanto a errores técnicos como a outputs que son injustos, incorrectos o dañinos.

### Auditoría: el registro que hace el compliance demostrable

La conformidad con una regulación no se declara: se demuestra. Y demostrarlo requiere registros. El sistema de IA que no tiene registros adecuados puede cumplir con todos los principios de privacidad, seguridad y gobernanza —y aun así no poder demostrarlo ante un auditor.

Los registros necesarios para la auditoría de un sistema de Context Engineering en sectores regulados incluyen:

**Registro de inferencias:** para cada solicitud procesada, el log debe incluir: timestamp, identificador de sesión (anonimizado si es necesario), versión del system prompt activa, herramientas ejecutadas, tiempo de respuesta, tokens utilizados. No necesariamente el contenido completo de la conversación, pero sí los metadatos suficientes para reconstruir qué ocurrió.

**Registro de cambios de configuración:** cada modificación al system prompt, cada cambio en las herramientas habilitadas, cada actualización del índice RAG queda registrada con: qué cambió, quién lo aprobó, cuándo se desplegó y por qué se realizó el cambio.

**Registro de accesos a datos sensibles:** cuando el sistema accede a datos de usuarios, documentos confidenciales o sistemas críticos, el acceso queda registrado con el identificador del usuario que originó la solicitud y el dato que fue accedido.

**Registro de incidentes:** los eventos de seguridad detectados —intentos de prompt injection, accesos no autorizados detectados, comportamientos anómalos del modelo— se registran con la información necesaria para investigarlos.

**Registro de decisiones de alto impacto:** en sistemas que apoyan decisiones sobre personas (aprobación de crédito, selección de candidatos, priorización médica), cada decisión del sistema queda registrada junto con la información en la que se basó, para poder explicarla y revertirla si es necesario.

### La auditoría del contexto como extensión de la observabilidad

El capítulo anterior construyó la capacidad de observar el sistema en producción. La auditoría del contexto es la extensión de esa observabilidad hacia los requerimientos de compliance: no solo registrar qué ocurrió para detectar problemas operativos, sino registrar qué ocurrió de manera que pueda ser inspeccionado por auditores externos.

La diferencia práctica está en el formato y la retención de los registros:

- Los logs de observabilidad pueden ser registros técnicos en formatos internos, con retención de 30 a 90 días.
- Los logs de auditoría deben estar en formatos accesibles, firmados digitalmente para garantizar su integridad, con retención alineada al período legal aplicable (frecuentemente de 5 a 7 años en sectores regulados).

### Transparencia con el usuario final

La mayoría de las regulaciones emergentes incluyen un requisito de transparencia hacia el usuario: el usuario que interactúa con un sistema de IA debe saber que está interactuando con un sistema de IA, qué puede hacer y qué limitaciones tiene, cómo puede reportar problemas.

Para el AI Engineer, este requisito se traduce en:

- El sistema se identifica como un asistente basado en IA, no como un agente humano.
- La interfaz incluye información accesible sobre las capacidades y limitaciones del sistema.
- Existe un mecanismo para que el usuario reporte respuestas incorrectas o problemáticas.
- El sistema no afirma ser humano cuando el usuario pregunta directamente.

Este último punto es especialmente relevante para sistemas de atención al cliente que imitan el estilo conversacional humano: la fluidez del sistema no justifica la ambigüedad sobre su naturaleza.

### Nota del arquitecto

La regulación de IA es un campo en evolución rápida. Lo que el AI Engineer puede hacer hoy es construir sistemas con las propiedades que hacen posible el compliance: trazabilidad, supervisión humana, documentación y transparencia. Un sistema construido con esos principios puede adaptarse a nuevos requisitos regulatorios sin rediseño desde cero. Un sistema construido sin esos principios puede cumplir con las regulaciones actuales y ser imposible de adaptar a las futuras.

La siguiente sección integra todos los principios de seguridad, privacidad y compliance en un conjunto de patrones de arquitectura para sistemas de IA empresariales seguros.
