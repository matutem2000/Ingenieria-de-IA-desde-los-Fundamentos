# Módulo 4 – Capítulo 09 – Sección 05

## Indicadores de Madurez y Evaluación Continua

El gobierno de IA no tiene un estado final de "completo": es un proceso de mejora continua donde la organización incrementa progresivamente su capacidad para gestionar sistemas de IA con confianza, consistencia y responsabilidad. Los indicadores de madurez son el sistema de medición que permite a la organización saber dónde se encuentra en ese proceso de madurez y qué debe mejorar para avanzar al siguiente nivel. Sin ellos, el gobierno de IA es una aspiración sin método de verificación.

Los modelos de madurez de IA más referenciados en la industria — como el AI Maturity Model de NIST, el Gartner AI Maturity Model, o el modelo específico de la consultora McKinsey — comparten una estructura común de niveles: desde la ausencia de gobierno formal (Nivel 0) hasta la IA como capacidad estratégica organizacional con mejora continua demostrable (Nivel 4 o 5). Las dimensiones que estos modelos evalúan incluyen:

**Dimensión de estrategia y liderazgo:** ¿existe una estrategia de IA aprobada por la dirección? ¿hay un rol dedicado de responsabilidad sobre la IA (Chief AI Officer, AI Governance Lead)? ¿los objetivos de los sistemas de IA están alineados con los objetivos estratégicos del negocio?

**Dimensión de datos y conocimiento:** ¿existen políticas de calidad de datos para los sistemas de IA? ¿la base de conocimiento de los sistemas RAG tiene procesos de actualización y curación? ¿los datos de entrenamiento y evaluación están documentados y versionados?

**Dimensión de procesos y operaciones:** ¿existe un proceso estándar de despliegue de sistemas de IA? ¿los procesos de monitoreo, alerta y respuesta ante incidentes están documentados y probados? ¿el proceso de actualización de modelos y prompts sigue un procedimiento definido?

**Dimensión de cumplimiento y riesgo:** ¿todos los sistemas de IA en producción tienen un análisis de riesgo documentado? ¿existe un registro de sistemas de IA con su clasificación de riesgo? ¿la organización puede demostrar cumplimiento con el EU AI Act para sus sistemas de alto riesgo?

**Dimensión de cultura y capacidades:** ¿los equipos que construyen sistemas de IA tienen formación en gobierno de IA y en mejores prácticas de evaluación? ¿existe una comunidad de práctica interna que comparte aprendizajes entre proyectos?

**La evaluación continua como práctica de gobierno** merece un tratamiento específico porque es el mecanismo técnico que da sustento a varias de las dimensiones anteriores. La evaluación continua institucionaliza la medición periódica de la calidad de los sistemas de IA en producción como proceso de gobierno, no solo como actividad técnica de operación.

Los componentes de la evaluación continua como práctica de gobierno incluyen:

- **Datasets de evaluación curados por el equipo:** conjuntos de consultas con respuestas esperadas, representativos del uso real del sistema, mantenidos y actualizados regularmente. La curaduría de estos datasets requiere participación de expertos del dominio, no solo del equipo técnico.
- **Métricas de evaluación acordadas entre stakeholders:** las métricas RAGAS, LLM-as-judge, y otras métricas automatizadas deben complementarse con criterios de calidad definidos junto con los usuarios del sistema. Un sistema puede tener alta faithfulness (sus respuestas están fundamentadas en el contexto) pero baja utilidad práctica (las respuestas no responden a lo que el usuario realmente necesita).
- **Cadencia de evaluación:** frecuencia con que se ejecutan las evaluaciones y se revisan los resultados. Los sistemas críticos deben evaluarse semanalmente; los sistemas de menor impacto pueden evaluarse mensualmente.
- **Proceso de acción sobre resultados:** qué ocurre cuando los resultados de evaluación muestran degradación. El proceso debe estar documentado: quién es notificado, en qué plazo se espera una acción, y qué constituye una degradación que requiere acción inmediata versus una degradación que puede incluirse en el roadmap de mejora.
- **Testing de safety y guardrails:** evaluación periódica de los controles de seguridad del sistema. Red-teaming estructurado — intentos controlados de explotar vulnerabilidades de prompt injection, jailbreak, y filtración de datos — debe realizarse regularmente, especialmente antes de cambios significativos del sistema.

La práctica de evaluación continua cierra el ciclo de mejora del sistema de IA: el monitoreo operativo detecta síntomas, la evaluación continua diagnostica causas, los procesos de gobierno determinan prioridades de acción, y el desarrollo implementa mejoras. Sin evaluación continua, el sistema evoluciona a ciegas; con ella, la organización puede afirmar con datos que sus sistemas de IA mantienen y mejoran su calidad a lo largo del tiempo.

Los indicadores de madurez deben revisarse anualmente y compararse con los objetivos de madurez de la organización para el siguiente período. Esta revisión es el input para el roadmap de capacidades de gobierno de IA — el plan de mejora del propio gobierno — que cierra el ciclo de la gestión estratégica de la IA como capacidad organizacional.
