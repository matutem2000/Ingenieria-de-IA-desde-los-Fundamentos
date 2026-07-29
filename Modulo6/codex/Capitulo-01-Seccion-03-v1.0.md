# Módulo 6 – Capítulo 01 – Sección 03

# El ciclo de vida de un documento en un sistema RAG

Un documento ingresa al sistema RAG como un archivo binario o texto crudo y experimenta una serie de transformaciones deterministas hasta convertirse en un conjunto de vectores indexados disponibles para consulta. El ciclo comienza con la extracción del contenido mediante parsers especializados (Unstructured.io, PyMuPDF, Docling) que manejan formatos complejos como PDFs con columnas o tablas; el texto resultante pasa por un pipeline de limpieza que elimina caracteres irrelevantes, normaliza espaciados y separa secciones lógicas. La segmentación divide el texto limpio en chunks con parámetros de tamaño y overlap configurables, y a cada chunk se le adjuntan metadatos de procedencia (nombre del archivo, número de página, fecha de ingesta, identificador único). Finalmente, cada chunk es embeddido mediante el modelo de embedding seleccionado, y el par (vector, metadatos) se persiste en la base vectorial, con un hash del contenido que permite detectar duplicados y actualizaciones incrementales.

## Fases del ciclo de vida de un documento

- Extracción: parsers como PyMuPDF o Unstructured.io convierten el binario en texto plano preservando la estructura semántica del documento original (títulos, listas, tablas)
- Limpieza y normalización: eliminación de ruido (encabezados y pies de página repetidos, caracteres de control), normalización unicode y detección de idioma para enrutamiento a modelos de embedding específicos
- Chunking: segmentación en fragmentos de 256–1024 tokens con overlap de 10–20%, balanceando precisión de recuperación y completitud de contexto en cada fragmento
- Enriquecimiento de metadatos: adjuntar a cada chunk información de procedencia estructurada (source, page, section, created_at, doc_id) para habilitar filtrado posterior en tiempo de consulta
- Embedding y persistencia: generación del vector de representación semántica mediante el modelo de embedding y escritura atómica en la base vectorial con ID reproducible basado en hash del contenido
- Gestión del ciclo de actualización: detección de cambios mediante comparación de hashes, eliminación del vector obsoleto e inserción del vector actualizado, manteniendo consistencia del índice

## Idea central

El ciclo de vida de un documento determina la calidad del índice: errores en extracción o limpieza propagan degradación a todos los chunks derivados y no pueden corregirse en tiempo de recuperación.
