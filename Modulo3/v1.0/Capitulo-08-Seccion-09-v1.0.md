# Módulo 3 — Context Engineering

# Capítulo 08 — Agentes de IA: Arquitectura y Orquestación

## Sección 09 — Patrones y anti-patrones de agentes

> *"Los anti-patrones no son errores de programadores inexpertos. Son errores de diseño que aparecen cuando la complejidad del sistema supera el modelo mental del equipo que lo construye."*

---

## Objetivos de aprendizaje

- Identificar los patrones de diseño que producen agentes robustos y mantenibles en producción.
- Reconocer los anti-patrones más frecuentes en sistemas de agentes y entender por qué surgen.
- Aplicar criterios concretos para evaluar si el diseño de un agente es sostenible a escala.
- Distinguir los fallos de diseño de los fallos de implementación.

---

## Patrones que funcionan

### Patrón: Herramientas atómicas

Las herramientas del agente deben hacer una sola cosa y hacerla bien. Una herramienta atómica tiene un input claro, un output predecible y no produce efectos secundarios fuera de su función declarada.

```
# Herramienta no atómica (problemática):
procesar_pedido(pedido_id) → busca el pedido, verifica stock, reserva inventario,
                              genera factura y envía email de confirmación

# Herramientas atómicas (preferible):
obtener_pedido(pedido_id) → devuelve los datos del pedido
verificar_stock(producto_id, cantidad) → devuelve disponibilidad
reservar_inventario(producto_id, cantidad, pedido_id) → realiza la reserva
generar_factura(pedido_id) → crea la factura
enviar_confirmacion(pedido_id, email) → envía el correo
```

Las herramientas atómicas permiten al agente construir flujos complejos combinando operaciones simples. Si algo falla, el fallo está localizado en una herramienta específica y es fácil de diagnosticar. Las herramientas monolíticas producen fallos difíciles de aislar y no pueden reutilizarse en otros contextos.

### Patrón: Verificación antes de acción irreversible

Antes de ejecutar cualquier acción que no pueda deshacerse, el agente debe verificar explícitamente que tiene la información correcta y que la acción es la adecuada.

```
Thought: Voy a eliminar el registro CLI-0892 de la base de datos. Antes de proceder,
verifico: el objetivo del usuario fue "eliminar el cliente Alfa de la base". CLI-0892
corresponde a "Distribuidora Meridional S.A.", no a "Alfa". Hay una discrepancia.
No ejecutaré la eliminación. Solicitaré clarificación.
```

Este patrón requiere que el razonamiento del agente incluya explícitamente una etapa de verificación antes de acciones sensibles, y que el system prompt del agente establezca esta expectativa claramente.

### Patrón: Terminación explícita

El agente debe generar explícitamente una declaración de terminación cuando considera que el objetivo está cumplido, en lugar de simplemente dejar de proponer acciones.

```
# Terminación implícita (ambigua):
Thought: Creo que ya respondí la pregunta.
[El agente genera texto sin invocar herramientas — la orquestación asume que terminó]

# Terminación explícita (preferible):
Thought: He completado los tres pasos del objetivo: identifiqué al cliente (CLI-0892),
verifiqué su elegibilidad para la promoción (elegible, segmento Premium) y redacté el
correo. El objetivo está cumplido.
Action: finalizar_tarea(estado="exitoso", resumen="Cliente CLI-0892 identificado y
correo de fidelización redactado.")
```

La terminación explícita produce sistemas más predecibles y más fáciles de depurar. La orquestación puede detectar la señal de terminación con certeza en lugar de inferirla.

### Patrón: Fallback con información parcial

Cuando el agente no puede completar el objetivo, debe reportar cuánto avanzó antes del obstáculo, no simplemente fallar.

```
No se pudo completar el análisis de ventas porque el sistema CRM reportó un error
de autenticación en la iteración 3. En ese punto ya se habían procesado los datos
de enero y febrero (adjuntos). El análisis de marzo, abril y mayo no pudo completarse.
Opciones para continuar: (1) reintentar en 30 minutos, (2) proveer las credenciales
actualizadas del CRM, (3) continuar con los datos disponibles de enero y febrero.
```

---

## Anti-patrones frecuentes

### Anti-patrón: El agente todo-en-uno

Diseñar un agente que intenta manejar todos los casos de uso posibles de una aplicación en un único agente con docenas de herramientas. El resultado es un sistema con un prompt excesivamente largo, un catálogo de herramientas que el LLM no puede gestionar eficientemente y un comportamiento impredecible.

**Por qué surge:** Parece más simple tener un solo agente que manejar múltiples agentes especializados. El problema aparece a escala.

**Consecuencias:** El LLM toma decisiones de herramienta incorrectas, el contexto se agota antes de completar tareas complejas, y depurar fallos requiere analizar un sistema de gran complejidad.

**Solución:** Agentes especializados para dominios o tipos de tarea distintos, coordinados por un agente orquestador ligero. Este patrón se desarrolla en el capítulo 09.

---

### Anti-patrón: Confianza ciega en el output de herramientas

El agente asume que el output de una herramienta es siempre correcto y completo, sin validación. Si la herramienta devuelve datos inconsistentes o parciales, el agente los incorpora al razonamiento sin cuestionar.

**Ejemplo:** Una herramienta de búsqueda devuelve `[]` (lista vacía). El agente razona "no hay resultados" y concluye que el cliente no tiene pedidos. En realidad, la herramienta falló silenciosamente porque la conexión a la base de datos se perdió.

**Consecuencias:** Respuestas incorrectas presentadas con confianza, sin indicación de que el resultado podría estar basado en datos incompletos.

**Solución:** Las herramientas deben distinguir explícitamente entre "no hay resultados" y "ocurrió un error". La orquestación debe validar que el output es coherente antes de pasarlo al agente.

---

### Anti-patrón: El agente que improvisa herramientas

El agente intenta usar herramientas con parámetros o en combinaciones que no fueron diseñadas para ese uso, porque el LLM "razona" que puede funcionar.

**Ejemplo:** El agente necesita calcular un promedio de ventas. No tiene una herramienta de cálculo, pero tiene acceso a una herramienta de búsqueda SQL. Genera una consulta SQL ad hoc sin conocer el esquema exacto de la base de datos.

**Consecuencias:** La herramienta puede fallar, devolver resultados incorrectos, o en casos extremos, ejecutar operaciones no previstas.

**Solución:** El catálogo de herramientas debe cubrir las operaciones que el agente necesita. Si el agente improvisa sistemáticamente, el catálogo está incompleto. El system prompt debe incluir instrucciones explícitas sobre qué hacer cuando no existe la herramienta adecuada (declarar limitación, no improvisar).

---

### Anti-patrón: Contexto sin gestión

El agente acumula todo el historial de iteraciones en el contexto sin ninguna estrategia de compresión o selección. En tareas largas, el contexto excede la ventana del modelo, se producen truncaciones silenciosas, o el costo por iteración se vuelve prohibitivo.

**Consecuencias:** Degradación del razonamiento (el LLM "olvida" información de iteraciones tempranas), fallos por exceso de tokens, o costos de inferencia que no escalan.

**Solución:** Implementar la estrategia de gestión de contexto diseñada en la sección 06: resúmenes progresivos del historial, estado estructurado separado del historial completo, puntos de guardado intermedios.

---

### Anti-patrón: Herramientas con efectos secundarios ocultos

Una herramienta que parece de solo lectura en realidad modifica el estado de un sistema externo como efecto secundario. El agente llama a esa herramienta múltiples veces sin saber que cada llamada tiene consecuencias.

**Ejemplo:** `obtener_estado_pedido(pedido_id)` — parece una herramienta de lectura. En realidad, cada llamada registra un evento de "consulta" en el sistema de auditoría y puede disparar notificaciones automáticas si el estado es "pendiente de confirmación".

**Consecuencias:** El agente invoca la herramienta en múltiples iteraciones de diagnóstico sin saber que está generando efectos no deseados en el sistema externo.

**Solución:** Las herramientas deben documentar todos sus efectos, incluyendo efectos secundarios. Las herramientas de solo lectura deben serlo realmente. Si un efecto secundario es inevitable, debe documentarse explícitamente en la descripción de la herramienta.

---

## Nota del Arquitecto

> La mayoría de los anti-patrones no aparecen en la primera versión del agente. Aparecen cuando el sistema escala: más usuarios, más tipos de tarea, más herramientas, más casos borde. El momento de anticiparlos es en el diseño, no cuando ya están en producción. Una revisión estructurada del diseño usando esta lista de anti-patrones como checklist, antes del primer despliegue, evita la mayoría de los problemas costosos.

---

## Ideas clave

- Los patrones de agentes robustos comparten tres características: herramientas atómicas, verificación antes de acciones irreversibles, y terminación explícita.
- Los anti-patrones más frecuentes son: el agente todo-en-uno (difícil de escalar), la confianza ciega en herramientas (produce errores silenciosos), la improvisación de herramientas (usa herramientas fuera de su diseño), el contexto sin gestión (degrada el razonamiento), y los efectos secundarios ocultos (produce consecuencias no previstas).
- Los anti-patrones surgen generalmente a escala, no en el prototipo inicial. El diseño debe anticiparlos.
- Un agente que falla gracefully, con información parcial y opciones de recuperación, es más valioso en producción que uno que falla silenciosamente.

---

## Transición hacia la siguiente sección

Los patrones y anti-patrones son conocimiento abstracto hasta que se aplican a un caso real. La siguiente sección presenta un caso de estudio empresarial completo que integra todos los conceptos de este capítulo en una implementación de principio a fin.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
