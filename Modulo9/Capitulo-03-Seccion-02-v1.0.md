# Módulo 9 – Capítulo 03 – Sección 02

# Ataques de transferencia: ejemplos adversariales que funcionan en múltiples modelos

La transferibilidad de ataques adversariales —la propiedad de que un ejemplo adversarial generado contra un modelo A también engaña a modelos B, C y D entrenados de forma independiente— es uno de los hallazgos más perturbadores de la investigación en seguridad de ML y tiene implicaciones directas en seguridad de producción. Este fenómeno, documentado por Szegedy et al. en 2014 y extensamente analizado desde entonces, indica que los ejemplos adversariales no son artefactos del modelo específico sino que explotan propiedades geométricas del espacio de representación que son compartidas entre modelos entrenados en datos similares. En el contexto de LLMs, la transferibilidad implica que un jailbreak o un ejemplo adversarial desarrollado contra GPT-4 puede funcionar directamente contra Claude 3, Gemini Ultra o LLaMA-3 sin modificación, porque los modelos aprenden representaciones similares a pesar de sus diferencias arquitectónicas. Esto significa que un atacante puede usar un modelo open-source (LLaMA, Mistral) como surrogate para desarrollar ataques que luego transfiere a modelos propietarios sin acceso a sus internals.

## Aspectos técnicos

- Mecanismo de transferibilidad: los modelos entrenados en datasets similares aprenden decision boundaries con geometría similar en el espacio de representación; los ejemplos adversariales que cruzan el decision boundary en el espacio de un modelo tienden a cruzarlo también en modelos similares
- Surrogate model attacks: el atacante entrena o usa un modelo open-source como proxy para generar ataques adversariales con acceso whitebox (gradientes completos) y luego transfiere los ejemplos al modelo propietario target — efectivo contra GPT-4 usando GPT-2 o LLaMA como surrogate
- Transferibilidad de jailbreaks: el paper "Universal and Transferable Adversarial Attacks on Aligned Language Models" (Zou et al., 2023, CMU) demostró sufijos adversariales generados automáticamente que transfieren exitosamente de Vicuna (LLaMA fine-tuned) a GPT-3.5, GPT-4, Claude y Bard
- GCG (Greedy Coordinate Gradient): el algoritmo de Zou et al. para encontrar sufijos adversariales transferibles usa búsqueda greedy sobre tokens con gradientes del modelo surrogate, generando strings como "! ! ! ! ! ! !" que al añadirse a cualquier prompt malicioso aumentan significativamente las tasas de jailbreak
- Implicaciones para defensa: los controles de seguridad deben ser robustos ante ejemplos adversariales nunca vistos, no solo ante los conocidos — la defensa basada en blacklists de prompts conocidos es fundamentalmente insuficiente ante la transferibilidad

## Para recordar

La transferibilidad de ataques adversariales convierte a cualquier modelo open-source en una herramienta para desarrollar ataques contra modelos propietarios: la defensa no puede basarse en la opacidad del modelo sino en controles independientes del modelo que validen el comportamiento observable del sistema.
