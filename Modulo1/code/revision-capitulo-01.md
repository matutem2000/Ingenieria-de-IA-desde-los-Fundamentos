# Revisión editorial — Capítulo 1

**Capítulo:** 1 — ¿Qué entendemos por inteligencia?  
**Versión origen:** 0.1  
**Versión generada:** 0.5  
**Fecha:** 2026-06-28  
**Editor:** Revisión técnica y pedagógica

---

## Cambios realizados

### Estructura

- La v0.1 tenía 8 secciones informales sin jerarquía consistente.
- La v0.5 tiene 17 secciones con estructura editorial estandarizada: objetivos, introducción, motivación, desarrollo conceptual, analogía, diagrama, ejemplo real, conversación con arquitecto, errores frecuentes, buenas prácticas, laboratorio, preguntas de reflexión, resumen, checklist, glosario, referencias cruzadas, próximos pasos.

### Narrativa

- La introducción pasó de 2 párrafos genéricos a 3 párrafos con argumento específico sobre por qué la claridad conceptual es una necesidad profesional, no filosófica.
- Se incorporó una sección de "Motivación del problema" que explica la paradoja de la industria actual: se implementa IA sin claridad sobre qué tipo de inteligencia se necesita.
- El tono mantuvo la conversación directa con el lector (tuteo), sin caer en lenguaje académico.

### Extensión

- v0.1: aproximadamente 750 palabras, 8 secciones.
- v0.5: aproximadamente 4.200 palabras, 17 secciones.

---

## Mejoras incorporadas

### Desarrollo conceptual expandido

- Se definieron 8 dimensiones cognitivas específicas (razonamiento lógico, memoria, aprendizaje, abstracción, planificación, lenguaje, percepción, metacognición) con descripción individual y relevancia para la IA.
- Se agregó la sección "¿Por qué importa esto para la IA?" que conecta cada dimensión cognitiva con tipos concretos de sistemas (LLM, ML clásico, sistemas expertos).
- Se incorporó la mención de la Prueba de Turing como punto de partida histórico concreto.

### Conversación con el arquitecto

- La v0.1 no tenía conversación con arquitecto.
- La v0.5 incorpora un diálogo de 5 intercambios entre Martina (desarrolladora senior) y Diego (arquitecto), con un caso real donde la decisión correcta fue NO usar IA, y donde el arquitecto debe argumentar esa decisión ante un cliente que venía convencido de necesitarla.

### Errores frecuentes

- Sección nueva con 3 errores detallados: tratar la IA como concepto unitario, confundir competencia en una dimensión con inteligencia general, ignorar la metacognición.
- Cada error incluye su consecuencia práctica y una heurística de mitigación.

### Buenas prácticas

- Sección nueva con 6 prácticas accionables orientadas a arquitectos y desarrolladores, no a investigadores.

### Laboratorio

- La v0.1 tenía 5 preguntas de ejercicio sin estructura.
- La v0.5 tiene un laboratorio estructurado con escenario realista (empresa FreightCore), 4 pasos con tiempo estimado para cada uno, tabla de trabajo, criterios de validación, preguntas de reflexión y 3 desafíos opcionales progresivos.

### Diagramas

- Se incorporó un diagrama mindmap Mermaid que mapea las 8 dimensiones cognitivas con los sistemas de IA que las cubren parcialmente.
- Se incorporó un segundo diagrama flowchart que modela el proceso de decisión para descomponer un problema de negocio en subproblemas y evaluar si requieren IA.

### Referencias cruzadas

- Se agregaron referencias explícitas a los capítulos 4, 6, 7, 8, 9, 10, 12 y 14 donde los conceptos introducidos aquí se desarrollan en profundidad.
- Se incorporó una tabla de referencias cruzadas al final del capítulo.

### Ejemplo real

- La v0.1 tenía ejemplos abstractos sin personajes ni contexto empresarial.
- La v0.5 incorpora el caso TerraLogix: empresa real ficticia con nombre, directora comercial (Valentina Soria), CTO (Rodrigo Méndez), y desenlace concreto donde un "proyecto de IA" se descompone en 3 subproblemas con soluciones distintas.

---

## Conceptos agregados

Los siguientes conceptos no estaban presentes en la v0.1 y fueron incorporados en la v0.5:

- **Metacognición** como dimensión cognitiva crítica y su ausencia en la mayoría de los sistemas de IA actuales.
- **Prueba de Turing** como referencia histórica concreta al origen del debate sobre inteligencia en máquinas.
- **Alucinación** como fenómeno emergente de los LLM que ilustra la diferencia entre competencia en una dimensión y confiabilidad general.
- **Primeros principios** como método de análisis explícito y nombrado.
- **Inferencia** en el glosario como término que reaparecerá en capítulos posteriores.
- La distinción entre **IA como producto** (ChatGPT) e **IA como campo** (décadas de investigación acumulada).
- La **paradoja de la industria actual**: velocidad de implementación sin claridad conceptual.

---

## Dudas detectadas

1. **¿Incluir o no la Prueba de Turing?** Se incluyó como referencia histórica porque sitúa el debate en el tiempo y es un concepto conocido por el público objetivo. Sin embargo, el capítulo 3 (Historia de la IA) podría profundizar más en este punto. Riesgo de redundancia leve si el Capítulo 3 la desarrolla en extenso.

2. **Nivel de profundidad en las dimensiones cognitivas.** Se optó por 8 dimensiones con descripciones de 2-3 oraciones cada una. Podría ser demasiado extenso para un capítulo introductorio, o insuficiente para quienes quieren fundamentos más sólidos. Recomendaría al editor principal confirmar si el nivel es adecuado para el perfil del lector objetivo.

3. **El laboratorio no requiere herramientas técnicas.** Es puramente conceptual. Esto es coherente con ser el Capítulo 1, pero algunos lectores pueden sentir que falta "manos en la masa". Los laboratorios técnicos comienzan naturalmente en el Capítulo 4.

4. **Las referencias cruzadas son todas hacia capítulos futuros.** El Capítulo 1 no puede referenciar capítulos anteriores por ser el primero. Esto es correcto pero significa que el lector tiene que confiar en que los conceptos se expandirán. Evaluar si agregar una nota explícita sobre la estructura del libro en la introducción.

---

## Recomendaciones para el editor principal

1. **Confirmar que el caso TerraLogix no colisione con casos en el Capítulo 14.** Si el Capítulo 14 tiene un caso de empresa consultora de infraestructura similar, conviene diferenciarlos o usar el mismo caso con más detalle.

2. **Verificar consistencia terminológica con el glosario global.** Los términos "alucinación", "inferencia" y "primeros principios" aparecen aquí por primera vez. Confirmar que el TERMINOLOGY.md los define de la misma forma.

3. **Evaluar si el laboratorio debe ser obligatorio o optativo.** Al ser puramente conceptual, podría perderse entre lectores que esperan código desde el inicio. Una nota aclaratoria ("los laboratorios técnicos comienzan en el Capítulo 4") podría calibrar expectativas.

4. **La conversación con el arquitecto es el elemento más distintivo del capítulo.** El diálogo Diego-Martina modela exactamente el tipo de razonamiento que el libro quiere desarrollar. Recomiendo preservarlo intacto en revisiones futuras y usarlo como referencia de tono para los diálogos de los capítulos posteriores.

5. **La sección de Referencias cruzadas puede ser opcional en la versión impresa.** Para la versión digital o ebook, sería valioso convertirlas en hipervínculos activos. Para la versión impresa podría eliminarse para economizar espacio, dado que la información ya está en el cuerpo del texto.
