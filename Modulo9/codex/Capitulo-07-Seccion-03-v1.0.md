# Módulo 9 – Capítulo 07 – Sección 03

# Input validation: sanitización y límites de longitud antes de llegar al modelo

La validación de inputs en sistemas de IA tiene dos objetivos distintos que frecuentemente se confunden: la seguridad (prevenir ataques de prompt injection, context flooding y otros abusos) y la calidad del servicio (asegurar que los inputs están en el formato esperado y dentro de los límites operacionales del sistema). La validación de seguridad no puede limitarse a pattern matching contra listas de palabras clave o frases prohibidas: esta estrategia es eludible trivialmente mediante sinónimos, idiomas alternativos, codificaciones o fragmentación del ataque en múltiples messages. La validación efectiva combina controles estructurales (longitud máxima de input, formato requerido, validación de schema para inputs estructurados) con controles semánticos usando modelos de clasificación especializados (LlamaGuard, Azure Content Safety, Prompt Guard de Meta) que analizan el intent del input. Un aspecto frecuentemente ignorado es la validación de la longitud del input en tokens (no solo en caracteres), porque el costo de procesamiento del modelo escala con los tokens, no con los bytes, y un texto corto en caracteres puede ser extremadamente largo en tokens para ciertos modelos y tokenizadores.

## Aspectos técnicos

- Límites de longitud en tokens: tokenizar el input antes de enviarlo al modelo y rechazar inputs que superen el límite máximo definido (que debe ser menor al context window del modelo para dejar espacio para el system prompt y la respuesta esperada); usar el tokenizador específico del modelo (tiktoken para modelos OpenAI, tokenizador de Anthropic para Claude) porque los conteos de tokens varían entre modelos para el mismo texto
- Validación estructural: si la aplicación acepta inputs estructurados (JSON, formularios, XML), validar el schema del input antes de incluirlo en el prompt; prevenir inyección de campos adicionales o modificación de la estructura esperada que podría alterar la interpretación del modelo
- Clasificación semántica del input: LlamaGuard-3 (Meta, disponible en Hugging Face) es un modelo de 8B parámetros fine-tuned para clasificar inputs y outputs contra 13 categorías de contenido dañino con F1 score superior al 80% en la mayoría de las categorías; Azure Content Safety API proporciona una alternativa gestionada con menor latencia de implementación
- Detección de patterns de prompt injection: Prompt Guard (Meta, 2024) es un modelo BERT-based fine-tuned específicamente para detectar intentos de prompt injection directa e indirecta, con baja latencia (<10ms) que permite su inclusión en el hot path de cada request
- Sanitización de contenido antes de RAG: los documentos que ingresan al pipeline de ingestión del vectorstore deben pasar por validación de contenido con las mismas herramientas que se aplican al input del usuario — un documento malicioso en el corpus es tan peligroso como un prompt malicioso

## Para recordar

La validación de input para sistemas de IA no puede basarse únicamente en reglas de filtering basadas en texto —son trivialmente eludibles— sino que debe combinarse con clasificadores semánticos especializados (LlamaGuard, Prompt Guard) y controles estructurales (límites de tokens, validación de schema) que juntos forman la primera línea de defensa del sistema.
