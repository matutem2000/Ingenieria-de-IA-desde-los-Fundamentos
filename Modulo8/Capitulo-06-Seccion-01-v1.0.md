# Módulo 8 – Capítulo 06 – Sección 01

# Por qué hacer fine-tuning: casos donde el prompting no es suficiente

El fine-tuning de un LLM sobre datos específicos del dominio es una técnica que modifica los pesos del modelo para internalizar conocimiento, estilos de respuesta o capacidades que no pueden obtenerse de forma confiable mediante prompt engineering, y la decisión de cuándo aplicarlo debe basarse en evidencia empírica de que el prompting ha alcanzado un plateau de rendimiento en la tarea objetivo. Los escenarios donde el prompting resulta insuficiente incluyen: formatos de salida altamente específicos que el modelo base no genera de forma consistente (JSON con schemas complejos, código en dialectos propietarios, reportes con estructuras fijas), estilos de escritura o tonos muy particulares que requieren decenas de ejemplos para establecerse y se pierden entre conversaciones, y conocimiento de dominio muy especializado que no aparece en los datos de preentrenamiento (terminología médica interna, sistemas legales de jurisdicciones específicas, arquitecturas de software propietarias). El fine-tuning instruction-following mejora la tasa de seguimiento de instrucciones complejas de forma más confiable que el few-shot prompting: un modelo fine-tuneado sobre 1.000-5.000 ejemplos de alta calidad en la tarea objetivo puede superar a un modelo 2-3x mayor usando solo prompting, con menor costo de inferencia. La decisión correcta sigue una secuencia: primero evalúa prompt engineering + few-shot, luego RAG, luego fine-tuning; el fine-tuning es el recurso de mayor costo de ingeniería y solo se justifica cuando los anteriores no alcanzan el umbral de calidad requerido.

## Casos de uso donde el fine-tuning supera al prompting

- Formato de salida estricto y consistente: cuando se requiere que el 99%+ de las respuestas sigan un schema JSON exacto o un formato de reporte específico que el few-shot prompting produce con 85-90% de consistencia; el fine-tuning puede elevar esto al 98-99%
- Dominio con terminología no en los datos de preentrenamiento: sistemas legacy, APIs propietarias, jerga interna de la empresa; el modelo base "inventa" terminología o referencias que no existen; el fine-tuning sobre documentación real resuelve este problema
- Eficiencia en inferencia: un modelo de 7B fine-tuneado en una tarea específica puede igualar o superar a un modelo de 70B con few-shot prompting en esa tarea; el costo de inferencia 10x menor justifica el costo único de fine-tuning
- Reducción de longitud del prompt: una capacidad que requiere 500-1000 tokens de context window en few-shot prompting puede reducirse a un system prompt de 50 tokens post fine-tuning, multiplicando la capacidad de contexto efectivo para datos de usuario
- Comportamiento ante edge cases: el few-shot prompting no garantiza comportamiento correcto en inputs que difieren del patrón de los ejemplos; el fine-tuning sobre un dataset diverso que incluye edge cases mejora la robustez ante entradas inesperadas

## Para recordar

El fine-tuning es la herramienta correcta cuando tienes datos de alta calidad representativos de la tarea, el prompting ha demostrado un techo claro de rendimiento y el volumen de uso justifica la inversión en preparación de datos y entrenamiento.
