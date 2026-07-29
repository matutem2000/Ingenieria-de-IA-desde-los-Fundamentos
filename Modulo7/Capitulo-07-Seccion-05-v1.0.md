# Módulo 7 – Capítulo 07 – Sección 05

# Pruebas de estrés: comportamiento bajo ambigüedad, herramientas rotas y bucles

Las pruebas de estrés de agentes verifican el comportamiento del sistema en condiciones adversas que no se presentan en los casos de prueba estándar: inputs ambiguos o contradictorios, herramientas que fallan con errores inesperados, bucles de razonamiento, y situaciones donde el agente no puede completar la tarea por limitaciones del entorno. Estos escenarios adversariales son los más importantes para validar la robustez de un agente en producción, porque en el mundo real los inputs son imperfectos, las APIs externas fallan, y los usuarios hacen preguntas ambiguas. El diseño de pruebas de estrés debe ser sistemático: crear categorías de adversarial inputs (ambigüedad semántica, instrucciones contradictorias, inputs malformados), categorías de fallos de herramientas (timeout, error 5xx, respuesta vacía, respuesta con formato incorrecto) y límites de iteración (¿qué hace el agente cuando alcanza max_steps sin completar la tarea?).

## Puntos críticos

- **Tests de ambigüedad**: inputs con información faltante, instrucciones vagas o múltiples interpretaciones posibles; verificar que el agente solicita clarificación cuando es apropiado en lugar de asumir y actuar sobre la interpretación incorrecta
- **Tests de herramientas rotas**: mockear herramientas para que devuelvan errores en momentos específicos de la cadena de ejecución; verificar que el agente aplica la política de retry correctamente, intenta alternativas cuando las hay y escala al humano o termina gracefully cuando no puede continuar
- **Tests de límite de iteraciones**: ejecutar el agente en tareas diseñadas para ser irresolubles en el número máximo de pasos; verificar que termina con un mensaje de error informativo en lugar de producir output parcial o quedar bloqueado
- **Tests de bucle**: diseñar scenarios donde el agente podría entrar en un bucle (la herramienta devuelve siempre el mismo resultado incorrecto, el razonamiento lleva de vuelta al mismo punto de partida); verificar que los mecanismos anti-bucle (detección de estados repetidos, límite de pasos) funcionan correctamente
- **Tests de prompt injection**: inputs que intentan redirigir al agente hacia objetivos diferentes al original; verificar que el agente mantiene su objetivo original incluso cuando el contenido procesado (páginas web, documentos, mensajes de herramientas) contiene instrucciones adversariales

## Para recordar

Un agente que solo funciona con inputs bien formados y herramientas perfectas no está listo para producción; las pruebas de estrés son el mecanismo que verifica que el agente falla de forma segura y predecible cuando el mundo real no coopera.
