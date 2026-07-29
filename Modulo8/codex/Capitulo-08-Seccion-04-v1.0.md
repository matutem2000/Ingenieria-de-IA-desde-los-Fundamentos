# Módulo 8 – Capítulo 08 – Sección 04

# Prompt caching en servidores locales: reutilización del KV cache entre peticiones

El prompt caching (también llamado prefix caching o KV cache reuse) es la técnica de almacenar y reutilizar el KV cache computado para prefijos de prompt que se repiten entre peticiones distintas, eliminando el costo de prefill para el segmento compartido y reduciendo tanto la latencia como el uso de compute. En aplicaciones multi-usuario con system prompts largos (500-2000 tokens que describen el comportamiento del asistente, instrucciones de formato y contexto de la empresa), el prefix caching puede reducir la latencia del TTFT en un 40-70% y el compute de prefill en 50-80% cuando la mayoría de las peticiones comparten el mismo system prompt. vLLM implementa prefix caching con la opción `--enable-prefix-caching`: cuando dos requests tienen un prefijo idéntico en los primeros K tokens (donde K debe ser múltiplo del block_size del KV cache, por defecto 16), vLLM reutiliza los bloques de KV cache del prefijo compartido sin recomputarlos. llama.cpp también soporta prompt caching: el estado del KV cache se puede serializar a disco con `--save-cache-kv` y restaurar al inicio de una sesión con `--load-cache-kv`, permitiendo que conversaciones largas reanuden sin recomputar el historial completo; esta funcionalidad es especialmente valiosa para RAG con contextos de recuperación largos que se actualizan raramente.

## Implementaciones y consideraciones del prefix caching

- Requisitos para el cache hit: en vLLM, el prefix caching es automático cuando los prefijos son idénticos token a token y la cuantización de tokens (block_size=16) alinea el límite del prefijo compartido; textos ligeramente distintos (un espacio, mayúscula) producen un miss completo
- Granularidad del cache: vLLM opera a nivel de bloque (16 tokens por defecto); un prefijo compartido de 512 tokens ocupa 32 bloques del KV cache; estos bloques se almacenan y recuperan como unidad atómica; la fragmentación de bloques entre requests que comparten solo parte del prefijo es mínima por el diseño de PagedAttention
- LLM caching a nivel de aplicación: para respuestas a preguntas frecuentes o queries idénticas, el caching de la respuesta completa (semantic cache con Redis o similares) es más efectivo que el prefix caching; herramientas como GPTCache implementan similarity search para servir respuestas en caché cuando la nueva query es semánticamente similar a una anterior
- Radix tree para prefix sharing: vLLM usa un Radix Tree para gestionar los bloques de KV cache compartidos entre requests; cada nodo del árbol representa un bloque de 16 tokens; peticiones con prefijos diferentes se separan en el árbol y comparten solo los bloques de los prefijos comunes
- Cache warming en inicio de servidor: para aplicaciones con system prompts fijos, es recomendable enviar una request de warmup al iniciar el servidor de inferencia para pre-computar y cachear el KV del system prompt; todas las requests posteriores se benefician del cache hit inmediatamente

## Para recordar

El prefix caching es la optimización de mayor impacto con menor complejidad de implementación para aplicaciones con system prompts largos compartidos entre usuarios: activa `--enable-prefix-caching` en vLLM y asegura que el system prompt sea idéntico entre peticiones para maximizar el hit rate.
