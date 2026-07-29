# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 05: Contexto para generación de código

Esta es la sección más crítica del capítulo. La generación de código es la aplicación de IA para desarrollo de software de mayor adopción actual, y también donde el impacto del Context Engineering es más inmediato y medible. Un experimento que cualquier desarrollador puede replicar en minutos demuestra el punto con claridad.

### El experimento del contexto

Tómese la siguiente tarea de generación de código:

> "Escribe una función que calcule el precio total de un pedido aplicando descuentos."

Esta misma tarea, enviada al mismo modelo, produce resultados radicalmente diferentes según el contexto que la acompaña.

**Caso 1: Sin contexto**

```python
# Output del modelo sin contexto adicional

def calcular_precio_total(items, descuento=0):
    """
    Calcula el precio total de un pedido aplicando un descuento.
    
    Args:
        items: lista de diccionarios con 'precio' y 'cantidad'
        descuento: porcentaje de descuento a aplicar (0-100)
    
    Returns:
        float: precio total con descuento aplicado
    """
    subtotal = sum(item['precio'] * item['cantidad'] for item in items)
    precio_final = subtotal * (1 - descuento / 100)
    return round(precio_final, 2)
```

El código es correcto en abstracto. Pero no sabe nada del proyecto: no usa las convenciones de naming, no usa las clases de dominio existentes, no maneja los tipos de descuento que el negocio tiene definidos, no lanza las excepciones que el proyecto usa, no incluye logging.

**Caso 2: Con contexto de módulo y convenciones**

```
CONTEXTO PROPORCIONADO:

Módulo: orders/services/pricing.py
Convenciones del proyecto:
  - Type hints obligatorios en todas las funciones
  - Docstrings en formato Google Style
  - Manejo de errores con excepciones custom de orders/exceptions.py
  - Logging con structlog

Clases disponibles en orders/models.py:
  class Order:
      items: list[OrderItem]
      customer_id: UUID
  class OrderItem:
      product_id: UUID
      quantity: int
      unit_price: Decimal
  class DiscountRule:
      type: Literal['percentage', 'fixed', 'buy_x_get_y']
      value: Decimal
      min_order_amount: Optional[Decimal]

Excepciones disponibles en orders/exceptions.py:
  class InvalidDiscountError(OrderError): ...
  class OrderCalculationError(OrderError): ...

Función de pricing existente como referencia:
  def calculate_tax(order: Order, tax_rate: Decimal) -> Decimal:
      # [código de la función existente]
```

Con este contexto, el output del modelo es sustancialmente diferente:

```python
# Output del modelo con contexto completo

import structlog
from decimal import Decimal
from orders.models import Order, DiscountRule
from orders.exceptions import InvalidDiscountError, OrderCalculationError

logger = structlog.get_logger(__name__)


def calculate_order_total(
    order: Order,
    discount_rules: list[DiscountRule],
) -> Decimal:
    """Calcula el precio total del pedido aplicando reglas de descuento.

    Args:
        order: Instancia del pedido con sus ítems.
        discount_rules: Lista de reglas de descuento a aplicar en orden.

    Returns:
        Precio total con todos los descuentos aplicados.

    Raises:
        InvalidDiscountError: Si alguna regla de descuento tiene valores inválidos.
        OrderCalculationError: Si el cálculo falla por datos inconsistentes.
    """
    logger.info("calculating_order_total", order_id=str(order.id))

    try:
        subtotal = sum(
            item.unit_price * item.quantity
            for item in order.items
        )
    except Exception as e:
        raise OrderCalculationError(
            f"Error calculando subtotal del pedido {order.id}"
        ) from e

    total = subtotal
    for rule in discount_rules:
        if rule.min_order_amount and subtotal < rule.min_order_amount:
            continue  # El pedido no alcanza el mínimo para este descuento

        if rule.type == 'percentage':
            if not (Decimal('0') <= rule.value <= Decimal('100')):
                raise InvalidDiscountError(
                    f"Porcentaje de descuento inválido: {rule.value}"
                )
            total -= total * (rule.value / Decimal('100'))

        elif rule.type == 'fixed':
            total = max(Decimal('0'), total - rule.value)

        else:
            raise InvalidDiscountError(
                f"Tipo de descuento no soportado: {rule.type}"
            )

    logger.info(
        "order_total_calculated",
        order_id=str(order.id),
        subtotal=str(subtotal),
        total=str(total),
    )
    return total
```

La diferencia no es cosmética. El segundo código es directamente integrable al proyecto. El primero requiere reescritura significativa.

### Los elementos del contexto para generación de código

El experimento anterior ilustra los cinco elementos de contexto que determinan la calidad del código generado:

**1. Ubicación en el repositorio.** El módulo, el paquete, el archivo donde se va a insertar el código. Esta información le dice al modelo el dominio, el nivel de abstracción y el propósito del código.

**2. Clases y tipos del dominio.** Las estructuras de datos del proyecto con las que el código debe trabajar. Sin esto, el modelo inventa sus propias estructuras que luego hay que integrar manualmente.

**3. Convenciones del proyecto.** Estilo de código, manejo de errores, logging, formato de documentación. Sin esto, el código generado es técnicamente correcto pero estilísticamente inconsistente, lo que genera fricción en la revisión de código.

**4. Funciones relacionadas existentes.** Las funciones que el código nuevo va a llamar o que lo llamarán. Sin esto, el modelo puede generar código que asume interfaces que no existen o que ignora funciones de utilidad que ya están disponibles.

**5. Tests existentes.** Los tests que el código debe pasar. Con tests en el contexto, el modelo puede generar código que directamente satisface esos tests, en lugar de código que el desarrollador luego debe ajustar para que los tests pasen.

### El rol de los tests como contexto

Este último elemento merece atención especial porque invierte la lógica habitual. En lugar de generar código y luego escribir tests, el workflow asistido por IA más productivo es:

1. El desarrollador escribe los tests primero (o tiene tests existentes para la función que está modificando).
2. Los tests se incluyen en el contexto del prompt de generación.
3. El modelo genera la implementación que satisface esos tests.
4. El desarrollador ejecuta los tests para verificar.

Este workflow — variante del Test-Driven Development — es especialmente efectivo con IA porque los tests son una especificación ejecutable precisa. El modelo no necesita inferir qué debe hacer la función: los tests se lo dicen.

```
WORKFLOW TDD-ASISTIDO POR IA

[PASO 1] Desarrollador escribe tests:
  def test_calculate_order_total_with_percentage_discount():
      order = Order(items=[OrderItem(unit_price=100, quantity=2)])
      rule = DiscountRule(type='percentage', value=10)
      result = calculate_order_total(order, [rule])
      assert result == Decimal('180.00')

  def test_calculate_order_total_skips_rule_below_minimum():
      order = Order(items=[OrderItem(unit_price=50, quantity=1)])
      rule = DiscountRule(type='percentage', value=20, min_order_amount=100)
      result = calculate_order_total(order, [rule])
      assert result == Decimal('50.00')  # Descuento no aplica

[PASO 2] Tests + contexto del módulo → modelo genera implementación

[PASO 3] Desarrollador ejecuta tests → verifica que pasan

[PASO 4] Desarrollador revisa el código → aprueba o ajusta
```

### Estrategias de selección de contexto para proyectos grandes

En proyectos grandes, incluir todo el código relacionado en el contexto no es práctico. El repositorio puede tener decenas de miles de archivos. La selección de contexto requiere estrategia.

**Selección manual guiada.** El desarrollador selecciona explícitamente los archivos relevantes: el módulo donde trabaja, las clases que va a usar, la función de referencia más similar a la que va a escribir. Herramientas como Cursor permiten hacer esta selección de forma visual.

**Recuperación automática por embeddings.** Un sistema de RAG indexa el repositorio por embeddings semánticos. Cuando el desarrollador formula la tarea, el sistema recupera automáticamente los fragmentos de código más similares semánticamente. Efectivo para repositorios grandes, pero requiere infraestructura de indexación.

**Archivos de contexto del proyecto.** Un archivo `CONTEXT.md` o `.claude/project.md` en el repositorio que documenta las convenciones, los patrones estándar del proyecto y las instrucciones para el asistente de IA. Este archivo, incluido automáticamente en cada sesión, establece el contexto base del proyecto sin necesidad de selección manual por tarea.

### Code review asistido por IA

La generación de código tiene un paso posterior que también se beneficia del Context Engineering: la revisión de código. Cuando un pull request incluye en el contexto el diff, las guías de estilo del proyecto, los requisitos que motivaron el cambio y el código de las funciones afectadas, el modelo puede hacer una revisión técnica más precisa que una revisión sin contexto.

El contexto para code review incluye:

- El diff completo del pull request
- El contexto de las funciones modificadas (no solo las líneas cambiadas)
- Los requisitos o issues que motivaron el cambio
- Las guías de estilo y convenciones del proyecto
- Los tests que se agregaron o modificaron

Con este contexto, el modelo puede identificar: casos borde no manejados, violaciones de convenciones del proyecto, inconsistencias con el diseño existente, riesgos de regresión en funciones relacionadas, y documentación faltante o incorrecta.

### Nota del arquitecto

El mayor riesgo en la generación de código asistida por IA no es que el modelo genere código incorrecto — eso lo detectan los tests y la revisión. El mayor riesgo es que el equipo adopte el código generado sin revisión crítica, confiando en que el modelo verificó su propia corrección. El modelo no puede verificar su propia corrección. Puede producir código que compila, que pasa los tests inmediatos y que aun así es incorrecto respecto a los requisitos de negocio que no estaban en el contexto.

El flujo de trabajo correcto siempre incluye: generación → verificación automática (tests, linter) → revisión humana → aprobación. La IA acelera la generación; el humano sigue siendo responsable de la corrección.

La siguiente sección analiza la fase de pruebas y aseguramiento de calidad: cómo el Context Engineering amplía la cobertura de tests y mejora la detección de defectos.
