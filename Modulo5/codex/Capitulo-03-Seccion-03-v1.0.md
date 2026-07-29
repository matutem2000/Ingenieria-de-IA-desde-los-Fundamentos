# Módulo 5 – Capítulo 03 – Sección 03

# LlamaIndex: orientado a RAG, índices, query engines y conectores de datos

LlamaIndex (anteriormente GPT Index) está diseñado específicamente para el patrón RAG (Retrieval-Augmented Generation): su abstracción central no es la cadena sino el índice, una estructura que organiza documentos para recuperación eficiente mediante búsqueda semántica, por palabras clave o híbrida. El flujo canónico de LlamaIndex tiene tres etapas: ingesta de datos (`SimpleDirectoryReader`, `PDFReader`, conectores de Notion, Slack, bases de datos SQL), indexación (`VectorStoreIndex` con embeddings sobre Qdrant, Pinecone, Chroma o pgvector), y consulta mediante un `QueryEngine` que orquesta la recuperación y síntesis de respuesta. Los `QueryEngine` permiten estrategias avanzadas de recuperación: `RetrieverQueryEngine` con `VectorIndexRetriever` para búsqueda semántica, `RouterQueryEngine` para seleccionar entre múltiples índices según la naturaleza de la pregunta, y `SubQuestionQueryEngine` que descompone preguntas complejas en subpreguntas sobre diferentes fuentes de datos. La abstracción `NodeParser` controla cómo se divide el documento en chunks para indexación, con opciones como `SentenceSplitter` (por oraciones), `SemanticSplitter` (por similitud semántica) y `MarkdownNodeParser` para documentos estructurados.

## Componentes principales de LlamaIndex

- `SimpleDirectoryReader`: carga documentos de un directorio con detección automática de tipo (PDF, DOCX, TXT, HTML, Markdown), devolviendo objetos `Document` con texto y metadata extendida
- `VectorStoreIndex`: indexa documentos generando embeddings con el modelo configurado (`text-embedding-3-small`, `embed-multilingual-v3.0` de Cohere, etc.) y los almacena en el vector store configurado, con persistencia automática si se especifica `persist_dir`
- `QueryEngine.query()`: recibe una pregunta en lenguaje natural, ejecuta la recuperación de los `top_k` nodos más relevantes, construye el prompt de síntesis y devuelve un objeto `Response` con la respuesta y las fuentes citadas
- `RetrieverQueryEngine` con `SimilarityPostprocessor`: filtra los nodos recuperados por umbral de score de similitud coseno antes de pasarlos al modelo de síntesis, reduciendo ruido en la respuesta
- `IngestionPipeline`: define un pipeline de transformaciones sobre los documentos (extracción de metadata, chunking, generación de embeddings) que puede ejecutarse de forma incremental, procesando solo los documentos nuevos o modificados

## Principio rector

LlamaIndex brilla en aplicaciones donde los datos son la fuente principal de variabilidad y el patrón es recuperar-sintetizar; para flujos que priorizan la lógica de negocio sobre los datos, LangChain o implementación directa son más apropiados.
