# Módulo 9 – Capítulo 10 – Sección 03

# Defense in depth: capas de control a nivel de prompt, API, red y datos

Defense in depth (DiD) —el principio de implementar múltiples capas de control independientes de forma que el fallo de una capa no compromise la seguridad del sistema completo— es especialmente relevante en sistemas de IA porque ningún control individual es completamente efectivo: los clasificadores de seguridad tienen falsos negativos, las instrucciones de refuerzo en el system prompt pueden ser evadidas por jailbreaks sofisticados, y el rate limiting puede ser superado por atacantes distribuidos. La arquitectura de defensa en profundidad para sistemas de IA debe implementar controles independientes en al menos cuatro capas: la capa de prompt (instrucciones de seguridad, separadores estructurales), la capa de API (rate limiting, autenticación, input/output validation con clasificadores), la capa de red (WAF, TLS, segmentación), y la capa de datos (cifrado, controles de acceso al vectorstore, inmutabilidad de logs). La independencia de las capas es crítica: si el clasificador de output y el sistema de logging usan la misma API key, un atacante que compromete esa key puede deshabilitar ambos controles simultáneamente — las capas deben tener diferentes superficies de ataque.

## Aspectos técnicos

- Capa de prompt (primera línea): system prompt con instrucciones explícitas de seguridad, separadores estructurales entre prompt sistema/documentos RAG/input usuario (`<system>`, `<context>`, `<user>`), instrucciones de no revelar el system prompt, instrucciones de no seguir instrucciones en documentos recuperados
- Capa de API (segunda línea): input validation con LlamaGuard/Prompt Guard antes de enviar al modelo, output validation con LlamaGuard/Presidio después del output del modelo, rate limiting multidimensional, autenticación JWT con claims granulares, y logging de cada request con safety scores
- Capa de red (tercera línea): WAF (AWS WAF + Lakera Guard en paralelo), TLS 1.3 con certificate pinning en clientes de API, segmentación de red entre el serving layer del modelo y otros componentes del sistema (el servidor del LLM no debe tener acceso directo a la base de datos de usuarios), y network egress filtering para agentes con acceso web
- Capa de datos (cuarta línea): cifrado AES-256 del vectorstore y logs de inferencia con claves KMS rotadas, controles de acceso RBAC a los índices vectoriales (un usuario solo puede recuperar documentos de su tenant), inmutabilidad de logs en S3 Object Lock COMPLIANCE, y auditoría de acceso a datos sensibles
- Testing de la defensa en profundidad: cada capa debe ser testeable de forma independiente; el red teaming debe incluir escenarios donde una capa falla y verificar que las capas restantes contienen el daño; la interdependencia entre capas (una capa asumiendo que otra ya limpió el input) es una fuente común de vulnerabilidades en sistemas con múltiples controles

## Para recordar

Defense in depth en sistemas de IA significa que un atacante que logra eludir el sistema prompt (primera capa) aún debe eludir el clasificador de output (segunda capa), el WAF semántico (tercera capa), y el control de acceso a datos (cuarta capa) para lograr un impacto significativo — cada capa reduce independientemente la probabilidad de un ataque exitoso de extremo a extremo.
