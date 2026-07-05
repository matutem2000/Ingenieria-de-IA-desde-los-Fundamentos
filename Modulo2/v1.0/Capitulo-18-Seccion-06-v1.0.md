# Módulo 2 — Prompt Engineering Profesional
# Capítulo 18 — Prompt Engineering para Producción
## Sección 06 — Despliegue continuo de prompts

> *"La calidad no se preserva mediante despliegues esporádicos. Se preserva mediante procesos repetibles."*

---

## Objetivos de aprendizaje

- Integrar diseño, evaluación y observabilidad en un flujo continuo.
- Comprender el papel del despliegue controlado de prompts.
- Introducir el concepto de integración continua para Prompt Engineering.
- Preparar las bases de PromptOps.

---

## Introducción

Estos procesos no deberían ejecutarse de manera aislada.

Las organizaciones que desarrollan soluciones de IA necesitan incorporar el Prompt Engineering dentro de un ciclo continuo de evolución, donde cada cambio sea evaluado, desplegado y monitoreado siguiendo procedimientos consistentes.

Desde la perspectiva del AI Engineering, un prompt debe recorrer un proceso similar al de cualquier componente de software.

---

## Del cambio al despliegue

Modificar un prompt implica introducir un cambio potencial sobre el comportamiento de la aplicación.

Por ello, cada nueva versión debería atravesar un flujo controlado antes de llegar a producción.

```mermaid
flowchart LR
A[Diseño]
--> B[Control de versiones]
--> C[Pruebas]
--> D[Evaluación]
--> E[Aprobación]
--> F[Despliegue]
--> G[Observabilidad]
--> H[Mejora continua]
```

Este ciclo reduce el riesgo de regresiones y facilita la incorporación de mejoras de forma incremental.

---

## Integración continua para prompts

Aunque el concepto proviene de la ingeniería de software, sus principios pueden aplicarse al Prompt Engineering.

Un flujo de integración continua puede incluir:

| Etapa | Objetivo |
|-------|----------|
| Validación sintáctica | Detectar errores evidentes. |
| Ejecución de evaluation sets | Comparar resultados con versiones anteriores. |
| Verificación del formato | Confirmar compatibilidad con aplicaciones consumidoras. |
| Revisión técnica | Evaluar cambios significativos. |
| Aprobación | Autorizar el despliegue. |

Automatizar estas tareas disminuye la probabilidad de introducir cambios no deseados.

---

## Despliegues progresivos

No todas las modificaciones requieren reemplazar inmediatamente la versión en producción.

En muchos escenarios resulta conveniente adoptar estrategias como:

- despliegues por etapas;
- grupos piloto;
- pruebas A/B (comparación simultánea de dos variantes sobre grupos de usuarios distintos para medir cuál obtiene mejor resultado);
- canary releases (despliegues graduales donde la nueva versión se habilita inicialmente para un porcentaje reducido de usuarios);
- reversión automática ante degradación.

Estas prácticas permiten validar el comportamiento del prompt utilizando evidencia obtenida en condiciones reales.

---

## Caso de estudio

Una empresa actualiza el prompt utilizado por un asistente de atención al cliente.

En lugar de reemplazar la versión existente para todos los usuarios, habilita la nueva variante únicamente para el 10 % de las consultas.

Las métricas muestran una mejora en la precisión, pero también un incremento en la latencia.

Con esta información el equipo optimiza el prompt antes de completar el despliegue.

La estrategia evita afectar a la totalidad de los usuarios y reduce el riesgo operativo.

---

## Buenas prácticas

- Automatizar el mayor número posible de verificaciones.
- Mantener criterios claros de aprobación.
- Desplegar cambios de forma gradual cuando el impacto sea elevado.
- Registrar cada despliegue y sus resultados.

---

## Errores frecuentes

- Modificar prompts directamente en producción.
- Desplegar sin ejecutar pruebas comparativas.
- Carecer de mecanismos de reversión.
- No medir el impacto posterior al despliegue.

---

## Ideas clave

- Los prompts deben evolucionar mediante procesos controlados.
- La automatización reduce riesgos y mejora la calidad.
- El despliegue constituye una etapa más del ciclo de vida del prompt.

---

## Transición hacia la siguiente sección

En la próxima sección integraremos todos los conceptos estudiados para introducir formalmente PromptOps como disciplina encargada de gobernar el ciclo de vida completo de los prompts en plataformas empresariales de IA.
