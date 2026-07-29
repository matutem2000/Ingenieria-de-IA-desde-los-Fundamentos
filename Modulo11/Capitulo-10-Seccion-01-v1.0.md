# Módulo 11 – Capítulo 10 – Sección 01

# Diagnóstico inicial: evaluar el estado actual del stack, los datos y las capacidades del equipo

El diagnóstico inicial de una organización enterprise que quiere adoptar IA de manera sistemática debe evaluarse en tres dimensiones ortogonales — el stack tecnológico, la calidad de los datos, y las capacidades del equipo — porque la brecha más crítica en cualquiera de las tres puede bloquear el progreso independientemente del nivel de madurez en las otras dos. El diagnóstico del stack tecnológico implica un inventario de los sistemas existentes: qué servicios cloud están disponibles y configurados (AWS, GCP, Azure, o on-premise), qué plataformas de datos existen (data lake, data warehouse, bases de datos), si existe infraestructura de CI/CD (Jenkins, GitLab CI, GitHub Actions), y qué herramientas de observabilidad están operativas (Prometheus, Grafana, Datadog). El diagnóstico de la calidad de los datos es frecuentemente la dimensión más reveladora: muchas organizaciones descubren durante este diagnóstico que sus datos de negocio tienen calidad insuficiente para entrenar o evaluar modelos de IA (duplicados sin reconciliar, campos nulos en columnas críticas, sesgos de muestreo que solo representan los casos más frecuentes), lo que requiere invertir primero en calidad de datos antes de cualquier iniciativa de IA. El diagnóstico de capacidades del equipo evalúa el conocimiento existente en las disciplinas relevantes: ingeniería de software (CI/CD, Docker, APIs REST), ingeniería de datos (pipelines de datos, SQL, calidad de datos), y conocimiento específico de IA (LLMs, embeddings, RAG, evaluación de modelos) — identificando las brechas que requieren contratación, capacitación, o apoyo externo.

## Componentes del diagnóstico inicial

- Inventario de stack tecnológico: tabla de capacidades existentes vs. requeridas por caso de uso objetivo, con gaps identificados y estimación de tiempo para implementar cada capacidad faltante
- Evaluación de calidad de datos: perfilado de datos con Great Expectations o dbt tests sobre las fuentes de datos candidatas para IA, con métricas de completitud (% campos no nulos), unicidad (% registros sin duplicados), y validez (% valores dentro de rango esperado)
- Assessment de capacidades del equipo: matrix de habilidades con autoevaluación y evaluación técnica por competencia (Python/data engineering, cloud infrastructure, LLMs/embeddings, evaluación y testing de IA) para identificar los gaps más críticos
- Inventario de casos de uso potenciales: identificar y priorizar los casos de uso de IA más relevantes para el negocio, evaluando cada uno por impacto estimado, disponibilidad y calidad de datos, y complejidad técnica
- Baseline de métricas actuales: documentar el estado actual de las métricas que los casos de uso de IA buscan mejorar (tiempo de proceso actual, tasa de error, costo por unidad), para poder calcular el ROI después del despliegue

## Buena práctica

El diagnóstico inicial debe completarse en no más de 4-6 semanas y producir un informe técnico con recomendaciones accionables — un diagnóstico que tarda 6 meses es una señal de que la organización no está lista para la velocidad que requiere la adopción de IA.
