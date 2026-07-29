# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 07: Contexto para depuración y mantenimiento

La depuración es la fase del ciclo de vida del software donde el Context Engineering tiene el mayor impacto en términos de tiempo ahorrado. Encontrar la causa raíz de un bug puede llevar horas o días cuando el desarrollador trabaja solo con su conocimiento del sistema y un stack trace. Con el contexto correcto, el modelo puede proponer hipótesis de causa raíz bien fundamentadas en minutos.

Pero el contexto correcto para debugging no es simplemente "el error que apareció". Es el conjunto de información que un desarrollador sénior experimentado necesitaría para analizar el problema: el stack trace completo, el código de las funciones implicadas, el historial de cambios recientes, los tests que fallan, el comportamiento observado versus el esperado.

### El problema del debugging sin contexto

El caso más común de debugging mal asistido por IA es este: el desarrollador pega el stack trace en el chat del modelo y pregunta "¿qué está fallando?". El modelo lee el stack trace y genera una explicación del tipo de error — "parece un NullPointerException en la línea X" — que no agrega información que el desarrollador no tenía ya.

La razón es que el stack trace solo describe el síntoma, no la causa. El modelo no puede inferir la causa sin el contexto del código que generó ese error, el estado del sistema cuando ocurrió y los cambios recientes que podrían haberlo introducido.

El debugging asistido por IA es valioso cuando el contexto incluye todo lo que un desarrollador sénior necesitaría para diagnosticar el problema.

### El contexto de diagnóstico completo

El contexto para debugging efectivo tiene seis componentes:

**El error observado.** No solo el mensaje de error, sino la descripción del comportamiento observado versus el esperado. "La función devuelve None cuando debería devolver el objeto Order" es más útil que "Error en pricing.py línea 47".

**El stack trace completo.** No el stack trace truncado que aparece en los logs de producción, sino el completo, con todos los frames, valores de variables locales si están disponibles, y el contexto de ejecución (request ID, usuario, timestamp).

**El código de las funciones implicadas.** Las funciones que aparecen en el stack trace, completas. No solo las líneas mencionadas en el trace, sino el código completo de cada función para que el modelo pueda razonar sobre el flujo de control.

**El historial de cambios recientes.** El output de `git log --oneline -20` y el diff de los cambios más recientes en los módulos afectados. Si el bug apareció después de un deploy específico, el diff de ese deploy es contexto crítico.

**Los tests que fallan.** Si el bug triggerea fallos en el test suite, los tests fallidos con su output completo son contexto adicional que describe el comportamiento incorrecto de manera ejecutable.

**La configuración del entorno.** Variables de entorno, versiones de dependencias, configuración de base de datos — especialmente si el bug se manifiesta en producción pero no en desarrollo.

### Construcción del contexto de diagnóstico: ejemplo práctico

Supóngase que el sistema de cálculo de precios comienza a devolver totales incorrectos en producción. El desarrollador construye el siguiente contexto:

```
CONTEXTO DE DIAGNÓSTICO:

[COMPORTAMIENTO OBSERVADO]
Desde las 14:35 UTC de hoy, algunos pedidos con descuentos de tipo 'fixed'
muestran totales negativos en la UI. El log de pagos muestra que se están
procesando como $0.00 en lugar del valor negativo (hay validación en el
servicio de pagos), pero el frontend muestra el valor incorrecto.

[STACK TRACE]
File "orders/services/pricing.py", line 89, in calculate_order_total
  total = max(Decimal('0'), total - rule.value)
- total: Decimal('-15.00')
- rule.value: Decimal('65.00')
- subtotal antes de descuento: Decimal('50.00')

[CÓDIGO DE LAS FUNCIONES IMPLICADAS]
# [código completo de calculate_order_total]
# [código de la función que llama a calculate_order_total]

[CAMBIOS RECIENTES - git log]
a3f91b2 feat: add free shipping promotion (hace 3 horas) - María García
b2e8d41 fix: correct tax rounding in checkout (hace 6 horas) - Juan López
c1d7f30 refactor: extract discount validation (hace 1 día) - Ana Martínez

[DIFF DEL COMMIT a3f91b2]
# [diff completo del commit de la promoción de envío gratis]

[TEST QUE FALLA]
FAILED tests/orders/test_pricing.py::test_fixed_discount_with_minimum_amount
AssertionError: assert Decimal('-15.00') == Decimal('35.00')
```

Con este contexto, el modelo puede razonar sobre la causa raíz con precisión: el commit de la promoción de envío gratis (a3f91b2) probablemente modificó el orden en que se aplican las reglas de descuento, o agregó una regla de tipo 'fixed' para el envío gratis con un valor que supera el subtotal del pedido, produciendo totales negativos para pedidos pequeños que tienen ese descuento.

Sin el contexto del diff reciente y la descripción del comportamiento observado, la misma pregunta produciría solo una explicación genérica del código de la función, que el desarrollador ya conoce.

### Debugging de sistemas distribuidos

Los sistemas distribuidos presentan un desafío adicional para el debugging: el error puede manifestarse en un servicio pero originarse en otro. El stack trace de un servicio no revela lo que ocurrió en los servicios upstream que lo llamaron.

El Context Engineering para debugging distribuido agrega al contexto estándar:

- Los logs del servicio upstream en el rango de tiempo del error (con correlation IDs para vincular las trazas)
- El contrato de la API entre los servicios (para verificar si el servicio upstream cumplió su contrato)
- El historial de cambios recientes en los servicios relacionados

Los sistemas de observabilidad modernos (Datadog, Grafana, OpenTelemetry) permiten recuperar este contexto de manera relativamente automatizada cuando están bien configurados. El AI Engineer puede diseñar herramientas que, dado un correlation ID de un error, recuperan automáticamente todos los logs relacionados de los servicios implicados y los ensamblan como contexto para el modelo.

### Mantenimiento: contexto para cambios en sistemas legados

El mantenimiento de sistemas existentes — en particular sistemas legados con documentación escasa o desactualizada — es uno de los casos de uso donde el Context Engineering para IA tiene mayor valor potencial y mayor riesgo.

El valor potencial: el modelo puede analizar código que el desarrollador actual no escribió y que no está documentado, y proporcionar un entendimiento de su lógica a partir del código mismo.

El riesgo: el modelo puede generar explicaciones plausibles del comportamiento de código legado que son incorrectas porque la lógica real depende de efectos colaterales, estado global o convenciones no documentadas que el modelo no puede inferir del código solo.

El contexto correcto para trabajo en código legado incluye:

- El código del módulo a modificar, completo
- Cualquier documentación existente, aunque esté desactualizada (la diferencia entre la documentación y el código real es información en sí misma)
- Los tests existentes (si los hay)
- El historial de commits del módulo (puede revelar la intención original)
- Los issues y PRs relacionados con ese módulo (pueden documentar decisiones que nunca llegaron al código)

Y, fundamentalmente, una advertencia explícita al modelo sobre el contexto: "Este es código legado. Puede tener comportamientos no documentados. Las hipótesis que generes sobre su funcionamiento deben considerarse preliminares hasta verificación."

### Automatización del contexto de diagnóstico

Para equipos con alta frecuencia de bugs o sistemas complejos, el proceso de construcción del contexto de diagnóstico puede automatizarse parcialmente. Un script que, dado un error en los logs de producción:

1. Recupera el stack trace completo con valores de variables
2. Identifica los archivos de código mencionados en el trace y los recupera del repositorio
3. Ejecuta `git log --oneline -10` en esos archivos para identificar cambios recientes
4. Recupera los tests del módulo afectado
5. Ensambla todo en un prompt de diagnóstico estructurado

Esta automatización no reemplaza el juicio del desarrollador en la evaluación del diagnóstico, pero reduce significativamente el tiempo de preparación del contexto.

### Nota del arquitecto

El debugging asistido por IA, bien implementado, reduce el tiempo de diagnóstico. Pero introduce un riesgo sutil: el modelo puede proponer hipótesis de causa raíz convincentes pero incorrectas, especialmente cuando el stack trace y el código disponible son ambiguos. La hipótesis convincente puede llevar al desarrollador a explorar una dirección incorrecta antes de verificarla.

El contrapeso es la verificación explícita antes de actuar: toda hipótesis de causa raíz generada por el modelo debe verificarse con un test o una reproducción local antes de aplicar el fix. El modelo propone; el desarrollador verifica y decide.

La siguiente sección sale del código en sí mismo para analizar el ecosistema donde ese código vive: los IDEs, repositorios y pipelines de CI/CD, y cómo el Context Engineering opera en esos entornos.
