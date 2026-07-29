# Módulo 11 – Capítulo 04 – Sección 02

# Aislamiento de datos entre tenants: cifrado por tenant y separación de índices vectoriales

El aislamiento de datos en sistemas multi-tenant de IA es más complejo que en aplicaciones CRUD convencionales porque los embeddings vectoriales son derivados de los datos originales: si un tenant A convierte en embedding un documento confidencial y ese embedding termina en un índice compartido sin aislamiento adecuado, es teóricamente posible que una búsqueda semántica de un tenant B recupere fragmentos de ese documento mediante similitud vectorial, aunque el tenant B nunca haya tenido acceso al documento original. El cifrado por tenant (envelope encryption con claves distintas por tenant gestionadas en AWS KMS, Azure Key Vault, o HashiCorp Vault) reduce el impacto de ciertos fallos de aislamiento, siempre que la autorización, la selección de claves y el contexto criptográfico también estén correctamente implementados: cada tenant tiene una Customer Managed Key (CMK) que puede revocar en cualquier momento, y la revocación hace inmediatamente inaccesibles todos sus datos almacenados en la plataforma. La separación de índices vectoriales es el control técnico más importante para el aislamiento en sistemas RAG multi-tenant: cada tenant debe tener su propio namespace en Pinecone, su propia colección en Weaviate o Qdrant, o su propio índice en pgvector con Row Level Security (RLS) activado, reduciendo el riesgo de recuperación cruzada; la garantía efectiva requiere además autorización, pruebas de aislamiento y controles en cada consulta.

## Controles técnicos de aislamiento de datos

- Envelope encryption por tenant: cada tenant tiene un Data Encryption Key (DEK) cifrado con su Key Encryption Key (KEK), ambas gestionadas en KMS; la revocación de la KEK del tenant hace ilegibles todos sus datos
- Namespaces en bases de datos vectoriales: Pinecone namespaces, Weaviate multi-tenancy nativa (class per tenant), Qdrant collections por tenant o payload filtering con tenant_id — cada opción con diferente trade-off de rendimiento
- Row Level Security en pgvector: politicas RLS de PostgreSQL que filtran automáticamente las filas por tenant_id extraído del JWT del usuario autenticado, garantizando aislamiento incluso ante errores de aplicación
- Tenant context propagation: el tenant_id debe propagarse mediante JWT claims o headers de contexto en cada llamada entre microservicios, y verificarse en cada punto de acceso a datos sin excepciones
- Auditoría de acceso a datos: logging de cada query vectorial con el tenant_id del solicitante, el índice consultado, y los documento IDs retornados, retenido mínimo 12 meses para auditoría forense

## Para recordar

El aislamiento de datos en multi-tenancy de IA debe implementarse como defensa en profundidad: cifrado a nivel de almacenamiento + separación de índices a nivel de base de datos vectorial + tenant_id en cada query a nivel de aplicación — ninguna capa sola es suficiente.
