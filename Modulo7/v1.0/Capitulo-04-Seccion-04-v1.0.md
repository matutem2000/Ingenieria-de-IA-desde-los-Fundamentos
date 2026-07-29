# Módulo 7 – Capítulo 04 – Sección 04

## Memory consolidation: comprimir y abstraer memorias episódicas en conocimiento

La memoria episódica acumula experiencias brutas: transcripciones de conversaciones, logs de acciones del agente, observaciones de herramientas, correcciones del usuario. Si se almacena todo tal como ocurre, el sistema de memoria crece indefinidamente con volumen creciente y calidad decreciente: la información más antigua se vuelve menos relevante, las memorias redundantes proliferan, y recuperar señal relevante del ruido acumulado se vuelve progresivamente más difícil. La consolidación de memoria es el proceso que convierte este volumen de experiencias en conocimiento: extrae patrones de múltiples episodios, abstrae preferencias de comportamientos recurrentes, y destila reglas aprendidas de casos específicos, produciendo representaciones compactas y generalizables que el agente puede aplicar a situaciones nuevas.

La analogía con la neurociencia es directa y útil: la consolidación de memoria durante el sueño en humanos transforma memorias episódicas específicas —"esto ocurrió hoy en este contexto"— en memoria semántica generalizada —"este tipo de situación suele requerir esta respuesta"—. En sistemas agénticos, la consolidación implementa un proceso análogo: un LLM con un prompt de extracción de conocimiento analiza N sesiones recientes y produce memorias consolidadas del tipo "el usuario prefiere respuestas en bullets cuando hace preguntas sobre procedimientos" o "en este dominio, la regla X tiene las excepciones Y y Z que deben verificarse antes de aplicarla".

La **consolidación offline en batch** es la implementación más común: un proceso que se ejecuta periódicamente —cada 24 horas es un punto de partida razonable para la mayoría de los casos de uso— analiza un conjunto de sesiones recientes y extrae conocimiento reutilizable. El prompt de extracción debe solicitar output estructurado en categorías específicas:

```
Analiza las últimas {N} sesiones del usuario {user_id} y extrae:
1. Preferencias identificadas: formas en que el usuario prefiere interactuar o recibir información
2. Patrones de comportamiento: categorías de tareas que solicita frecuentemente, horarios, contextos
3. Hechos nuevos aprendidos sobre el usuario o el dominio
4. Errores del agente que el usuario corrigió y deben evitarse
5. Reglas del dominio mencionadas o descubiertas durante las sesiones

Para cada ítem, indicar: la conclusión, la evidencia en las sesiones, y el nivel de confianza (alto/medio/bajo).
```

Este output estructurado facilita la categorización automática de las memorias consolidadas por tipo, la asignación de nivel de prioridad basado en frecuencia y confianza, y la deduplicación contra memorias ya existentes.

La **deduplicación y fusión** de memorias consolidadas es operativamente importante para prevenir el crecimiento indefinido del store. Si la consolidación del lunes extrae "el usuario prefiere respuestas concisas" y la del miércoles extrae "el usuario pide resúmenes breves", estas dos memorias expresan el mismo conocimiento con diferente formulación. Calcular la similaridad de los embeddings de ambas memorias (threshold de coseno > 0.92 como punto de partida) y fusionarlas en una representación más específica y respaldada por más evidencia es más eficiente que acumular duplicados.

La **trazabilidad de la consolidación** garantiza que el sistema de memoria sea auditable y corregible. Cada memoria consolidada debe mantener una referencia a los episodios de origen que la generaron: si en el futuro se descubre que esos episodios contenían información incorrecta o que el patrón era una coincidencia sin generalización válida, la memoria consolidada puede identificarse y eliminarse sin tener que revisar todo el store. Esta trazabilidad también facilita la explicabilidad: si el agente actúa de una forma que sorprende al usuario, puede explicar "Aprendí de nuestras interacciones anteriores que prefieres X" con referencia a los episodios concretos que generaron esa preferencia.

Los **niveles de abstracción** de las memorias consolidadas deben distinguirse explícitamente: hechos específicos ("el usuario prefiere respuestas en inglés, no en español"), patrones generales ("el usuario hace preguntas de análisis de datos principalmente los lunes por la mañana"), y reglas aprendidas ("cuando el usuario pide un resumen, limitarlo a 3-5 puntos con bullets"). Las memorias de nivel más abstracto son más generalizables pero tienen mayor riesgo de ser incorrectas; las de nivel más específico son más confiables pero menos reutilizables. El sistema de memoria debe poder distinguir entre estos niveles para aplicar diferente threshold de confianza mínima al recuperarlas.

## Aspectos técnicos

- **Offline consolidation batch**: proceso periódico (cada 24h o configurable) que analiza sesiones recientes con un LLM y extrae preferencias, patrones, hechos y reglas aprendidas en output estructurado por categoría
- **Prompt de extracción estructurado**: el prompt debe solicitar categorías específicas (preferencias, patrones, hechos, errores, reglas) con evidencia y nivel de confianza para cada ítem; el output estructurado facilita categorización y deduplicación automática
- **Deduplicación por similaridad semántica**: calcular similaridad coseno entre embeddings de memorias nuevas y existentes (threshold > 0.92 como punto de partida); fusionar memorias semánticamente equivalentes en lugar de acumularlas como duplicados separados
- **Trazabilidad a episodios de origen**: cada memoria consolidada debe referenciar los episodios que la generaron; permite auditar la base de cada creencia del agente y actualizar o eliminar memorias cuando los episodios de origen se revelan incorrectos
- **Niveles de abstracción**: distinguir entre hechos específicos (alta confianza, baja generalización), patrones generales (media confianza, media generalización), y reglas aprendidas (requiere validación más rigurosa, alta generalización)

## Para recordar

La consolidación transforma el volumen de experiencias del agente en calidad de conocimiento: sin ella, la memoria crece indefinidamente con información cruda de calidad decreciente; con ella, el agente acumula aprendizaje genuino en forma compacta y aplicable, que mejora su desempeño de forma verificable con cada ciclo de consolidación.

La sección siguiente examina la vectorización de memorias como el mecanismo que hace posible la recuperación semántica de toda esta información acumulada: cómo convertir memorias textuales en representaciones numéricas que permiten encontrar el conocimiento más relevante para cada nueva situación.
