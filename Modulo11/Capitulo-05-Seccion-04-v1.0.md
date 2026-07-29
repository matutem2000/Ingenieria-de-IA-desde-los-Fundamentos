# Módulo 11 – Capítulo 05 – Sección 04

# A/B testing de modelos y prompts en producción enterprise

El A/B testing en sistemas de LLM enterprise es técnicamente más complejo que en aplicaciones web convencionales porque la variable de respuesta no es binaria (hizo clic o no) sino multidimensional y subjetiva: la calidad de una respuesta de LLM debe medirse con combinaciones de métricas automáticas (evaluadores LLM-as-a-judge, similitud semántica con el golden set) y métricas de negocio (tasa de resolución de tickets sin escalar al agente humano, reducción del tiempo de generación de contratos, NPS del sistema). La asignación de tráfico entre variantes en un test A/B de LLM debe ser consistente por usuario o por sesión (no por petición individual), porque comparar la variante A en un mensaje y la variante B en el siguiente mensaje de la misma conversación contamina el experimento: un framework de feature flagging (LaunchDarkly, Unleash) que asigna la variante basándose en el hash del user_id o del session_id garantiza esta consistencia. El cálculo de significancia estadística en A/B tests de LLM requiere tamaños de muestra mayores que en tests de click-through rates porque la varianza de las métricas de calidad es mayor: típicamente se necesitan 1.000-5.000 conversaciones por variante para detectar diferencias del 5-10% en métricas de calidad con potencia estadística del 80%, lo que puede representar días o semanas de tráfico en sistemas de uso moderado. Los tests de modelos (comparar GPT-4o vs Claude Sonnet para el mismo caso de uso) son especialmente valiosos porque permiten tomar decisiones de selección de modelo basadas en datos de negocio reales en lugar de en benchmarks públicos que pueden no reflejar el caso de uso específico.

## Aspectos técnicos del A/B testing en LLMOps

- Asignación de variante: hash consistente del user_id o tenant_id módulo 100 para asignar porcentajes exactos de tráfico, registrado en el log de cada petición para poder segmentar el análisis posterior por variante
- Métricas de evaluación A/B: combinación de métricas automáticas (calidad LLM-as-a-judge, similarity score contra golden set) y métricas de negocio (thumbs up/down del usuario, tasa de follow-up de aclaración, tiempo hasta resolución)
- Multi-armed bandit como alternativa: en lugar de A/B testing clásico con asignación fija, usar algoritmos de bandit (Epsilon-Greedy, Thompson Sampling) que asignan más tráfico a la variante ganadora de manera dinámica durante el experimento
- Análisis de resultados con bootstrapping: para métricas no normales (scores de calidad discretos de 1-5), usar bootstrapping para calcular intervalos de confianza en lugar de t-tests que asumen normalidad
- Logging estructurado de experimentos: registrar en cada petición el experiment_id, la variante asignada, el model_id, el prompt_version, y todas las métricas de calidad calculadas en formato estructurado (JSON) para análisis posterior en BigQuery o ClickHouse

## Buena práctica

Nunca ejecutar más de un experimento simultáneo que afecte la misma métrica de negocio: la interferencia entre experimentos produce resultados espurios que llevan a decisiones erróneas sobre qué variante es superior.
