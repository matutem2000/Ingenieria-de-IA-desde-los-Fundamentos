# Módulo 9 – Capítulo 08 – Sección 03

# Trazabilidad de decisiones: explicabilidad y atribución en sistemas de IA

La trazabilidad de decisiones en sistemas de IA responde a la pregunta de por qué el sistema produjo un output específico dado un input específico, lo cual es crítico tanto para seguridad (análisis forense de incidentes) como para compliance regulatorio (el EU AI Act y el GDPR exigen explicabilidad de decisiones automatizadas que afectan a personas). Para LLMs, la explicabilidad completa en el sentido matemático (por qué exactamente este output dado exactamente este input) es computacionalmente intractable para modelos de producción; pero la trazabilidad práctica —qué documentos RAG fueron recuperados, qué tool calls se ejecutaron, qué score de clasificadores se obtuvo, qué versión del system prompt estaba activa— es suficiente para la mayoría de los casos de uso regulatorio y forense. La diferencia entre explicabilidad y trazabilidad es importante: la explicabilidad intenta responder "por qué el modelo tomó esta decisión"; la trazabilidad registra "qué inputs, herramientas y contexto estaban presentes cuando el sistema produjo este output".

## Aspectos técnicos

- Chain of thought logging: en sistemas que usan CoT (chain of thought) o extended thinking, el razonamiento intermedio del modelo debe registrarse como parte del log del request — es la mejor aproximación disponible a la explicabilidad del proceso de decisión y es crítica para análisis forense (¿el modelo razonó incorrectamente o fue manipulado?)
- Atribución de documentos RAG: cada afirmación factual en el output del modelo debe ser atribuible a un documento fuente específico del corpus RAG; sistemas como LlamaIndex y LangChain soportan citation generation que incluye el chunk de documento y su score de similitud en la respuesta — este mecanismo es tanto de explicabilidad (el usuario sabe de dónde viene la información) como de trazabilidad forense
- Versioning del system prompt: el sistema debe registrar con qué versión exacta del system prompt se procesó cada request; un cambio en el system prompt puede cambiar significativamente el comportamiento del modelo, y sin versioning es imposible determinar si un comportamiento anómalo se debe a un ataque o a un cambio no autorizado del prompt
- Model card y version tracking: el model_id + version debe registrarse en cada request; en sistemas que usan múltiples modelos (un clasificador para el input, un LLM para la generación, otro para output scoring), cada componente debe estar versionado y su versión registrada en el log del request
- Decision audit trail para sistemas de alto impacto: en sistemas donde la IA toma o influye en decisiones que afectan a personas (préstamos, diagnósticos, contratación), el audit trail debe incluir el output del modelo, los documentos de contexto, el confidence score, cualquier override humano, y el outcome final — suficiente para una revisión regulatoria post-hoc

## Para recordar

La trazabilidad de decisiones en sistemas de IA no es lo mismo que la explicabilidad matemática del modelo, sino el registro completo de las condiciones bajo las que se produjo cada output: versión del modelo, version del system prompt, documentos recuperados, tool calls ejecutadas y scores de clasificadores — suficiente para análisis forense y compliance regulatorio.
