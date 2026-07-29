# Capítulo 04 — Sección 09

# Patrones de diseño

Un patrón de diseño es una solución repetible para un problema recurrente en un contexto dado. En el diseño de sistemas de memoria para IA, ciertos problemas aparecen una y otra vez independientemente del dominio de aplicación: cómo estructurar el perfil del usuario, cómo inyectar la memoria en el contexto sin saturarlo, cómo actualizar memoria sin perder información válida.

Esta sección presenta los patrones que han emergido como soluciones robustas a esos problemas. Para cada patrón: el problema que resuelve, la estructura de la solución y las condiciones en que aplica.

## Patrón 1: Memory Store

**Problema:** el sistema necesita almacenar y recuperar información de usuario de forma confiable, pero la implementación directa mezcla lógica de negocio con lógica de almacenamiento.

**Solución:** encapsular todo el acceso a la memoria en un objeto o módulo dedicado con una interfaz clara: `guardar`, `recuperar`, `actualizar`, `eliminar`. El resto del sistema nunca accede directamente al backend de almacenamiento; solo interactúa con el Memory Store.

```python
class MemoryStore:
    """Abstrae el acceso a la capa de almacenamiento de memoria."""

    def __init__(self, vector_store, kv_store):
        self._vector_store = vector_store
        self._kv_store = kv_store

    def guardar_hecho(self, user_id: str, hecho: str, tipo: str, metadata: dict = {}):
        """Guarda un hecho semántico sobre el usuario."""
        embedding = generar_embedding(hecho)
        self._vector_store.upsert(
            id=generar_id(user_id, hecho),
            embedding=embedding,
            metadata={"user_id": user_id, "tipo": tipo, "contenido": hecho, **metadata}
        )

    def recuperar_relevante(self, user_id: str, consulta: str, top_k: int = 5) -> list[dict]:
        """Recupera los hechos más relevantes para una consulta dada."""
        embedding_consulta = generar_embedding(consulta)
        return self._vector_store.buscar(
            embedding=embedding_consulta,
            filtros={"user_id": user_id},
            top_k=top_k
        )

    def obtener_perfil(self, user_id: str) -> dict:
        """Recupera el perfil estructurado del usuario."""
        return self._kv_store.get(f"perfil:{user_id}") or {}

    def eliminar_usuario(self, user_id: str):
        """Elimina toda la memoria de un usuario (para cumplimiento de privacidad)."""
        self._vector_store.eliminar(filtros={"user_id": user_id})
        self._kv_store.delete(f"perfil:{user_id}")
```

**Cuándo aplica:** siempre. Es el patrón base sobre el que construyen todos los demás.

## Patrón 2: Context Assembler

**Problema:** la información disponible en la memoria (perfil, memorias episódicas, preferencias) supera el espacio disponible en el contexto. El sistema necesita decidir qué incluir y qué omitir para cada consulta específica.

**Solución:** un componente dedicado que recibe la consulta actual y ensambla el contexto óptimo para esa consulta, priorizando y filtrando la memoria disponible según relevancia y restricciones de tokens.

```python
class ContextAssembler:
    def __init__(self, memory_store: MemoryStore, max_tokens_memoria: int = 1500):
        self._memory = memory_store
        self._max_tokens = max_tokens_memoria

    def ensamblar(self, user_id: str, consulta: str, historial: list[dict]) -> str:
        """
        Produce el bloque de contexto de memoria para inyectar en el prompt.
        Prioriza: perfil > memorias relevantes a la consulta > historial reciente.
        """
        perfil = self._memory.obtener_perfil(user_id)
        memorias_relevantes = self._memory.recuperar_relevante(
            user_id=user_id,
            consulta=consulta,
            top_k=8
        )

        # Construir bloque de contexto con control de tokens
        bloque = []
        tokens_usados = 0

        # Siempre incluir el perfil (alta prioridad)
        perfil_str = formatear_perfil(perfil)
        bloque.append(f"### Contexto del usuario\n{perfil_str}")
        tokens_usados += contar_tokens(perfil_str)

        # Añadir memorias relevantes hasta el límite de tokens
        memorias_str_list = []
        for memoria in memorias_relevantes:
            m_str = f"- {memoria['contenido']}"
            if tokens_usados + contar_tokens(m_str) > self._max_tokens:
                break
            memorias_str_list.append(m_str)
            tokens_usados += contar_tokens(m_str)

        if memorias_str_list:
            bloque.append(f"### Memorias relevantes\n" + "\n".join(memorias_str_list))

        return "\n\n".join(bloque)
```

**Cuándo aplica:** cuando el sistema tiene memoria persistente significativa y el riesgo de saturar el contexto con memoria es real.

## Patrón 3: Memory Extractor

**Problema:** después de cada conversación, el sistema necesita identificar qué información nueva merece ser persistida, pero no es viable hacer eso manualmente ni guardar todo indiscriminadamente.

**Solución:** un paso dedicado de extracción que usa el LLM para identificar hechos memorables al final de la conversación (o de forma incremental durante la misma).

```python
PROMPT_EXTRACCION = """Eres un sistema de extracción de memoria. 
Analiza la conversación siguiente e identifica únicamente la información que 
vale la pena recordar para futuras interacciones.

Criterios para incluir:
- Preferencias explícitas o implícitas del usuario
- Hechos sobre su rol, empresa, proyectos o dominio de trabajo
- Decisiones o acuerdos tomados que afectan trabajo futuro
- Restricciones o limitaciones mencionadas

Criterios para excluir:
- Preguntas exploratorias sin conclusión
- Contenido válido solo para esta sesión
- Información trivial o rutinaria

Responde en formato JSON con la lista de hechos a guardar:
{"hechos": [{"contenido": "...", "tipo": "preferencia|hecho|decision|restriccion", "confianza": "alta|media"}]}

Conversación:
{conversacion}"""

def extraer_memorias(conversacion: list[dict], llm) -> list[dict]:
    respuesta = llm.completar(
        prompt=PROMPT_EXTRACCION.format(conversacion=formatear_conversacion(conversacion))
    )
    return json.loads(respuesta)["hechos"]
```

**Cuándo aplica:** cuando la captura de memoria es implícita (el sistema infiere qué guardar, no espera instrucciones explícitas del usuario).

## Patrón 4: Memory Updater (Upsert semántico)

**Problema:** cuando el sistema intenta guardar un hecho nuevo, puede que ya exista un hecho similar o contradictorio en la memoria. Guardar ambos produce inconsistencias; descartar el nuevo puede perder información válida.

**Solución:** antes de insertar, buscar si existe un registro semánticamente similar. Si existe y el nuevo hecho lo contradice, actualizar. Si existe y el nuevo hecho lo confirma, reforzar su score de confianza. Si no existe, insertar.

```python
def upsert_semantico(memory_store: MemoryStore, user_id: str, hecho_nuevo: dict):
    """
    Inserta o actualiza un hecho en memoria, resolviendo conflictos semánticamente.
    """
    similares = memory_store.recuperar_relevante(
        user_id=user_id,
        consulta=hecho_nuevo["contenido"],
        top_k=3
    )

    for similar in similares:
        if similar["score"] > 0.92:  # Alta similitud: mismo hecho
            if hay_contradiccion(similar["contenido"], hecho_nuevo["contenido"]):
                # El nuevo hecho contradice al existente: actualizar
                memory_store.actualizar(
                    id=similar["id"],
                    contenido=hecho_nuevo["contenido"],
                    metadata={"actualizado_en": datetime.now().isoformat()}
                )
                return "actualizado"
            else:
                # El nuevo hecho confirma al existente: reforzar confianza
                memory_store.incrementar_confianza(id=similar["id"])
                return "confirmado"

    # No hay similar: insertar como nuevo
    memory_store.guardar_hecho(user_id, hecho_nuevo["contenido"], hecho_nuevo["tipo"])
    return "insertado"
```

**Cuándo aplica:** en cualquier sistema que capture memoria implícita durante períodos extendidos. Es el patrón que previene la acumulación de memorias contradictorias.

## Patrón 5: Sesión con Checkpoint

**Problema:** en sesiones largas o en agentes que operan durante horas, el estado de la sesión puede perderse por fallos del sistema, timeouts, o desconexiones del usuario.

**Solución:** guardar checkpoints del estado de la sesión (incluyendo el historial de conversación, el estado de las herramientas y cualquier output parcial) en almacenamiento persistente a intervalos regulares o en puntos críticos del flujo.

```python
class SesionConCheckpoint:
    def __init__(self, session_id: str, storage):
        self.session_id = session_id
        self._storage = storage
        self.historial = []
        self.estado = {}
        self._cargar_checkpoint()

    def _cargar_checkpoint(self):
        checkpoint = self._storage.get(f"checkpoint:{self.session_id}")
        if checkpoint:
            self.historial = checkpoint["historial"]
            self.estado = checkpoint["estado"]

    def guardar_checkpoint(self):
        self._storage.set(
            key=f"checkpoint:{self.session_id}",
            value={"historial": self.historial, "estado": self.estado},
            ttl=86400  # 24 horas
        )

    def agregar_turno(self, role: str, content: str):
        self.historial.append({"role": role, "content": content})
        if len(self.historial) % 5 == 0:  # Checkpoint cada 5 turnos
            self.guardar_checkpoint()
```

**Cuándo aplica:** en agentes autónomos de larga duración, en aplicaciones donde la sesión puede interrumpirse, en cualquier contexto donde perder el estado de sesión tiene costo significativo para el usuario.

---

*La siguiente sección examina los anti-patrones: los errores de diseño más comunes en sistemas de memoria de IA y por qué producen los comportamientos problemáticos que producen.*
