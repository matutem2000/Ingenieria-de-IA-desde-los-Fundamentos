# Módulo 8 – Capítulo 01 – Sección 03

# Licencias: MIT, Apache 2.0, Llama Community License y sus restricciones comerciales

Las licencias de modelos de lenguaje de gran escala no son equivalentes a las licencias de software tradicional: incluso las más permisivas pueden contener cláusulas que restringen el uso comercial, la redistribución de modelos derivados o la integración en servicios con umbrales de usuarios activos. La licencia MIT, usada por modelos como Falcon-7B y algunos checkpoints de Phi-2, permite uso comercial sin restricciones, redistribución y modificación sin requerir atribución prominente en el producto final. La Apache 2.0, aplicada a Gemma 2 y a muchos modelos de Hugging Face, añade protección de patentes al licenciante y requiere preservar los avisos de copyright, pero sigue siendo compatible con uso comercial libre. La Llama Community License, aplicada a todas las variantes de Llama 2 y 3, impone restricciones específicas: no puede usarse para entrenar otros LLMs fuera del ecosistema Meta y los servicios con más de 700 millones de usuarios activos mensuales requieren una licencia comercial adicional directa con Meta.

## Aspectos técnicos de las licencias

- MIT: sin restricciones de uso, redistribución o modificación; compatible con productos propietarios; no requiere liberar código fuente derivado ni pesos modificados
- Apache 2.0: concede derechos de patente explícitos; requiere NOTICE con cambios realizados; compatible con GPL v3 pero no con GPL v2; usada por Gemma 2, StableLM y muchos modelos de Stability AI
- Llama Community License: prohíbe usar outputs del modelo para entrenar LLMs competidores; activa restricción de usuarios activos mensuales (700M MAU); cada nueva versión (Llama 3, 3.1, 3.2) requiere aceptar la licencia actualizada separadamente
- Licencias mixtas: algunos modelos como DeepSeek V2 usan MIT para los pesos pero aplican términos de uso adicionales a través de su política de uso aceptable (AUP), creando capas de restricciones que van más allá del texto de la licencia formal
- Pesos derivados: el fine-tuning de un modelo con licencia restrictiva hereda generalmente las restricciones del modelo base; distribuir un LoRA adapter sobre Llama requiere cumplir la Llama Community License incluso si el adapter en sí tiene licencia MIT

## Para recordar

Antes de integrar cualquier modelo open weights en un producto, verifica la licencia exacta del checkpoint específico que usas, ya que versiones distintas del mismo modelo pueden tener licencias diferentes.
