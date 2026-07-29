# Módulo 8 – Capítulo 01 – Sección 01

# Open weights vs open source: qué significa "abierto" en el contexto de los LLM

El término "open source" en el contexto de los LLM es técnicamente ambiguo: la mayoría de los modelos llamados abiertos publican únicamente los pesos entrenados (open weights), pero no el código de entrenamiento completo, los datasets utilizados ni los procedimientos exactos de curación de datos. Llama 3 de Meta, por ejemplo, libera los pesos bajo una licencia comunitaria propia, pero no publica el pipeline de preentrenamiento ni los datos de instrucción usados en el ajuste fino. En contraste, modelos como OLMo de AI2 publican los pesos, el código de entrenamiento, los datos completos y los checkpoints intermedios, acercándose a una definición más rigurosa de open source. Esta distinción no es filosófica sino operativa: afecta directamente qué puedes reproducir, auditar, modificar y redistribuir sin restricciones legales.

## Diferencias técnicas clave

- Open weights: se publican los parámetros del modelo en formato SafeTensors o GGUF, pero el pipeline de entrenamiento permanece cerrado o parcialmente documentado
- Open source completo: incluye código de entrenamiento (a menudo PyTorch/JAX), datasets indexados en Hugging Face Datasets o similares, y scripts de evaluación reproducibles
- Licencias restrictivas: modelos como Llama 2/3 prohíben explícitamente uso en servicios con más de 700 millones de usuarios activos mensuales sin acuerdo especial con Meta
- Transparencia de datos: OLMo y Mistral 7B v0.1 documentan sus fuentes de datos; la mayoría de los demás no detallan la composición exacta del corpus de preentrenamiento
- Reproducibilidad: sin el código de entrenamiento y los datos exactos, un modelo open weights no puede ser reproducido desde cero, lo que limita la auditoría de sesgos y vulnerabilidades

## Para recordar

La distinción entre open weights y open source determina qué puedes hacer legalmente y técnicamente con un modelo: siempre lee la licencia antes de integrar un modelo en un producto.
