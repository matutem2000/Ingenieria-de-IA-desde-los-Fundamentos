# Módulo 12 – Capítulo 03 – Sección 01

# Diseño del pipeline de ingesta: fuentes de datos, parsers y pipeline de procesamiento

El pipeline de ingesta es la primera capa del sistema RAG y determina la calidad de la base de conocimiento sobre la que opera el agente. Las fuentes de datos del proyecto incluyen documentación técnica en Markdown (archivos .md en repositorios Git), especificaciones de API en OpenAPI YAML, runbooks en Confluence exportados como HTML, y ADRs en formato Markdown; cada tipo de fuente requiere un parser específico porque la estructura del texto condiciona la calidad del chunking posterior. El parser de Markdown usa el árbol AST para preservar la jerarquía de headings como metadatos (h1, h2, h3) que se almacenan en el payload de Qdrant y permiten filtrar por sección. El pipeline de procesamiento es asíncrono, tolerante a fallos y usa hashing SHA-256 del contenido para detectar documentos duplicados o sin cambios, evitando re-indexaciones innecesarias que incrementan el costo de embedding.

## Componentes del pipeline de ingesta

- Detectores de fuente: conectores para Git (PyGithub), Confluence (atlassian-python-api) y filesystem local con detección de tipo MIME
- Parsers: LlamaParse para PDF, python-markdown para Markdown con preservación de AST, BeautifulSoup para HTML de Confluence
- Deduplicación: hash SHA-256 por documento con registro en tabla PostgreSQL de documentos procesados para evitar re-indexación
- Queue de procesamiento: Celery + Redis para procesamiento asíncrono con retry exponencial y dead-letter queue para fallos persistentes
- Normalización: limpieza de whitespace, eliminación de artefactos de exportación y normalización de encoding a UTF-8

## Para recordar

La calidad del pipeline de ingesta determina el techo de calidad del sistema RAG — ninguna mejora en retrieval o generación puede compensar una base de conocimiento fragmentada, ruidosa o desactualizada.
