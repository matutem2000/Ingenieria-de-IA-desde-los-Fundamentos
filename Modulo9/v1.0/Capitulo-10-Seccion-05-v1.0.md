# Módulo 9 – Capítulo 10 – Sección 05

## Security testing pipeline y matriz de control: verificación continua y referencia operacional

Los principios de security by design, mínimo privilegio y defense in depth que articularon las secciones anteriores de este capítulo son necesarios pero insuficientes sin un mecanismo que verifique continuamente que los controles implementados funcionan como se diseñaron. Los controles de seguridad degradan con el tiempo: las reglas de un WAF dejan de detectar nuevas variantes de ataque; los clasificadores de seguridad como LlamaGuard experimentan drift ante técnicas de evasión que evolucionan; las configuraciones de seguridad se modifican inadvertidamente durante deployments; las dependencias de seguridad acumulan vulnerabilidades. El security testing pipeline es la respuesta de ingeniería a esta degradación: un conjunto de verificaciones automatizadas que corren continuamente en el ciclo de desarrollo y deployment para detectar regresiones de seguridad antes de que lleguen a producción o, si ya están en producción, antes de que sean explotadas.

El security testing pipeline para sistemas de IA combina técnicas del security testing de software tradicional con técnicas específicas de IA. SAST (Static Application Security Testing) con Semgrep y Bandit detecta vulnerabilidades en el código de la aplicación que rodea al modelo: concatenación directa de user input en prompts sin separadores estructurales, uso de `pickle.load` para deserializar artefactos de modelo (vulnerable a deserialization attacks), API keys hardcodeadas en código o en archivos de configuración versionados, y logging de inputs completos del usuario sin cifrado. Las reglas SAST para proyectos de IA deben incluir estas verificaciones específicas que no existen en los rulesets genéricos.

DAST (Dynamic Application Security Testing) con OWASP ZAP o Burp Suite prueba el endpoint de la API de IA en ejecución contra ataques de capa HTTP: verificar que todos los endpoints requieren autenticación (no solo los endpoints de inferencia sino también los de administración, health check, y métricas), verificar que el rate limiting devuelve HTTP 429 con Retry-After correcto, verificar que los headers de seguridad están presentes (Content-Security-Policy, X-Content-Type-Options, Strict-Transport-Security), y verificar que los mensajes de error no exponen información sensible del sistema (versiones de librerías, rutas internas, mensajes de stack trace).

El fuzzing de prompts automatiza la generación y ejecución de variaciones adversariales sobre el sistema: toma prompts de ataque conocidos como baseline y genera mutaciones mediante inserción de caracteres especiales, sustitución por homoglifos, traducción parcial a otros idiomas, fragmentación en múltiples messages, y codificación en Base64 o ROT13. Herramientas como Garak (NVIDIA) y un subset de PyRIT (Microsoft) pueden ejecutarse en el pipeline de CI/CD como gates de deployment: si la tasa de activación de safety filters cae por debajo de un umbral esperado ante categorías de ataque conocidas, el deployment se bloquea hasta que el equipo de seguridad revise la regresión.

La evaluación periódica de los clasificadores de seguridad cierra el ciclo: LlamaGuard, Azure Content Safety y otros clasificadores usados como controles deben evaluarse semanalmente con un dataset de golden tests que incluya tanto true positives (contenido dañino que debe ser bloqueado) como false positives (contenido benigno que no debe bloquearse). La degradación del F1 score del clasificador en el tiempo puede indicar model drift o nuevas técnicas de evasión que el clasificador no conoce, y debe triggear una revisión antes de que el gap entre el clasificador y las técnicas actuales de ataque sea explotado.

## Matriz de control del Módulo 9

La tabla siguiente mapea las amenazas principales del módulo con sus controles de mitigación, el capítulo donde se desarrolla el control, y las herramientas de implementación. Esta matriz es el artefacto de referencia operacional que consolida los controles de los diez capítulos en formato consultable.

| Amenaza | Control técnico | Capítulo | Herramienta de implementación |
|---|---|---|---|
| Prompt injection directa | Separadores estructurales + instrucciones de refuerzo + clasificador de input | Cap. 02 | Prompt Guard (Meta), diseño de system prompt |
| Prompt injection indirecta (RAG) | Tratar documentos RAG como untrusted + validación de output antes de ejecutar acciones | Cap. 02, 05 | Tags `<retrieved_context>`, output filter |
| Jailbreaking | Validación semántica del output independiente del modelo + defense in depth | Cap. 02 | LlamaGuard-3 (Meta) |
| RAG poisoning | Validación de contenido en ingestión + RBAC al vectorstore + auditoría periódica del corpus | Cap. 05 | LlamaGuard, Microsoft Presidio, pgvector RBAC |
| Cascading compromise multi-agente | Tratar output de sub-agentes como input untrusted + sandboxing de comunicaciones | Cap. 05 | Validación de schema inter-agente, LlamaGuard |
| Ataques adversariales en guardrails | Múltiples clasificadores con arquitecturas distintas + ensemble de detección | Cap. 03 | LlamaGuard + Azure Content Safety + Perspective API |
| Model extraction | Rate limiting multidimensional + monitoreo de distribución de topics | Cap. 07 | Redis sliding window, análisis de embeddings |
| Memorización de training data | Deduplicación del corpus + DP-SGD durante fine-tuning | Cap. 06 | Opacus (Meta), MinHash LSH |
| Data poisoning | Auditoría estadística del dataset + activation clustering + escaneo safetensors | Cap. 03, 01 | modelscan, trivy, activación clustering |
| Supply chain attacks | Verificación de integridad de pesos (SHA256) + safetensors en lugar de pickle + SBOM | Cap. 01 | modelscan, pip-audit, trivy |
| PII exposure | Detección automática de PII en input/output + pseudonimización + cifrado por usuario | Cap. 06 | Microsoft Presidio, Amazon Comprehend |
| Prompt leaking | No almacenar credenciales en system prompt + output filter para texto del system prompt | Cap. 02 | Output filter con n-gram matching |
| Backdoors en modelos | Pruebas de comportamiento pre-deployment + verificación de integridad de artefactos | Cap. 03 | Activation clustering, behavioral testing |
| Falta de trazabilidad | Audit log con schema completo + inmutabilidad + integración SIEM | Cap. 08 | S3 Object Lock, Splunk/Sentinel, HMAC-SHA256 |
| Incumplimiento GDPR | Borrado selectivo en logs + machine unlearning + minimización de datos | Cap. 09 | Cifrado por usuario con TTL, SISA training |
| Incumplimiento EU AI Act | Risk management system + technical documentation + human oversight | Cap. 09 | Control matrix, red team reports |

## Aspectos técnicos

- **SAST adaptado a IA:** reglas Semgrep personalizadas para detectar concatenación directa de user input en prompts, uso de pickle.load para artefactos de modelo, API keys en código, y logging sin cifrado de inputs del usuario; Bandit para vulnerabilidades Python en el código de la aplicación.
- **DAST para endpoints de IA:** OWASP ZAP con extensiones específicas para IA; verificar autenticación en todos los endpoints, rate limiting activo, headers de seguridad, y ausencia de información sensible en mensajes de error.
- **Fuzzing de prompts en CI/CD:** Garak como gate de deployment con subset de probes para categorías de ataque conocidas; umbral de activación de safety filter definido como SLA de seguridad que bloquea el deploy si no se cumple.
- **Evaluación de clasificadores:** dataset de golden tests (true positives + false positives) evaluado semanalmente; alerta si F1 score cae más del 5% respecto al baseline; triggerar revisión del clasificador o reentrenamiento si la degradación supera el umbral.
- **Pipeline completo en CI/CD:** SAST en cada PR (fallo si hallazgos críticos) → DAST en staging antes de cada deploy → evaluación de clasificadores semanal → red teaming automatizado (Garak) como gate de deployment → red teaming manual periódico para vulnerabilidades que requieren creatividad adversarial.

> **Nota del Arquitecto:** La matriz de control tiene valor operacional solo si está actualizada. Un control marcado como "implementado" que fue deshabilitado hace tres meses por un incidente de falsos positivos pero no fue eliminado de la matriz es peor que no tener la matriz: da una falsa sensación de cobertura. Mantener la matriz como código en el repositorio del proyecto con CI que verifique automáticamente los controles que pueden verificarse de forma programática (cifrado habilitado, logs fluyendo al SIEM, clasificador respondiendo) es la forma de convertirla en un artefacto de referencia confiable en lugar de un documento decorativo.

El security testing pipeline automatizado proporciona la cobertura consistente que ningún proceso manual puede garantizar, y la matriz de control proporciona la referencia operacional que permite al equipo responder rápidamente a cualquier pregunta sobre el estado de cobertura de seguridad del sistema: qué amenazas están mitigadas, con qué controles, y dónde están los gaps.
