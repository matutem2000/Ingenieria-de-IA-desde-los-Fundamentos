# Capítulo 04 — Sección 08

# Arquitecturas modernas

Las secciones anteriores establecieron los principios del diseño de memoria: qué tipos de memoria existen, cómo se almacenan, cómo se recuperan, cómo se consolidan y cómo se olvidan. Esta sección conecta esos principios con las implementaciones concretas que están siendo adoptadas en producción.

Las arquitecturas que presentamos aquí no son experimentos de investigación. Son patrones que equipos de ingeniería están usando para construir sistemas con memoria persistente, y cuya evolución en los últimos dos años ha acelerado significativamente el estado del arte.

## MemGPT: el modelo de gestión de memoria por capas

MemGPT es una arquitectura publicada en 2023 que introduce un modelo de gestión de memoria inspirado en los sistemas operativos: igual que un SO gestiona la memoria RAM y el almacenamiento en disco mediante paginación y swapping, MemGPT gestiona la ventana de contexto del LLM y el almacenamiento externo de manera análoga.

La idea central es que el LLM actúa como procesador que trabaja exclusivamente con lo que tiene en "memoria RAM" (la ventana de contexto), y cuando necesita información que no está en esa ventana, llama a una función para traerla desde el "almacenamiento externo" (la memoria persistente).

```
┌─────────────────────────────────────────────────────┐
│                    CONTEXT (RAM)                    │
│                                                     │
│  [System prompt] [Core memory] [Conversation]      │
│                      ↑    ↑                         │
│              in-context memory                      │
└─────────────────────┬───────────────────────────────┘
                      │ función: search_archival_memory()
                      │ función: recall_memory()
                      ↓
┌─────────────────────────────────────────────────────┐
│                 EXTERNAL STORAGE                    │
│                                                     │
│  [Archival memory] ← conversaciones anteriores      │
│  [Recall memory]  ← hechos semánticos del usuario  │
└─────────────────────────────────────────────────────┘
```

El LLM en MemGPT no recibe toda la memoria de golpe. Recibe solo lo que está en contexto, y cuando necesita más, llama explícitamente a las funciones de recuperación. Esto hace que el sistema sea escalable: la cantidad de memoria almacenada no está limitada por el tamaño del contexto.

**Lo que MemGPT enseña al ingeniero:** la memoria persistente debe ser accesible mediante funciones explícitas (herramientas), no inyectada masivamente al inicio de cada sesión. El LLM debe poder decidir cuándo y qué recuperar.

## Mem0: memoria gestionada como servicio

Mem0 es un framework open source (y servicio cloud) que abstrae la capa de gestión de memoria para aplicaciones LLM. Su propuesta central es que la memoria debería ser un componente de infraestructura separado del modelo, al igual que la base de datos de una aplicación web es un componente separado del servidor de aplicaciones.

Mem0 gestiona automáticamente:
- La extracción de hechos memorables de cada conversación.
- La deduplicación y resolución de conflictos.
- El almacenamiento en una base de datos vectorial interna.
- La recuperación por similitud semántica.
- La actualización de memorias cuando la información cambia.

```python
from mem0 import Memory

m = Memory()

# Añadir memorias desde una conversación
resultado = m.add(
    messages=[
        {"role": "user", "content": "Trabajo como analista de riesgo en un fondo de inversión"},
        {"role": "assistant", "content": "Entendido, trabajaré con el contexto financiero en mente."}
    ],
    user_id="laura_martinez"
)

# Recuperar memorias relevantes para una consulta
memorias = m.search(
    query="¿Qué tipo de informes prefiere este usuario?",
    user_id="laura_martinez"
)

for memoria in memorias:
    print(f"[{memoria['score']:.2f}] {memoria['memory']}")
```

**Lo que Mem0 enseña al ingeniero:** la gestión de memoria puede ser externalizada como servicio, con una API simple de add/search/update. Para proyectos que no justifican una implementación de memoria desde cero, este tipo de abstracción reduce enormemente la complejidad de desarrollo.

## LangMem: integración de memoria en frameworks de agentes

LangMem es el sistema de memoria integrado en el ecosistema LangChain/LangGraph. Su diseño está orientado a agentes que mantienen conversaciones largas y necesitan memoria persistente entre sesiones.

La arquitectura de LangMem distingue tres tipos de memoria con semánticas diferenciadas:

- **InMemoryStore:** almacenamiento en memoria del proceso, sin persistencia. Útil para estado temporal dentro de una sesión.
- **PostgresSaver / SqliteSaver:** almacenamiento de checkpoints de conversación, con persistencia y recuperación por `thread_id`.
- **Semantic memory stores:** integración con bases de datos vectoriales para recuperación por similitud.

Lo que distingue a LangMem es su integración nativa con el grafo de ejecución de agentes: la memoria no es un add-on sino un componente que el agente consulta y actualiza como parte de su ciclo de razonamiento.

## El patrón de triple almacenamiento

Independientemente del framework usado, los sistemas de memoria de producción más maduros convergen en un patrón de triple almacenamiento:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRIPLE STORAGE PATTERN                       │
├─────────────────┬───────────────────┬───────────────────────────┤
│  KEY-VALUE      │  VECTOR STORE     │  RELATIONAL / DOCUMENT    │
│                 │                   │                           │
│  Perfiles de   │  Memorias         │  Historial de             │
│  usuario       │  episódicas y     │  conversaciones,          │
│  (acceso por   │  semánticas       │  logs de acciones,        │
│  ID exacto)    │  (búsqueda por    │  checkpoints              │
│                │  similitud)       │                           │
│  Redis         │  Qdrant/Pinecone  │  PostgreSQL/SQLite        │
│  DynamoDB      │  Weaviate/Chroma  │  MongoDB                  │
└─────────────────┴───────────────────┴───────────────────────────┘
```

La ventaja de este patrón es que cada backend se usa para lo que hace mejor: key-value para acceso por ID exacto y alta velocidad, vectorial para recuperación semántica, relacional para queries estructurados y auditoría.

El costo es la complejidad operativa: tres sistemas de almacenamiento que mantener, sincronizar y respaldad. Este trade-off se justifica en sistemas de producción con alto volumen de usuarios; para sistemas pequeños o en desarrollo, una sola base de datos vectorial (que puede también manejar filtros por metadata) es frecuentemente suficiente.

## Decisiones de diseño al elegir una arquitectura

La elección de arquitectura de memoria no debe hacerse en abstracto sino en función de los requisitos concretos del sistema:

| Pregunta | Implicancia de diseño |
|---|---|
| ¿Cuántos usuarios simultáneos habrá? | Escala del backend, uso de servicios cloud vs. self-hosted |
| ¿Qué tan larga es la relación típica con el usuario? | Importancia de la memoria semántica vs. solo episódica |
| ¿El sistema opera en tiempo real o puede tolerar latencia? | Recuperación sincrónica vs. asincrónica |
| ¿Hay requisitos regulatorios sobre retención de datos? | Necesidad de TTL, eliminación garantizada, auditoría |
| ¿El equipo tiene expertise en operación de bases de datos vectoriales? | Framework vs. implementación desde cero |
| ¿El presupuesto de infraestructura es limitado? | Soluciones managed (Pinecone, Mem0 cloud) vs. self-hosted |

No existe una arquitectura universalmente correcta. Existe la arquitectura que mejor resuelve los requisitos específicos del sistema dentro de las restricciones de equipo, tiempo y presupuesto.

---

*La siguiente sección sistematiza los patrones de diseño que han demostrado funcionar bien en sistemas de memoria de producción: las soluciones repetibles para los problemas recurrentes que el ingeniero encontrará al construir este tipo de sistemas.*
