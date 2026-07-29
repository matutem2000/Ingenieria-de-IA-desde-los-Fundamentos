# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 13 — Resumen del capítulo

Este capítulo construyó el marco completo para diseñar, implementar y operar sistemas de IA con herramientas. A continuación se sintetizan los conceptos centrales de cada sección.

---

**Las herramientas como mecanismo de integración** (sección 01)

Una herramienta es cualquier función, API o servicio externo que el modelo puede invocar durante una interacción para obtener información dinámica o ejecutar una acción. El modelo razona y genera solicitudes de invocación estructuradas; la aplicación ejecuta las herramientas y devuelve los resultados al contexto. El ciclo fundamental — solicitud → razonamiento → invocación → resultado → respuesta — puede iterarse varias veces dentro de una sola interacción. Las herramientas se clasifican en herramientas de consulta (idempotentes, sin efectos) y herramientas de acción (con efectos secundarios, potencialmente irreversibles).

---

**Model Context Protocol** (sección 02)

MCP es un protocolo abierto que define un estándar para que los modelos descubran y usen herramientas a través de servidores especializados. Resuelve el problema de la fragmentación de integraciones cuando múltiples aplicaciones necesitan las mismas herramientas: la lógica de cada herramienta vive en el servidor correspondiente, no en cada aplicación. MCP define tres componentes — cliente, servidor y protocolo — y tres capacidades — herramientas, recursos y prompts. Justifica su complejidad cuando el ecosistema lo requiere; no es necesario para sistemas simples con pocas herramientas en una sola aplicación.

---

**Mecanismo de invocación: Function Calling y Tool Calling** (sección 03)

El mecanismo de invocación — llamado function calling, tool use o tool calling según el proveedor — sigue la misma estructura conceptual: el desarrollador define herramientas en JSON Schema, el modelo genera solicitudes de invocación estructuradas, la aplicación las ejecuta y devuelve los resultados. Las diferencias entre proveedores son de formato, no de lógica. La descripción de una herramienta es su instrucción operativa para el modelo: ambigüedades en la descripción producen invocaciones incorrectas. El modo de control de invocación (automático, forzado, herramienta específica) permite al desarrollador ajustar el comportamiento del modelo.

---

**Arquitectura de integración** (sección 04)

El loop de ejecución es el componente central de cualquier sistema con herramientas: itera entre el modelo y las herramientas hasta que el modelo produce una respuesta final. Los patrones de arquitectura van desde la integración directa (todas las herramientas en la aplicación) hasta la capa de herramientas compartida y los microservicios de herramientas. Toda arquitectura de producción debe incluir registro completo de cada invocación para diagnóstico y auditoría. El crecimiento del contexto por acumulación de resultados de herramientas debe gestionarse activamente.

---

**Diseño de herramientas robustas** (sección 05)

Los siete principios del diseño de herramientas robustas son: una herramienta, una responsabilidad; descripciones operativas no documentales; esquemas de parámetros precisos; contratos de respuesta predecibles; errores informativos y accionables para el modelo; idempotencia en herramientas de acción; y timeouts y límites de tamaño de respuesta. El texto de la descripción es parte del contrato técnico del sistema. Los errores deben diseñarse para que el modelo pueda razonar sobre ellos, sin exponer detalles del stack técnico.

---

**Orquestación y selección de herramientas** (sección 06)

El modelo selecciona herramientas basándose exclusivamente en sus descripciones. Las descripciones solapadas producen selección incorrecta. La secuenciación ocurre cuando el resultado de una herramienta determina la siguiente invocación; el modelo gestiona esta lógica de forma natural. Las invocaciones paralelas reducen la latencia cuando las herramientas son independientes entre sí. El anti-patrón de sobre-selección — el modelo invoca más herramientas de las necesarias — se combate con descripciones precisas, herramientas de enrutamiento e instrucciones en el system prompt. El loop debe tener un límite máximo de iteraciones.

---

**Seguridad y control de ejecución** (sección 07)

El principio del mínimo privilegio aplicado a herramientas significa que el modelo solo recibe las herramientas que el usuario está autorizado a usar, y esas herramientas solo tienen los permisos mínimos necesarios. Las herramientas de acción irreversible requieren confirmación explícita del usuario antes de ejecutarse. El prompt injection indirecto — instrucciones ocultas en datos externos que el modelo procesa — se mitiga con instrucciones en el system prompt, sanitización de resultados y confirmación humana para acciones de alto impacto. La auditoría completa de cada invocación es tanto un recurso operativo como un requisito de cumplimiento en industrias reguladas.

---

**Integración con sistemas empresariales** (sección 08)

Los sistemas empresariales más frecuentes — CRM, ERP, bases de datos internas, sistemas de tickets, plataformas de comunicación, calendarios — tienen patrones de integración distintos. Las herramientas deben abstraer la complejidad técnica de la API subyacente y exponer operaciones con semántica de negocio. Los sistemas legados pueden integrarse a través de una capa de adaptación o, en el peor caso, mediante RPA. La latencia de herramientas que acceden a sistemas externos impone restricciones de diseño que deben gestionarse con caché, invocación paralela y degradación elegante.

---

**Patrones y anti-patrones** (sección 09)

Los patrones más útiles son: herramienta de enrutamiento (para sistemas con muchas herramientas), verificación antes de acción (para operaciones irreversibles), herramienta como esquema de salida estructurada, y caché semántica de resultados frecuentes. Los anti-patrones más peligrosos son: la herramienta omnipotente que ejecuta código o SQL arbitrario, las descripciones duplicadas que producen selección ambigua, ignorar los errores de herramientas, los efectos secundarios ocultos, exponer el stack técnico en los errores, y devolver respuestas de tamaño ilimitado.

---

**Caso de estudio** (sección 10) y **Laboratorio práctico** (sección 11)

El caso de estudio mostró la implementación de un asistente de atención al cliente con seis herramientas que integran un OMS, un CRM y un sistema de tickets. Las lecciones más importantes: la confirmación antes de cancelar es esencial, las descripciones requieren iteración para eliminar solapamientos, y los logs de ejecución son el principal recurso de diagnóstico.

El laboratorio permitió implementar dos herramientas — una de consulta y una de acción — integradas en un loop de ejecución funcional, con manejo de errores deliberados y observación directa del comportamiento del modelo.

---

### Los conceptos clave del capítulo

- **El modelo razona, la aplicación actúa.** El modelo genera solicitudes de invocación; la aplicación las ejecuta.
- **La descripción es el contrato operativo.** El modelo toma decisiones de invocación basado en el texto de la descripción.
- **Consulta versus acción determina el nivel de control.** Las herramientas de acción requieren controles de seguridad más estrictos que las de consulta.
- **Los errores deben diseñarse para el modelo.** Un error informativo permite al modelo razonar; un stack trace no.
- **El mínimo privilegio aplica a herramientas.** El modelo solo debe ver las herramientas que el usuario puede usar.
- **La confirmación humana es la defensa definitiva.** Para acciones irreversibles, no hay sustituto para la confirmación explícita del usuario.
