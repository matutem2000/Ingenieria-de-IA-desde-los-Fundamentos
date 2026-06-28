# Capítulo 8 — Seguridad, Gobernanza y Gestión Responsable de la IA
## Sección 06 — Supervisión Humana y Niveles de Autonomía

**Versión:** 1.0  
**Estado:** Aprobado para publicación

> *"La autonomía de un sistema nunca elimina la responsabilidad de la organización que lo utiliza."*

---

# Objetivos de aprendizaje

Al finalizar esta sección el lector será capaz de:

- comprender los distintos niveles de autonomía en soluciones de IA;
- identificar cuándo incorporar supervisión humana;
- diseñar arquitecturas con mecanismos de aprobación y escalamiento;
- equilibrar automatización, eficiencia y control.

---

# Introducción

Uno de los errores más frecuentes consiste en considerar la Inteligencia Artificial como un reemplazo absoluto del criterio humano.

En entornos empresariales ocurre lo contrario.

Cuanto mayor es el impacto potencial de una decisión, mayor suele ser la necesidad de incorporar mecanismos de supervisión.

La arquitectura debe definir explícitamente qué decisiones puede tomar el sistema de manera autónoma, cuáles requieren validación y cuáles permanecen exclusivamente bajo responsabilidad humana.

---

# Niveles de autonomía

```mermaid
flowchart LR
A[Asistencia]
--> B[Recomendación]
--> C[Ejecución supervisada]
--> D[Ejecución autónoma]
```

Cada nivel implica diferentes requisitos de seguridad, auditoría y gobierno.

No existe un nivel universalmente superior. La elección depende del riesgo asociado al proceso.

---

# Human in the Loop

El patrón **Human in the Loop (HITL)** incorpora a una persona antes de ejecutar acciones relevantes.

Algunos ejemplos son:

- aprobación de respuestas regulatorias;
- autorización de operaciones financieras;
- validación de diagnósticos clínicos;
- revisión de contratos generados automáticamente.

La IA acelera el trabajo, pero la decisión final continúa siendo humana.

---

# Human on the Loop

En otros escenarios el sistema ejecuta acciones automáticamente, mientras un operador supervisa el proceso y puede intervenir cuando detecta comportamientos anómalos.

Este enfoque resulta habitual en:

- monitoreo de infraestructura;
- clasificación masiva de documentos;
- automatización de procesos administrativos;
- atención inicial de consultas frecuentes.

---

# Caso de estudio

Una compañía aseguradora implementa un agente para procesar denuncias de siniestros.

Los casos simples son resueltos automáticamente.

Cuando el sistema detecta información inconsistente, documentación incompleta o un importe superior a un umbral definido, deriva la operación a un analista.

La arquitectura combina automatización con supervisión humana, reduciendo tiempos de respuesta sin comprometer el control sobre las decisiones de mayor impacto.

---

# Buenas prácticas

- Definir criterios claros para la intervención humana.
- Registrar quién aprobó cada decisión relevante.
- Permitir revertir acciones automatizadas cuando corresponda.
- Diseñar interfaces que faciliten la revisión de evidencia.
- Revisar periódicamente los umbrales de autonomía.

---

# Errores frecuentes

- Automatizar procesos críticos sin mecanismos de revisión.
- Delegar decisiones sensibles exclusivamente al modelo.
- No registrar intervenciones humanas.
- Incrementar la autonomía sin evaluar el riesgo del negocio.

---

# Ideas clave

- Automatizar no significa eliminar la supervisión.
- La autonomía debe crecer de forma gradual y controlada.
- El nivel de intervención humana depende del riesgo, no de la capacidad tecnológica.

---

# Transición hacia la siguiente sección

La próxima sección analizará los principios éticos aplicados al diseño de soluciones empresariales de IA y cómo traducir esos principios en decisiones concretas de arquitectura, gobierno y operación.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
