# Módulo 10 – Capítulo 02 – Sección 06

# Cierre: una buena plataforma se percibe como un multiplicador de productividad, no como burocracia

El test definitivo del diseño de una plataforma de IA es simple: ¿los equipos la usan voluntariamente o la evitan siempre que pueden? Una plataforma que se percibe como burocracia tiene síntomas técnicos identificables: los ingenieros prefieren configurar su propio cluster de Kubernetes antes de aprender la API de la plataforma, crean instancias de EC2 directas para eludir el scheduler de jobs, o construyen sus propios wrappers de MLflow en lugar de usar el SDK interno. Cuando una plataforma funciona como multiplicador de productividad, en cambio, los tiempos de ciclo se reducen significativamente: un fine-tuning que antes requería tres días de configuración de infraestructura se lanza en 30 minutos, el proceso de despliegue que requería intervención del equipo de plataforma se completa de forma autónoma en menos de una hora, y los incidentes de producción relacionados con configuración incorrecta de infraestructura desaparecen de los postmortems. El diseño para la productividad implica decisiones técnicas concretas: CLIs con mensajes de error accionables (no "error 403"), documentación con ejemplos de código ejecutables, y ciclos de feedback de máximo 48 horas entre la solicitud de un feature y la respuesta del equipo de plataforma sobre su viabilidad.

## Indicadores de una plataforma que multiplica productividad

- Adoption rate superior al 80% de los equipos de AI Engineering elegible dentro de los primeros seis meses de un nuevo feature
- Time-to-first-deploy inferior a 4 horas para un nuevo equipo que se integra a la plataforma por primera vez
- Reduction in infrastructure-related postmortems: caída medible trimestre a trimestre en incidentes cuya causa raíz es configuración de infraestructura

## Para recordar

Una plataforma de IA bien diseñada hace que hacer las cosas bien sea más fácil que hacerlas mal: los guardrails técnicos y los golden paths deben ser el camino de menor resistencia, no obstáculos.

---

*"Any organization that designs a system will produce a design whose structure is a copy of the organization's communication structure."*
— Melvin Conway, ingeniero de software, formulador de la Ley de Conway (1967)
