# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 14: Autoevaluación

Las siguientes preguntas permiten verificar la comprensión de los conceptos centrales de este capítulo. Las primeras ocho son preguntas de comprensión conceptual; las dos últimas son ejercicios de análisis aplicado.

---

**Pregunta 1**

¿Cuál es la diferencia fundamental entre el prompt injection directo y el prompt injection indirecto? ¿Por qué el segundo es considerado más peligroso para sistemas de producción?

*Respuesta esperada:* El prompt injection directo ocurre cuando el atacante es el usuario del sistema y coloca instrucciones maliciosas en su mensaje. El indirecto ocurre cuando el atacante modifica una fuente de datos externa (un documento en el corpus RAG, el resultado de una API, etc.) y esas instrucciones llegan al modelo a través del pipeline de recuperación, sin que el atacante necesite interactuar directamente con el sistema. El indirecto es más peligroso porque el atacante no necesita acceso al sistema de IA; solo necesita acceso a cualquier fuente que el sistema indexe. El ataque puede estar latente en el corpus durante tiempo indefinido, activándose solo cuando una consulta relevante lo recupera, y puede estar oculto en documentos largos donde la inspección manual es impráctica.

---

**Pregunta 2**

¿Por qué no es correcto usar el secreto del system prompt como mecanismo de seguridad? ¿Qué tipo de controles deben implementarse en su lugar?

*Respuesta esperada:* El secreto del system prompt es un mecanismo frágil porque el system prompt puede ser extraído mediante técnicas de elicitación o prompt injection. Un sistema cuya seguridad depende de que el atacante no conozca el system prompt no es un sistema seguro; es uno que aún no ha sido atacado con suficiente sofisticación. Los controles reales deben estar en la infraestructura: filtros de entrada y salida, permisos mínimos de herramientas, aislamiento de datos por usuario, validación de entradas. El system prompt puede incluir instrucciones de resistencia a la manipulación, pero esas instrucciones son una capa adicional, no la única línea de defensa.

---

**Pregunta 3**

Describe el principio de "fail closed" aplicado a un sistema de Context Engineering. Da un ejemplo concreto de una situación donde aplicarlo puede crear fricción operativa y explica por qué es preferible aceptar esa fricción.

*Respuesta esperada:* "Fail closed" significa que cuando un componente del sistema falla, la operación es denegada en lugar de procesada sin ese control. Ejemplo: si el clasificador de inyección de entradas falla por un error técnico (timeout de la API, error de red), el mensaje del usuario es rechazado y el sistema devuelve un error, en lugar de procesar el mensaje sin inspección. La fricción operativa es que los usuarios reciben errores cuando el clasificador tiene problemas de disponibilidad, lo que puede parecer innecesariamente restrictivo. Es preferible aceptar esa fricción porque el resultado contrario —procesar mensajes sin inspección cuando el control falla— convierte cada falla técnica del componente de seguridad en una ventana de vulnerabilidad explotable deliberadamente.

---

**Pregunta 4**

¿Cuáles son las tres diferencias entre un log de observabilidad (para diagnóstico operativo) y un log de auditoría (para compliance)? ¿Por qué no basta con usar el mismo registro para ambos fines?

*Respuesta esperada:* Las diferencias principales son: (1) Formato: los logs de observabilidad pueden ser registros técnicos en formatos internos; los de auditoría deben estar en formatos accesibles para auditores externos. (2) Integridad: los logs de auditoría deben estar protegidos contra modificación (firma digital, sistema de inmutabilidad); los de observabilidad pueden no requerir ese nivel de protección. (3) Retención: los logs de observabilidad tienen retención de 30 a 90 días típicamente; los de auditoría pueden requerir retención de 5 a 7 años en sectores regulados. No basta con el mismo registro porque los requisitos son diferentes: el log de observabilidad puede contener datos en bruto convenientes para diagnóstico pero inapropiados para retención larga; el log de auditoría necesita estar anonimizado donde corresponda, protegido y en un formato que los auditores puedan consumir.

---

**Pregunta 5**

¿Qué es el principio de minimización de datos aplicado al contexto? Da tres ejemplos concretos de cómo se aplica en el diseño de un sistema de Context Engineering.

*Respuesta esperada:* La minimización de datos significa incluir en el contexto solo la información que el modelo necesita para completar la tarea, no toda la información disponible. Ejemplos: (1) En un asistente de soporte al cliente, incluir el resumen del problema del cliente en lugar del historial completo de todas sus transacciones; el modelo necesita entender el problema, no todo el historial. (2) En un sistema RAG que indexa documentos de distintos departamentos, no recuperar documentos de Recursos Humanos en respuesta a una consulta sobre precios de productos; recuperar solo los documentos relevantes para la tarea. (3) En el contexto del usuario, usar el nombre del usuario cuando sea necesario para la interacción, pero no incluir su dirección, fecha de nacimiento u otros datos personales que la tarea no requiere.

---

**Pregunta 6**

Explica la diferencia entre "aislamiento de contexto por usuario" y "aislamiento de tenants". ¿En qué tipo de sistema se aplica cada uno?

*Respuesta esperada:* El aislamiento de contexto por usuario aplica dentro de un mismo sistema donde múltiples usuarios interactúan simultáneamente: garantiza que el contexto construido para el usuario A no contiene datos del usuario B. Se aplica en cualquier sistema con múltiples usuarios, incluso si todos pertenecen a la misma organización. El aislamiento de tenants aplica en sistemas SaaS o multiorganización: garantiza que los datos, configuración y contexto de la organización A no son accesibles para la organización B. Va más allá del usuario individual: incluye índices vectoriales en namespaces separados, modelos ajustados separados si los hubiera y logs completamente separados. El aislamiento de tenants incluye el de usuario (los usuarios de un tenant están aislados entre sí y de los de otros tenants), pero no a la inversa.

---

**Pregunta 7**

¿Cuál es la relación entre la gobernanza del system prompt y la seguridad del sistema? ¿Qué puede salir mal si el system prompt no tiene control de versiones ni proceso de aprobación?

*Respuesta esperada:* El system prompt define el comportamiento, los límites y las restricciones del sistema. Un cambio no revisado puede introducir vulnerabilidades (añadir información técnica innecesaria, eliminar instrucciones de resistencia a la manipulación), alterar el comportamiento del sistema de maneras no previstas o violar políticas de negocio. Sin control de versiones, el equipo no sabe cuál es la versión actual del system prompt en producción, no puede identificar qué cambio causó un comportamiento anómalo y no puede revertir a una versión anterior si un cambio produce problemas. Sin proceso de aprobación, cualquier persona con acceso puede modificar el sistema en producción, lo que convierte la gobernanza en nominal.

---

**Pregunta 8**

¿Qué tipos de sistemas de IA clasifica el AI Act europeo como "de alto riesgo" y qué requisitos impone para ellos? ¿Cuál de esos requisitos tiene el impacto más directo en el diseño del Context Engineering?

*Respuesta esperada:* El AI Act clasifica como de alto riesgo sistemas que toman o apoyan decisiones en dominios críticos: salud, educación, empleo, justicia, infraestructuras críticas, biometría, migración. Los requisitos para sistemas de alto riesgo incluyen: documentación técnica exhaustiva, sistemas de gestión de riesgos, registro de actividad (logging), supervisión humana y, en algunos casos, certificación por terceros. El requisito con impacto más directo en el diseño del Context Engineering es el registro de actividad (logging de auditoría): el sistema debe poder registrar qué información recibió el modelo, qué decisión tomó y por qué, para cualquier solicitud dentro del período de retención. Esto requiere diseñar la trazabilidad del contexto desde el inicio, no añadirla retroactivamente.

---

**Ejercicio 9 (análisis aplicado)**

Un equipo está construyendo un asistente de recursos humanos que ayuda a los managers a redactar evaluaciones de desempeño. El sistema tiene acceso al historial de evaluaciones anteriores de cada empleado (en el sistema RAG), puede consultar las políticas de RRHH y puede sugerir textos basados en los comentarios que el manager proporciona. El asistente está disponible para todos los managers de la empresa.

Identifica tres riesgos de seguridad o privacidad específicos de este sistema y propón un control para cada uno.

*Respuesta esperada (posibles respuestas):*

**Riesgo 1 — Acceso cruzado a evaluaciones:** un manager puede construir una consulta que recupere evaluaciones de empleados que no son de su equipo. El sistema RAG puede recuperar esos documentos si el índice no aplica filtros por relación manager-empleado.
Control: el índice RAG filtra los documentos de evaluaciones por el equipo directo del manager autenticado. Los registros de evaluaciones tienen metadatos de manager asignado como filtro obligatorio.

**Riesgo 2 — PII de empleados en logs:** el sistema registra el texto de los comentarios que el manager ingresa para generar las sugerencias. Esos textos pueden contener información personal sensible sobre empleados (datos de salud, situación familiar).
Control: los logs de las conversaciones se anonimzan antes del almacenamiento, reemplazando nombres y datos de identificación por tokens. La política de retención de esos logs es de máximo 90 días, dado que no se usan para auditoría de decisiones sino para diagnóstico técnico.

**Riesgo 3 — El asistente como herramienta de sesgo institucional:** si las evaluaciones históricas en el RAG contienen sesgos (evaluaciones más positivas para ciertos perfiles demográficos), el asistente puede replicar y amplificar esos sesgos en sus sugerencias.
Control: los textos generados se marcan explícitamente como sugerencias, no como textos finales. Se implementa un aviso al manager recordando que es responsable del contenido final. Se registran las sugerencias y las versiones finales publicadas para un análisis periódico de sesgo (comparando los textos sugeridos vs. los aprobados por categorías demográficas).

---

**Ejercicio 10 (análisis aplicado)**

¿En qué casos específicos sería justificable no implementar el principio de "fail closed" en un sistema de Context Engineering? ¿Qué alternativas de diseño existen para esas situaciones?

*Respuesta esperada:* El "fail closed" puede no ser apropiado cuando la disponibilidad del sistema es tan crítica que una interrupción causa daños comparables o mayores al riesgo de seguridad que se mitiga. Por ejemplo, un sistema de soporte médico de urgencias donde interrumpir el servicio durante una falla de un componente de seguridad puede retrasar la atención a pacientes. En esos casos, las alternativas son: (1) Modo degradado seguro: si el clasificador de inyección falla, el sistema opera solo con las herramientas de menor impacto (lectura de información pública), no con todas las herramientas habilitadas. (2) Redundancia del componente de seguridad: el clasificador de inyección tiene instancias redundantes, de manera que la falla de una no interrumpe el servicio. (3) Aumento del logging compensatorio: si el sistema opera temporalmente sin un control de seguridad, incrementa el nivel de logging para tener mayor visibilidad del tráfico durante ese período. La decisión de cuándo no aplicar "fail closed" debe ser explícita, documentada y revisada por el área de seguridad.

---

La última sección del capítulo establece la transición hacia el proyecto integrador del módulo.
