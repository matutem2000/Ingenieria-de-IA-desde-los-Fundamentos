# Capitulo-02-Seccion-02-v1.0

# El ciclo de vida del contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Una de las ideas más importantes del Context Engineering es que **el contexto no es estático**. Se crea, se enriquece, se transforma y finalmente se descarta o resume. Comprender este ciclo de vida es esencial para diseñar aplicaciones con LLM que sean eficientes y predecibles.

---

# El contexto como un flujo

En una aplicación empresarial, el contexto atraviesa varias etapas antes de llegar al modelo.

```text
Solicitud del usuario
        │
        ▼
Validación y autenticación
        │
        ▼
Construcción del contexto
        │
        ├─► Perfil del usuario
        ├─► Memoria
        ├─► Historial
        ├─► RAG
        ├─► Herramientas
        └─► Políticas
        │
        ▼
LLM
        │
        ▼
Respuesta
        │
        ▼
Actualización de memoria e historial
```

Cada fase puede modificar el contexto antes de la inferencia.

---

# Etapa 1 – Recepción

El sistema recibe la solicitud y obtiene información básica:

- identidad del usuario;
- canal de acceso;
- fecha y hora;
- permisos disponibles.

En esta etapa todavía no interviene el modelo.

---

# Etapa 2 – Enriquecimiento

La aplicación incorpora información adicional:

- memoria persistente;
- historial reciente;
- documentos recuperados mediante RAG;
- resultados de consultas a APIs;
- políticas internas.

El objetivo es entregar al modelo únicamente la información relevante.

---

# Etapa 3 – Inferencia

Con el contexto construido, el LLM genera una respuesta.

En este punto el modelo no consulta nuevas fuentes por sí mismo: razona sobre el contexto recibido.

Por ello, cualquier omisión o contradicción afecta directamente la calidad del resultado.

---

# Etapa 4 – Persistencia

Una vez obtenida la respuesta, el sistema decide qué conservar.

No todo debe almacenarse.

Ejemplos de información persistente:

- nuevas preferencias del usuario;
- decisiones relevantes;
- tareas pendientes.

En cambio, mensajes triviales o datos temporales pueden descartarse.

---

# Riesgos comunes

Un mal diseño del ciclo de vida suele producir:

- historiales interminables;
- memorias desactualizadas;
- documentos duplicados;
- aumento del costo por tokens;
- respuestas inconsistentes.

Estos problemas no suelen resolverse cambiando el modelo, sino rediseñando el flujo del contexto.

---

# Buenas prácticas

- Construir el contexto justo antes de la inferencia.
- Mantener separadas memoria e historial.
- Recuperar conocimiento bajo demanda.
- Eliminar información irrelevante.
- Persistir solo aquello que aporte valor futuro.

---

# Resumen

El contexto tiene un ciclo de vida completo: nace con la solicitud del usuario, se enriquece con distintas fuentes, alimenta al modelo y finalmente deja información útil para futuras interacciones. Diseñar correctamente este ciclo es una de las responsabilidades centrales del AI Engineer.

La siguiente sección analizará en detalle el papel de las instrucciones del sistema como la capa más estable y determinante del contexto.
