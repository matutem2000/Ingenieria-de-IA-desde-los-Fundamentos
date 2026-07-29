# Módulo 8 – Capítulo 03 – Sección 02

# Ollama: gestión simplificada de modelos locales con API compatible con OpenAI

Ollama es una plataforma de gestión y serving de modelos locales que abstrae la complejidad de descarga, cuantización, configuración y ejecución de LLMs detrás de una CLI y una API HTTP idéntica a la de OpenAI, permitiendo que aplicaciones existentes que consumen la API de OpenAI migren a modelos locales cambiando únicamente el base URL. El comando `ollama run llama3` descarga automáticamente el modelo en formato GGUF desde el registro de Ollama (ollama.com/library), lo almacena en `~/.ollama/models/` y lanza un servidor local en `localhost:11434` con endpoints `/api/generate` y `/api/chat` que aceptan el mismo JSON que la API de OpenAI. Ollama gestiona el ciclo de vida del proceso de llama.cpp internamente: inicia el proceso al recibir la primera petición, mantiene el modelo cargado en memoria durante el tiempo de `OLLAMA_KEEP_ALIVE` (por defecto 5 minutos), y lo descarga automáticamente cuando el periodo de inactividad expira, liberando VRAM o RAM para otros procesos. La API `/api/tags` permite listar los modelos instalados y `/api/show` devuelve metadatos del modelo como arquitectura, tamaño, cuantización y el Modelfile activo.

## Componentes principales de Ollama

- Ollama CLI: comandos `pull`, `run`, `list`, `rm`, `show`, `create`, `push` y `cp` para gestionar el ciclo de vida completo de modelos; `ollama serve` inicia el servidor sin lanzar una sesión interactiva
- API REST: endpoint `/v1/chat/completions` compatible con el SDK de OpenAI permite reutilizar código existente; `openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` es suficiente para migrar
- Registro de modelos: ollama.com/library alberga versiones oficiales de los principales modelos (Llama, Mistral, Gemma, Phi, Qwen, CodeLlama); los tags permiten especificar variante y cuantización, e.g., `mistral:7b-instruct-q5_K_M`
- Detección automática de hardware: Ollama detecta GPUs NVIDIA (vía CUDA), AMD (vía ROCm en Linux) y Apple Silicon (Metal) y configura llama.cpp con los flags apropiados sin intervención manual del usuario
- Variables de entorno de configuración: `OLLAMA_NUM_PARALLEL` controla peticiones simultáneas, `OLLAMA_MAX_LOADED_MODELS` el número de modelos en memoria, `OLLAMA_HOST` la interfaz de red y `OLLAMA_ORIGINS` la política CORS

## Para recordar

Ollama reduce el despliegue de un LLM local a tres comandos: `ollama pull <modelo>`, `ollama serve` y una llamada HTTP al endpoint OpenAI-compatible, haciendo que la curva de entrada para modelos locales sea prácticamente plana.
