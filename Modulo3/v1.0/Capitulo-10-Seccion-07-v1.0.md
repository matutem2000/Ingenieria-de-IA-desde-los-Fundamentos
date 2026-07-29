# Capítulo 10 — Planificación y Razonamiento

## Sección 07: Verificación y corrección de resultados

La reflexión, como se examinó en la sección anterior, es un mecanismo de autoevaluación que tiene límites estructurales: el mismo sistema que generó el resultado es el que lo evalúa. Para resultados donde la corrección importa — código que debe ejecutarse, respuestas que serán citadas como fuente de verdad, planes que guiarán decisiones de negocio — la verificación debe involucrar mecanismos externos al modelo.

La verificación externa no reemplaza la reflexión; la complementa. La reflexión mejora la coherencia y la completitud. La verificación externa garantiza la corrección en dimensiones que el modelo no puede verificar por sí mismo.

### Taxonomía de estrategias de verificación

La estrategia de verificación correcta depende del tipo de output. Un enfoque único no funciona para todos los casos. A continuación se presentan las estrategias principales organizadas por tipo de output.

---

#### Tipo 1: Código y outputs computacionales

**El problema:** Un modelo puede generar código que parece sintácticamente correcto, pero que falla en ejecución, produce resultados incorrectos o no maneja casos borde.

**Estrategia de verificación:**

```
NIVEL 1 — VERIFICACIÓN SINTÁCTICA
  Pasar el código por un linter o parser del lenguaje objetivo.
  Costo: negligible. Detecta: errores de sintaxis.
  No detecta: errores lógicos, casos borde.

NIVEL 2 — VERIFICACIÓN DE EJECUCIÓN
  Ejecutar el código en un sandbox aislado.
  Verificar que termina sin excepción con un input de prueba básico.
  Costo: bajo. Detecta: errores de runtime obvios.
  No detecta: resultados incorrectos, casos borde específicos.

NIVEL 3 — VERIFICACIÓN CON TESTS
  Ejecutar el código contra una suite de tests unitarios predefinida.
  Costo: medio. Detecta: errores lógicos para los casos testeados.
  No detecta: casos fuera de la suite de tests.

NIVEL 4 — VERIFICACIÓN POR ANÁLISIS
  Usar otro LLM con un prompt de revisión de código para identificar
  problemas que los tests no cubren.
  Costo: alto. Detecta: problemas de diseño, patrones de error comunes.
  No detecta: errores factuales, problemas de dominio muy específicos.
```

**Ejemplo de flujo:**

Un agente genera una función Python para calcular el interés compuesto de un préstamo. El sistema de verificación:

1. Pasa el código por `pyflakes` (nivel 1): sin errores de sintaxis.
2. Ejecuta la función con un input conocido — 10.000 de capital, 5% de tasa, 3 años — y compara el resultado contra el valor calculado manualmente (nivel 2): el resultado es correcto.
3. Ejecuta los tests unitarios que incluyen casos con tasa 0%, periodos = 1, capital negativo (nivel 3): la función falla con capital negativo — no valida el input.
4. El sistema retroalimenta el error al agente para que corrija la función.

---

#### Tipo 2: Respuestas factuales con fuente de verdad disponible

**El problema:** Un modelo puede afirmar datos que son incorrectos, desactualizados o fabricados (alucinación), incluso con aparente confianza.

**Estrategia de verificación:**

La verificación factual requiere una fuente de verdad externa. Si esa fuente existe, el proceso es:

```
1. El agente genera la respuesta.
2. El sistema extrae las afirmaciones verificables de la respuesta
   (puede ser una segunda llamada al modelo: "extrae todas las afirmaciones
   de hechos específicos de este texto").
3. Para cada afirmación, el sistema busca evidencia en la fuente de verdad
   (base de datos, documentos RAG, API de datos).
4. Las afirmaciones con evidencia se marcan como verificadas.
5. Las afirmaciones sin evidencia se marcan como no verificadas.
6. La respuesta final incluye solo afirmaciones verificadas, o incluye
   las no verificadas con una indicación explícita de que no fueron verificadas.
```

**Cuándo no se puede verificar factualmente:** Si no existe una fuente de verdad accesible, la verificación factual no es posible mediante este mecanismo. En ese caso, la estrategia es limitar el alcance de las afirmaciones del modelo: instruir al sistema para que solo afirme lo que puede soportar con citas de los documentos del contexto, y que marque explícitamente como "no verificado" cualquier conocimiento que proviene de los pesos del modelo.

---

#### Tipo 3: Planes de acción y workflows

**El problema:** Un plan generado por el modelo puede ser estructuralmente correcto pero incluir pasos que no son ejecutables — porque la herramienta requerida no está disponible, porque los permisos necesarios no existen, o porque el output de un paso no es compatible con el input que espera el siguiente paso.

**Estrategia de verificación:**

```
VERIFICACIÓN DE VIABILIDAD
  Para cada paso del plan:
  - ¿La herramienta requerida está disponible en el sistema?
  - ¿El agente tiene los permisos necesarios para usar esa herramienta?
  - ¿El formato del output del paso anterior es compatible con
    el formato de input que espera este paso?

VERIFICACIÓN DE COMPLETITUD
  - ¿El plan cubre todos los requisitos de la tarea?
  - ¿Hay pasos de verificación después de acciones críticas?
  - ¿Hay un mecanismo de rollback si un paso falla?

VERIFICACIÓN DE COHERENCIA
  - ¿El plan termina en un estado que satisface la tarea?
  - ¿Hay dependencias cíclicas entre pasos?
  - ¿El orden de los pasos es correcto (no se usa output antes de generarlo)?
```

Esta verificación puede hacerse de forma parcialmente automatizada (verificación de herramientas disponibles mediante lookup en un registro de herramientas) y de forma asistida por LLM (verificación de coherencia y completitud mediante una llamada de revisión).

---

#### Tipo 4: Outputs estructurados (JSON, XML, tablas)

**El problema:** El modelo puede generar un JSON que no cumple el esquema esperado — campos ausentes, tipos incorrectos, valores fuera de rango — lo que rompe el sistema downstream que consume ese output.

**Estrategia de verificación:**

Esta es la verificación más mecánica y la más fácil de implementar. Antes de pasar el output a cualquier sistema downstream:

1. Validar el JSON/XML contra el esquema esperado (JSON Schema, XSD).
2. Verificar que los campos obligatorios están presentes.
3. Verificar que los valores están dentro de rangos válidos para el dominio.
4. Si la validación falla, retroalimentar el error al modelo con el esquema esperado y el mensaje de error, y pedir una corrección.

La mayoría de los frameworks de agentes modernos incluyen soporte para generación de outputs estructurados con validación automática (structured outputs, tool calling con schemas). Usar esta capacidad en lugar de parsear texto libre elimina la mayoría de los errores de tipo 4.

---

### LLM-as-judge: verificación asistida por modelo

Cuando la verificación automática no es posible — el output es texto no estructurado y no existe una fuente de verdad mecánicamente accesible — una opción es usar un segundo modelo como evaluador. Este patrón se conoce como LLM-as-judge.

**Principios de diseño del LLM-as-judge:**

- El modelo evaluador recibe: el output original, los criterios de evaluación explícitos y, si es posible, ejemplos de outputs buenos y outputs malos.
- El prompt del evaluador debe pedir una evaluación estructurada: puntaje en cada criterio, justificación específica para cada puntaje.
- El evaluador debe ser instruido para buscar problemas activamente, no para confirmar calidad.
- Si es posible, usar un modelo diferente al generador para el evaluador. Si el mismo modelo se usa, el prompt debe ser significativamente diferente.

**Limitación fundamental:** El LLM-as-judge hereda los puntos ciegos del modelo evaluador. Para cualquier error que el modelo evaluador no pueda detectar, este mecanismo no ayuda. Es una capa adicional de calidad, no una garantía de corrección.

### Combinando verificación y reflexión

El flujo de alta calidad en producción combina ambos mecanismos:

```
[Generación] → [Reflexión interna: coherencia y completitud]
             → [Verificación externa: corrección según tipo de output]
             → [Si verificación falla: retroalimentación al agente]
             → [Nueva generación con contexto de error]
             → [Re-verificación]
             → [Output final si verificación pasa]
             → [Escalada a humano si no converge en N iteraciones]
```

### Nota del arquitecto

La tentación en producción es confiar en la reflexión interna y omitir la verificación externa para reducir latencia y costo. Este es el error que lleva a sistemas que funcionan bien en demos pero fallan en producción. Para cualquier output que tomará una decisión real — código que se desplegará, respuesta que se presentará como hecho, plan que se ejecutará sobre recursos reales — la verificación externa no es opcional. El costo de la verificación es una fracción del costo de los errores que previene.

La siguiente sección examina cómo estos mecanismos se integran en arquitecturas empresariales de mayor escala.
