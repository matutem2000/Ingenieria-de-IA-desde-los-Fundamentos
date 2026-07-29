# Módulo 5 – Capítulo 05 – Sección 05

# Regression testing: detectar degradaciones entre versiones de modelos

El regression testing en sistemas de IA detecta si un cambio —en el prompt, en el modelo, en la configuración de parámetros, o en el framework de orquestación— degrada la calidad de las respuestas respecto a la versión anterior, antes de que el cambio llegue a producción. La estrategia canónica es mantener una suite de evaluación con dataset curado (50-500 casos de prueba con respuestas de referencia o criterios de calidad), ejecutar la suite sobre la versión anterior y la nueva, y definir criterios de umbral para aprobar el despliegue (ej: "la nueva versión no puede degradar el score medio en más del 3%"). Los cambios de versión de modelos por parte de los proveedores son una fuente frecuente de regresiones: cuando Anthropic o OpenAI actualiza un modelo manteniendo el mismo identificador, el comportamiento puede cambiar sutilmente; monitorear el `model_id` devuelto en cada respuesta y comparar con el esperado detecta actualizaciones silenciosas. Herramientas como DeepEval, RAGAS o LangSmith Dataset & Testing permiten almacenar el dataset de evaluación versionado y comparar automáticamente las métricas entre runs para detectar regresiones con un solo comando de CI.

## Aspectos técnicos del regression testing

- Snapshot testing de prompts: almacenar el output del LLM para inputs de referencia con `temperature=0` y comparar en cada PR; no como test de igualdad exacta sino como señal de que algo cambió que requiere revisión manual
- Comparación de distribuciones de métricas: en lugar de comparar scores individuales, comparar la distribución del score de calidad (media, P25, P75) entre la versión de baseline y la nueva versión usando tests estadísticos como Mann-Whitney U si el dataset tiene >30 muestras
- Versionado de prompts como código: guardar prompts en archivos `.txt` o `.jinja2` versionados en Git con tags semánticos (`prompt_v1.0.0`, `prompt_v1.1.0`), permitiendo identificar exactamente qué versión de prompt produjo los resultados del dataset de evaluación histórico
- CI job de evaluación condicional: configurar el pipeline de CI para ejecutar la suite de regression tests solo cuando los archivos de prompt, configuración del modelo o código del pipeline cambian, evitando el costo de ejecutarla en cada commit
- Alertas de degradación en producción: además del regression testing en CI, monitorear métricas de calidad en tiempo real en producción con Langfuse o LangSmith y disparar alertas cuando el score medio de un evaluador automático cae más del X% en las últimas N horas

## Principio rector

Las regresiones de calidad en sistemas de IA son silenciosas: el sistema sigue respondiendo sin errores de runtime, pero la calidad de las respuestas se degrada; solo un sistema de evaluación automatizado con métricas de calidad las detecta antes de que los usuarios las reporten.
