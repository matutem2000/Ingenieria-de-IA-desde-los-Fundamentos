# Módulo 7 – Capítulo 07 – Sección 01

# El desafío de testear agentes: no-determinismo, cadenas largas y efectos secundarios

Testear agentes de IA presenta desafíos cualitativamente distintos a los del testing de software tradicional: los agentes son no-deterministas (el mismo input puede producir diferentes trayectorias de acciones en diferentes ejecuciones), operan en cadenas largas donde el espacio de estados intermedios es exponencialmente grande, y ejecutan acciones con efectos secundarios reales en el mundo (escritura en bases de datos, envío de emails, llamadas a APIs externas). Las técnicas estándar de unit testing —dado un input X, el output es siempre Y— fallan ante el no-determinismo: con temperatura > 0, el LLM puede elegir diferentes herramientas o diferentes argumentos en ejecuciones distintas. Esto requiere un cambio de paradigma en el testing de agentes: en lugar de verificar outputs exactos, se verifica que el comportamiento del agente cumple con propiedades especificables —usó la herramienta correcta, llegó al resultado correcto, no ejecutó acciones prohibidas— que pueden evaluarse con mayor tolerancia al no-determinismo.

## Conceptos clave

- **No-determinismo controlado**: usar `temperature=0` durante los tests para reducir la variabilidad y hacer los resultados más reproducibles; esto no elimina el no-determinismo completamente (el modelo puede cambiar entre versiones) pero lo reduce a niveles manejables para evaluación automatizada
- **Trayectoria vs output final**: en agentes, la calidad de la trayectoria (qué herramientas invocó, en qué orden, con qué argumentos) puede ser tan importante como el output final; testear ambas dimensiones de forma independiente
- **Mocking de herramientas**: reemplazar herramientas con efectos secundarios reales (escritura en DB, envío de emails) con mocks que registran las invocaciones y devuelven responses predefinidos; permite ejecutar tests en aislamiento sin efectos en producción
- **Idempotencia de tests**: los tests de agentes deben diseñarse para poder ejecutarse múltiples veces sin efectos acumulados; el entorno de test debe resetearse a un estado limpio antes de cada ejecución
- **Complejidad del espacio de estados**: con N herramientas y M pasos máximos, el número de trayectorias posibles es O(N^M); los tests no pueden ser exhaustivos y deben enfocarse en los caminos críticos y los casos de fallo más probables

## Principio rector

Testear agentes requiere evaluar comportamiento (¿actuó el agente correctamente dadas las circunstancias?) en lugar de verificar outputs (¿produjo exactamente este string?); este cambio de perspectiva es la diferencia entre encontrar bugs de comportamiento agéntico y perdérselos.
