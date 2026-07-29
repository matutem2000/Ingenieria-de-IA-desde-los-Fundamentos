# Módulo 11 – Capítulo 07 – Sección 01

## El costo de IA a escala: cómo un sistema eficiente a pequeña escala puede ser insostenible en enterprise

Hay un momento en la vida de todo proyecto de IA enterprise que los equipos recuerdan vívidamente: la llegada de la primera factura mensual del proveedor de LLM después del lanzamiento a producción completa. El número que aparece en esa factura — con frecuencia entre tres y diez veces lo que el equipo había estimado basándose en los costos del piloto — es el resultado de una ilusión matemática: el costo unitario por petición es pequeño y constante, pero el volumen en producción enterprise es órdenes de magnitud mayor que el volumen del piloto, y la multiplicación produce un número que raramente está en el presupuesto operacional previsto.

Un sistema que procesa 1.000 peticiones diarias con un costo de 0,05 USD por petición tiene un costo mensual de aproximadamente 1.500 USD — razonable para un piloto. El mismo sistema escalado a 1.000.000 de peticiones diarias genera un costo mensual de 1.500.000 USD. Un enterprise con 10.000 empleados que usan un asistente de IA con una media de 100 peticiones diarias cada uno produce exactamente ese volumen — y eso es sin contar los procesos batch de análisis de documentos, los pipelines de indexación del RAG, y las peticiones de los sistemas integrados que el asistente sirve en background.

El costo de IA a escala enterprise se distribuye entre tres categorías principales. El **costo de inferencia** — tokens consumidos en llamadas a APIs de LLM externas, o costo de GPU para modelos self-hosted — domina el total, representando típicamente entre el 70% y el 80% del costo total del sistema. Dentro del costo de inferencia, la composición de los tokens es especialmente reveladora: en un sistema de RAG, el prompt (el system prompt + el historial de conversación + los fragmentos de documentos recuperados) puede representar el 80-90% de los tokens de entrada totales, mientras la respuesta del usuario representa solo el 10-20%. Esta proporción convierte la optimización del prompt — cuántos tokens enviamos al LLM por petición — en la palanca de reducción de costos más poderosa disponible.

El **costo de recuperación** — operaciones vectoriales en la base de datos vectorial para el pipeline de RAG, incluyendo los costos de reranking con modelos cross-encoder — es frecuentemente subestimado en las estimaciones iniciales. En Pinecone Serverless, el costo se factura por operación de query y por storage; a 1 millón de queries diarias con 1.000 resultados candidatos cada una, el costo de storage y operaciones puede superar los 2.000-5.000 USD/mes antes de contar el costo de los modelos. El **costo de almacenamiento e indexación** — embeddings almacenados en la base de datos vectorial, documentos en el data lake, y logs de trazas en los sistemas de observabilidad — completa el cuadro con costos fijos que crecen con el tamaño del corpus y con la granularidad del logging.

## Mapa de priorización de técnicas de optimización

Antes de implementar cualquier técnica de optimización de costos, es útil tener un mapa de priorización que organice las técnicas por facilidad de implementación y magnitud del impacto potencial. Esta jerarquía es específica al perfil de costo de cada sistema, pero una secuencia general válida para la mayoría de los sistemas de RAG enterprise es:

1. **Prompt caching** (impacto: alto, esfuerzo: bajo): la mayoría de los proveedores (Anthropic, OpenAI) ofrecen descuentos del 50-90% en tokens de entrada repetidos entre peticiones. Activar el prompt caching para el system prompt — que es idéntico en todas las peticiones del mismo tenant — es la optimización de menor esfuerzo y mayor impacto inmediato. Solo requiere estructurar el prompt para que los tokens estáticos aparezcan al inicio, antes de los tokens dinámicos.

2. **Semantic caching** (impacto: medio-alto, esfuerzo: medio): almacenar respuestas a preguntas similares en Redis y retornarlas sin llamar al LLM cuando la similitud vectorial supera el threshold. Puede eliminar el 20-40% de las llamadas al LLM en sistemas de soporte interno con alta repetición de preguntas.

3. **Model routing** (impacto: alto, esfuerzo: medio): enrutar peticiones simples al modelo económico (GPT-4o-mini) y peticiones complejas al modelo premium (GPT-4o), reduciendo el costo de inferencia en 12-15x para el 70-80% de las peticiones que no requieren el modelo premium.

4. **Prompt compression** (impacto: medio, esfuerzo: medio-alto): comprimir los fragmentos del contexto RAG con LLMLingua o PromptCompressor, reduciendo el número de tokens de contexto en un 50-80% con degradación de calidad del 5-15%.

5. **Infraestructura de cómputo optimizada** (impacto: alto para sistemas self-hosted, esfuerzo: alto): Reserved Instances, Spot Instances para batch, y quantización de modelos self-hosted.

## Componentes del costo de IA a escala

- **Costo de tokens de entrada:** en GPT-4o (referencia: 2,50 USD/1M tokens de entrada, verificar precio actual en platform.openai.com), un prompt con 4.000 tokens de contexto cuesta 0,01 USD por petición; a 1M peticiones/día, ese componente del costo supera los 10.000 USD/día.
- **Costo de tokens de salida:** los tokens de salida cuestan típicamente 3-5x más que los de entrada; calcular el costo de salida esperado basándose en la longitud media de respuesta del caso de uso específico.
- **Costo de embeddings:** verificar el precio actual en la página del proveedor; indexar documentos tiene un costo único que puede parecer bajo pero se multiplica con la frecuencia de reindexación y el volumen del corpus.
- **Costo de almacenamiento vectorial:** variable con el motor elegido; a 10M vectores, el costo de almacenamiento puede superar los 1.000 USD/mes antes de contar las operaciones de query.
- **Costo de observabilidad:** los sistemas de trazas de LLM sin sampling pueden costar el 5-15% del costo de inferencia; implementar sampling del 10-20% para reducir el costo de logging sin perder visibilidad.

---

**Para recordar:** Calcular el costo unitario por petición en el piloto y proyectarlo al volumen enterprise estimado debe ser un ejercicio obligatorio antes de comprometer la arquitectura de diseño — no después de recibir la primera factura sorpresa. Incluir en la proyección todos los componentes del costo: inferencia, embeddings, almacenamiento vectorial, y observabilidad.

*Nota: Los precios de referencia en este capítulo corresponden al momento de escritura (2026). Los precios de inferencia de LLM cambian con frecuencia; verificar los precios actuales directamente en las páginas de precios de cada proveedor antes de calcular proyecciones de costo para decisiones de inversión.*

La sección siguiente desarrolla las tres técnicas de optimización de tokens con mayor impacto en el costo de inferencia: la compresión de prompts, el semantic caching, y el prompt caching nativo de los proveedores.
