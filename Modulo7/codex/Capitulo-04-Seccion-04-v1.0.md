# Módulo 7 – Capítulo 04 – Sección 04

# Memory consolidation: comprimir y abstraer memorias episódicas en conocimiento

La consolidación de memoria es el proceso de transformar memorias episódicas brutas —transcripciones de conversaciones, logs de acciones, observaciones individuales— en representaciones más abstractas y generalizables: preferencias del usuario, patrones de comportamiento recurrentes, reglas aprendidas de casos anteriores o heurísticas de resolución de problemas. Este proceso es el análogo computacional de la consolidación de memoria durante el sueño descrita en neurociencia: múltiples episodios específicos se comprimen en esquemas conceptuales que pueden aplicarse a nuevas situaciones. En sistemas agénticos, la consolidación puede implementarse como un proceso batch que se ejecuta periódicamente (offline consolidation): un LLM analiza N sesiones recientes de un usuario y extrae patrones, preferencias y hechos relevantes que se almacenan como ítems de memoria semántica de alta prioridad. Sistemas como MemGPT implementan esto como una operación de "compactación de contexto" que el propio agente puede invocar cuando su memoria de trabajo se llena.

## Aspectos técnicos

- **Offline consolidation batch**: proceso que se ejecuta fuera del ciclo de atención del agente (p.ej. cada 24h) para analizar sesiones recientes y extraer patrones; implementado como un worker LLM con prompt especializado en identificar información reutilizable
- **Prompt de extracción de conocimiento**: el prompt de consolidación debe solicitar output estructurado: lista de preferencias identificadas, patrones de comportamiento observados, hechos nuevos aprendidos sobre el usuario o el dominio, y errores del agente que deben evitarse
- **Deduplicación y fusión**: la consolidación periódica puede generar memorias redundantes; implementar deduplicación por similaridad semántica (coseno > 0.95 como threshold) antes de escribir nuevas memorias para evitar el crecimiento indefinido del store
- **Niveles de abstracción**: las memorias consolidadas deben distinguir entre hechos específicos ("el usuario prefiere respuestas en inglés"), patrones generales ("el usuario hace preguntas de análisis de datos los lunes por la mañana") y reglas aprendidas ("cuando el usuario pide un resumen, limitarlo a 3 puntos")
- **Trazabilidad de la consolidación**: cada memoria consolidada debe referir a los episodios de origen que la generaron; permite auditar por qué el agente tiene una determinada creencia y actualizar o descartar la consolidación si los episodios de origen se revelan incorrectos

## Para recordar

La consolidación transforma el volumen de experiencias del agente en calidad de conocimiento: sin ella, la memoria crece indefinidamente con información cruda; con ella, el agente acumula aprendizaje genuino que mejora su desempeño con el tiempo.
