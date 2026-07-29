# Capítulo 12 — Context Engineering Empresarial

## Sección 05: Integración con sistemas corporativos

Una organización rara vez construye su sistema de IA en un vacío. Existe una infraestructura de tecnología de la información preexistente: un CRM que registra las interacciones con clientes, un ERP que gestiona los procesos financieros y operativos, un sistema de gestión documental que centraliza los documentos corporativos, un directorio de empleados que controla la autenticación y los permisos, y decenas de otros sistemas sectoriales según el tipo de organización. El sistema de IA empresarial debe integrarse con esa infraestructura, no ignorarla ni reemplazarla.

Esta integración no es un problema técnico trivial. Los sistemas corporativos preexistentes tienen APIs propias, esquemas de datos que evolucionaron durante años, controles de acceso establecidos y equipos responsables de su mantenimiento. La integración con el sistema de IA añade un consumidor nuevo —el modelo de lenguaje— con requisitos de consumo de datos que difieren de los que los sistemas existentes fueron diseñados para servir.

### El mapa de integración

El primer paso para diseñar la integración es construir un inventario de los sistemas corporativos existentes y clasificarlos según su rol en el contexto del sistema de IA.

**Sistemas fuente de conocimiento.** Son los sistemas cuyo contenido se indexa en la base de conocimiento vectorial. El repositorio de documentos corporativos, la wiki interna, la base de conocimiento de soporte, el catálogo de productos. La integración con estos sistemas puede ser por lotes —el indexador extrae documentos periódicamente y actualiza la base vectorial— o en tiempo real, con un webhook o evento que dispara la reindexación cuando un documento cambia.

**Sistemas fuente de contexto dinámico.** Son los sistemas cuya información no se indexa en la base vectorial sino que se recupera dinámicamente en el momento de cada consulta para enriquecer el contexto específico de esa interacción. El CRM, que contiene el historial de interacciones del cliente que está escribiendo en este momento. El ERP, que contiene el estado actual de un pedido sobre el que el usuario pregunta. La base de datos de inventario, que contiene la disponibilidad real de un producto en este instante. Esta información cambia con tanta frecuencia que indexarla en una base vectorial produciría resultados constantemente desactualizados; la solución correcta es recuperarla como herramienta en el momento de la consulta.

**Sistemas de autenticación y autorización.** El directorio corporativo —Active Directory, LDAP, o un sistema de SSO basado en SAML u OAuth 2.0— que controla quién puede acceder al sistema de IA y con qué permisos. La integración con estos sistemas es estructural: el sistema de IA no gestiona usuarios propios; se apoya en la infraestructura de identidad existente de la organización.

**Sistemas destino de acciones.** Si el sistema de IA es un agente con capacidad de actuar —no solo de responder—, necesita integrarse con los sistemas sobre los que puede actuar. El sistema de tickets de soporte, donde el agente puede crear, actualizar o escalar un ticket. El sistema de gestión de tareas, donde el agente puede asignar una tarea a un miembro del equipo. El sistema de calendario, donde el agente puede agendar una reunión.

### Patrones de integración

La forma en que el sistema de IA accede a los sistemas corporativos determina tanto la calidad del contexto como la complejidad del mantenimiento. Hay cuatro patrones fundamentales, con sus compromisos específicos.

**Integración directa vía API.** El sistema de IA llama directamente a la API del sistema corporativo en el momento de la consulta. Es el patrón más simple y más fresco —los datos son tan actuales como el sistema puede proporcionar— pero tiene dos limitaciones. La primera es la latencia: cada llamada a un sistema externo agrega tiempo de respuesta al sistema de IA. Si una consulta requiere datos de tres sistemas corporativos, la latencia total puede volverse inaceptable para el usuario. La segunda es el acoplamiento: si el sistema corporativo tiene una interrupción o un cambio de API, el sistema de IA queda afectado directamente.

**Capa de servicio intermediaria.** El sistema de IA no llama directamente a los sistemas corporativos; llama a una capa de servicio intermedia que sí conoce los detalles de cada sistema. La capa de servicio puede implementar caché para reducir latencia, transformación de datos para normalizar los formatos, y reintentos para manejar errores transitorios. Este patrón desacopla el sistema de IA de los sistemas corporativos al costo de una capa adicional de mantenimiento.

**Integración por eventos.** Los sistemas corporativos publican eventos cuando su estado cambia, y el sistema de IA se suscribe a esos eventos para actualizar su contexto. Un evento de "pedido actualizado" en el ERP desencadena la actualización del estado del pedido en la capa de contexto del sistema de IA. Es eficiente para mantener el contexto actualizado sin polling constante, pero requiere que los sistemas corporativos soporten una arquitectura de eventos, que no siempre es el caso en sistemas heredados.

**Indexación periódica con caché.** Para datos que cambian con frecuencia pero no en tiempo real, el sistema extrae los datos de los sistemas corporativos periódicamente —cada hora, cada día, según la volatilidad— y los almacena en una capa de caché accesible rápidamente por el sistema de IA. El catálogo de productos actualizado diariamente, el directorio de empleados actualizado semanalmente, las listas de precios actualizadas con cada ciclo comercial. Este patrón reduce la latencia y el acoplamiento en tiempo real al costo de datos que pueden tener un retardo respecto del sistema fuente.

### Integración con sistemas heredados

Un desafío específico en el contexto empresarial es la integración con sistemas heredados: aplicaciones que llevan décadas en funcionamiento, que gestionan datos críticos del negocio y que no tienen APIs modernas, documentación accesible ni equipos disponibles para agregarla.

La integración con sistemas heredados requiere un enfoque diferente al de sistemas modernos. Las opciones disponibles son, en orden de preferencia:

**Adaptar a través de una capa de integración.** Construir un servicio que traduzca entre el protocolo del sistema heredado —SOAP, EDI, pantallas green-screen, archivos planos— y las interfaces que el sistema de IA puede consumir. Este servicio añade complejidad pero desacopla el sistema de IA de las peculiaridades del sistema heredado.

**Exportación periódica de datos.** Si el sistema heredado no tiene API pero puede exportar datos en algún formato —archivos CSV, volcados de base de datos—, el sistema de IA puede consumir esas exportaciones periódicas. La frescura de los datos estará limitada por la frecuencia de las exportaciones, pero para muchos casos de uso esto es aceptable.

**Integración mediante herramientas humanas en el loop.** Para sistemas heredados que no pueden integrarse de ninguna manera automatizada, el sistema de IA puede solicitar al usuario que le proporcione la información del sistema heredado directamente. No es la solución ideal, pero es pragmática cuando la alternativa es bloquear el proyecto por meses esperando una integración técnica con un sistema que nadie quiere tocar.

### Controles de seguridad en la integración

La integración del sistema de IA con los sistemas corporativos requiere que los controles de seguridad existentes en esos sistemas se extiendan al sistema de IA, no que se ignoren.

Cuando el sistema de IA actúa como agente que llama a sistemas corporativos, lo hace con un conjunto de credenciales. Esas credenciales deben tener el mínimo de permisos necesarios para la funcionalidad requerida —el principio de mínimo privilegio—. Un agente que necesita leer el estado de pedidos en el ERP no debe tener permisos de escritura en el ERP. Un asistente que necesita consultar el CRM no debe tener permisos para exportar la base de clientes completa.

El sistema de IA debe registrar cada llamada a sistemas corporativos —qué sistema, qué datos solicitó, en el contexto de qué consulta de usuario— para que exista un registro de auditoría que permita revisar el comportamiento del sistema ante un incidente de seguridad.

Las credenciales de acceso a sistemas corporativos nunca deben estar en el contexto del sistema de IA donde el modelo puede leerlas. Deben gestionarse en un sistema de gestión de secretos externo al modelo.

### Nota del arquitecto

La integración con sistemas corporativos es el lugar donde los proyectos de IA empresarial tardan más de lo esperado. Las APIs están mal documentadas, los datos tienen problemas de calidad, los equipos responsables de los sistemas corporativos tienen sus propias prioridades, y los sistemas heredados presentan sorpresas en cada conexión. Una estimación realista para un proyecto de integración corporativa es al menos el doble del tiempo inicial estimado para la integración pura, más tiempo adicional para los problemas de calidad de datos que inevitablemente aparecen.

El consejo práctico es comenzar con el sistema corporativo más simple y mejor documentado para aprender los patrones de integración de la organización específica antes de abordar los sistemas más complejos. Cada organización tiene sus peculiaridades: sus políticas de seguridad para conceder acceso a APIs, sus procesos de aprobación para integraciones nuevas, sus equipos con más y menos capacidad de colaboración. Conocer esas peculiaridades antes de enfrentar la integración más difícil reduce los riesgos del proyecto.

La siguiente sección examina cómo se comparte el contexto entre múltiples equipos que usan sistemas de IA distintos dentro de la misma organización.
