# Módulo 8 – Capítulo 03 – Sección 03

# Modelfile: personalización de parámetros de sistema, temperatura y comportamiento

El Modelfile de Ollama es un archivo de configuración declarativo, similar en concepto a un Dockerfile, que define cómo construir y personalizar un modelo local: especifica el modelo base a usar, el system prompt, los parámetros de sampleo y las instrucciones de conversación de ejemplo para guiar el comportamiento del modelo en una aplicación específica. El comando `ollama create mi-asistente -f ./Modelfile` genera un nuevo modelo derivado registrado localmente bajo el nombre `mi-asistente`, que puede ejecutarse con `ollama run mi-asistente` y publicarse en el registro con `ollama push usuario/mi-asistente`. Los parámetros de sampleo configurables en el Modelfile incluyen `temperature` (aleatoriedad, 0.0 a 2.0), `top_p` (nucleus sampling), `top_k` (top-k sampling), `repeat_penalty` (penalización de repetición), `num_ctx` (tamaño de ventana de contexto en tokens) y `num_predict` (número máximo de tokens a generar), permitiendo optimizar el comportamiento del modelo para casos de uso específicos sin modificar los pesos. La instrucción `TEMPLATE` del Modelfile permite sobrescribir el chat template por defecto del modelo, lo cual es útil cuando se usa un modelo base (no instruction-tuned) que requiere un formato de prompt específico diferente al estándar de la familia.

## Componentes del Modelfile

- `FROM <modelo>`: especifica el modelo base como punto de partida; puede ser un nombre del registro de Ollama (`llama3:8b`), una ruta local a un archivo GGUF (`/ruta/a/modelo.gguf`) o un nombre de otro Modelfile creado previamente
- `SYSTEM "<texto>"`: define el system prompt que se prepend a cada conversación; es el mecanismo primario para dar identidad, restricciones y comportamiento específico al asistente
- `PARAMETER <nombre> <valor>`: establece parámetros de inferencia; los más críticos son `temperature 0.7`, `num_ctx 4096`, `repeat_penalty 1.1` y `stop "<token>"` para definir tokens de parada personalizados
- `MESSAGE <rol> <contenido>`: inyecta ejemplos de conversación few-shot directamente en el Modelfile; útil para demostrar el formato de respuesta esperado sin modificar el system prompt
- `TEMPLATE "{{ .System }}{{ .Prompt }}"`: permite definir el formato exacto de concatenación del contexto; debe coincidir con el formato usado durante el instruction tuning del modelo base para máxima efectividad

## Para recordar

El Modelfile es la capa de personalización que convierte un modelo general en un asistente especializado sin fine-tuning: un system prompt bien diseñado y los parámetros de sampleo correctos pueden mejorar dramáticamente la adecuación del modelo a la tarea específica.
