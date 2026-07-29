# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 12 — Checklist del AI Engineer

> *"Una lista de verificación no reemplaza el juicio. Lo complementa: captura el conocimiento acumulado de lo que puede salir mal antes de que salga mal."*

---

## Propósito

Esta sección presenta la lista de verificación que el AI Engineer debe aplicar antes de desplegar un agente en un entorno de producción. Está organizada por las categorías críticas de diseño identificadas a lo largo del capítulo.

La lista no es exhaustiva para todos los contextos posibles. Es el conjunto mínimo de verificaciones que deben superarse antes de que un agente opere con usuarios o sistemas reales.

---

## Categoría 1: Definición del agente

- [ ] El objetivo del agente está definido con precisión: qué debe producir, para quién y en qué condiciones.
- [ ] Las condiciones de éxito son verificables, no ambiguas.
- [ ] Las condiciones de fallo están definidas y son detectables por la capa de orquestación.
- [ ] El nivel de autonomía está documentado y aprobado por el responsable del sistema.
- [ ] Los límites del agente están establecidos en el system prompt: qué puede hacer y qué nunca debe intentar.

---

## Categoría 2: Herramientas

- [ ] Cada herramienta tiene una descripción que indica cuándo usarla y cuándo no.
- [ ] El formato de parámetros y el formato del output están documentados para cada herramienta.
- [ ] Las herramientas irreversibles están marcadas como tales en su descripción.
- [ ] No hay herramientas con efectos secundarios ocultos no documentados.
- [ ] El catálogo de herramientas cubre las operaciones necesarias sin incluir herramientas innecesarias.
- [ ] Existe una herramienta o mecanismo explícito para que el agente declare terminación.

---

## Categoría 3: Puntos de control y supervisión

- [ ] Todas las acciones irreversibles tienen un punto de control que requiere confirmación humana antes de ejecutarse.
- [ ] Todas las acciones que afectan a terceros (enviar comunicaciones, modificar datos de clientes) tienen punto de control.
- [ ] La política de escalada está definida: cuándo el agente escala y a quién.
- [ ] El agente tiene instrucciones explícitas sobre cómo comportarse en situaciones ambiguas (escalar, no adivinar).

---

## Categoría 4: Condiciones de terminación y fallos

- [ ] Existe un límite de iteraciones implementado en la capa de orquestación (no solo en el razonamiento del LLM).
- [ ] Existe un timeout absoluto de ejecución.
- [ ] La capa de orquestación detecta bucles (misma acción, mismos parámetros, iteraciones consecutivas).
- [ ] El agente produce una respuesta de fallo informativa cuando no puede completar el objetivo.
- [ ] La respuesta de fallo incluye: qué se completó, en qué punto ocurrió el obstáculo, y las opciones disponibles.

---

## Categoría 5: Gestión de contexto y memoria

- [ ] El contexto no crece sin límite: existe una estrategia de compresión o gestión del historial.
- [ ] El límite de tokens por iteración está calculado y no supera el 70% de la ventana disponible en la iteración más costosa esperada.
- [ ] La información que persiste en memoria está definida: qué se guarda y qué se descarta.
- [ ] La memoria con datos sensibles tiene controles de acceso y política de retención.

---

## Categoría 6: Seguridad

- [ ] El agente no puede actuar fuera de su alcance definido, incluso si el usuario lo solicita explícitamente.
- [ ] Las herramientas que acceden a sistemas externos usan autenticación y no exponen credenciales en el contexto.
- [ ] El sistema valida los parámetros generados por el LLM antes de pasarlos a las herramientas (no confía ciegamente en la generación del modelo).
- [ ] Existe logging de todas las acciones del agente para auditoría posterior.
- [ ] Se han probado escenarios de inyección de prompt: ¿puede un input malicioso del usuario hacer que el agente ejecute acciones no autorizadas?

---

## Categoría 7: Evaluación y monitoreo

- [ ] Existe un conjunto de casos de prueba que cubren el happy path, casos borde y escenarios de fallo.
- [ ] El número promedio de iteraciones por tarea ha sido medido en el entorno de staging.
- [ ] El costo promedio por ejecución ha sido calculado y es aceptable para el volumen esperado.
- [ ] Existen métricas en producción: latencia por iteración, tasa de éxito, tasa de escalada, número de iteraciones promedio.
- [ ] Existe una alerta para cuando la tasa de fallos supera un umbral definido.

---

## Categoría 8: Documentación operativa

- [ ] El system prompt del agente está bajo control de versiones.
- [ ] Los cambios al system prompt tienen un proceso de revisión y testing antes de desplegarse.
- [ ] Existe documentación de las herramientas disponible para el equipo de operaciones.
- [ ] Existe un runbook para los fallos más frecuentes: cómo diagnosticar, cómo intervenir manualmente si el agente falla.

---

## Uso de la lista

Esta lista debe completarse antes del primer despliegue a producción y revisarse antes de cada cambio significativo en el sistema (nuevas herramientas, cambios en el system prompt, cambios en la capa de orquestación).

Los ítems marcados como no aplica deben documentarse con la justificación. Un ítem que no aplica sin justificación es un ítem pendiente.

---

## Nota del Arquitecto

> Esta lista cubre el diseño del agente. La operación del agente después del despliegue requiere una lista adicional: qué monitorear, cómo interpretar las métricas, cuándo intervenir manualmente y cómo actualizar el agente sin interrumpir el servicio. La lista de diseño y la lista de operación son complementarias; una sin la otra produce sistemas que funcionan en el despliegue inicial pero degradan en las semanas siguientes.

---

## Ideas clave

- El checklist de despliegue organiza las verificaciones en ocho categorías: definición, herramientas, puntos de control, condiciones de terminación, gestión de contexto, seguridad, evaluación y documentación.
- Los ítems de seguridad y puntos de control no son negociables antes del despliegue en producción.
- Un ítem marcado como "no aplica" debe justificarse. La ausencia de justificación es una señal de que el ítem no fue considerado.
- La lista de despliegue es distinta de la lista de operación. Ambas son necesarias para un sistema de agentes en producción.

---

## Transición hacia la siguiente sección

Con el checklist completado, el capítulo llega a su cierre. La siguiente sección consolida las ideas principales del capítulo en un resumen estructurado que puede usarse como referencia rápida.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
