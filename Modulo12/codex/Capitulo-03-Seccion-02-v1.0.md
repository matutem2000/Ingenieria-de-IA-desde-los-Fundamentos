# Módulo 12 – Capítulo 03 – Sección 02

# Estrategia de chunking implementada: parámetros, validación y métricas de calidad

La estrategia de chunking del proyecto implementa un enfoque híbrido: chunking recursivo por caracteres como estrategia base, con chunking semántico por párrafos como fallback para documentos con estructura markdown bien definida. El RecursiveCharacterTextSplitter de LangChain se configura con chunk_size=512 tokens, chunk_overlap=64 tokens y separadores en orden de prioridad: doble salto de línea, salto de línea, punto, espacio; este orden preserva la coherencia semántica al mantener párrafos completos siempre que sea posible. Para documentos de código técnico (fragmentos de runbooks con comandos), se usa un CodeTextSplitter que respeta los bloques de código delimitados por backticks, evitando cortar un fragmento de código en el medio. La validación de calidad del chunking mide tres métricas: distribución de tamaños de chunk (desviación estándar < 100 tokens), ausencia de chunks truncados a mitad de oración, y context precision RAGAS sobre el golden dataset.

## Parámetros de chunking validados

- chunk_size: 512 tokens medidos con tiktoken cl100k_base, seleccionado por maximizar context precision en evaluación RAGAS
- chunk_overlap: 64 tokens (12.5% del chunk size) para preservar contexto en boundaries sin duplicar información en exceso
- Separadores: ["\n\n", "\n", ".", " "] en orden descendente de prioridad para preservar estructura semántica del documento
- Metadatos por chunk: source_url, document_type, section_heading, chunk_index, document_hash, ingested_at
- Validación post-chunking: rechazo de chunks < 50 tokens (fragmentos sin contenido semántico suficiente para retrieval)

## Buena práctica

Los parámetros de chunking deben validarse sobre un conjunto de documentos representativos del dominio real — los valores por defecto de los frameworks rara vez son óptimos para un caso de uso específico.
