# Módulo 5 – Capítulo 01 – Sección 05

# Elección de herramientas según el caso de uso: criterios técnicos y económicos

La decisión de qué API, SDK y framework usar no debe tomarse por popularidad sino por una evaluación rigurosa de los requisitos del caso de uso: latencia máxima aceptable, volumen de requests por día, complejidad del flujo, presupuesto mensual y requisitos de privacidad de datos. Un chatbot de atención al cliente de alto volumen (>100.000 requests/día) requiere un modelo rápido y económico como Claude 3.5 Haiku o gpt-4o-mini; una tarea de análisis profundo de documentos legales con baja frecuencia justifica modelos de mayor capacidad como Claude 3.5 Sonnet o gpt-4o. La latencia de time-to-first-token (TTFT) es el criterio dominante en interfaces conversacionales en tiempo real, mientras que el throughput en tokens por segundo importa más en generación por lotes. Los requisitos de privacidad o soberanía de datos pueden descartar APIs públicas en favor de modelos desplegados en infraestructura propia (Llama 3 via Ollama o vLLM) o servicios con contratos BAA como Azure OpenAI.

## Criterios técnicos y económicos de selección

- Latencia vs capacidad: Claude 3.5 Haiku ofrece TTFT <500ms con capacidad de razonamiento media; gpt-4o balances capacidad y velocidad; o1 prioriza razonamiento sobre latencia con tiempos de respuesta de segundos a minutos
- Costo por tarea: el costo real se calcula como `(input_tokens * precio_entrada + output_tokens * precio_salida) * volumen_diario`; modelos pequeños pueden costar 10-50x menos por request con calidad suficiente para tareas simples de extracción o clasificación
- Ventana de contexto: Gemini 1.5 Pro soporta 1 millón de tokens de contexto; Claude 3.5 Sonnet 200K; gpt-4o 128K; la elección depende del tamaño del corpus que debe caber en una sola llamada
- Privacidad y cumplimiento: APIs de terceros envían datos a servidores externos; modelos locales con vLLM o Ollama mantienen datos on-premise pero requieren GPU propia con ≥24GB VRAM para modelos de 7B-70B parámetros
- Ecosistema y soporte: proveedores con SLA documentado, foro activo, changelog público y latencia de soporte <24h tienen ventaja en proyectos de producción donde los incidentes deben resolverse rápidamente

## Buena práctica

Evaluar modelos con un benchmark representativo del caso de uso real antes de comprometer la arquitectura con un proveedor, midiendo la relación costo-calidad con al menos 100-200 ejemplos del dominio específico.
