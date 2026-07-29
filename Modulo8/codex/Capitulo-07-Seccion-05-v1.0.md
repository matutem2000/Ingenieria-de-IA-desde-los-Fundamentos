# Módulo 8 – Capítulo 07 – Sección 05

# Optimización de costos: batching, cuantización y selección de instancia correcta

La optimización de costos en inferencia de LLMs en la nube opera en tres niveles independientes pero complementarios: el nivel de request (maximizar el batch size para amortizar el costo fijo de cargar pesos en VRAM entre múltiples requests), el nivel de modelo (elegir la cuantización que minimiza el tamaño de instancia necesaria sin degradar la calidad), y el nivel de instancia (seleccionar el tipo de GPU que ofrece el mejor ratio tokens/dólar para el throughput requerido). El batching es el mecanismo de mayor impacto: una GPU A10G sirviendo requests individuales puede procesar 100-200 tokens/s, pero con continuous batching de vLLM sirviendo 16 requests simultáneas puede superar los 1.500 tokens/s (un factor de 7-15x); el costo por token se reduce proporcionalmente, pasando de ~0.007 USD por 1K tokens a ~0.0005 USD por 1K tokens con el mismo hardware. La cuantización reduce directamente el costo de instancia: servir un modelo de 13B en Q4 requiere una GPU de 8 GB VRAM (g5.xlarge con A10G de 24 GB es más que suficiente) vs 28 GB en BF16 (requiere múltiples GPUs o una A100); la diferencia de costo entre estas instancias puede ser de 3-5x. La selección de instancia requiere calcular el ratio de tokens/hora por dólar: una g5.xlarge (A10G, 1.006 USD/hora) sirviendo Llama 3 8B Q4 a 1.500 tokens/s genera 5.4M tokens/hora a un costo de 0.187 USD/1M tokens, mientras una p4d.24xlarge (8xA100, 32.77 USD/hora) generando 20.000 tokens/s produce 72M tokens/hora a 0.455 USD/1M tokens — la instancia más cara no siempre tiene mejor costo por token.

## Estrategias de optimización de costos en la nube

- Spot para entrenamiento + on-demand para inferencia: la división más simple y efectiva; el 90% del costo de entrenamiento puede reducirse con Spot; para inferencia con SLA, on-demand o reserved instances (hasta 60% de descuento con compromiso de 1-3 años)
- Reserved Instances (RI) o Savings Plans: AWS reservations de 1 o 3 años para instancias de inferencia con demanda predecible reducen el costo 30-60% respecto on-demand; adecuado cuando el workload de inferencia tiene al menos 50% de utilización constante
- Prefix caching para workloads con prompts compartidos: en aplicaciones donde muchos usuarios comparten el mismo system prompt largo, el prefix caching de vLLM reduce el costo de prefill eliminando el computo redundante; puede reducir el compute de prefill en 70-90% en aplicaciones multi-tenant con prompts largos estáticos
- Right-sizing de instancias: usa `nvidia-smi dmon -s u` para monitorear el uso real de VRAM y GPU compute; una GPU al 30% de utilización promedio indica que la instancia es demasiado grande; considera bajar al tier inferior o incrementar el batch size para aumentar la utilización
- Cost per token tracking: instrumentar el sistema para calcular y registrar el costo por 1K tokens en tiempo real (costo_hora / (tokens_generados / 3600)); permite detectar regresiones de eficiencia al actualizar el modelo o la configuración y tener un KPI de negocio claro

## Para recordar

El costo de inferencia de LLMs en la nube se puede reducir 3-10x con las optimizaciones correctas de batching y cuantización antes de considerar cambiar de proveedor o de tipo de instancia.
