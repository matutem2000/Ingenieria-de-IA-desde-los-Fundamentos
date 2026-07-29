# Módulo 8 – Capítulo 03 – Sección 03

## Modelfile: personalización de parámetros de sistema, temperatura y comportamiento

Un modelo general descargado desde el registro de Ollama produce respuestas genéricas que pueden ser adecuadas para exploración pero raramente son suficientes para un caso de uso de producto. El asistente de soporte técnico de una empresa necesita conocer el tono correcto, las restricciones de lo que puede y no puede responder, y el formato exacto de sus salidas. El agente de análisis de contratos legales necesita precisión sobre creatividad y debe rechazar preguntas fuera del dominio. El Modelfile de Ollama es el mecanismo que transforma un modelo general en un asistente especializado sin modificar un solo peso del modelo base.

El Modelfile sigue una sintaxis declarativa similar a un Dockerfile: cada instrucción define un aspecto del comportamiento del modelo derivado. La instrucción `FROM` especifica el punto de partida, que puede ser un modelo del registro de Ollama (`llama3:8b`), una ruta local a un archivo GGUF (`/ruta/a/modelo.gguf`) o incluso el nombre de otro Modelfile creado previamente, permitiendo composición de personalizaciones. La instrucción `SYSTEM` define el system prompt que se antepone a cada conversación y es el mecanismo primario para establecer la identidad, el dominio y las restricciones del comportamiento del asistente. La instrucción `PARAMETER` ajusta los parámetros de sampleo que determinan cómo el modelo selecciona el siguiente token: `temperature 0.1` para respuestas deterministas en tareas de extracción, `temperature 0.9` para mayor creatividad en generación de contenido, `num_ctx 8192` para ampliar la ventana de contexto más allá del default de 4096, `repeat_penalty 1.1` para reducir la tendencia del modelo a repetir frases.

Una vez escrito el Modelfile, el comando `ollama create mi-asistente -f ./Modelfile` registra el modelo derivado localmente bajo el nombre `mi-asistente`, disponible inmediatamente via `ollama run mi-asistente` o via API con `model: "mi-asistente"`. Para compartir el modelo derivado en un equipo, `ollama push usuario/mi-asistente` lo publica en el registro de Ollama privado o público. El Modelfile completo se puede recuperar de un modelo existente con `ollama show --modelfile mi-asistente`, facilitando la inspección y modificación de modelos creados por otros miembros del equipo.

La instrucción `TEMPLATE` del Modelfile cubre un caso especial importante: cuando se usa un modelo base que no ha sido instruction-tuned, o cuando el chat template por defecto del modelo no produce los resultados esperados, `TEMPLATE` permite especificar explícitamente el formato de serialización de la conversación. Esto es crítico porque el chat template incorrecto introduce tokens de control visibles en las respuestas o degrada la calidad del instruction following sin mensajes de error explícitos. Para modelos Llama 3, el template correcto incluye los tokens especiales `<|begin_of_text|>`, `<|start_header_id|>` y `<|eot_id|>` en las posiciones exactas que el modelo espera.

La instrucción `MESSAGE` permite inyectar ejemplos de conversación few-shot directamente en el Modelfile: `MESSAGE user "¿Puedes analizar este contrato?"` seguido de `MESSAGE assistant "Claro, voy a identificar..."` establece el patrón de respuesta esperado sin ocupar espacio del context window de cada petición individual. Esto es más eficiente que incluir los ejemplos en el system prompt porque llama.cpp puede cachear el KV del Modelfile entre peticiones, reduciendo el costo de prefill.

## Componentes del Modelfile

- **`FROM <modelo>`:** modelo base o ruta a archivo GGUF; puede ser un nombre del registro, una ruta local o el nombre de otro Modelfile.
- **`SYSTEM "<texto>"`:** system prompt antepuesto a cada conversación; mecanismo primario para definir identidad, dominio y restricciones del asistente.
- **`PARAMETER <nombre> <valor>`:** parámetros de inferencia clave: `temperature`, `num_ctx`, `repeat_penalty`, `top_p`, `top_k`, `stop "<token>"`.
- **`MESSAGE <rol> <contenido>`:** ejemplos few-shot inyectados en el Modelfile; el KV cache los comparte entre peticiones, reduciendo el costo de prefill.
- **`TEMPLATE "{{ .System }}{{ .Prompt }}"`:** formato de serialización de la conversación; debe coincidir con el chat template del modelo base para máxima efectividad.

> **Nota del Arquitecto:** El System prompt es el parámetro de mayor impacto en el comportamiento del modelo derivado, y también el más difícil de diseñar bien. Un System prompt efectivo define no solo lo que el modelo debe hacer sino explícitamente lo que no debe hacer, el tono y registro del lenguaje, el formato de las respuestas y cómo manejar preguntas fuera del dominio. Escribir y evaluar el System prompt en el golden dataset del Capítulo 1 antes de deplorar el modelo ahorra iteraciones costosas en producción.

El Modelfile es la capa de personalización que convierte un modelo general en un asistente especializado sin fine-tuning, con un ciclo de iteración de minutos. La sección siguiente muestra cómo integrar estos modelos locales en aplicaciones usando SDKs, LangChain y llamadas HTTP directas.

---
