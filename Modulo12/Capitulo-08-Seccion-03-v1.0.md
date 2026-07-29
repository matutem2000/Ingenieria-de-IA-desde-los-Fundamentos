# Módulo 12 – Capítulo 08 – Sección 03

# Dashboard operativo: visualización de métricas clave en tiempo real

El dashboard operativo del sistema integrador en Grafana organiza las métricas en cuatro secciones: overview de sistema, calidad del RAG, comportamiento del agente y métricas de seguridad. La sección de overview muestra en la primera fila los cuatro KPIs principales como stat panels: peticiones por minuto, latencia P95, error rate y costo por hora; estos son los indicadores que el equipo de operaciones revisa primero ante un incidente. La sección de calidad RAG muestra gráficos de serie temporal de faithfulness y answer_relevance sobre muestras de producción, con líneas de umbral en rojo en 0.85 y 0.80 respectivamente; una caída por debajo de la línea roja dispara una alerta. La sección de agente muestra: distribución de iteraciones por tarea (histograma), tool usage rate por herramienta (bar chart) y task completion rate por ventana de 1 hora. La sección de seguridad muestra: contador de queries rechazadas por tipo (injection detectada, rate limit, token excedido) y rate de bypass de injection (debería ser 0 en operación normal).

## Paneles del dashboard operativo

- Overview row: peticiones/minuto, latencia P95, error_rate % y costo USD/hora como stat panels con colores semafóricos
- Calidad RAG: series temporales de faithfulness y answer_relevance con umbrales de alerta en rojo sobre fondo de 24h
- Rendimiento: heatmap de latencia por hora del día para detectar patrones de carga, throughput req/s en tiempo real
- Comportamiento agéntico: histograma de iterations_per_task, bar chart de tool_usage_count, task_completion_rate/hora
- Seguridad: contador de rechazos por tipo (injection/rate_limit/auth_failure), geographic heatmap de orígenes de petición

## Para recordar

Un dashboard operativo efectivo tiene dos versiones: una para el ingeniero de guardia durante un incidente (alta densidad de información, correlaciones visibles) y una para el equipo de producto (métricas de negocio simplificadas, tendencias de largo plazo).
