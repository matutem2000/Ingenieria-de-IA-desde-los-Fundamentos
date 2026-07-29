# Módulo 8 – Capítulo 03 – Sección 02

## Ollama: gestión simplificada de modelos locales con API compatible con OpenAI

La potencia técnica de llama.cpp tiene un precio: descargar el modelo correcto, identificar los flags de aceleración apropiados para el hardware, gestionar el ciclo de vida del proceso de inferencia y construir una API HTTP sobre él requieren trabajo de integración que no es trivial. Ollama resuelve exactamente esta fricción: es una plataforma de gestión y serving de modelos locales que convierte todo ese proceso en tres comandos y una llamada HTTP, sin sacrificar la flexibilidad técnica subyacente de llama.cpp.

El comando `ollama run llama3` desencadena una secuencia de operaciones automáticas: descarga el modelo en formato GGUF desde el registro oficial de Ollama en `ollama.com/library` con verificación de integridad, lo almacena localmente en `~/.ollama/models/`, detecta el hardware disponible (GPU NVIDIA via CUDA, AMD via ROCm en Linux, Apple Silicon via Metal), configura llama.cpp con los flags apropiados para ese hardware, y lanza un servidor HTTP local en `localhost:11434` con endpoints compatibles con la API de OpenAI. Todo esto ocurre transparentemente sin que el usuario especifique ningún parámetro de hardware o cuantización.

La compatibilidad con la API de OpenAI es el aspecto técnico más valioso de Ollama para equipos que ya tienen código existente. El endpoint `/v1/chat/completions` acepta exactamente el mismo JSON que la API oficial: `client = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` convierte cualquier aplicación que use el SDK de OpenAI en una aplicación que puede apuntar a modelos locales con un cambio de una línea. Esto significa que los sistemas de agentes del Módulo 7, los pipelines RAG construidos con LangChain y los prototipos de cualquier aplicación LLM pueden ejecutarse completamente localmente durante el desarrollo sin ningún cambio de código, reduciendo el costo de experimentación a cero.

La gestión del ciclo de vida del proceso de llama.cpp es otro aspecto donde Ollama aporta valor operativo. El servidor de Ollama mantiene el modelo cargado en memoria durante el tiempo configurado en `OLLAMA_KEEP_ALIVE` (por defecto 5 minutos) y lo descarga automáticamente cuando el período de inactividad expira, liberando VRAM o RAM para otros procesos. Para entornos de desarrollo compartido donde múltiples desarrolladores usan el mismo servidor, `OLLAMA_NUM_PARALLEL` permite configurar hasta 4 peticiones en paralelo sobre el mismo modelo, y `OLLAMA_MAX_LOADED_MODELS` permite mantener múltiples modelos en memoria simultáneamente, habilitando cambios de modelo sin tiempo de carga. El endpoint `GET /api/tags` lista los modelos instalados con su tamaño y fecha de descarga; `POST /api/show` devuelve la arquitectura, cuantización, template de chat y Modelfile activo de cualquier modelo instalado.

El registro de modelos de Ollama (`ollama.com/library`) organiza los modelos por familia con tags para variantes y cuantizaciones: `mistral:7b-instruct-q5_K_M` descarga exactamente la variante de instrucción de Mistral 7B en Q5_K_M, sin ambigüedad sobre qué archivo GGUF se está usando. Para modelos no disponibles en el registro oficial, el Modelfile (que se describe en la siguiente sección) permite crear entradas locales a partir de archivos GGUF descargados de Hugging Face u otras fuentes.

## Componentes principales de Ollama

- **Ollama CLI:** comandos `pull`, `run`, `list`, `rm`, `show`, `create`, `push` y `cp` para gestionar el ciclo de vida completo; `ollama serve` inicia el servidor sin lanzar una sesión interactiva.
- **API REST compatible con OpenAI:** el endpoint `/v1/chat/completions` permite reutilizar código existente sin modificaciones; soporte completo para streaming con SSE y model listing via `/v1/models`.
- **Registro de modelos:** `ollama.com/library` alberga versiones oficiales de Llama, Mistral, Gemma, Phi, Qwen, CodeLlama y otros; los tags permiten especificar variante y cuantización exacta.
- **Detección automática de hardware:** configura llama.cpp con los flags apropiados para NVIDIA, AMD o Apple Silicon sin intervención del usuario.
- **Variables de entorno de configuración:** `OLLAMA_NUM_PARALLEL` controla peticiones simultáneas; `OLLAMA_MAX_LOADED_MODELS` el número de modelos en memoria; `OLLAMA_HOST` la interfaz de red; `OLLAMA_ORIGINS` la política CORS para integraciones desde el navegador.

> **Nota del Arquitecto:** En entornos de equipo, desplegar un servidor Ollama centralizado en una máquina con una RTX 3090 o Apple M2 Max elimina la necesidad de que cada desarrollador descargue y gestione sus propios modelos. Un servidor único con `OLLAMA_HOST=0.0.0.0` y los modelos más usados pre-descargados reduce el tiempo de acceso a un modelo nuevo de "30 minutos de setup" a "0 segundos" para cada nuevo miembro del equipo.

Ollama reduce el despliegue de un LLM local a comandos comprensibles y una API estándar, democratizando el acceso a inferencia local para cualquier desarrollador independientemente de su familiaridad con CUDA o los detalles de llama.cpp. La sección siguiente explica cómo personalizar el comportamiento del modelo usando Modelfiles para ir más allá de los valores por defecto.

---
