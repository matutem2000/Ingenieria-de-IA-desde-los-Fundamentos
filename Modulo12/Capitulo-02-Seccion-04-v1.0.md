# Módulo 12 – Capítulo 02 – Sección 04

# ADR 003: diseño de agentes — framework, herramientas y nivel de autonomía

El ADR-003 documenta las decisiones sobre el framework agéntico, las herramientas disponibles y el nivel de autonomía otorgado al agente. La comparación entre LangChain AgentExecutor, LangGraph y AutoGen mostró que LangGraph es el único que soporta grafos de estado con ciclos condicionales, checkpointing para reanudación de conversaciones y control granular del flujo de ejecución; esto es crítico para implementar patrones ReAct donde el agente puede iterar sobre herramientas hasta alcanzar una condición de parada. El nivel de autonomía fue limitado deliberadamente: el agente puede llamar herramientas de lectura (search_knowledge_base, get_document, list_sources) pero no puede escribir en sistemas externos ni ejecutar código arbitrario, reduciendo la superficie de ataque agéntica. El número máximo de iteraciones se fijó en 5 para prevenir bucles infinitos, con un fallback explícito que devuelve la mejor respuesta parcial disponible.

## Decisiones del diseño agéntico

- Framework: LangGraph seleccionado sobre LangChain AgentExecutor por soporte de grafos con ciclos y checkpointing nativo
- Patrón de razonamiento: ReAct (Reasoning + Acting) con max_iterations=5 y fallback a respuesta parcial al alcanzar el límite
- Herramientas disponibles: search_knowledge_base, get_document_by_id, list_available_sources (solo lectura, sin escritura)
- Nivel de autonomía: Human-in-the-loop opcional para queries clasificadas como high_risk por el clasificador de intent
- Gestión de estado: checkpointing en PostgreSQL con LangGraph Persistence para mantener historial de conversación entre sesiones

## Buena práctica

Documentar el nivel de autonomía máximo del agente en el ADR es una decisión de seguridad, no solo de diseño — define qué acciones el sistema puede tomar sin aprobación humana y cuáles requieren confirmación explícita.
