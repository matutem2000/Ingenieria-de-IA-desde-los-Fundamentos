# Capítulo 15 — Proyecto Integrador

## Sección 07: Observabilidad y seguridad de la solución

Observabilidad y seguridad no son capas que se agregan al final del diseño. Son dimensiones que se planifican desde el primer diagrama de arquitectura. En el caso de TechCore, ambas son requisitos explícitos del pliego: auditoría completa de interacciones (RNF-03) y control de acceso por departamento y rol (RF-06). Esta sección traduce esos requisitos en componentes concretos del sistema.

### La capa de observabilidad

La observabilidad de un sistema de IA tiene tres niveles de granularidad, y TechCore los implementa todos.

**Nivel 1 — Trazas de interacción.** Cada conversación genera una traza que registra la secuencia completa de eventos: entrada del usuario, instrucción del sistema utilizada, fragmentos RAG recuperados, herramientas invocadas y resultados, respuesta del LLM, respuesta final al usuario. Una traza es el registro forense de lo que pasó en una interacción.

**Nivel 2 — Métricas de operación.** Resúmenes cuantitativos del comportamiento del sistema en el tiempo: latencia por etapa, tasa de recuperación de documentos relevantes, tasa de uso de herramientas, tasa de errores, costo de tokens por usuario y por departamento.

**Nivel 3 — Alertas operacionales.** Umbrales configurados sobre las métricas que disparan notificaciones cuando el sistema se comporta fuera de los parámetros normales.

### Estructura de la traza de interacción

Cada evento en el sistema emite un registro con la siguiente estructura:

```json
{
  "trace_id": "trc-20260725-0842-emp0472",
  "session_id": "ses-20260725-0831",
  "user_id": "emp-0472",
  "department": "ti",
  "timestamp": "2026-07-25T08:42:17.334Z",
  "event_type": "interaction_complete",
  "latency_ms": {
    "total": 4821,
    "memory_retrieval": 43,
    "rag_query": 312,
    "llm_inference": 4290,
    "tool_execution": 0
  },
  "context_tokens": {
    "system_prompt": 987,
    "memory": 412,
    "rag_fragments": 1843,
    "conversation_history": 1102,
    "total_input": 4344,
    "output": 287
  },
  "rag": {
    "query_embedding_generated": true,
    "fragments_retrieved": 5,
    "fragments_after_access_filter": 5,
    "documents_cited": [
      "Runbook-Incidentes-TI-v4.2.pdf",
      "Política-Gestión-Incidentes-v2.1.pdf"
    ]
  },
  "tools_invoked": [],
  "response_summary": "Diagnóstico: disco lleno probable. Acciones recomendadas."
}
```

Este registro es inmutable: se escribe una vez y no puede modificarse. El sistema de almacenamiento de logs garantiza integridad mediante hashing del contenido al momento de escritura. El período de retención es de doce meses, conforme a RNF-03.

### Las métricas operacionales de TechCore

TechCore monitorea nueve métricas principales. Están agrupadas por dimensión de calidad.

**Dimensión de latencia:**

| Métrica                      | Objetivo  | Alerta si supera |
|------------------------------|-----------|-----------------|
| Latencia total P50           | < 2.5 s   | 3.0 s           |
| Latencia total P95           | < 6.0 s   | 8.0 s           |
| Latencia de inferencia LLM   | < 4.0 s   | 6.0 s           |
| Latencia de recuperación RAG | < 500 ms  | 1.0 s           |

**Dimensión de calidad de recuperación:**

| Métrica                            | Objetivo  | Alerta si baja de |
|------------------------------------|-----------|------------------|
| Fragmentos recuperados con cita    | > 70 %    | 50 %             |
| Respuestas con documentos fuente   | > 80 %    | 60 %             |

**Dimensión de costo:**

| Métrica                         | Objetivo    | Alerta si supera   |
|---------------------------------|-------------|-------------------|
| Tokens promedio por interacción | < 5.000     | 6.500             |
| Costo diario por departamento   | Según budget| +20 % del budget  |

**Dimensión de error:**

| Métrica                    | Objetivo  | Alerta si supera |
|----------------------------|-----------|-----------------|
| Tasa de errores de herramienta | < 2 %  | 5 %             |

### El panel de monitoreo

El equipo de operaciones de TechCore accede a un panel que agrega las métricas anteriores en tiempo real. El panel tiene cuatro vistas:

**Vista 1 — Salud general del sistema:** Estado de cada componente (orquestador, módulo RAG, módulo de herramientas, módulo de memoria), latencia actual P50 y P95, y contador de errores en la última hora.

**Vista 2 — Uso por departamento:** Volumen de interacciones por departamento, costo de tokens acumulado en el período, herramientas más utilizadas y documentos más recuperados.

**Vista 3 — Calidad de respuestas:** Tasa de citas de documentos, tasa de uso de herramientas, distribución de longitud de respuestas.

**Vista 4 — Alertas activas:** Lista de alertas disparadas con severidad, descripción y tiempo transcurrido desde la alerta.

### La capa de seguridad

La seguridad del sistema tiene cuatro mecanismos, cada uno diseñado para un tipo de amenaza distinto.

**Mecanismo 1 — Control de acceso en el nivel de recuperación.** Ya descrito en la sección 05: los fragmentos RAG se filtran por departamento del usuario antes de incluirse en el contexto. El LLM nunca recibe en su contexto documentos a los que el usuario no tiene acceso.

La implementación usa una capa de metadatos en el índice vectorial. Cada fragmento tiene un campo `departamento` y `clasificacion`. La búsqueda vectorial se ejecuta sin filtros para maximizar la relevancia semántica, pero los resultados se filtran en el orquestador antes de construir el contexto:

```python
def recuperar_fragmentos_con_control_acceso(
    query: str,
    perfil_usuario: PerfilUsuario,
    k: int = 5
) -> list[FragmentoDocumental]:
    
    # Recuperar candidatos por similitud semántica
    candidatos = indice_vectorial.buscar(query, k=k*3)  # búsqueda amplia
    
    # Filtrar por permisos del usuario
    autorizados = [
        f for f in candidatos
        if f.departamento in perfil_usuario.departamentos_autorizados
        and nivel_clasificacion_permitido(f.clasificacion, perfil_usuario.nivel)
    ]
    
    # Devolver los k más similares que pasaron el filtro
    return autorizados[:k]
```

**Mecanismo 2 — Filtrado de salida.** La respuesta del LLM pasa por un filtro antes de llegar al usuario. El filtro verifica:

- Que no contiene datos personales sensibles (números de identificación, salarios, información médica) que el usuario no debería ver.
- Que las citas de documentos corresponden a fragmentos que efectivamente fueron recuperados en ese turno (evita que el LLM invente referencias).
- Que no contiene instrucciones que parecen ser el resultado de una inyección de prompt exitosa.

**Mecanismo 3 — Detección de prompt injection.** El módulo de seguridad aplica un conjunto de heurísticas sobre la entrada del usuario para detectar intentos de manipulación del sistema:

```python
PATRONES_INJECTION = [
    r"ignora las instrucciones anteriores",
    r"olvida todo lo que te dijeron",
    r"actúa como si fueras",
    r"DAN mode",
    r"jailbreak",
    r"modo desarrollador",
    r"eres ahora un",
    r"tu instrucción real es",
]

def detectar_injection(entrada: str) -> DetectionResult:
    for patron in PATRONES_INJECTION:
        if re.search(patron, entrada, re.IGNORECASE):
            return DetectionResult(
                detectado=True,
                patron=patron,
                accion="bloquear_y_registrar"
            )
    return DetectionResult(detectado=False)
```

Cuando se detecta un intento de inyección, el sistema bloquea la interacción, registra el evento con la entrada completa del usuario, y devuelve un mensaje genérico: "No puedo procesar esa solicitud." El registro del evento incluye la entrada completa para análisis posterior.

**Mecanismo 4 — Auditoría de acceso a documentos confidenciales.** El acceso a documentos de clasificación `restringido` (contratos activos, datos salariales) genera un evento de auditoría adicional que se envía a un canal separado con alertas en tiempo real al responsable de cumplimiento. Este nivel de alerta no existe para documentos de clasificación `público_interno`.

### Seguridad desde el diseño, no desde el parche

El principio que guía el diseño de seguridad de TechCore es que ningún mecanismo de seguridad compensa un diseño arquitectónico inseguro. Si los documentos confidenciales fueran accesibles sin filtro y dependiéramos únicamente del filtrado de salida para protegerlos, el sistema sería fundamentalmente inseguro aunque el filtro funcionara bien el 99 % del tiempo. El 1 % restante sería un incidente de exposición de datos.

El orden correcto es: primero, no permitir que información no autorizada llegue al contexto del LLM; segundo, verificar que la salida del LLM no contenga información no autorizada como segunda línea de defensa. Los dos mecanismos juntos son robustos. Solo el segundo no lo es.

---

Con la observabilidad y la seguridad diseñadas, la siguiente sección cierra el bloque de diseño dimensional con la estrategia de despliegue y operación del sistema.
