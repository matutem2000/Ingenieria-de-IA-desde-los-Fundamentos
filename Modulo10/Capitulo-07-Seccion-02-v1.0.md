# Módulo 10 – Capítulo 07 – Sección 02

# Rate limiting y cuotas por equipo, proyecto o usuario

El rate limiting en un LLM Gateway no es solo una medida de protección contra abuso, sino un mecanismo de gestión equitativa de recursos escasos: cuando múltiples equipos comparten un límite de tokens-per-minute (TPM) o requests-per-minute (RPM) de un proveedor como OpenAI o Anthropic, sin rate limiting interno, un equipo con picos de tráfico puede agotar el límite global afectando a todos los demás. La granularidad del rate limiting debe ir de más gruesa a más fina: límite global de la organización (definido por los contratos con los proveedores), límite por equipo o BU (asignado según el presupuesto de IA aprobado), límite por proyecto (para controlar el consumo de features individuales), y opcionalmente límite por usuario final (para proteger contra abuso en aplicaciones públicas). La implementación técnica del rate limiting distribuido en un gateway desplegado en múltiples réplicas requiere un contador compartido: Redis con el algoritmo de Token Bucket o Sliding Window (usando las primitivas `INCR` y `EXPIRE` de Redis para contadores atómicos) o una solución especializada como Redis Rate Limiting. Los algoritmos de rate limiting relevantes para LLMs son: Fixed Window (simple pero susceptible a burst al inicio del window), Sliding Window (más suave, evita bursts), Token Bucket (permite bursts controlados hasta el tamaño del bucket), y Leaky Bucket (tasa de salida constante, protege el backend de variaciones de carga).

## Aspectos técnicos del rate limiting para LLM Gateway

- Dimensiones de rate limiting: tokens-per-minute (TPM) para controlar costo, requests-per-minute (RPM) para controlar throughput, y concurrent requests para controlar latencia de cola
- Jerarquía de límites: límite global de organización → límite por equipo → límite por proyecto → límite por usuario; el límite más restrictivo aplicable se respeta, con headers informativos de cuánto queda disponible
- Redis Token Bucket: cada cliente tiene un bucket con capacidad máxima C; se añaden R tokens por segundo; cada request consume tokens según el número de tokens de input estimados; requests rechazados devuelven HTTP 429
- Graceful degradation: cuando un equipo alcanza su límite, el gateway puede ofrecer fallback a un modelo más económico (ej. de GPT-4 a GPT-3.5) en lugar de rechazar directamente, con un header informativo
- Cuotas mensuales: además del rate limiting de velocidad, cuotas de gasto mensual por equipo que cuando se alcanzan bloquean el acceso hasta el inicio del siguiente período o hasta aprobación manual de extensión

## Principio rector

El rate limiting efectivo protege tanto al proveedor externo (evitando superar los límites de contrato) como a los equipos internos (garantizando que ningún equipo monopoliza la capacidad compartida), y debe ser visible y predecible para los equipos que lo experimentan.
