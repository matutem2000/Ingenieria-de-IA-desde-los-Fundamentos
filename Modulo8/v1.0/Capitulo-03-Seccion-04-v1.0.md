# Módulo 8 – Capítulo 03 – Sección 04

## Integración con aplicaciones: SDKs, LangChain y llamadas HTTP directas

La compatibilidad de Ollama y llama.cpp server con la API de OpenAI no es un detalle de implementación sino la decisión de diseño que hace posible la integración sin fricciones con todo el ecosistema de herramientas construido alrededor de OpenAI. Cualquier librería, SDK o framework que use el patrón `openai.OpenAI(base_url=..., api_key=...)` puede apuntar a un servidor Ollama local simplemente cambiando esas dos configuraciones, sin modificar nada de la lógica de construcción de prompts, parseo de respuestas, gestión de streaming o función calling básica.

En Python, la migración más directa es a través del SDK oficial de OpenAI versión 1.0+. El código `client = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` reemplaza la clave de API de producción por la cadena literal `"ollama"` (ignorada por el servidor local) y redirige todas las peticiones al servidor Ollama. A partir de ese punto, `client.chat.completions.create(model="llama3:8b", messages=[...], stream=True)` funciona exactamente igual que la llamada equivalente a OpenAI, incluyendo streaming token por token con `stream=True`. Esta compatibilidad es especialmente valiosa para los sistemas de agentes del Módulo 7, donde los frameworks como LangChain o LlamaIndex construyen sus pipelines sobre la interfaz de OpenAI y pueden redirigirse a modelos locales sin refactorizar.

LangChain ofrece dos integraciones nativas con Ollama: `from langchain_community.llms import Ollama` para el patrón de completion simple, y `from langchain_ollama import ChatOllama` para el patrón de conversación con mensajes. `ChatOllama(model="llama3:8b", temperature=0.7)` implementa la interfaz `BaseChatModel` de LangChain, lo que significa que es compatible con toda la maquinaria del ecosistema: `LCEL` pipelines con el operador `|`, `RunnablePassthrough` para pasar contexto, `StrOutputParser` para parseo de respuestas, y las cadenas de RAG estándar de LangChain como `RetrievalQA` o `ConversationalRetrievalChain`. Para embeddings locales que completen el stack RAG sin llamadas externas, `OllamaEmbeddings(model="nomic-embed-text")` genera embeddings en el mismo servidor local.

LlamaIndex, el framework alternativo para RAG y agentes, soporta Ollama con `from llama_index.llms.ollama import Ollama` y `from llama_index.embeddings.ollama import OllamaEmbedding`. La compatibilidad permite construir query engines, agentes con herramientas y sistemas de memoria conversacional completamente locales: desde la generación de embeddings hasta la inferencia final, sin ninguna llamada a servicios externos. Este stack completamente local es el escenario ideal para prototipar aplicaciones con datos sensibles antes de decidir qué componentes, si los hay, se moverán a la nube en producción.

Para integración desde lenguajes distintos a Python, o cuando se quiere el máximo control sin dependencias adicionales, las llamadas HTTP directas son la opción más portable. El endpoint `/api/chat` acepta un JSON con `model`, `messages` y `stream`: con `"stream": true`, la respuesta llega como líneas NDJSON donde cada línea es un objeto JSON con el campo `message.content` conteniendo el fragmento de texto del siguiente token. Esta interfaz funciona desde cualquier lenguaje con soporte HTTP: JavaScript con `fetch()`, Go con `net/http`, Rust con `reqwest`, o incluso `curl` para testing rápido desde terminal.

## Patrones de integración

- **SDK de OpenAI redirigido:** `openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` migra código existente sin cambios; soporta streaming, function calling básico y model listing.
- **LangChain ChatOllama:** compatible con la interfaz `BaseChatModel`; soporta `invoke()`, `stream()`, `batch()` e integración completa con LCEL pipelines.
- **LlamaIndex con Ollama:** backend nativo para query engines y agentes; `OllamaEmbedding` para embeddings locales en pipelines RAG completamente sin API externa.
- **HTTP directo con streaming:** el endpoint `/api/generate` con `"stream": true` devuelve NDJSON; útil para integración desde lenguajes sin SDK oficial de OpenAI.
- **Endpoint de embeddings:** `/api/embeddings` con `{"model": "nomic-embed-text", "prompt": "texto"}` devuelve el vector de embedding; permite RAG completamente local.

> **Nota del Arquitecto:** La decisión más práctica para un equipo que ya usa LangChain o LlamaIndex con OpenAI es añadir una variable de entorno `LLM_BASE_URL` que apunte a Ollama en desarrollo y a la API de producción en staging/producción. Un único cambio de configuración permite a todo el equipo trabajar localmente sin costos de API durante el desarrollo, con la misma base de código que corre en producción.

La compatibilidad con la API de OpenAI elimina el lock-in en el código de aplicación y convierte la decisión local vs nube en una cuestión de configuración, no de arquitectura. La sección siguiente examina las limitaciones estructurales del despliegue con Ollama que determinan cuándo esta solución es suficiente y cuándo se requiere un motor de serving más potente.

---
