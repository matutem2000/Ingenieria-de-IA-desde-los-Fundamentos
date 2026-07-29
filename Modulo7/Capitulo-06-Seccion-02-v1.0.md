# Módulo 7 – Capítulo 06 – Sección 02

# Patrones de coordinación: secuencial, paralelo, jerárquico y de debate

Los sistemas multiagente se organizan en cuatro patrones de coordinación fundamentales, cada uno con trade-offs diferentes en términos de latencia, determinismo y calidad del resultado. El patrón secuencial encadena agentes en pipeline: el output del agente N es el input del agente N+1; es el más predecible y fácil de depurar pero no aprovecha el paralelismo. El patrón paralelo ejecuta múltiples agentes concurrentemente sobre el mismo input o sobre particiones del problema y combina sus resultados mediante una función de merge o un agente agregador; reduce la latencia total pero requiere que las subtareas sean verdaderamente independientes. El patrón jerárquico introduce un agente orquestador que planifica, delega y coordina a agentes especializados subordinados; añade flexibilidad adaptativa pero el orquestador se convierte en un punto de fallo central. El patrón de debate (sociedades de agentes) ejecuta múltiples agentes sobre el mismo problema y los hace "debatir" sus respuestas hasta llegar a un consenso; mejora la robustez ante errores individuales pero tiene el mayor costo computacional.

## Aspectos técnicos

- **Patrón secuencial (pipeline)**: implementado como una cadena de llamadas donde `agent_N.run(context)` produce el `context` para `agent_N+1`; latencia total = suma de latencias individuales; apropiado para transformaciones encadenadas con dependencias estrictas entre pasos
- **Patrón paralelo (map-reduce)**: los agentes "mappers" procesan particiones del input en paralelo (asyncio.gather) y el agente "reducer" combina sus outputs; latencia total = máx(latencias individuales) + latencia del reducer; apropiado para análisis de múltiples documentos, evaluaciones multi-criterio
- **Patrón jerárquico (orchestrator-workers)**: el orquestador genera un plan, delega subtareas a workers especializados y valida sus resultados; el orquestador debe poder manejar workers que fallan, reasignando la subtarea o modificando el plan
- **Patrón de debate (agent debate/reflection)**: múltiples agentes (típicamente 3-5) generan respuestas independientes, luego leen las respuestas de los otros y refinan las suyas; después de N rondas de debate, se aplica voting o se usa un judge LLM para seleccionar la mejor respuesta; mejora calidad en 10-25% en benchmarks de razonamiento complejo
- **Patrones híbridos**: los sistemas de producción combinan patrones; p.ej., un orquestador jerárquico que internamente ejecuta etapas paralelas y usa un pipeline secuencial para el post-procesamiento final

## Para recordar

La elección del patrón de coordinación debe basarse en la estructura natural del problema: si las subtareas son independientes, usar paralelismo; si tienen dependencias estrictas, usar pipeline; si requieren expertise adaptativo, usar jerarquía; si la calidad supera al costo, considerar debate.
