# Módulo 5 – Capítulo 10 – Sección 05

# Patrón de composición: encadenamiento de llamadas y manejo de dependencias

El patrón de composición en sistemas de IA conecta múltiples llamadas al LLM en una secuencia donde la salida de cada paso es la entrada del siguiente, implementando workflows de múltiples pasos como extracción + validación + generación, o clasificación + recuperación + síntesis. La composición puede ser secuencial (cada paso espera el resultado del anterior), paralela (múltiples pasos independientes se ejecutan simultáneamente con `asyncio.gather()`), o condicional (el paso siguiente depende del resultado del paso actual). La gestión de dependencias entre pasos es el aspecto más crítico: si el paso 2 espera una estructura específica del paso 1, y el paso 1 devuelve algo inesperado, el error debe detectarse y manejarse en el boundary entre pasos, no silenciosamente propagarse hasta producir un resultado incorrecto en el paso final. El patrón "fan-out, fan-in" es una variante de composición donde un único input se expande en N llamadas paralelas (ej. resumir cada capítulo de un libro en paralelo) y los resultados se agregan en un único output final (ej. generar el resumen ejecutivo a partir de los resúmenes de capítulo), aprovechando `asyncio.gather()` para reducir la latencia total de N*latencia a latencia_max.

## Aspectos técnicos del patrón de composición

- Composición secuencial tipada: cada función de un pipeline devuelve un tipo Pydantic específico que es la entrada de la siguiente; la cadena `extraction_result = extract(text); validated = validate(extraction_result); final = generate(validated)` detecta type errors en tiempo de desarrollo vía mypy
- Paralelismo con `asyncio.gather()`: `results = await asyncio.gather(*[process_chunk(chunk) for chunk in chunks], return_exceptions=True)` procesa todos los chunks en paralelo con un máximo de concurrencia controlado por un semáforo `asyncio.Semaphore(MAX_CONCURRENT_LLM_CALLS)`
- Manejo de dependencias entre pasos: verificar explícitamente que la salida del paso anterior cumple los requisitos del siguiente antes de continuar, en lugar de asumir que el LLM siempre devuelve el formato esperado; `if not result.category: raise PipelineError("Step 1 failed to extract category")` detiene el pipeline con un error claro
- Idempotencia de pasos: diseñar cada paso del pipeline como idempotente (el mismo input siempre produce el mismo output) facilita el retry parcial: si el paso 3 de 5 falla, se puede reintentar desde el paso 3 sin re-ejecutar los pasos 1 y 2
- Checkpoint y resumption: para pipelines largos (análisis de documentos con 10+ pasos, agentes con muchas herramientas), persistir el estado después de cada paso completado en Redis o una base de datos permite reanudar el pipeline desde el punto de fallo sin re-ejecutar los pasos anteriores, ahorrando tokens y tiempo

## Buena práctica

El patrón de composición más mantenible es el que minimiza el acoplamiento entre pasos: cada paso tiene un input y output bien definido con tipos estrictos, puede testarse de forma aislada con mocks de sus dependencias, y falla explícitamente ante inputs que no cumplen los requisitos.
