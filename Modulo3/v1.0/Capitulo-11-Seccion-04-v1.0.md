# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 04: Contexto para diseño y arquitectura

La fase de diseño es donde el arquitecto de software toma las decisiones más difíciles del proyecto: qué estructura tendrá el sistema, cómo se comunicarán sus componentes, qué patrones se aplicarán, qué restricciones no funcionales determinan las elecciones técnicas. Estas decisiones tienen efectos de largo plazo — el costo de revertirlas una vez que el código está escrito puede ser enorme.

La IA puede asistir en esta fase de formas valiosas, pero opera bajo una limitación fundamental que el arquitecto debe entender claramente: el modelo no tiene juicio de negocio propio, no conoce el contexto organizacional del equipo y no evaluará correctamente las restricciones tácitas que solo el arquitecto conoce. Lo que puede hacer es amplificar el razonamiento del arquitecto cuando se le proporciona el contexto correcto.

### Qué aporta la IA al diseño arquitectónico

La asistencia de IA en diseño y arquitectura es valiosa en cuatro áreas específicas:

**Evaluación de alternativas.** Dado un problema de diseño con restricciones explícitas, el modelo puede describir las alternativas de solución conocidas, con sus trade-offs, precedentes de uso y condiciones bajo las cuales cada una es preferible. El arquitecto no usa esto como un oráculo que le dice qué hacer — lo usa como un sistema de consulta que le muestra el espacio de soluciones antes de tomar su decisión.

**Verificación de consistencia.** Una vez que el arquitecto tiene un diseño propuesto, el modelo puede verificar si ese diseño es consistente con los principios y restricciones documentados del proyecto. Si el ADR número 7 establece que el sistema no debe tener dependencias directas entre el módulo A y el módulo B, y el diseño propuesto introduce una dependencia de ese tipo, el modelo puede identificarlo — si esos ADRs están en el contexto.

**Documentación de decisiones.** Los ADRs son artefactos de alta calidad que los equipos producen con baja frecuencia, en parte porque documentarlos correctamente es costoso en tiempo. Con el contexto de la discusión de diseño y la decisión tomada, el modelo puede generar un borrador de ADR que el arquitecto revisa y aprueba. Esto reduce el costo de documentar sin reducir la calidad.

**Identificación de riesgos.** Dado un diseño propuesto, el modelo puede identificar patrones de riesgo conocidos: acoplamientos que pueden crear bottlenecks, decisiones que limitan la escalabilidad futura, dependencias de terceros con historial de breaking changes. El arquitecto evalúa cuáles de estos riesgos son relevantes en su contexto específico.

### El contexto necesario para asistencia en diseño

La calidad de la asistencia en diseño depende directamente de qué contexto recibe el modelo. Los elementos mínimos necesarios son:

**Restricciones del sistema.** Los requisitos no funcionales del proyecto: latencia máxima, throughput esperado, presupuesto de infraestructura, restricciones de seguridad, regulaciones aplicables. Sin estas restricciones, el modelo generará diseños académicamente correctos pero posiblemente inviables en el contexto del proyecto.

**Principios arquitectónicos establecidos.** Si el equipo adoptó decisiones arquitectónicas previas — microservicios vs. monolito, base de datos centralizada vs. distribuida, patrones de messaging — estas decisiones deben estar en el contexto. El modelo debe saber que está trabajando dentro de un sistema existente con principios ya establecidos, no diseñando desde cero.

**ADRs relevantes.** Los Architecture Decision Records de decisiones relacionadas con el problema actual. Si el equipo ya decidió que usa event sourcing para el dominio de pedidos, y ahora está diseñando el dominio de inventario, los ADRs de pedidos son contexto relevante.

**El problema específico.** La descripción precisa del problema de diseño que se está resolviendo: qué módulo, qué interacciones, qué restricciones locales, qué casos de uso debe satisfacer.

```
ESTRUCTURA DE CONTEXTO PARA SESIÓN DE DISEÑO

[PRINCIPIOS ARQUITECTÓNICOS DEL PROYECTO]
  - Arquitectura: microservicios con API Gateway
  - Comunicación: REST para sincrónico, eventos (Kafka) para asincrónico
  - Base de datos: una base por servicio, sin compartir esquemas
  - Lenguaje: Python 3.11+, FastAPI

[ADRs RELEVANTES]
  ADR-003: Decisión de usar Kafka para notificaciones
  ADR-007: Prohibición de dependencias directas entre servicios

[RESTRICCIONES NO FUNCIONALES]
  - Latencia máxima para checkout: 300ms P95
  - Disponibilidad requerida: 99.9%
  - Compliance: PCI-DSS para datos de pago

[PROBLEMA A DISEÑAR]
  Diseñar el servicio de reconciliación de pagos que debe:
  - Recibir eventos de pagos procesados
  - Verificar contra registros del banco
  - Emitir alertas para discrepancias
  - Generar reportes diarios
```

Con este contexto, el modelo puede razonar sobre el diseño del servicio respetando los principios y restricciones del sistema real, no un sistema hipotético.

### El arquitecto decide, el modelo asiste

Hay una diferencia cualitativa entre las fases de análisis y diseño en cuanto al rol del modelo. En análisis, el trabajo principal es de síntesis de información: el modelo puede procesar grandes volúmenes de texto y extraer patrones. En diseño, el trabajo principal es de evaluación y juicio: cuál alternativa es mejor para este equipo, este proyecto y esta organización.

La evaluación y el juicio requieren información que el modelo generalmente no tiene y no puede tener en el contexto: las capacidades reales del equipo, la deuda técnica acumulada, las restricciones políticas de la organización, la visión de largo plazo del producto, los compromisos con clientes específicos. El arquitecto tiene acceso a toda esa información. El modelo no.

El error de diseño más frecuente es tratar al modelo como árbitro de decisiones arquitectónicas. El flujo correcto es el inverso: el arquitecto formula la decisión que considera correcta, proporciona al modelo el contexto del problema y la decisión propuesta, y le pide que identifique riesgos, casos no considerados o alternativas que el arquitecto no evaluó. El arquitecto usa ese output como insumo para revisar su decisión, no como sustituto de ella.

### Generación de diagramas y documentación

Una de las aplicaciones más inmediatamente útiles de la IA en diseño es la asistencia en documentación. Los arquitectos suelen tener el diseño claro en su cabeza pero posterguen documentarlo porque es costoso en tiempo.

El modelo puede asistir en la traducción del diseño a distintos formatos de documentación:

- A partir de una descripción en lenguaje natural del diseño, generar la especificación en formato de diagrama (PlantUML, Mermaid, C4 model en texto)
- A partir de la discusión del equipo sobre una decisión, generar el borrador del ADR con la estructura estándar (contexto, decisión, consecuencias)
- A partir del diseño aprobado, generar la documentación de API en formato OpenAPI
- A partir de los diagramas de secuencia, generar los contratos entre servicios

En todos estos casos, el modelo trabaja con el contexto del diseño aprobado para producir artefactos de documentación que el arquitecto revisa y ajusta. El costo de documentación se reduce significativamente sin comprometer la calidad, porque el arquitecto evalúa el output antes de aprobarlo.

### Validación del diseño contra el análisis

Un uso de alto valor que suele pasarse por alto es la verificación de que el diseño propuesto cubre todos los requisitos del análisis. Con las especificaciones funcionales y el diseño propuesto en el contexto, el modelo puede identificar requisitos funcionales que no tienen un componente de diseño correspondiente, o componentes de diseño que no responden a ningún requisito documentado.

Este tipo de verificación es tedioso de hacer manualmente y fácil de omitir bajo presión de tiempo. La IA puede ejecutarlo sistemáticamente como un paso de validación antes de que el equipo avance a la generación de código.

### Nota del arquitecto

La trampa más sutil en el uso de IA para diseño arquitectónico es la de la coherencia superficial: el modelo puede generar diseños que parecen técnicamente sólidos pero que en realidad son compilaciones de patrones tomados de contextos diferentes. Un diseño que usa event sourcing para el módulo A, CQRS para el módulo B y una base de datos compartida para el módulo C puede parecerle coherente al modelo (cada patrón es válido en sí mismo) pero ser arquitectónicamente inconsistente para el sistema completo.

La verificación de coherencia arquitectónica global requiere el juicio del arquitecto, que conoce el sistema como un todo. El modelo puede identificar inconsistencias locales si el contexto de los principios globales está disponible, pero no puede sustituir la visión de conjunto que solo el arquitecto tiene.

La siguiente sección entra en la fase de generación de código — el corazón del capítulo desde la perspectiva del impacto inmediato — y analiza en profundidad cómo el contexto transforma la calidad del código generado.
