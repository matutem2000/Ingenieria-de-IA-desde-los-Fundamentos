# Módulo 11 – Capítulo 07 – Sección 03

# Model routing enterprise: combinar modelos de bajo costo para tareas simples con modelos premium para tareas complejas

El model routing enterprise es la práctica de seleccionar dinámicamente el modelo de LLM más apropiado para cada petición individual basándose en la complejidad estimada de la tarea, el requisito de calidad del caso de uso, y el costo objetivo por petición — evitando el anti-patrón de enviar todas las peticiones al modelo más caro disponible cuando el 70-80% de las peticiones pueden resolverse con calidad suficiente usando modelos significativamente más baratos. La diferencia de costo entre un modelo premium (GPT-4o: 2,50 USD/1M input tokens + 10 USD/1M output tokens) y un modelo económico (GPT-4o-mini: 0,15 USD/1M input tokens + 0,60 USD/1M output tokens) es de aproximadamente 15-20x, lo que significa que un sistema que enruta el 80% del tráfico al modelo económico y el 20% al premium reduce el costo de inferencia en aproximadamente 12-15x respecto a enviar todo al modelo premium. El clasificador de complejidad que toma la decisión de routing puede implementarse de múltiples formas con diferente latencia y precisión: reglas heurísticas basadas en longitud del input y keywords (baja latencia, menor precisión), un modelo lightweight de clasificación de complejidad entrenado sobre peticiones etiquetadas (latencia de 10-50ms, mayor precisión), o el propio LLM económico con un prompt de routing que evalúa si puede responder la petición con calidad suficiente o debe escalar al modelo premium (mayor latencia, máxima precisión pero costo adicional del propio routing).

## Patrones de model routing enterprise

- Reglas heurísticas de routing: tabla de decisión basada en longitud del prompt (< 500 tokens → modelo económico), presencia de keywords (análisis legal, diagnóstico médico → modelo premium), y tipo de tarea (FAQ → económico, redacción de contrato → premium)
- Clasificador de complejidad lightweight: modelo BERT fine-tuned o XGBoost entrenado sobre 1.000-5.000 pares (petición, modelo_apropiado) etiquetados, con inferencia de 10-30ms para no impactar la latencia del usuario
- Cascading (escalada automática): enviar la petición al modelo económico primero y, si la respuesta generada tiene una puntuación de confianza baja (estimada por un evaluador LLM-as-a-judge), re-enviarla automáticamente al modelo premium — con el riesgo de duplicar la latencia en el peor caso
- Routing por caso de uso: configuración explícita por endpoint de API que asigna un modelo específico a cada tipo de petición (soporte_faq → gpt-4o-mini, analisis_contrato → gpt-4o, generacion_informe → claude-sonnet)
- A/B testing del router: experimentar con diferentes estrategias de routing y medir el impacto en costo y calidad de respuesta para encontrar el punto óptimo del trade-off para cada caso de uso específico

## Principio rector

El model routing empresarial debe optimizarse para minimizar el costo total dado un umbral mínimo de calidad — no para maximizar la calidad ignorando el costo, ni para minimizar el costo ignorando la calidad.
