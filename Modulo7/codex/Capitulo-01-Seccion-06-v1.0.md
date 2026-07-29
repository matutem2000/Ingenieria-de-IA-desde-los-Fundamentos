# Módulo 7 – Capítulo 01 – Sección 06

# Cierre: un agente no es un LLM con herramientas — es un sistema con autonomía acotada

La distinción conceptual más importante del capítulo es que un agente de IA no se define por tener acceso a herramientas, sino por operar con autonomía acotada: toma decisiones secuenciales de forma independiente dentro de límites establecidos por el diseñador (scope de herramientas, límites de iteración, condiciones de parada, políticas de escalado a humanos). Agregar function calling a un LLM sin un bucle de control explícito, sin gestión de estado y sin criterios de terminación produce un sistema frágil que parece un agente pero no lo es: cualquier fallo de herramienta lo deja sin capacidad de recuperación. La verdadera ingeniería agéntica está en definir con precisión qué puede y qué no puede hacer el agente, asegurar que sus acciones sean observables y auditables, y diseñar mecanismos de fallback que mantengan al sistema en estados seguros ante fallos imprevistos. Un agente confiable es el resultado de decisiones de diseño explícitas sobre autonomía, no de dar acceso irrestricto a herramientas.

## Para recordar

La autonomía de un agente no se mide por la cantidad de herramientas a las que tiene acceso, sino por la calidad de las decisiones que toma de forma independiente dentro de los límites que el ingeniero ha definido con precisión.

*"The key question is not whether machines can think, but whether they can be designed to behave appropriately in situations their designers did not anticipate."* — Stuart Russell, "Human Compatible: Artificial Intelligence and the Problem of Control" (2019)
