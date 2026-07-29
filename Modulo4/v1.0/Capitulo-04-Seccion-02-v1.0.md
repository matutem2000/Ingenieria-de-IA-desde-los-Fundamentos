# Módulo 4 – Capítulo 04 – Sección 02

## Componentes de un Agente

Un agente de IA productivo no es un LLM con acceso a herramientas. Es un sistema con arquitectura interna propia, donde cada componente tiene una responsabilidad específica y una interfaz definida. Entender esa arquitectura interna es el requisito previo para diseñar agentes que sean predecibles, mantenibles y observables. La ausencia de ese diseño explícito es la causa más frecuente de agentes que funcionan en demos pero fallan en producción.

El primer componente es el modelo de razonamiento, que es el motor de toma de decisiones del agente. El modelo recibe el contexto actual — el objetivo, el historial de pasos previos, las observaciones de las herramientas ejecutadas — y produce la decisión del siguiente paso: qué herramienta invocar, con qué parámetros, o si el objetivo ha sido alcanzado. La elección del modelo de razonamiento es una decisión arquitectónica con consecuencias significativas en costo y latencia: modelos más potentes (GPT-4o, Claude 3.5 Sonnet) producen mejor razonamiento en tareas complejas pero son más costosos por llamada. En un agente que puede ejecutar decenas de pasos para completar una tarea, el costo acumulado de tokens puede ser sustancial. Una estrategia es utilizar un modelo ligero para pasos de razonamiento simples y un modelo potente solo cuando se detecta alta complejidad.

El segundo componente es la memoria, y es donde la arquitectura de agentes se diferencia de manera más significativa de un chatbot. La memoria de un agente opera en dos niveles fundamentales:

- **Memoria episódica (corto plazo):** el contexto de la sesión actual o tarea en curso. Incluye el objetivo, los pasos ejecutados, las observaciones recibidas y el estado actual. Esta memoria vive en la ventana de contexto del modelo o en una estructura de datos en memoria que se serializa y deserializa entre llamadas al LLM. Su limitación es la ventana de contexto: a medida que el agente ejecuta más pasos, el historial crece y puede superar el límite del modelo.
- **Memoria semántica (largo plazo):** conocimiento persistente entre sesiones. Puede incluir el perfil del usuario, las preferencias aprendidas, el resultado de investigaciones previas, o el estado de tareas de larga duración. Esta memoria se almacena externamente — en una base de datos relacional, un vector store o un sistema de almacenamiento de clave-valor — y el agente la consulta cuando es relevante para la tarea actual.

La gestión del crecimiento de la memoria episódica es un problema de diseño real. Estrategias como la compresión del historial (resumir pasos previos en lugar de conservarlos íntegros), la paginación del contexto, o el archivado selectivo de pasos relevantes deben considerarse desde el diseño inicial para agentes destinados a tareas de larga duración.

El tercer componente es el registro de herramientas (tool registry). Las herramientas son las acciones que el agente puede ejecutar: búsquedas en bases de datos, llamadas a APIs externas, ejecución de código, lectura y escritura de archivos, o cualquier función del sistema que haya sido envuelta con una interfaz compatible con el protocolo de herramientas del modelo. El registro de herramientas es el catálogo de capacidades del agente: qué puede hacer, cómo se llama cada herramienta, qué parámetros acepta y qué devuelve. La calidad de las descripciones de las herramientas en el registro es crítica: el modelo decide qué herramienta usar basándose en esas descripciones, y una descripción ambigua produce invocaciones incorrectas.

El cuarto componente es el bucle de observación-acción (observation-action loop), que es el ciclo de ejecución del agente. El bucle tiene la siguiente estructura: el modelo de razonamiento recibe el estado actual y produce una acción (herramienta a invocar y parámetros); la herramienta se ejecuta y produce una observación (resultado de la ejecución); la observación se incorpora al contexto; y el ciclo se repite hasta que el modelo decide que el objetivo ha sido alcanzado o se supera un límite configurado de iteraciones. La gestión de fallos en el bucle — qué sucede si la herramienta devuelve un error, si el modelo produce una invocación con formato incorrecto, o si el timeout del paso es superado — debe estar explícitamente diseñada.

Los parámetros de configuración del agente que deben establecerse en el diseño incluyen:

- **Número máximo de iteraciones:** límite absoluto del número de pasos antes de terminar con error. Previene bucles infinitos.
- **Timeout por paso:** tiempo máximo permitido para la ejecución de una herramienta individual.
- **Política de reintento:** qué hacer si una herramienta falla (reintentar, usar herramienta alternativa, escalar a humano).
- **Umbral de confianza:** cuándo el agente debe pausar y solicitar confirmación antes de ejecutar una acción de alto impacto.

La arquitectura interna de un agente bien diseñado convierte al modelo de lenguaje en un tomador de decisiones informado, no en un generador de texto sin control. La siguiente sección explora uno de los aspectos más complejos de los agentes de larga duración: cómo gestionar el estado y la memoria cuando la tarea se extiende a través de múltiples sesiones o cuando el contexto crece más rápido de lo que la ventana del modelo puede absorber.
