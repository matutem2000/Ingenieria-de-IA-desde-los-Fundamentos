# Módulo 9 – Capítulo 01 – Sección 01

# La superficie de ataque de los sistemas de IA: qué es nuevo respecto a sistemas tradicionales

Los sistemas de IA introducen vectores de ataque que no existen en el software tradicional: el modelo mismo —sus pesos, su comportamiento ante inputs inusuales y su capacidad de seguir instrucciones en lenguaje natural— es una superficie de ataque activa. A diferencia de una API REST convencional donde el servidor ejecuta lógica determinista, un LLM como GPT-4 o Claude 3 puede ser inducido a cambiar su comportamiento mediante texto cuidadosamente construido, sin necesidad de explotar una vulnerabilidad en el código. El embedding space de los modelos de representación y los vectorstores como Pinecone o Weaviate agregan superficies de ataque adicionales que no tienen equivalente en sistemas CRUD clásicos. Esta expansión de la superficie de ataque requiere repensar fundamentalmente los modelos de amenaza aplicados al software.

## Componentes de la nueva superficie de ataque

- Model input surface: el prompt —en texto, imágenes, audio o documentos— es un vector de entrada no sanitizable mediante reglas tradicionales de WAF
- Model weights y fine-tuning pipeline: los pesos del modelo pueden ser adulterados durante fine-tuning con datasets contaminados, modificando el comportamiento del modelo en producción
- Retrieval layer (RAG): los índices vectoriales y los documentos recuperados son superficies de inyección de instrucciones maliciosas que el modelo ejecutará como parte de su contexto
- Tool-calling interface: en sistemas agénticos, las herramientas expuestas al modelo (ejecutar código, llamar APIs, leer archivos) amplifican el impacto de cualquier ataque exitoso
- Output processing pipeline: las respuestas del modelo pueden contener código malicioso, instrucciones de rendering o exfiltración de datos si se renderizan sin sanitización

## Principio rector

La superficie de ataque de un sistema de IA incluye cada capa del pipeline —desde el input del usuario hasta los pesos del modelo— y cada capa debe tener controles de seguridad independientes porque ninguna capa es confiable por sí sola.
