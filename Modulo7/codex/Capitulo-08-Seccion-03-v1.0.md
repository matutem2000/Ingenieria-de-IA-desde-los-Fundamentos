# Módulo 7 – Capítulo 08 – Sección 03

# Minimal footprint: principio de mínimo privilegio aplicado a herramientas de agentes

El principio de mínimo privilegio (Principle of Least Privilege, PoLP), enunciado originalmente por Jerome Saltzer y Michael Schroeder en "The Protection of Information in Computer Systems" (1975), establece que cualquier entidad del sistema debe tener acceso exclusivamente a los recursos que necesita para cumplir su función y nada más. Aplicado a herramientas de agentes, este principio significa que el conjunto de herramientas disponibles para un agente debe ser el mínimo necesario para completar las tareas que se le asignan: un agente de customer support no necesita herramientas de administración de base de datos; un agente de análisis de datos no necesita herramientas de envío de emails sin confirmación humana; un agente de research no necesita herramientas de escritura en el sistema de archivos. El concepto de "minimal footprint" extiende el PoLP más allá de las herramientas: incluye el scope de datos al que accede el agente (solo los datos relevantes para la tarea actual), los permisos de las herramientas (read-only cuando sea posible), y el tiempo de vida de los tokens y credenciales usados.

## Aspectos técnicos

- **Tool scope por tarea**: en lugar de proveer al agente un conjunto fijo de todas las herramientas disponibles, definir subsets de herramientas específicos por tipo de tarea; el routing al agente correcto con el subconjunto apropiado es más seguro que herramientas disponibles universalmente
- **Read-only by default**: diseñar herramientas en modo de solo lectura como opción por defecto y requerir parámetros explícitos de confirmación para operaciones de escritura; p.ej. `query_database(sql, dry_run=True)` antes de `query_database(sql, execute=True)`
- **Scoped API credentials**: las herramientas que acceden a APIs externas deben usar credenciales con el scope mínimo necesario; una API key de solo lectura para Notion no debe también tener permisos de escritura aunque la API lo soporte, si el agente solo necesita leer
- **Data access boundaries**: el agente debe tener acceso solo a los datos relevantes para la tarea actual; implementar filtros a nivel de herramienta (p.ej. la herramienta de búsqueda en base de datos solo accede a tablas del tenant del usuario actual) en lugar de delegar el filtrado al razonamiento del LLM
- **Short-lived credentials**: las credenciales usadas por las herramientas del agente deben tener TTL cortos (minutos u horas, no días); usar token exchange patterns (p.ej. AssumeRole en AWS) para generar credenciales temporales por invocación del agente

## Buena práctica

Antes de desplegar un agente en producción, realizar una revisión explícita de cada herramienta contra la pregunta: "¿Puede esta herramienta, si fuera mal usada por prompt injection, causar daño irreversible?" Cualquier herramienta que responda afirmativamente debe añadir una capa adicional de protección.
