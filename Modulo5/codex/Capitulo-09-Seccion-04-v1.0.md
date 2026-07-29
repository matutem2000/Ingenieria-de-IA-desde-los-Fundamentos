# Módulo 5 – Capítulo 09 – Sección 04

# Elección de modelo por costo-beneficio: cuándo usar modelos más pequeños

La elección del modelo de LLM para cada tarea es la decisión de costo-calidad con mayor impacto en el presupuesto total de un sistema de IA: usar `gpt-4o` para clasificar intenciones de usuario con 5 categorías en lugar de `gpt-4o-mini` puede ser 15-20x más caro por request sin ninguna mejora measurable en la tarea. El principio de routing por complejidad asigna el modelo más capaz y costoso solo a las tareas que genuinamente lo requieren, usando modelos más económicos para tareas simples y bien definidas. La forma correcta de decidir si una tarea necesita el modelo grande es empírica: ejecutar la tarea sobre el dataset de evaluación con modelos de diferentes capacidades y comparar la calidad; si el modelo pequeño obtiene >90% de la calidad del modelo grande en la tarea específica del dominio, el modelo pequeño es la elección correcta. El patrón LLM router lleva este principio al extremo: un modelo pequeño y rápido clasifica la complejidad de la query del usuario y la enruta al modelo adecuado (Haiku para queries simples, Sonnet para queries medias, Opus/GPT-4o para queries que requieren razonamiento profundo).

## Criterios técnicos para la selección de modelo por tarea

- Clasificación e intent detection: `gpt-4o-mini` o `claude-3-haiku-20240307` son suficientes para clasificación con pocas categorías bien definidas; la diferencia de calidad vs el modelo grande es típicamente <3% en dominios estables con buenos ejemplos few-shot
- Extracción de entidades simples: nombre, fecha, importe, categoría de un texto estructurado → modelos pequeños con extracción JSON obtienen 95%+ de accuracy vs el modelo grande a 10-20x menor costo
- Resumen de documentos largos: ventana de contexto extendida y capacidad de síntesis son ventajas del modelo grande; modelos pequeños tienden a omitir detalles o repetir el texto; el modelo grande justifica su costo en resúmenes de alta calidad
- Razonamiento multi-paso y coding: tareas que requieren mantener múltiples constraints simultáneos, razonamiento causal complejo o generación de código correcto → el modelo grande ofrece mejoras medibles de 10-20% en calidad que justifican el costo adicional
- LLM router pattern: `small_model.classify_query_complexity(query)` devuelve `{"complexity": "simple|medium|complex", "task_type": "classification|generation|reasoning"}`; el resultado enruta a diferentes endpoints con diferentes modelos, con logging del modelo usado para análisis de distribución de rutas

## Principio rector

Sobre-aprovisionar modelo para una tarea es tan ineficiente como sub-aprovisionar infraestructura: el modelo correcto no es el más capaz disponible sino el menos capaz que cumple el requisito de calidad medido en el dataset de evaluación del dominio.
