# Módulo 6 – Capítulo 01 – Sección 02

# Arquitectura básica de RAG: ingesta, indexación, recuperación y generación

Un sistema RAG canónico se descompone en cuatro etapas secuenciales que operan sobre planos de tiempo distintos: la ingesta y la indexación son procesos offline o near-realtime que preparan el corpus, mientras que la recuperación y la generación son operaciones online que responden cada consulta del usuario en tiempo de inferencia. La etapa de ingesta transforma documentos crudos (PDFs, HTML, bases de datos) en chunks de texto mediante loaders y splitters como los de LangChain o LlamaIndex; la indexación convierte esos chunks en vectores mediante un modelo de embedding y los almacena en una base vectorial como Pinecone, Qdrant o pgvector. En tiempo de consulta, el retriever convierte la query del usuario en un vector de embedding, ejecuta una búsqueda ANN (Approximate Nearest Neighbor) en el índice, y devuelve los K chunks más similares. Finalmente, esos chunks se concatenan al prompt del LLM como contexto adicional mediante un template estructurado, y el generador produce la respuesta fundamentada en la evidencia recuperada.

## Componentes principales de la arquitectura RAG

- Document loaders: parsers específicos por tipo de fuente (PyMuPDF para PDFs, BeautifulSoup para HTML, connectors de bases de datos) que extraen texto plano y metadatos estructurados
- Text splitters: algoritmos de chunking que segmentan el texto en unidades indexables; RecursiveCharacterTextSplitter de LangChain es el estándar de facto para texto libre no estructurado
- Embedding models: modelos como text-embedding-3-small (OpenAI) o voyage-3 (Voyage AI) que proyectan chunks de texto a vectores densos en espacios de alta dimensionalidad (256–3072 dimensiones)
- Vector store: base de datos especializada que persiste los vectores y sus metadatos asociados, y expone una interfaz de búsqueda por similitud coseno o producto punto con filtrado por atributos
- Retriever: componente que ejecuta la query de búsqueda vectorial, aplicando opcionalmente filtros de metadatos y reranking, y retorna los top-K chunks con sus scores de similitud
- Prompt template: plantilla que estructura la inyección del contexto recuperado junto a la pregunta del usuario, definiendo el formato y las instrucciones que recibe el LLM generador para responder con fidelidad

## Principio rector

La separación en etapas offline (ingesta/indexación) y online (recuperación/generación) es el principio arquitectónico que permite escalar el corpus a millones de documentos sin impacto en la latencia de inferencia.
