# Módulo 7 – Capítulo 09 – Sección 04

## Observabilidad agéntica y gestión de presupuesto de tokens

La observabilidad de sistemas tradicionales captura inputs y outputs de los servicios: request recibido, response enviado, latencia, código de estado. Esta granularidad es insuficiente para diagnosticar comportamiento agéntico en producción. Un agente que devuelve una respuesta incorrecta puede haberlo hecho por razones completamente diferentes: el razonamiento del LLM se desvió en el paso 7 de 12; la herramienta de búsqueda devolvió resultados desactualizados; la observación fue mal interpretada en el paso 9; el agente no incorporó una corrección de error que recibió en el paso 11. Sin trazas granulares de cada paso del ciclo de razonamiento-acción, reproducir y diagnosticar un fallo de producción requiere reconstruir manualmente una cadena de eventos que puede tener decenas de pasos, con el agravante de que el entorno puede haber cambiado desde que ocurrió el fallo.

La observabilidad agéntica requiere capturar el ciclo completo con **trazas anidadas** (spans) que representan la estructura jerárquica de la ejecución: la traza raíz corresponde a la sesión completa del agente, con spans hijos para cada iteración del ciclo, y spans nietos para cada llamada al LLM y cada invocación de herramienta dentro de cada iteración. Esta estructura anidada permite navegar la ejecución en dos formas: top-down (¿qué ocurrió en la sesión completa?) y bottom-up (¿en qué contexto específico ocurrió esta invocación de herramienta que falló?). El formato OpenTelemetry (OTLP) está siendo adoptado como estándar para trazas de LLMs, con soporte nativo en Langfuse, Arize Phoenix, y otras plataformas de observabilidad especializadas.

Las **métricas por paso** que deben capturarse en cada span son: la latencia del LLM (tiempo de espera de la respuesta de la API, incluyendo time-to-first-token para streaming), la latencia de la herramienta (tiempo de ejecución de la herramienta, separado de la latencia del LLM), los tokens de input y output del LLM en ese paso, el nombre de la herramienta invocada y sus argumentos, la longitud de la observación retornada, y el costo estimado en USD del paso individual. Estos datos, agregados por sesión y por período de tiempo, producen los dashboards que permiten al equipo entender el comportamiento del agente a escala: cuál es la latencia típica de cada tipo de tarea, cuáles herramientas son las más lentas, en qué tipos de tareas el agente usa más iteraciones de las esperadas.

**LangSmith** (LangChain), **Langfuse** (open-source, auto-hosteable), y **Arize Phoenix** son las plataformas de observabilidad más adoptadas en el ecosistema agéntico. Langfuse se destaca por ser open-source y auto-hosteable, lo que lo hace apropiado para contextos con restricciones de privacidad de datos; su integración con LangGraph es sencilla mediante callbacks. LangSmith ofrece la integración más profunda con el ecosistema LangChain, incluyendo herramientas de evaluación y datasets de prueba. Arize Phoenix es especialmente fuerte en evaluación basada en LLM-judge integrada en el pipeline de observabilidad. La elección entre plataformas depende de las restricciones de privacidad, el stack tecnológico existente, y los requerimientos de evaluación integrada.

### Gestión de presupuesto de tokens y control de costos

La observabilidad de costos de tokens merece tratamiento propio porque es la dimensión que más frecuentemente sorprende a los equipos que despliegan agentes en producción. Un agente que funciona con costo aceptable en tests puede generar costos inesperadamente altos en producción por razones que no son visibles sin monitoreo específico: el historial de mensajes crece en cada iteración hasta llenar el contexto y producir prompts enormes; las observaciones de herramientas son más largas de lo esperado con datos reales; el agente usa más iteraciones de las esperadas en ciertos tipos de tareas que son más frecuentes en producción que en el test set.

La **fórmula de estimación de costo por tarea** proporciona una referencia de planificación:

```
costo_estimado_por_tarea = pasos_estimados × tokens_por_paso × precio_por_millón_de_tokens / 1.000.000
```

Para un agente con `pasos_estimados = 10`, `tokens_por_paso = 3.000` (sumando input + output + observaciones de herramientas), y usando Claude 3.5 Sonnet a `$3.00 por millón de tokens de input y $15.00 por millón de output`:

```
tokens_input_por_tarea  ≈ 10 × 2.500 = 25.000 tokens  →  $0.075
tokens_output_por_tarea ≈ 10 × 500   =  5.000 tokens  →  $0.075
costo_estimado_total    ≈ $0.15 por tarea
```

Si el sistema procesa 10.000 tareas/día, el costo estimado es $1.500/día o $45.000/mes. Esta estimación es el punto de partida para el dimensionamiento presupuestario; el monitoreo de producción revelará si los valores reales se desvían de la estimación y en qué dirección.

El **token budget middleware** es el patrón de implementación que previene que tareas individuales consuman un número irrazonablemente alto de tokens. Implementado como una función que se ejecuta antes de cada llamada al LLM, verifica el número de tokens del contexto actual y actúa cuando supera un umbral: si el contexto supera el 70% del límite configurado, comprimir el historial (resumir los mensajes más antiguos); si supera el 90%, terminar la tarea con el resultado parcial disponible y una nota de que el contexto fue agotado; si supera el límite de la API del modelo, la llamada fallará con un error —el peor outcome posible.

```python
MAX_CONTEXT_TOKENS = 100_000  # presupuesto de tokens por sesión

def check_token_budget(messages: list[dict]) -> tuple[bool, int]:
    """Verifica si el contexto actual excede el presupuesto de tokens."""
    estimated_tokens = sum(len(m["content"].split()) * 1.3 for m in messages)
    if estimated_tokens > MAX_CONTEXT_TOKENS * 0.9:
        return False, estimated_tokens  # presupuesto agotado
    return True, estimated_tokens

# En el ciclo del agente, antes de cada llamada al LLM:
budget_ok, current_tokens = check_token_budget(state["messages"])
if not budget_ok:
    # resumir historial o terminar con resultado parcial
    state["messages"] = summarize_history(state["messages"])
```

Las **alertas de anomalías de costo** son la segunda capa de control. Configurar alertas cuando: el costo de una sesión individual supera un umbral (p.ej., $5 por sesión), el costo promedio por tarea de un período supera el 150% del baseline histórico, o el número de tokens por sesión del percentil 95 supera el doble del P50 (indica outliers que consumen recursos desproporcionados). Estas alertas permiten detectar cambios en el comportamiento del agente —causados por cambios en la distribución de inputs o por modificaciones no previstas de prompts o herramientas— antes de que produzcan impacto presupuestario significativo.

## Aspectos técnicos

- **Trazas anidadas (spans)**: traza raíz por sesión completa del agente, con spans hijos por iteración y spans nietos por llamada al LLM y por invocación de herramienta; formato OpenTelemetry (OTLP) como estándar emergente; soporte en Langfuse, Arize Phoenix, LangSmith
- **Métricas por paso**: latencia del LLM, latencia de la herramienta, tokens de input/output por paso, costo estimado por paso, nombre y argumentos de la herramienta invocada, longitud de la observación; base para dashboards de comportamiento a escala
- **Session replay**: reproducción paso a paso de la ejecución de un agente usando trazas almacenadas; disponible en LangSmith y Langfuse; esencial para investigar incidentes reportados por usuarios sin necesidad de reproducir el entorno
- **Fórmula de costo por tarea**: `pasos_estimados × tokens_por_paso × precio / 1M`; usar para planificación presupuestaria; validar contra costo real en producción y ajustar si la desviación supera el 50%
- **Token budget middleware**: verificación del número de tokens del contexto antes de cada llamada al LLM; umbral de compresión al 70% (resumir historial), umbral de terminación al 90% (devolver resultado parcial); previene llamadas que superan el límite de la API del modelo
- **Sampling adaptativo de trazas**: en producción de alto volumen, capturar 100% de las sesiones que fallan o superan umbrales de latencia/costo, y un porcentaje configurable (10-20%) de las sesiones exitosas; reduce el costo de almacenamiento sin perder cobertura de los casos críticos

> **Nota del Arquitecto**: El error más frecuente en observabilidad agéntica no es no tener las herramientas correctas sino no configurar alertas sobre las métricas correctas desde el primer día en producción. Un dashboard sin alertas es un instrumento de diagnóstico reactivo; las alertas son el instrumento de detección proactiva. Configurar al menos estas tres alertas desde el despliegue inicial: tasa de sesiones que alcanzan `max_steps` (indica tareas más complejas de lo diseñado), costo medio por sesión (detecta degradaciones de eficiencia), y tasa de fallos de herramientas (detecta cambios en APIs externas antes de que los usuarios lo reporten).

## Para recordar

La observabilidad agéntica no es logging de texto plano; es la captura estructurada de cada decisión del ciclo de razonamiento-acción, con la granularidad suficiente para diagnosticar exactamente en qué paso el agente tomó la decisión incorrecta. La gestión de presupuesto de tokens es parte de la observabilidad, no un añadido: un agente que no controla su consumo de tokens no puede ofrecer garantías de costo predecibles en producción.
