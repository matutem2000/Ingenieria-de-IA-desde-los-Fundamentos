# Capítulo 09 — Arquitecturas Multiagente

## Sección 06 — Planificadores y agentes supervisores

En un sistema multiagente que funciona correctamente, la inteligencia del sistema no reside únicamente en los agentes que ejecutan tareas. Reside también, y de forma crítica, en los agentes que deciden qué tareas ejecutar y que verifican que las tareas ejecutadas produjeron resultados correctos. Estos son los roles del planificador y del supervisor, y son los que transforman un conjunto de agentes independientes en un sistema con comportamiento coherente.

### El planificador: de la tarea al plan

El planificador recibe una tarea compleja del nivel superior del sistema —ya sea del usuario directamente, de una aplicación o de otro agente de nivel superior— y la transforma en un plan: una secuencia ordenada de subtareas, cada una asignada a un agente específico, con las dependencias entre ellas explicitadas.

Esta función de descomposición es más difícil de lo que parece. Una buena descomposición tiene tres características:

**Completitud:** el plan cubre todas las acciones necesarias para completar la tarea original. No hay subtareas implícitas que algún agente deba inferir o que queden sin asignación.

**No redundancia:** cada parte del trabajo está asignada a exactamente un agente. Cuando dos agentes hacen trabajo solapado, el resultado es ineficiencia y, peor, posibles inconsistencias si sus outputs sobre la misma pieza de trabajo no coinciden.

**Corrección de dependencias:** las dependencias entre subtareas están correctamente identificadas. Si la subtarea B requiere el resultado de la subtarea A, esa dependencia debe estar en el plan. Si A y B son independientes, el plan debe permitir su ejecución paralela.

El planificador implementa esta función usando el propio modelo de lenguaje como motor de razonamiento. A diferencia de un scheduler determinístico de software que ejecuta reglas predefinidas, el planificador de un sistema multiagente de IA puede razonar sobre tareas que no fueron anticipadas en su diseño. Esta flexibilidad es una de las propiedades más valiosas del planificador basado en modelos de lenguaje: puede descomponer problemas que el diseñador del sistema no pudo prever completamente.

El riesgo simétrico es que el planificador puede generar planes incorrectos. Un modelo de lenguaje que razona sobre cómo descomponer una tarea puede hacerlo de forma plausible pero errónea: olvidar una dependencia, asignar una tarea al agente equivocado, o generar subtareas que no cubren completamente la tarea original. Este riesgo es la razón por la que el planificador y el supervisor no son el mismo agente.

### Estructura de un plan

Un plan en un sistema multiagente tiene una representación formal, no textual. El planificador no produce un párrafo explicando qué deben hacer los agentes: produce una estructura de datos que el sistema puede interpretar y ejecutar. Una representación típica es una lista de nodos con sus dependencias:

```json
{
  "plan_id": "plan_001",
  "tareas": [
    {
      "id": "t1",
      "agente": "investigador",
      "descripcion": "Recuperar los estados financieros del cliente X de los últimos tres años",
      "dependencias": []
    },
    {
      "id": "t2",
      "agente": "investigador",
      "descripcion": "Recuperar el historial legal del cliente X en los últimos cinco años",
      "dependencias": []
    },
    {
      "id": "t3",
      "agente": "analista_financiero",
      "descripcion": "Analizar los estados financieros recuperados y producir un resumen de riesgo",
      "dependencias": ["t1"]
    },
    {
      "id": "t4",
      "agente": "analista_legal",
      "descripcion": "Analizar el historial legal y producir un resumen de riesgo",
      "dependencias": ["t2"]
    },
    {
      "id": "t5",
      "agente": "redactor",
      "descripcion": "Redactar el informe de due diligence integrando ambos análisis",
      "dependencias": ["t3", "t4"]
    }
  ]
}
```

Este plan codifica que t1 y t2 pueden ejecutarse en paralelo (sin dependencias), que t3 y t4 pueden ejecutarse en paralelo entre sí pero requieren que t1 y t2 hayan terminado, y que t5 solo puede comenzar cuando t3 y t4 estén completas. El ejecutor del plan —que puede ser el mismo planificador u otro componente del sistema— lee esta estructura y la ejecuta respetando las dependencias.

### El supervisor: verificación independiente de calidad

El supervisor recibe el output de un agente ejecutor y lo evalúa contra criterios explícitos antes de que ese output sea aceptado como válido por el sistema. No produce contenido: produce evaluaciones.

La lógica de la supervisión es análoga a la revisión por pares en contextos humanos: la persona que generó el trabajo no es la mejor posición para detectar sus propios errores. El supervisor es el segundo par de ojos que puede detectar lo que el agente ejecutor no vio, precisamente porque no participó en la generación.

Un supervisor bien diseñado tiene criterios de evaluación explícitos en su instrucción de sistema. No evalúa de forma genérica ("¿esto es bueno?") sino contra dimensiones específicas relevantes para la tarea:

- Para un análisis financiero: ¿los números citados corresponden a las fuentes recuperadas? ¿Las conclusiones siguen lógicamente de los datos presentados? ¿Hay afirmaciones que no están respaldadas por evidencia?
- Para un bloque de código generado: ¿el código maneja los casos borde identificados en la especificación? ¿Hay dependencias no declaradas? ¿El código es ejecutable sin modificaciones?
- Para un informe redactado: ¿el tono es apropiado para la audiencia especificada? ¿La estructura sigue el formato requerido? ¿Hay inconsistencias entre diferentes secciones?

El output del supervisor es una evaluación estructurada que incluye: si el output es aceptable o requiere corrección, qué problemas específicos fueron encontrados y —opcionalmente— qué tipo de corrección resolvería cada problema. El supervisor no corrige: señala. La corrección es responsabilidad del agente que generó el output.

### El ciclo planificador-ejecutor-supervisor

La arquitectura completa del sistema de control en un sistema multiagente de producción tiene la forma de un ciclo:

1. El planificador recibe la tarea y genera el plan de subtareas.
2. El ejecutor (orquestador) distribuye las subtareas a los agentes especializados según el plan.
3. Cada agente especializado ejecuta su subtarea y produce su output.
4. El supervisor recibe cada output y lo evalúa.
5. Si el output es aceptable, el ejecutor avanza al siguiente paso del plan.
6. Si el output requiere corrección, el ejecutor reenvía la subtarea al agente especializado con el feedback del supervisor.
7. El agente especializado produce una versión corregida.
8. El ciclo de supervisión se repite hasta que el output es aceptable o se alcanza un límite de reintentos.

Este ciclo añade latencia y costo en comparación con un sistema que acepta todos los outputs sin supervisión. El valor que justifica ese costo es la reducción de errores en el output final. Para tareas de baja criticidad donde el usuario puede evaluar y corregir el resultado, la supervisión puede omitirse. Para tareas de alta criticidad donde un error en el output tiene consecuencias reales, el ciclo planificador-ejecutor-supervisor es la arquitectura correcta.

### Planificación adaptativa

En los sistemas multiagente más sofisticados, el planificador no genera un plan único al inicio y lo ejecuta de forma rígida. Genera un plan inicial, pero también tiene la capacidad de revisar ese plan cuando los resultados intermedios revelan información que cambia lo que se debe hacer.

Considera un sistema de investigación que planificó cinco búsquedas independientes. Las primeras dos búsquedas revelan que el problema tiene una dimensión no anticipada. Un planificador adaptativo puede actualizar el plan para añadir tres búsquedas adicionales que cubran esa dimensión nueva, antes de que el agente síntesis intente producir la respuesta final con información incompleta.

Esta capacidad de replanificación requiere que el planificador tenga acceso a los resultados intermedios del sistema y que su instrucción de sistema incluya explícitamente la responsabilidad de revisar y actualizar el plan cuando el contexto lo justifique. Sin esa capacidad, el planificador es rígido y el sistema produce resultados de menor calidad en tareas que no se ajustan perfectamente al plan inicial.

---

*La sección 07 aborda el problema técnico más desafiante de los sistemas multiagente: cómo múltiples agentes acceden y actualizan un estado compartido sin generar inconsistencias. Este no es un problema de coordinación de alto nivel sino un problema de ingeniería de sistemas que requiere soluciones concretas.*
