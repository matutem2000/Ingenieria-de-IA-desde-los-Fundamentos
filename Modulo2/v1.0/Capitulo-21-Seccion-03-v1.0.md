# Módulo 2 — Prompt Engineering Profesional

# Capítulo 21 — Laboratorios de Prompt Engineering

## Sección 03 — Laboratorio de Extracción Estructurada

> *"La verdadera utilidad de un modelo no reside únicamente en generar texto. Reside en transformar información desestructurada en datos utilizables por otros sistemas."*

---

## Objetivos de aprendizaje

- Diseñar prompts para extracción estructurada de información.
- Comprender la importancia de formatos de salida consistentes.
- Aplicar criterios de validación sobre datos generados por un LLM.
- Incorporar prácticas de ingeniería orientadas a la integración con aplicaciones empresariales.

---

## Introducción

Uno de los usos más frecuentes de los Large Language Models (LLM) consiste en convertir información escrita en lenguaje natural en estructuras que puedan ser procesadas automáticamente. Correos electrónicos, documentos, contratos, expedientes o conversaciones contienen gran cantidad de información útil, pero difícil de utilizar directamente desde una aplicación.

A diferencia del laboratorio anterior, donde el objetivo era asignar una categoría, aquí el desafío consiste en extraer múltiples campos de forma precisa y devolverlos en un formato estable que otro sistema pueda consumir sin procesamiento adicional.

---

## El problema

Una organización recibe solicitudes por correo electrónico para registrar incidentes técnicos. Cada mensaje debe transformarse en un registro con la siguiente información:

- nombre del solicitante;
- área responsable;
- prioridad;
- descripción resumida;
- fecha estimada del incidente.

La salida será utilizada directamente por un sistema de gestión de tickets, sin edición humana intermedia.

---

## Estrategia de resolución

```mermaid
flowchart LR
A[Correo electrónico]
--> B[Prompt de extracción]
--> C[Validación]
--> D[Estructura normalizada]
--> E[Sistema de tickets]
```

El éxito del laboratorio no depende únicamente de identificar la información correcta, sino también de producir un formato consistente en todas las ejecuciones. La salida del modelo requiere validación externa antes de ser consumida: incluso un prompt bien diseñado puede producir variaciones en los nombres de campos o en el orden de los datos cuando el mensaje de entrada es ambiguo o incompleto.

---

## Casos de prueba

El conjunto de evaluación debe incluir escenarios que representen la variedad de entradas reales:

| Tipo de caso | Objetivo |
|--------------|----------|
| Información completa | Validar el comportamiento esperado. |
| Datos faltantes | Verificar el manejo de valores ausentes. |
| Información contradictoria | Evaluar las reglas de prioridad. |
| Mensajes extensos | Analizar la capacidad de síntesis. |
| Formato irregular | Comprobar robustez frente a entradas reales. |

Estos escenarios permiten identificar limitaciones antes del despliegue. Los casos con datos faltantes o información contradictoria suelen ser los más reveladores: exponen cómo el prompt gestiona la incertidumbre y si genera valores inventados cuando la información no está presente.

---

## Criterios de evaluación

La calidad del prompt puede medirse considerando:

- **Exactitud de los campos extraídos**: porcentaje de campos correctamente identificados sobre el total esperado.
- **Estabilidad del formato**: las respuestas respetan de forma consistente la estructura definida en el prompt.
- **Porcentaje de información omitida**: campos requeridos que el modelo no extrae, ya sea porque no están presentes en el mensaje o porque el prompt no los solicita con suficiente precisión.
- **Necesidad de intervención humana posterior**: número de registros que requieren corrección manual antes de ser procesados.
- **Facilidad de integración con aplicaciones consumidoras**: cantidad de transformaciones necesarias sobre la salida antes de poder utilizarla, como pasos de parseo, normalización de nombres o reordenamiento de campos.

No siempre el prompt más detallado produce el mejor resultado. La simplicidad y la consistencia suelen ser los factores determinantes para la integración con otros sistemas.

---

## Caso de estudio

Durante las primeras pruebas, el modelo identifica correctamente los datos principales, pero utiliza distintos nombres para el mismo campo según el mensaje de entrada —"solicitante", "remitente" y "nombre del usuario" para referirse al mismo dato— y altera el orden de la salida entre ejecuciones.

El sistema de tickets espera siempre los mismos nombres de campo en el mismo orden. Cuando el prompt no los especifica, el model produce una salida semánticamente correcta pero estructuralmente inestable.

En lugar de modificar la lógica de la aplicación consumidora para adaptarse a la variabilidad del modelo, el equipo ajusta el prompt: define explícitamente los nombres exactos de cada campo y establece el orden en que deben aparecer en la salida. Como consecuencia, la complejidad del procesamiento posterior disminuye significativamente.

Este caso ilustra un principio fundamental: el Prompt Engineering no impacta solo sobre la calidad del contenido generado, sino también sobre la arquitectura del software que lo consume. Un prompt que produce una estructura estable reduce el acoplamiento entre el modelo y los sistemas integrados.

---

## Buenas prácticas

- Definir claramente el formato esperado en el prompt, incluyendo los nombres exactos de los campos y el orden en que deben aparecer.
- Mantener nombres de campos consistentes entre todas las versiones del prompt.
- Validar la salida del modelo antes de consumirla, verificando que todos los campos requeridos estén presentes y con el formato correcto.
- Diseñar prompts pensando en los sistemas que utilizarán la información: cada decisión de formato tiene consecuencias sobre la integración.
- Especificar explícitamente cómo manejar datos ausentes: si el campo no está en el mensaje, el modelo debe indicarlo con un valor convenido (por ejemplo, `null` o `"No especificado"`).

---

## Errores frecuentes

- Permitir formatos variables, delegando al modelo la decisión de cómo presentar la información.
- Mezclar información extraída con texto explicativo o comentarios del modelo en la misma respuesta.
- No contemplar el manejo de datos ausentes, lo que puede llevar al modelo a inventar valores.
- Acoplar el procesamiento posterior a respuestas impredecibles, trasladando la variabilidad del prompt hacia la lógica de la aplicación.

---

## Ideas clave

- La extracción estructurada es uno de los casos de uso más importantes del Prompt Engineering en aplicaciones empresariales.
- La estabilidad del formato es tan importante como la calidad de la extracción: una respuesta correcta con formato inestable no es utilizable.
- Diseñar pensando en la integración simplifica toda la arquitectura del sistema.

---

## Transición hacia la siguiente sección

En la próxima sección desarrollamos un laboratorio centrado en generación controlada de contenido, donde el objetivo consiste en producir respuestas consistentes respetando restricciones de estilo, longitud, formato y políticas organizacionales.
