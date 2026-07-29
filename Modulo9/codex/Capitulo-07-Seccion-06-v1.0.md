# Módulo 9 – Capítulo 07 – Sección 06

# Cierre: el hardening del endpoint es la primera línea de defensa del sistema de IA

El hardening del endpoint de IA —la combinación de rate limiting inteligente, autenticación y autorización granular, input validation semántica, output filtering, y WAF adaptado— es la primera línea de defensa del sistema porque es el punto donde todos los inputs externos convergen antes de llegar al modelo. Un endpoint bien hardenizado no previene todos los ataques (algunos, como data poisoning o model extraction distribuido, operan por debajo de sus umbrales de detección), pero eleva significativamente el costo y la complejidad de los ataques exitosos, limitando el radio de acción de los atacantes que no tienen capacidades avanzadas. En términos prácticos, la mayoría de los intentos de abuso de sistemas de IA en producción son oportunistas, no sofisticados: un rate limiting apropiado, una autenticación correcta y un output filter básico son suficientes para neutralizarlos. Los ataques sofisticados (actores estatales, competidores con alta motivación) requieren defensa en profundidad que va más allá del endpoint, pero no existe defensa en profundidad efectiva sin una primera línea robusta.

*"Defense is difficult not because attackers are smart, but because defenders must be right every time while attackers only need to be right once."* — John Chambers, ex CEO de Cisco, sobre el principio de asimetría fundamental entre atacantes y defensores que hace al hardening de endpoints crítico como primera barrera.

## Conceptos clave del capítulo

- Rate limiting multidimensional: RPM + TPM + detección de patterns de model extraction mediante análisis de distribución de topics de requests; Token Bucket o Sliding Window en Redis para implementación de producción
- Autenticación y autorización granular: OAuth 2.0 con PKCE para usuarios finales, API keys rotadas automáticamente para server-to-server, RBAC por modelo y capacidad, secrets en KMS nunca en código ni contexto del modelo
- Input validation semántica: límites de longitud en tokens (no bytes), clasificadores especializados (LlamaGuard, Prompt Guard) como primera línea, validación de schema para inputs estructurados
- Output filtering: LlamaGuard sobre el output como segunda línea de defensa, Presidio para redacción de PII, detección del system prompt en la respuesta para prevenir prompt leaking
- WAF especializado para IA: capa HTTP (AWS WAF, Cloudflare) + capa semántica (Lakera Guard, Prompt Security, Rebuff) operando en paralelo para detección complementaria

## Idea central

El hardening del endpoint es el prerequisito para todas las demás capas de defensa: sin controles robustos en el punto de entrada del sistema, ninguna defensa interna puede ser efectiva porque el atacante llega al modelo con acceso sin restricciones.
