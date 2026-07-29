# Módulo 7 – Capítulo 02 – Sección 01

# Chain-of-Thought (CoT): pensamiento paso a paso y sus variantes

Chain-of-Thought (CoT) es una técnica de prompting que mejora el rendimiento de los LLMs en tareas de razonamiento al instruir al modelo a generar pasos intermedios explícitos antes de producir la respuesta final, en lugar de mapear directamente el input al output. Introducida por Wei et al. (2022) en el paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", demostró mejoras de hasta 40-50% en benchmarks de aritmética (GSM8K) y razonamiento de sentido común (StrategyQA) para modelos de +100B parámetros. Las variantes principales incluyen Zero-Shot CoT (agregar "Let's think step by step" al prompt), Few-Shot CoT (proveer ejemplos de razonamiento completo en el contexto) y Auto-CoT (generar automáticamente los ejemplos de razonamiento usando el propio LLM). En el contexto agéntico, CoT es el mecanismo interno de razonamiento que antecede cada decisión de qué herramienta invocar o qué acción ejecutar.

## Conceptos clave

- **Zero-Shot CoT**: la adición de la instrucción "Let's think step by step" o su equivalente al final del prompt activa el modo de razonamiento en modelos de gran tamaño sin necesidad de ejemplos en el contexto
- **Few-Shot CoT**: proveer 3-8 ejemplos de (pregunta + cadena de razonamiento + respuesta) en el system prompt mejora la coherencia y el formato del razonamiento generado
- **Scratchpad**: espacio de texto interno donde el agente genera su razonamiento antes de tomar una decisión; en Anthropic Claude esto sucede en bloques `<thinking>` separados del output final visible
- **Faithfulness del razonamiento**: el razonamiento generado puede no reflejar el proceso real de inferencia del modelo; estudios muestran que modelos pueden llegar a la respuesta correcta con razonamientos post-hoc incorrectos
- **CoT en sistemas agénticos**: en frameworks como LangGraph y ReAct, el CoT ocurre antes de cada llamada a herramienta, permitiendo al agente articular por qué invoca una herramienta específica y con qué parámetros

## Principio rector

Chain-of-Thought no hace al modelo más inteligente; le permite usar mejor la capacidad de razonamiento que ya tiene, distribuyendo la carga computacional de inferencia a través de tokens intermedios explícitos en lugar de comprimirla en una sola predicción.
