# Capitulo-02-Seccion-03-v1.0

# Las instrucciones del sistema: el ADN del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Si el contexto fuese una organización, las instrucciones del sistema serían su estatuto. Definen las reglas permanentes de funcionamiento del modelo y establecen los límites dentro de los cuales deberá responder.

En la mayoría de las aplicaciones empresariales, esta es la capa más estable y una de las más importantes de toda la arquitectura.

---

# ¿Qué son las instrucciones del sistema?

Las instrucciones del sistema son mensajes preparados por la aplicación antes de incorporar el mensaje del usuario.

Su finalidad es definir:

- el rol del modelo;
- el idioma de respuesta;
- el nivel técnico esperado;
- restricciones de seguridad;
- formato de salida;
- objetivos del asistente.

Estas instrucciones no deberían contener información específica de una conversación, sino reglas generales de comportamiento.

---

# Responsabilidades

Una buena instrucción del sistema responde preguntas como:

- ¿Quién sos?
- ¿Cómo debés responder?
- ¿Qué nunca debés hacer?
- ¿Qué formato debés utilizar?
- ¿Qué prioridad tienen otras instrucciones?

Separar estas decisiones del resto del contexto simplifica el mantenimiento de la solución.

---

# Ejemplo

En lugar de escribir en cada consulta:

> "Actuá como un arquitecto de software, respondé en español, utilizá Markdown y justificá las decisiones."

Una aplicación profesional incorpora estas reglas una sola vez dentro de la capa de sistema.

El usuario únicamente expresa su necesidad.

---

# Qué NO debería incluir

Evite colocar en las instrucciones del sistema:

- datos temporales;
- resultados de APIs;
- documentos RAG;
- historial conversacional;
- preferencias específicas de un usuario.

Esos elementos pertenecen a otras capas del contexto.

---

# Diseño recomendado

Una estructura habitual incluye:

1. Identidad del asistente.
2. Objetivo principal.
3. Restricciones.
4. Políticas de seguridad.
5. Formato esperado.
6. Criterios de calidad.

Este orden facilita la lectura y el mantenimiento.

---

# Error frecuente

Un error común consiste en convertir las instrucciones del sistema en un documento enorme que intenta resolver todos los escenarios posibles.

Esto produce:

- mayor consumo de tokens;
- contradicciones;
- dificultad para evolucionar la aplicación.

Las reglas permanentes deben ser pocas, claras y estables.

---

# Nota del arquitecto

Cada vez que una regla cambia con frecuencia, pregúntese si realmente pertenece a la capa de sistema o debería convertirse en contexto dinámico.

Las capas estables y dinámicas no deberían mezclarse.

---

# Resumen

Las instrucciones del sistema constituyen el fundamento sobre el cual se construye el resto del contexto. Definen la identidad del asistente y garantizan un comportamiento consistente entre conversaciones.

En la próxima sección analizaremos el contexto de ejecución y cómo incorporar información dinámica sin comprometer la estabilidad de la arquitectura.
