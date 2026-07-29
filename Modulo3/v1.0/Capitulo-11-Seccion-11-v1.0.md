# Capítulo 11 — Context Engineering para Desarrollo de Software

## Sección 11: Laboratorio práctico

Este laboratorio tiene un objetivo preciso: demostrar, de manera ejecutable, que el contexto determina la calidad del diagnóstico asistido por IA. El ejercicio trabaja con un repositorio de ejemplo que contiene un bug real, y el estudiante construye el contexto mínimo necesario para que el modelo identifique correctamente el problema.

La elección del debugging como ejercicio del laboratorio es deliberada: es el caso de uso donde el impacto del contexto es más dramático y más fácil de medir objetivamente. Un diagnóstico correcto vs. uno incorrecto es verificable sin ambigüedad.

### Descripción del escenario

El repositorio de práctica contiene el backend simplificado de un sistema de procesamiento de pedidos. El sistema tiene el siguiente bug en producción:

> Pedidos con múltiples descuentos aplicados muestran totales incorrectos cuando el segundo descuento tiene un monto mínimo mayor al subtotal después de aplicar el primer descuento.

El sistema recibe el bug como un reporte de un cliente:

```
REPORTE: ORD-2024-0847
Fecha: hoy, 09:23 UTC
Descripción: El pedido ORD-2024-0847 muestra un total de $89.10 en la 
confirmación de compra, pero el cliente recibió un cargo de $99.00 en 
su tarjeta. Los descuentos aplicados: 10% por volumen + $5 de descuento 
por primera compra.
```

El test suite también reporta un fallo:

```
FAILED tests/orders/test_pricing.py::test_stacked_discounts_with_minimum
AssertionError: 
  Expected: Decimal('89.10')
  Got: Decimal('99.00')
  
  Input: order.subtotal = Decimal('110.00')
         discount_1: type='percentage', value=10    [sin mínimo]
         discount_2: type='fixed', value=Decimal('10.90') [mínimo: Decimal('95.00')]
```

### El ejercicio: construir el contexto mínimo

El objetivo del ejercicio no es encontrar el bug — es construir el contexto correcto para que el modelo lo encuentre. Esto requiere que el estudiante decida:

1. ¿Qué información del repositorio es relevante para este diagnóstico?
2. ¿Cómo estructurar esa información en el prompt?
3. ¿Qué está omitiendo que impide que el modelo llegue a la causa raíz?

**Paso 1: El intento sin contexto**

El estudiante formula el primer prompt solo con el reporte del cliente:

```
PROMPT (sin contexto):
Un cliente reporta que su pedido ORD-2024-0847 muestra un total de $89.10
en la confirmación pero recibió un cargo de $99.00. 
¿Cuál puede ser la causa?
```

El modelo responde con hipótesis genéricas: descuento no aplicado correctamente, error de redondeo, problema de sincronización entre el total de la confirmación y el cargo procesado, etc. Ninguna es específica al código del proyecto.

**Paso 2: Agregar el stack trace y el test fallido**

```
PROMPT (con stack trace y test):
El sistema de procesamiento de pedidos tiene el siguiente test fallido:

[FALLO DE TEST]
FAILED test_stacked_discounts_with_minimum
Expected: Decimal('89.10'), Got: Decimal('99.00')
Input: subtotal=$110.00, discount_1=10% sin mínimo, 
       discount_2=$10.90 fijo con mínimo $95.00

¿Cuál puede ser la causa?
```

El modelo puede inferir que el segundo descuento no se está aplicando — el total de $99.00 corresponde al subtotal después del primer descuento (10% de $110 = $99), sin el segundo. Pero no puede saber por qué: si es un bug de lógica de condición, un bug de orden de operaciones, o un bug de comparación de tipos.

**Paso 3: Agregar el código de la función**

```python
# CÓDIGO DE calculate_order_total (versión con el bug):

def calculate_order_total(
    order: Order,
    discount_rules: list[DiscountRule],
) -> Decimal:
    subtotal = sum(item.unit_price * item.quantity for item in order.items)
    total = subtotal
    
    for rule in discount_rules:
        if rule.min_order_amount and total < rule.min_order_amount:
            continue
        
        if rule.type == 'percentage':
            total -= total * (rule.value / Decimal('100'))
        elif rule.type == 'fixed':
            total = max(Decimal('0'), total - rule.value)
    
    return total
```

Con el código, el modelo puede identificar el bug: la condición `total < rule.min_order_amount` compara el total **después** de aplicar los descuentos anteriores, no el subtotal original. El segundo descuento tiene un mínimo de $95.00, y el total después del primer descuento es $99.00. La condición `$99 < $95` es False, así que el descuento se aplica. Espera — eso significa que sí se aplica. El modelo necesita verificar con los valores exactos.

**Paso 4: Agregar el historial de cambios recientes**

```
GIT LOG (últimos 5 commits en orders/services/pricing.py):
a3f91b2 feat: evaluate discounts against running total, not subtotal
b2e8d41 fix: correct decimal precision in percentage calculation  
c1d7f30 refactor: extract discount rule validation
d8e9a10 test: add integration tests for stacked discounts
e5b2f1a feat: add minimum order amount support for discount rules
```

El commit `a3f91b2` ("evaluate discounts against running total, not subtotal") es el cambio que introdujo el bug. El modelo puede ahora formular la hipótesis precisa: el cambio modificó la variable comparada en la condición del mínimo, de `subtotal` a `total` (el total acumulado después de descuentos anteriores). Esto puede hacer que un descuento que debería aplicar (el total original supera el mínimo) no aplique (el total reducido ya no supera el mínimo), o viceversa.

En el caso del reporte: el total después del 10% de descuento es $99.00, que supera el mínimo de $95.00. El descuento debería aplicarse. Pero el test dice que no se aplica. La hipótesis ahora es: ¿la comparación usa `<` cuando debería usar `<=`? ¿O hay un problema de tipo entre Decimal?

**Paso 5: Verificar la hipótesis**

El estudiante revisa el diff del commit `a3f91b2`:

```diff
- if rule.min_order_amount and subtotal < rule.min_order_amount:
+ if rule.min_order_amount and total < rule.min_order_amount:
```

El cambio es exactamente lo que el modelo predijo. Pero la hipótesis del bug es: el total después del primer descuento (10% de $110 = $99.00) es mayor que el mínimo ($95.00), entonces la condición `$99 < $95` es False, y el descuento debería aplicarse.

El estudiante ejecuta el test localmente con el código del commit anterior (revertiendo el cambio) y confirma que el test pasa. El bug es el cambio de `subtotal` a `total` en la condición del mínimo — no porque el cálculo sea incorrecto conceptualmente (evaluar contra el total corriente puede ser un comportamiento deseado en algunos sistemas), sino porque el cambio rompió el contrato documentado en los tests existentes y en el comportamiento que el cliente esperaba.

### La lección del ejercicio

El diagnóstico del bug requirió cuatro capas de contexto para ser completo y verificable:

| Contexto | Lo que agregó al diagnóstico |
|---|---|
| Reporte del cliente + test fallido | Síntoma y valores exactos del fallo |
| Código de la función | Candidatos de mecanismos del bug |
| Git log reciente | Identificación del commit que introdujo el cambio |
| Diff del commit | Verificación de la hipótesis exacta |

Sin ninguna de estas capas, el diagnóstico hubiera sido incompleto. Con cada capa adicional, el diagnóstico se volvió más preciso y más verificable.

### Extensión del laboratorio: el test de regresión

Como extensión, el estudiante escribe el test que habría detectado este bug antes del deployment:

```python
def test_stacked_discounts_uses_subtotal_for_minimum_check():
    """
    Verifica que el mínimo de un descuento se evalúa contra el subtotal
    original, no contra el total reducido por descuentos anteriores.
    
    Regresión para: commit a3f91b2, bug reportado en ORD-2024-0847
    """
    items = [OrderItemFactory(unit_price=Decimal('110.00'), quantity=1)]
    order = OrderFactory(items=items)
    
    # Primer descuento: 10% sin mínimo → total $99.00
    # Segundo descuento: $10.90 fijo con mínimo $95.00
    # El subtotal original ($110) supera el mínimo, por lo que debe aplicar.
    discount_rules = [
        DiscountRule(type='percentage', value=Decimal('10')),
        DiscountRule(
            type='fixed',
            value=Decimal('10.90'),
            min_order_amount=Decimal('95.00'),
        ),
    ]
    
    result = calculate_order_total(order, discount_rules)
    
    # $110 - 10% = $99.00; $99.00 - $10.90 = $88.10
    assert result == Decimal('88.10'), (
        f"Expected $88.10 but got ${result}. "
        "Check that min_order_amount is evaluated against original subtotal."
    )
```

Este test, agregado al commit de fix, habría prevenido regresiones futuras del mismo bug.

### Nota del arquitecto

El laboratorio ilustra un principio general: la construcción del contexto de diagnóstico no es una operación de un solo paso. Es un proceso iterativo donde cada capa de contexto agregada revela la capa siguiente que se necesita. El AI Engineer que diseña sistemas de debugging asistido debe diseñar flujos que faciliten esta construcción incremental, no solo flujos que entreguen todo el contexto posible de una vez.

La siguiente sección consolida las prácticas del capítulo en un checklist accionable para el AI Engineer.
