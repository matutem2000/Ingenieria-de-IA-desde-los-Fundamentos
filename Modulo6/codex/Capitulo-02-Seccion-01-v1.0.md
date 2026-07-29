# Módulo 6 – Capítulo 02 – Sección 01

# Qué son los embeddings y cómo capturan significado semántico

Un embedding es una proyección de un objeto (texto, imagen, audio) a un vector de números reales en un espacio de alta dimensionalidad donde la distancia geométrica entre vectores refleja la similitud semántica entre los objetos originales. Los modelos de embedding son redes neuronales entrenadas con objetivos contrastivos, como el propuesto en el paper SBERT (Reimers y Gurevych, 2019), que aprenden a colocar textos semánticamente similares cerca en el espacio vectorial y textos disímiles lejos, usando pares positivos (frases equivalentes) y negativos (frases no relacionadas) durante el entrenamiento. La intuición fundamental es que el modelo aprende representaciones distribuidas donde dimensiones del vector corresponden (de forma difusa) a conceptos del dominio, permitiendo que la distancia coseno entre los vectores de "perro" y "can" sea casi cero mientras que la distancia entre "perro" y "avión" sea cercana a 1. En RAG, los embeddings permiten encontrar chunks de documentos que son semánticamente relevantes para una query incluso cuando no comparten ninguna palabra en común, superando las limitaciones de la búsqueda léxica basada en TF-IDF o BM25.

## Conceptos técnicos fundamentales

- Espacio latente: espacio vectorial de D dimensiones (típicamente 256–3072) donde cada punto representa un texto; la geometría del espacio codifica relaciones semánticas aprendidas del corpus de entrenamiento
- Encoder transformer: arquitectura basada en BERT/RoBERTa que procesa el texto de entrada y genera representaciones contextualizadas por posición y por atención cruzada entre tokens
- Pooling de secuencia: operación que reduce la secuencia de vectores de tokens a un único vector de documento; las estrategias incluyen CLS token, mean pooling y max pooling, siendo mean pooling la más robusta en SBERT
- Entrenamiento contrastivo: objetivo de pérdida (InfoNCE loss, Multiple Negatives Ranking loss) que maximiza la similitud de pares positivos y minimiza la de pares negativos en el batch
- Similitud coseno: métrica de distancia normalizada en rango [-1, 1] que mide el ángulo entre dos vectores, invariante a la magnitud; es la métrica estándar para comparar embeddings de texto en búsqueda semántica
- Sentence transformers: familia de modelos fine-tuneados sobre BERT con datos de pares de frases (NLI, STS) para optimizar la calidad de la representación de oraciones completas en lugar de tokens individuales

## Para recordar

Los embeddings no representan significado de forma explícita sino que encodifican patrones estadísticos de co-ocurrencia del corpus de entrenamiento; su calidad en un dominio específico depende de cuánto texto de ese dominio vio el modelo durante el entrenamiento.
