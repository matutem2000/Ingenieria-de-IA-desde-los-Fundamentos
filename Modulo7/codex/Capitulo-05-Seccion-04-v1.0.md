# Módulo 7 – Capítulo 05 – Sección 04

# Pydantic AI: agentes tipados con validación de entrada/salida

Pydantic AI es un framework de agentes desarrollado por el equipo de Pydantic que trae el rigor de tipado estático de Python a la ingeniería agéntica: las entradas y salidas de cada agente son modelos Pydantic con validación automática, lo que convierte los contratos de interfaz entre agentes y herramientas de convenciones implícitas a contratos validados en tiempo de ejecución. A diferencia de frameworks que aceptan respuestas en texto libre y confían en el parsing posterior, Pydantic AI instruye al LLM a generar output que valide contra el schema Pydantic definido, reintentando automáticamente si la respuesta no cumple el schema. Esta garantía de estructura hace que la salida del agente sea directamente consumible por código Python sin transformación adicional, reduciendo la superficie de bugs en la integración entre el agente y el sistema que lo consume. Pydantic AI soporta OpenAI, Anthropic, Google Gemini y Groq como backends de LLM con una interfaz unificada.

## Aspectos técnicos

- **Output model typing**: el agente se define con `Agent[ResultType]` donde `ResultType` es un modelo Pydantic; el LLM genera output JSON que se valida y deserializa automáticamente a la instancia del modelo, con reintentos automáticos ante fallos de validación
- **Tool typing con Pydantic**: las herramientas se definen como funciones Python con anotaciones de tipo Pydantic; el schema JSON Schema de la herramienta se genera automáticamente de las anotaciones, eliminando la necesidad de escribirlo manualmente
- **RunContext y dependency injection**: Pydantic AI usa un sistema de inyección de dependencias (`RunContext[Dependencies]`) que provee a cada herramienta y al agente acceso a servicios externos (base de datos, HTTP client, configuración) de forma con seguridad de tipos sin variables globales
- **Structured validation retries**: cuando el LLM genera output inválido, Pydantic AI construye un mensaje de error descriptivo con los campos faltantes o incorrectos y reintenta la generación hasta `max_retries` veces antes de lanzar una excepción
- **Streaming tipado**: el método `agent.run_stream()` devuelve un stream donde los eventos intermedios disponibles mediante la API, como las llamadas a herramientas, se representan mediante objetos tipados, no texto libre, facilitando la construcción de UIs reactivas que muestran el progreso del agente

## Principio rector

Pydantic AI aplica el principio de "fallar pronto" a la integración agéntica: en lugar de descubrir en producción que la salida del agente no tiene el formato esperado, la validación en tiempo de ejecución garantiza que el output sea correcto antes de que llegue al código consumidor.
