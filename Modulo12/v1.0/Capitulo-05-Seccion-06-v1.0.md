# Módulo 12 – Capítulo 05 – Sección 06

## Cierre: la seguridad como hilo que recorre el sistema, no como bloque aislado

El Capítulo 5 cierra el ciclo de seguridad que comenzó en el Capítulo 1 con la definición de los criterios de éxito de seguridad, continuó en el Capítulo 2 con el ADR-004 que documentó el threat model y los controles seleccionados, se enhebró en el Capítulo 3 con la sanitización de documentos en la ingesta y en el Capítulo 4 con el filtro de autorización en las herramientas del agente, y culmina aquí con la implementación completa de los controles de input/output y el red teaming que valida su efectividad. Este enhebrado no es accidental — es la aplicación del principio de que la seguridad no se agrega al final del proyecto como una capa de barniz; se diseña en cada componente del sistema desde el inicio.

La diferencia entre la seguridad de este sistema y la de un sistema donde la seguridad se añadió al final es estructural. En un sistema con seguridad retrofitted, los controles operan como filtros externos: una API Gateway que valida el input y otro servicio que audita el output, pero entre los dos el sistema opera sin restricciones. En este sistema, la seguridad opera en capas acopladas al comportamiento del sistema: los delimitadores XML no son un control externo al prompt — son parte del prompt mismo. El filtro de autorización no es un check después del retrieval — está embebido en la query de Qdrant. El audit logging no es un sistema separado — es parte del middleware de autenticación que procesa cada petición. Esta integración no solo hace los controles más efectivos; los hace más difíciles de omitir por error.

El red teaming produjo evidencia empírica de la efectividad de los controles y, más importante, identificó los puntos ciegos que ningún análisis estático habría detectado. Los 3 bypasses de la sesión inicial — 1 por injection en japonés y 2 por instrucciones en bloques de código Python — son exactamente el tipo de vulnerabilidad que los equipos descubren en producción cuando un incidente de seguridad ocurre. El red teaming convirtió ese descubrimiento en una sesión controlada con mejoras aplicadas antes del despliegue, en lugar de un incidente de producción con impacto real en usuarios.

El capítulo siguiente implementa el despliegue del sistema — el paso donde el sistema pasa del entorno de desarrollo al entorno de producción. El conjunto de controles de seguridad implementados en este capítulo son prerrequisitos del despliegue, verificados por el checklist de producción del Capítulo 10 y por el gate del pipeline CI/CD que incluye la ejecución de la suite de adversarial tests como condición de avance.

## Lo que el Capítulo 5 implementó

- **Threat model → controles**: cada amenaza del ADR-004 implementada como control concreto y verificable, con referencia al ADR que lo originó — sin repetición del análisis de amenazas, solo implementación de los controles decididos.
- **Controles anti-injection**: lista negra multilingüe de 200 patrones, clasificador de intent fine-tuned, delimitadores XML en el system prompt con instrucción de grounding, sanitización de documentos en la ingesta (incluyendo bloques de código).
- **RBAC a nivel de herramientas**: `allowed_document_types` del JWT como filtro mandatory en Qdrant — garantía estructural de que el agente no puede acceder a documentos no autorizados; 100% de efectividad en el red teaming.
- **Input validation multicapa**: schema Pydantic + lista negra + clasificador de intent + rechazo con mensajes genéricos que no revelan detalles del sistema.
- **Output filtering**: regex PII + NER para nombres de personas + patterns de credenciales; allowlist de nombres de secrets que son seguros de reproducir; streaming con post-procesamiento para minimizar impacto en latencia.
- **Red teaming documentado**: 50 ataques en 4 categorías, tasa de bypass inicial del 6% (3/50), reducida al 2% (1/50) con los controles corregidos; 3 bypasses convertidos en tests de regresión permanentes.

> **Nota del Arquitecto**: La seguridad de un sistema de IA tiene un adversario que los sistemas de software convencionales no tienen: el modelo fundacional mismo. El LLM que usamos para generar respuestas de alta calidad es el mismo LLM que puede ser manipulado para producir respuestas maliciosas, exfiltrar información del contexto, o ignorar sus instrucciones de sistema si el atacante formula el prompt correcto. Los controles de seguridad de este capítulo mitigan el riesgo pero no lo eliminan — un atacante con acceso al modelo fundacional y suficiente tiempo de experimentación puede encontrar variantes de injection que evaden todos los controles implementados. La honestidad sobre esta limitación, documentada en el ADR-004 como "riesgo residual aceptado", es la postura de seguridad madura que distingue un sistema responsable de uno que promete más de lo que puede garantizar.

Un sistema de IA sin hardening es un prototipo — no un producto en producción. El hardening de este capítulo convierte el sistema en uno que puede desplegarse con confianza, monitorearse con métricas de seguridad y mejorarse con cada sesión de red teaming.

**Para recordar**: El hardening de un sistema de IA es un proceso continuo, no un hito de proyecto — cada nueva capacidad del sistema introduce nuevas superficies de ataque que deben modelarse y mitigarse.

*"Security is always excessive until it's not enough." — Robbie Sinclair, Head of Security, Country Energy*
