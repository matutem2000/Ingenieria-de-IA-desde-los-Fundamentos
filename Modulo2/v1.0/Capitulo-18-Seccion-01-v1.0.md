# Módulo 2 — Prompt Engineering Profesional

# Capítulo 18 — Prompt Engineering para Producción

## Sección 01 — Del prototipo al producto

> *"Un prompt puede funcionar perfectamente en una demostración y fracasar por completo cuando miles de usuarios comienzan a utilizarlo."*

---

## Objetivos de aprendizaje

- Comprender las diferencias entre un prompt experimental y uno preparado para producción.
- Identificar los requisitos no funcionales que debe satisfacer un prompt empresarial.
- Introducir el concepto de robustez en Prompt Engineering.
- Establecer las bases para el ciclo de vida operativo de los prompts.

---

## Introducción

Durante los capítulos anteriores analizamos cómo diseñar prompts y cómo seleccionar patrones adecuados para distintos problemas.

Sin embargo, escribir un buen prompt no garantiza el éxito de una aplicación.

La verdadera prueba comienza cuando ese prompt abandona el laboratorio y pasa a formar parte de un sistema utilizado por cientos o miles de personas.

En ese momento aparecen desafíos que no suelen manifestarse durante las pruebas iniciales:

- entradas impredecibles;
- variabilidad en las consultas;
- cambios en los modelos;
- restricciones de costo;
- integración con otros sistemas;
- requisitos de auditoría y cumplimiento.

El Prompt Engineering para Producción estudia precisamente cómo diseñar prompts capaces de soportar estas condiciones.

---

## Del prototipo al producto

En una prueba de concepto el objetivo consiste en demostrar que una idea es viable.

En producción, el objetivo cambia.

Ahora el sistema debe ser:

- confiable;
- mantenible;
- observable;
- reproducible;
- escalable.

El prompt deja de ser un experimento y pasa a convertirse en un componente crítico de la plataforma.

```mermaid
flowchart LR
A[Prototipo]
--> B[Validación]
--> C[Evaluación]
--> D[Versionado]
--> E[Producción]
--> F[Operación continua]
```

---

## Requisitos de un prompt de producción

| Requisito | Descripción |
|-----------|-------------|
| Robustez | Mantener un comportamiento consistente frente a entradas diversas. |
| Trazabilidad | Identificar la versión utilizada en cada ejecución. |
| Observabilidad | Medir calidad, costos y comportamiento. |
| Mantenibilidad | Facilitar cambios sin introducir regresiones. |
| Reproducibilidad | Poder repetir una ejecución bajo las mismas condiciones. En sistemas basados en Large Language Models (LLM), la reproducibilidad es un objetivo de control, no una garantía absoluta. |

Estos requisitos son comparables a los exigidos para cualquier otro componente de software empresarial.

---

## Caso de estudio

Una organización desarrolla un asistente para responder consultas de recursos humanos.

Durante las pruebas internas el sistema obtiene excelentes resultados.

Tras el despliegue aparecen consultas incompletas, mensajes con errores ortográficos, instrucciones ambiguas y solicitudes fuera del alcance previsto.

El problema no reside en el modelo.

Tampoco en el conocimiento disponible.

El problema radica en que el prompt fue diseñado para un entorno controlado y no para un escenario real de producción.

---

## Buenas prácticas

- Diseñar pensando en entradas impredecibles.
- Definir criterios objetivos de calidad.
- Incorporar evaluación continua.
- Mantener un historial de versiones.
- Instrumentar métricas desde el primer despliegue.

---

## Errores frecuentes

- Considerar suficiente una demostración exitosa.
- Desplegar prompts sin pruebas sistemáticas.
- No registrar la versión utilizada.
- Ignorar requisitos no funcionales.

---

## Ideas clave

- Producción exige requisitos diferentes a los de un prototipo.
- Un prompt empresarial debe ser robusto, medible y mantenible.
- Gobernar un prompt implica trazabilidad, observabilidad y mejora continua basada en evidencia.

---

## Transición hacia la siguiente sección

En la próxima sección analizaremos el concepto de robustez en profundidad y estudiaremos técnicas para diseñar prompts capaces de responder correctamente frente a entradas inesperadas.
