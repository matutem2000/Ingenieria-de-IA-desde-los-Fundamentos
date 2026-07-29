# Módulo 10 – Capítulo 09 – Sección 04

# FinOps para IA: integración del modelo de costos con las prácticas de FinOps de la organización

FinOps (Financial Operations) es la práctica de ingeniería de costos cloud que une los equipos de finanzas, tecnología y negocio para optimizar el gasto en cloud de forma continua; aplicado a IA, FinOps para IA extiende estas prácticas para gestionar los costos específicos de inferencia, entrenamiento y almacenamiento de modelos con la misma disciplina con que se gestiona el costo de compute general. La FinOps Foundation define tres fases: Inform (visibilidad y atribución de costos), Optimize (reducción activa del gasto sin degradar capacidad), y Operate (cultura continua de responsabilidad de costos); para plataformas de IA, la fase de Inform requiere instrumentación adicional respecto al cloud nativo (tagging de GPU hours por experimento, atribución de tokens de LLM por aplicación, visibilidad del costo del feature store por equipo). Las herramientas de FinOps para IA incluyen: AWS Cost Explorer con cost allocation tags para atribución, GCP Billing con BigQuery export para análisis ad-hoc, Kubecost para costos de Kubernetes, y LLM cost tracking integrado en el gateway con reporting a las mismas herramientas de FinOps. Un modelo de costos de IA bien implementado permite a los product managers tener visibilidad del "costo por query" o "costo por usuario activo mensual" de sus features de IA, posibilitando decisiones de pricing y priorización de optimizaciones basadas en el margen real de cada feature.

## Prácticas de FinOps aplicadas a plataformas de IA

- Unit economics de IA: calcular y publicar el costo por unidad de valor de negocio: costo por predicción, costo por query LLM, costo por usuario activo diario que usa features de IA; permite decisiones de ROI explícitas
- Reserved capacity para GPU: GPU Reserved Instances (AWS) o Committed Use Discounts (GCP) para carga base predecible de producción; reducción del 40-60% vs on-demand; spot/preemptible solo para training
- Rightsizing de clusters: análisis mensual de utilización de recursos (CPU, memoria, GPU) de los pods del training cluster; reducir las resource requests y limits a lo que realmente se usa para reducir el desperdicio
- Spot instance strategy para training: usar AWS Spot Instances o GCP Preemptible VMs para training jobs tolerantes a interrupciones, con checkpointing cada N minutos para recuperar el progreso; reducción de costo del 60-90%
- Cost anomaly detection: alertas automáticas cuando el gasto diario de un equipo supera 2x su gasto diario promedio de los últimos 30 días; investigación proactiva antes de que el gasto escale a final de mes

## Para recordar

FinOps para IA requiere que los equipos de ingeniería adopten responsabilidad por los costos que generan sus decisiones técnicas: qué modelo seleccionan, qué contexto envían, qué frecuencia de reentrenamiento configuran; sin esa responsabilidad, las optimizaciones son esfuerzos aislados sin efecto sostenido.
