# Módulo 4 – Capítulo 02 – Sección 03

## Microservicios e IA

Cuando un sistema de IA crece en complejidad, en volumen de uso y en tamaño del equipo de desarrollo, las limitaciones del monolito se vuelven obstáculos concretos. El servicio de inferencia necesita escalar de forma independiente del servicio de negocio. El equipo de ML necesita desplegar cambios en el pipeline de RAG sin esperar al ciclo de despliegue del equipo de frontend. El servicio de embeddings necesita ejecutarse en hardware con GPU mientras el servicio de autenticación no. Es en ese momento cuando la arquitectura de microservicios comienza a producir valor real, no antes.

En una arquitectura de microservicios aplicada a sistemas de IA, los componentes del sistema se organizan en servicios independientes con fronteras bien definidas, contratos de API estables y ciclos de despliegue autónomos. Una configuración típica para un sistema RAG productivo puede incluir un servicio de ingesta responsable de procesar documentos nuevos o actualizados, un servicio de retrieval que opera sobre la base vectorial, un servicio de inferencia que gestiona las llamadas al modelo de lenguaje, un servicio de composición de contexto que combina el resultado del retrieval con la solicitud del usuario, y un API gateway que autentica las solicitudes y las enruta hacia el servicio correspondiente.

**Beneficios de los microservicios en sistemas de IA:**

- **Escalado granular:** el servicio de inferencia puede escalarse horizontalmente durante los picos de demanda sin incrementar los recursos del servicio de ingesta, que opera de manera asíncrona y con carga predecible.
- **Despliegues independientes:** el equipo de ML puede actualizar la estrategia de retrieval y el modelo de embeddings sin afectar al equipo de backend que mantiene la lógica de negocio.
- **Isolation de fallos:** si el servicio de inferencia del modelo comercial experimenta una degradación de la API externa, el resto del sistema puede continuar operando. Un circuit breaker puede activar un fallback hacia un modelo local o una respuesta cacheada.
- **Heterogeneidad tecnológica:** el servicio de inferencia puede estar implementado en Python con acceso a GPU, mientras el servicio de autenticación opera en Go con requisitos de latencia sub-milisegundo.

**Limitaciones específicas para sistemas de IA:**

- **Latencia de red acumulativa:** si una solicitud de usuario pasa por el API gateway, el servicio de composición de contexto, el servicio de retrieval y el servicio de inferencia de forma secuencial, la latencia de red de cada salto se acumula. En sistemas con requisitos de respuesta inferior a dos segundos, este presupuesto de latencia puede resultar ajustado.
- **Complejidad operativa:** múltiples servicios implican múltiples pipelines de CI/CD, múltiples configuraciones de logging y múltiples puntos de observabilidad que deben ser correlacionados mediante trazas distribuidas.
- **Service mesh y coordinación:** en sistemas con muchos servicios, la coordinación de la comunicación entre ellos puede requerir un service mesh (como Istio o Linkerd), que agrega una capa adicional de infraestructura.

**Patrones específicos de microservicios para sistemas de IA:**

- **Sidecar de observabilidad:** un contenedor auxiliar que acompaña al servicio de inferencia y captura todas las llamadas al modelo, los tokens consumidos y los tiempos de respuesta sin modificar el código del servicio principal. Este patrón permite instrumentar sin intrusión.
- **API contract entre servicio de negocio y servicio de RAG:** definir un esquema estricto para la solicitud de contexto (qué filtros se aplican, qué campos se incluyen en los metadatos de los chunks, qué nivel de confianza mínimo se acepta) desacopla al equipo de negocio del equipo de ML de forma que cada uno puede evolucionar su lado del contrato independientemente.
- **Circuit breaker para llamadas a LLM externos:** cuando la API de un proveedor externo experimenta alta latencia o errores, el circuit breaker abre el circuito y activa una respuesta alternativa — un mensaje de degradación elegante o una llamada a un modelo de respaldo — en lugar de propagar los errores a todos los usuarios.
- **Dedicated pod de inferencia en Kubernetes:** el servicio de inferencia se despliega en nodos con GPU dedicados, aislados de los nodos de CPU del resto de los servicios, permitiendo una política de escalado y un presupuesto de costos independientes.

> **Nota del Arquitecto:** El error de diseño más frecuente al adoptar microservicios en sistemas de IA es dividir los servicios por tecnología en lugar de por dominio funcional. Crear un "servicio de Python" y un "servicio de Node.js" no produce los beneficios de los microservicios. Crear un "servicio de ingesta" y un "servicio de recuperación" con responsabilidades de dominio claras sí los produce.

Cuando la carga de trabajo tiene una naturaleza asíncrona — ingesta de documentos, procesamiento de lotes, evaluación periódica de calidad — los microservicios pueden combinarse con el patrón de arquitectura basada en eventos que examina la sección siguiente.
