# Módulo 12 – Capítulo 07 – Sección 02

# Golden dataset de evaluación: construcción, anotación y uso en la evaluación continua

El golden dataset del proyecto es un conjunto de 200 pares (pregunta, respuesta_esperada, contextos_relevantes, metadata) anotados manualmente por ingenieros que conocen el dominio. La construcción del dataset sigue un proceso de tres fases: generación de preguntas representativas del caso de uso real (distribuidas en categorías: preguntas factuales simples 30%, razonamiento multi-documento 40%, preguntas sobre procedimientos 30%), anotación de la respuesta esperada y los chunks que la soportan, y revisión cruzada donde un segundo anotador valida cada par y marca discrepancias para discusión. Los metadatos por par incluyen: `difficulty` (easy/medium/hard), `requires_multi_doc` (boolean), `domain_area` (adr/runbook/api-spec) y `last_reviewed` (fecha). El dataset se divide 80/20: 160 pares para evaluación continua y 40 pares como test set reservado que solo se usa para comparaciones entre versiones mayores del sistema.

## Proceso de construcción del golden dataset

- Generación de preguntas: muestreo estratificado por tipo (factual, multi-documento, procedimental) y dificultad
- Anotación: respuesta esperada + lista de chunk_ids que la soportan + nivel de confianza del anotador (1-5)
- Revisión cruzada: segundo anotador revisa cada par, con resolución por consenso para discrepancias
- Metadatos: difficulty, requires_multi_doc, domain_area, last_reviewed, annotator_id para trazabilidad
- División train/test: 80% para evaluación continua en CI/CD, 20% reservado para comparaciones entre versiones mayores

## Para recordar

El golden dataset es el artefacto más valioso del framework de evaluación — su calidad determina la confianza en las métricas RAGAS, y debe actualizarse cuando el dominio de conocimiento evoluciona o cuando se detectan brechas de cobertura.
