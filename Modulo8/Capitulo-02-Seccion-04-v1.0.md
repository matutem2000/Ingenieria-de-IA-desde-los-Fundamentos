# Módulo 8 – Capítulo 02 – Sección 04

# AWQ (Activation-aware Weight Quantization): menor pérdida de calidad que GPTQ

AWQ (Activation-aware Weight Quantization), desarrollado por Lin et al. del MIT-Han Lab (2023), parte de una observación empírica clave: no todos los pesos de un modelo son igual de importantes para la calidad de la salida, y los pesos más críticos son aquellos que corresponden a activaciones de alta magnitud en el dataset de calibración. A diferencia de GPTQ, que minimiza el error cuadrático capa por capa, AWQ identifica el 1% de canales con activaciones de mayor magnitud y los protege con mayor precisión (o sin cuantizar), mientras cuantiza los canales restantes agresivamente a 4 bits. Esta decisión de diseño produce modelos con degradación de perplexity consistentemente menor que GPTQ en el mismo nivel de compresión, especialmente en modelos pequeños (1B-7B) donde la cuantización agresiva tiene mayor impacto relativo. AWQ es significativamente más rápido de generar que GPTQ: el proceso de cuantización de un modelo de 7B tarda minutos en lugar de horas porque no requiere resolver sistemas de ecuaciones de segunda orden como el OBS framework.

## Componentes principales de AWQ

- Búsqueda de canales salientes: AWQ analiza estadísticas de activación en el dataset de calibración (típicamente entre 128 y 512 muestras) e identifica los canales cuya magnitud media supera un umbral; estos canales reciben tratamiento especial de scaling antes de cuantizar
- Scaling pre-cuantización: en lugar de proteger directamente los canales importantes, AWQ escala matemáticamente los pesos y las activaciones para que la cuantización introducida tenga menor impacto perceptible; esto preserva la equivalencia matemática de la capa
- Compatibilidad con TinyChat y vLLM: AWQ tiene soporte nativo en múltiples motores de inferencia; el paquete `autoawq` genera modelos compatibles con vLLM directamente mediante `AutoAWQForCausalLM.from_pretrained()` y `model.quantize()`
- Formato de distribución: los modelos AWQ se distribuyen en SafeTensors con un archivo `quant_config.json`; el sufijo estándar en Hugging Face es `-AWQ`; son compatibles con carga directa en transformers desde la versión 4.35
- Comparación con GPTQ: en benchmarks sobre Llama 2-7B, AWQ-4bit logra perplexity de 5.78 en WikiText-2 vs 5.84 de GPTQ-4bit (vs 5.47 del modelo FP16 original), representando una degradación 40% menor en términos relativos

## Para recordar

AWQ es la opción de cuantización preferida cuando la calidad es la prioridad principal y el tiempo disponible para cuantización es limitado, especialmente en modelos de 7B o menos donde la degradación de GPTQ es más pronunciada.
