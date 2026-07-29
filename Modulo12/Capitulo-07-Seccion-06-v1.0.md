# Módulo 12 – Capítulo 07 – Sección 06

# Cierre: un sistema que no puede evaluarse no puede mejorarse

El framework de evaluación del proyecto final cierra el loop entre implementación y mejora continua: las métricas RAGAS sobre el golden dataset revelan dónde el pipeline RAG falla; las métricas agénticas revelan dónde el agente usa mal sus herramientas; las métricas de rendimiento revelan dónde está el cuello de botella de latencia; y los resultados del red teaming revelan qué controles de seguridad son insuficientes. Sin este conjunto de métricas correlacionadas, cada decisión de mejora sería basada en intuición — con él, cada cambio al sistema puede ser evaluado cuantitativamente antes de llegar a producción. El pipeline CI/CD con gate de evaluación automática garantiza que solo las versiones que mejoran o mantienen las métricas clave avanzan al despliegue, creando un ciclo de mejora que es auditable, reproducible y continuo. La evaluación no termina con el despliegue: el monitoreo continuo en producción detecta drifts de calidad que el golden dataset estático no puede capturar.

## Aspectos técnicos que integra este capítulo

- Framework tri-capa: métricas RAG (RAGAS), agénticas (task completion, hallucination) y de sistema (latencia, costo, error_rate)
- Golden dataset: 200 pares anotados con división 80/20, proceso de revisión cruzada y metadatos de trazabilidad
- Evaluación de calidad: faithfulness, answer_relevance, completeness personalizada y user satisfaction implícita
- Evaluación de rendimiento: latencia por etapa con OpenTelemetry, benchmark Locust, costo por petición desagregado
- Evaluación de seguridad: matriz de resultados del red teaming con tasa de bypass por categoría y mejoras aplicadas

## Para recordar

La evaluación es la capacidad que convierte un sistema de IA en un sistema de ingeniería — sin métricas cuantificables, no hay forma de demostrar mejora, detectar degradación ni tomar decisiones de arquitectura basadas en evidencia.

*"Without data, you're just another person with an opinion." — W. Edwards Deming*
