# Módulo 8 – Capítulo 01 – Sección 04

# Leaderboards y evaluación: LMSYS Chatbot Arena, Open LLM Leaderboard

Los benchmarks públicos son la principal herramienta para comparar modelos antes de la evaluación en dominio específico, pero cada leaderboard mide dimensiones distintas y ninguno captura completamente el rendimiento en tareas de producción reales. El Open LLM Leaderboard de Hugging Face mide rendimiento en benchmarks estandarizados como MMLU (conocimiento de múltiples dominios, 57 tareas), ARC-Challenge (razonamiento científico), HellaSwag (coherencia de texto) y GSM8K (matemáticas de nivel escolar), ejecutados de forma reproducible con LM Evaluation Harness. LMSYS Chatbot Arena utiliza el sistema Elo de ajedrez calculado a partir de más de un millón de evaluaciones head-to-head ciegas realizadas por usuarios humanos, lo que lo hace más correlacionado con preferencia humana real pero menos reproducible y sesgado hacia inglés conversacional. La evaluación efectiva de un modelo para producción combina scores de leaderboard con benchmarks específicos del dominio y evaluación humana en las tareas exactas del producto.

## Puntos críticos sobre leaderboards

- MMLU (Massive Multitask Language Understanding): 14.000 preguntas de opción múltiple en 57 materias; mide conocimiento factual pero no razonamiento complejo ni instrucción following; susceptible a contaminación de datos de preentrenamiento
- Open LLM Leaderboard v2: introdujo benchmarks más difíciles como GPQA (Graduate-Level Google-Proof Q&A), MuSR (razonamiento multi-step) y MATH-Hard para reducir la saturación de scores en la v1
- LMSYS Chatbot Arena: calcula Elo con intervalos de confianza del 95%; requiere entre 1.000 y 5.000 comparaciones por modelo para estabilizar el ranking; favorece modelos con buena presentación y formato sobre modelos técnicamente más precisos
- Contaminación de benchmarks: modelos entrenados con datos que incluyen preguntas de MMLU, HellaSwag o GSM8K pueden mostrar scores inflados no representativos del rendimiento real; esto es difícil de detectar sin acceso al dataset de preentrenamiento
- Evaluación en dominio: ningún leaderboard público reemplaza la evaluación en las tareas exactas del producto; los equipos de producción deben mantener un golden set de preguntas representativas evaluadas con métricas específicas del dominio

## Para recordar

Los leaderboards públicos son un punto de partida, no una decisión final: el modelo que lidera MMLU puede rendir por debajo de uno más pequeño en tu tarea específica una vez evaluado con datos de producción reales.
