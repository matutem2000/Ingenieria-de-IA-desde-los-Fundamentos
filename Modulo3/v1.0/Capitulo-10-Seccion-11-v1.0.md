# Capítulo 10 — Planificación y Razonamiento

## Sección 11: Laboratorio práctico

### Ejercicio: Trazado del árbol de planificación

El objetivo de este laboratorio es que el lector diseñe el árbol de planificación de un agente antes de escribir ningún código. El trazado previo — definir qué piensa el agente primero, qué ejecuta, qué verifica — es la práctica de diseño más importante en sistemas de razonamiento. Un árbol de planificación bien trazado es la especificación del sistema; el código que lo implementa es secundario.

---

### El caso de negocio

Una empresa de comercio electrónico quiere implementar un agente que asista a los analistas de operaciones en la detección de anomalías en sus procesos logísticos. El agente recibe como input un reporte diario de operaciones (datos de pedidos, tiempos de entrega, tasas de error por centro de distribución, datos de devoluciones) y debe producir como output:

1. Un listado de anomalías detectadas, ordenadas por severidad.
2. Para cada anomalía: descripción, datos que la evidencian, posible causa raíz, acción recomendada.
3. Una síntesis ejecutiva de dos párrafos para el responsable de operaciones.

Las herramientas disponibles para el agente son:
- `leer_reporte`: accede al reporte diario de operaciones en formato JSON.
- `consultar_historico`: consulta datos históricos de hasta 90 días para comparación.
- `buscar_incidentes`: busca en la base de conocimiento de incidentes previos similares.
- `calcular_estadisticas`: calcula estadísticas descriptivas sobre series de datos.
- `generar_alerta`: registra una alerta en el sistema de monitoreo.

---

### Parte 1: Diseño del árbol de planificación

El lector debe completar el siguiente árbol de planificación antes de continuar a la parte 2.

**Instrucción:** Para cada nodo del árbol, definir:
- La acción o decisión que representa el nodo
- La herramienta utilizada (si aplica)
- El output esperado
- El criterio de éxito para ese nodo
- Qué ocurre si el nodo falla

```
NODO RAÍZ
  Input: [definir qué información recibe el agente al inicio]
  Tarea: [formular la tarea completa en una frase]

NIVEL 1 — COMPRENSIÓN DEL ESTADO ACTUAL
  Nodo 1.1: _______________
    Herramienta: _______________
    Output esperado: _______________
    Criterio de éxito: _______________
    Si falla: _______________

  Nodo 1.2: _______________
    Herramienta: _______________
    Output esperado: _______________
    Criterio de éxito: _______________
    Si falla: _______________

NIVEL 2 — DETECCIÓN DE ANOMALÍAS
  Nodo 2.1: _______________
    [completar]

  Nodo 2.2: _______________
    [completar]

  Nodo 2.3: _______________
    [completar]

NIVEL 3 — ANÁLISIS DE CAUSAS
  Nodo 3.1: _______________
    [completar]

NIVEL 4 — SÍNTESIS Y OUTPUT
  Nodo 4.1: _______________
    [completar]

  Nodo 4.2: _______________
    [completar]
```

---

### Parte 2: Árbol de planificación de referencia

Una vez que el lector ha completado su propio árbol, puede compararlo con el árbol de referencia a continuación. No existe una única respuesta correcta; el árbol de referencia es una implementación válida entre varias posibles.

```
NODO RAÍZ
  Input: reporte diario en JSON + fecha del reporte
  Tarea: "Detectar anomalías en el reporte de operaciones del [fecha],
    identificar causas probables y producir recomendaciones priorizadas."

NIVEL 1 — COMPRENSIÓN DEL ESTADO ACTUAL

  Nodo 1.1: Lectura y estructura del reporte
    Herramienta: leer_reporte
    Output esperado: JSON con datos del día estructurados
    Criterio de éxito: JSON válido, campos de pedidos, tiempos, errores y
      devoluciones presentes
    Si falla: abortar y notificar — sin datos no hay análisis posible

  Nodo 1.2: Obtención del histórico de comparación
    Herramienta: consultar_historico (últimos 30 días)
    Output esperado: serie temporal de los mismos indicadores
    Criterio de éxito: datos disponibles para al menos 20 de los últimos 30 días
    Si falla: continuar sin comparación histórica, marcar todos los hallazgos
      como "sin contexto histórico"

NIVEL 2 — DETECCIÓN DE ANOMALÍAS

  Nodo 2.1: Cálculo de métricas del día actual
    Herramienta: calcular_estadisticas
    Input: datos del nodo 1.1
    Output esperado: media, desviación y percentil de cada indicador para el día
    Criterio de éxito: métricas calculadas para todos los indicadores clave

  Nodo 2.2: Comparación con histórico
    Herramienta: calcular_estadisticas
    Input: datos del nodo 1.2
    Output esperado: media histórica y umbral de anomalía (media ± 2σ) para
      cada indicador
    Criterio de éxito: umbrales calculados para todos los indicadores

  Nodo 2.3: Identificación de anomalías (modelo — análisis)
    Input: métricas del día (2.1) + umbrales históricos (2.2)
    Output esperado: lista de indicadores que superan los umbrales, con la
      magnitud de la desviación y la severidad (alta/media/baja)
    Criterio de éxito: lista estructurada, cada anomalía justificada con
      los datos que la evidencian
    Verificación: la lista es coherente con los umbrales calculados en 2.2
      (verificación mecánica: cada anomalía declarada supera efectivamente el umbral)

NIVEL 3 — ANÁLISIS DE CAUSAS

  Nodo 3.1: Búsqueda de incidentes similares (por cada anomalía)
    Herramienta: buscar_incidentes
    Input: descripción de cada anomalía
    Output esperado: incidentes previos similares con sus causas raíz y resoluciones
    Criterio de éxito: búsqueda ejecutada; puede retornar vacío si no hay precedente

  Nodo 3.2: Hipótesis de causas raíz (modelo — razonamiento, con reflexión)
    Input: cada anomalía + incidentes similares (3.1) + datos del reporte
    Output esperado: para cada anomalía, lista de causas raíz posibles ordenadas
      por probabilidad, con la evidencia que soporta cada hipótesis
    Reflexión: el evaluador verifica que las causas son consistentes con los datos
      disponibles y no contradicen la información del histórico
    Criterio de éxito: al menos una hipótesis de causa raíz por anomalía,
      con evidencia explícita

NIVEL 4 — SÍNTESIS Y OUTPUT

  Nodo 4.1: Generación de recomendaciones (modelo — síntesis)
    Input: anomalías + causas raíz + incidentes previos (con resoluciones)
    Output esperado: para cada anomalía, acción recomendada concreta y responsable
      sugerido (si se puede inferir del contexto)
    Criterio de éxito: cada recomendación es accionable — especifica qué hacer,
      no solo qué revisar

  Nodo 4.2: Síntesis ejecutiva (modelo — redacción)
    Input: listado completo de anomalías, causas y recomendaciones
    Output esperado: dos párrafos en lenguaje no técnico para el responsable
      de operaciones: (1) situación general del día, (2) las dos o tres acciones
      más urgentes
    Criterio de éxito: coherente con el listado detallado; sin contradecir
      ningún hallazgo del análisis

  Nodo 4.3: Registro de alertas
    Herramienta: generar_alerta
    Input: anomalías de severidad alta
    Output esperado: confirmación de registro en el sistema de monitoreo
    Criterio de éxito: confirmación recibida para cada alerta de severidad alta
```

---

### Parte 3: Preguntas de análisis

Una vez completado el árbol, responder las siguientes preguntas:

**Pregunta 1:** En el árbol de referencia, el nodo 2.2 usa `calcular_estadisticas` en lugar de un modelo para calcular los umbrales. ¿Por qué esta decisión es más robusta que usar el modelo para ese cálculo? ¿En qué condiciones podría revertirse esta decisión?

**Pregunta 2:** El nodo 3.2 incluye reflexión; el nodo 4.1 no. Justifique esta asimetría: ¿qué características de la tarea del nodo 3.2 hacen que la reflexión agregue valor, y qué características del nodo 4.1 hacen que no sea necesaria?

**Pregunta 3:** Diseñe el mecanismo de escalada para este sistema: ¿qué condiciones deben disparar una escalada al analista humano antes de que el agente complete su ciclo? ¿Qué información debe incluir la escalada?

**Pregunta 4:** El nodo 1.2 tiene un comportamiento de degradación graceful: si el histórico no está disponible, continúa sin él. Identifique otros dos nodos del árbol donde un comportamiento similar sería apropiado, y describa cómo se degradaría el output en cada caso.

---

### Evaluación del laboratorio

El árbol de planificación diseñado por el lector se evalúa en cinco dimensiones:

1. **Completitud:** ¿Cubre el árbol todos los pasos necesarios para producir los tres outputs requeridos?
2. **Verificabilidad:** ¿Cada nodo tiene un criterio de éxito explícito y verificable?
3. **Manejo de fallos:** ¿Está definido el comportamiento de cada nodo cuando falla?
4. **Uso apropiado de herramientas:** ¿Las herramientas deterministas se usan para cálculos y las llamadas al modelo se reservan para razonamiento?
5. **Economía de llamadas:** ¿El árbol evita llamadas al modelo donde una herramienta determinista es suficiente?

Un árbol que puntúa bien en estas cinco dimensiones es, en sí mismo, la especificación del sistema. El código que lo implementa es un paso de traducción, no un paso de diseño.
