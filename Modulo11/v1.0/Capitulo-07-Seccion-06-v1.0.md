# Módulo 11 – Capítulo 07 – Sección 06

## Cierre: a escala enterprise, una mejora del 10% en eficiencia puede representar millones de dólares al año

La optimización de costos en sistemas de IA enterprise no es un ejercicio de austeridad que compromete la calidad del sistema: es una disciplina de ingeniería que determina si la iniciativa de IA puede escalar de manera sostenible o si el crecimiento del uso eventualmente genera costos que el negocio no puede asumir. Un sistema de IA con costos de inferencia insostenibles no muere por fallo técnico sino por decisión de negocio: el proyecto se cancela, o se limita artificialmente su uso para controlar el gasto, o se busca una solución alternativa más barata aunque de menor calidad. La optimización de costos es, en este sentido, una responsabilidad de continuidad del sistema.

Las técnicas cubiertos en este capítulo son complementarias y sus efectos se multiplican. Un sistema que implementa prompt caching para el system prompt (reduce en 50-90% el costo de los tokens del system prompt), semantic caching para preguntas frecuentes (elimina el 25-35% de las llamadas al LLM), y model routing para enviar el 75% del tráfico al modelo económico (reduce el costo de inferencia por petición en 10-15x para esas peticiones) puede alcanzar una reducción total del 70-80% respecto al diseño inicial naïve — transformando un sistema con un costo mensual de 500.000 USD en uno con un costo mensual de 100.000-150.000 USD, con impacto marginal en la calidad percibida por el usuario.

La secuencia de implementación importa tanto como las técnicas individuales. Como se describió en la sección introductoria de este capítulo, el orden de mayor impacto para menor esfuerzo en la mayoría de los sistemas de RAG enterprise es: prompt caching nativo primero (horas de implementación, impacto inmediato), semantic caching después (días de implementación, impacto en semanas), y model routing más tarde (semanas de implementación, impacto continuo). La infraestructura de Reserved e Spot Instances es independiente de las optimizaciones de nivel de aplicación y puede implementarse en paralelo.

La responsabilidad de la optimización de costos en sistemas de IA enterprise recae sobre el AI Engineer: no puede delegarse a un equipo de FinOps que no entiende los trade-offs técnicos entre calidad y costo de inferencia. El equipo de FinOps puede proporcionar visibilidad sobre los costos actuales y las tendencias, pero las decisiones sobre qué técnica de optimización implementar, con qué trade-offs de calidad, y con qué threshold de semantic caching son decisiones técnicas que requieren comprensión del sistema.

---

*"La arquitectura de un sistema exitoso debe ser económicamente sostenible: un sistema brillante técnicamente que nadie puede pagar en producción es un fracaso de ingeniería, no un éxito."* — Werner Vogels, CTO de Amazon Web Services
