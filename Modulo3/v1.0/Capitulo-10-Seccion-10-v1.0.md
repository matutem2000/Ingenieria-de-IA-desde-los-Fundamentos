# Capítulo 10 — Planificación y Razonamiento

## Sección 10: Caso de estudio empresarial

### Sistema de análisis y aprobación de préstamos asistido por IA

Una institución financiera de tamaño mediano procesa entre 200 y 400 solicitudes de préstamos personales por día. El proceso actual es manual: un analista de crédito revisa cada solicitud, consulta el bureau de crédito, verifica documentación y emite una recomendación. El tiempo promedio por solicitud es de 45 minutos. La institución busca implementar un sistema de IA que reduzca ese tiempo a menos de 5 minutos, mantenga la calidad de las decisiones y cumpla con la regulación de transparencia de decisiones crediticias vigente en su jurisdicción.

Este caso de estudio examina las decisiones de arquitectura de planificación que hacen posible ese sistema.

---

### Análisis del problema

**Complejidad de la tarea:** Alta. Una solicitud de préstamo requiere integrar información de múltiples fuentes heterogéneas (datos del solicitante, historial crediticio, documentos de ingreso, contexto macroeconómico), aplicar criterios regulatorios específicos y producir una recomendación justificada.

**Calidad requerida:** Crítica. Un error puede implicar pérdida financiera (aprobación incorrecta de un préstamo que no se pagará) o daño reputacional y regulatorio (rechazo incorrecto de un solicitante elegible, con potencial de discriminación).

**Latencia requerida:** Moderada. El analista humano puede revisar el output del sistema antes de la decisión final; no es necesaria una respuesta en tiempo real.

**Auditabilidad requerida:** Obligatoria. La regulación exige que la institución pueda explicar cualquier decisión crediticia al solicitante que la solicite.

**Control humano:** El sistema produce recomendaciones, no decisiones. El analista humano tiene la decisión final. El sistema puede operar en modo completamente autónomo solo para solicitudes que caen claramente dentro de criterios predefinidos (aprobación automática o rechazo automático) y con límites de monto.

---

### Decisiones de arquitectura

**Patrón de planificación:** Plan-and-Execute. La secuencia de pasos es suficientemente estable como para pre-definirse, pero debe adaptarse al estado de cada solicitud.

**Número de modelos:** Dos. Un modelo mayor y más preciso para el análisis de riesgo y la redacción de la justificación; un modelo menor y más rápido para la extracción de datos estructurados de los documentos.

**Verificación:** Múltiples capas, específicas por tipo de output.

---

### El plan de análisis de solicitud

El sistema genera el siguiente plan estándar al inicio de cada solicitud. Los pasos varían según el tipo de solicitud y el perfil del solicitante.

```
PLAN DE ANÁLISIS — SOLICITUD DE PRÉSTAMO

Paso 1: Extracción de datos del solicitante
  Acción: Extraer del formulario de solicitud los campos estandarizados.
  Herramienta: extractor de formularios (modelo menor).
  Output esperado: JSON con campos validados contra esquema.
  Criterio de éxito: JSON válido, todos los campos obligatorios presentes.

Paso 2: Consulta al bureau de crédito
  Acción: Consultar el historial crediticio del solicitante.
  Herramienta: API bureau de crédito (datos externos).
  Output esperado: perfil crediticio estructurado.
  Criterio de éxito: respuesta recibida sin error; puntaje crediticio presente.

Paso 3: Verificación de documentación de ingresos
  Acción: Analizar los documentos de ingreso adjuntos a la solicitud.
  Herramienta: analizador de documentos (modelo mayor).
  Output esperado: ingreso mensual neto verificado, fuente de ingreso clasificada.
  Criterio de éxito: ingreso verificable en al menos dos documentos consistentes.

Paso 4: Cálculo de ratios financieros
  Acción: Calcular indicadores clave para la decisión.
  Herramienta: calculadora financiera (función determinista, no modelo).
  Output esperado: DTI (debt-to-income), LTI (loan-to-income), capacidad de pago.
  Criterio de éxito: todos los ratios calculados con los datos de pasos 1-3.

Paso 5: Evaluación de riesgo
  Acción: Integrar todos los datos y producir una evaluación de riesgo.
  Herramienta: modelo de análisis (modelo mayor, con reflexión).
  Output esperado: nivel de riesgo (bajo/medio/alto), factores que lo determinan.
  Criterio de éxito: evaluación justificada, coherente con los datos de entrada.

Paso 6: Generación de recomendación
  Acción: Producir la recomendación final para el analista humano.
  Herramienta: modelo de síntesis (modelo mayor).
  Output esperado: recomendación (aprobar/rechazar/solicitar información adicional),
    justificación en lenguaje claro, factores decisivos, condiciones (si aplica).
  Criterio de éxito: recomendación coherente con la evaluación del paso 5;
    justificación verificable contra los datos de los pasos 1-4.
```

---

### Ejecución: un caso real

**Solicitud:** María García solicita un préstamo personal de 25.000 para consolidación de deudas. Ingreso declarado: 3.200 mensuales. Solicitud de plazo: 48 meses.

**Paso 1 — Extracción:**

El extractor procesa el formulario. JSON generado incluye todos los campos. Verificación de esquema: válido. Tiempo: 8 segundos.

**Paso 2 — Bureau de crédito:**

Puntaje crediticio: 682/850. Historial: 2 deudas activas (tarjeta de crédito: 4.800 pendiente, préstamo de vehículo: 8.200 pendiente). Sin mora en los últimos 24 meses. Tiempo: 3 segundos (API externa).

**Paso 3 — Verificación de ingresos:**

El analizador de documentos procesa tres documentos: nómina del último mes (3.180), nómina del mes anterior (3.210), declaración fiscal del año anterior (ingreso anual: 38.400 / 12 = 3.200 mensual). Consistencia: alta. Ingreso verificado: 3.195 (promedio de los tres documentos). Tiempo: 22 segundos.

**Paso 4 — Ratios financieros:**

```
Cuota mensual del préstamo solicitado (25.000, 48 meses, tasa 8.5% anual):
  → 616 / mes

Deudas actuales:
  Tarjeta de crédito (pago mínimo estimado): 144 / mes
  Préstamo de vehículo (cuota conocida): 230 / mes

Total compromisos de deuda tras el nuevo préstamo:
  616 + 144 + 230 = 990 / mes

DTI (Debt-to-Income): 990 / 3.195 = 31%
LTI (Loan-to-Income): 25.000 / (3.195 × 12) = 0.65
Capacidad de pago residual: 3.195 - 990 = 2.205 / mes
```

Verificación: todos los ratios calculados. DTI del 31% está dentro del umbral aceptable (límite regulatorio: 40%). LTI de 0.65 está dentro del límite institucional (1.0). Tiempo: 2 segundos.

**Paso 5 — Evaluación de riesgo (con reflexión):**

*Generación inicial:*
El modelo produce una evaluación preliminar de riesgo bajo-medio, basada en el puntaje crediticio de 682, el historial sin moras y el DTI del 31%.

*Reflexión — evaluación de la generación inicial:*
El evaluador identifica un factor que la evaluación inicial no consideró: la solicitante tiene dos deudas activas que pretende consolidar con este préstamo. Si el préstamo se aprueba, la institución debe verificar que las deudas actuales serán efectivamente saldadas, de lo contrario el DTI real podría ser más alto que el calculado.

*Revisión:*
La evaluación revisada mantiene el nivel de riesgo bajo-medio pero añade una condición: la aprobación debe incluir la obligación de presentar comprobantes de liquidación de las deudas existentes dentro de los 30 días siguientes al desembolso.

**Paso 6 — Recomendación:**

```
RECOMENDACIÓN PARA EL ANALISTA

Solicitante: María García
Solicitud: Préstamo personal 25.000 / 48 meses

RECOMENDACIÓN: APROBACIÓN CONDICIONAL

FACTORES FAVORABLES:
- Puntaje crediticio 682: sobre el umbral mínimo (650).
- Sin moras en 24 meses: historial de pago consistente.
- DTI proyectado 31%: dentro del límite del 40%.
- Ingresos verificados en tres fuentes consistentes: 3.195/mes.
- Capacidad de pago residual de 2.205/mes: margen adecuado.

FACTORES DE ATENCIÓN:
- La solicitud es para consolidación de deudas. El DTI calculado asume que
  las deudas actuales serán liquidadas con el préstamo. Si no se liquidan,
  el DTI real sería del 31% + deudas actuales no liquidadas.

CONDICIÓN DE APROBACIÓN:
- Presentación de comprobantes de liquidación de deudas existentes (tarjeta
  4.800 y vehículo 8.200) dentro de los 30 días posteriores al desembolso.
- El desembolso puede realizarse directamente a los acreedores (recomendado)
  o a la solicitante con verificación posterior.

CRITERIOS REGULATORIOS CUMPLIDOS:
- DTI dentro del límite (31% < 40%).
- Ingresos verificados documentalmente.
- Puntaje crediticio sobre el mínimo institucional.

Esta recomendación está basada en la información disponible al momento del
análisis. La decisión final corresponde al analista responsable.
```

---

### Resultados del diseño

**Tiempo total de análisis:** 8 + 3 + 22 + 2 + 35 (reflexión en paso 5) + 18 (síntesis en paso 6) = 88 segundos.

El objetivo era menos de 5 minutos. Se cumple con margen amplio.

**Auditabilidad:** Cada paso tiene registrado su input, output y tiempo. La recomendación cita los datos que la fundamentan. El analista puede verificar cualquier dato contra la fuente original.

**Calidad:** La reflexión en el paso 5 detectó un factor que la evaluación inicial no había considerado — la consolidación de deudas — y lo incorporó como condición. Sin la reflexión, la recomendación habría sido menos precisa.

**Control humano:** El sistema produce una recomendación, no una decisión. El analista humano tiene toda la información necesaria para aceptar, modificar o rechazar la recomendación.

---

### Lecciones del caso

1. El diseño del plan de ejecución es tan importante como la calidad del modelo. Un plan bien estructurado con pasos verificables produce resultados más confiables que un modelo superior con un plan deficiente.

2. La reflexión debe tener un criterio de activación. En este caso, se activó en el paso de evaluación de riesgo — el paso de mayor impacto y mayor probabilidad de error — y no en los pasos de extracción o cálculo, donde la verificación mecánica es más efectiva.

3. Las herramientas deterministas son superiores al modelo para cálculos numéricos. El paso 4 usa una función de cálculo, no el modelo, para los ratios financieros. Los modelos cometen errores aritméticos; las funciones no.

4. La auditabilidad no es un añadido posterior. Se diseña desde el inicio como parte del output de cada paso.

La siguiente sección presenta el laboratorio práctico donde el lector aplica estos principios a su propio caso de uso.
