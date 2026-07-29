# Capítulo 12 — Context Engineering Empresarial

## Sección 03: Arquitecturas empresariales basadas en contexto

Una arquitectura empresarial de IA no es un sistema monolítico; es una infraestructura de contexto que permite a múltiples equipos construir aplicaciones de IA sin duplicar el trabajo de base. La distinción importa porque define el problema de diseño correcto. El AI Engineer que diseña arquitecturas empresariales no diseña una aplicación; diseña la plataforma sobre la que otros construirán aplicaciones.

Esta sección delimita el alcance arquitectónico que le corresponde a este capítulo. Las decisiones de infraestructura profunda —cómo desplegar un clúster de bases vectoriales, cómo configurar un pipeline de LLMOps, cómo implementar un sistema de monitoreo de modelos— son responsabilidad del capítulo de operaciones del Módulo 4. Lo que este capítulo examina es la capa intermedia: cómo estructurar el contexto en una organización para que sea compartido, gobernable y escalable.

### El problema de escala que define la arquitectura

Una única aplicación de IA necesita un sistema de recuperación, una base de conocimiento y un conjunto de instrucciones del sistema. Cuando una organización tiene diez aplicaciones de IA, necesita decidir qué comparte entre ellas y qué es específico de cada una.

Esta decisión no es evidente. Las opciones en los extremos son claramente incorrectas: indexar todo el conocimiento corporativo en una única base vectorial monolítica ignora las diferencias de dominio y de permisos de acceso; construir diez bases vectoriales independientes duplica el costo de mantenimiento y produce silos de información que pueden contradecirse entre sí. La arquitectura correcta está en el espacio intermedio: un modelo de capas que separa lo que es común de lo que es específico.

### El modelo de capas de contexto

Una arquitectura empresarial de contexto se organiza en tres capas superpuestas que reflejan los niveles de especificidad del conocimiento.

**Capa corporativa.** Contiene el conocimiento que debe ser consistente en todos los sistemas de IA de la organización: políticas aprobadas, valores institucionales, requisitos legales aplicables, glosario de términos, tono de comunicación oficial. Esta capa es administrada centralmente, con un proceso formal de aprobación para cualquier modificación. Todos los sistemas de IA de la organización acceden a esta capa, garantizando que ningún asistente contradiga la política corporativa oficial.

**Capa departamental.** Contiene el conocimiento específico de cada área de la organización: procedimientos del equipo de soporte, catálogo de productos del equipo comercial, guías de proceso del equipo de recursos humanos, repositorio de contratos del equipo legal. Cada departamento administra su propia capa con autonomía dentro de las políticas definidas en la capa corporativa. Un sistema de IA del equipo de soporte tiene acceso a la capa corporativa más la capa de soporte. Un sistema del equipo comercial tiene acceso a la capa corporativa más la capa comercial.

**Capa de aplicación.** Contiene el conocimiento específico de cada caso de uso individual: la historia de conversación de un caso de atención al cliente, los documentos relevantes para una sesión de análisis de contratos, el contexto del proyecto que el equipo de desarrollo está trabajando. Esta capa es efímera o de corta duración; se construye dinámicamente en cada interacción y no persiste como conocimiento organizacional.

```
ARQUITECTURA DE CAPAS DE CONTEXTO EMPRESARIAL

┌─────────────────────────────────────────────────────────┐
│  CAPA CORPORATIVA (universal, gestionada centralmente)  │
│  Políticas | Marco legal | Tono | Glosario              │
└─────────────────────────────────────────────────────────┘
         ↑                    ↑
┌──────────────────┐  ┌──────────────────────────────────┐
│  CAPA SOPORTE    │  │  CAPA COMERCIAL  │  CAPA LEGAL   │
│  (departamental) │  │  (departamental) │  (dept.)      │
└──────────────────┘  └──────────────────────────────────┘
         ↑                    ↑                  ↑
┌──────────────────┐  ┌───────────────┐  ┌──────────────┐
│ APP: Asistente   │  │ APP: Asistente│  │ APP: Buscador│
│ de soporte       │  │ de ventas     │  │ de contratos │
│ (aplicación)     │  │ (aplicación)  │  │ (aplicación) │
└──────────────────┘  └───────────────┘  └──────────────┘
```

### Componentes de la plataforma de contexto empresarial

Una plataforma de contexto empresarial tiene cinco componentes que se especializan según su función.

**El registro de instrucciones del sistema.** Una organización con múltiples sistemas de IA necesita un lugar centralizado donde se gestionan las instrucciones del sistema de producción. Este registro no es un simple repositorio de textos; es un sistema con control de versiones, historial de cambios, proceso de aprobación y mecanismo de despliegue. Cuando la política corporativa cambia, la actualización se hace en el registro, y todos los sistemas que dependen de esa instrucción la reciben de forma coordinada.

**La base de conocimiento corporativa.** La base vectorial de la capa corporativa, indexada con el conocimiento de alta autoridad y alta vigencia de la organización. Su actualización sigue un proceso formal —no cualquier empleado puede agregar documentos a esta capa— y está sujeta a revisiones periódicas de calidad y vigencia.

**Las bases de conocimiento departamentales.** Una base vectorial por departamento o dominio significativo, administrada por el equipo responsable de ese dominio. El equipo de soporte administra la base de conocimiento de productos y procedimientos de soporte; el equipo legal administra la base de contratos y jurisprudencia aplicable. La plataforma corporativa proporciona la infraestructura técnica; cada departamento proporciona el contenido y los procesos de mantenimiento.

**El sistema de control de acceso al contexto.** Mecanismo que determina, para cada solicitud al sistema de IA, qué capas de conocimiento son accesibles dado el rol del usuario solicitante. Un empleado de soporte accede a la capa corporativa y a la capa de soporte, pero no a la capa legal ni a los documentos de contratos de clientes. La implementación técnica puede variar —metadatos de permisos en los documentos indexados, filtros aplicados en la recuperación, validación antes de incluir fragmentos en el contexto— pero el principio es invariante: el sistema de IA hereda los controles de acceso de la organización, no los ignora.

**El bus de contexto.** En organizaciones con múltiples sistemas de IA interactuando entre sí —el asistente de ventas que consulta al sistema de inventario, el agente de soporte que escala al agente de gestión de casos—, el bus de contexto es el mecanismo que permite transmitir contexto relevante entre sistemas sin que cada sistema necesite acceder directamente a todas las fuentes. El contexto acumulado en una conversación de soporte puede enriquecerse con el historial de compras del cliente (proveniente del sistema de CRM) y con el estado actual de los tickets abiertos (proveniente del sistema de gestión de casos) sin que el asistente de soporte tenga que indexar directamente esas fuentes.

### Patrones de integración entre capas

La arquitectura de capas funciona solo si los mecanismos de integración entre capas están bien diseñados. Hay tres patrones que resuelven esta integración de formas diferentes.

**Contexto jerárquico estático.** Las instrucciones de las capas superiores se prependen al contexto de cada llamada, seguidas de las instrucciones de la capa inferior. Es el patrón más simple: la capa corporativa siempre está presente, la capa departamental se agrega según el sistema, la capa de aplicación se construye dinámicamente. Su limitación es el costo en tokens: si la capa corporativa es extensa, consume una porción significativa de la ventana de contexto en cada llamada.

**Contexto jerárquico recuperado.** En lugar de prepender todo el contenido de las capas superiores, el sistema recupera solo los fragmentos relevantes de cada capa para la consulta específica. La capa corporativa no está completa en el contexto; está indexada en una base vectorial, y solo los fragmentos pertinentes se incluyen. Este patrón reduce el costo en tokens pero requiere que el sistema de recuperación sea suficientemente preciso para no omitir restricciones o políticas relevantes.

**Contexto por composición.** El sistema mantiene un grafo de conocimiento que describe las relaciones entre las capas y los tipos de consulta. Cuando llega una consulta, el sistema determina dinámicamente qué combinación de capas es relevante y construye el contexto por composición. Es el patrón más flexible pero también el más complejo de implementar y mantener.

Para la mayoría de las organizaciones en etapas iniciales de implementación empresarial de IA, el contexto jerárquico estático con compresión progresiva —las instrucciones corporativas de alta autoridad completas, el conocimiento departamental recuperado por relevancia— es el balance correcto entre simplicidad y eficiencia.

### Qué este capítulo no cubre (y el Módulo 4 sí)

La arquitectura descrita en esta sección opera al nivel de diseño del contexto. Las decisiones de infraestructura que hacen que esa arquitectura sea técnicamente robusta son un dominio diferente: cómo escalar la base vectorial para soportar miles de consultas simultáneas, cómo gestionar el ciclo de vida de los modelos de embedding cuando el modelo de base cambia, cómo implementar el monitoreo de calidad de los sistemas de IA en producción continua. Esas decisiones pertenecen al dominio de LLMOps y se abordan en el Módulo 4. El AI Engineer empresarial necesita entender ambas capas, pero sin confundir cuál problema está resolviendo en cada momento.

### Nota del arquitecto

La tentación en proyectos de IA empresarial es resolver primero el problema técnico —elegir las herramientas, construir los conectores, desplegar la infraestructura— y dejar para después las decisiones de gobierno y de estructura del conocimiento. Esta secuencia produce sistemas que funcionan en la demostración pero que se vuelven imposibles de gobernar cuando escalan. La experiencia consistente en organizaciones que han transitado ese camino indica que el orden correcto es el inverso: primero definir la arquitectura de capas de conocimiento y las responsabilidades de gobierno, luego seleccionar las herramientas que implementan esa arquitectura. Las herramientas son fungibles; la arquitectura de contexto que una organización establece tiende a perdurar.

La siguiente sección examina en profundidad el gobierno del conocimiento: quién decide qué entra en cada capa, con qué proceso de aprobación y con qué mecanismo de actualización.
