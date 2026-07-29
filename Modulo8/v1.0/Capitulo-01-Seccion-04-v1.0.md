# Módulo 8 – Capítulo 01 – Sección 04

## Leaderboards y evaluación: LMSYS Chatbot Arena, Open LLM Leaderboard y lm-evaluation-harness

La primera decisión operativa al comenzar un proyecto con modelos locales es elegir el modelo base. Esta decisión, que precede a cualquier inversión en fine-tuning o infraestructura, debería estar respaldada por evidencia empírica en la tarea concreta del producto —no solo en benchmarks genéricos. El error más frecuente que cometen los equipos es seleccionar el modelo con el score más alto en el Open LLM Leaderboard sin verificar que ese ranking se transfiere a su tarea, idioma y dominio específicos. Un modelo que lidera MMLU puede quedar tercero en extracción de entidades en español médico; un modelo mediocre en HumanEval puede ser exactamente lo que se necesita para completar consultas SQL en el dialecto propietario de una empresa.

Los **leaderboards públicos** son un punto de partida, no una decisión final. El **Open LLM Leaderboard** de Hugging Face mide rendimiento en benchmarks estandarizados ejecutados de forma reproducible con LM Evaluation Harness: MMLU (conocimiento factual en 57 materias, 14.000 preguntas de opción múltiple), ARC-Challenge (razonamiento científico de nivel escolar avanzado), HellaSwag (coherencia de texto en contextos cotidianos), GSM8K (matemáticas de nivel primaria-secundaria) y, en la versión v2, benchmarks más difíciles como GPQA (preguntas de nivel de doctorado), MuSR (razonamiento multi-paso) y MATH-Hard para reducir la saturación de scores. La fortaleza del Open LLM Leaderboard es la reproducibilidad: cualquier equipo puede replicar los números ejecutando los mismos benchmarks sobre el mismo modelo.

El **LMSYS Chatbot Arena** complementa esta vista con evaluaciones humanas: usuarios reales comparan pares de respuestas de modelos sin saber qué modelo genera cada una, y el sistema calcula un ranking Elo con intervalos de confianza del 95%. Chatbot Arena es más correlacionado con la preferencia humana real que MMLU (las preguntas de opción múltiple no capturan calidad conversacional), pero tiene tres limitaciones sistemáticas: está sesgado hacia inglés conversacional, favorece modelos con buena presentación y formato sobre modelos técnicamente más precisos, y no permite evaluar tareas de dominio específico (no puedes añadir tus propias preguntas al sistema).

La herramienta que cierra la brecha entre leaderboards genéricos y evaluación en dominio propio es **lm-evaluation-harness** de EleutherAI. Esta librería de Python permite ejecutar más de 200 benchmarks estandarizados localmente sobre cualquier modelo de Hugging Face, GGUF o servido via API compatible con OpenAI, con resultados exactamente reproducibles. La instalación es directa:

```bash
pip install lm-eval
# Evaluar Llama 3.1 8B en MMLU y GSM8K
lm_eval --model hf \
    --model_args pretrained=meta-llama/Llama-3.1-8B-Instruct \
    --tasks mmlu,gsm8k \
    --batch_size auto \
    --output_path ./resultados/
```

Para modelos servidos localmente con Ollama o vLLM, el backend `local-completions` permite evaluar sin cargar el modelo directamente en la librería:

```bash
lm_eval --model local-completions \
    --model_args model=llama3:8b,base_url=http://localhost:11434/v1 \
    --tasks mmlu_es,hellaswag_es \
    --batch_size 8
```

Los benchmarks más relevantes según el tipo de tarea son: **MMLU/MMLU-Pro** para conocimiento factual general; **HumanEval y MBPP** para generación de código en Python; **GSM8K y MATH** para razonamiento matemático; **MT-Bench** para evaluación de instrucción following multi-turno con juez LLM; y **BBH (BIG-Bench Hard)** para razonamiento complejo en tareas que los modelos más pequeños aún no dominan. Para tareas en español, los benchmarks **XNLI** (inferencia de lenguaje natural multilingüe) y **IberBench** cubren razonamiento y conocimiento en el idioma.

La evaluación en dominio propio requiere construir un **golden dataset** antes de seleccionar el modelo base: un conjunto de 100 a 500 preguntas o tareas representativas del producto real con las respuestas esperadas. Este golden set es más valioso que cualquier benchmark público porque mide exactamente lo que importa. Para construirlo, el proceso recomendado es: (1) extraer ejemplos reales del backlog de casos de uso o consultas de usuarios; (2) incluir explícitamente casos fáciles, casos medios y edge cases conocidos; (3) definir métricas de evaluación para cada categoría (exact match, ROUGE-L, o LLM-as-judge con GPT-4o como árbitro para respuestas abiertas). Con este golden set, la comparación entre modelos candidatos se convierte en una decisión empírica, no en una discusión de opiniones.

## Puntos críticos sobre leaderboards y evaluación

- **MMLU:** 14.000 preguntas de opción múltiple en 57 materias; mide conocimiento factual pero no razonamiento complejo; susceptible a contaminación de datos si el modelo fue entrenado con preguntas de MMLU.
- **Open LLM Leaderboard v2:** introdujo GPQA, MuSR y MATH-Hard para reducir la saturación de scores que afectó a la v1 en modelos de 7B o más.
- **LMSYS Chatbot Arena:** calcula Elo con intervalos de confianza del 95%; requiere entre 1.000 y 5.000 comparaciones para estabilizar el ranking; favorece modelos con buena presentación.
- **lm-evaluation-harness:** más de 200 benchmarks ejecutables localmente; soporte para modelos Hugging Face, GGUF via llama.cpp, y APIs OpenAI-compatible; resultados reproducibles.
- **Golden dataset propio:** entre 100 y 500 ejemplos representativos de la tarea real; la métrica más confiable para la selección final del modelo base.
- **Contaminación de benchmarks:** modelos entrenados con preguntas de benchmarks públicos muestran scores inflados; difícil de detectar sin acceso al dataset de preentrenamiento.

> **Nota del Arquitecto:** El golden dataset propio es el único benchmark que no puede ser contaminado, porque nadie más tiene acceso a tus casos de uso reales. Invertir dos o tres días en construirlo antes de seleccionar el modelo base ahorra semanas de fine-tuning para corregir la elección incorrecta. En equipos maduros, este golden set se convierte en el gate de calidad de todos los despliegues futuros.

La evaluación empírica con lm-evaluation-harness y un golden dataset propio es el puente entre los benchmarks genéricos de los leaderboards y la realidad del rendimiento del modelo en producción. La sección siguiente completa el marco de selección con los criterios cuantitativos de tamaño, idioma, dominio y licencia que, combinados con la evaluación empírica, determinan el modelo base óptimo para cada proyecto.

---
