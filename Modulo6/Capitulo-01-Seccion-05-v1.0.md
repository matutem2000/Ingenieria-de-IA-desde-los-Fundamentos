# Módulo 6 – Capítulo 01 – Sección 05

# Cuándo usar RAG vs fine-tuning vs contexto largo

La decisión entre RAG, fine-tuning y context stuffing no es estética sino técnica y económica: cada aproximación tiene un perfil de costo-beneficio diferente que depende del volumen de datos, la frecuencia de actualización, el presupuesto de inferencia y los requisitos de trazabilidad. El fine-tuning (ya sea SFT sobre LoRA/QLoRA o full fine-tuning) es adecuado cuando el dominio requiere adaptar el estilo de respuesta, el vocabulario técnico o los patrones de razonamiento del modelo, pero no sirve para inyectar conocimiento factual actualizable porque los hechos quedan "congelados" en los pesos. El context stuffing (cargar documentos completos en una ventana de contexto de 128K–1M tokens disponible en modelos como Gemini 1.5 Pro o Claude 3 Opus) es viable para corpus pequeños de hasta algunos centenares de documentos o en consultas one-off, pero el costo por inferencia escala linealmente con los tokens de contexto y la latencia crece con la longitud. RAG es la opción correcta cuando el corpus tiene decenas de miles o millones de documentos, se actualiza frecuentemente, requiere citar fuentes específicas y debe operar con latencia y costo controlables a escala de millones de consultas.

## Criterios de decisión técnica

- Fine-tuning es adecuado cuando: el objetivo es adaptar el comportamiento o estilo del modelo (formato de salida, terminología específica de dominio) pero el corpus de conocimiento es estático y pequeño (menos de 10K ejemplos)
- Fine-tuning no resuelve: la incorporación de conocimiento factual actualizable; los hechos aprenden con overfitting a los datos de entrenamiento y se degradan con actualizaciones posteriores del corpus
- Context stuffing es viable cuando: el corpus cabe en la ventana de contexto del modelo (Gemini 1.5 Pro: 1M tokens, GPT-4o: 128K tokens), la consulta es one-off y el costo de tokens de contexto no es una restricción operativa
- RAG es la opción correcta cuando: el corpus supera la ventana de contexto, los documentos se actualizan con frecuencia diaria o semanal, se requiere trazabilidad de fuentes o el sistema atiende millones de consultas con presupuesto acotado
- Combinación RAG + fine-tuning (RAG-Fusion): fine-tuning del LLM para seguir instrucciones del sistema RAG con mayor fidelidad, manteniendo RAG como mecanismo de conocimiento y fine-tuning solo para el comportamiento generativo
- Métricas de decisión: comparar costo por consulta (tokens de contexto × precio/token), latencia p95, Recall@K del retriever y faithfulness de las respuestas en un dataset de evaluación representativo del caso de uso

## Buena práctica

Comenzar siempre con RAG naive antes de invertir en fine-tuning; el 80% de los casos de uso empresariales se resuelven con RAG bien diseñado sin necesidad de modificar los pesos del modelo.
