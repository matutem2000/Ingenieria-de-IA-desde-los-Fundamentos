# Módulo 8 – Capítulo 03 – Sección 05

## Limitaciones del despliegue local: concurrencia, latencia y gestión de memoria

Ollama y llama.cpp son herramientas extraordinariamente efectivas para lo que están diseñadas: desarrollo individual, evaluación de modelos y serving para un número pequeño de usuarios concurrentes. La pregunta que todo equipo que ha tenido éxito con Ollama en desarrollo enfrenta en algún momento es: ¿puede este mismo stack servir a 100, 1.000 o 10.000 usuarios simultáneos? La respuesta técnica es no, sin cambios arquitectónicos significativos, y entender por qué es importante para no construir sobre una base que no escala.

La limitación más fundamental de Ollama en el contexto de múltiples usuarios simultáneos es la gestión del KV cache. Cada petición activa al servidor de inferencia requiere su propio KV cache: para un modelo Llama 3 8B con contexto de 4096 tokens en FP16, cada petición adicional en paralelo consume aproximadamente 1 GB de VRAM para el KV cache solamente, sobre los 4.1 GB de los pesos del modelo. Con `OLLAMA_NUM_PARALLEL=4`, cuatro peticiones simultáneas requieren 4 GB de KV cache adicionales. En una GPU de 16 GB de VRAM con el modelo Q4_K_M cargado (~4.1 GB), esto deja apenas 12 GB para KV cache, permitiendo a lo sumo 12 peticiones paralelas —y eso asumiendo que el contexto de cada petición es de exactamente 4096 tokens, lo que en la práctica no ocurre de forma uniforme.

Sin `OLLAMA_NUM_PARALLEL` configurado, el comportamiento por defecto de Ollama es procesar peticiones de forma secuencial: si dos usuarios envían peticiones simultáneas, la segunda espera en cola hasta que la primera termina completamente. En hardware típico de desarrollo (modelo 7B en CPU o GPU de 8 GB), el tiempo de generación de una respuesta completa puede ser de 10-30 segundos, lo que significa que el tercer usuario en cola puede estar esperando 60 segundos antes de que su petición comience a procesarse. Este patrón de cola FIFO es inaceptable para aplicaciones de producción con latencia perceptible por el usuario.

La latencia del primer token (TTFT) en hardware local es sistemáticamente superior a la de APIs de producción que operan con GPUs de datacenter. Un modelo de 7B en una RTX 3090 produce el primer token en 200-500ms en condiciones de carga ligera; los servicios de producción basados en H100 con vLLM pueden producirlo en 50-150ms bajo cargas similares. Esta diferencia de 2-4x en TTFT es perceptible en aplicaciones interactivas como autocompletado de código o asistentes de chat donde el usuario espera una respuesta inmediata al finalizar su mensaje.

Las limitaciones de gestión de memoria fuera de VRAM son igualmente importantes. En sistemas donde la GPU comparte hardware con otras aplicaciones (un portátil de desarrollo donde el usuario también tiene Chrome, IDEs y otras aplicaciones), los spikes de uso de VRAM de otras aplicaciones pueden provocar OOM errors en llama.cpp con caída del proceso de inferencia y pérdida de la sesión activa. Sin mecanismos de supervisión automática y reinicio del proceso, estos fallos se convierten en interrupciones del servicio que requieren intervención manual.

## Limitaciones técnicas del despliegue local

- **Concurrencia limitada:** sin `OLLAMA_NUM_PARALLEL`, una petición a la vez por modelo; incluso con paralelismo, el máximo práctico es 4-8 peticiones antes de que el KV cache agote la VRAM disponible.
- **Sin autoscaling horizontal:** Ollama no distribuye carga entre múltiples instancias nativamente; escalar requiere un proxy externo con round-robin sobre múltiples instancias.
- **Latencia de cold start:** cargar un modelo desde disco por primera vez tarda 5-30 segundos dependiendo del tamaño del modelo y la velocidad del almacenamiento.
- **Interferencia de memoria:** en sistemas con GPU compartida, spikes de otras aplicaciones pueden provocar OOM errors en llama.cpp con caída del servicio.
- **Ausencia de SLA y monitoreo integrado:** los despliegues locales no tienen garantías de disponibilidad ni métricas de Prometheus para alertas; cualquier implementación de producción real requiere wrappers adicionales.

> **Nota del Arquitecto:** Ollama con `OLLAMA_NUM_PARALLEL=4` es suficiente para un equipo de desarrollo de hasta 8-10 personas con uso no simultáneo. Para cualquier servicio de producción con usuarios reales, la respuesta correcta es vLLM —que se presenta en el Capítulo 5. El error más común que veo es intentar escalar Ollama con múltiples instancias manuales y balanceadores de carga caseros, cuando el motor de serving diseñado exactamente para eso ya existe y es de código abierto.

Entender dónde terminan las capacidades de Ollama y llama.cpp es tan importante como saber cómo usarlos: son las herramientas correctas para su caso de uso y las herramientas incorrectas para casos de uso de producción a escala. La sección de cierre sintetiza este aprendizaje y prepara la transición hacia los motores de serving de producción.

---
