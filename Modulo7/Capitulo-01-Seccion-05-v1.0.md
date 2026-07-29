# Módulo 7 – Capítulo 01 – Sección 05

# Riesgos y limitaciones de los sistemas agénticos en producción

Los sistemas agénticos amplifican tanto las capacidades como los riesgos de los LLMs base: cada paso del ciclo es una oportunidad para que un error de razonamiento se propague y se amplifique en acciones con efectos reales en el mundo. Los fallos más críticos en producción incluyen la acumulación de errores a lo largo de cadenas largas (compound errors), la ejecución de acciones irreversibles basadas en inferencias incorrectas (como eliminar registros de base de datos o enviar emails), y la susceptibilidad a prompt injection cuando el agente procesa contenido externo no confiable como páginas web, archivos o respuestas de APIs de terceros. La observabilidad deficiente es un multiplicador de riesgo: sin trazas detalladas de cada paso (LangSmith, Arize, Langfuse), diagnosticar un fallo en producción puede requerir reproducir toda la cadena de eventos desde el inicio.

## Puntos críticos

- **Compound errors**: errores de razonamiento en pasos tempranos distorsionan todos los pasos posteriores; en cadenas de 10+ pasos, una tasa de error del 5% por paso produce un 40% de fallo en la tarea completa
- **Acciones irreversibles**: operaciones como DELETE en bases de datos, envío de mensajes a usuarios reales o llamadas a APIs de pago deben protegerse con confirmación humana o mecanismos de dry-run antes de ejecutar
- **Prompt injection**: contenido malicioso en páginas web, documentos o respuestas de APIs puede redirigir el comportamiento del agente; mitigado mediante separación de canales de instrucción y datos
- **Context window overflow**: ciclos largos llenan la ventana de contexto (128K tokens en GPT-4o, 200K en Claude 3.5 Sonnet) y degradan el rendimiento; requiere gestión activa de memoria y summarization
- **Costos descontrolados**: un agente en bucle infinito o con max_steps elevado puede consumir miles de tokens por tarea; los límites de costo y duración deben ser configurados explícitamente antes del despliegue

## Buena práctica

Antes de desplegar un agente en producción, clasificar cada herramienta disponible por reversibilidad —read-only, reversible, irreversible— y requerir confirmación humana explícita para cualquier acción de la categoría irreversible.
