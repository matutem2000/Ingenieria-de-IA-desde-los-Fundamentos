# Capitulo-03-Seccion-05-v1.0

# Cuando el contexto supera la ventana disponible

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Toda ventana de contexto, por grande que sea, tiene un límite. Tarde o temprano una conversación extensa, un conjunto de documentos o una combinación de herramientas y memoria terminarán superando esa capacidad.

El desafío del ingenieros de IA consiste en decidir **qué información conservar, cuál resumir y cuál descartar**, maximizando la calidad del contexto sin exceder el límite del modelo.

---

# ¿Qué ocurre al superar el límite?

Cuando el contexto excede la capacidad admitida por el modelo, pueden producirse distintas situaciones dependiendo del proveedor:

- rechazo de la solicitud;
- truncamiento automático del contexto;
- eliminación de los mensajes más antiguos;
- necesidad de reconstruir el contexto antes de reenviar la consulta.

En cualquier caso, el modelo no podrá razonar sobre información que ya no forme parte de la ventana.

---

# El problema de las conversaciones largas

Imagine un asistente que acompaña a un usuario durante varias semanas.

Cada interacción agrega:

- nuevos mensajes;
- resultados de herramientas;
- documentos recuperados;
- instrucciones adicionales.

Si todo permanece dentro del contexto, llegará un momento en que el modelo no podrá procesarlo completamente.

Por este motivo, las aplicaciones profesionales nunca dependen exclusivamente del historial conversacional.

---

# Estrategias de administración

Existen varias técnicas para mantener el contexto dentro de límites razonables.

## 1. Descarte selectivo

Eliminar información que ya no aporta valor.

Ejemplos:

- saludos;
- mensajes repetidos;
- respuestas obsoletas.

## 2. Resumido

Reemplazar múltiples interacciones por un resumen estructurado que conserve únicamente los hechos relevantes.

## 3. Recuperación bajo demanda

En lugar de mantener toda la información en memoria, recuperarla cuando realmente sea necesaria mediante mecanismos como RAG.

## 4. Memoria persistente

Guardar únicamente conocimientos duraderos y reutilizables, evitando conservar eventos transitorios.

---

# Elegir qué conservar

Una pregunta útil durante el diseño es:

> "¿El modelo necesitará esta información para responder correctamente dentro de diez minutos?"

Si la respuesta es negativa, probablemente no deba permanecer en el contexto activo.

---

# Caso práctico

Supongamos un asistente de soporte que atiende un incidente durante varios días.

Una arquitectura eficiente podría:

1. mantener únicamente las últimas interacciones;
2. resumir las decisiones tomadas;
3. recuperar documentación técnica mediante RAG;
4. conservar en memoria únicamente las preferencias del usuario.

El resultado es un contexto compacto, relevante y mucho más eficiente.

---

# Buenas prácticas

- Diseñar una política explícita de descarte.
- Resumir antes de alcanzar el límite del modelo.
- Evitar duplicar información entre historial y memoria.
- Medir el crecimiento del contexto durante las pruebas.
- Tratar la ventana como un recurso limitado.

---

# Resumen

La administración del contexto es una tarea continua, no una operación puntual. Las aplicaciones modernas combinan descarte, resumido, memoria y recuperación inteligente para mantener conversaciones extensas sin comprometer la calidad de las respuestas.

En la próxima sección estudiaremos las técnicas de resumido y compresión que permiten reducir el tamaño del contexto preservando la información esencial.
