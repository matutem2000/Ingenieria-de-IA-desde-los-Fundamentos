# Módulo 5 – Capítulo 10 – Sección 04

# Patrón Circuit Breaker: resiliencia ante fallos del proveedor de IA

El Circuit Breaker es un patrón de resiliencia que previene que un servicio siga intentando conectarse a una dependencia que está fallando, protegiendo los recursos propios y dando tiempo al servicio externo para recuperarse. Aplicado a llamadas a LLMs, el Circuit Breaker tiene tres estados: Closed (operación normal, las llamadas pasan), Open (el proveedor está fallando, las llamadas se rechazan inmediatamente sin intentar la conexión), y Half-Open (se permite una llamada de prueba para verificar si el servicio se recuperó). La transición de Closed a Open ocurre cuando N llamadas consecutivas o una fracción X de llamadas en una ventana de tiempo T fallan con errores retryables (429, 5xx, timeout); la transición de Open a Half-Open ocurre después de un cooldown configurable (30-120 segundos típicamente). Implementar Circuit Breaker para APIs de LLM previene el escenario donde una degradación del proveedor hace que todos los threads o coroutines del servicio se bloqueen esperando timeouts, agotando los recursos del servidor propio; con Circuit Breaker, las llamadas en estado Open fallan inmediatamente con un error predecible que puede manejarse con un fallback definido.

## Aspectos técnicos del Circuit Breaker para APIs de LLM

- Implementación con `pybreaker`: `cb = CircuitBreaker(fail_max=5, reset_timeout=30); @cb def call_llm(messages): return client.messages.create(...)` abre el breaker después de 5 fallos y cierra 30 segundos después de abrirse
- Estado Open con fallback: cuando el breaker está abierto, en lugar de devolver un error al usuario, activar una respuesta de fallback: una respuesta genérica pre-definida, resultados de búsqueda keyword en lugar del LLM, o un mensaje de degradación graceful que invita al usuario a reintentar en unos minutos
- Métricas del circuit breaker: exportar a Prometheus los estados del breaker (`llm_circuit_breaker_state`, `llm_circuit_breaker_calls_total{result="success|failure|rejected"}`) para visualizar en Grafana y alertar cuando el breaker se abre
- Breakers separados por proveedor: si el sistema tiene múltiples proveedores (Anthropic + OpenAI), mantener un breaker independiente por proveedor permite que el fallo de uno no afecte la disponibilidad del otro, y que el fallback automático al proveedor secundario funcione incluso cuando el breaker del primario está abierto
- Half-Open con sampling: en estado Half-Open, en lugar de permitir solo una llamada de prueba, permitir el N% del tráfico normal para medir la tasa de éxito antes de transicionar a Closed; reduce el riesgo de abrir el breaker prematuramente ante fluctuaciones transitorias de la carga del proveedor

## Para recordar

Un sistema de IA sin Circuit Breaker en sus dependencias externas convierte una degradación del proveedor —que normalmente dura minutos— en una indisponibilidad del servicio propio que puede extenderse por horas, hasta que los threads bloqueados se agotan y el sistema se reinicia.
