# Capitulo-20-Seccion-02-v0.1

# Módulo 2 — Prompt Engineering Profesional

# Capítulo 20 — Arquitecturas Basadas en Prompts

**Versión:** 0.1  
**Estado:** Manuscrito del autor

> *"Una arquitectura escalable no depende de componentes más grandes. Depende de componentes mejor organizados."*

---

# Objetivos de aprendizaje

- Comprender los principios de composición de prompts.
- Analizar estrategias para construir flujos reutilizables.
- Diseñar arquitecturas modulares basadas en prompts especializados.
- Introducir patrones de orquestación entre prompts.

---

# Introducción

En la sección anterior analizamos cómo un prompt puede convertirse en un componente arquitectónico.

Sin embargo, pocas aplicaciones empresariales resuelven un problema utilizando un único componente.

La mayoría implementa una secuencia de prompts especializados que colaboran entre sí para alcanzar un objetivo común.

La calidad de la solución deja de depender únicamente del diseño individual de cada prompt y pasa a depender de la forma en que estos interactúan.

---

# Composición de prompts

La composición consiste en organizar varios prompts especializados para resolver un problema complejo mediante una secuencia de tareas más simples.

Cada componente recibe una entrada, produce una salida y delega el siguiente paso cuando corresponde.

```mermaid
flowchart LR
A[Consulta]
--> B[Prompt de clasificación]

B --> C[Prompt de recuperación]

C --> D[Prompt de análisis]

D --> E[Prompt de validación]

E --> F[Prompt de generación]

F --> G[Respuesta]
```

Este enfoque favorece la separación de responsabilidades y reduce el impacto de los cambios.

---

# Beneficios de la modularidad

Una arquitectura modular ofrece ventajas tanto técnicas como operativas.

| Beneficio | Descripción |
|-----------|-------------|
| Reutilización | Un mismo prompt puede participar en distintos procesos. |
| Mantenibilidad | Los cambios afectan únicamente al componente involucrado. |
| Escalabilidad | Es posible incorporar nuevos módulos sin rediseñar toda la solución. |
| Observabilidad | Permite medir el comportamiento de cada etapa del flujo. |
| Pruebas independientes | Cada prompt puede validarse de forma aislada. |

Estos principios resultan familiares para cualquier arquitecto de software y mantienen plena vigencia en AI Engineering.

---

# Patrones de composición

Existen diversas formas de organizar una arquitectura basada en prompts.

- **Pipeline secuencial:** cada prompt consume la salida del anterior.
- **Ramificación:** diferentes prompts resuelven tareas específicas en paralelo.
- **Convergencia:** múltiples resultados se integran en una respuesta unificada.
- **Orquestación condicional:** el flujo cambia según el resultado de una etapa previa.

La elección dependerá de la naturaleza del problema y de los requisitos del negocio.

---

# Caso de estudio

Una aseguradora implementa un asistente para gestionar siniestros.

La solución se divide en cinco componentes:

1. clasificación de la consulta;
2. recuperación de información relevante;
3. validación de cobertura;
4. generación de recomendaciones;
5. construcción de la respuesta final.

Cuando cambia la normativa de cobertura, únicamente se modifica el prompt responsable de esa etapa.

El resto de la arquitectura permanece inalterado.

---

# Buenas prácticas

- Asignar una única responsabilidad a cada prompt.
- Definir contratos de entrada y salida.
- Diseñar componentes reutilizables.
- Evitar dependencias innecesarias entre módulos.
- Documentar cada flujo de composición.

---

# Errores frecuentes

- Encadenar prompts sin una estrategia de diseño.
- Transferir información redundante entre componentes.
- Acoplar varios procesos en un único prompt.
- Ignorar el impacto acumulado sobre latencia y consumo de tokens.

---

# Ideas clave

- La composición transforma prompts individuales en arquitecturas completas.
- La modularidad facilita mantenimiento, pruebas y evolución.
- Un buen diseño reduce complejidad sin perder capacidad funcional.

---

# Transición hacia la siguiente sección

En la próxima sección estudiaremos arquitecturas jerárquicas de prompts, donde un componente coordinador distribuye responsabilidades entre prompts especializados siguiendo principios de orquestación propios del AI Engineering.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
