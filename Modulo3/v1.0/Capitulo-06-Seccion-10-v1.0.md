# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 10 — Caso de estudio completo

> *"Un caso de estudio no es un tutorial. Es la demostración de que las decisiones de diseño tienen consecuencias concretas, y de que las mismas herramientas pueden producir sistemas excelentes o sistemas deficientes según cómo se use el criterio."*

---

## Objetivos de aprendizaje

- Aplicar los conceptos del capítulo a un escenario empresarial realista y concreto.
- Analizar y justificar cada decisión de diseño en función de los requisitos del negocio.
- Identificar las diferencias entre un diseño RAG naive y un diseño RAG robusto para el mismo problema.
- Comprender cómo los requisitos de acceso, actualización y trazabilidad moldean la arquitectura.

---

## El problema: asistente de consultas normativas para una firma de servicios financieros

Una firma de servicios financieros con 800 empleados en cuatro países (Argentina, Chile, México y España) necesita un asistente interno que responda consultas sobre:

- Normativa regulatoria aplicable por país (CNBV, CNMV, CMF, CNV).
- Procedimientos internos de compliance.
- Políticas de riesgo de crédito.
- Contratos marco con contrapartes.

El contexto determina los requisitos:

1. La normativa cambia con frecuencia: actualizaciones regulatorias ocurren varias veces al año.
2. Los documentos tienen distintos niveles de confidencialidad: algunos contratos solo pueden verlos los socios; las políticas generales las puede ver todo el personal.
3. La normativa varía por país: un analista en Chile no debería recibir como primera respuesta la regulación de México.
4. La firma necesita trazabilidad: cuando el sistema cita una normativa, el compliance officer debe poder verificar qué versión del documento fue la fuente.

---

## Decisión 1: ¿RAG o fine-tuning?

El corpus normativo cambia varias veces al año. La trazabilidad es un requisito explícito. La información es tanto pública (normativa regulatoria) como privada (contratos internos). Fine-tuning no produce trazabilidad y no puede actualizarse sin reentrenar.

**Decisión:** RAG como mecanismo principal de acceso al conocimiento. Fine-tuning no está descartado para una segunda fase donde se quiera ajustar el tono formal y la estructura de las respuestas del modelo, pero no es el punto de partida.

---

## Decisión 2: Chunking

Los documentos del corpus tienen características distintas:

- **Normativa regulatoria:** documentos estructurados por artículos numerados. Cada artículo es una unidad semántica completa. → Chunking por artículo.
- **Procedimientos internos:** documentos en prosa con secciones numeradas. → Chunking semántico por sección, con solapamiento del 15% para preservar la coherencia entre secciones contiguas.
- **Contratos:** estructura legal con cláusulas. → Chunking por cláusula. Cada cláusula se almacena con referencia a las cláusulas que la condicionan (metadato `clausulas_relacionadas`).

El tamaño máximo de chunk se establece en 400 tokens, compatible con el modelo de embedding seleccionado.

---

## Decisión 3: Modelo de embedding

El corpus contiene documentos en español de cuatro variedades (rioplatense, chilena, mexicana, peninsular) y terminología legal y financiera especializada. Un modelo de embedding general en inglés no es adecuado.

Opciones evaluadas:
- **mE5-large (multilingual):** buen rendimiento en español, entrenado con corpus multilingüe que incluye texto legal.
- **text-embedding-3-large de OpenAI:** alto rendimiento general, disponible vía API, texto enviado a terceros.
- **BGE-M3:** modelo de código abierto con soporte multilingüe, ejecutable localmente.

Dado que el corpus incluye contratos confidenciales que no deben enviarse a APIs externas, se selecciona **BGE-M3 ejecutado localmente**. El costo de infraestructura es mayor, pero el requisito de privacidad es no negociable.

---

## Decisión 4: Base vectorial

Requisitos:
- Filtrado por metadatos (país, nivel de acceso, tipo de documento).
- Búsqueda híbrida (los usuarios a veces buscan por número de artículo exacto).
- Soporte para actualización incremental.
- Equipo de operaciones pequeño: no se puede gestionar un clúster distribuido complejo.

**Decisión:** Qdrant ejecutado en contenedor Docker. Soporta filtrado avanzado por metadatos, búsqueda híbrida (dense + sparse) y actualización incremental sin downtime. El volumen del corpus (estimado en 50.000 fragmentos) es manejable con una instancia única bien dimensionada.

---

## Decisión 5: Metadatos del índice

Cada fragmento se indexa con:

```json
{
  "fuente": "CNBV_Circular_2024_003_art_42",
  "tipo": "normativa",
  "pais": "MX",
  "organismo": "CNBV",
  "fecha_publicacion": "2024-03-15",
  "fecha_vigencia": "2024-04-01",
  "nivel_acceso": "todos",
  "version": "1.0",
  "clausulas_relacionadas": ["art_38", "art_41"]
}
```

---

## Decisión 6: Estrategia de recuperación

El sistema implementa búsqueda híbrida porque los usuarios a veces preguntan por número de artículo exacto ("¿qué dice el artículo 42 de la circular CNBV?") y a veces por concepto ("¿qué requisitos de capital mínimo aplican a fondos de inversión?").

El retrieval aplica pre-filtro por `pais` (determinado a partir del perfil del usuario autenticado) y por `nivel_acceso` (determinado a partir de los roles del usuario). Sobre el subconjunto filtrado, se ejecuta búsqueda híbrida con Reciprocal Rank Fusion.

Se recuperan los top 20 candidatos, que pasan a la etapa de re-ranking.

---

## Decisión 7: Re-ranking

Dos criterios de re-ranking se aplican en secuencia:

1. **Re-ranking semántico** con un cross-encoder fine-tuneado para texto legal en español (BGE Reranker). Produce una puntuación de relevancia más precisa que la similitud vectorial para consultas con condiciones específicas.

2. **Re-ranking temporal**: fragmentos de documentos publicados en los últimos 12 meses reciben una bonificación del 20%. Fragmentos de documentos de más de 36 meses reciben una penalización del 40%. Esto refleja la dinámica regulatoria del sector.

Los top 5 fragmentos tras el re-ranking se insertan en el contexto del modelo.

---

## Decisión 8: Política de actualización del índice

La normativa regulatoria se actualiza mediante un proceso batch diario que consulta los repositorios oficiales de cada organismo regulatorio. Cuando se detecta un documento nuevo o modificado, el proceso:

1. Elimina del índice todos los fragmentos del documento anterior (identificados por `fuente`).
2. Procesa el nuevo documento (chunking, embedding).
3. Agrega los nuevos fragmentos con los metadatos actualizados.
4. Registra el evento en el log de auditoría.

Los documentos internos se actualizan mediante webhook: cuando un documento se modifica en el sistema de gestión documental interno, se dispara la reindexación automática.

---

## Decisión 9: Trazabilidad

Cada respuesta del sistema incluye, junto al texto generado, una lista de las fuentes utilizadas:

```
Respuesta: Los fondos de inversión que operen en México están sujetos a
un requisito de capital mínimo de [X] según la normativa vigente...

Fuentes:
  [1] CNBV Circular 2024-003, Art. 42 (publicado 2024-03-15, vigente desde 2024-04-01)
  [2] CNBV Circular 2023-019, Art. 38 (publicado 2023-09-01)
```

Esta trazabilidad está implementada recuperando los metadatos de los fragmentos usados en el contexto y formateándolos como parte de la respuesta. El compliance officer puede verificar que la cita corresponde a la versión correcta del documento.

---

## Resultado: diferencias entre el diseño naive y el diseño robusto

| Dimensión | Diseño naive | Diseño robusto |
|---|---|---|
| Chunking | Por tamaño fijo (500 chars) | Por artículo/sección/cláusula según tipo de documento |
| Filtrado por país | Ausente | Pre-filtro por país del usuario autenticado |
| Control de acceso | Ausente | Filtrado por nivel de acceso en el retrieval |
| Re-ranking | Ausente (top-k directo) | Cross-encoder + temporal |
| Actualización del índice | Manual, ad hoc | Batch diario + webhook |
| Trazabilidad | Ausente | Metadatos de fuente en cada respuesta |
| Búsqueda | Solo dense | Híbrida (dense + sparse) |

La diferencia no está en el modelo de lenguaje —ambos sistemas usarían el mismo modelo— sino en las decisiones de ingeniería que rodean al modelo.

---

## Ideas clave

- Los requisitos de negocio (privacidad, trazabilidad, multijurisdicción) determinan las decisiones de arquitectura RAG, no las preferencias tecnológicas.
- Un sistema RAG empresarial robusto no se diferencia del naive en el modelo sino en el diseño del pipeline completo.
- La política de actualización del índice debe diseñarse desde el primer día, no como una mejora futura.
- La trazabilidad de fuentes es un requisito frecuente en dominios regulados y debe planificarse desde la arquitectura.

---

## Transición hacia la siguiente sección

El caso de estudio describe decisiones. La siguiente sección convierte esas decisiones en experiencia práctica: el laboratorio práctico propone construir un pipeline RAG mínimo viable, desde la ingesta hasta la evaluación de los fragmentos recuperados.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
