# Notas de Revisión Editorial — Capítulo 4: Machine Learning

**Versión revisada:** v0.5 (Draft)
**Versión base:** v0.1
**Fecha:** 2026-06-28
**Editor técnico:** Editor técnico y pedagógico del proyecto

---

## Resumen de la revisión

La versión v0.5 representa una expansión significativa respecto al borrador v0.1. Se preservó la estructura conceptual original y se profundizó en todos los ejes pedagógicos identificados como insuficientes en la versión inicial.

---

## Cambios principales respecto a v0.1

### 1. Metadata y encabezado
- **v0.1:** Encabezado con título y versión básica.
- **v0.5:** Frontmatter YAML completo con módulo, capítulo, versión, estado, autor y fecha.

### 2. Objetivos de aprendizaje
- **v0.1:** Lista de 6 objetivos generales con verbos poco precisos.
- **v0.5:** Lista de 7 objetivos con verbos de acción taxonomía Bloom (explicar, identificar, describir, diferenciar, ubicar, aplicar, reconocer). Cada objetivo es verificable.

### 3. Introducción
- **v0.1:** 5 párrafos cortos, directos pero superficiales.
- **v0.5:** 3 párrafos narrativos que contextualizan el problema histórico, reconocen el valor del paradigma tradicional y establecen el problema central sin anticipar la solución.

### 4. Motivación del problema
- **v0.1:** El ejemplo del perro estaba presente pero sin análisis de por qué falla estructuralmente.
- **v0.5:** Se amplió con dos escenarios (reconocimiento de imágenes + filtro de spam), se explicó por qué el problema es estructural —no de implementación— y se articuló la pregunta que cambió la historia.

### 5. Desarrollo conceptual — nuevo contenido v0.5
Los siguientes conceptos no existían en v0.1 y fueron incorporados desde primeros principios:
- Notación matemática de modelo como función paramétrica `f(x; θ) = ŷ`
- Función de costo: definición conceptual y rol en el entrenamiento
- Gradiente descendente: intuición geométrica y fórmula de actualización `θ = θ - α ∇L`
- Tasa de aprendizaje: concepto y consecuencias de valores extremos
- Ciclo completo de entrenamiento supervisado como proceso iterativo de 6 pasos

### 6. Analogía
- **v0.1:** Sin analogía explícita.
- **v0.5:** Analogía del lanzamiento de dardo con ojos vendados. Breve, precisa, escalable (introduce el concepto de escala como diferenciador respecto al aprendizaje humano).

### 7. Diagramas Mermaid
- **v0.1:** Árbol de texto plano (no Mermaid) para la jerarquía IA→ML.
- **v0.5:** Dos diagramas Mermaid:
  - Diagrama 1: Flujo completo de entrenamiento supervisado (flowchart con ciclo de retroalimentación, evaluación y decisión de generalización).
  - Diagrama 2: Jerarquía IA→ML→DL→LLM con modelos específicos en hoja (graph TD con estilos de colores).

### 8. Tipos de aprendizaje
- **v0.1:** Tres secciones breves con ejemplos mínimos.
- **v0.5:** Cada paradigma incluye una explicación del mecanismo subyacente, no solo ejemplos. Se agregó la mención de RLHF en aprendizaje por refuerzo como conexión con LLM (capítulo futuro).

### 9. Código Python — nuevo en v0.5
Incorporado según instrucciones editoriales para v0.5. Nivel 1 (mínimo). Dos bloques:
- Clasificador de spam con reglas explícitas (enfoque tradicional).
- Clasificador de spam con Naive Bayes de scikit-learn (enfoque ML).
Ambos resuelven el mismo problema para hacer el contraste de paradigma tangible. El código incluye comentarios pedagógicos que explican el "por qué" de cada línea, no solo el "qué".

### 10. Ejemplo empresarial
- **v0.1:** Un párrafo sobre clasificación de reclamos con dos opciones sin análisis profundo.
- **v0.5:** Caso Meridian Seguros completamente desarrollado:
  - Contexto cuantificado (8.000 reclamos/semana, 12 analistas, 120.000 históricos).
  - Dos opciones de arquitectura con análisis de 5 variables en tabla comparativa.
  - Decisión documentada con su justificación técnica.
  - Resultado medible (precisión 91%, tiempo de 2-4 horas a 3 segundos).
  - Lección explícita para el arquitecto.

### 11. Conversación con un arquitecto
- **v0.1:** Un intercambio de 2 turnos (cliente + arquitecto). Demasiado corto para ser pedagógico.
- **v0.5:** Diálogo de 5 intercambios que modela el razonamiento real de un arquitecto: pregunta por el problema antes de la tecnología, evalúa los datos disponibles, verifica si conviene un enfoque más simple primero, y cierra con un criterio de decisión concreto.

### 12. Errores frecuentes — nuevo en v0.5
Cinco errores documentados con explicación causal:
1. Confundir ML con IA en general.
2. Empezar por el algoritmo antes que los datos.
3. Ignorar la distribución de los datos de entrenamiento (dataset shift).
4. Asumir que más datos siempre mejoran el modelo.
5. Olvidar el mantenimiento del modelo en producción.

### 13. Buenas prácticas — nuevo en v0.5
Seis buenas prácticas con nivel de detalle profesional:
1. Definir el problema antes del algoritmo.
2. Auditar datos antes del entrenamiento.
3. Establecer línea base con el enfoque más simple.
4. Separar correctamente los conjuntos de entrenamiento, validación y prueba.
5. Diseñar el pipeline de reentrenamiento desde el principio.
6. Documentar decisiones de arquitectura con justificación.

### 14. Laboratorio
- **v0.1:** 4 ítems de reflexión sin estructura formal.
- **v0.5:** Laboratorio completo según LAB_GUIDE.md:
  - Objetivo, Nivel, Tiempo estimado, Prerrequisitos, Herramientas.
  - Escenario narrativo (TransAndina) con tres iniciativas de decisión.
  - 5 pasos detallados con Acción + Motivo + Resultado esperado.
  - 3 bloques de código Python ejecutables.
  - Criterios de validación explícitos.
  - Reflexión final narrativa.
  - 4 desafíos opcionales graduados en dificultad.

### 15. Preguntas de reflexión
- **v0.1:** 4 preguntas breves.
- **v0.5:** 7 preguntas de profundidad variable que cubren: decisión de paradigma, evaluación en producción, explicabilidad, sesgo en datos, combinación de enfoques, limitaciones del gradiente descendente, y principios de arquitectura responsable.

### 16. Resumen narrativo
- **v0.1:** 3 párrafos que resumen sin integrar los conceptos del capítulo.
- **v0.5:** 5 párrafos que sintetizan el argumento central, conectan los conceptos (función de costo, gradiente, paradigmas, jerarquía) y refuerzan el rol del arquitecto como tomador de decisiones.

### 17. Checklist del capítulo — nuevo en v0.5
7 ítems verificables con checkbox Markdown. Cada ítem corresponde directamente a un objetivo de aprendizaje.

### 18. Glosario breve — nuevo en v0.5
8 términos definidos con precisión técnica:
- Función de costo, Gradiente descendente, Hiperparámetro, Generalización, Overfitting, TF-IDF, Dataset shift, Aprendizaje supervisado.

---

## Verificación de reglas editoriales

| Regla | Estado |
|---|---|
| Primeros principios antes del "cómo" | Cumplida |
| Tono profesional y conversacional | Cumplida |
| Terminología oficial (IA, ML, DL, LLM) con sigla en primera aparición | Cumplida |
| Diagramas en Mermaid | Cumplida — 2 diagramas |
| NUNCA "La IA piensa/entiende/sabe" | Cumplida — ninguna instancia |
| Frase de cierre obligatoria | Cumplida |
| Estructura obligatoria v0.5 (17 secciones) | Cumplida — todas presentes |
| Laboratorio con al menos 5 pasos | Cumplida — 5 pasos detallados |
| Dos diagramas Mermaid | Cumplida |
| Código Python nivel 1 | Cumplida — 3 bloques ejecutables |
| Ejemplo empresarial expandido | Cumplida — Meridian Seguros |

---

## Pendientes para v0.6

Los siguientes puntos quedan abiertos para la siguiente iteración:

1. **Validación de diagramas Mermaid:** Los diagramas deben ser renderizados en el entorno de publicación para verificar que la sintaxis es correcta. Algunos nodos usan notación matemática simplificada para evitar problemas de parsing (`f x semicolon θ` en lugar de `f(x; θ)`).

2. **Ejecución del código:** Los tres bloques de código Python deben ser ejecutados en un entorno limpio con scikit-learn instalado para confirmar que no hay errores de sintaxis o dependencias.

3. **Revisión de dominio:** El caso Meridian Seguros usa métricas estimadas para propósitos pedagógicos (91% de precisión, 8.000 reclamos/semana). Si el caso se mantiene en versiones posteriores, las métricas deben ser consistentes con los rangos reales de clasificadores de texto en dominios similares.

4. **Conexión hacia atrás:** El capítulo referencia el Capítulo 3 (Historia de la IA) en la introducción. Verificar que la mención de Machine Learning en ese capítulo establece correctamente la continuidad narrativa.

5. **Conexión hacia adelante:** La introducción del Capítulo 5 (Deep Learning) debe conectar explícitamente con la jerarquía y con las limitaciones de los algoritmos clásicos de ML mencionadas en este capítulo.

6. **Accesibilidad del código:** Evaluar si el código Python del Paso 3 del laboratorio es ejecutable por un lector con perfil no-desarrollador. Si el público incluye arquitectos de soluciones o product managers técnicos, puede ser necesario agregar instrucciones de instalación del entorno más detalladas.

7. **Segunda revisión de errores frecuentes:** Considerar si el Error 3 (dataset shift) podría estar fuera del nivel esperado para v0.5. Puede quedar como "para profundizar" o ser movido al laboratorio de desafíos opcionales.

---

## Métricas del capítulo

| Métrica | v0.1 | v0.5 |
|---|---|---|
| Secciones | 11 | 17 |
| Palabras aproximadas | ~700 | ~4.800 |
| Diagramas | 1 (texto plano) | 2 (Mermaid) |
| Bloques de código | 0 | 3 |
| Errores frecuentes | 0 | 5 |
| Buenas prácticas | 4 (en "Lo que un arquitecto debería recordar") | 6 |
| Pasos de laboratorio | 4 (no estructurados) | 5 (estructurados) |
| Preguntas de reflexión | 4 | 7 |
| Términos en glosario | 0 | 8 |
