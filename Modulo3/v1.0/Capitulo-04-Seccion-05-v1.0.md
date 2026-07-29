# Capítulo 04 — Sección 05

# Memoria persistente

La memoria conversacional existe dentro de una sesión. Cuando la sesión termina, esa memoria desaparece. La memoria persistente es la respuesta a esa discontinuidad: información almacenada fuera del modelo, en un sistema externo de almacenamiento, disponible para ser recuperada en cualquier sesión futura.

Si la memoria conversacional es la memoria de trabajo de la sesión actual, la memoria persistente es el cuaderno que el ingeniero deja sobre el escritorio antes de apagar la computadora: al día siguiente, todo lo importante sigue ahí.

## Qué se persiste y qué no

No toda la información de una conversación merece ser persisted. Persistir indiscriminadamente produce bases de datos ruidosas y recuperaciones imprecisas. El primer principio del diseño de memoria persistente es la selectividad.

La información que típicamente vale la pena persistir incluye:

**Preferencias del usuario:**
- Formato de respuesta preferido (detallado vs. sintético, con ejemplos vs. sin ejemplos)
- Idioma o registro lingüístico
- Áreas de expertise o conocimiento previo que el sistema debería asumir
- Temas o enfoques que el usuario ha rechazado explícitamente

**Hechos sobre el dominio de trabajo:**
- Nombres de proyectos, clientes, productos o entidades recurrentes
- Restricciones o reglas de negocio mencionadas por el usuario
- Decisiones tomadas en sesiones anteriores que afectan el trabajo actual
- Estado actualizado de proyectos en curso

**Contexto de la relación:**
- Objetivos de largo plazo expresados por el usuario
- Historial de tareas completadas o en progreso
- Feedback dado sobre respuestas anteriores del sistema

La información que generalmente no vale la pena persistir incluye: preguntas de exploración sin conclusión, contenido trivial o rutinario, información válida solo para el contexto inmediato de una sesión específica.

## Tecnologías de almacenamiento persistente

La elección del backend de almacenamiento depende de cómo se va a recuperar la información. Hay tres familias principales:

### Key-value stores y bases de datos documentales

Son la opción más simple y apropiada para perfiles de usuario estructurados y memoria semántica de baja complejidad.

```json
{
  "user_id": "usr_4821",
  "perfil": {
    "nombre": "Laura",
    "rol": "Analista de riesgo",
    "empresa": "Fondo Austral",
    "preferencias": {
      "formato_respuesta": "sintético con bullet points",
      "nivel_detalle_técnico": "alto",
      "idioma_código": "Python"
    },
    "dominios_expertise": ["renta fija", "derivados", "riesgo cambiario"],
    "proyectos_activos": ["informe_riesgo_Q3_2026", "modelo_stress_test"]
  },
  "ultima_actualizacion": "2026-07-24T15:32:00Z"
}
```

**Cuándo usar:** cuando la recuperación es siempre por ID de usuario o entidad conocida, cuando la estructura de datos es predecible, cuando no se necesita búsqueda por similitud semántica.

**Tecnologías:** Redis, MongoDB, DynamoDB, PostgreSQL con JSONB, SQLite para proyectos pequeños.

### Bases de datos vectoriales

Son la opción apropiada cuando la recuperación necesita ser semántica: no busco "el perfil del usuario 4821" sino "algo relacionado con lo que el usuario preguntó antes sobre estrategias de cobertura".

En una base de datos vectorial, cada registro de memoria se almacena junto con su embedding —una representación numérica de su contenido semántico—. La recuperación consiste en encontrar los registros cuyos embeddings son más similares al embedding de la consulta actual.

```python
# Ejemplo de almacenamiento en base de datos vectorial
def guardar_memoria(contenido: str, metadata: dict, coleccion: str):
    embedding = generar_embedding(contenido)
    registro = {
        "id": generar_id(),
        "contenido": contenido,
        "embedding": embedding,
        "metadata": {
            "user_id": metadata["user_id"],
            "timestamp": datetime.now().isoformat(),
            "tipo": metadata["tipo"],  # "episodica", "semantica", "procedimental"
            "fuente": metadata["fuente"]  # "conversacion", "documento", "inferida"
        }
    }
    coleccion.insert(registro)

# Recuperación por similitud semántica
def recuperar_memoria_relevante(consulta: str, user_id: str, top_k: int = 5):
    embedding_consulta = generar_embedding(consulta)
    resultados = coleccion.buscar(
        embedding=embedding_consulta,
        filtros={"user_id": user_id},
        top_k=top_k
    )
    return resultados
```

**Cuándo usar:** cuando la recuperación debe ser por relevancia conceptual, cuando el volumen de memorias es alto y la búsqueda exacta no escala, cuando se necesita encontrar memorias relacionadas sin saber exactamente cuáles son.

**Tecnologías:** Pinecone, Weaviate, Qdrant, Chroma, pgvector (extensión de PostgreSQL).

### Grafos de conocimiento

Son la opción más expresiva pero también la más compleja. Permiten representar relaciones entre entidades de forma que el sistema puede razonar sobre conexiones: "Laura trabaja en Fondo Austral → Fondo Austral tiene exposición al sector energético → el cliente del sector energético es TotalEnergies Argentina".

**Cuándo usar:** cuando las relaciones entre entidades son parte del modelo de datos (no solo los atributos individuales), cuando el sistema necesita hacer razonamiento multi-hop, cuando el dominio es complejo con muchas entidades interrelacionadas.

**Tecnologías:** Neo4j, Amazon Neptune, MemGraph, o implementaciones ad-hoc sobre grafos Python (NetworkX) para sistemas pequeños.

## Estrategias de escritura

La escritura en memoria persistente puede ocurrir de tres maneras:

**Escritura al cierre de sesión:** el sistema procesa toda la conversación al final y extrae los elementos persistibles. Tiene la ventaja de contar con el contexto completo de la sesión para decidir qué guardar.

**Escritura incremental:** el sistema escribe en memoria después de cada turno o cada grupo de turnos. Útil para sesiones muy largas o cuando la información es urgente (un agente que necesita que otros agentes accedan a información generada en tiempo real).

**Escritura bajo demanda:** el sistema solo escribe en memoria cuando detecta explícitamente que algo merece ser recordado —porque el usuario lo indica, o porque el modelo lo infiere con alta confianza. Más selectiva, más difícil de implementar bien.

## El problema de la consistencia

La memoria persistente introduce un problema que la memoria conversacional no tiene: la información puede volverse inconsistente con la realidad.

Un perfil de usuario guardado hace seis meses puede contener información desactualizada: el usuario cambió de empresa, el proyecto que estaba activo ya cerró, las preferencias de formato evolucionaron. Si el sistema recupera y usa esa información sin verificarla, puede producir respuestas basadas en realidades que ya no existen.

La gestión de la consistencia requiere diseño explícito:
- **Timestamps:** toda memoria persistida debería incluir cuándo fue capturada y cuándo fue usada por última vez.
- **Vencimiento:** algunos tipos de memoria deberían tener fechas de expiración automáticas (información de proyectos activos, por ejemplo).
- **Resolución de conflictos:** cuando la nueva información contradice la memoria existente, el sistema debe actualizar la memoria en lugar de acumular versiones contradictorias.
- **Confirmación periódica:** para memorias de alta importancia, el sistema puede incluir en la conversación una verificación implícita de que la información sigue siendo correcta.

Este aspecto —cuándo y cómo actualizar o eliminar memoria— es tan importante que tiene su propia sección en este capítulo: la sección 07, dedicada a consolidación y olvido.

---

*La siguiente sección examina la memoria semántica desde el punto de vista de la recuperación por similitud, y establece la distinción entre memoria semántica gestionada por la aplicación y la recuperación RAG —que será el tema del capítulo 06.*
