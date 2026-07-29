# Módulo 7 – Capítulo 02 – Sección 05

# Verificación y autocorrección: el agente evalúa sus propios pasos

La autocorrección agéntica es la capacidad del sistema para detectar errores en sus propios pasos intermedios y corregirlos antes de continuar, sin intervención humana. Este patrón puede implementarse mediante un LLM critic separado (LLM-as-judge) que evalúa la salida del agente ejecutor, mediante self-consistency (generar múltiples respuestas y elegir la más frecuente), o mediante reflexión explícita donde el mismo agente revisa su trabajo con un prompt de evaluación diferenciado. En LangGraph, la autocorrección se implementa añadiendo un nodo evaluador después de cada acción crítica, con una arista condicional que redirige al agente a un nodo de corrección si el evaluador detecta un error. La limitación fundamental de la autocorrección basada en LLM es que el modelo puede cometer el mismo error tanto en la generación como en la evaluación; la corrección es más efectiva cuando involucra verificación externa (ejecutar el código generado, validar el JSON contra un schema, verificar URLs devueltas).

## Puntos críticos

- **Self-consistency**: generar k respuestas independientes (k=3-10) para el mismo problema y aplicar majority voting; efectivo para problemas con respuesta única discreta pero costoso en tokens y latencia
- **LLM-as-judge**: usar un segundo prompt (o segundo modelo) para evaluar la calidad de la respuesta del agente; el juez puede ser el mismo modelo con un prompt de evaluación o un modelo especializado (GPT-4o como judge para outputs de modelos menores)
- **Reflection pattern**: el agente genera su respuesta, luego se le pide que identifique posibles errores y se corrige a sí mismo; mejora resultados en 10-30% en tareas de codificación y razonamiento matemático
- **Verificación externa**: la corrección más confiable es ejecutar la acción y verificar el resultado contra criterios programáticos (el código compila y pasa tests, el JSON valida contra schema, la URL devuelve HTTP 200)
- **Límite de intentos de corrección**: la autocorrección sin límite puede generar bucles donde el agente corrige indefinidamente sin mejorar; establecer max_retries=3 y escalar a humano si se supera

## Buena práctica

Priorizar verificación externa sobre autocorrección por LLM siempre que sea posible: ejecutar el resultado en un sandbox es una verificación de verdad objetiva, mientras que la autocorrección por LLM es solo otra inferencia probabilística sujeta a los mismos sesgos del modelo.
