# Módulo 5 – Capítulo 07 – Sección 04

# Benchmarks comparativos: modelos, versiones y configuraciones

Los benchmarks comparativos permiten tomar decisiones de selección de modelo basadas en evidencia empírica sobre el dominio y caso de uso específico, en lugar de basarse en rankings generales como MMLU, HumanEval o Chatbot Arena que miden capacidades que pueden no correlacionar con el rendimiento en la tarea objetivo. El proceso de benchmarking interno sigue cuatro pasos: definir el conjunto de evaluación (dataset curado del dominio, con 100-500 casos representativos), definir las métricas (las mismas que se usarán en producción), ejecutar el mismo dataset sobre cada candidato (modelo A, modelo B, configuración X, configuración Y) de forma controlada (misma temperatura, mismos seeds donde aplique), y comparar los resultados con análisis estadístico para determinar si las diferencias son significativas. Las comparaciones deben ser multidimensionales: un modelo puede ser mejor en faithfulness pero peor en latencia y más costoso; la decisión final integra calidad, velocidad y costo, ponderados según los requisitos del caso de uso.

## Aspectos técnicos del benchmarking comparativo

- Grid de configuraciones: definir una matriz de experimentos con las variables a comparar (`model x temperature x prompt_version`), ejecutar cada combinación sobre el mismo dataset y registrar las métricas en una tabla comparativa estructurada
- Bootstrap confidence intervals: calcular intervalos de confianza del 95% para las métricas de cada modelo usando bootstrap resampling; dos modelos con scores medios similares pero intervalos de confianza que se solapan no tienen diferencia estadísticamente significativa
- Latencia y costo como métricas de primera clase: registrar P50/P90/P99 de latencia y costo por request para cada configuración, no solo las métricas de calidad; una diferencia de calidad del 2% raramente justifica un incremento de costo del 300%
- Análisis por subgrupo: desagregar los resultados por categoría de consulta (preguntas simples vs complejas, preguntas en inglés vs español, preguntas sobre el dominio A vs el dominio B) para identificar dónde cada modelo tiene fortalezas específicas
- Versionado del benchmark: guardar el resultado completo de cada run de benchmark (configuración exacta, dataset hash, scores por caso, métricas agregadas) en un registro persistente para poder reproducir y comparar benchmarks históricos ante cambios de versión del modelo del proveedor

## Para recordar

El benchmark interno sobre el dominio específico es siempre más predictivo del rendimiento en producción que los benchmarks públicos generales; invertir en construirlo es una de las decisiones de ingeniería de mayor retorno en proyectos de IA de larga duración.
