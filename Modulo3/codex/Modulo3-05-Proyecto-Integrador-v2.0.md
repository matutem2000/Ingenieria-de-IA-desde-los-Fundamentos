# Proyecto integrador

## Título

Diseño de una plataforma empresarial de IA basada en Context Engineering.

## Objetivo

Diseñar y defender la arquitectura de una plataforma empresarial que utilice un Large Language Model (LLM) para resolver un problema concreto. La propuesta deberá integrar instrucciones, estado, memoria, conocimiento y herramientas, y demostrar cómo controla la calidad, el costo, la latencia, la seguridad y la trazabilidad.

El proyecto evalúa criterio de arquitectura. No alcanza con enumerar componentes o productos: cada decisión debe vincularse con un requisito, una restricción, una alternativa considerada y una evidencia de validación.

## Escenario mínimo

La solución deberá:

- atender a más de un perfil de usuario;
- consultar conocimiento empresarial con permisos diferenciados;
- conservar el estado necesario entre interacciones;
- ejecutar al menos una acción mediante una herramienta;
- manejar información desactualizada, ausente o contradictoria;
- registrar evidencia suficiente para explicar y evaluar su comportamiento.

El lector podrá elegir el dominio —por ejemplo, desarrollo de software, industria, finanzas, salud o gobierno— siempre que documente sus supuestos y respete las restricciones propias del escenario.

## Entregables

1. **Definición del problema:** usuarios, necesidades, alcance, supuestos y exclusiones.
2. **Requisitos:** requisitos funcionales y no funcionales, restricciones y criterios de éxito.
3. **Documento de arquitectura:** componentes, responsabilidades, límites y flujos principales.
4. **Diagramas:** contexto, contenedores y secuencia de una interacción representativa.
5. **Registros de decisiones de arquitectura (ADR):** decisiones principales, alternativas y consecuencias.
6. **Diseño del contexto:** fuentes, prioridades, presupuesto, ensamblado y política de descarte.
7. **Estrategia de instrucciones:** jerarquía, reglas, formatos y manejo de conflictos.
8. **Estrategia de memoria:** tipos, persistencia, recuperación, actualización, caducidad y aislamiento.
9. **Estrategia de recuperación:** fuentes, segmentación, relevancia, permisos, procedencia y vigencia.
10. **Diseño de herramientas:** contratos, validación, autorización, errores, reintentos e idempotencia.
11. **Modelo de amenazas y controles:** fuga de datos, inyección de prompts, acceso indebido y acciones no autorizadas.
12. **Plan de evaluación:** conjunto de pruebas, métricas, línea de base y umbrales de aceptación.
13. **Estimación operativa:** costo, latencia, escalabilidad, observabilidad y mantenimiento.
14. **Limitaciones y evolución:** riesgos residuales, deuda técnica y próximos pasos.

## Criterios de evaluación

| Dimensión | Evidencia esperada |
|---|---|
| Coherencia arquitectónica | Los componentes y flujos responden al problema y no se contradicen. |
| Trazabilidad | Cada decisión principal se relaciona con requisitos, restricciones o riesgos. |
| Calidad del contexto | Las fuentes, prioridades y políticas de selección están justificadas y pueden evaluarse. |
| Seguridad y privacidad | Los permisos, límites de confianza, datos sensibles y acciones están controlados. |
| Escalabilidad y resiliencia | La propuesta contempla carga, fallas, degradación y recuperación. |
| Costo y rendimiento | Existen presupuestos, métricas y compromisos explícitos de costo y latencia. |
| Mantenibilidad | Las responsabilidades están separadas y las decisiones relevantes están documentadas. |
| Evaluación | Las métricas, pruebas y umbrales permiten detectar mejoras y regresiones. |
| Comunicación técnica | Los documentos y diagramas permiten comprender y defender la solución. |

## Criterios de aprobación

El proyecto se considerará aprobado cuando:

- todos los entregables obligatorios estén presentes y sean consistentes;
- las decisiones principales estén justificadas mediante evidencia o supuestos explícitos;
- exista al menos una alternativa descartada para cada decisión crítica;
- el plan de evaluación incluya casos normales, casos límite y fallas previsibles;
- los riesgos residuales y las limitaciones estén declarados;
- otra persona pueda comprender, evaluar y continuar el diseño a partir de la documentación.

## Defensa del proyecto

La presentación final deberá explicar:

1. qué problema se resolvió;
2. qué decisiones determinaron la arquitectura;
3. qué compromisos se aceptaron;
4. cómo se comprobará que la solución funciona;
5. qué condiciones obligarían a revisar el diseño.

> Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones.
