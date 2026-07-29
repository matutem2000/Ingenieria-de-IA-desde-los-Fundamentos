# Módulo 7 – Capítulo 03 – Sección 06

# Cierre: las herramientas son la interfaz entre el razonamiento del agente y el mundo real

El capítulo sobre tool use establece que las herramientas son el punto de contacto entre el razonamiento interno del agente —que ocurre en el espacio de tokens del LLM— y el mundo externo donde existen APIs, bases de datos, sistemas de archivos y usuarios. La calidad de esta interfaz determina cuánto del potencial de razonamiento del agente puede materializarse en acciones útiles: un agente con razonamiento excelente pero herramientas mal diseñadas producirá resultados mediocres porque sus decisiones no podrán ejecutarse con precisión. Inversamente, herramientas bien diseñadas pueden compensar parcialmente debilidades en el razonamiento, ya que descripciones precisas guían al modelo hacia el uso correcto. El diseño de herramientas es ingeniería de software más ingeniería de prompts simultáneamente: la implementación debe ser robusta, la descripción debe ser inequívoca, la respuesta debe ser informativa y el manejo de errores debe ser predecible. Tratar cada herramienta como un microservicio con su contrato de API, sus SLOs de latencia y sus políticas de error es la práctica correcta.

## Principio rector

Las herramientas son código; sus descripciones son prompts; y los bugs en ambas tienen consecuencias igualmente reales en el comportamiento del agente en producción.

*"Any sufficiently advanced technology is indistinguishable from magic. But magic that fails silently is just a bug with a good story."* — paráfrasis de Arthur C. Clarke aplicada al context de tool use agéntico: la magia de function calling solo funciona si la interfaz entre el razonamiento y la ejecución está definida con la misma precisión que cualquier API de producción.
