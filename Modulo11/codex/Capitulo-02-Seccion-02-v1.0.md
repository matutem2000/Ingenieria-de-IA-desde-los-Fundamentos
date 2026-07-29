# Módulo 11 – Capítulo 02 – Sección 02

# Patrón Hub-and-Spoke: plataforma centralizada con spokes por dominio de negocio

El patrón Hub-and-Spoke aplicado a IA enterprise establece una plataforma central (hub) que provee capacidades compartidas — acceso a LLMs, servicio de embeddings, base de datos vectorial, observabilidad, gestión de costos — mientras cada dominio de negocio opera un spoke que contiene su lógica específica de IA, sus datos propios, y sus evaluaciones particulares, sin duplicar la infraestructura subyacente. Este patrón resuelve el dilema entre centralización total (un equipo central que se convierte en cuello de botella para todos los dominios) y descentralización total (cada equipo construye su propio stack de IA, multiplicando costos y fragmentando la gobernanza): el hub es responsable de los estándares, la seguridad, y la infraestructura compartida, mientras los spokes son autónomos en sus decisiones de producto y en la velocidad de iteración. La implementación técnica del hub incluye un portal de developer self-service (Internal Developer Portal con Backstage) que permite a los equipos de los spokes aprovisionar nuevos casos de uso de IA mediante templates, sin necesidad de involucrar al equipo central en cada nuevo proyecto. Los spokes se conectan al hub a través de APIs internas versionadas y políticas de red que garantizan el aislamiento entre dominios: el spoke de recursos humanos no puede acceder a los datos o índices vectoriales del spoke de finanzas.

## Aspectos técnicos del patrón

- Hub: plataforma gestionada por un equipo central de AI Platform Engineering, con SLOs de disponibilidad, documentación, y soporte a los equipos de spokes
- Spoke por dominio: microservicio de orquestación específico del dominio que consume APIs del hub, con su propio namespace en Kubernetes y sus propias políticas de RBAC
- Conectividad hub-spoke: Private Service Connect (GCP) o PrivateLink (AWS) para llamadas intra-VPC, con mTLS entre servicios y autorización basada en Service Accounts
- Aislamiento de datos: cada spoke tiene su propio índice en la base de datos vectorial, con namespaces separados en Pinecone o colecciones separadas en Weaviate con políticas de acceso
- Gobernanza federada: el hub define los estándares y los guardrails; los spokes los implementan y son responsables de cumplirlos dentro de su dominio

## Buena práctica

El hub debe proveer capacidades, no imponer implementaciones: los spokes necesitan libertad para elegir el framework de orquestación más adecuado a su caso de uso respetando los contratos del hub.
