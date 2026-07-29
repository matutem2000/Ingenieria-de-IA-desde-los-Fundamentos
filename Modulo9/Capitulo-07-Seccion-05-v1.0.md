# Módulo 9 – Capítulo 07 – Sección 05

# Web Application Firewall (WAF) adaptado para APIs de IA

Los Web Application Firewalls tradicionales (AWS WAF, Cloudflare WAF, ModSecurity) fueron diseñados para proteger aplicaciones web contra ataques como SQL injection, XSS, CSRF y path traversal, basándose en reglas de matching contra patrones de requests HTTP conocidos. Para APIs de IA, esta protección es necesaria pero insuficiente: un WAF tradicional no puede detectar un prompt injection porque el payload malicioso es semánticamente válido dentro del protocolo HTTP, y la firma de ataque está en el significado del texto, no en su estructura. Un WAF para IA debe complementar las reglas tradicionales con capacidades específicas: detección de patterns de model extraction (análisis estadístico de las requests para detectar cobertura sistemática del espacio de temas), rate limiting inteligente por categoría de request, detección de inputs que buscan eludir guardrails (mediante clasificadores semánticos), y protección contra ataques específicos de LLMs documentados en OWASP LLM Top 10. Soluciones emergentes como Lakera Guard, Prompt Security y Rebuff implementan capas de WAF semántico específicamente diseñadas para endpoints de IA.

## Aspectos técnicos

- WAF tradicional para el perímetro HTTP: AWS WAF con reglas de OWASP Core Rule Set, Cloudflare WAF, o ModSecurity protegen contra ataques de capa HTTP convencionales (rate limiting, geo-blocking, IP reputation); esta capa es necesaria y no reemplazable por controles de IA, pero insuficiente por sí sola para proteger endpoints de LLMs
- Lakera Guard: proxy inverso para APIs de LLMs que intercepta requests y responses, aplica clasificadores de prompt injection y jailbreak entrenados en un dataset propietario, y proporciona scores de riesgo por request; soporta integración con OpenAI, Anthropic y endpoints de modelos propios; arquitectura de sidecar que no modifica el código de la aplicación
- Prompt Security: solución similar a Lakera que añade análisis de comportamiento (tracking de patterns de uso anómalos entre sesiones), protección contra model extraction (detección de queries sistemáticas), y shadow mode (logging de todos los prompts sin bloqueo para análisis forense) antes de activar el modo de bloqueo
- Rebuff (open-source): combina tres capas de detección de prompt injection: heurísticas basadas en reglas (pattern matching rápido), LLM-based detection (un LLM secundario evalúa si el input contiene injection), y VectorDB-based detection (compara el embedding del input contra una base de ejemplos conocidos de injection) — diseñado como librería para integración directa en la aplicación
- Análisis de patrones de model extraction en el WAF: un WAF para IA debe monitorear la distribución de topics de los últimos N requests de cada API key y alertar si la cobertura de topics supera un umbral de diversidad (indicativo de systematic querying) — esto requiere embeddings de los inputs y análisis estadístico de distancias en el espacio de representación

## Para recordar

Un WAF para APIs de IA debe operar en dos capas independientes: la capa HTTP tradicional (AWS WAF, Cloudflare) para protección perimetral convencional, y la capa semántica especializada (Lakera Guard, Prompt Security, o Rebuff) para detectar ataques específicos de LLMs que no tienen firma a nivel de protocolo HTTP.
