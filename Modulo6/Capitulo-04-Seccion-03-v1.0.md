# Módulo 6 – Capítulo 04 – Sección 03

# Chunk size vs chunk overlap: trade-offs de precisión y cobertura

Los parámetros de chunk_size y chunk_overlap son las dos dimensiones de configuración más influyentes en una estrategia de chunking fijo o recursivo, y presentan trade-offs opuestos que deben calibrarse según el tipo de queries y el corpus del sistema. Un chunk_size pequeño (128–256 tokens) produce vectores muy específicos con alta similitud coseno cuando la query es precisa y coincide exactamente con la información del chunk, pero el chunk puede carecer del contexto necesario para que el LLM generador produzca una respuesta completa; esto favorece el Precision@K pero perjudica la calidad de la generación por falta de contexto. Un chunk_size grande (1024–2048 tokens) permite al LLM tener más contexto en cada chunk pero diluye el vector embedding al promediar múltiples temas, reduciendo el Recall@K para queries específicas. El chunk_overlap introduce redundancia controlada entre chunks consecutivos para evitar que información que cae en el límite de un chunk sea inaccesible: un overlap del 10–20% del chunk_size es el rango recomendado en la mayoría de los casos; un overlap excesivo (>50%) incrementa el número total de chunks, el costo de almacenamiento y el riesgo de recuperar contenido duplicado en una sola consulta.

## Trade-offs técnicos de tamaño y overlap

- Chunk size 128–256 tokens: alta especificidad del vector; útil para QA factual donde la respuesta es una frase o dato puntual; riesgo de falta de contexto para el LLM; requiere mayor K en recuperación para cubrir el contexto necesario para la respuesta
- Chunk size 512–768 tokens: punto de equilibrio más común en producción; cubre típicamente 1–3 párrafos; vector suficientemente específico con contexto suficiente para generación; rango óptimo para la mayoría de corpora de texto técnico o documental
- Chunk size 1024–2048 tokens: adecuado para documentos con alta coherencia temática (artículos científicos, contratos legales por cláusula); riesgo de vectores promediados si el documento mezcla temas; requiere modelos de embedding con ventanas de contexto largas (voyage-3 soporta 32K tokens)
- Chunk overlap 0%: sin redundancia; máxima eficiencia de almacenamiento; información en límites de chunk puede perderse; solo recomendable cuando los separadores de chunking son semánticamente significativos (headers de sección, fin de párrafo)
- Chunk overlap 10–20% (50–150 tokens sobre chunk de 512): rango estándar que garantiza continuidad de contexto en límites; incrementa el corpus indexado en un 10–20%; recomendado como configuración por defecto en RecursiveCharacterTextSplitter
- Chunk overlap >50%: produce chunks altamente redundantes que inflan el índice y pueden devolver chunks casi idénticos en la misma búsqueda; raramente justificable; puede indicar que la estrategia de chunking no es la adecuada para el tipo de documento

## Para recordar

Chunk size de 512 tokens con overlap de 10–15% es el punto de partida empíricamente más robusto; cualquier desviación de este punto debe justificarse con métricas de Recall@K medidas sobre el corpus y las queries del caso de uso específico.
