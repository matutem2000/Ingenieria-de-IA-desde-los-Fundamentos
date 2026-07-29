# Módulo 7 – Capítulo 03 – Sección 01

# Anatomía de una herramienta: nombre, descripción, esquema de parámetros y respuesta

Una herramienta en el contexto de sistemas agénticos es una función con una interfaz definida formalmente que el LLM puede invocar mediante function calling: tiene un nombre único que actúa como identificador semántico, una descripción en lenguaje natural que el modelo usa para decidir cuándo y por qué usarla, un esquema JSON Schema que especifica los parámetros de entrada con sus tipos y restricciones, y una respuesta estructurada que el agente incorpora como observación en el contexto. Esta interfaz es la unidad fundamental de extensibilidad agéntica: todo lo que un agente puede hacer en el mundo real —buscar en la web, ejecutar código, leer archivos, llamar APIs— está mediado por esta estructura. La calidad de la descripción de la herramienta tiene un impacto directo en la precisión con la que el LLM selecciona la herramienta correcta: una descripción pobre lleva a invocaciones incorrectas incluso cuando la implementación subyacente es perfecta.

## Componentes principales

- **Nombre**: identificador sin espacios que el LLM usa para invocar la herramienta; debe ser un verbo-objeto descriptivo (`search_web`, `execute_python`, `read_file`) que comunique la acción de forma inequívoca
- **Descripción**: texto en lenguaje natural (50-200 palabras recomendado) que explica qué hace la herramienta, cuándo usarla y cuándo NO usarla; este campo es el principal mecanismo de control de selección de herramientas
- **JSON Schema de parámetros**: especificación formal de los inputs usando el estándar JSON Schema (type, description, enum, required, format); tipos soportados: string, number, boolean, array, object; el campo `description` de cada parámetro es igualmente crítico
- **Tipo de retorno y formato**: la respuesta debe ser serializable a string para incorporarse al contexto del LLM; formatos recomendados: texto plano para resultados simples, JSON estructurado para datos complejos, con límite de longitud para evitar overflow de contexto
- **Metadatos de herramienta**: información adicional como si la herramienta requiere confirmación humana, si es idempotente, su latencia esperada y su tasa de error; útil para sistemas de routing y priorización de herramientas

## Principio rector

Una herramienta mal descrita es más peligrosa que una herramienta con bugs: los bugs en la implementación producen errores detectables, mientras que una descripción ambigua produce invocaciones incorrectas silenciosas que generan resultados plausibles pero equivocados.
