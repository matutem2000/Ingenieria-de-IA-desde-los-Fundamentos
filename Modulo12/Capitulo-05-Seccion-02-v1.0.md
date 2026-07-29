# Módulo 12 – Capítulo 05 – Sección 02

# Implementación de controles contra prompt injection: en el agente y en el pipeline RAG

La protección contra prompt injection en el sistema integrador opera en dos capas: en el agente a nivel de system prompt y en el pipeline RAG a nivel de contenido de los documentos recuperados. En el agente, el system prompt usa delimitadores XML explícitos para separar instrucciones de sistema de datos de usuario: las instrucciones del agente están en la sección `<system_instructions>` y la query del usuario en `<user_query>`, con una instrucción explícita de que el contenido de `<user_query>` son datos a procesar, no instrucciones a ejecutar. En el pipeline RAG, cada chunk recuperado se envuelve en `<retrieved_document id="{doc_id}">` antes de incluirse en el contexto, con una instrucción que indica al modelo que estos son documentos de referencia cuyo contenido no puede modificar las instrucciones del agente. El input validator rechaza queries que contienen patrones de injection conocidos: frases como "ignora las instrucciones anteriores", "actúa como", "olvida tu rol" detectadas con una lista negra de 200 patrones en múltiples idiomas.

## Controles anti-injection implementados

- Delimitadores XML: separación estructural de instrucciones de sistema y datos de usuario en el prompt del agente
- Instrucción de grounding: el system prompt especifica que el contenido de documentos recuperados son datos, no instrucciones
- Input validator: lista negra de 200 patrones de injection en español e inglés aplicada antes de procesar la query
- Document sanitization: strip de patrones de injection conocidos en el contenido de documentos durante la ingesta
- Assertion post-retrieval: validación de que los chunks recuperados no contienen instrucciones dirigidas al sistema

## Buena práctica

La defensa contra prompt injection requiere controles en múltiples capas — ningún control individual es suficiente, y la defensa en profundidad (input validation + delimitadores en prompt + output filtering) es el estándar mínimo para sistemas en producción.
