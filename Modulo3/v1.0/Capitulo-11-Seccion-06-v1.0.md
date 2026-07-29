# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 06: Contexto para pruebas y aseguramiento de calidad

Las pruebas son el mecanismo principal de verificación de que el software hace lo que se supone que debe hacer. También son, en muchos equipos, el artefacto más costoso de producir en relación a su impacto: escribir buenos casos de prueba requiere una comprensión profunda de los requisitos, del código bajo prueba y de los escenarios de falla posibles.

La IA puede asistir de manera significativa en esta fase — pero, como en las anteriores, la calidad de la asistencia depende del contexto disponible. Esta sección analiza cómo construir ese contexto.

### Los tres problemas que la IA resuelve en testing

**Cobertura incompleta.** Los desarrolladores tienden a escribir tests para el caso feliz y los casos de error obvios. Los casos borde — condiciones límite, combinaciones inusuales de parámetros, comportamientos de sistema bajo carga — frecuentemente no tienen tests porque requieren esfuerzo adicional para identificarlos. El modelo, dado el código de la función y su especificación, puede generar sistemáticamente casos borde que el desarrollador no consideró.

**Eficiencia de escritura.** Escribir tests bien estructurados — con setup, assertions claras, nombres descriptivos — es trabajo repetitivo. El modelo puede generar la estructura de los tests a partir de los casos de prueba que el desarrollador identifica, reduciendo el tiempo de escritura.

**Revisión de tests existentes.** Los tests antiguos pueden ser obsoletos (verifican comportamientos que ya cambiaron), redundantes (múltiples tests verifican lo mismo) o incompletos (no verifican el comportamiento actual de la función). El modelo puede revisar un conjunto de tests y señalar estos problemas cuando tiene el contexto del código actual y la especificación vigente.

### El contexto para generación de tests

El contexto para la generación de tests de calidad tiene cinco componentes:

**La función o módulo bajo prueba.** El código que se quiere testear, completo. Esto es obvio, pero frecuentemente los desarrolladores proporcionan solo la firma de la función y esperan que el modelo infiera el comportamiento. El modelo genera mejores tests cuando puede analizar la implementación real.

**La especificación funcional.** Los requisitos o user stories que definen qué debe hacer el código. Sin esto, el modelo solo puede generar tests que verifican la implementación actual, no tests que verifican que la implementación cumple los requisitos. La diferencia es crítica: un test que verifica la implementación siempre pasa (valida lo que el código hace), pero puede no detectar un bug donde el código hace algo diferente a lo especificado.

**Los tests existentes del módulo.** Para no duplicar cobertura y para mantener el estilo y las convenciones de testing del proyecto. Si el proyecto usa fixtures de pytest de cierta manera, los nuevos tests deben seguir el mismo patrón.

**Las dependencias y sus mocks.** Si la función usa base de datos, APIs externas u otros servicios, el modelo necesita saber cómo esas dependencias están mockeadas en el proyecto, o sugerirá mocks que son incompatibles con la infraestructura de testing existente.

**Criterios de aceptación explícitos.** Los casos de prueba que el equipo ya identificó como obligatorios. El modelo los incluye en los tests generados y agrega casos adicionales para completar la cobertura.

### Ejemplo: generación de tests con contexto completo

```
CONTEXTO PARA GENERACIÓN DE TESTS:

[FUNCIÓN BAJO PRUEBA]
def calculate_order_total(
    order: Order,
    discount_rules: list[DiscountRule],
) -> Decimal:
    # [implementación completa]

[ESPECIFICACIÓN FUNCIONAL]
- El total debe calcularse como la suma de (precio_unitario * cantidad)
  para todos los ítems del pedido.
- Las reglas de descuento se aplican en el orden en que se proveen.
- Si el subtotal no alcanza el monto mínimo de una regla, esa regla
  se omite sin error.
- Los descuentos de tipo 'percentage' reducen el total en ese porcentaje.
- Los descuentos de tipo 'fixed' reducen el total en esa cantidad fija,
  con un piso de 0 (el total no puede ser negativo).
- Si el valor de un descuento percentage está fuera del rango [0, 100],
  debe lanzarse InvalidDiscountError.

[TESTS EXISTENTES DEL MÓDULO]
# [contenido de tests/orders/test_pricing.py existente]

[MOCKS DISPONIBLES]
# El proyecto usa pytest-mock y factory_boy para fixtures
# Ver conftest.py para las factories de Order y OrderItem

TAREA: Genera tests que cubran los casos borde de la función,
       además de los casos especificados. Usa el estilo del
       proyecto (factory_boy para fixtures, pytest para assertions).
```

Con este contexto, el modelo genera tests que cubren: pedido vacío, un solo ítem, múltiples ítems, descuento no aplicable por monto mínimo, múltiples descuentos apilados, descuento que llevaría el total a negativo, y valores inválidos de descuento — casos que el desarrollador podría haber pasado por alto.

### Testing de propiedades y mutación

Un uso avanzado de IA en testing que el Context Engineering habilita es la generación de property-based tests y la sugerencia de operadores de mutación para evaluación de la calidad del test suite.

Los property-based tests, a diferencia de los tests de ejemplo, verifican propiedades generales del código para un espacio amplio de entradas generadas automáticamente. Son especialmente útiles para funciones matemáticas o de transformación de datos.

El modelo puede sugerir propiedades relevantes para una función dada su especificación:

```
PROPIEDAD 1: El total con descuento siempre es <= al subtotal sin descuento.
PROPIEDAD 2: Si el descuento es 0%, el total es igual al subtotal.
PROPIEDAD 3: Aplicar dos reglas de descuento en orden diferente puede
             producir totales diferentes (el orden importa).
PROPIEDAD 4: El total nunca es negativo, incluso con descuentos fixed grandes.
```

Estas propiedades, identificadas por el modelo a partir de la especificación, se convierten en tests de Hypothesis (Python) o QuickCheck (Haskell/Scala) que el desarrollador configura para exploración automática.

### IA para revisión de pull requests

La revisión de pull requests es una de las aplicaciones de mayor impacto empresarial de la IA en QA, y está directamente relacionada con el Context Engineering. El valor de una revisión automática depende casi completamente de la calidad del contexto disponible.

Una revisión con contexto mínimo (solo el diff) puede identificar: problemas de sintaxis, violaciones de linting, variables no usadas. Útil, pero replicable por herramientas estáticas existentes.

Una revisión con contexto completo puede identificar: casos borde no cubiertos por los nuevos tests, inconsistencias con las guías de diseño del proyecto, regresiones potenciales en funciones que llaman al código modificado, violaciones de invariantes de negocio documentados en la especificación, y documentación faltante o incorrecta.

```
CONTEXTO PARA REVISIÓN DE PULL REQUEST:

[DIFF DEL PR]
# [contenido del git diff]

[CONTEXTO DE FUNCIONES AFECTADAS]
# [código completo de las funciones modificadas y las que las llaman]

[REQUISITOS QUE MOTIVARON EL CAMBIO]
# Issue #342: El cálculo de descuentos no respeta el monto mínimo

[GUÍAS DE ESTILO DEL PROYECTO]
# [extracto del documento de convenciones]

[TESTS DEL MÓDULO AFECTADO]
# [tests existentes y nuevos tests del PR]

TAREA: Revisa el PR con foco en:
1. ¿Los nuevos tests cubren los casos de la issue #342?
2. ¿Hay casos borde de la especificación sin test?
3. ¿El código sigue las convenciones del proyecto?
4. ¿Hay riesgos de regresión en el código que usa esta función?
```

### Testing no funcional

La IA también puede asistir en la generación de tests de performance, seguridad y resiliencia cuando el contexto incluye las restricciones no funcionales del sistema.

Por ejemplo, con los requisitos de latencia del sistema (P95 < 300ms para checkout), el modelo puede generar scripts de carga usando k6 o Locust que simulan la carga esperada y verifican que el sistema cumple esas restricciones. Sin las restricciones no funcionales en el contexto, el modelo generaría scripts de carga genéricos que no corresponden a los objetivos reales del sistema.

### Nota del arquitecto

Un error frecuente al implementar IA para generación de tests es confundir cobertura de líneas con calidad de tests. El modelo puede generar tests que aumentan la métrica de cobertura sin agregar valor real de verificación — por ejemplo, tests que llaman a una función y solo verifican que no lanza excepciones, sin verificar el output. El ingeniero de QA debe evaluar la calidad de los tests generados, no solo su cantidad.

La métrica correcta no es "cuántos tests generó el modelo" sino "cuántos bugs adicionales detectarían estos tests que los tests anteriores no detectaban". Esa evaluación requiere juicio humano.

La siguiente sección aborda la fase de depuración y mantenimiento: cómo construir el contexto de diagnóstico para que la IA asista en la identificación de causas raíz de manera efectiva.
