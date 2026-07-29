# Módulo 8 – Capítulo 03 – Sección 04

# Integración con aplicaciones: SDKs, LangChain y llamadas HTTP directas

La API HTTP de Ollama y llama.cpp server es intencionalmente compatible con la API de OpenAI, lo que significa que cualquier librería o SDK diseñado para consumir OpenAI puede redirigirse a un servidor local cambiando únicamente el parámetro `base_url`, sin modificar la lógica de construcción de prompts, parseo de respuestas o gestión de streaming. En Python, `from langchain_community.llms import Ollama` y `from langchain_ollama import ChatOllama` permiten usar modelos locales de Ollama directamente como `llm` en cualquier cadena o agente de LangChain, habilitando pipelines RAG, agentes con herramientas y memoria conversacional sobre infraestructura completamente local. El SDK oficial de OpenAI (`openai` >= 1.0) soporta la misma redirección: `client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` convierte cualquier código que use `client.chat.completions.create()` en una llamada al modelo local, manteniendo soporte para streaming con `stream=True` y structured outputs básicos. Para casos donde se requiere máximo control, las llamadas HTTP directas con `requests.post("http://localhost:11434/api/chat", json={...})` o `curl` permiten integración desde cualquier lenguaje sin dependencias adicionales.

## Patrones de integración

- SDK de OpenAI redirigido: `openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` es la forma más directa de migrar código existente; funciona con streaming, function calling básico y model listing vía `/v1/models`
- LangChain ChatOllama: `ChatOllama(model="llama3:8b", temperature=0.7)` es compatible con la interfaz `BaseChatModel` de LangChain; soporta `invoke()`, `stream()`, `batch()` y se integra con `RunnablePassthrough` y LCEL pipelines
- LlamaIndex con Ollama: `from llama_index.llms.ollama import Ollama` permite usar Ollama como backend en pipelines de LlamaIndex para RAG, query engines y agentes; compatible con los modelos de embedding locales vía `OllamaEmbedding`
- HTTP directo con streaming: el endpoint `/api/generate` con `"stream": true` devuelve líneas NDJSON donde cada línea es un objeto JSON con el campo `response` conteniendo el siguiente token; útil para integración en lenguajes sin SDK oficial de OpenAI
- Endpoint de embeddings: `/api/embeddings` acepta `{"model": "nomic-embed-text", "prompt": "texto"}` y devuelve el vector de embedding; permite construir pipelines RAG completamente locales sin llamadas a APIs externas

## Para recordar

La compatibilidad de Ollama con la API de OpenAI elimina el lock-in en el código de aplicación: el mismo código puede apuntar a GPT-4o en producción y a Llama 3 en desarrollo local con un cambio de una línea de configuración.
