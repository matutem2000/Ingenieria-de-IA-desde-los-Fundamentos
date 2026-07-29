# Cuando el contexto supera la ventana disponible

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Toda ventana de contexto, por grande que sea, tiene un límite. Tarde o temprano una conversación extensa, un conjunto de documentos o una combinación de herramientas y memoria terminarán superando esa capacidad.

El desafío del AI Engineer consiste en decidir **qué información conservar, cuál resumir y cuál descartar**, maximizando la calidad del contexto sin exceder el límite del modelo.

---

# ¿Qué ocurre al superar el límite?

Cuando el contexto excede la capacidad admitida por el modelo, pueden producirse distintas situaciones dependiendo del proveedor:

- rechazo de la solicitud con un error de límite excedido;
- truncamiento automático del contexto por el lado del proveedor;
- eliminación de los mensajes más antiguos del historial;
- necesidad de reconstruir el contexto antes de reenviar la consulta.

En cualquier caso, el modelo no podrá razonar sobre información que ya no forme parte de la ventana. Una arquitectura que no gestiona activamente este límite dejará que el proveedor tome esa decisión, generalmente con resultados menos precisos que una política diseñada deliberadamente.

---

# El problema de las conversaciones largas

Imagine un asistente que acompaña a un usuario durante varias semanas.

Cada interacción agrega:

- nuevos mensajes del usuario y respuestas del modelo;
- resultados de herramientas ejecutadas;
- documentos recuperados para responder consultas específicas;
- instrucciones adicionales incorporadas en distintos momentos.

Si todo permanece dentro del contexto, llegará un momento en que el modelo no podrá procesarlo completamente.

Por este motivo, las aplicaciones profesionales nunca dependen exclusivamente del historial conversacional. Requieren una política activa de administración del contexto.

---

# Estrategias de administración

Existen varias técnicas para mantener el contexto dentro de límites razonables.

## 1. Descarte selectivo

Eliminar mensajes o fragmentos que ya no aportan valor para las consultas futuras.

Candidatos habituales al descarte:

- saludos y cortesías de inicio de sesión;
- mensajes repetidos o reformulaciones del mismo pedido;
- respuestas del modelo ya superadas por versiones posteriores;
- resultados de herramientas de una tarea ya concluida.

## 2. Resumido

Reemplazar múltiples interacciones por un resumen estructurado que conserve únicamente los hechos relevantes: decisiones adoptadas, compromisos asumidos, datos confirmados y estado actual del problema.

El resumen puede generarse con el mismo modelo o con uno más económico dedicado a esa tarea.

## 3. Recuperación bajo demanda

En lugar de mantener toda la información en el contexto activo, almacenarla fuera y recuperarla cuando realmente sea necesaria mediante mecanismos como RAG.

Esta estrategia es especialmente efectiva para bases de conocimiento estables: manuales, políticas, documentación técnica.

## 4. Memoria persistente

Guardar únicamente conocimientos duraderos y reutilizables —preferencias del usuario, acuerdos de largo plazo, perfil del cliente— evitando conservar eventos transitorios que solo son relevantes durante una sesión.

---

# Elegir qué conservar

Una pregunta útil durante el diseño es:

> "¿El modelo necesitará esta información para responder correctamente dentro de diez minutos?"

Si la respuesta es negativa, probablemente no deba permanecer en el contexto activo. Si la respuesta es "tal vez", la estrategia correcta es almacenarla fuera del contexto y recuperarla en caso necesario.

---

# Caso práctico

Supongamos un asistente de soporte que atiende un incidente durante varios días.

Sin gestión activa del contexto, el historial crece linealmente hasta superar la ventana del modelo.

Una arquitectura eficiente podría:

1. mantener únicamente las últimas cinco a diez interacciones en el contexto activo;
2. resumir las decisiones y acciones tomadas en un bloque de estado que se actualiza al cierre de cada sesión;
3. recuperar documentación técnica relevante mediante RAG en el momento de cada consulta;
4. conservar en memoria persistente únicamente las preferencias del usuario y el historial de incidentes resueltos.

El resultado es un contexto compacto, relevante y mucho más eficiente que acumular días de conversación sin filtrado.

---

# Buenas prácticas

- Diseñar una política explícita de descarte desde el inicio del proyecto.
- Resumir el contexto antes de alcanzar el límite del modelo, no después.
- Evitar duplicar información entre el historial, la memoria y los documentos RAG.
- Medir el crecimiento del contexto durante las pruebas de carga.
- Tratar la ventana como un recurso limitado, no como un almacén ilimitado.

---

# Resumen

La administración del contexto es una tarea continua, no una operación puntual. Las aplicaciones modernas combinan descarte, resumido, memoria y recuperación inteligente para mantener conversaciones extensas sin comprometer la calidad de las respuestas.

En la próxima sección estudiaremos las técnicas de resumido y compresión que permiten reducir el tamaño del contexto preservando la información esencial.
