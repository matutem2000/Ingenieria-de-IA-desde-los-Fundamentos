# Módulo 7 – Capítulo 09 – Sección 03

# Timeouts y cancelación: qué hacer cuando un agente no termina en tiempo

Los agentes en producción pueden no terminar en tiempo por múltiples razones: el LLM devuelve razonamientos circulares que no convergen, una herramienta externa no responde y el agente espera indefinidamente, el problema es intrínsecamente más difícil de lo estimado y requiere más iteraciones que el límite configurado, o el agente entra en un bucle de corrección donde cada intento de solucionar un error introduce uno nuevo. Sin mecanismos de timeout y cancelación explícitos, estos escenarios producen requests que consumen recursos indefinidamente, degradan la latencia de otros usuarios del sistema y pueden generar costos descontrolados de tokens y cómputo. La gestión de timeouts en agentes debe operar en múltiples capas: timeout por paso individual (cuánto tiempo puede tardar cada herramienta), timeout por sesión (cuánto tiempo total puede ejecutar el agente), y timeout de cancelación explícita (el usuario o el sistema cancela la tarea antes de que termine).

## Aspectos técnicos

- **Timeout por herramienta**: cada invocación de herramienta debe tener un timeout individual (`asyncio.wait_for(tool_call, timeout=30)`) con manejo explícito de `asyncio.TimeoutError`; el timeout debe ser proporcional a la latencia esperada de la herramienta (búsqueda web: 5-15s, ejecución de código: 30-60s, API externa: 5-30s)
- **Timeout de sesión total**: el agente como unidad completa debe tener un tiempo máximo de ejecución; implementado como un timer global que cancela el task asyncio completo cuando se supera; el estado hasta ese punto puede guardarse en el checkpointer para revisión
- **max_steps como límite de iteraciones**: límite explícito en el número de iteraciones del ciclo agéntico (típicamente 15-50 según la complejidad esperada); cuando se alcanza, el agente debe devolver el mejor resultado parcial disponible con una nota explicando que no pudo completar la tarea
- **Cancelación explícita (cancellation token)**: el cliente o el operador puede enviar una señal de cancelación al agente en ejecución; el agente debe verificar esta señal en puntos de control seguros (entre iteraciones, no a mitad de una operación crítica) y terminar limpiamente guardando el estado actual
- **Graceful degradation en timeout**: en lugar de fallar con un error genérico, el agente debe producir el mejor output posible con el trabajo completado hasta el momento del timeout, indicando explícitamente qué fue completado y qué quedó pendiente

## Principio rector

Los timeouts no son configuraciones de performance; son garantías de comportamiento: sin ellos, el agente no puede garantizar que terminará en un tiempo razonable, lo que hace imposible ofrecer SLOs sobre latencia y costo de las tareas.
