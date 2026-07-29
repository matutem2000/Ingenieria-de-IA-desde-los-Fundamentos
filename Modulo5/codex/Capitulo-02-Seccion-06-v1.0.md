# Módulo 5 – Capítulo 02 – Sección 06

# Cierre: buenas prácticas para consumir APIs de LLM en producción

Consumir APIs de LLM en producción implica operar sobre una dependencia externa con latencia variable (50ms a 30+ segundos), disponibilidad imperfecta (SLA típico del 99.5% no garantiza ausencia de degradaciones), y costo por uso que puede dispararse ante errores de programación como loops infinitos o prompts no acotados. Las buenas prácticas convergen en cuatro disciplinas: implementar resiliencia (retry con backoff, circuit breaker, timeouts explícitos), gestionar el costo activamente (conteo previo de tokens, caching, elección de modelo por tarea), instrumentar cada llamada (logging de tokens usados, latencia, costo estimado, errores), y versionar los prompts como código para tener trazabilidad del comportamiento del sistema a lo largo del tiempo. Un sistema sin observabilidad de sus llamadas a LLM es un sistema que no puede diagnosticarse ni optimizarse: cada llamada debe emitir al menos latencia, tokens de entrada, tokens de salida, modelo usado y si fue un hit o miss de caché. La simplicidad en el código de integración —funciones pequeñas con responsabilidad única, validación de entrada y salida, manejo explícito de errores— es el predictor más confiable de mantenibilidad a largo plazo.

## Buenas prácticas consolidadas

- Wrapper de cliente con observabilidad: encapsular el SDK del proveedor en una función o clase propia que añada logging, métricas y manejo de errores, evitando dispersar esta lógica en todos los puntos de llamada de la aplicación
- Validación de salida estructurada: si se espera JSON, validar con Pydantic o `json.loads()` dentro de un try/except e implementar al menos un reintento con instrucción de corrección antes de propagar el error
- Límites de gasto configurables: configurar `spending_limits` en la consola del proveedor y alertas vía webhook o email antes de alcanzar el límite, evitando interrupciones de servicio por cuota agotada
- Separación de ambientes: usar API keys distintas para desarrollo, staging y producción con límites de gasto diferenciados, evitando que experimentos en desarrollo consuman cuota de producción
- Testing sin costo real: usar mocks del cliente LLM en tests unitarios y de integración que no requieran la red, reservando las llamadas reales para tests de evaluación de calidad ejecutados bajo demanda

*"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* — Martin Fowler. En AI Engineering, esto se traduce en que el código de integración con APIs de LLM debe ser tan legible y mantenible como cualquier otro código de producción, independientemente de la complejidad del modelo que orquesta.
