# Módulo 5 – Capítulo 03 – Sección 01

# Por qué usar un framework de orquestación: abstracción, cadenas y composición

Los frameworks de orquestación como LangChain y LlamaIndex emergen como respuesta a la complejidad creciente de los flujos de IA que encadenan múltiples llamadas al modelo, recuperación de documentos, ejecución de herramientas y gestión de memoria conversacional: código que sin framework requiere centenares de líneas con gestión manual de estado, con framework se reduce a una composición declarativa de componentes. La abstracción central que ofrecen es la idea de una "cadena" o "pipeline": una secuencia de pasos donde la salida de uno es la entrada del siguiente, con manejo automático de tipos, serialización y propagación de errores. LangChain Expression Language (LCEL) modela esta composición con el operador `|`: `chain = prompt | llm | parser` crea un objeto ejecutable que maneja internamente el formateo del prompt, la llamada al LLM, el parseo de la respuesta y el retry si el parseo falla. Esta abstracción facilita la intercambiabilidad de componentes: cambiar el proveedor de LLM en una cadena LCEL requiere cambiar solo el objeto `llm` sin tocar el resto del flujo.

## Conceptos clave de la orquestación

- Cadena (chain): secuencia de pasos que transforma una entrada en una salida mediante llamadas a LLMs, herramientas y transformaciones de datos; es la unidad de composición fundamental en frameworks de orquestación
- Runnable interface (LCEL): protocolo común en LangChain que implementan todos los componentes con métodos `invoke()`, `stream()` y `batch()`, permitiendo conectarlos con `|` independientemente de su tipo interno
- Memory y state management: los frameworks proveen abstracciones para mantener historial conversacional en memoria, Redis, bases de datos SQL o vectoriales, con compresión automática cuando el contexto excede el límite del modelo
- Composición declarativa vs imperativa: declarar el flujo como composición de componentes facilita la inspección, el testing por partes y la modificación sin tocar la lógica de integración
- Observabilidad integrada: LangChain emite callbacks en cada paso de la cadena que herramientas como LangSmith capturan automáticamente sin modificar el código de la aplicación

## Principio rector

Un framework de orquestación justifica su adopción cuando el beneficio en legibilidad, mantenibilidad y reutilización de componentes supera el costo de aprender su modelo mental y gestionar sus actualizaciones frecuentes de API.
