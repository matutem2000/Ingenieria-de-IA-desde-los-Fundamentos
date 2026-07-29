# Módulo 11 – Capítulo 05 – Sección 02

# Evaluación continua de LLM en producción: calidad, coherencia y alineación con el negocio

La evaluación de LLMs en producción enterprise debe operar en tres planos simultáneos: la evaluación de calidad técnica (coherencia gramatical, seguimiento de instrucciones, ausencia de alucinaciones verificables), la evaluación de alineación con el negocio (las respuestas representan correctamente la política, el tono, y el conocimiento de la empresa), y la evaluación de seguridad y cumplimiento (ausencia de contenido prohibido, no divulgación de información confidencial, respeto a las restricciones configuradas por el tenant). La implementación técnica de la evaluación continua combina tres tipos de evaluadores: evaluadores basados en reglas para verificaciones deterministas (la respuesta contiene una referencia de ticket, la respuesta está en el idioma correcto, la longitud de respuesta está dentro del rango esperado), evaluadores basados en embeddings para verificar la similitud semántica entre la respuesta generada y las respuestas de referencia del golden set, y evaluadores LLM-as-a-judge (usando GPT-4o o Claude Opus como juez) para evaluar dimensiones subjetivas como la claridad, la utilidad, y la precisión de la respuesta. El sistema de evaluación continua se integra en dos puntos del pipeline: pre-despliegue (como gate en el pipeline de CI/CD que bloquea el despliegue si las métricas de evaluación caen por debajo de thresholds definidos) y post-despliegue (sampling del 1-5% del tráfico de producción para evaluación asíncrona con alertas cuando se detectan degradaciones estadísticamente significativas).

## Componentes del sistema de evaluación continua

- Golden dataset: conjunto de 100-500 pares (input, output_esperado) representativos de los casos de uso críticos, mantenido en Git con proceso de revisión para agregar nuevos casos y actualizar los existentes
- Evaluadores LLM-as-a-judge: prompts de evaluación calibrados que usan un LLM para calificar dimensiones como relevancia (1-5), precisión factual (1-5), y adherencia al estilo (1-5), con correlación validada contra evaluación humana
- Métricas de evaluación de RAG: RAGAS framework para evaluar faithfulness (la respuesta es fiel al contexto recuperado), answer relevancy (la respuesta es relevante a la pregunta), y context precision (el contexto recuperado es relevante para la pregunta)
- CI/CD gate de calidad: job en GitHub Actions, GitLab CI, o Jenkins que ejecuta la suite de evaluación sobre los cambios de prompt o modelo antes de permitir el merge a la rama de producción
- Sampling de producción: interceptor en el servicio de orquestación que con probabilidad configurable (1-5%) registra el par (input, output) en una cola asíncrona para evaluación posterior, sin impactar la latencia del usuario

## Buena práctica

Las métricas de evaluación deben definirse antes de desplegar el primer sistema de IA a producción, junto con los thresholds que disparan una alerta o un rollback automático — definirlos después del primer incidente es siempre demasiado tarde.
