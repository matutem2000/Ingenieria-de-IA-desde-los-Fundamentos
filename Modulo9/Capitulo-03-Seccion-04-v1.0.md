# Módulo 9 – Capítulo 03 – Sección 04

# Membership inference: determinar si un dato fue usado en el entrenamiento

El ataque de membership inference (MIA) tiene como objetivo determinar si un ejemplo de datos específico fue parte del dataset de entrenamiento de un modelo, lo cual constituye una violación de privacidad cuando esos datos son sensibles —registros médicos, comunicaciones privadas, datos financieros personales. El ataque fue formalizado por Shokri et al. (2017) en "Membership Inference Attacks Against Machine Learning Models" y posteriormente adaptado específicamente para LLMs por Carlini et al. en "Extracting Training Data from Large Language Models" (2021), donde demostraron que GPT-2 memorizaba y reproducía verbatim secuencias de texto del corpus de pretraining, incluyendo nombres, emails, números de teléfono y fragmentos de código. La susceptibilidad al membership inference es una función directa de la tasa de memorización del modelo, que aumenta con el tamaño del modelo (modelos más grandes memorizan más), con la frecuencia de aparición del dato en el training set, y con el nivel de overfitting durante el entrenamiento.

## Aspectos técnicos

- Mecanismo del ataque: el adversario consulta el modelo con secuencias de texto candidatas y observa la perplexity (log-likelihood) que el modelo asigna a esa secuencia; los datos que fueron parte del entrenamiento reciben mayor log-likelihood que los datos no vistos, permitiendo inferir la pertenencia con precisión superior al azar
- Ataque de Carlini et al. contra GPT-2: generación de millones de secuencias con GPT-2 y posterior filtrado por métricas de memorización (log-likelihood alta, ratio elevado respecto a un modelo de referencia), recuperando secuencias verbatim del training set incluyendo PII real
- Extractabilidad en LLMs de producción: el paper "Scalable Extraction of Training Data from (Production) Language Models" (Nasr et al., 2023) demostró extracción de datos de entrenamiento de ChatGPT (GPT-3.5 en producción) mediante el truco de repetir indefinidamente una palabra ("poem poem poem poem..."), provocando que el modelo salga de su modo generativo y repita memorization del training set
- Mitigaciones técnicas: differential privacy durante el entrenamiento (DP-SGD con epsilon bajo) reduce la memorización pero degrada la calidad del modelo; deduplicación agresiva del dataset de entrenamiento reduce la memorización de ejemplos vistos muchas veces; técnicas de unlearning selectivo (machine unlearning) para eliminar datos memorados sin reentrenar desde cero
- Implicaciones legales: la capacidad de un modelo de reproducir datos personales identificables de su corpus de entrenamiento es el fundamento técnico de las demandas legales por violación de GDPR contra proveedores de LLMs en Europa

## Para recordar

Membership inference y la memorización de training data no son riesgos teóricos: Carlini et al. demostraron extracción exitosa de PII de GPT-2 y GPT-3.5 en producción, y cualquier sistema que haga fine-tuning con datos de usuarios debe implementar differential privacy, deduplicación y auditorías de memorización antes de desplegar el modelo.
