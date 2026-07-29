# Laboratorio práctico: diseño de contexto para aplicaciones empresariales

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Los conceptos de este capítulo —tokens, tokenización, ventanas de contexto, técnicas de compresión y patrones de administración— cobran significado real cuando se aplican a una situación concreta.

Este laboratorio propone tres ejercicios progresivos. Cada uno tiene un objetivo técnico específico y puede resolverse con papel y lápiz, con código o con llamadas directas a la API del modelo.

---

# Ejercicio 1: Estimación del consumo de contexto

## Escenario

Un equipo está desarrollando un asistente de soporte interno para una empresa de software. El system prompt actual tiene aproximadamente 800 palabras. El asistente mantiene en contexto las últimas 10 interacciones del usuario (promedio de 60 palabras por mensaje, entre usuario y modelo). En cada consulta, el sistema RAG recupera tres fragmentos de documentación técnica de 300 palabras cada uno.

## Tarea

1. Estime la cantidad de tokens de entrada por solicitud, considerando que el español tiene aproximadamente 1,3 tokens por palabra en la mayoría de los tokenizadores modernos.
2. Identifique qué capa del contexto consume más tokens.
3. Proponga una estrategia para reducir el consumo total en al menos un 30 % sin degradar la calidad de las respuestas.

## Referencia de cálculo

| Capa | Palabras | Tokens estimados |
|---|---|---|
| System prompt | 800 | ~1.040 |
| Historial (10 intercambios) | 600 | ~780 |
| Documentos RAG (3 x 300) | 900 | ~1.170 |
| **Total estimado** | **2.300** | **~2.990** |

Una reducción del 30 % en los documentos RAG —pasando de tres fragmentos de 300 palabras a dos fragmentos de 200 palabras cada uno— reduce el consumo de esa capa en más de un 55 %, llevando el total de entrada a aproximadamente 2.050 tokens.

---

# Ejercicio 2: Selección del patrón de administración

## Escenarios

Para cada uno de los siguientes casos, seleccione el patrón de administración más adecuado entre los cuatro estudiados en la sección anterior (Sliding Window, Summary + Window, RAG First, Memoria + Historial + RAG) y justifique la elección en dos o tres oraciones.

**Caso A:** Una empresa de e-commerce quiere implementar un chatbot de preguntas frecuentes sobre sus productos. El catálogo tiene 5.000 productos con especificaciones técnicas. Las consultas son mayoritariamente independientes entre sí.

**Caso B:** Un despacho legal usa un asistente para gestionar un caso judicial que se extiende durante ocho meses. El asistente debe recordar todas las decisiones procesales, los documentos analizados y las estrategias acordadas.

**Caso C:** Una plataforma de e-learning ofrece un tutor de programación. El tutor debe conocer el nivel actual del estudiante y su historial de errores anteriores, y al mismo tiempo consultar la documentación técnica del lenguaje que se está enseñando.

## Respuestas de referencia

**Caso A:** RAG First. Las consultas son independientes, el catálogo es extenso y cambia con frecuencia. No hay necesidad de continuidad histórica entre sesiones. La recuperación en tiempo real garantiza que las especificaciones estén actualizadas.

**Caso B:** Summary + Window. El caso dura meses y la continuidad histórica es fundamental. Un resumen estructurado de las decisiones procesales reemplaza el historial completo sin perder los hechos relevantes. La ventana reciente permite trabajar sobre los documentos del día.

**Caso C:** Memoria + Historial + RAG. El tutor necesita tres capas: la memoria persistente del estudiante (nivel, errores frecuentes, temas cubiertos), el historial reciente de la sesión actual y los documentos técnicos del lenguaje recuperados por RAG. Ninguna de las otras opciones proporciona las tres capacidades simultáneamente.

---

# Ejercicio 3: Auditoría de un system prompt

## Tarea

Analice el siguiente system prompt y aplique compresión semántica para reducir su longitud sin perder información operativa relevante.

**System prompt original (versión a auditar):**

> Eres un asistente de soporte técnico para la empresa Acme. Tu función principal y más importante es ayudar a los usuarios que trabajan en la empresa con sus problemas técnicos de computadoras, software y equipos de oficina. Debes ser siempre muy amable, cortés y respetuoso con todos los usuarios en todo momento. Cuando un usuario te haga una pregunta, debes escucharla con atención y tratar de entenderla bien antes de responder. Si no sabes la respuesta a una pregunta, debes decírselo honestamente al usuario y sugerirle que contacte al equipo de soporte de nivel dos. Nunca debes inventar información ni dar datos incorrectos. Responde siempre en español. Mantén tus respuestas breves y al punto, sin información innecesaria. No discutas temas que no estén relacionados con soporte técnico.

**Versión comprimida (referencia):**

> Eres el asistente de soporte técnico de Acme. Ayudas a empleados con problemas de hardware, software y equipos de oficina. Sé amable y directo. Si no conoces la respuesta, derívalo al soporte de nivel dos. No inventes información. Responde siempre en español y fuera del ámbito de soporte técnico.

La versión original tiene aproximadamente 135 palabras (~175 tokens). La versión comprimida tiene aproximadamente 55 palabras (~72 tokens), una reducción del 59 % sin pérdida de instrucciones operativas.

---

# Lista de verificación del arquitecto

Antes de desplegar una aplicación basada en LLM, verifique:

- [ ] El contexto contiene únicamente información relevante para la consulta actual.
- [ ] Existe una política explícita de descarte y resumido documentada en el código.
- [ ] El consumo de tokens se registra en cada solicitud: entrada, salida y costo estimado.
- [ ] Las capas de historial, memoria y RAG están claramente separadas y no duplican información.
- [ ] El system prompt ha sido auditado en los últimos tres meses.
- [ ] El patrón de administración elegido está documentado y el equipo conoce sus compromisos.
- [ ] Se ha evaluado la posibilidad de aplicar caching de prefijos para reducir costos en solicitudes frecuentes.

---

# Errores frecuentes

- **Llenar la ventana por precaución:** incorporar documentos o historial "por si acaso" degrada el razonamiento y aumenta el costo sin beneficio proporcional.
- **Duplicar información entre capas:** el mismo dato en el system prompt, en la memoria y en el RAG no aporta valor al modelo; solo consume tokens.
- **No medir costos:** operar sin instrumentación hace imposible detectar regresiones ni evaluar el impacto de cambios en la arquitectura del contexto.
- **Confiar exclusivamente en el historial:** una aplicación que depende solo del historial conversacional se vuelve inoperable a medida que la conversación crece.
- **Actualizar el resumen demasiado tarde:** resumir después de haber superado el límite obliga a reconstruir el contexto desde cero, con el riesgo de perder información relevante.

---

# Resumen

La ingeniería del contexto es, en último término, una disciplina de diseño. Los conceptos de este capítulo —tokens, ventanas, compresión, patrones— son herramientas. La habilidad del AI Engineer está en combinarlas correctamente para cada situación específica.

En la próxima sección cerraremos el capítulo con una síntesis de los conceptos clave y la transición hacia el diseño de sistemas de memoria, que es el paso natural después de haber comprendido los límites y la gestión de la ventana de contexto.
