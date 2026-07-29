# Módulo 8 – Capítulo 04 – Sección 05

# Comparación costo-rendimiento: GPU en la nube vs hardware dedicado local

La decisión entre cloud GPU y hardware dedicado local es un análisis de punto de equilibrio (break-even analysis) que depende de las horas de uso previstas, el horizonte temporal de la inversión y los costos operativos asociados a cada opción. Una RTX 4090 de 24 GB cuesta aproximadamente 1.500-1.800 USD en 2025, mientras que una instancia `g5.xlarge` de AWS (A10G de 24 GB VRAM) cuesta 1.006 USD/hora en on-demand; esto significa que el hardware local amortiza su costo en aproximadamente 1.500/1.006 = 1.500 horas de uso continuo (~63 días operando 24/7), o alrededor de 6-9 meses si se usa 8 horas diarias. Para fine-tuning que requiere GPUs de 40-80 GB (A100/H100), el análisis cambia: el costo de una A100 SXM de 80 GB en instancias dedicadas (~10.000-30.000 USD) eleva el break-even a cientos de días de uso, haciendo que el cloud sea más económico para workloads intermitentes de entrenamiento mientras que el hardware local es más económico para inferencia continua de producción. Los costos operativos del hardware local frecuentemente ignorados incluyen electricidad (una RTX 4090 consume ~350W bajo carga, ~2.500 USD/año a tarifas europeas), cooling, mantenimiento del sistema y el costo de oportunidad del capital inmovilizado.

## Comparación costo-rendimiento

- Nube on-demand (AWS g5.xlarge con A10G 24 GB): 1.006 USD/hora, ideal para workloads intermitentes o experimentos; sin costo inicial; SLA de disponibilidad garantizado; acceso a GPUs de mayor capacidad cuando necesario
- Nube spot/preemptible (AWS EC2 Spot con A10G): 60-70% de descuento respecto on-demand; viable para entrenamiento tolerante a interrupciones; no recomendado para inferencia de producción donde las interrupciones afectan usuarios
- Hardware local (RTX 4090): 1.600 USD capex + ~250 USD/año electricidad; óptimo para equipos con uso intensivo continuo (>8h/día); máximo control sobre configuración y datos; sin costos de transferencia de datos; latencia de red cero
- Hardware de terceros dedicado (Lambda Labs, RunPod): precios intermedios (~0.50-0.80 USD/hora para A100 40 GB); más económico que AWS para GPUs de alta gama; sin el costo inicial del hardware pero con menos garantías de SLA
- Análisis de break-even real: el cloud es más económico para teams con <4 horas de uso GPU por día o con necesidades variables; el hardware local es más económico para teams con >8 horas de uso continuo y workloads predecibles

## Para recordar

El error más común en la decisión cloud vs local es ignorar los costos operativos del hardware propio y subestimar cuántas horas reales se usará la GPU; realiza el análisis de break-even con los costos totales reales, no solo el precio del hardware.
