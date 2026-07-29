# Módulo 10 – Capítulo 05 – Sección 02

# Métricas de calidad: coherencia, fidelidad y relevancia medidas en producción

Medir la calidad de un LLM en producción es significativamente más complejo que medir la calidad de un modelo de clasificación o regresión: no existe una métrica escalar única equivalente al accuracy, y las métricas de referencia como BLEU o ROUGE, aunque útiles en benchmarks offline, tienen poca correlación con la percepción de calidad de los usuarios en producción. Las tres dimensiones de calidad más relevantes para LLMs en producción son: coherencia (si la respuesta es internamente consistente y libre de contradicciones), fidelidad o factual accuracy (si las afirmaciones del modelo son correctas respecto a los datos de referencia disponibles, especialmente crítico en sistemas RAG), y relevancia (si la respuesta aborda la pregunta o tarea del usuario de forma apropiada). Medir estas dimensiones en producción requiere uno de tres enfoques: evaluación con LLM-as-a-judge (usar un modelo más capaz como GPT-4 o Claude para evaluar las salidas del modelo de producción en una muestra estadística representativa), evaluación humana sobre muestras (Human Evaluation Pipeline con crowdworkers o evaluadores internos usando plataformas como Scale AI o Toloka), o métricas automáticas de proxy (ROUGE-L para relevancia, BERTScore para coherencia, factual consistency con NLI classifiers como TRUE o minicheck).

## Métricas de calidad para LLMs en producción

- Coherencia: evaluada con LLM-as-a-judge preguntando "¿es esta respuesta internamente consistente?" en escala 1-5; o con NLI classifier detectando auto-contradicciones entre sentencias de la respuesta
- Fidelidad/Grounding: en sistemas RAG, porcentaje de afirmaciones del modelo que pueden ser respaldadas por los documentos recuperados; medido con classifiers de factual consistency (minicheck, TRUE)
- Relevancia: similitud semántica entre la pregunta y la respuesta usando embedding cosine similarity; o evaluación con LLM-as-a-judge del grado en que la respuesta aborda la pregunta
- Toxicidad y safety: clasificadores especializados (Perspective API, Llama Guard, custom fine-tuned classifiers) aplicados a todas las salidas para detectar contenido dañino
- Task completion rate: para sistemas agentes o de múltiples turnos, porcentaje de conversaciones que resultan en completión exitosa de la tarea del usuario; medido con análisis de conversaciones o feedback explícito del usuario

## Buena práctica

Muestrear el 1-5% de todas las llamadas en producción para evaluación automática con LLM-as-a-judge proporciona una señal de calidad continua y estadísticamente significativa con un costo operativo manejable.
