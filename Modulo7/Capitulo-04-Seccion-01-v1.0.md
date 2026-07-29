# Módulo 7 – Capítulo 04 – Sección 01

# Tipos de memoria: in-context, episódica, semántica y procedimental

La memoria en sistemas agénticos no es un componente único sino un conjunto heterogéneo de mecanismos de almacenamiento y recuperación que operan en diferentes escalas temporales y con diferentes semánticas de acceso. La memoria in-context es la más inmediata: es el historial de mensajes y observaciones que cabe dentro de la ventana de contexto activa del LLM (128K tokens en GPT-4o, 200K en Claude 3.5 Sonnet); todo lo que está aquí es accesible directamente por el modelo sin operación de recuperación. La memoria episódica almacena experiencias pasadas del agente —conversaciones previas, tareas completadas, errores cometidos— en almacenamiento externo (PostgreSQL, Redis, S3) y se recupera selectivamente cuando es relevante. La memoria semántica contiene conocimiento factual del dominio, almacenado típicamente en vectorstores (Pinecone, Weaviate, Chroma) con recuperación por similaridad semántica. La memoria procedimental codifica habilidades y workflows reutilizables, análogos a funciones que el agente puede invocar sin razonar sobre ellas desde cero.

## Conceptos clave

- **Memoria in-context**: contenido actualmente disponible en la ventana de contexto del LLM; acceso instantáneo sin latencia adicional pero limitado por el tamaño de la ventana y degradación de atención en contextos muy largos (lost-in-the-middle problem)
- **Memoria episódica**: registro de interacciones y eventos pasados con timestamps; almacenada externamente y recuperada mediante búsqueda por metadata (fecha, usuario, tarea) o por similitud semántica del texto del episodio
- **Memoria semántica**: conocimiento factual y conceptual del dominio almacenado como embeddings en vectorstores; recuperada mediante búsqueda approximate nearest neighbor (ANN) con modelos como text-embedding-3-large o voyage-3
- **Memoria procedimental**: workflows, reglas de negocio y heurísticas aprendidas almacenados como texto estructurado o como prompts especializados; se inyectan en el contexto cuando la tarea en curso las requiere
- **Working memory**: subset del contexto activo que el agente mantiene actualizado como estado de la tarea actual; análogo al `AgentState` en LangGraph, que persiste entre iteraciones del ciclo agéntico

## Principio rector

Los cuatro tipos de memoria no son alternativos sino complementarios: un agente de producción usa memoria in-context para el razonamiento inmediato, memoria episódica para aprender de interacciones pasadas, memoria semántica para acceso a conocimiento del dominio y memoria procedimental para reutilizar workflows ya validados.
