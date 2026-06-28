---
capitulo: 11
titulo: "Temperatura, Top-K, Top-P y Sampling"
version: 0.5
tipo: notas-revision
fecha: 2026-06-28
revisor: Editor técnico y pedagógico
estado: Borrador revisión conceptual
---

# Notas de Revisión — Capítulo 11: Temperatura, Top-K, Top-P y Sampling

**Versión revisada:** 0.5 (desde v0.1)
**Fecha:** 2026-06-28

---

## 1. Resumen de cambios respecto de la v0.1

La versión 0.1 era un borrador esquemático que cubría los conceptos centrales con corrección pero sin profundidad pedagógica. El texto era breve, estructurado como lista de definiciones yuxtapuestas, sin análisis de trade-offs ni contexto de aplicación. La v0.5 representa una expansión sustancial en múltiples dimensiones.

| Dimensión | v0.1 | v0.5 |
|---|---|---|
| Longitud estimada | ~900 palabras | ~6.000 palabras |
| Secciones | 12 básicas | 17 completas según estructura obligatoria |
| Diagramas Mermaid | 0 | 2 |
| Explicación de Greedy Decoding | Ausente | Sección dedicada con análisis de fallos |
| Intuición matemática de la Temperatura | Ausente | Analogía del paisaje (afilamiento/aplanamiento) |
| Tabla de configuraciones por tipo de tarea | Ausente | 7 tipos de aplicación con 4 parámetros cada uno |
| Parámetro seed | No mencionado | Sección propia + integrado en laboratorio y tabla |
| Conversación con arquitecto | 2 intercambios genéricos | 5 intercambios con profundidad técnica y de negocio |
| Errores frecuentes | Ausentes | 5 errores documentados con mecanismo y heurística |
| Buenas prácticas | 4 ítems en lista | 6 prácticas con justificación técnica |
| Laboratorio | 3 pasos genéricos | 5 pasos estructurados con tabla de registro y reflexión post-lab |
| Preguntas de reflexión | 3 preguntas | 7 preguntas con escenarios concretos |
| Glosario | Ausente | 8 términos con definición precisa |
| Checklist | Ausente | 9 ítems verificables y accionables |

---

## 2. Decisiones editoriales tomadas

### 2.1 Reordenamiento de la estructura conceptual

La v0.1 presentaba los conceptos en este orden: analogía, temperatura, sampling, Top-K, Top-P, casos prácticos. Este orden es funcional pero no parte de primeros principios.

La v0.5 reestructura el desarrollo conceptual en el siguiente orden:
1. La distribución de probabilidades (el fundamento que todo lo demás presupone).
2. Greedy Decoding (la estrategia más simple y sus fallos).
3. Sampling (la alternativa y su problema).
4. Temperatura (el modificador de la distribución, antes de cualquier filtro).
5. Top-K (filtro de candidatos fijo).
6. Top-P (filtro adaptativo).
7. Seed (reproducibilidad).

Este orden sigue la lógica de necesidad: cada concepto surge como solución a un problema del concepto anterior. Greedy Decoding es simple pero produce loops → Sampling lo resuelve pero introduce tokens marginales → Top-K los elimina pero con corte fijo → Top-P mejora con corte adaptativo. La Temperatura no es una solución a un problema específico sino el parámetro que atraviesa toda la cadena.

### 2.2 Incorporación de Greedy Decoding como sección propia

La v0.1 no mencionaba Greedy Decoding. Esta es una omisión significativa porque:
- Es el punto de contraste necesario para explicar por qué existe el Sampling.
- Sus fallos (loops, pobreza léxica, falta de coherencia global) son problemas reales en producción que los lectores necesitan anticipar.
- Muchos frameworks lo usan como default implícito, lo cual lleva a errores de configuración.

La sección de Greedy Decoding fue incluida como subsección 4.2 con tres fallos concretos: loops repetitivos, pobreza léxica y pérdida de coherencia global.

### 2.3 Tratamiento de la Temperatura sin fórmulas

La instrucción especificaba explicar la intuición matemática de la temperatura sin fórmulas. El recurso utilizado es la analogía del "paisaje": la distribución de probabilidades como terreno con montañas y valles, donde la temperatura afila o aplana ese paisaje.

Se eligió este recurso por tres razones:
- Es intuitivamente accesible para el perfil del lector (profesional de tecnología sin formación en ML).
- Captura el efecto real del parámetro de forma correcta sin simplificación engañosa.
- Se integra naturalmente con la analogía del dado cargado de la sección 5.

### 2.4 Analogía del dado cargado

La v0.1 usaba la analogía de completar "Hoy está haciendo mucho..." que ilustra bien la variabilidad, pero no conecta con la mecánica de los parámetros de sampling.

La v0.5 mantiene esa introducción en la sección de motivación y construye la analogía central del dado cargado en la sección 5, que cubre explícitamente:
- Dado como metáfora de la distribución de probabilidades.
- Greedy Decoding como "no tirar el dado".
- Temperatura baja como dado más extremo.
- Temperatura alta como dado aplanado.
- Top-K como tapar caras.
- Top-P como tapar hasta alcanzar el 80% de la superficie.

Esto permite que el lector use una sola metáfora para entender todos los parámetros en conjunto, en lugar de metáforas desconectadas para cada uno.

### 2.5 Tabla de configuraciones recomendadas

La instrucción pedía una tabla de configuraciones por tipo de tarea. La tabla incluye 7 tipos de aplicación (generación de código, QA empresarial, chatbot de atención, escritura creativa, análisis de datos, lluvia de ideas, resumen de documentos) con 4 parámetros cada uno (temperatura, Top-K, Top-P, seed) y una columna de fundamento.

Decisión clave: los rangos son deliberadamente amplios y las notas de fundamento explican el razonamiento, no solo el número. El objetivo es que el lector entienda el criterio, no que memorice valores.

### 2.6 Tratamiento del seed

El parámetro seed no estaba en la v0.1 pero sí en las instrucciones de ampliación. Se integró en:
- Una subsección propia (4.7) que explica el mecanismo y los casos de uso.
- La tabla de configuraciones (columna seed con indicación Fijo/No).
- El laboratorio (pasos 2-4 usan seed fijo; paso 5 lo remueve deliberadamente para observar la variabilidad natural).
- Error frecuente 4 (no usar seed en contextos de auditoría).
- Buena práctica 2 (baseline con seed fijo antes de optimizar).

Esta integración múltiple asegura que el concepto no quede como un apéndice sino como parte del toolkit de configuración del arquitecto.

### 2.7 Conversación con el arquitecto

La v0.1 tenía un intercambio de dos líneas genéricas. La v0.5 construye una conversación de 5 intercambios anclada en un escenario concreto: un asistente de consultas sobre contratos de servicio con temperatura incorrectamente configurada en 1.2.

Los intercambios cubren:
1. El síntoma reportado por el desarrollador.
2. El diagnóstico del arquitecto (pedido de contexto de configuración).
3. La explicación del problema con temperatura 1.2 para ese caso de uso.
4. La pregunta sobre los riesgos de temperatura demasiado baja.
5. La recomendación sobre Top-K versus Top-P y la nota sobre configuración como parámetro de infraestructura.

El escenario de contratos legales fue elegido porque hace tangibles las consecuencias de una configuración incorrecta: no es solo texto subóptimo, es riesgo legal.

### 2.8 Laboratorio en 5 pasos

La v0.1 tenía un laboratorio de 3 ítems genéricos sin estructura. La v0.5 diseña un laboratorio con:
- Objetivo explícito.
- Lista de materiales.
- 5 pasos secuenciales con instrucciones concretas de configuración (temperatura, top_p, seed).
- Una tabla de registro con columnas predefinidas.
- Una sección de reflexión post-laboratorio con 3 preguntas.

El laboratorio usa seed fijo en los primeros pasos para separar el efecto de la temperatura del ruido del sampler, y luego lo remueve en el paso 5 para observar la variabilidad natural. Esta progresión es pedagógicamente deliberada.

---

## 3. Decisiones sobre los diagramas Mermaid

### 3.1 Diagrama de distribuciones (sección 6)

La instrucción pedía un diagrama de distribución de probabilidades con distintas temperaturas. Se tomó la decisión de usar dos diagramas complementarios:

- Un `xychart-beta` para mostrar la distribución base (temperatura 1.0).
- Un `graph TD` con tres subgrafos side-by-side que muestran cómo cambian los pesos con temperatura 0.2, 1.0 y 1.8.

La razón de no usar solo el xychart: no permite mostrar fácilmente múltiples distribuciones para comparar. El graph TD permite mostrar los tres escenarios de forma paralela y visualmente contrastante.

### 3.2 Diagrama de estrategias de sampling (sección 7)

Se usó `flowchart TD` para mostrar las cuatro estrategias (Greedy Decoding, Sampling puro, Top-K, Top-P) como ramas paralelas desde la misma distribución de entrada, con los resultados y riesgos de cada una al final.

Código de colores:
- Rojo: Greedy Decoding (más restrictivo, más riesgos de loops).
- Amarillo: Sampling puro (intermedio pero con riesgo de tokens marginales).
- Azul: Top-K (mejora estructurada pero con limitación del corte fijo).
- Verde: Top-P (mejor equilibrio variedad/coherencia).

La codificación de colores no es arbitraria: sigue una escala semántica de restrictividad/riesgo que el lector puede leer sin necesidad de explicación.

---

## 4. Elementos que no fueron incorporados y justificación

### 4.1 Fórmulas matemáticas de softmax y temperatura

La instrucción explícita era explicar la intuición sin fórmulas. La fórmula de softmax con temperatura (softmax(logits/T)) fue omitida intencionalmente. El lector objetivo no necesita implementar el algoritmo; necesita tomar decisiones de configuración. La intuición del paisaje cumple ese objetivo sin la carga cognitiva de la notación matemática.

### 4.2 Comparación detallada entre APIs

No se incluyó comparación de cómo distintas APIs (OpenAI, Anthropic, Google) implementan estos parámetros, porque:
- Cambia con frecuencia y desactualizaría el capítulo.
- Es información que el lector puede encontrar en la documentación de cada proveedor.
- El capítulo se focaliza en los conceptos, no en la implementación específica de cada plataforma.

### 4.3 Repetition penalty y presence penalty

Existen parámetros relacionados (repetition_penalty en modelos Hugging Face, presence_penalty y frequency_penalty en OpenAI) que también controlan la diversidad. Se decidió no incluirlos en este capítulo para mantener el foco en los cuatro parámetros centrales (temperatura, Top-K, Top-P, seed). Estos parámetros adicionales podrían ser tema de un capítulo complementario o apéndice.

---

## 5. Observaciones para la próxima revisión (v0.7)

1. **Validar los valores de la tabla de configuraciones** con benchmarks o referencias de la industria. Los valores actuales son recomendaciones basadas en práctica común pero no están citados.

2. **Considerar agregar un caso de estudio de fallo real**: un sistema de producción que tuvo problemas por configuración incorrecta de temperatura. Aumentaría la credibilidad y la relevancia práctica.

3. **Revisar compatibilidad de los diagramas Mermaid** con el renderizador del entorno de publicación final. El `xychart-beta` es una característica relativamente nueva de Mermaid y puede no estar disponible en todas las versiones.

4. **Evaluar agregar un diagrama de flujo del laboratorio** para guiar visualmente la secuencia de experimentos.

5. **Preguntas de reflexión 6 y 7** son las más complejas del conjunto. Evaluar si son adecuadas para el nivel del capítulo o si deberían moverse a una sección de ejercicios avanzados.
