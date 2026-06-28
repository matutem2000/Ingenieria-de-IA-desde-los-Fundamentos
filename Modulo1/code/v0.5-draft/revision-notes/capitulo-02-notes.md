# Notas de revisión — Capítulo 2, v0.5

**Capítulo:** 2 — ¿Por qué nació la Inteligencia Artificial?
**Módulo:** I
**Versión base:** v0.1
**Versión generada:** v0.5
**Fecha de revisión:** 2026-06-28
**Estado:** Borrador para revisión editorial

---

## 1. Qué existía en v0.1

La v0.1 del capítulo contenía:

- Una introducción de 2 párrafos sobre el origen filosófico de la IA.
- Una sección breve sobre automatización vs. inteligencia con ejemplos del reloj y el termostato.
- Tres motivaciones para construir IA (comprendernos, resolver problemas complejos, ampliar capacidades).
- Una conversación de 2 intercambios (gerente + arquitecto).
- Tres casos de aplicación sin nombres ni contexto empresarial.
- Un resumen de 5 puntos sin narrativa.
- Un ejercicio simple de 4 preguntas sobre sistemas cotidianos.

La v0.1 era un esqueleto conceptualmente correcto pero sin profundidad suficiente para cumplir los objetivos de aprendizaje declarados ni la estructura obligatoria del proyecto.

---

## 2. Qué se expandió en v0.5

### 2.1 Objetivos de aprendizaje

**v0.1:** 5 preguntas en formato de interrogante ("¿Qué problema...?").
**v0.5:** 6 objetivos con verbos de acción (explicar, diferenciar, identificar, aplicar, evaluar, articular), como requiere la estructura obligatoria.

Razón del cambio: los verbos de acción permiten verificar el aprendizaje. Las preguntas abiertas no definen qué nivel de comprensión se espera.

---

### 2.2 Introducción narrativa

**v0.1:** 5 oraciones cortas, sin ganchos narrativos.
**v0.5:** 3 párrafos que conectan el origen filosófico (Aristóteles, Leibniz, Turing) con la implicación práctica para el lector. El gancho inicial es explícito: la respuesta popular ("para reemplazar personas") se califica como "históricamente incorrecta, conceptualmente imprecisa y profesionalmente peligrosa".

Razón del cambio: el lector debe tener un motivo para seguir leyendo. El contraste entre la creencia popular y la realidad histórica cumple esa función.

---

### 2.3 Motivación del problema

**v0.1:** No existía como sección separada.
**v0.5:** Sección dedicada que articula el límite específico de la programación tradicional (describir mediante reglas lo que sabemos hacer pero no podemos articular). Introduce el problema técnico antes que la solución.

Razón del cambio: la estructura obligatoria exige esta sección. Además, sin ella, el lector no entiende por qué existe la distinción entre automatización e IA.

---

### 2.4 Desarrollo conceptual: el espectro en tres niveles

**v0.1:** Dos párrafos sobre automatización vs. inteligencia con ejemplos del reloj y termostato.
**v0.5:** Tres niveles de análisis detallados:
- Nivel 1: Automatización determinista (con 4 ejemplos y criterio definitorio).
- Nivel 2: Programación basada en reglas con complejidad media (con 3 ejemplos y análisis del límite).
- Nivel 3: Machine Learning (ML) y LLMs (con 3 ejemplos y criterio definitorio).
- Cierre con el espectro como herramienta de diagnóstico (3 preguntas de clasificación).

Razón del cambio: la instrucción explícita en el brief pedía "al menos 3 niveles de análisis" en la distinción automatización vs. inteligencia.

---

### 2.5 Motivaciones originales de la IA

**v0.1:** Tres ítems en una lista (comprendernos, resolver problemas, ampliar capacidades).
**v0.5:** Las mismas tres motivaciones expandidas como párrafos narrativos, con mayor profundidad en cada una. Se agrega la paradoja de que la IA ayudó a comprender mejor la cognición humana.

---

## 3. Qué se agregó nuevo

### 3.1 Sección de Analogía formal

La analogía del sommelier es nueva en v0.5. No existía en v0.1.

**Analogía usada:** El sommelier conoce el maridaje vino-comida pero no puede articular completamente las reglas que sigue. Ese tipo de conocimiento implícito, que existe pero no puede formalizarse, es exactamente el tipo de problema para el que fue diseñado el ML.

**Por qué esta analogía:** Cumple los tres criterios del STYLE_GUIDE (breve, aclara sin simplificar en exceso, no reemplaza la explicación técnica). Además, el sommelier es universalmente familiar para el público objetivo (profesionales de tecnología) y no introduce jerga del campo.

**Contraste adicional:** Se agrega la distinción "termostato vs. sommelier" para anclar los dos extremos del espectro en imágenes concretas.

---

### 3.2 Diagrama Mermaid

En v0.1 no existía ningún diagrama.

**Diagrama creado:** Flowchart de decisión que recorre el espectro completo: desde el problema inicial hasta la clasificación en automatización determinista, motor de reglas, ML clásico, LLM y deep learning. Incluye las características de cada nivel (confiabilidad, costo, interpretabilidad) como nodos terminales con colores diferenciados (verde = bajo costo/alta confiabilidad, amarillo = complejidad media, rojo = alta complejidad/costo).

**Concepto central explicado:** El criterio de decisión entre niveles del espectro.

**Nota editorial:** El diagrama incluye una leyenda de colores al pie. Esto es necesario porque el formato Mermaid no permite leyendas nativas; la leyenda en texto evita ambigüedad.

---

### 3.3 Ejemplo real expandido: Meridian S.A.

**v0.1:** Tres casos sin nombre, sin contexto empresarial, sin análisis de la decisión.
**v0.5:** Empresa ficticia con nombre realista (Soluciones Empresariales Meridian S.A.), contexto (800 empleados, servicios financieros, 3 países), mandato directivo ("adoptar IA"), y tres proyectos con:
- Diagnóstico del arquitecto.
- Razonamiento detrás de la decisión.
- Resultado (incluyendo un caso donde se decide NO usar IA).

**Por qué este enfoque:** El lector del libro es un profesional técnico. Los casos anónimos no anclan en la realidad organizacional. Un contexto empresarial concreto activa el reconocimiento de patrones ("esto me pasa a mí").

---

### 3.4 Conversación con un arquitecto expandida

**v0.1:** 1 intercambio (gerente dice "necesitamos IA", arquitecto pregunta "¿qué problema?").
**v0.5:** 5 intercambios que desarrollan un diálogo completo:
- El gerente presenta el mandato vago ("adoptar IA").
- El arquitecto pregunta por el problema concreto.
- El gerente describe síntomas, no el problema (eficiencia, costos, experiencia de cliente).
- El arquitecto reformula para llegar al problema específico (reclamos por demoras).
- El gerente da datos concretos (300/día, 70% tracking, 30% complejos).
- El arquitecto descompone en dos proyectos con niveles de complejidad distintos.
- El gerente reconoce que la propuesta tiene más sentido que la del proveedor anterior.
- El arquitecto articula el principio ("el objetivo no es maximizar el uso de IA").

**Empresa ficticia usada:** Empresa de logística (sin nombre), con datos concretos de volumen.

---

### 3.5 Errores frecuentes

**v0.1:** No existía esta sección.
**v0.5:** Cuatro errores detallados:
1. Llamar IA a cualquier sistema automático (con consecuencias específicas de usar el término incorrectamente).
2. Comenzar por la herramienta, no por el problema (con análisis del costo real).
3. Creer que la IA reemplaza la infraestructura existente (con ejemplos de falsas propuestas de reemplazo).
4. Ignorar el costo de los datos (con las preguntas concretas que deben hacerse antes de proponer ML).

---

### 3.6 Buenas prácticas

**v0.1:** 5 puntos en lista ("Lo que un arquitecto debería recordar"), sin desarrollo.
**v0.5:** 6 buenas prácticas accionables con desarrollo:
1. Articular el problema en una sola oración antes de evaluar soluciones.
2. Aplicar el principio del mínimo sistema viable.
3. Separar el componente de IA del resto del sistema.
4. Documentar el criterio de decisión.
5. Planificar el monitoreo desde el diseño.
6. Tratar la elección de la herramienta como reversible.

---

### 3.7 Laboratorio estructurado completo

**v0.1:** Un ejercicio de 4 preguntas sobre sistemas cotidianos, sin estructura formal.
**v0.5:** Laboratorio completo con todos los elementos requeridos por la estructura obligatoria:
- Objetivo
- Nivel
- Tiempo estimado (90 minutos)
- Prerrequisitos
- Herramientas
- Escenario: TalentFlow S.A. con 5 iniciativas empresariales
- 5 pasos detallados (incluyendo uso de un LLM real para contraste)
- Tabla de clasificación
- Validación (3 preguntas de cierre)
- Reflexión (3 preguntas)
- 3 desafíos opcionales

**Por qué el paso 5 incluye uso de un LLM:** El capítulo habla sobre LLMs. Que el lector lo use para analizar el mismo problema que acaba de analizar él crea una experiencia de aprendizaje directa y contrasta las capacidades del modelo con las del criterio propio del lector.

---

### 3.8 Preguntas de reflexión

**v0.1:** No existía esta sección formalmente.
**v0.5:** 7 preguntas que cubren:
- Precisión conceptual (qué es IA vs. automatización).
- Relevancia histórica del campo para decisiones actuales.
- Límites epistemológicos de los LLMs (producir texto coherente no es razonar).
- Responsabilidad profesional ante pedidos que no justifican IA.
- Restricciones de datos en ML.
- Consideraciones éticas (sesgo en sistemas de RR.HH.).
- El límite entre ampliar y desplazar capacidades humanas.

---

### 3.9 Checklist del capítulo

**v0.1:** No existía.
**v0.5:** 7 ítems verificables en formato de casilla, alineados con los objetivos de aprendizaje.

---

### 3.10 Glosario breve

**v0.1:** No existía.
**v0.5:** 8 términos definidos en una línea:
- Automatización determinista
- Inteligencia Artificial (IA)
- Machine Learning (ML)
- Large Language Model (LLM)
- Motor de reglas
- Comportamiento probabilístico
- Alucinación (en LLMs)
- Sesgo en modelos de ML

---

## 4. Observaciones editoriales

### 4.1 Tono y voz

El capítulo mantiene el tono definido en STYLE_GUIDE: profesional, conversacional, técnicamente riguroso. Las secciones de análisis son directas; las secciones narrativas (introducción, analogía, conversación) tienen un ritmo diferente que refleja la "conversación con un arquitecto experimentado".

Se evitaron las frases prohibidas en todo el documento. No aparece "la IA piensa", "la IA entiende", "el modelo sabe", "el modelo tiene conciencia".

---

### 4.2 Coherencia con el Capítulo 1

El capítulo abre con "Después de preguntarnos qué entendemos por inteligencia", lo que asume que el Capítulo 1 trató ese tema. Esta continuidad narrativa está alineada con la v0.1 original. En la v0.5 se mantiene ese vínculo pero se fortalece con la referencia a "que el punto de partida siempre es el problema, nunca la herramienta", que es el hilo conductor del módulo.

---

### 4.3 Preparación del Capítulo 3

El capítulo cierra preparando al lector para el Capítulo 3 (Historia de la IA) con una promesa narrativa: la historia no es una línea de tiempo triunfal sino una sucesión de problemas y fracasos que abrieron caminos. Esa promesa establece expectativas correctas y mantiene la tensión narrativa del libro.

---

### 4.4 Extensión

La v0.5 es significativamente más extensa que la v0.1. Eso es consistente con la definición del estado v0.5 en el EDITORIAL_GUIDE ("revisión conceptual"). La extensión está justificada por la profundidad del tratamiento de cada concepto y la incorporación de todos los elementos de la estructura obligatoria.

---

### 4.5 Elementos que podrían revisarse en v0.8

- La tabla del laboratorio (Paso 2) podría beneficiarse de una versión pre-completada con uno o dos ejemplos para guiar al lector.
- El diagrama Mermaid podría simplificarse si el renderizado en el contexto de publicación no soporta los colores de fondo (fill). Una versión alternativa sin estilos de nodo podría prepararse como fallback.
- La analogía del sommelier funciona bien para un público general, pero podría no resonar en todos los contextos culturales. Una analogía alternativa podría ser un médico que diagnostica por experiencia clínica (patrón que conoce de ver miles de casos pero que no puede articular como un algoritmo de decisión).
- Las preguntas de reflexión 6 y 7 rozan temas éticos y sociotécnicos que merecerían un capítulo propio. En v0.8 puede ser útil agregar una nota que indique en qué capítulo futuro se desarrollan esos temas.

---

## 5. Resumen de cambios cuantitativos

| Elemento | v0.1 | v0.5 |
|---|---|---|
| Secciones | 8 | 17 |
| Objetivos de aprendizaje | 5 (preguntas) | 6 (verbos de acción) |
| Intercambios en diálogo | 1 | 5 |
| Casos empresariales | 3 (sin nombre) | 3 (Meridian) + 5 (TalentFlow) |
| Errores frecuentes | 0 | 4 |
| Buenas prácticas | 5 (lista) | 6 (con desarrollo) |
| Diagramas | 0 | 1 (Mermaid) |
| Analogías formales | 0 | 1 (sommelier) |
| Pasos de laboratorio | 4 preguntas | 5 pasos + validación + reflexión + desafíos |
| Preguntas de reflexión | 0 | 7 |
| Glosario | 0 | 8 términos |
| Checklist | 0 | 7 ítems |
