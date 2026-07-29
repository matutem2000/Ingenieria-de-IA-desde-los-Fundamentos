# Módulo 5 – Capítulo 05 – Sección 01

# El desafío de testear sistemas no deterministas: estrategias y restricciones

Los sistemas de IA basados en LLMs son no deterministas por naturaleza: dos ejecuciones del mismo prompt con temperatura > 0 pueden producir respuestas diferentes, ambas correctas, lo que invalida la estrategia de testing por igualdad exacta de string que funciona en software tradicional. Esta no-determinismo se manifiesta en tres capas: la variabilidad estocástica del modelo (misma entrada, diferentes tokens), la variabilidad de versiones del modelo (un proveedor actualiza silenciosamente el modelo sin cambiar el identificador), y la variabilidad del prompt (cambios menores en el texto pueden cambiar significativamente el comportamiento). La estrategia de testing para sistemas no deterministas se articula en: tests de propiedades en lugar de tests de igualdad (verificar que la respuesta contiene ciertos elementos o satisface ciertas condiciones), tests basados en LLM-as-judge (usar otro modelo para evaluar si la respuesta es correcta), y suites de evaluación con datasets de casos de prueba con respuestas esperadas o criterios de aceptación. Con `temperature=0` el modelo es casi determinista (seed fijo en OpenAI hace que sea reproducible), lo que permite tests exactos en un subconjunto de casos.

## Aspectos técnicos del testing no determinista

- Testing por propiedades: en lugar de `assert response == expected_string`, verificar `assert len(response) > 50`, `assert "precio" in response.lower()`, `assert json.loads(response)["category"] in VALID_CATEGORIES`; las propiedades son más robustas que la igualdad exacta
- Seeds para reproducibilidad: `seed=42` en OpenAI hace el sampling determinista cuando la infraestructura del modelo no cambia; útil para snapshots temporales pero frágil ante actualizaciones del modelo
- Evaluación basada en criterios: definir criterios de calidad explícitos ("¿la respuesta menciona todos los elementos del contexto?", "¿la respuesta está en el idioma del usuario?") y verificarlos con regex, parsers o con un LLM-as-judge
- Umbral de pass/fail estadístico: para funcionalidades críticas, ejecutar el mismo caso de prueba N=10-20 veces y verificar que pasa al menos el X% de las veces (ej. 90%), en lugar de exigir el 100%
- Mocks del LLM para unit tests: usar respuestas ficticias predefinidas en lugar del LLM real en tests unitarios, para testear la lógica de parsing, validación y manejo de errores sin incurrir en latencia ni costo de API

## Principio rector

El objetivo del testing en sistemas de IA no es verificar que la respuesta es exactamente la esperada, sino verificar que satisface los criterios de calidad del negocio con suficiente consistencia estadística bajo condiciones controladas.
