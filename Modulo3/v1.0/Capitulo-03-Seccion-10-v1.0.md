# Cierre del capítulo: ventanas de contexto y gestión de tokens

> Módulo 3 — Context Engineering Profesional

---

# Síntesis del capítulo

Este capítulo recorrió los conceptos fundamentales que determinan la capacidad y el rendimiento de cualquier aplicación basada en LLM.

Empezamos por entender que la **ventana de contexto** es el espacio de trabajo del modelo: todo lo que entra en ella —instrucciones, historial, memoria, documentos, resultados de herramientas— compite por un recurso limitado. Administrar ese espacio es una responsabilidad explícita del AI Engineer, no una tarea delegable al modelo.

Aprendimos que la unidad de medida de ese espacio es el **token**, una representación que no equivale a palabras ni a caracteres. Los tokens de entrada y los de salida tienen costos distintos; ambos deben medirse. La **tokenización** varía según el modelo y el tokenizador, por lo que las estimaciones deben hacerse sobre el sistema concreto que se va a utilizar.

Estudiamos cómo **evolucionaron las ventanas de contexto** y por qué un mayor tamaño no garantiza mejores resultados: el fenómeno "lost in the middle" demuestra que la posición de la información dentro del contexto importa tanto como su presencia. La calidad del contexto siempre precede a su cantidad.

Analizamos qué ocurre cuando el **contexto supera el límite** disponible y las cuatro estrategias para administrarlo: descarte selectivo, resumido, recuperación bajo demanda y memoria persistente.

Desarrollamos las **técnicas de compresión** —extractiva, abstractiva, jerárquica, incremental y semántica— con sus casos de uso, ventajas y limitaciones. Cada técnica responde a un tipo diferente de problema; la elección depende del tipo de contenido, la frecuencia de actualización y el nivel de fidelidad requerido.

Exploramos las **estrategias de optimización de tokens** tanto en el nivel del prompt como en el nivel de la arquitectura, incluyendo el caching de prefijos y las herramientas de medición disponibles en los principales proveedores.

Describimos los **cuatro patrones arquitectónicos** de administración del contexto —Sliding Window, Summary + Window, RAG First y Memoria + Historial + RAG— con sus criterios de selección, ventajas y compromisos.

Finalmente, aplicamos todos los conceptos en un **laboratorio práctico** con ejercicios de estimación, selección de patrones y auditoría de prompts.

---

# Autoevaluación

Las siguientes preguntas permiten verificar la comprensión de los conceptos del capítulo.

**1. ¿Qué diferencia existe entre palabras y tokens?**

Un token es la unidad mínima de procesamiento del modelo, y no equivale a una palabra ni a un carácter. Una palabra puede generar uno o varios tokens dependiendo del tokenizador; una misma frase produce cantidades distintas de tokens en modelos diferentes. No existe una tasa de conversión fija.

**2. ¿Por qué una ventana más grande no garantiza mejores respuestas?**

Por dos razones principales. La primera es el fenómeno "lost in the middle": los modelos prestan menos atención a la información ubicada en el centro del contexto, de modo que agregar más texto no asegura que el modelo lo procese con igual eficacia. La segunda es que más información sin filtrar introduce ruido, y el razonamiento del modelo sobre un contexto de calidad reducida tiende a ser menos preciso.

**3. ¿Cuándo conviene resumir el contexto?**

Antes de alcanzar el límite del modelo, no después. La política de resumido debe activarse a medida que el historial crece, de forma incremental y controlada. Resumir en reacción a un error de límite excedido obliga a reconstruir el contexto con riesgo de pérdida de información.

**4. ¿Qué patrón utilizaría para un asistente empresarial que trabaja con usuarios durante semanas y necesita consultar documentación técnica actualizada?**

El patrón Memoria + Historial + RAG es el más adecuado. La memoria persistente conserva el perfil y el historial a largo plazo del usuario; el historial reciente más un resumen captura el contexto de la sesión actual; y el RAG recupera en tiempo real los documentos técnicos relevantes para cada consulta. Ninguno de los tres mecanismos por separado cumple los tres requisitos simultáneamente.

---

# Checklist del arquitecto

Antes de pasar al siguiente capítulo, verifique que puede responder afirmativamente a cada uno de los siguientes puntos:

- [ ] Comprendo qué es un token y por qué no equivale a una palabra.
- [ ] Sé distinguir los tokens de entrada de los de salida y entiendo su impacto en el costo.
- [ ] Puedo estimar el consumo de tokens de una solicitud típica de mi aplicación.
- [ ] Conozco el fenómeno "lost in the middle" y sé cómo mitigarlo en el diseño del contexto.
- [ ] Tengo clara la diferencia entre descarte, resumido, recuperación bajo demanda y memoria persistente.
- [ ] Puedo elegir entre las cinco técnicas de compresión según el tipo de contenido y los requisitos.
- [ ] Conozco los cuatro patrones de administración y sé cuándo aplicar cada uno.
- [ ] Mi aplicación tiene o tendrá instrumentación para registrar el consumo de tokens en producción.

---

# Hacia el siguiente capítulo

El capítulo 03 nos dio las herramientas para administrar lo que el modelo puede ver en un momento dado. Pero una pregunta queda abierta: ¿qué ocurre con la información que necesita persistir más allá de la ventana de contexto, entre sesiones, a lo largo del tiempo?

La respuesta está en el diseño de la **memoria**. Una vez que comprendemos los límites de la ventana —cuánto cabe, cuánto cuesta, qué se pierde y por qué— el paso natural es profundizar en uno de sus componentes más complejos: cómo construir sistemas que recuerdan, que aprenden del historial del usuario y que mantienen estado entre sesiones separadas por horas, días o semanas.

El capítulo 04 abordará la memoria de corto y largo plazo y las estrategias avanzadas para construir asistentes persistentes.
