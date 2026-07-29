# Módulo 4 – Capítulo 02 – Sección 02

## Arquitectura Monolítica

La arquitectura monolítica tiene mala reputación en el ecosistema tecnológico contemporáneo, asociada en el imaginario colectivo con sistemas heredados, lentos y difíciles de mantener. Esa reputación es injusta y, en muchos contextos de sistemas de IA, directamente contraproducente. Entender cuándo un monolito es la decisión correcta — y cuándo deja de serlo — es una de las competencias más prácticas de un arquitecto.

Un monolito es una aplicación en la que todos los componentes del sistema se despliegan como una unidad única. El pipeline de ingesta de documentos, la lógica de recuperación, el servicio de inferencia, la autenticación y la interfaz de usuario viven en el mismo proceso, en el mismo servidor y se despliegan juntos. Esa unidad produce una lista de beneficios concretos que los sistemas más complejos no tienen.

**Beneficios del monolito para sistemas de IA:**

- **Simplicidad operativa:** un único proceso para monitorear, desplegar y escalar. No hay comunicación de red entre servicios, no hay problemas de consistencia entre versiones de distintos componentes, no hay latencia adicional por llamadas entre servicios.
- **Velocidad de iteración:** los cambios en cualquier parte del sistema se despliegan en una única operación. En un producto de IA en fase de validación de mercado, donde el equipo modifica la estrategia de prompting, los criterios de retrieval y la lógica de negocio varias veces por semana, la simplicidad del ciclo de despliegue tiene un valor real.
- **Coherencia de datos:** todos los componentes acceden a las mismas bases de datos, con las mismas credenciales y las mismas reglas de consistencia. No hay sincronización entre bases de datos de servicios distintos.
- **Observabilidad unificada:** todos los logs, trazas y métricas comparten el mismo contexto de ejecución. El debugging de un flujo completo — desde la solicitud del usuario hasta la respuesta del modelo — no requiere correlacionar trazas entre múltiples servicios.

**Limitaciones del monolito:**

- **Escalabilidad no granular:** si el servicio de inferencia requiere GPU y el servicio de autenticación no, ambos deben desplegarse en el mismo servidor, lo que implica pagar por GPU también para los componentes que no la necesitan.
- **Acoplamiento involuntario:** sin fronteras de servicio explícitas, los equipos tienden a crear dependencias no intencionales entre módulos, haciendo que el sistema sea progresivamente más difícil de modificar.
- **Despliegues totales:** cualquier cambio, por pequeño que sea, requiere redesplegar el sistema completo, lo que incrementa el riesgo de cada despliegue.
- **Punto único de fallo:** un error en cualquier componente puede afectar la disponibilidad de todo el sistema.

**Casos de uso donde el monolito es la elección correcta:**

- MVP o producto en validación de mercado con menos de 50 usuarios activos.
- Equipo de desarrollo pequeño (1-5 personas) sin experiencia operativa en sistemas distribuidos.
- Presupuesto limitado que no justifica la complejidad operativa de múltiples servicios.
- Sistema de IA interno con carga predecible y baja, como un asistente de documentación para uso del equipo de ingeniería.

El patrón que sugiere comenzar con un monolito y extraer servicios cuando sea necesario ("Modular Monolith") es una estrategia arquitectónica reconocida y respetada. Sam Newman, autor de *Building Microservices*, recomienda explícitamente comenzar con un monolito para sistemas nuevos, porque los límites del servicio se descubren operando el sistema, no en una reunión de diseño inicial.

> **Nota del Arquitecto:** El error más común que cometen los equipos con experiencia en microservicios es aplicar ese patrón a un sistema nuevo desde el primer día, convencidos de que es la "mejor práctica". El resultado habitual es un sistema distribuido en el que la complejidad operativa supera la capacidad del equipo, los servicios están mal divididos porque los límites del dominio no estaban claros, y la velocidad de desarrollo es una fracción de lo que sería con un monolito bien estructurado.

La transición del monolito al sistema distribuido debe estar motivada por necesidades reales: escalado diferencial de componentes, equipos independientes que necesitan ciclos de despliegue autónomos, o requisitos de resiliencia que el monolito no puede satisfacer. La siguiente sección examina el patrón al que ese monolito eventualmente puede evolucionar: microservicios e IA.
