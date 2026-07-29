# Módulo 5 – Capítulo 09 – Sección 01

## Anatomía del costo: tokens de entrada, salida, caché y llamadas a herramientas

El gasto en APIs de LLM es uno de los pocos costos de infraestructura en tecnología que puede variar en un orden de magnitud entre una implementación eficiente y una ineficiente con el mismo nivel de funcionalidad: el mismo sistema de chat puede costar $1.200 o $8.000 al mes con 100.000 requests diarios, dependiendo de si el equipo eligió el modelo correcto para cada tarea, implementó prompt caching, controla la longitud del historial conversacional, y usa batching donde la latencia lo permite. Entender la anatomía del costo —de qué partes se compone la factura de cada request— es el prerrequisito para cualquier optimización que no sea aleatoria.

La factura de una llamada al LLM se compone de cuatro componentes con precios radicalmente diferentes. Los tokens de entrada —el prompt completo incluyendo system prompt, historial conversacional, documentos recuperados y la query del usuario— representan el mayor volumen de tokens en la mayoría de los sistemas pero el menor precio por token: $3 por millón en Claude 3.5 Sonnet. Los tokens de salida —la respuesta generada— son el componente de mayor precio por token: $15 por millón en el mismo modelo, cinco veces más que los de entrada. Esta asimetría tiene una implicación directa de diseño: reducir la longitud de las respuestas del LLM —instruyendo al modelo a ser conciso, usando formatos compactos como JSON en lugar de prosa extendida cuando los datos son lo que importa— reduce el costo de forma más efectiva que reducir el tamaño del prompt de entrada.

Los tokens de caché de Anthropic introducen una tercera categoría con precio diferencial. Los tokens de cache write —cuando se escribe un nuevo prefijo al caché— cuestan $3.75 por millón, un 25% más caro que la lectura normal. Los tokens de cache read —cuando el mismo prefijo se reutiliza en llamadas subsiguientes— cuestan $0.30 por millón, un 90% de descuento sobre el precio normal. El breakeven se alcanza con apenas 1.25 llamadas que reutilicen el mismo prefijo: después de esa primera llamada, cada reutilización ahorra el 90% del costo del prefijo cacheado. Para un system prompt de 3.000 tokens en Claude 3.5 Sonnet, el ahorro por cada cache hit es de $0.0081 —pequeño individualmente pero significativo a 100.000 requests diarios: $810 diarios o $29.000 mensuales de ahorro potencial.

Los costos multimodales y de herramientas añaden complejidad adicional. Las imágenes en OpenAI se facturan por "tiles" de 512×512 píxeles: una imagen de 1024×1024 ocupa 4 tiles y tiene un costo equivalente a varios centenares de tokens de texto. Los tool use blocks en el array de mensajes de conversaciones multi-turno con herramientas se cuentan como tokens de entrada en cada turno subsiguiente, acumulando el historial de herramientas en el contexto.

## Componentes del costo de las APIs de LLM

- **Tokens de entrada:** incluyen system prompt, historial conversacional, documentos recuperados por RAG, ejemplos few-shot, y la query del usuario; crecen sin control si no se implementan límites de contexto explícitos.
- **Tokens de salida:** menor volumen pero mayor precio (3-5x más que entrada); controlables con `max_tokens`, con instrucciones de concisión en el prompt, y eligiendo formatos compactos (JSON vs narrativa extendida).
- **Cache write tokens:** 25% más caro que lectura normal en Anthropic; costo de escritura amortizado en 1.25 llamadas con el mismo prefijo; activable marcando bloques con `cache_control: {"type": "ephemeral"}`.
- **Cache read tokens:** 90% de descuento sobre el precio normal; el mecanismo de mayor impacto en costo para sistemas con system prompts largos o documentos de referencia fijos por sesión.
- **Costos multimodales:** imágenes facturadas por tiles de 512×512px; documentos PDF en Anthropic facturados por página como imagen; tool use blocks acumulados en el historial de mensajes como tokens de entrada en turnos subsiguientes.

La instrumentación del costo en cada request —campo `cost_usd` calculado localmente y loggeado— es el prerequisito para cualquier optimización. Sin saber cuánto cuesta cada request desagregado por componente y por feature, la optimización de costos es ciega. Con instrumentación completa, las oportunidades de ahorro más grandes son evidentes desde el primer análisis de los datos de producción.

---

**Principio rector:** El costo total de un sistema de IA es predecible e instrumentable; la variabilidad de costo sin instrumentación convierte el presupuesto en una sorpresa mensual en lugar de una métrica gestionada activamente por el equipo de ingeniería.
