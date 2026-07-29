# Capítulo 04 — Sección 06

# Memoria semántica y recuperación

En la sección anterior vimos cómo la memoria persistente permite al sistema recordar información entre sesiones. En esta sección nos concentramos en la forma más conceptualmente rica de esa memoria: la memoria semántica.

La memoria semántica, como vimos en la taxonomía cognitiva, almacena conocimiento general sobre el dominio, el usuario y la organización. No son eventos ("en la sesión del jueves el usuario preguntó X") sino hechos destilados ("el usuario trabaja en riesgo de crédito y tiene expertise en modelos paramétricos"). Es el conocimiento que el sistema acumula sobre su mundo de trabajo.

Esta sección también establece una distinción que es crítica para el diseño de sistemas de IA: la diferencia entre memoria semántica de aplicación y recuperación RAG. Ambas usan tecnologías similares, pero responden a problemas fundamentalmente distintos.

## Qué es la memoria semántica en IA

La memoria semántica en un sistema de IA es el conjunto de representaciones de conocimiento que el sistema ha construido sobre el usuario, el dominio de aplicación y el contexto organizacional, a través de la acumulación e inferencia sobre interacciones pasadas.

Ejemplos concretos:

```
MEMORIA SEMÁNTICA DEL USUARIO:
- Trabaja como Product Manager en empresa de logística
- Sus análisis siempre incluyen KPIs de tiempo de entrega y NPS
- Prefiere comparaciones con benchmarks del sector
- Ha rechazado recomendaciones basadas en reingeniería de procesos
- Su empresa opera en Argentina, Brasil y Chile

MEMORIA SEMÁNTICA DEL DOMINIO:
- La empresa llama "último kilómetro" al segmento de entrega residencial
- "El cliente A" es su cuenta más grande, con contrato hasta diciembre 2026
- Los datos de logística tienen un lag de 48 horas antes de aparecer en el dashboard
- El equipo usa Notion para documentación y Jira para tracking de proyectos
```

Nótese que esta información no está en ningún manual ni base de conocimiento externa. Es conocimiento construido a través de las interacciones, que la aplicación gestiona activamente.

## Cómo se construye la memoria semántica

La memoria semántica se construye mediante tres mecanismos:

**Extracción directa:** el sistema identifica afirmaciones factuales en las conversaciones y las almacena como hechos semánticos. "Trabajo en una empresa de logística con operaciones en tres países" se convierte en tres hechos estructurados: `industry: logistics`, `country_operations: [AR, BR, CL]`, `company_size: multinacional`.

**Inferencia:** el sistema infiere hechos a partir de patrones de comportamiento. Si el usuario siempre añade contexto de costos cuando el sistema no lo incluye, el sistema puede inferir `preferencia: incluir_análisis_de_costo = true`. Esta inferencia se puede almacenar con un nivel de confianza menor que los hechos explícitos.

**Actualización:** cuando la nueva información contradice la memoria existente, el sistema actualiza el hecho en lugar de crear un duplicado. Si el usuario menciona que cambió de empresa, los hechos relacionados con la empresa anterior se marcan como inactivos.

## Recuperación semántica: embeddings y similitud

La recuperación de memoria semántica por similitud es el mecanismo que permite al sistema encontrar conocimiento relevante sin saber exactamente qué buscar.

El proceso tiene tres pasos:

**1. Representación como vector (embedding):**
Cada registro de memoria se convierte en un vector numérico de alta dimensión usando un modelo de embedding. Memorias con contenido semánticamente similar producen vectores que están cerca en ese espacio.

```python
# "El cliente usa Python para análisis" → [0.21, -0.44, 0.87, ...]
# "Prefiere código en Python sobre R"   → [0.19, -0.41, 0.89, ...]
# "Trabaja en logística"                → [0.63,  0.12, 0.05, ...]
```

Los dos primeros vectores son cercanos (misma semántica). El tercero es distante.

**2. Generación del vector de consulta:**
Cuando llega una consulta ("¿Puedes mostrarme el análisis en código?"), se genera su embedding y se busca en la base de datos los registros cuyo vector es más cercano al vector de la consulta.

**3. Ranking y selección:**
Los registros más cercanos (mayor similitud coseno) se seleccionan y se inyectan en el contexto. El número de registros a seleccionar es un parámetro de diseño: demasiados satura el contexto, demasiado pocos puede perder información relevante.

## La distinción crítica: memoria semántica vs. RAG

Esta distinción es fundamental y debe quedar completamente clara antes de continuar.

| Dimensión | Memoria semántica | RAG (Retrieval-Augmented Generation) |
|---|---|---|
| Fuente del conocimiento | Construida por la aplicación a partir de interacciones | Documentos externos preexistentes |
| Quién la gestiona | La aplicación de IA | El sistema RAG (indexador + retriever) |
| Qué representa | Conocimiento sobre el usuario y el dominio de uso | Conocimiento sobre el mundo externo o la base de conocimiento de la organización |
| Ejemplo | "Este usuario prefiere respuestas sintéticas" | "El manual de producto dice que el componente X tiene una garantía de 2 años" |
| Cuando usar | Para personalizar la experiencia y recordar el contexto | Para responder preguntas sobre documentos, bases de conocimiento, o información que el modelo no tiene |

La confusión entre ambos es común porque ambos usan bases de datos vectoriales y recuperación por similitud. La diferencia no está en la tecnología sino en el tipo de conocimiento y en quién lo produce.

La memoria semántica es conocimiento que la aplicación construye sobre su propio contexto de uso. RAG es conocimiento que la organización tiene en documentos y que el sistema recupera para responder preguntas.

Un sistema completo puede tener ambos. La memoria semántica le dice al sistema cómo hablar con este usuario específico. RAG le dice al sistema qué responder sobre el dominio de conocimiento de la organización.

El capítulo 06 está dedicado íntegramente a RAG. Lo que aquí establecemos es el punto de articulación: la memoria semántica es interna a la relación aplicación-usuario, RAG es externa y orientada al conocimiento del dominio.

## Actualización de la memoria semántica

A diferencia de la memoria episódica —que simplemente acumula eventos— la memoria semántica requiere un mecanismo de actualización activa porque representa el estado actual del conocimiento, no una historia de eventos.

El proceso de actualización incluye:

**Detección de contradicción:** el sistema compara la nueva información con la memoria existente. Si encuentra una contradicción directa, no acumula ambas versiones —actualiza el hecho.

**Versionado:** en casos donde la trayectoria temporal importa, puede ser útil versionar los hechos en lugar de sobreescribirlos: `empresa = Fondo Austral (hasta 2025-12), empresa = LogisticAR (desde 2026-01)`.

**Confianza decreciente:** los hechos inferidos deberían tener un score de confianza que decae si no se confirman con evidencia adicional. Un hecho inferido hace 6 meses sin confirmación reciente debería tener menor peso en la recuperación.

---

*La siguiente sección aborda uno de los problemas más importantes y menos discutidos del diseño de memoria: la consolidación y el olvido deliberado. Diseñar bien qué recordar es la mitad del trabajo; diseñar bien qué olvidar y cuándo es la otra mitad.*
