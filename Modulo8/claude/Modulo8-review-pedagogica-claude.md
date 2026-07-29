# Informe Pedagógico — Módulo 8: Modelos Locales e Infraestructura
**Revisado por:** Director Pedagógico / Claude  
**Fecha:** 2026-07-25  
**Muestra analizada:** 42 secciones de 60 totales (secciones 01, 02, 03, 04, 05 y 06 de capítulos seleccionados; muestra completa de secciones 01, 03 y 06 de los 10 capítulos)

---

## Síntesis ejecutiva

El Módulo 8 es el módulo más técnicamente denso del libro hasta ahora y uno de los más prácticos. Cubre con solidez el ecosistema de modelos open weights, cuantización, herramientas de inferencia local, hardware, serving de producción, fine-tuning eficiente, infraestructura cloud, optimización de inferencia, gobierno del ciclo de vida y arquitecturas híbridas. La precisión técnica es consistentemente alta: cifras concretas, flags reales, formulas aplicables, nombres exactos de herramientas y librerías. El esqueleto estructural está bien construido y el autor podrá desarrollarlo con seguridad.

Sin embargo, el módulo tiene **tres problemas de fondo**: (1) un orden de capítulos que genera adelantos de conceptos no introducidos aún, (2) la ausencia de un capítulo o sección dedicada a evaluación de modelos — la habilidad de elegir el modelo correcto para una tarea — que es la primera decisión que toma un AI Engineer, y (3) una articulación deficiente con los módulos adyacentes (7 y 9).

---

## 1. Fortalezas

### Progresión temática general sólida
El módulo sigue un arco lógico: qué son los modelos abiertos → cómo comprimir su footprint → cómo ejecutarlos localmente → en qué hardware → cómo servirlos en producción → cómo especializarlos → dónde alojar la infraestructura → cómo optimizar la inferencia → cómo gestionar el ciclo de vida → cuándo usar local vs nube. Este arco es correcto desde la perspectiva del AI Engineer que incorpora modelos locales a su stack.

### Precisión técnica excepcional
Los datos son concretos y actualizados para la fecha de escritura. Ejemplos: la fórmula de VRAM en Cap 4 Sec 02 (`parámetros × bits_cuantización / 8 / 1e9`), los rangos de throughput de llama.cpp en CPU (15-40 tokens/s para Q4_K_M), el análisis de PagedAttention con la cifra de 3-4x más requests concurrentes, los tiempos de compilación de TRT-LLM (30-90 minutos), y la penalización de velocidad de QLoRA (15-30% respecto a LoRA en BF16). Esta densidad técnica es exactamente lo que necesita un AI Engineer o Arquitecto de IA.

### Estructura interna de sección consistente y efectiva
El patrón introducción conceptual → bullets técnicos → "Para recordar" es pedagógicamente sólido y consistente en los 60 archivos. El "Para recordar" activa la memoria a largo plazo estableciendo la regla práctica más útil de cada sección. Los cierres de capítulo con cita técnica relevante añaden perspectiva histórica sin resultar forzados.

### Hilo conductor del KV cache bien construido
El KV cache aparece progresivamente en Cap 2 (costo de memoria de la cuantización), Cap 3 (gestión en llama.cpp), Cap 4 (fórmula de requisitos de VRAM), Cap 5 (PagedAttention en vLLM) y Cap 8 (prefix caching, chunked prefill, crecimiento del KV cache durante el decode). Este hilo conductor construye comprensión acumulativa en lugar de introducir el concepto una sola vez.

### Conexiones horizontales planificadas entre capítulos
El cierre de Cap 2 ya menciona QLoRA como prerequisito del fine-tuning eficiente, anticipando Cap 6. El cierre de Cap 3 menciona explícitamente vLLM como el siguiente paso más allá de Ollama, motivando Cap 5. Cap 6 Sec 01 establece la secuencia correcta (prompting → RAG → fine-tuning) que conecta con el Módulo 5. Estas conexiones demuestran que el módulo fue diseñado como sistema integrado, no como capítulos independientes.

### Capítulo 9 (gobierno del ciclo de vida) es una fortaleza diferencial
El tratamiento del model registry, versionado, validación pre-despliegue, canary deployment y rollback en el Cap 9 es de un nivel de madurez que raramente aparece en libros técnicos de IA. La sección 9.03 sobre golden datasets y load tests pre-despliegue, y la 9.04 sobre canary y shadow mode son contenido de alta calidad que diferencia este libro de los tutoriales superficiales. Esto prepara bien al lector para el módulo de seguridad (Módulo 9) que require procesos de governance maduros.

### Capítulo 6 (fine-tuning) tiene cobertura técnica completa
El capítulo cubre correctamente: cuándo no hacer prompting (Sec 01), LoRA con su matemática de bajo rango (Sec 02), QLoRA con NF4 y double quantization (Sec 03), preparación de datasets con chat template y loss masking (Sec 04), y herramientas concretas — Unsloth, Axolotl, LLaMA-Factory, TRL — con sus diferencias (Sec 05). Este es el capítulo más completo del módulo.

---

## 2. Debilidades

### Debilidad 1: Orden subóptimo en los primeros cuatro capítulos

**Capítulo 3 (llama.cpp/Ollama) aparece antes que Capítulo 4 (hardware)**, creando una inversión pedagógica. El Cap 3 Sec 01 introduce flags de llama.cpp (`--n-gpu-layers`, `--ctx-size`) y da cifras de throughput ("15 y 40 tokens por segundo dependiendo del número de capas") sin que el lector tenga aún el marco conceptual de hardware que le permita interpretar esas cifras. Cap 4 Sec 02 introduce las fórmulas de VRAM que debería haberse dado antes de usar `--n-gpu-layers`. El resultado es que el lector aprende a usar una herramienta antes de entender el recurso que gestiona.

Adicionalmente, Cap 4 Sec 01 repite parte del razonamiento sobre Apple Silicon y throughput que ya apareció implícito en Cap 3, y Cap 4 Sec 02 recalcula la VRAM de pesos que ya se estimó en Cap 2 Sec 01. La repetición no es suficientemente aditiva para justificarse pedagógicamente.

**Capítulo 6 (fine-tuning) aparece antes que Capítulo 7 (cloud GPU)**, lo que obliga al lector a aprender QLoRA y sus requisitos de hardware ("fine-tuning de modelos de 70B en una sola GPU A100 de 40 GB") sin haber recibido el contexto de dónde conseguir esa A100. La sección 6.05 menciona Axolotl con DeepSpeed y multi-GPU, pero el lector todavía no conoce los proveedores de GPU cloud (Cap 7) ni ha aprendido cómo containerizar el entorno (Cap 7 Sec 03). Esto produce adelantos de referencias no explicadas.

**Capítulo 8 (optimización de inferencia) está separado por dos capítulos del Capítulo 5 (vLLM)**, siendo Flash Attention y speculative decoding técnicas de optimización del mismo motor de serving presentado en Cap 5. El lector que termina Cap 5 no recibe las optimizaciones de ese motor hasta tres capítulos después. El Gap Caps 5→8 lo llena infraestructura cloud (Cap 7) y fine-tuning (Cap 6), que tienen menor afinidad técnica con las optimizaciones de serving.

### Debilidad 2: Ausencia de un capítulo o sección de evaluación y selección de modelos

El Cap 1 presenta las familias de modelos (Llama, Mistral, Gemma, Phi, Qwen) con sus características técnicas, pero **no incluye ninguna sección sobre cómo evaluarlos y elegir entre ellos para una tarea concreta**. La pregunta "¿qué modelo uso para mi caso de uso?" es la primera decisión de un AI Engineer al comenzar un proyecto con modelos locales, y el módulo no la responde metodológicamente.

No hay ninguna sección que cubra: `lm-evaluation-harness` como herramienta estándar de evaluación, benchmarks relevantes para distintas tareas (MMLU para conocimiento general, HumanEval para código, HellaSwag para razonamiento), diseño de evaluaciones domain-specific, o el proceso de comparación empírica entre modelos candidatos. Esta laguna es especialmente problemática porque el módulo instruye al lector en cuantizar, fine-tunear y desplegar modelos antes de enseñarle a seleccionarlos objetivamente.

### Debilidad 3: DPO/RLHF ausente como técnica de fine-tuning

Cap 6 Sec 05 menciona que TRL soporta DPO y RLHF pero no hay ninguna sección dedicada a explicar qué es DPO (Direct Preference Optimization), cuándo se prefiere sobre SFT supervisado, qué formato tiene un dataset de preferencias, y cómo ejecutarlo. En 2025-2026, DPO es la técnica principal de alignment y mejora de instruction following para modelos locales. Su ausencia como concepto standalone (no solo como mención de compatibilidad de librería) es una laguna significativa para un AI Engineer que quiere producir modelos alineados con comportamientos específicos.

### Debilidad 4: Fine-tuning distribuido y multi-GPU insuficientemente cubierto

Cap 7 Sec 04 menciona DeepSpeed ZeRO stages 2/3 a través de Axolotl, pero no hay una sección que explique sistemáticamente qué es ZeRO Stage 1/2/3, qué es FSDP (Fully Sharded Data Parallel), cómo funciona el model parallelism vs data parallelism, y cómo configurar un job de entrenamiento multi-nodo. Para modelos de 13B o más, el fine-tuning single-GPU no es viable incluso con QLoRA, y el lector no tiene las herramientas conceptuales para abordar este escenario.

### Debilidad 5: Triton Inference Server en el mismo capítulo que vLLM genera confusión de propósito

Cap 5 pone en el mismo nivel vLLM (la herramienta de default para producción GPU, de adopción masiva) y Triton Inference Server (plataforma empresarial multi-framework, de mayor complejidad operativa y caso de uso diferente). La sección 5.03 es técnicamente buena, pero introducirla en el mismo capítulo que vLLM sin una guía clara de "elige vLLM si X, elige Triton si Y" puede llevar al lector a pensar que son herramientas intercambiables. TRT-LLM en Sec 5.04 suma una tercera opción de serving en el mismo capítulo, complejizando aún más la decisión.

### Debilidad 6: Articulación deficiente con los módulos adyacentes

**Hacia el Módulo 7 (Ingeniería de Agentes):** El Cap 1 del Módulo 8 abre con "open weights vs open source" sin ninguna referencia al contexto del Módulo 7. El lector que terminó de construir sistemas de agentes con APIs de OpenAI/Anthropic no tiene una razón pedagógica explícita para comenzar a explorar modelos locales. La motivación natural existe (costo de loops agénticos, privacidad de datos que pasan por el agente, latencia en agentes de tiempo real) pero no se articula en el módulo. La compatibilidad de formatos de tool calling entre modelos locales (Llama 3 function calling format, Hermes format) y los frameworks de agentes del Módulo 7 tampoco se menciona.

**Hacia el Módulo 9 (AI Security Engineering):** El Cap 10 cierra el módulo sin ninguna referencia a las implicaciones de seguridad de desplegar modelos locales y fine-tuneados. Cuando el lector llegue al Módulo 9, encontrará que el attack surface de un sistema con modelos locales es diferente al de uno basado en APIs: data poisoning en el pipeline de fine-tuning, extracción de datos de entrenamiento mediante ataques de memorización, prompt injection en sistemas RAG con modelos locales, y gestión de versiones de modelos desde una perspectiva de seguridad. Una transición explícita haría el Módulo 9 más coherente.

---

## 3. Conceptos a ampliar

### 3.1 Evaluación y selección de modelos (laguna crítica — Cap 1 o capítulo nuevo)

Debe añadirse una sección completa (idealmente la Sección 04 del Cap 01, antes del paisaje del ecosistema) que cubra:
- `lm-evaluation-harness` de EleutherAI: instalación, benchmarks disponibles, cómo ejecutar evaluaciones locales
- Benchmarks relevantes por tipo de tarea: MMLU/MMLU-Pro (conocimiento general), HumanEval/MBPP (código), GSM8K/MATH (matemáticas), MT-Bench (instrucción multi-turno), BBH (razonamiento complejo)
- Construcción de un evaluation set domain-specific: 100-200 ejemplos representativos antes de seleccionar el modelo base
- Framework de decisión: modelo base vs instruction-tuned vs fine-tuned; tamaño vs calidad vs costo de inferencia
- Concepto de Pareto frontier en selección de modelos (calidad vs VRAM vs throughput)

### 3.2 DPO y técnicas de alignment (Cap 6, nueva sección entre Sec 03 y Sec 04)

Una sección dedicada que cubra:
- Qué problema resuelve DPO vs SFT: instrucción following mejorada, reducción de outputs no deseados, preferencia humana capturada sin RL
- Formato del dataset de preferencias: pares `chosen`/`rejected`, cómo construirlos con anotación humana o con LLM-as-judge
- Implementación con TRL `DPOTrainer`: configuración de `beta`, `max_length`, `max_prompt_length`
- ORPO como alternativa sin modelo de referencia: combinación de SFT loss y odds ratio preference loss en un solo paso
- Cuándo usar DPO vs SFT: SFT para conocimiento de dominio y formato, DPO para refinamiento de tono, seguridad y preferencias comportamentales

### 3.3 Multi-GPU training y distributed fine-tuning (Cap 6 o Cap 7, nueva sección)

Sección que explique:
- Data Parallelism vs Model Parallelism vs Pipeline Parallelism: conceptos y cuándo aplicar cada uno
- ZeRO Stage 1/2/3 de DeepSpeed: qué se fragmenta en cada stage (optimizer states, gradients, parameters) y qué memoria ahorra
- FSDP (Fully Sharded Data Parallel): alternativa nativa de PyTorch a DeepSpeed ZeRO; cuándo preferirlo
- Configuración de Axolotl para multi-GPU: el YAML de DeepSpeed, `accelerate config`, `torchrun --nproc_per_node`
- Multi-nodo: `--nnodes`, `--node_rank`, `--master_addr` en entornos cloud (AWS EFA, GCP Interconnect)

### 3.4 Model serving con múltiples adaptadores LoRA (Cap 5 o Cap 6, ampliar)

Cap 6 Sec 02 menciona `model.set_adapter("tarea_1")` y Cap 7 Sec 04 menciona `--enable-lora` en vLLM brevemente. Merece una sección dedicada:
- vLLM multi-LoRA serving: `--enable-lora --max-loras 4 --max-lora-rank 64`: cómo funciona, qué overhead introduce
- Hot-swapping de adaptadores: aplicaciones con múltiples personalidades o especializaciones sobre el mismo modelo base
- Fusión de adaptadores para producción: `merge_and_unload()` y sus implicaciones para distribución como GGUF
- Cuándo fusionar vs cuándo servir dinámicamente: trade-off entre flexibilidad y overhead de VRAM

### 3.5 CI/CD para modelos (Cap 9, ampliar Sec 02 o nueva sección)

Cap 9 menciona el golden dataset y el load test pero no detalla el pipeline de CI/CD:
- GitHub Actions workflow para evaluación automática en cada commit al adaptador LoRA
- Integración de `lm-evaluation-harness` como step de CI: falla el PR si la evaluación cae del umbral
- Automatización del push a registry post-aprobación: `huggingface_hub.upload_folder()` solo si pasan los gates
- Artifact versioning: asociar el hash del dataset, el hash del código de entrenamiento y el hash de la config al artefacto del modelo

### 3.6 Implicaciones de seguridad de modelos locales (Cap 10, ampliar cierre)

El cierre del módulo debería incluir un puente explícito hacia el Módulo 9:
- Memorización de datos de entrenamiento: riesgo de que el fine-tuning sobre datos propietarios permita extraer esos datos mediante prompts específicos
- Data poisoning en el pipeline de fine-tuning: qué hacer si el dataset de entrenamiento está comprometido
- Modelo fine-tuneado como superficie de ataque: jailbreaking de modelos fine-tuneados con safety training removido
- Control de acceso al modelo local: quién puede descargar los pesos fine-tuneados, cómo proteger los adaptadores LoRA con datos propietarios

---

## 4. Conceptos a resumir o eliminar

### 4.1 Duplicación de fórmulas de VRAM entre Cap 2 y Cap 4

Cap 2 Sec 01 presenta la estimación de memoria: "un modelo de 7B parámetros en BF16 requiere 14 GB de VRAM; el mismo modelo en INT4 ocupa aproximadamente 3.5 GB". Cap 4 Sec 02 re-deriva la misma fórmula: `VRAM_pesos (GB) = parámetros × bits_cuantización / 8 / 1e9`. La segunda instancia es más formal, pero no añade suficiente valor nuevo para justificar la repetición. La solución: en Cap 2, presentar la intuición y los ejemplos concretos. En Cap 4, SOLO añadir el componente del KV cache (que es genuinamente nuevo) y referenciar explícitamente la fórmula del Cap 2. Esto reduciría la Sec 02 del Cap 4 y la haría más enfocada.

### 4.2 Precios específicos en dólares de GPUs y cloud providers (Cap 4 y Cap 7)

Cap 4 Sec 03 incluye: "precio de mercado ~1.600 USD" para la RTX 4090. Cap 7 Sec 01 incluye: "los precios on-demand de una p5.48xlarge con 8 H100 superan los 98 USD/hora". Estos números se desactualizan en meses. El principio es durable; los números no. Recomendación: reemplazar los precios absolutos por comparativas relativas ("la RTX 4090 es el punto de entrada más económico entre las GPUs de 24 GB de VRAM de consumo; consulta los precios actuales en [fuente]") o por ratios de costo que permanecen más estables ("los proveedores especializados ofrecen A100 a 2-3x menor precio que los hiperescaladores en sus tarifas on-demand").

### 4.3 Detalle excesivo de Kubernetes en Cap 7 Sec 03

La sección sobre contenedores en Cap 7 Sec 03 baja al nivel de `nodeSelector: nvidia.com/gpu.product: A100-SXM4-80GB`, `runtimeClassName: nvidia`, y `livenessProbe` con `initialDelaySeconds: 120`. Este nivel de detalle de Kubernetes es operativo (pertenece a un runbook de plataforma) más que pedagógico para un AI Engineer. El contenido es correcto pero excede el nivel de abstracción del libro. Recomendación: condensar a los conceptos clave (GPU Device Plugin, resource requests/limits, PVC para modelos, health checks) y mover el YAML específico a un ejemplo de referencia separado o un apéndice.

### 4.4 Descripción de la cabecera GGUF (Cap 2 Sec 02)

Cap 2 Sec 02 incluye detalles del formato de archivo GGUF al nivel de "magic number `GGUF` de 4 bytes seguido de versión, número de tensores y número de pares de metadatos key-value". Para un AI Engineer, el formato binario interno de GGUF no tiene valor práctico inmediato — lo que importa es que el archivo es autónomo, multiplataforma y especifica cuantización. Este nivel de detalle pertenece a una referencia técnica del formato, no a un libro de ingeniería. Se puede condensar el bullet de cabecera a una descripción de una línea.

---

## 5. Recomendaciones editoriales

### Recomendación 1: Reordenar los capítulos para eliminar adelantos de conceptos
Propuesta de nuevo orden:
- Cap 01: Ecosystem (sin cambios)
- Cap 02: Quantization (sin cambios)
- **Cap 03 nuevo: Hardware** (actual Cap 04) — el lector necesita el marco de VRAM y hardware antes de aprender las herramientas que lo gestionan
- **Cap 04 nuevo: Local inference tools** (actual Cap 03) — ahora el `--n-gpu-layers` y los números de throughput tienen contexto
- **Cap 05 nuevo: Cloud GPU infrastructure** (actual Cap 07) — establece dónde ejecutar los workloads de producción y fine-tuning antes de enseñar ambos
- **Cap 06 nuevo: Production serving** (actual Cap 05) — el reader ya sabe qué hardware usar, en qué entorno
- **Cap 07 nuevo: Inference optimization** (actual Cap 08) — inmediatamente después del serving, las optimizaciones de ese motor
- **Cap 08 nuevo: Fine-tuning** (actual Cap 06) — el lector ya conoce el hardware y la infraestructura para ejecutarlo
- Cap 09: Model lifecycle (sin cambios)
- Cap 10: Hybrid architecture (sin cambios)

Este reordenamiento elimina los tres problemas de inversión pedagógica sin cambiar el contenido de ningún capítulo, solo su posición.

### Recomendación 2: Añadir una sección de evaluación y selección de modelos en Cap 01
Convertir la actual Sección 05 del Cap 01 (que en el esquema actual parece ser el puente entre familias de modelos y el cierre) en una sección de evaluación práctica. Cubrir: `lm-evaluation-harness`, benchmarks por tipo de tarea, cómo construir una evaluación domain-specific, y el framework de decisión modelo → cuantización → hardware. La Sección 06 mantiene su rol de cierre. Esta sección resuelve la Debilidad 2 sin añadir un capítulo nuevo.

### Recomendación 3: Añadir DPO como sección explícita en Cap 06 (o Cap 08 nuevo post-reorden)
Insertar una nueva sección entre la actual Sec 03 (QLoRA) y Sec 04 (Datasets): "DPO: fine-tuning por preferencias para alignment y mejora de instrucción following". El contenido mínimo: qué problema resuelve, formato del dataset (pares chosen/rejected), `DPOTrainer` de TRL con `beta=0.1`, y cuándo elegir DPO sobre SFT adicional.

### Recomendación 4: Consolidar el capítulo de serving (Cap 05 actual / Cap 06 nuevo) con una guía de selección de motor
Al inicio del capítulo, añadir una tabla de decisión explícita:
- Desarrollo local / prototipado → Ollama + llama.cpp
- Producción GPU, equipo pequeño, un tipo de modelo → vLLM
- Producción GPU, múltiples tipos de modelos (embeddings + LLM + clasificadores) → Triton con backends específicos
- Máxima eficiencia en NVIDIA, costo por token crítico → TRT-LLM

Sin esta guía, el lector que llega al capítulo no sabe en qué sección enfocarse.

### Recomendación 5: Añadir la apertura al Módulo 7 en Cap 01 Sec 01 o como introducción del módulo
Un párrafo introductorio que conecte con el Módulo 7: "Los agentes construidos en el módulo anterior consumen APIs de modelos propietarios. Este módulo te da las herramientas para reemplazar o complementar esas APIs con modelos que corren en tu propia infraestructura: con menor costo para loops de agentes de alto volumen, con privacidad para datos que no pueden salir del perímetro organizacional, y con latencia predecible para agentes de tiempo real." Esta motivación ancla el módulo en el trabajo previo del lector.

### Recomendación 6: Añadir la transición al Módulo 9 en Cap 10 Sec 06
Al final del cierre del módulo, un párrafo que anticipe el Módulo 9: "Desplegar modelos locales y fine-tuneados introduce superficies de ataque específicas que las arquitecturas API-first no tienen: los pesos de un modelo fine-tuneado sobre datos propietarios pueden ser objeto de ataques de extracción de memorización; el pipeline de entrenamiento puede ser comprometido con data poisoning; los modelos locales sin safety training son más vulnerables a jailbreaking. El Módulo 9 examinará estas superficies de ataque y las defensas correspondientes."

### Recomendación 7: Consolidar la fórmula de VRAM en un único lugar de referencia
Definir la fórmula completa (pesos + KV cache + overhead del framework) una sola vez en el capítulo de cuantización (Cap 02) con la nota de que el KV cache se detalla más en el capítulo de hardware. En Cap 04, referenciar la fórmula y añadir únicamente el componente nuevo (KV cache por petición paralela). Esto elimina la repetición y crea una sección de referencia canónica para el lector.

### Recomendación 8: Añadir una sección sobre entrenamiento distribuido en Cap 06 (o Cap 08 nuevo)
Una sección Sec 06 de "Distributed fine-tuning: ZeRO, FSDP y multi-GPU" antes del cierre del capítulo (o como penúltima sección). Cubrir: ZeRO Stage 1/2/3 como concepto, la configuración de Axolotl con `deepspeed_zero_stage: 3`, y cuándo se necesita multi-nodo (modelos >30B, datasets >500K ejemplos con sequence packing). La sección actual Sec 06 de cierre del capítulo se convierte en Sec 07.

### Recomendación 9: Reemplazar precios absolutos por principios de comparación relativa
En Cap 04 Sec 03 y Cap 07 Sec 01, eliminar los precios en USD y reemplazarlos con: categorías de costo relativo (consumo / profesional / datacenter), ratios de costo entre categorías, y una referencia a las páginas de pricing oficiales con nota editorial de actualización trimestral. Los principios de selección ("para inferencia local de producción, la GPU de 24 GB GDDR6X de la gama de consumo es el mejor punto de entrada; para producción escalable en la nube, los aceleradores HBM son el estándar") envejecen mejor que los números.

### Recomendación 10: Separar Triton del capítulo de serving o añadir guía de selección explícita
Dos opciones igualmente válidas: (a) mover Triton a Cap 09 (Lifecycle y Governance) como la herramienta de serving para entornos multi-modelo de enterprise, donde encaja conceptualmente con la madurez operativa; o (b) mantenerlo en el capítulo de serving pero añadir explícitamente en Sec 01 de ese capítulo la tabla de selección de herramienta (Recomendación 4 anterior) para que el lector sepa desde el inicio que Triton y vLLM tienen targets distintos y que puede leer selectivamente.

---

## 6. Evaluación por dimensión

### Progresión pedagógica de los 10 capítulos
**Calificación: 7/10**  
El arco general (ecosistema → compresión → herramientas → hardware → serving → especialización → infraestructura → optimización → governance → arquitectura híbrida) es lógico, pero el orden interno de los primeros cuatro capítulos genera inversiones conceptuales que el reordenamiento propuesto resolvería.

### Coherencia temática entre capítulos
**Calificación: 8/10**  
Los capítulos están bien conectados mediante referencias explícitas y el hilo conductor del KV cache. La mayor debilidad es la separación entre serving (Cap 5) y optimización de serving (Cap 8) por dos capítulos de distancia.

### Profundidad técnica del contenido
**Calificación: 9/10**  
Excepcionalmente alta para un formato de esqueleto. Los datos son concretos, los flags son reales, las herramientas son actuales. La única deducción es la ausencia de DPO y de distributed training como temas tratados con la misma profundidad que el resto.

### Articulación con Módulo 7 (Ingeniería de Agentes)
**Calificación: 4/10**  
La articulación es prácticamente inexistente. El módulo comienza sin ninguna referencia al trabajo previo del lector. La compatibilidad de formatos de tool calling y la motivación económica (costo de loops agénticos) no se mencionan.

### Articulación con Módulo 9 (AI Security Engineering)
**Calificación: 5/10**  
Cap 10 Sec 04 sobre privacidad diferencial es un buen puente parcial hacia la seguridad, pero no cierra el módulo con una transición explícita hacia los temas de seguridad específicos de modelos locales y fine-tuneados.

### Lagunas conceptuales críticas
- Evaluación y selección de modelos: **ausente**
- DPO/preference fine-tuning: **ausente como concepto standalone**
- Distributed training ZeRO/FSDP: **mencionado pero no explicado**
- CI/CD para modelos: **parcialmente cubierto en Cap 9 pero sin pipeline concreto**

---

*Informe generado sobre 42 secciones de 60 totales del Módulo 8. Secciones no leídas: secciones 04 y 05 de Capítulos 01, 02, 07, 09, 10 y sección 05 de Capítulo 08. La muestra analizada es representativa del módulo completo.*
