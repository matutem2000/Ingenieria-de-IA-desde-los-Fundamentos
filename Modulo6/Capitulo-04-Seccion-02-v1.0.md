# Módulo 6 – Capítulo 04 – Sección 02

# Estrategias de chunking: fijo, semántico, recursivo y por estructura del documento

Las estrategias de chunking van desde el enfoque más simple (dividir por número fijo de caracteres) hasta el más sofisticado (usar un LLM o modelo de segmentación semántica para identificar límites de ideas coherentes). El chunking por tamaño fijo o `CharacterTextSplitter` de LangChain divide el texto en segmentos de N caracteres sin considerar la estructura del contenido; es el método más rápido y predecible pero produce cortes en mitad de oraciones o párrafos que fragmentan unidades semánticas. El `RecursiveCharacterTextSplitter` mejora esto usando una jerarquía de separadores ("\n\n", "\n", ". ", " ") para intentar dividir en límites naturales del texto; es el método más utilizado en la práctica por su balance entre sencillez y calidad. El chunking semántico, implementado en LlamaIndex como `SemanticSplitterNodeParser`, usa el propio modelo de embedding para detectar cambios bruscos de similitud coseno entre oraciones consecutivas y coloca los límites de chunk en esos puntos de quiebre semántico; produce chunks más coherentes pero es computacionalmente costoso. El chunking por estructura del documento (Markdown, HTML, LaTeX, código) aprovecha los separadores explícitos del formato para dividir en secciones, subsecciones, bloques de código o celdas de tabla, produciendo chunks con cohesión garantizada por la estructura del autor.

## Estrategias de chunking con sus trade-offs

- Chunking por tamaño fijo (CharacterTextSplitter): parámetros chunk_size y chunk_overlap en caracteres; O(N) en tiempo; no considera estructura ni semántica; produce cortes arbitrarios que pueden partir oraciones; adecuado solo cuando el texto es muy homogéneo y ya está preprocesado
- RecursiveCharacterTextSplitter: usa jerarquía de separadores configurables; primero intenta dividir por "\n\n" (párrafos), luego "\n" (líneas), luego ". " (oraciones); mucho mejor que el fijo para texto natural; estándar de facto en LangChain para texto libre
- Chunking semántico (SemanticSplitterNodeParser): calcula similitud coseno entre oraciones consecutivas y coloca límites donde la similitud cae por debajo de un umbral; produce los chunks más cohesivos semánticamente pero requiere llamadas al modelo de embedding durante la ingesta, incrementando costo y tiempo de procesamiento
- Chunking por estructura (MarkdownHeaderTextSplitter, HTMLHeaderTextSplitter): extrae la jerarquía de headers del documento y divide respetando los límites de sección; propaga los headers como metadatos del chunk (H1, H2, H3) habilitando búsqueda jerárquica y filtrado por sección
- Parent-child chunking: estrategia de doble indexación donde chunks pequeños (128 tokens) se indexan para recuperación precisa y chunks grandes padres (512 tokens) se recuperan para proveer contexto al LLM; implementado en LlamaIndex como `ParentDocumentRetriever`
- Chunking por proposiciones: técnica avanzada que usa un LLM para segmentar el texto en proposiciones atómicas (unidades de conocimiento mínimas), indexar las proposiciones y recuperar el párrafo completo que las contiene; máxima precisión pero alto costo computacional en ingesta

## Buena práctica

Implementar siempre al menos dos estrategias de chunking y evaluarlas con el dataset de queries de producción antes de producción; la diferencia de Recall@5 entre una estrategia bien elegida y el default del framework puede ser de 10–15 puntos porcentuales.
