# Capitulo-02-Seccion-04-v1.0

# El contexto de ejecución

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Las instrucciones del sistema proporcionan estabilidad, pero por sí solas no alcanzan para responder correctamente en un entorno empresarial. Cada interacción ocurre dentro de una situación concreta que cambia continuamente.

**El contexto de ejecución** es el conjunto de datos temporales que describen el estado actual de la aplicación, del usuario y del entorno en un instante determinado. A diferencia de las instrucciones del sistema, estos datos pueden variar entre dos solicitudes consecutivas y carecen de valor una vez finalizada la operación.

---

# Características

El contexto de ejecución posee cuatro propiedades fundamentales:

1. **Temporal**: cambia constantemente.
2. **Específico**: pertenece a una única interacción o sesión.
3. **Derivado**: suele obtenerse de otros sistemas.
4. **Descartable**: gran parte deja de tener valor al finalizar la operación.

---

# ¿Qué contiene?

Ejemplos habituales de datos de ejecución:

- usuario autenticado;
- rol y permisos;
- organización;
- idioma de la sesión;
- fecha y hora;
- ubicación;
- estado de un proceso;
- identificadores de recursos.

---

# Ejemplo práctico

Supongamos una aplicación de gestión documental.

El usuario solicita:

> "Mostrame los expedientes pendientes."

La aplicación incorpora automáticamente:

- usuario: María Gómez;
- organismo: Dirección Jurídica;
- permisos: lectura y aprobación;
- fecha actual;
- expediente activo;
- filtros de seguridad.

El LLM ya no responde a una pregunta genérica, sino a una consulta contextualizada.

---

# Separación de responsabilidades

Una arquitectura saludable mantiene separados:

| Componente | Responsabilidad |
|------------|-----------------|
| Sistema | Reglas permanentes |
| Contexto de ejecución | Estado actual |
| Memoria | Información persistente |
| Historial | Conversación vigente |
| RAG | Conocimiento recuperado |

Esta separación reduce el acoplamiento y facilita la evolución del sistema.

---

# Errores frecuentes

Entre los problemas más habituales se encuentran:

- incluir datos temporales dentro del prompt del sistema;
- reutilizar contexto de una sesión anterior;
- enviar permisos incorrectos;
- no validar la identidad del usuario antes de construir el contexto.

Cada uno de estos errores puede producir respuestas incorrectas o incluso incidentes de seguridad.

---

# Buenas prácticas

- Construir el contexto inmediatamente antes de la inferencia.
- Validar siempre autenticación y autorización.
- Incorporar únicamente información necesaria para la solicitud actual.
- Evitar duplicar datos presentes en otras capas.

---

# Resumen

El contexto de ejecución conecta el mundo real con el modelo de lenguaje. Es la capa que adapta las reglas generales del sistema a la situación concreta de cada interacción.

En la próxima sección analizaremos cómo el historial conversacional aporta continuidad y cuáles son las estrategias para administrarlo sin superar los límites de la ventana de contexto.
