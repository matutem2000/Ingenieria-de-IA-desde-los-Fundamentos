# Módulo 9 – Capítulo 03 – Sección 03

# Model extraction: reconstruir el comportamiento de un modelo propietario via API

Model extraction —también llamado model stealing— es el ataque mediante el cual un adversario construye un modelo sustituto (surrogate model) que aproxima el comportamiento del modelo target consultando sistemáticamente su API, sin acceso a los pesos ni al proceso de entrenamiento original. El paper seminal de Tramèr et al. (2016) "Stealing Machine Learning Models via Prediction APIs" demostró que modelos comerciales podían ser reconstruidos con exactitud alta mediante relativamente pocos queries, sentando las bases teóricas del ataque. En el contexto de LLMs, model extraction es tanto un ataque de propiedad intelectual (replicar el comportamiento de GPT-4 entrenando un modelo más pequeño con sus outputs — el proceso que produjo modelos como Alpaca) como un ataque de privacidad (inferir propiedades del dataset de entrenamiento a través del comportamiento del modelo). La API de distillation —la práctica legítima de usar un LLM grande para generar datos de entrenamiento de un modelo más pequeño— y model extraction son técnicamente indistinguibles desde la perspectiva del proveedor.

## Aspectos técnicos

- Mechanism de extracción: el atacante genera un dataset de inputs diseñados para cubrir el espacio de comportamientos del modelo target, obtiene los outputs via API, y entrena un surrogate model (distilación) sobre esos pares input-output — el resultado es un modelo que replica el comportamiento sin los costos de entrenamiento originales
- Extracción funcional vs. fidelity extraction: la extracción funcional busca replicar el comportamiento del modelo en el dominio de interés del atacante (suficiente para la mayoría de los casos de uso malicioso); la fidelity extraction busca maximizar la similitud global del comportamiento, incluyendo outputs en distribuciones raras
- Detección de model extraction: los proveedores como OpenAI y Anthropic monitorean patrones de queries (alta diversidad de inputs, queries sistemáticas que cubren el espacio de temas, volumen anormal para el tier del cliente) y pueden detectar intentos de extracción — los ToS de todos los proveedores principales prohíben explícitamente distillation sin licencia
- Watermarking de modelos: técnicas como text watermarking (insertar patrones estadísticos en los outputs del modelo) permiten a los proveedores verificar si un modelo fue entrenado con outputs de su API, incluso si el atacante no lo declara
- Extractabilidad de fine-tuned models: modelos fine-tuned con datos propietarios son especialmente vulnerables porque su comportamiento diferencial (respecto al modelo base) puede ser extraído con relativamente pocas consultas enfocadas en el dominio del fine-tuning

## Para recordar

Model extraction es un ataque de propiedad intelectual que los términos de servicio no pueden prevenir técnicamente: la defensa efectiva incluye rate limiting agresivo, monitoreo de patrones de query anómalos, output watermarking, y el argumento comercial de que el modelo propietario es más que sus outputs —incluye el pipeline de entrenamiento, datos, y capacidad de actualización continua.
