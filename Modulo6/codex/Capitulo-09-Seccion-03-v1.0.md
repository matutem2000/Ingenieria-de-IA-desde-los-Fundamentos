# Módulo 6 – Capítulo 09 – Sección 03

# Compresión de contexto: reducir tokens sin perder información relevante

La compresión de contexto aborda el trade-off fundamental entre la calidad de la recuperación (más chunks = más Recall) y el costo y latencia de la generación (más tokens de contexto = mayor costo de inferencia y mayor latencia); el objetivo es maximizar la información relevante en el contexto del LLM mientras se minimiza el número de tokens utilizados. Los chunks recuperados contienen frecuentemente información irrelevante para la query específica: un chunk de 500 tokens sobre un proceso legal puede contener la respuesta a la query en 2 oraciones, rodeada de 450 tokens de contexto adicional que el LLM debe procesar pero que no aportan información adicional para la respuesta. LongContextReorder de LangChain reordena los chunks para poner los más relevantes al inicio y al final del contexto (donde la atención del LLM es mayor) y los menos relevantes en el centro, explotando el "lost-in-the-middle" effect documentado por Liu et al. (2023). ContextualCompression de LangChain implementa compresión activa: usa un LLM pequeño (claude-3-haiku, gpt-4o-mini) o un extracto basado en embeddings para filtrar de cada chunk solo las oraciones o párrafos que son relevantes para la query específica, reduciendo el texto del contexto en un 40–70% sin perder la información clave.

## Técnicas de compresión de contexto

- LLMChainExtractor: usa un LLM pequeño y económico (GPT-4o-mini: $0.15/M tokens, claude-3-haiku: $0.25/M tokens) para extraer de cada chunk solo las oraciones que responden a la query; reduce el contexto 40–70%; overhead de latencia de 200–400ms adicionales por chunk; implementado en LangChain como `LLMChainExtractor`
- EmbeddingsFilter: alternativa más rápida que usa la similitud coseno entre el embedding de la query y el embedding de cada oración del chunk para filtrar; retiene solo las oraciones con similitud > threshold; más rápido que LLMChainExtractor (sin latencia de LLM adicional) pero con menor precisión en la extracción
- LongContextReorder: reordena los chunks para poner los más relevantes en posición 1 y posición K (inicio y fin del contexto), y los menos relevantes en posiciones centrales; no reduce el número de tokens pero mejora la capacidad del LLM de prestar atención a la información más relevante sin comprimir nada
- Sentence-level chunking con agregación: en lugar de comprimir chunks grandes, usar chunks a nivel de oración (1–2 oraciones por chunk) en la indexación y agregar los chunks más similares en grupos coherentes para el contexto; combina recuperación granular con contexto coherente
- Token budget management: implementar un presupuesto máximo de tokens de contexto (por ejemplo, 3000 tokens para el contexto recuperado) y seleccionar los top chunks que caben dentro del presupuesto después del reranking; si los chunks seleccionados superan el presupuesto, comprimir el más largo con LLMChainExtractor
- Sliding window context: para queries que requieren información de documentos muy largos, usar una ventana deslizante que evalúa múltiples segmentos del documento y selecciona el segmento de mayor relevancia; evita chunking arbitrario que puede cortar la respuesta en el límite del chunk

## Buena práctica

Implementar compresión de contexto después de establecer el pipeline base de recuperación y medir primero el impacto sin compresión; la compresión añade latencia y costo adicionales de LLM que solo se justifican si el sistema tiene restricciones severas de tokens de contexto o de costo por inferencia.
