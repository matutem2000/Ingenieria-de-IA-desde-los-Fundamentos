# Módulo 8 – Capítulo 02 – Sección 04

## AWQ (Activation-aware Weight Quantization): menor pérdida de calidad que GPTQ

Tanto GPTQ como los K-quants de GGUF tratan los pesos del modelo de forma relativamente uniforme, aplicando el mismo proceso de cuantización a todos los canales de una capa (con diferencias en sofisticación del algoritmo, pero no en la información usada para decidir qué cuantizar agresivamente y qué proteger). AWQ parte de una observación diferente y más poderosa: los pesos no son uniformemente importantes para la calidad del modelo, y los pesos que afectan más al output son precisamente los que corresponden a las activaciones de mayor magnitud en el dataset de calibración. Si se pueden identificar y proteger estos pesos críticos, el resto puede cuantizarse más agresivamente con menor impacto total en la calidad.

AWQ (Activation-aware Weight Quantization), desarrollada por Lin et al. del MIT-Han Lab en 2023, implementa esta intuición de forma matemáticamente elegante. El proceso de cuantización analiza las estadísticas de activación en un dataset de calibración (128 a 512 muestras son suficientes) e identifica el 1% de los canales de salida con activaciones de mayor magnitud media. En lugar de proteger directamente estos canales aplicando más bits —lo que rompería la uniformidad del formato de cuantización y complicaría la implementación de kernels eficientes— AWQ aplica un scaling matemático previo: escala los pesos importantes en un factor `s > 1` y las activaciones correspondientes en `1/s`, preservando la equivalencia matemática de la capa pero haciendo que la cuantización introduzca un error relativo menor en los canales importantes. El resultado es un modelo INT4 con calidad consistentemente superior a GPTQ para el mismo nivel de compresión, especialmente pronunciado en modelos pequeños de 1B-7B donde la cuantización agresiva tiene mayor impacto relativo.

La ventaja operativa más inmediata de AWQ respecto a GPTQ es la velocidad de cuantización: el proceso completo para un modelo de 7B tarda minutos en lugar de horas porque no resuelve sistemas de ecuaciones de segunda orden. Esto hace que AWQ sea especialmente relevante para equipos que iteran frecuentemente entre versiones de modelos fine-tuneados y necesitan re-cuantizar en cada iteración del ciclo de desarrollo. La integración con el ecosistema de producción es también directa: el paquete `autoawq` genera modelos compatibles con vLLM directamente mediante:

```python
from awq import AutoAWQForCausalLM
model = AutoAWQForCausalLM.from_pretrained("meta-llama/Llama-3.1-8B-Instruct")
model.quantize(tokenizer, quant_config={"zero_point": True, "q_group_size": 128, "w_bit": 4})
model.save_quantized("./Llama-3.1-8B-Instruct-AWQ")
```

Los modelos resultantes se cargan en vLLM con `--quantization awq` sin configuración adicional, permitiendo usar el mismo pipeline de serving para modelos en FP16, GPTQ y AWQ con un único flag de diferencia.

En benchmarks comparativos sobre Llama 2-7B, AWQ-4bit logra perplexity de 5.78 en WikiText-2 versus 5.84 de GPTQ-4bit y 5.47 del modelo FP16 original. Esta diferencia de 0.06 puntos representa una degradación relativa aproximadamente 40% menor que GPTQ. Para modelos más grandes (13B o más), la diferencia entre AWQ y GPTQ se reduce porque ambos métodos tienen más "presupuesto" de bits para mantener la calidad. Los modelos AWQ se distribuyen en Hugging Face con el sufijo `-AWQ` en el nombre del repositorio, incluyen un archivo `quant_config.json` y son compatibles con carga directa en `transformers` desde la versión 4.35.

## Componentes principales de AWQ

- **Búsqueda de canales importantes:** análisis de estadísticas de activación en 128-512 muestras; identifica el 1% de canales con mayor magnitud media de activación; proceso en minutos, no horas.
- **Scaling pre-cuantización:** escala matemática de pesos y activaciones para reducir el error de cuantización en canales importantes sin cambiar el formato de representación.
- **Compatibilidad con vLLM:** modelos AWQ son compatibles de forma nativa con vLLM vía `--quantization awq`; también compatibles con transformers directamente desde la versión 4.35.
- **Formato de distribución:** SafeTensors con `quant_config.json`; identificables por el sufijo `-AWQ` en Hugging Face.
- **Comparación de calidad:** AWQ-4bit logra degradación de perplexity aproximadamente 40% menor que GPTQ-4bit para modelos de 7B; diferencia se reduce para modelos de 13B o más.

> **Nota del Arquitecto:** AWQ ha desplazado a GPTQ como primera opción de cuantización para GPU en muchos equipos porque combina lo mejor de dos mundos: mejor calidad que GPTQ y proceso de cuantización 10-20x más rápido. Si estás comenzando un proyecto y necesitas cuantización para GPU, AWQ es el punto de inicio recomendado. Si tu stack ya usa GPTQ con exllamav2 y el throughput es el factor dominante, el cambio puede no justificarse sin benchmarking específico.

La elección entre GGUF, GPTQ y AWQ depende del hardware objetivo, la librería de inferencia usada y la frecuencia de iteración sobre modelos. La sección siguiente pone estas alternativas en perspectiva con una comparación directa de las variantes más comunes, incluyendo los números de calidad y velocidad que permiten tomar decisiones informadas para un proyecto específico.

---
