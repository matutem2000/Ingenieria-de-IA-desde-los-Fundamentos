# Capítulo 15 — Proyecto Integrador

## Sección 03: Diseño de la arquitectura completa

Esta sección es el corazón del capítulo. El diagrama que produce no es un resumen de los capítulos anteriores: es el plano de trabajo que te guiará durante las secciones 04 a 08. Consérvalo como plantilla para tus propios proyectos.

### Los siete componentes de la arquitectura

Una solución de IA de producción basada en Context Engineering se organiza en siete componentes interconectados. Cada uno tiene responsabilidades precisas y límites bien definidos.

**Componente 1 — Capa de presentación.** Es la interfaz a través de la cual el usuario interactúa. Puede ser una interfaz de chat web, una API REST consumida por otras aplicaciones internas o un bot de mensajería corporativa. Su responsabilidad es capturar la entrada del usuario, enviarla al orquestador y renderizar la respuesta. No tiene lógica de negocio.

**Componente 2 — Orquestador de contexto.** Es el núcleo de la arquitectura. Recibe la entrada del usuario, construye el contexto que se enviará al LLM, coordina la recuperación de memoria y documentos, invoca herramientas cuando el LLM lo solicita, y devuelve la respuesta ensamblada a la capa de presentación. El orquestador es quien toma las decisiones de qué cabe en la ventana de contexto y en qué orden.

**Componente 3 — Módulo de instrucciones del sistema.** Almacena y sirve las instrucciones del sistema según el perfil del usuario. Cada departamento tiene al menos una instrucción del sistema distinta. El módulo recibe el perfil del usuario (departamento, rol, nivel de autorización) y devuelve la instrucción del sistema correspondiente. Puede almacenar múltiples versiones de la misma instrucción para pruebas A/B.

**Componente 4 — Módulo de memoria.** Gestiona dos tipos de memoria: memoria de sesión (dentro de una conversación) y memoria persistente (entre conversaciones). Persiste en un almacén de clave-valor. El orquestador consulta este módulo al inicio de cada turno para recuperar el contexto relevante de conversaciones previas y actualiza el almacén al final del turno con la información nueva que vale la pena conservar.

**Componente 5 — Motor de recuperación (RAG).** Contiene el pipeline de recuperación aumentada: un índice vectorial con los fragmentos de la documentación interna, el componente de embedding que convierte consultas en vectores, y el motor de búsqueda semántica. Devuelve los fragmentos más relevantes para cada consulta, acompañados de metadatos de origen (documento, sección, fecha de última actualización) que se usan para las citas y para el control de acceso.

**Componente 6 — Módulo de herramientas.** Expone las acciones que el LLM puede invocar sobre sistemas externos: creación de tickets, consulta del directorio, verificación de solicitudes, agendamiento de recordatorios. Cada herramienta tiene una firma de entrada y salida tipada, validación de permisos, y un mecanismo de confirmación que pausa la ejecución hasta que el usuario apruebe la acción.

**Componente 7 — Capa de observabilidad y seguridad.** Registra cada evento del sistema: entrada del usuario, contexto enviado al LLM, respuesta recibida, herramientas invocadas, fuentes recuperadas, latencias en cada etapa. También aplica los controles de seguridad: filtrado de salida, validación de referencias de documentos, enforcement de control de acceso, y detección de intentos de prompt injection.

### El diagrama de referencia

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USUARIO                                       │
│                     (Empleado TechCore)                              │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ entrada de usuario
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   CAPA DE PRESENTACIÓN                               │
│              (Chat Web / API / Bot Corporativo)                      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                  ORQUESTADOR DE CONTEXTO                             │
│                                                                      │
│   1. Recibe entrada + perfil de usuario                              │
│   2. Consulta módulo de instrucciones → obtiene system prompt        │
│   3. Consulta módulo de memoria → recupera contexto previo           │
│   4. Consulta motor RAG → recupera fragmentos relevantes             │
│   5. Construye el contexto completo (system + memoria + RAG + turno) │
│   6. Envía al LLM                                                    │
│   7. Si LLM solicita herramienta → invoca módulo de herramientas     │
│   8. Actualiza memoria con información nueva                         │
│   9. Devuelve respuesta a capa de presentación                       │
└──────┬───────────────────┬──────────────────┬───────────────────────┘
       │                   │                  │
       ▼                   ▼                  ▼
┌──────────────┐  ┌────────────────┐  ┌───────────────────┐
│  MÓDULO DE   │  │    MÓDULO DE   │  │  MOTOR DE         │
│ INSTRUCCIONES│  │    MEMORIA     │  │  RECUPERACIÓN     │
│ DEL SISTEMA  │  │                │  │  (RAG)            │
│              │  │  ┌──────────┐  │  │                   │
│ ┌──────────┐ │  │  │ Sesión   │  │  │  ┌─────────────┐ │
│ │ Perfil   │ │  │  │ (en mem) │  │  │  │  Embeddings │ │
│ │ TI       │ │  │  └──────────┘  │  │  └─────────────┘ │
│ ├──────────┤ │  │  ┌──────────┐  │  │  ┌─────────────┐ │
│ │ Perfil   │ │  │  │Persistente│  │  │  │ Índice      │ │
│ │ Legal    │ │  │  │(KV store) │  │  │  │ Vectorial   │ │
│ ├──────────┤ │  │  └──────────┘  │  │  └─────────────┘ │
│ │ Perfil   │ │  └────────────────┘  │  ┌─────────────┐ │
│ │ RRHH     │ │                      │  │ Documentos  │ │
│ ├──────────┤ │                      │  │ internos    │ │
│ │ Perfil   │ │                      │  └─────────────┘ │
│ │ Finanzas │ │                      └───────────────────┘
│ └──────────┘ │
└──────────────┘
       │
       ▼
┌──────────────────────────────────────────────┐
│         MÓDULO DE HERRAMIENTAS               │
│                                              │
│  • crear_ticket(tipo, descripción, prioridad)│
│  • consultar_directorio(nombre, departamento)│
│  • verificar_solicitud(id_solicitud)         │
│  • agendar_recordatorio(fecha, descripción)  │
│                                              │
│  [Todas con validación de permisos +         │
│   confirmación de usuario antes de ejecutar] │
└──────────────────────────────────────────────┘

Transversal a todos los componentes:
┌─────────────────────────────────────────────────────────────────────┐
│            CAPA DE OBSERVABILIDAD Y SEGURIDAD                        │
│                                                                      │
│  Logging de cada evento  │  Control de acceso  │  Filtrado de salida │
│  Métricas de latencia    │  Detección de ataques│  Auditoría         │
└─────────────────────────────────────────────────────────────────────┘
```

### Las cinco decisiones de arquitectura

Un diagrama sin las decisiones que lo produjeron es incompleto. Cada elección estructural de esta arquitectura tiene una justificación y una alternativa descartada.

**Decisión 1: Orquestador propio en lugar de framework de alto nivel.**

Se decidió construir el orquestador como componente propio en lugar de usar un framework de agentes de alto nivel (LangChain, LlamaIndex, AutoGPT). La razón es el control de observabilidad: los frameworks de alto nivel ocultan las llamadas al LLM y dificultan el registro granular de cada paso. En un sistema empresarial con requisitos de auditoría (RNF-03), la transparencia de cada operación no es negociable. El costo de esa decisión es mayor tiempo de desarrollo inicial; el beneficio es inspectabilidad completa del flujo.

**Decisión 2: Instrucciones del sistema gestionadas como datos, no como código.**

Las instrucciones del sistema se almacenan en una base de datos o sistema de archivos versionado, no en el código fuente de la aplicación. Esto permite actualizar el comportamiento del asistente sin re-desplegar el servicio. Un cambio en la política de escalación de TI se refleja actualizando el texto de la instrucción del sistema del perfil TI, no modificando el código. La alternativa —instrucciones embebidas en el código— haría cada ajuste editorial una operación de ingeniería.

**Decisión 3: RAG en lugar de fine-tuning para el conocimiento interno.**

La documentación interna de TechCore cambia frecuentemente: las políticas se actualizan, los runbooks se modifican, los contratos se renuevan. Fine-tuning de un modelo con documentación interna requeriría re-entrenamiento cada vez que hay un cambio, con los costos y plazos que eso implica. RAG permite actualizar el índice vectorial sin modificar el modelo base y, adicionalmente, provee referencias exactas a los documentos fuente, lo que cumple el requisito de auditoría. Fine-tuning tiene sentido cuando el conocimiento es estable y la velocidad de inferencia es crítica; ninguna de las dos condiciones aplica a TechCore v1.0.

**Decisión 4: Un solo agente de análisis de incidentes, no multiagente.**

RF-05 podría haberse implementado con una arquitectura multiagente: un agente coordinador que delega en agentes especializados de diagnóstico, búsqueda en runbooks y escalación. Esa arquitectura añade flexibilidad pero también añade puntos de falla, latencia acumulada y complejidad de depuración. Para v1.0, un agente único con herramientas bien definidas es suficiente: puede diagnosticar, buscar en runbooks y escalar. La transición a multiagente se justificará cuando los ciclos de razonamiento del agente único sean insuficientes para los incidentes más complejos.

**Decisión 5: Confirmación de usuario antes de ejecutar herramientas.**

Toda acción sobre sistemas externos requiere confirmación explícita del usuario. Esta decisión sacrifica velocidad de interacción a favor de control: el usuario siempre sabe qué va a hacer el sistema antes de que lo haga. Un sistema que crea tickets o agenda reuniones sin confirmación puede generar efectos no deseados difíciles de revertir. La confirmación es el mecanismo de supervisión humana en el nivel de interacción.

### La arquitectura como contrato

El diagrama y las cinco decisiones funcionan como un contrato entre el equipo de ingeniería, los usuarios del sistema y los administradores: definen qué hace el sistema, qué no hace, y por qué. Un contrato arquitectónico documentado es la diferencia entre un sistema que el equipo puede mantener y evolucionar de manera razonada, y un sistema que crece de manera improvisada hasta volverse inmanejable.

Las secciones que siguen desarrollan cada componente con el nivel de detalle necesario para pasar del diagrama a la implementación.
