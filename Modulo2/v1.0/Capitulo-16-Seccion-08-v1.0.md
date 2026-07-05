# Módulo 2 — Prompt Engineering Profesional

# Capítulo 16 — Ingeniería del Prompt

## Sección 8 — Evaluación de prompts

> *"Todo componente de software se prueba. Un prompt profesional no debería ser la excepción."*

---

## Objetivos de aprendizaje

- Comprender por qué un prompt debe evaluarse sistemáticamente.
- Diferenciar pruebas informales de evaluación de ingeniería.
- Introducir métricas para medir la calidad de un prompt.
- Establecer las bases metodológicas de la evaluación como práctica de PromptOps.

---

## Introducción

Diseñar un buen prompt constituye únicamente la primera etapa del proceso.

Una vez construido, debe responder una pregunta fundamental:

**¿Cumple realmente con el objetivo para el cual fue diseñado?**

En aplicaciones personales esta validación suele realizarse de manera intuitiva. El usuario formula algunas consultas y decide, según su percepción, si el resultado es satisfactorio.

Ese enfoque resulta insuficiente cuando el prompt forma parte de una solución empresarial.

En un entorno de producción, cada modificación puede afectar miles de respuestas, procesos automatizados o decisiones críticas. Por ese motivo, el Prompt Engineering incorpora prácticas de evaluación similares a las utilizadas en la ingeniería de software.

---

## ¿Qué significa evaluar un prompt?

Evaluar un prompt consiste en comprobar de forma repetible que produce resultados alineados con los requisitos del negocio.

La evaluación debe responder preguntas como:

- ¿Las respuestas son correctas?
- ¿Son consistentes ante consultas similares?
- ¿Respetan las restricciones definidas?
- ¿Mantienen el formato esperado?
- ¿Continúan siendo válidas después de modificar el prompt?

```mermaid
flowchart LR
A[Prompt] --> B[Conjunto de pruebas]
B --> C[LLM]
C --> D[Resultados]
D --> E[Métricas]
E --> F[Decisión]
```

---

## El conjunto de casos de prueba

Antes de medir, es necesario construir el conjunto de casos sobre el cual se medirá.

Un conjunto representativo incluye al menos tres tipos de consultas:

- **Casos típicos**: las consultas más frecuentes que el sistema recibirá en producción.
- **Casos de borde**: entradas inusuales, incompletas o ambiguas que ponen a prueba las restricciones del prompt.
- **Casos adversariales**: entradas que podrían llevar al modelo a ignorar restricciones o a generar respuestas fuera del dominio definido.

Para cada caso debe definirse un criterio de aceptación: no necesariamente la respuesta exacta esperada, sino las condiciones que debe cumplir la respuesta para considerarse correcta. Este criterio es el que permite comparar versiones del prompt de manera objetiva.

---

## Métricas iniciales

Aunque cada organización definirá sus propios indicadores, existen métricas comunes.

| Métrica | Objetivo |
|---------|----------|
| Precisión | Verificar la corrección de las respuestas. |
| Consistencia | Medir estabilidad entre ejecuciones. |
| Cumplimiento | Confirmar que respeta las restricciones. |
| Formato | Validar la estructura de salida. |
| Cobertura | Evaluar distintos tipos de consultas. |

Estas métricas miden el comportamiento del sistema prompt+modelo. Cuando una métrica falla, conviene aislar la causa: si el problema desaparece al modificar el prompt con el mismo modelo, el error estaba en el diseño del prompt; si persiste con distintas formulaciones del prompt, puede ser una limitación del modelo en sí. Esa distinción es parte del criterio que el arquitecto debe desarrollar.

---

## Automatización de la evaluación

La recomendación de "automatizar las evaluaciones siempre que sea posible" merece una aclaración.

Cuando las salidas son datos estructurados —JSON con campos definidos, tablas, listas con formato fijo—, la automatización puede basarse en validación de esquema o comparación con valores esperados.

Cuando las salidas son texto en lenguaje natural, la automatización requiere un enfoque diferente. No es posible comparar la respuesta con una cadena exacta, porque las respuestas correctas admiten múltiples formulaciones. En esos casos la automatización puede basarse en criterios de aceptación verificables (¿la respuesta contiene las secciones requeridas?, ¿cita la fuente cuando se le pide?), en checklists de requisitos, o en el uso de un segundo LLM que actúa como evaluador siguiendo los criterios definidos. El principio es siempre el mismo: reemplazar la percepción subjetiva por una comparación objetiva y repetible.

---

## Caso de estudio

Un equipo modifica el prompt de un asistente financiero para obtener respuestas más breves.

La nueva versión parece mejorar las pruebas manuales.

Sin embargo, al ejecutar una batería de cien consultas representativas —que incluye casos típicos, de borde y adversariales—, se observa que disminuye la precisión en operaciones complejas y aumenta el número de respuestas incompletas.

Gracias a la evaluación sistemática, el equipo detecta el problema antes del despliegue en producción y revierte la modificación hasta encontrar un ajuste que mejore la brevedad sin sacrificar precisión.

---

## Buenas prácticas

- Definir un conjunto estable de casos de prueba que incluya casos típicos, de borde y adversariales.
- Definir criterios de aceptación para cada caso antes de ejecutar las pruebas.
- Comparar versiones utilizando las mismas consultas y los mismos criterios.
- Registrar resultados y métricas para cada versión evaluada.
- Automatizar las evaluaciones en la medida en que el tipo de salida lo permita.

---

## Errores frecuentes

- Evaluar únicamente ejemplos exitosos o conocidos de antemano.
- Cambiar varias variables del prompt al mismo tiempo, lo que impide aislar la causa de los cambios en las métricas.
- Confiar exclusivamente en la percepción subjetiva sin criterios objetivos.
- No conservar el historial de versiones evaluadas y sus resultados.

---

## Ideas clave

- Un prompt profesional debe poder medirse con criterios objetivos y repetibles.
- La evaluación reduce el riesgo de regresiones cuando el prompt evoluciona.
- La calidad surge de un proceso sistemático, no de impresiones aisladas.

---

## Transición hacia la siguiente sección

La evaluación produce evidencia. El versionado convierte esa evidencia en trazabilidad. En la próxima sección estudiaremos cómo gestionar la evolución de un prompt de manera controlada dentro del ciclo de vida de una aplicación empresarial.
