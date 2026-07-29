# Módulo 7 – Capítulo 08 – Sección 06

# Cierre: la autonomía de un agente debe ser proporcional a la confianza que inspira

La seguridad en sistemas agénticos no es un conjunto de patches que se aplican después de que el sistema está construido; es una dimensión de diseño que determina qué puede hacer el agente, cómo se lo autorizamos y qué sucede cuando algo sale mal. La autonomía de un agente —su capacidad de actuar sin intervención humana— es una deuda de confianza que se acumula iteración por iteración: cada vez que el agente demuestra comportamiento correcto en escenarios de riesgo, la confianza justificada crece y la necesidad de confirmación humana puede reducirse. Pero esa confianza no puede darse a priori solo porque el sistema funciona en demos o en tests con inputs benignos; debe ganarse en producción con observabilidad completa de cada acción, con mecanismos de reversión de las acciones incorrectas, y con limits claros sobre qué acciones nunca deben ejecutarse de forma autónoma sin importar cuánta confianza inspire el agente. La seguridad agéntica es un proceso continuo, no un estado final.

## Para recordar

Un agente con autonomía irrestricta en un sistema de producción es un riesgo operacional; un agente con autonomía proporcional a su historial de comportamiento verificado es un sistema confiable.

*"Security is always excessive until it's not enough."* — Robbie Sinclair, Head of Security at Country Energy; aplicado a sistemas agénticos: las restricciones de autonomía que parecen excesivas en el diseño son las que previenen los incidentes que no debería ocurrir en producción.
