# Módulo 9 – Capítulo 02 – Sección 02

# Prompt injection indirecta: instrucciones maliciosas en datos recuperados por el sistema (RAG, web)

La prompt injection indirecta es significativamente más peligrosa que la directa porque el atacante no necesita interactuar con la aplicación: basta con colocar instrucciones maliciosas en documentos, páginas web o bases de datos que el sistema de IA recuperará automáticamente como parte de su flujo de trabajo. En un sistema RAG (Retrieval-Augmented Generation), si un atacante logra inyectar un documento en el índice vectorial —o si el corpus incluye documentos de internet no verificados— ese documento puede contener instrucciones que el modelo ejecutará como parte del contexto recuperado. Esta vulnerabilidad fue demostrada por el investigador Johann Rehberger en 2023 mediante ataques contra ChatGPT Plugins, Copilot y múltiples asistentes agénticos, demostrando exfiltración de datos de conversación a través de documentos maliciosos en el contexto. El vector de ataque más crítico es el agente que navega la web o lee emails: cualquier página o email puede contener instrucciones ocultas para el modelo.

## Aspectos técnicos

- Mecanismo de ataque indirecto: el modelo recibe documentos recuperados por el sistema (vía RAG, web scraping, email parsing, o tool results) como contexto confiable y no puede distinguir instrucciones legítimas del sistema de instrucciones inyectadas en esos datos
- Técnicas de ocultamiento en documentos: instrucciones en texto blanco sobre fondo blanco, en comentarios HTML invisibles al usuario pero visibles al scraper, en metadatos de archivos PDF, en texto muy pequeño, o en caracteres Unicode de control que los parsers exponen al modelo
- Exfiltración vía indirect injection: el atacante diseña el documento malicioso para instruir al modelo a incluir datos sensibles de la conversación en un URL que el agente visitará, o en una request a una herramienta externa que el atacante controla
- Casos documentados: Johann Rehberger demostró en 2023 exfiltración de historial de conversación de ChatGPT vía documentos maliciosos; Bing Copilot manipulado vía páginas web con instrucciones ocultas; Claude Computer Use vulnerable a instrucciones en capturas de pantalla
- Vectorstores como superficie de ataque: en sistemas RAG, la pipeline de ingestión de documentos es tan crítica para la seguridad como el gateway de API; documentos de fuentes no verificadas o con permisos de escritura insuficientemente controlados son vectores de indirect injection

## Buena práctica

La mitigación de prompt injection indirecta requiere tratar todos los datos recuperados externamente —documentos RAG, resultados de web search, emails, outputs de herramientas— como untrusted input, aplicando separadores explícitos en el contexto y validación del output antes de ejecutar cualquier acción basada en el contenido recuperado.
