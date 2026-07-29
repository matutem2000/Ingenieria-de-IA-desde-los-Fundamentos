# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 06: Gestión de identidades y permisos

Un sistema de Context Engineering en producción no interactúa con un usuario abstracto. Interactúa con personas concretas que tienen roles, pertenecen a organizaciones y tienen distintos niveles de autorización para acceder a información y ejecutar acciones. La gestión de identidades y permisos (IAM, por sus siglas en inglés) es el conjunto de mecanismos que hace operativa esa distinción.

En el software tradicional, la IAM es un dominio maduro con patrones establecidos: autenticación mediante credenciales, autorización basada en roles (RBAC), tokens de sesión, control de acceso a recursos. Los sistemas de IA heredan estos mecanismos y añaden una complejidad nueva: el modelo que procesa el contexto no es un usuario humano ni un componente de software determinista. Es un agente que puede tomar decisiones sobre qué información acceder y qué herramientas ejecutar. Esa autonomía hace que la IAM en sistemas de IA requiera consideraciones adicionales.

### Identidades en un sistema de Context Engineering

Un sistema de Context Engineering tiene al menos tres tipos de identidades que requieren gestión separada:

**Identidad del usuario final:** la persona que interactúa con el sistema a través de la interfaz. Su identidad determina qué información puede ver (qué documentos puede recuperar el RAG), qué acciones puede ejecutar (qué herramientas puede activar el agente en su nombre) y qué datos propios del sistema puede modificar (su historial, sus preferencias).

**Identidad del sistema (service identity):** la identidad con la que el sistema de IA se autentica ante los servicios que llama: la base de datos vectorial, la API del modelo, los sistemas de herramientas. Esta identidad determina qué puede hacer el sistema en el backend, independientemente de quién sea el usuario. Es frecuente que los sistemas de IA en producción temprana usen una sola identidad de sistema con permisos amplios por simplicidad; esa práctica es un riesgo.

**Identidad de los componentes del sistema:** en arquitecturas de múltiples agentes (capítulo 11), cada subagente puede tener su propia identidad y permisos. El agente orquestador puede tener permisos de lectura amplia para planificar; los subagentes especializados tienen permisos restringidos al alcance de sus tareas.

### Autenticación y propagación de identidad

El primer problema de IAM en sistemas de IA es establecer con certeza quién es el usuario que realiza una solicitud. La autenticación en sistemas de IA empresariales debe cumplir las mismas exigencias que en cualquier sistema empresarial: autenticación de doble factor para sistemas que acceden a información sensible, tokens de sesión con expiración, revocación de acceso cuando el usuario abandona la organización.

El segundo problema, más específico del Context Engineering, es la **propagación de identidad**: cuando el agente llama a una herramienta o recupera documentos del sistema RAG, ¿qué identidad usa para esa llamada?

Hay dos enfoques:

**Propagación de identidad del usuario:** el sistema propaga la identidad del usuario final a todos los componentes que llama. El sistema RAG, al recibir una consulta, sabe quién es el usuario que la originó y aplica sus permisos. Las herramientas reciben el token del usuario y actúan en su nombre. Este enfoque es más complejo de implementar pero es el correcto para sistemas que acceden a recursos con distintos niveles de acceso por usuario.

**Identidad del sistema con filtros de aplicación:** el sistema usa su propia identidad (con acceso amplio) para todas las llamadas al backend, y aplica los filtros de acceso del usuario en la capa de aplicación antes de incluir el contenido en el contexto. Este enfoque es más simple pero introduce un riesgo: si los filtros de aplicación tienen un bug, el sistema puede acceder a recursos que el usuario no debería ver.

Para sistemas con datos de distintos niveles de confidencialidad, la propagación de identidad del usuario es la opción más segura, aunque requiere que los servicios del backend soporten autenticación por usuario.

### Control de acceso basado en roles para sistemas de IA

El RBAC (Role-Based Access Control) aplicado a sistemas de IA define qué puede hacer cada rol de usuario con el sistema. Los roles típicos incluyen:

**Usuario estándar:** puede realizar consultas, usar las herramientas básicas habilitadas para su perfil, acceder a la información que su rol organizacional autoriza.

**Administrador del sistema:** puede modificar la configuración del sistema (system prompt, herramientas habilitadas, fuentes RAG), revisar logs de conversaciones, gestionar usuarios.

**Auditor:** puede acceder a los logs y registros del sistema con fines de auditoría, pero no puede modificar el sistema ni ver el contenido completo de conversaciones de otros usuarios (solo metadatos para auditoría).

**Propietario del sistema:** tiene acceso completo al sistema y es responsable de las decisiones de gobernanza.

La definición de roles debe ser explícita y documentada. Un error común es tener roles implementados en el código pero no documentados, lo que hace imposible auditar quién tiene qué permisos sin leer el código fuente.

### Permisos de herramientas: el eslabón más crítico

Las herramientas que el agente puede ejecutar merecen una atención especial en la gestión de permisos. Cada herramienta tiene un perfil de riesgo distinto según su impacto:

| Tipo de herramienta | Ejemplos | Impacto de abuso | Requiere |
|---------------------|----------|------------------|----------|
| Lectura de datos públicos | Búsqueda web, documentación pública | Bajo | Autenticación básica |
| Lectura de datos privados | Base de datos de clientes, documentos internos | Medio | Permisos del usuario, propagación de identidad |
| Escritura de datos | Actualizar registros, crear documentos | Alto | Confirmación, log de auditoría |
| Comunicación externa | Enviar correo, publicar en sistemas externos | Alto | Aprobación explícita o límites estrictos |
| Ejecución de código | Intérprete Python, comandos de sistema | Muy alto | Sandbox aislado, permisos mínimos |
| Transacciones | Autorizar pagos, modificar configuraciones críticas | Crítico | Confirmación humana, registro completo |

El principio es claro: las herramientas de mayor impacto requieren controles más estrictos. Para herramientas de impacto alto o crítico, la autorización automática por parte del agente puede no ser apropiada: puede requerir confirmación del usuario antes de ejecutar, o en algunos casos, aprobación de un supervisor humano.

### Sandboxing de herramientas

El sandboxing es el mecanismo que aísla la ejecución de herramientas para limitar el daño que un agente comprometido puede causar. Un agente en ejecución en un sandbox tiene acceso restringido a los recursos del sistema: no puede leer archivos fuera de un directorio designado, no puede realizar llamadas de red a destinos no autorizados, no puede persistir cambios fuera de su espacio de trabajo designado.

Para sistemas de Context Engineering empresariales, el sandboxing de herramientas tiene implementaciones prácticas:

**Contenedores aislados para ejecución de código:** cuando el agente ejecuta código Python o realiza operaciones de sistema, ese código corre en un contenedor con recursos y red limitados. El contenedor tiene tiempo de vida máximo y se destruye al finalizar.

**APIs con permisos de escritura acotados:** en lugar de dar al agente acceso directo a una base de datos, se expone una API que solo permite las operaciones necesarias. La API puede aplicar validaciones adicionales, registrar cada operación y rechazar operaciones que superen un umbral de impacto.

**Circuit breakers para herramientas:** si una herramienta produce errores repetidos o resultados anómalos, el sistema puede desactivarla automáticamente para esa sesión y escalar el incidente al equipo de operaciones.

### El problema de las herramientas encadenadas

En sistemas de múltiples agentes y herramientas encadenadas, los permisos pueden amplificarse de maneras no previstas. Un agente que solo tiene acceso de lectura puede llamar a una herramienta que internamente tiene acceso de escritura. Un agente que opera con la identidad del usuario puede llamar a un subagente que opera con la identidad del sistema.

El AI Engineer que diseña sistemas de herramientas encadenadas debe razonar sobre los permisos efectivos de cada cadena completa, no solo de cada herramienta individual. La pregunta relevante es: ¿qué puede hacer realmente el agente, considerando todas las herramientas que puede encadenar?

### Nota del arquitecto

La gestión de identidades y permisos es el área donde el AI Engineer más frecuentemente necesita coordinarse con el equipo de seguridad de la organización. Los sistemas IAM existentes —Active Directory, Identity Providers (IdP), sistemas de RBAC empresariales— son la base sobre la que se construye la IAM del sistema de IA. El AI Engineer no diseña esos sistemas desde cero; los integra. Pero la integración requiere entender qué controles de permisos son necesarios para el sistema de IA y comunicarlos al equipo de seguridad antes del despliegue.

La siguiente sección aborda el cumplimiento normativo y la auditoría: los requisitos externos que organizaciones en sectores regulados deben satisfacer y los mecanismos de registro que hacen posible demostrarlo.
