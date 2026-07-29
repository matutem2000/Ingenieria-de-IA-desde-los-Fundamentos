# Módulo 12 – Capítulo 10 – Sección 03

# Lecciones aprendidas: reflexión sobre las decisiones técnicas tomadas durante el proyecto

Las lecciones aprendidas del proyecto final son las insights técnicos más valiosos que emergen de haber construido el sistema completo bajo restricciones reales. La primera lección es sobre chunking: los parámetros por defecto de los frameworks (1024 tokens con 200 de overlap) rara vez son óptimos para un dominio específico — la validación con RAGAS sobre el golden dataset mostró que 512 tokens con 64 de overlap producía 0.09 puntos más de context precision para este corpus de documentación técnica. La segunda lección es sobre el reranking: eliminarlo del pipeline para reducir latencia degradó faithfulness de 0.87 a 0.74, demostrando que los 280ms de latencia adicional del reranker Cohere son una inversión justificada. La tercera lección es sobre los ADRs: las decisiones documentadas en los primeros ADRs fueron las que el equipo más agradeció cuando llegó a revisar el sistema 6 semanas después — el razonamiento detrás de elegir LangGraph sobre AgentExecutor no era obvio sin el ADR que lo documentaba.

## Lecciones aprendidas por componente

- Chunking: los parámetros por defecto son punto de partida, no configuración óptima; siempre validar con RAGAS sobre golden dataset
- Reranking: la latencia del reranker es pequeña comparada con la degradación de faithfulness al eliminarlo — mantenerlo siempre
- ADRs: las decisiones que se toman bajo presión de tiempo son exactamente las que más importa documentar, no las "obvias"
- Testing agéntico: los escenarios de fallo (retrieval vacío, timeout, max_iterations) deben testearse desde el inicio, no al final
- Observabilidad: instrumentar con OpenTelemetry desde el primer commit es más económico que agregar instrumentación a un sistema existente

## Para recordar

Las lecciones aprendidas del proyecto son más valiosas que el código del proyecto — el código puede reescribirse, pero las decisiones mal tomadas que no se documentan se repetirán en el siguiente proyecto del equipo.
