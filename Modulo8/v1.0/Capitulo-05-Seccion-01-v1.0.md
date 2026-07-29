# Módulo 8 – Capítulo 05 – Sección 01

## Guía de selección y vLLM: PagedAttention y continuous batching para producción GPU

Antes de profundizar en los motores de serving de producción, es necesario establecer cuándo corresponde usar cada herramienta disponible. Las cuatro opciones principales del ecosistema de serving de LLMs tienen casos de uso primarios distintos y elegir el motor incorrecto resulta en complejidad innecesaria o rendimiento subóptimo:

| Escenario | Motor recomendado |
|-----------|-------------------|
| Desarrollo local / prototipado | Ollama + llama.cpp (Cap. 3) |
| Producción GPU, equipo pequeño, un tipo de modelo | vLLM |
| Producción GPU, múltiples tipos de modelos (embeddings + LLM + clasificadores) | Triton Inference Server con backends específicos |
| Máxima eficiencia en NVIDIA, costo por token crítico | TRT-LLM |

Esta guía evita que el lector profundice en el motor incorrecto para su caso de uso. Para la mayoría de los equipos que despliegan un único LLM en GPU para servir usuarios en producción, **vLLM es la elección correcta**.

---

vLLM es el motor de serving de LLMs de mayor adopción en producción GPU, desarrollado por el Sky Computing Lab de UC Berkeley, que resuelve el problema fundamental de la gestión ineficiente del KV cache mediante PagedAttention. El problema que vLLM ataca es concreto: los sistemas de inferencia tradicionales pre-reservan una región contigua de VRAM para el KV cache de cada request basada en la longitud máxima de contexto configurada, independientemente de si la request real usa esa longitud completa. Si configuras un contexto máximo de 8192 tokens y recibes peticiones que usan en promedio 1024 tokens, el 87% de la VRAM reservada para KV cache está siendo desperdiciada en fragmentación interna. Con 1.000 requests concurrentes posibles pero solo 100 activas en promedio, 900 "slots" de VRAM están vacíos pero bloqueados.

PagedAttention, el mecanismo central de vLLM, resuelve este desperdicio aplicando el mismo principio de paginación de memoria virtual que los sistemas operativos usan para la RAM física: divide el KV cache en bloques de tamaño fijo (páginas de 16 tokens por defecto) y los asigna dinámicamente desde un pool centralizado solo cuando son necesarios. Cuando una request termina, sus bloques de KV cache se liberan de vuelta al pool y quedan disponibles para nuevas requests sin necesidad de defragmentación. El resultado medido es que la fragmentación interna cae de 60-80% en implementaciones tradicionales a menos del 4% con PagedAttention, permitiendo servir 3-4x más peticiones simultáneas con el mismo hardware.

El continuous batching (también llamado iteration-level scheduling) complementa PagedAttention en la dimensión del tiempo. En sistemas de batching tradicionales, un batch se forma al inicio, se procesa hasta que todas las requests del batch terminan, y solo entonces se acepta el siguiente batch. Si el batch tiene una request que genera 2.000 tokens (larga) y otras nueve que generan 50 tokens (cortas), las nueve requests cortas terminan en fracciones del tiempo total, pero la GPU permanece "esperando" a la request larga con los slots de las requests cortas vacíos. Con continuous batching, en cada iteración de decode vLLM puede incorporar nuevas requests al batch activo: tan pronto como una request corta termina, su slot en el batch se rellena con la siguiente request en la cola, manteniendo la GPU ocupada de forma continua.

## Componentes técnicos de vLLM

- **PagedAttention:** KV cache dividido en bloques de 16 tokens asignados dinámicamente; reduce fragmentación interna a <4%; permite prefix caching compartiendo bloques entre requests con el mismo prefijo.
- **Continuous batching:** nuevas requests se incorporan al batch activo en cada iteración de decode; elimina el "bubble time" de GPU idle esperando que el batch completo termine.
- **Prefix caching:** cuando múltiples requests comparten el mismo system prompt o prefijo largo, vLLM comparte los bloques del KV cache entre todas; reduce el compute de prefill y el uso de VRAM.
- **Tensor parallelism:** `tensor_parallel_size=N` distribuye el modelo entre N GPUs con sharding de pesos; pipeline parallelism para modelos que no caben en multi-GPU tensor-parallel.
- **Gestión de memoria dinámica:** copy-on-write para beam search; garbage collector de bloques al finalizar requests; uso de VRAM predecible y máximo por diseño, sin memory leaks.

> **Nota del Arquitecto:** PagedAttention y continuous batching no son optimizaciones opcionales que se activan cuando se busca rendimiento extra —son la razón fundamental por la que vLLM existe. La diferencia entre Hugging Face Transformers en modo básico y vLLM con el mismo hardware puede ser de 5-10x en throughput agregado. Para cualquier sistema que sirva a más de 2-3 usuarios concurrentes, vLLM no es un lujo sino un requisito.

La arquitectura interna de vLLM y su mecanismo de PagedAttention establecen el fundamento sobre el que se construye todo el sistema de serving de producción. La sección siguiente detalla cómo configurar y desplegar vLLM como servidor de producción con API compatible con OpenAI.

---
