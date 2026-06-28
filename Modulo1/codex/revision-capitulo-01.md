# Revisión técnica y pedagógica — Capítulo 1

**Proyecto:** Ingeniería de IA desde los Fundamentos  
**Módulo:** I — Los Fundamentos de la Inteligencia Artificial  
**Capítulo:** 1 — ¿Qué entendemos por inteligencia?  
**Versión de entrada:** v0.1  
**Versión generada:** v0.5  
**Archivo generado:** `Modulo1/codex/capitulo-01-v0.5.md`

---

## Guías revisadas

Se revisaron completas las guías disponibles en el árbol del proyecto:

- `../EDITORIAL_GUIDE.md`
- `../adr/STYLE_GUIDE.md`
- `../adr/REVIEW_PROCESS.md`
- `../adr/TERMINOLOGY.md`
- `../adr/LAB_GUIDE.md`
- `../adr/CODE GUIDE.md`

La ruta indicada por la consigna (`../../editorial/...`) no existe desde `Modulo1`. La guía de código existe en `../adr/` con nombre de archivo `CODE GUIDE.md` (con espacio), aunque su encabezado interno indica `CODE_GUIDE.md`.

---

## Alcance

Se trabajó únicamente sobre el Capítulo 1 y se generaron solo los tres archivos solicitados dentro de `Modulo1/codex/`:

- `capitulo-01-v0.5.md`
- `revision-capitulo-01.md`
- `diagramas-capitulo-01.md`

No se sobrescribió el archivo original v0.1.

---

## Cambios editoriales principales

La versión v0.1 presentaba una buena pregunta inicial y una orientación correcta hacia el criterio profesional. La versión v0.5 amplía esa base para convertirla en un capítulo editorial completo.

Cambios realizados:

- Se agregó front matter editorial.
- Se incorporaron objetivos de aprendizaje verificables.
- Se expandió la introducción con una narrativa más conectada al trabajo profesional.
- Se desarrolló la motivación del problema: por qué definir inteligencia importa para diseñar sistemas de IA.
- Se agregó explicación desde primeros principios.
- Se diferenció inteligencia como capacidad única de inteligencia como conjunto de capacidades.
- Se incorporó una tabla de capacidades asociadas con inteligencia.
- Se reforzó la distinción entre conducta inteligente y comprensión humana.
- Se agregaron analogías nuevas: empresa como sistema inteligente y tablero de control.
- Se agregó un diagrama Mermaid principal.
- Se incorporaron ejemplos empresariales: soporte interno, clasificación de tickets y decisiones de crédito.
- Se agregó conversación con un arquitecto.
- Se agregaron errores frecuentes y buenas prácticas.
- Se diseñó un laboratorio completo siguiendo `LAB_GUIDE.md`.
- Se agregaron preguntas de reflexión.
- Se incorporó resumen, checklist, glosario breve, referencias cruzadas, bibliografía y próximo capítulo.

---

## Decisiones técnicas y pedagógicas

1. **No comenzar por herramientas.**  
   El capítulo mantiene el principio editorial de partir del problema antes que de modelos, algoritmos o proveedores.

2. **Usar una definición operativa, no filosófica.**  
   Se evita cerrar el debate sobre qué es inteligencia. En su lugar, se propone una definición útil para ingeniería: capacidades observables aplicadas a problemas concretos.

3. **Introducir terminología oficial sin sobrecargar.**  
   Se mencionan Inteligencia Artificial (IA), Machine Learning (ML), Deep Learning (DL), Large Language Models (LLMs), Context Window, Retrieval-Augmented Generation (RAG), Inference y Modelo con la terminología indicada en `TERMINOLOGY.md`.

4. **Prevenir antropomorfismo.**  
   Se explicita que el modelo genera, clasifica o infiere, pero no "sabe", "entiende todo" ni tiene conciencia.

5. **Preparar continuidad.**  
   El capítulo queda conectado con los capítulos posteriores mediante referencias cruzadas, especialmente Capítulos 2, 4, 7, 12 y 14.

6. **Aplicar CODE_GUIDE sin incorporar código innecesario.**  
   El Capítulo 1 es conceptual y no requiere código ejecutable. Por consistencia con `CODE GUIDE.md`, no se agregaron ejemplos artificiales de código: el laboratorio se mantuvo como actividad de análisis, porque introducir código en este capítulo reduciría claridad pedagógica.

---

## Validación contra criterios editoriales

| Criterio | Estado |
|---|---|
| Objetivos definidos | Cumple |
| Introducción clara | Cumple |
| Motivación del problema | Cumple |
| Desarrollo conceptual | Cumple |
| Analogías | Cumple |
| Diagrama Mermaid | Cumple |
| Ejemplos reales | Cumple |
| Conversación con un arquitecto | Cumple |
| Errores frecuentes | Cumple |
| Buenas prácticas | Cumple |
| Laboratorio | Cumple |
| Preguntas de reflexión | Cumple |
| Resumen | Cumple |
| Checklist | Cumple |
| Bibliografía | Cumple |
| Próximo capítulo | Cumple |

---

## Observaciones para v0.8

- Confirmar si el proyecto tendrá un formato bibliográfico único.
- Validar si la definición operativa de inteligencia debe repetirse o refinarse en el Capítulo 2.
- Revisar la compatibilidad del diagrama Mermaid con el pipeline editorial final.
- Confirmar la numeración definitiva de capítulos antes de cerrar referencias cruzadas.
- Si en v0.8 se decide incorporar código, aplicar la estructura indicada por `CODE GUIDE.md`: ejemplo mínimo, reproducible, explicado, con nombres claros y sin dependencias innecesarias.

---

## Estado

Capítulo 1 listo como v0.5 para revisión conceptual y pedagógica.
