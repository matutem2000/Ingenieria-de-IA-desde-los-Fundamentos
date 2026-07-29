# Módulo 12 – Capítulo 01 – Sección 06

# Cierre: el proyecto final integra todo el conocimiento del libro en un sistema real

El proyecto final del Módulo 12 no es el último ejercicio del libro — es la demostración de que los conceptos de los módulos anteriores forman un sistema coherente cuando se aplican juntos bajo restricciones reales. El diseño del sistema integrador exige combinar RAG (Módulo 6 y 7), ingeniería de prompts (Módulo 3), agentes (Módulo 8), seguridad (Módulo 10), MLOps (Módulo 9) y observabilidad (Módulo 11) en una arquitectura que funcione en producción, no solo en un notebook de desarrollo. Cada decisión técnica tomada en este capítulo de diseño tiene un costo: elegir GPT-4o sobre Claude 3.5 Sonnet cambia el perfil de costos; elegir Qdrant sobre Pinecone cambia la operabilidad; elegir LangGraph sobre un agente custom cambia la complejidad de debugging. El valor del proyecto final reside precisamente en haber tomado esas decisiones con evidencia, haberlas documentado en ADRs, y haber construido un sistema que puede evaluarse, monitorearse y mejorarse de forma continua.

## Aspectos técnicos que integra este capítulo

- Definición de caso de uso con restricciones cuantitativas medibles, no cualitativas ni aspiracionales
- Arquitectura de alto nivel con flujos de datos explícitos para los paths de ingesta y de consulta
- Stack tecnológico con justificación comparativa por cada componente y alternativa evaluada y descartada
- Criterios de éxito técnico trazables: RAGAS, latencia P95, costo/petición, tasa de bypass de seguridad
- Alcance acotado con exclusiones explícitas que protegen la integridad del sistema ante ataques de scope creep

## Para recordar

El diseño de un sistema de IA comienza por las restricciones y los criterios de éxito — la tecnología viene después.

*"Good software systems are not built by accumulating features, but by restricting what they do." — Fred Brooks, The Mythical Man-Month*
