# Módulo 4 – Capítulo 08 – Sección 04

## Optimización de Costos

El costo operativo de un sistema de IA en producción puede ser sorprendentemente alto si no se gestiona activamente. Un sistema que realiza 100.000 consultas diarias con un contexto promedio de 10.000 tokens de entrada y 500 tokens de salida, usando un modelo de precio medio, puede generar una factura mensual de decenas de miles de dólares solo en costos de inferencia. A esto se suman los costos de la base vectorial, el almacenamiento, la red, los servicios de soporte y la infraestructura de GPU si el equipo opera sus propios modelos. La optimización de costos no es una consideración secundaria: es una dimensión de diseño que debe abordarse desde la arquitectura.

**Selección del modelo por tipo de tarea** es la palanca de optimización de mayor impacto. No todas las tareas en un sistema de IA requieren el modelo más potente. Una taxonomía de tareas por complejidad permite asignar cada tipo de consulta al modelo de menor costo que produce calidad aceptable:

- **Modelos de alta capacidad** (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro): reservados para razonamiento complejo, síntesis de múltiples fuentes, generación de documentos largos, y cualquier tarea donde la calidad del output es crítica.
- **Modelos de capacidad media** (GPT-4o mini, Claude 3 Haiku, Gemini Flash): adecuados para la mayoría de las consultas de soporte, respuestas basadas en RAG con contexto bien recuperado, y síntesis de documentos cortos.
- **Modelos ligeros y especializados**: para tareas de clasificación, extracción de entidades, generación de embeddings, reranking, y cualquier tarea que pueda resolverse con un modelo fine-tuned más pequeño.

El enrutamiento inteligente entre modelos — usar el modelo ligero por defecto y escalar al modelo potente solo cuando la complejidad lo requiere — puede reducir el costo de inferencia entre un 40% y un 70% en sistemas con distribución mixta de consultas.

**Continuous batching** es la técnica más importante para maximizar la eficiencia de GPU en infraestructura propia. Un modelo LLM servido de forma ingenua procesa una solicitud a la vez, con la GPU esperando mientras el cliente envía la siguiente solicitud. El continuous batching agrupa dinámicamente múltiples solicitudes en un solo forward pass de la GPU, maximizando su utilización. Servidores como vLLM y TGI implementan continuous batching de forma nativa, y pueden aumentar el throughput de GPU por un factor de 5-10x respecto al serving naive.

**Caché de KV (Key-Value cache)** es una técnica específica para sistemas con prefijos de prompt repetitivos. En un sistema de soporte donde el system prompt es idéntico para todas las consultas, la KV cache de ese prompt puede reutilizarse entre solicitudes, evitando el cómputo repetido del prefijo compartido. OpenAI ofrece Prompt Caching con descuento en tokens de prefijo repetidos. Anthropic tiene funcionalidad equivalente en su API. vLLM implementa prefix caching a nivel de infraestructura propia.

**Caché semántico de respuestas** (descrito en la sección de balanceo) es la técnica de mayor impacto en sistemas con distribución de consultas concentrada. En sistemas de soporte con preguntas frecuentes, un caché semántico bien calibrado puede eliminar el 30-50% de las llamadas al LLM, con un ahorro proporcional en costo de inferencia.

**Procesamiento batch para el pipeline de ingesta** reemplaza la indexación de documentos en tiempo real (costosa en GPU) por procesamiento batch programado (que puede ejecutarse en horarios de menor demanda o en hardware más económico). El pipeline de ingesta — extracción, limpieza, chunking, embedding — no tiene requisitos de latencia en tiempo real: puede ejecutarse en lotes cada hora, cada día o en cada actualización del repositorio de documentos. Ejecutar este procesamiento en instancias spot de AWS, preemptible VMs de GCP, o Spot VMs de Azure reduce el costo entre un 50% y un 80% respecto a instancias on-demand.

**Right-sizing de la infraestructura** es la práctica de ajustar el tamaño de cada instancia a la carga real que procesa. Muchos sistemas se despliegan con instancias sobredimensionadas "por si acaso" y operan con utilización media del 15-20%. Monitorear la utilización real durante varias semanas y redimensionar según el percentil P95 de la demanda — en lugar del pico máximo histórico — puede reducir costos de infraestructura significativamente sin impacto en la experiencia del usuario.

> **Nota del Arquitecto:** El error más costoso que he visto en sistemas de IA productivos es usar el modelo más poderoso disponible para todas las consultas porque "es el que da mejores resultados en las demos". En producción, el 80% de las consultas son suficientemente simples como para que un modelo de categoría media las resuelva con la misma calidad percibida por el usuario. Implementar el enrutamiento por complejidad en el primer mes de operación es la optimización de mayor retorno disponible.

La optimización de costos debe ser una práctica continua, no una iniciativa puntual. Los costos del sistema de IA deben monitorearse semanalmente, con alertas cuando el costo por consulta aumenta por encima de la línea base, y revisiones trimestrales de la arquitectura de costos a medida que los volúmenes de uso cambian y los precios de los proveedores evolucionan.
