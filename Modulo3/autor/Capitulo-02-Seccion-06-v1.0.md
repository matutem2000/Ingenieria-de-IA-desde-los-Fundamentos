# Capitulo-02-Seccion-06-v1.0

# La memoria persistente

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Mientras que el historial conversacional permite mantener el hilo de una sesión, la **memoria persistente** permite que un sistema recuerde información relevante entre conversaciones diferentes.

Esta capacidad es uno de los elementos que distingue a un asistente moderno de un simple chatbot.

---

# ¿Qué es la memoria persistente?

La memoria persistente es el conjunto de datos que una aplicación conserva más allá de una conversación individual para mejorar futuras interacciones.

A diferencia del historial, no representa una secuencia cronológica de mensajes, sino conocimiento útil sobre el usuario, el dominio o la aplicación.

---

# ¿Qué puede recordar un asistente?

Dependiendo del caso de uso, la memoria puede almacenar:

- preferencias del usuario;
- idioma habitual;
- zona horaria;
- proyectos activos;
- decisiones previas;
- configuraciones frecuentes;
- estilo de comunicación.

En un entorno empresarial también puede registrar:

- equipos asignados;
- áreas de trabajo;
- autorizaciones;
- procesos iniciados;
- contexto de negocio.

---

# ¿Qué NO debería almacenarse?

No toda la información merece convertirse en memoria.

Evite persistir:

- datos temporales;
- resultados de consultas puntuales;
- información desactualizada;
- mensajes triviales;
- contenido redundante.

Una memoria excesiva termina degradando la calidad del contexto.

---

# Tipos de memoria

## Memoria del usuario

Describe características relativamente estables del usuario.

## Memoria de la aplicación

Conserva estado y decisiones relevantes para el funcionamiento del sistema.

## Memoria del dominio

Almacena información específica del negocio que puede reutilizarse en múltiples conversaciones.

Cada tipo posee un ciclo de vida diferente y requiere políticas propias de actualización.

---

# Ciclo de vida

Una implementación profesional responde cuatro preguntas:

1. ¿Qué información se almacena?
2. ¿Cuándo se actualiza?
3. ¿Cuándo deja de ser válida?
4. ¿Quién puede utilizarla?

Responder estas preguntas evita memorias inconsistentes y problemas de seguridad.

---

# Caso práctico

En un asistente corporativo, un usuario indica que prefiere recibir las respuestas en español técnico y en formato Markdown.

Esa preferencia puede almacenarse como memoria persistente.

En futuras conversaciones ya no será necesario solicitarla nuevamente.

Sin embargo, el estado de un ticket consultado hace una semana probablemente no deba conservarse como memoria.

---

# Buenas prácticas

- Definir criterios claros de persistencia.
- Versionar estructuras de memoria cuando evolucionen.
- Permitir actualizar o eliminar información.
- Evitar almacenar datos sensibles sin necesidad.
- Auditar periódicamente la calidad de la memoria.

---

# Error frecuente

Un error habitual consiste en utilizar la memoria como un depósito ilimitado de información.

La memoria no debe crecer indefinidamente. Debe permanecer útil, consistente y relevante para las tareas futuras.

---

# Resumen

La memoria persistente aporta continuidad entre conversaciones y permite personalizar la experiencia del usuario. Diseñarla correctamente requiere definir políticas de creación, actualización y eliminación, diferenciándola claramente del historial conversacional.

En la siguiente sección estudiaremos cómo interactúan memoria, historial y recuperación de conocimiento para construir un contexto completo y equilibrado.
