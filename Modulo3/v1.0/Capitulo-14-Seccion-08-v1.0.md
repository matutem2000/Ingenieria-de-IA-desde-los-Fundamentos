# Capítulo 14 — Seguridad, Gobernanza y Compliance

## Sección 08: Arquitecturas seguras para IA empresarial

Las secciones anteriores de este capítulo construyeron los fundamentos: las amenazas que enfrentan los sistemas de Context Engineering, los controles técnicos para mitigarlas, los principios de privacidad por diseño, la gestión de identidades, los requisitos de compliance y la auditoría. Esta sección integra todo eso en un conjunto de principios de arquitectura que guían el diseño de sistemas de IA empresariales seguros.

Los principios de arquitectura segura para IA no son nuevos: provienen de la ingeniería de seguridad de software y de las mejores prácticas de seguridad en la nube. Lo que es nuevo es su aplicación específica a sistemas de Context Engineering, donde la superficie de ataque incluye el contexto del modelo, el comportamiento del agente y las herramientas que ejecuta.

### Principio 1: Secure by Default

**Secure by default** significa que la configuración predeterminada del sistema es la más segura, no la más conveniente. El usuario o administrador debe hacer un esfuerzo explícito para reducir los controles de seguridad; no para añadirlos.

Aplicado al Context Engineering:

- La memoria del agente está **desactivada por defecto**. Si la función requiere memoria, el administrador la activa explícitamente para ese uso específico.
- Las herramientas disponibles para el agente son las **estrictamente necesarias**, no todas las disponibles. Añadir una herramienta nueva requiere un proceso deliberado.
- Los logs de auditoría están **activados por defecto**. Desactivarlos requiere justificación y aprobación.
- El acceso al sistema RAG está **filtrado por defecto** según los permisos del usuario. Ampliar el acceso requiere cambio explícito de configuración.
- Las respuestas del sistema pasan por **filtros de salida por defecto**. Desactivarlos requiere justificación.

La trampa del "secure by default" es que puede crear fricción en el desarrollo y en las primeras fases de despliegue. El AI Engineer enfrenta la presión de "temporalmente" relajar controles para avanzar más rápido. La palabra clave es "temporalmente": los controles relajados temporalmente tienden a convertirse en permanentes si no hay un proceso para revisarlos.

### Principio 2: Defense in Depth

**Defense in depth** (defensa en profundidad) significa que la seguridad no depende de un único control. Si ese control falla, hay otros que limitan el daño. La profundidad se construye con capas de controles en distintos puntos del sistema.

Para un sistema de Context Engineering completo, las capas de defensa son:

**Capa de autenticación:** el usuario debe autenticarse antes de interactuar con el sistema. Autenticación multifactor para sistemas que acceden a información sensible.

**Capa de validación de entrada:** los mensajes del usuario pasan por un clasificador antes de llegar al sistema. Mensajes con patrones de inyección son rechazados o marcados para revisión.

**Capa de construcción de contexto:** el pipeline de construcción del contexto aplica filtros de acceso, elimina PII innecesaria, inspecciona documentos recuperados y aplica las instrucciones de separación entre instrucciones y datos.

**Capa del system prompt:** el system prompt incluye instrucciones de resistencia a la manipulación, confirmación de identidad del sistema y referencias explícitas a los límites del sistema.

**Capa de ejecución de herramientas:** las herramientas corren en entornos aislados, con permisos mínimos, con confirmación de usuario para acciones de alto impacto y con registro de cada ejecución.

**Capa de filtrado de salida:** las respuestas del modelo son inspeccionadas antes de enviarse al usuario para detectar revelaciones no autorizadas o contenido problemático.

**Capa de auditoría:** todas las capas anteriores generan registros que permiten reconstruir qué ocurrió y detectar patrones de ataque en el tiempo.

Ninguna capa es perfecta. Todas juntas hacen que un atacante necesite comprometer múltiples controles simultáneamente para causar daño significativo.

### Principio 3: Fail Closed

**Fail closed** (fallar de manera cerrada) significa que cuando el sistema falla o encuentra una condición inesperada, deniega el acceso o la operación en lugar de concederla. El opuesto es "fail open": cuando algo falla, el sistema continúa con acceso total, para no interrumpir el servicio.

"Fail open" es tentador porque minimiza las interrupciones de servicio visibles. Es peligroso porque convierte cada falla técnica en una vulnerabilidad de seguridad.

Aplicado al Context Engineering:

- Si el clasificador de inyección falla (error técnico, timeout), el mensaje del usuario es **rechazado**, no procesado.
- Si el sistema RAG no puede aplicar los filtros de acceso del usuario (por un error de IAM), la recuperación de documentos es **denegada**, no realizada con acceso total.
- Si el sistema de sandbox de herramientas no puede establecer el entorno aislado, la herramienta **no se ejecuta**, el agente recibe un error y lo reporta al usuario.
- Si el sistema de logging está caído, las solicitudes en sectores con requisitos de auditoría son **detenidas** hasta que el logging se restaure, no procesadas sin registro.

"Fail closed" puede parecer excesivo en algunos casos. El AI Engineer debe evaluar cuándo la pérdida de disponibilidad es más aceptable que el riesgo de seguridad, y diseñar los mecanismos de failover apropiados: colas de solicitudes, modo degradado con funcionalidad reducida, escalación automática al equipo de operaciones.

### Principio 4: Aislamiento de tenants

En sistemas multiusuario —especialmente en sistemas SaaS donde múltiples organizaciones comparten la misma infraestructura—, el **aislamiento de tenants** garantiza que los datos y el contexto de un usuario u organización no son accesibles para otro.

El aislamiento de tenants en Context Engineering se aplica en:

- **El índice vectorial del RAG:** los documentos de cada tenant están en un namespace separado o el índice aplica metadatos de tenant como filtro obligatorio en todas las consultas.
- **La memoria del agente:** el almacenamiento de memoria es completamente separado por tenant, sin posibilidad de compartir información entre sesiones de distintos tenants.
- **Los logs de auditoría:** cada tenant puede acceder a los logs de sus propias sesiones, no a los de otros.
- **Los modelos:** si el sistema usa modelos ajustados específicamente para un tenant, esos modelos no son accesibles para otros.

### Principio 5: Superficie de ataque mínima

Reducir la superficie de ataque significa exponer al mundo exterior solo lo que es estrictamente necesario para la función del sistema.

En sistemas de Context Engineering:

- El sistema no expone al modelo las herramientas que no son necesarias para la tarea del usuario actual. Si el usuario es un cliente externo, el agente no tiene acceso a herramientas de administración interna.
- Las APIs del sistema no exponen endpoints que no están en uso activo. Las APIs de administración están en redes internas, no en internet.
- El system prompt no contiene información técnica sensible (nombres de sistemas internos, estructuras de bases de datos, credenciales) que podría ser extraída mediante prompt injection.
- El modelo recibe solo la información del contexto que necesita para la tarea actual, no todo el historial disponible.

### Un modelo de referencia de arquitectura segura

La combinación de los cinco principios anteriores produce una arquitectura de referencia para sistemas de Context Engineering empresariales:

```
[Usuario autenticado]
        │
        ▼
[Validación de identidad y permisos]
        │
        ▼
[Clasificador de entrada] ──── Sospechoso ──→ [Rechazo / Log de incidente]
        │
    Seguro
        │
        ▼
[Constructor de contexto]
  ├── System prompt (control de versiones)
  ├── RAG con filtros de acceso por usuario
  ├── Historial de conversación (con política de retención)
  └── Memoria del agente (con aislamiento por tenant)
        │
        ▼
[Modelo de lenguaje]
        │
        ▼
[Decisión: respuesta o herramienta]
  ├── Respuesta → [Filtro de salida] → [Usuario]
  └── Herramienta → [Sandbox] → [Registro de ejecución]
                        │
                    Resultado
                        │
                        ▼
                 [Vuelve al modelo]
        
[Capa transversal: Logging de auditoría en todos los pasos]
```

Este modelo no es prescriptivo en la tecnología de implementación, sino en los controles que cada componente debe incluir. Las tecnologías específicas —el motor de vectores, el sistema de logging, el proveedor de identidades— son decisiones de implementación que dependen del contexto de la organización.

### El costo de la seguridad

La arquitectura descrita añade complejidad, latencia y costo al sistema. El clasificador de entrada introduce latencia adicional. El filtrado de documentos RAG añade pasos al pipeline. El sandbox de herramientas consume recursos. El logging de auditoría tiene costos de almacenamiento.

El AI Engineer necesita hacer ese intercambio explícito y documentado, no ocultarlo. La pregunta no es "¿podemos evitar estos costos?" sino "¿son estos costos apropiados para el perfil de riesgo de este sistema?"

Un asistente de productividad interno con datos no sensibles tiene un perfil de riesgo diferente al de un sistema que apoya decisiones crediticias o que procesa datos de salud. El nivel de control debe ser proporcional al riesgo.

### Nota del arquitecto

Las arquitecturas seguras no son arquitecturas perfectas. Son arquitecturas que hacen explícitas sus asunciones de seguridad, implementan controles proporcionales al riesgo y tienen mecanismos para detectar cuándo esos controles fallan. El AI Engineer que diseña con seguridad no garantiza que el sistema nunca será comprometido: garantiza que el sistema puede detectarlo cuando ocurra y que el daño está limitado.

La siguiente sección organiza estos principios en catálogos prácticos de patrones (qué diseños funcionan) y anti-patrones (qué diseños crear problemas recurrentes).
