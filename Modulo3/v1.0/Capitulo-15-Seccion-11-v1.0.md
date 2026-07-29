# Capítulo 15 — Proyecto Integrador

## Sección 11: Laboratorio integrador

El laboratorio integrador tiene un único objetivo: que hagas el trabajo de diseñar, no de describir lo que harías. Está estructurado en tres niveles de profundidad. Puedes completar solo el nivel básico, los dos primeros, o los tres. Cada nivel tiene valor independiente. No se requiere infraestructura de producción para ninguno de los tres niveles: solo papel, diagrama y capacidad de razonamiento.

---

### Nivel básico — Diseñar la arquitectura para un caso propio

**Consigna:**

Elige un problema de negocio de tu propio contexto (laboral, académico o personal) que cumpla estas tres condiciones:
1. Existe documentación interna relevante que podría ser indexada en RAG.
2. Hay al menos una acción sobre un sistema externo que el asistente debería poder ejecutar.
3. El asistente debe recordar algo entre sesiones para ser verdaderamente útil.

Si no encuentras un caso en tu contexto, usa este: **Asistente de atención al cliente para una ferretería con catálogo de 3.000 productos, precios que cambian semanalmente, y un sistema de inventario al que se puede consultar el stock en tiempo real.**

**Entregables:**

1. **Descripción del problema** (máximo 200 palabras): qué problema resuelve el asistente, quiénes son los usuarios, qué decisión tomarían mejor o más rápido con el asistente que sin él.

2. **Diagrama de arquitectura** (puede ser dibujado a mano o con cualquier herramienta de diagramas): los siete componentes de la arquitectura de TechCore adaptados a tu caso. Nombra cada componente con su función específica en tu caso, no con nombres genéricos.

3. **Tabla de cobertura de componentes**: misma tabla que se usó en la sección 02 para TechCore, pero para tu caso. Verifica que cada componente del módulo (instrucciones del sistema, memoria, RAG, herramientas, agentes, observabilidad, seguridad) está activo en tu diseño. Si algún componente no aplica, justifica por qué.

**Criterio de calidad:** El diagrama debe poder ser entendido por alguien que no estuvo en el proceso de diseño. Si tienes que explicar verbalmente cada caja, el diagrama no es suficientemente claro.

---

### Nivel intermedio — Documentar las decisiones de diseño

**Consigna:**

Toma el diseño producido en el nivel básico y documenta las cinco decisiones de arquitectura más importantes. Para cada decisión:

1. **La decisión**: qué elegiste hacer (una frase).
2. **La alternativa considerada**: qué otra opción evaluaste (una frase).
3. **La justificación**: por qué elegiste la opción que elegiste y no la alternativa (dos a cuatro oraciones).
4. **El costo de la decisión**: qué sacrificaste al tomar esa decisión (una o dos oraciones).
5. **La condición de reversión**: en qué circunstancia cambiarías esta decisión (una oración).

**Plantilla de decisión:**

```
DECISIÓN [número]: [título breve]

Elegí: [opción elegida]
Alternativa: [opción descartada]

Justificación:
[Por qué la opción elegida es mejor que la alternativa en este contexto específico]

Costo:
[Qué se sacrifica al tomar esta decisión]

Condición de reversión:
[Cuándo esta decisión debería revisarse]
```

**Cinco preguntas guía para identificar las decisiones de arquitectura de tu caso:**

- ¿Por qué RAG en lugar de fine-tuning, o viceversa?
- ¿Por qué un agente en lugar de un flujo fijo de herramientas, o viceversa?
- ¿Por qué ventana deslizante en lugar de resumen incremental para el historial, o viceversa?
- ¿Por qué confirmación de usuario antes de ejecutar herramientas, o sin confirmación?
- ¿Por qué un único perfil de instrucciones del sistema, o perfiles diferenciados por rol?

Si tu caso tiene decisiones más relevantes que las sugeridas, documéntalas en lugar de las que no apliquen.

**Criterio de calidad:** Una decisión bien documentada debe permitir a otro ingeniero entender por qué se tomó esa decisión en este contexto y qué haría que cambiara. Si la justificación es genérica ("es más escalable", "es la mejor práctica"), no es suficientemente buena. La justificación debe ser específica para tu caso.

---

### Nivel avanzado — Análisis de riesgos y mitigaciones

**Consigna:**

Identifica tres riesgos del diseño que produciste. Un riesgo no es un error de implementación: es una condición del entorno o del uso del sistema que, si ocurre, puede degradar o comprometer el sistema. Para cada riesgo:

1. **Descripción del riesgo**: qué puede salir mal, en qué circunstancias (dos a tres oraciones).
2. **Probabilidad estimada**: alta / media / baja, con una justificación de la estimación.
3. **Impacto estimado**: crítico / alto / medio / bajo, con una justificación.
4. **Señal de detección**: cómo sabrías que el riesgo se está materializando antes de que cause daño severo.
5. **Mitigación propuesta**: qué cambio de diseño o qué proceso operacional reduce el riesgo a un nivel aceptable.

**Plantilla de riesgo:**

```
RIESGO [número]: [nombre del riesgo]

Descripción:
[Qué puede salir mal y en qué circunstancias]

Probabilidad: [alta/media/baja]
Justificación: [por qué estimas esa probabilidad]

Impacto: [crítico/alto/medio/bajo]
Justificación: [por qué estimas ese impacto]

Señal de detección:
[Indicador observable que permite detectar el riesgo antes de que escale]

Mitigación propuesta:
[Cambio de diseño o proceso que reduce el riesgo a nivel aceptable]
```

**Tres categorías de riesgo para guiar la búsqueda:**

- **Riesgos de datos**: la base documental RAG se desactualiza, los documentos tienen errores, la calidad del chunking es deficiente para ciertos tipos de documentos.
- **Riesgos de comportamiento del modelo**: el LLM alucina con documentos de dominio especializado, la instrucción del sistema se vuelve ambigua a medida que se agregan casos borde, el agente entra en bucles en escenarios no anticipados.
- **Riesgos operacionales**: el costo de la API del LLM escala inesperadamente, la disponibilidad del proveedor de LLM cae, un cambio en la API del proveedor rompe el orquestador.

**Criterio de calidad:** La mitigación debe ser concreta. "Mejorar el monitoreo" no es una mitigación concreta. "Agregar una alerta cuando el número de fragmentos recuperados con cita cae por debajo del 50 % durante tres días consecutivos, lo que indica posible desactualización del índice RAG" es una mitigación concreta.

---

### Reflexión final del laboratorio

El laboratorio tiene tres niveles porque integrar un sistema de IA requiere tres capacidades distintas:

El nivel básico ejercita la síntesis estructural: ¿puedo producir una arquitectura coherente que integre todos los componentes necesarios para resolver el problema?

El nivel intermedio ejercita el razonamiento de diseño: ¿puedo justificar por qué elegí esta arquitectura y no otra, con argumentos específicos para este caso?

El nivel avanzado ejercita el pensamiento de riesgo: ¿puedo anticipar qué puede fallar en un sistema que diseñé, antes de que falle en producción?

Las tres capacidades son necesarias para un AI Engineer profesional. Un sistema diseñado sin razonamiento documentado no puede mantenerse. Un sistema diseñado sin análisis de riesgos sorprende a quien lo opera en el momento más inoportuno.

---

Con el laboratorio completo, el capítulo entra en su bloque de cierre. La siguiente sección entrega el checklist profesional definitivo del módulo.
