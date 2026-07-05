# Capitulo-18-Seccion-04-v0.1

# Módulo 2 — Prompt Engineering Profesional

# Capítulo 18 — Prompt Engineering para Producción

**Versión:** 0.1  
**Estado:** Manuscrito del autor

> *"Si un prompt no puede probarse de manera sistemática, tampoco puede mejorarse de forma confiable."*

---

# Objetivos de aprendizaje

- Comprender cómo diseñar pruebas para prompts empresariales.
- Diferenciar pruebas exploratorias de pruebas sistemáticas.
- Introducir conjuntos de evaluación (*evaluation sets*).
- Establecer criterios objetivos de aceptación antes del despliegue.

---

# Introducción

En el desarrollo de software resulta impensable desplegar una aplicación sin algún tipo de validación.

El mismo principio debe aplicarse a los prompts.

Probar un prompt ejecutando unas pocas consultas manuales puede ser suficiente durante una etapa exploratoria, pero no alcanza para garantizar un comportamiento consistente en producción.

A medida que una solución evoluciona, también debe evolucionar su estrategia de pruebas.

---

# ¿Qué es una prueba de prompts?

Una prueba consiste en ejecutar un conjunto controlado de consultas sobre una versión específica del prompt y comparar los resultados obtenidos con criterios previamente definidos.

El objetivo no es demostrar que el prompt funciona, sino descubrir en qué condiciones deja de hacerlo.

```mermaid
flowchart LR
A[Prompt]
--> B[Conjunto de pruebas]
--> C[LLM]
--> D[Resultados]
--> E[Evaluación]
--> F[Aprobación o mejora]
```

---

# Construcción de un conjunto de evaluación

Un *evaluation set* debería incluir distintos tipos de consultas.

| Tipo de caso | Finalidad |
|--------------|-----------|
| Casos típicos | Validar el comportamiento esperado. |
| Casos límite | Detectar fallos en situaciones extremas. |
| Entradas ambiguas | Evaluar la robustez. |
| Datos incompletos | Verificar respuestas seguras. |
| Casos históricos | Evitar regresiones entre versiones. |

La diversidad del conjunto de pruebas resulta tan importante como su tamaño.

---

# Criterios de aceptación

Cada organización definirá sus propios indicadores, pero un proceso de evaluación suele responder preguntas como:

- ¿La respuesta es correcta?
- ¿Respeta las restricciones del prompt?
- ¿Mantiene el formato esperado?
- ¿Es consistente respecto de versiones anteriores?
- ¿Cumple los objetivos del negocio?

Estos criterios permiten tomar decisiones basadas en evidencia y no únicamente en impresiones subjetivas.

---

# Caso de estudio

Un equipo mantiene un asistente para interpretar expedientes administrativos.

Antes de desplegar una nueva versión del prompt ejecuta automáticamente quinientas consultas representativas.

El análisis muestra una mejora en la calidad de las respuestas generales, pero detecta una regresión en expedientes con múltiples anexos.

Gracias al conjunto de pruebas, el problema se identifica antes de afectar a los usuarios finales.

---

# Buenas prácticas

- Mantener un conjunto de pruebas estable y versionado.
- Incorporar nuevos casos cuando aparezcan incidentes.
- Automatizar la ejecución siempre que sea posible.
- Comparar resultados utilizando las mismas condiciones de inferencia.

---

# Errores frecuentes

- Validar únicamente ejemplos favorables.
- Cambiar el conjunto de pruebas en cada evaluación.
- No registrar los resultados obtenidos.
- Considerar suficiente una revisión manual.

---

# Ideas clave

- Un prompt debe someterse a pruebas repetibles.
- Los conjuntos de evaluación reducen el riesgo de regresiones.
- La calidad se demuestra mediante evidencia objetiva.

---

# Transición hacia la siguiente sección

En la próxima sección analizaremos cómo medir el desempeño de los prompts mediante métricas operativas y de negocio, incorporando observabilidad al ciclo de vida de una solución basada en IA.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
