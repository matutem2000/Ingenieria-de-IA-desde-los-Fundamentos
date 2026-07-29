# Módulo 7 – Capítulo 03 – Sección 03

# Diseño de herramientas: por qué la descripción importa tanto como la implementación

El diseño de herramientas para agentes es una forma de programación con lenguaje natural: el campo `description` de cada herramienta y de cada parámetro es el código que el LLM ejecuta internamente para decidir si esta herramienta es la apropiada, con qué argumentos llamarla y qué esperar de ella. Un error frecuente en la ingeniería de agentes es dedicar el 90% del tiempo a la implementación de la herramienta y el 10% a su descripción; en producción, la mayoría de los fallos de selección de herramientas provienen de descripciones ambiguas, incompletas o que no especifican los casos de no-uso. La descripción debe incluir: qué hace la herramienta en términos de efecto en el mundo, cuándo es apropiado usarla vs alternativas disponibles, qué formato de entrada espera para casos no triviales, y qué limitaciones tiene (número máximo de resultados, formatos de archivo soportados, límites de tamaño). Tests unitarios sobre la selección de herramientas —verificando que el agente elige la herramienta correcta dado un input específico— deben incluirse en la suite de evaluación desde el inicio del proyecto.

## Puntos críticos

- **Especificidad de la descripción**: descripciones vagas como "busca información" llevan a invocaciones erróneas; la descripción debe especificar la fuente, el tipo de dato retornado y el caso de uso exacto ("busca páginas web públicas en tiempo real; usa esto cuando necesites información actualizada después de tu fecha de entrenamiento")
- **Documentación de no-uso**: explicitar cuándo NO usar la herramienta es tan importante como cuándo usarla; "no uses esta herramienta si ya tienes la información en el contexto" previene llamadas innecesarias que aumentan latencia y costo
- **Descripciones de parámetros**: cada parámetro debe tener su propio campo `description` con el tipo de valor esperado, ejemplos concretos y restricciones de formato ("`date`: fecha en formato ISO 8601, ejemplo: '2024-03-15'")
- **Namespacing de herramientas**: cuando el agente tiene acceso a 10+ herramientas, agrupaciones semánticas en el nombre (`db_query`, `db_insert`, `db_update`) o uso de enum para el parámetro de tipo reducen la ambigüedad de selección
- **Evaluación de selección de herramientas**: construir un banco de 20-50 scenarios con la herramienta esperada y ejecutarlo regularmente contra nuevas versiones del agente o del modelo base; cambios de modelo pueden alterar el comportamiento de selección

## Buena práctica

Tratar las descripciones de herramientas como contratos de API: deben ser tan precisas, completas y sin ambigüedad como los docstrings de una función pública en una librería que usan otros desarrolladores.
