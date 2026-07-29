# Módulo 6 – Capítulo 04 – Sección 04

# Enriquecimiento de chunks: metadatos, resúmenes y jerarquías de contexto

El enriquecimiento de chunks extiende el chunk indexado más allá del texto crudo del fragmento, añadiéndole información estructurada que mejora tanto la precisión de recuperación como la calidad de la generación. Los metadatos estructurados adjuntados a cada chunk (nombre del archivo, número de página, sección, subsección, fecha de creación, autor, versión del documento) habilitan filtrado preciso en tiempo de búsqueda y atribución de fuentes en las respuestas del LLM. Una técnica de enriquecimiento especialmente efectiva es la "contextual retrieval" publicada por Anthropic en 2024: para cada chunk, se genera un breve contexto de 50–100 tokens usando un LLM que describe el rol del fragmento dentro del documento completo ("Este fragmento forma parte de la sección de contraindicaciones del medicamento X y describe los efectos adversos en pacientes con insuficiencia renal"); este contexto se prepende al chunk antes de generar el embedding, mejorando el Recall@20 en hasta 49% según los experimentos de Anthropic. La indexación jerárquica o parent-document indexing mantiene chunks pequeños para recuperación precisa pero los vincula a sus chunks padres (o documentos completos) que se envían al LLM como contexto, combinando la precisión de la recuperación de chunks pequeños con la riqueza contextual de fragmentos más grandes.

## Técnicas de enriquecimiento de chunks

- Metadatos de procedencia: adjuntar source_file, page_number, section_title, document_type, created_date, document_id a cada chunk; habilitan filtrado por metadatos en búsqueda y atribución automática de fuentes en respuestas del LLM
- Contextual retrieval (Anthropic, 2024): generar con Claude Haiku un párrafo de contexto de 50–100 tokens por chunk que describe el rol del fragmento dentro del documento completo; prepender el contexto al chunk antes de embedir; mejora Recall@20 en 35–49% con un costo adicional de ~$1 por 1M tokens usando claude-3-haiku-20240307
- Resúmenes de chunk: para chunks de más de 256 tokens, generar un resumen de 1–3 oraciones con un LLM y usarlo como texto alternativo para el embedding; el vector del resumen es más específico que el vector del chunk completo para queries cortas; indexar ambos vectores permite dual retrieval
- Indexación jerárquica (parent-child): indexar chunks de 128 tokens para recuperación precisa y mantener referencia al chunk padre de 512 tokens y al documento completo; al recuperar, devolver el chunk padre al LLM en lugar del chunk hijo; implementado en LlamaIndex como `ParentDocumentRetriever`
- Title prepending: para documentos con título significativo (artículos, contratos, reportes), prepender el título del documento a cada chunk antes de generar el embedding; mejora la recuperación cuando la query menciona el nombre del documento o su tema principal
- Hypothetical questions indexing: generar para cada chunk 3–5 preguntas hipotéticas que el chunk podría responder (usando un LLM) e indexar las preguntas en lugar del chunk; en búsqueda, la similitud entre la query del usuario y las preguntas hipotéticas es mayor que con el texto directo del chunk

## Principio rector

El enriquecimiento de chunks es una inversión en calidad de índice con retorno medible: cada técnica de enriquecimiento añade costo de ingesta pero mejora el Recall@K de forma sistemática y cuantificable; evaluar el ROI de cada técnica sobre el dataset de evaluación antes de incluirla en el pipeline de producción.
