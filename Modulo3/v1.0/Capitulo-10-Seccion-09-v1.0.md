# Capítulo 10 — Planificación y Razonamiento

## Sección 09: Patrones y anti-patrones

El conocimiento de los patrones correctos tiene un valor limitado si no se acompaña del conocimiento de los patrones incorrectos y de por qué fallan. Esta sección documenta los anti-patrones más frecuentes en sistemas de planificación y razonamiento en producción, con el análisis de las condiciones que los generan y las decisiones de diseño que los evitan.

---

### Patrones que funcionan

#### Patrón P1: Razonamiento visible y auditable

El agente produce los pasos de razonamiento como texto explícito antes de producir el output final. Cada paso es un fragmento de texto independiente que puede revisarse y auditarse.

**Por qué funciona:** El razonamiento explícito reduce la tasa de errores porque el modelo "piensa en voz alta" antes de comprometerse con una respuesta. Los errores en el razonamiento son detectables antes de que lleguen al output final. El sistema de verificación puede revisar la cadena de razonamiento, no solo el output.

**Señal de éxito:** El equipo puede depurar un output incorrecto mirando el razonamiento y identificando exactamente en qué paso se introdujo el error.

---

#### Patrón P2: Verificación por tipo de output

El sistema aplica una estrategia de verificación específica al tipo de output que produce cada paso (código, texto, datos estructurados, plan).

**Por qué funciona:** Cada tipo de output tiene formas de fallo características y mecanismos de verificación apropiados. Un sistema de verificación genérico no puede detectar los errores específicos de cada tipo. La especialización por tipo incrementa la cobertura de detección de errores.

---

#### Patrón P3: Escalada explícita y predefinida

El sistema tiene definidas, en el diseño, las condiciones exactas bajo las cuales escala al operador humano: tipos de error, umbrales de confianza, categorías de decisión de alto riesgo.

**Por qué funciona:** Sin escalada explícita, los sistemas de planificación intentan resolver todo de forma autónoma, incluyendo situaciones para las que no están diseñados. La escalada predefinida convierte el fallo en un proceso gestionado en lugar de en una crisis.

---

#### Patrón P4: Límites de recursos explícitos

El sistema tiene configurados límites explícitos de iteraciones, llamadas al modelo, tiempo de ejecución y costo por tarea.

**Por qué funciona:** Previene que los sistemas entren en loops indefinidos, generen gastos inesperados o bloqueen recursos por tiempo ilimitado. Los límites son la red de seguridad que convierte un sistema potencialmente inestable en uno predeciblemente acotado.

---

### Anti-patrones que fallan

#### Anti-patrón AP1: El optimista de una sola llamada

**Descripción:** El sistema confía en que una sola llamada al modelo producirá un output de calidad suficiente para cualquier tarea, sin pasos de verificación ni reflexión.

**Por qué falla:** Para tareas simples, esto es correcto y eficiente. Para tareas complejas, el modelo omite pasos de razonamiento, produce respuestas incompletas y comete errores que una segunda llamada de verificación habría detectado. El sistema funciona bien en las demos (las demos suelen usar tareas simples y bien formadas) y falla en producción (donde las tareas son más complejas e impredecibles).

**Síntoma característico:** Alta tasa de fallos en producción que no aparecía en las pruebas. Los ingenieros no pueden reproducir el fallo porque en el entorno de prueba se usaron inputs más simples.

**Corrección:** Categorizar las tareas por complejidad y aplicar la arquitectura de razonamiento apropiada para cada categoría. No todas las tareas necesitan reflexión; pero las tareas complejas la necesitan.

---

#### Anti-patrón AP2: La reflexión infinita

**Descripción:** El sistema realiza múltiples iteraciones de reflexión sin un criterio de terminación claro, con la esperanza de que más iteraciones producirán un output mejor.

**Por qué falla:** La reflexión sin criterio de terminación produce tres problemas: (a) el sistema puede no converger, generando iteraciones indefinidamente sin mejorar el output; (b) más allá de 2-3 iteraciones, la reflexión frecuentemente empeora el output — el modelo se vuelve excesivamente cauteloso, añade calificaciones innecesarias o rompe la coherencia del texto; (c) el costo y la latencia crecen sin límite.

**Síntoma característico:** El sistema tarda mucho más de lo esperado en producir respuestas. Los outputs tienen calidad irregular: excelentes para algunas entradas, degradados para otras. El costo de la API es mucho mayor al estimado.

**Corrección:** Definir el criterio de convergencia antes de implementar la reflexión: qué característica del output indica que la reflexión ha sido suficiente. Si no se puede definir un criterio claro, limitar las iteraciones a un número fijo (generalmente 2) y aceptar ese output.

---

#### Anti-patrón AP3: El plan que no puede fallar

**Descripción:** El sistema genera un plan y lo ejecuta paso a paso sin ningún mecanismo de detección de fallo intermedio. Si un paso falla, el sistema intenta continuar con el siguiente paso usando un resultado incompleto o incorrecto.

**Por qué falla:** Los errores en pasos tempranos se propagan a través de todos los pasos siguientes. El output final puede ser totalmente incorrecto sin que ningún paso individualmente parezca haber fallado. El diagnóstico es extremadamente difícil porque el fallo visible (el output final) está desconectado de la causa (el paso que falló primero).

**Síntoma característico:** Outputs que son coherentes internamente pero incorrectos globalmente. El sistema no reporta ningún error pero el resultado es inutilizable.

**Corrección:** Añadir verificación del output de cada paso antes de pasarlo al siguiente. Definir el comportamiento cuando un paso falla: reintento, plan alternativo o escalada. Nunca pasar un resultado de fallo a un paso siguiente como si fuera un resultado exitoso.

---

#### Anti-patrón AP4: El agente sin herramientas que ejecuta herramientas

**Descripción:** El sistema planifica acciones que requieren herramientas no disponibles, o usa herramientas fuera del rango de inputs para los que fueron diseñadas, sin verificar la disponibilidad ni los límites antes de ejecutar.

**Por qué falla:** El modelo no sabe qué herramientas están disponibles a menos que se le informe explícitamente. Si el prompt de planificación no incluye el catálogo exacto de herramientas disponibles con su descripción de uso y límites, el modelo planificará usando herramientas que no existen o usando herramientas existentes de formas no soportadas. La ejecución fallará en tiempo de ejecución de formas que son difíciles de anticipar.

**Síntoma característico:** Altas tasas de error en la fase de ejecución. Los logs muestran llamadas a herramientas con parámetros inválidos, herramientas no encontradas, o timeouts inesperados.

**Corrección:** El prompt de planificación debe incluir siempre el catálogo completo de herramientas disponibles con sus inputs esperados, outputs producidos y limitaciones conocidas. La verificación de viabilidad del plan (sección 07) debe incluir verificar que cada herramienta del plan existe en el catálogo.

---

#### Anti-patrón AP5: La verificación circular

**Descripción:** El sistema usa el mismo modelo con el mismo prompt para generar el output y para verificarlo. El evaluador tiene exactamente los mismos puntos ciegos que el generador.

**Por qué falla:** Si el modelo cometió un error porque no conoce algo, o porque tiene un sesgo particular en un dominio, el mismo modelo con los mismos sesgos no detectará ese error al evaluarlo. La verificación circular da una falsa sensación de seguridad: el sistema reporta que el output fue verificado, pero la verificación no agregó ninguna garantía real.

**Síntoma característico:** El sistema reporta alta confianza en sus outputs, pero la tasa de errores en producción es más alta de lo esperado. Los errores que el sistema "verifica" y considera correctos son sistemáticamente del mismo tipo.

**Corrección:** Para verificación de calidad del output, usar un prompt de evaluación significativamente diferente al prompt de generación. Para verificación factual, usar una fuente de verdad externa. Para verificación de código, usar ejecución real. Para verificación de planes, usar validación mecánica del catálogo de herramientas.

---

### Tabla resumen

| Anti-patrón | Síntoma principal | Corrección clave |
|---|---|---|
| Optimista de una sola llamada | Fallos en producción no reproducibles en pruebas | Categorizar por complejidad |
| Reflexión infinita | Latencia alta, costo inesperado, output degradado | Criterio de convergencia + límite de iteraciones |
| Plan que no puede fallar | Output final incorrecto sin error visible | Verificación por paso |
| Agente sin herramientas | Errores de ejecución frecuentes | Catálogo de herramientas en el prompt de planificación |
| Verificación circular | Alta confianza reportada, alta tasa de error real | Evaluador independiente o verificación externa |

La siguiente sección aplica todos estos principios a un caso de estudio empresarial completo.
