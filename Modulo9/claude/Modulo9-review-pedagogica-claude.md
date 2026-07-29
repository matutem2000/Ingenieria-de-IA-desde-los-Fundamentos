# Informe Pedagógico — Módulo 9: AI Security Engineering
**Revisado por:** Director Pedagógico / Claude  
**Fecha:** 2026-07-25  
**Alcance:** 10 capítulos, 60 secciones — muestra revisada: secciones 01, 03 y 06 de todos los capítulos + secciones 02, 04 y 05 de capítulos seleccionados (01, 02, 04, 05, 06, 07, 09, 10)

---

## 1. Fortalezas

### 1.1 Progresión temática global del módulo: sólida y coherente

El módulo sigue un arco pedagógico reconocible y efectivo: **amenazas → ataques específicos → metodología de prueba → seguridad por sistema → privacidad de datos → controles operacionales → trazabilidad → cumplimiento → principios de diseño**. Esta secuencia respeta el orden natural de razonamiento de un AI Engineer: primero entender el problema (Caps. 1-3), luego saber cómo buscarlo activamente (Cap. 4), después dominar los controles por dominio (Caps. 5-8), y finalmente integrar compliance y síntesis arquitectónica (Caps. 9-10). El lector que avanza linealmente acumula vocabulario, conceptos y herramientas que se reutilizan y amplían en capítulos posteriores sin necesidad de recapitulaciones extensas.

### 1.2 Precisión técnica y referencias al estado del arte

Las referencias a herramientas, frameworks y papers están bien seleccionadas y son verificables:
- Cap. 02: many-shot jailbreaking (Anthropic 2024), Crescendo attack (Microsoft Research 2024), técnica de LlamaGuard como guardrail.
- Cap. 03: Tramèr et al. (2016) para model extraction, Carlini et al. para memorización en GPT, paper de Nasr et al. (2023) para extracción de datos de ChatGPT.
- Cap. 04: PyRIT (Microsoft), Garak (NVIDIA), PAIR (Chao et al. 2023), TAP (Mehrotra et al. 2023) — tooling actual del estado del arte.
- Cap. 06: Opacus (Meta) para DP-SGD, epsilon como presupuesto de privacidad con valores orientativos.
- Cap. 09: EU AI Act con número de reglamento (2024/1689), GDPR Art. 17 y Art. 25, HIPAA Technical Safeguards con referencias a 45 CFR 164.312.

Esta densidad de referencias concretas y actualizadas es exactamente lo que espera un AI Engineer o Arquitecto de IA en este nivel del libro.

### 1.3 Estructura interna consistente en todos los capítulos

Cada capítulo mantiene el mismo patrón: apertura con el concepto central articulado claramente, desarrollo de aspectos técnicos en bullet points accionables, y cierre con un "Para recordar" o "Idea central" que sintetiza el aprendizaje. Este patrón crea predecibilidad cognitiva — el lector sabe cómo navigar cada capítulo — y las secciones de cierre (06) con su cita de autoridad refuerzan el concepto clave con un gancho memorable. La consistencia del formato es una fortaleza editorial significativa.

### 1.4 Cobertura completa de las superficies de ataque de mayor riesgo en producción

Los temas de mayor impacto en producción real están bien cubiertos:
- **Prompt injection** (directa, indirecta, via RAG): Caps. 2 y 5 con variantes, mecanismos y defensas multicapa. Excelente.
- **Jailbreaking**: Cap. 2 Sec. 03 cubre DAN, many-shot, Crescendo, obfuscation y virtualization con profundidad suficiente.
- **RAG poisoning y prompt injection indirecta**: Cap. 5 Secs. 01 y 02 desarrollan el ataque con ejemplos documentados (Rehberger 2023) y mitigaciones arquitectónicas concretas.
- **Seguridad agéntica**: Cap. 5 Secs. 03 y 04 cubren amplificación de impacto, tool call injection, confused deputy problem y sandboxing con nivel técnico apropiado.
- **Privacidad de datos de entrenamiento**: Cap. 6 Secs. 03 y 04 sobre memorización de LLMs (Carlini) y differential privacy (DP-SGD con Opacus) son técnicamente sólidos.
- **Red teaming**: Cap. 4 cubre metodología manual y automatizada con tooling específico — uno de los tratamientos más completos del módulo.

### 1.5 Articulación efectiva del principio de defense in depth

El módulo construye progresivamente el modelo mental de defensa en profundidad sin nombrarlo explícitamente hasta Cap. 10: las capas de control se van añadiendo a lo largo de los capítulos — guardrails en el prompt (Cap. 2), validación del corpus RAG (Cap. 5), PII en todas las capas (Cap. 6), rate limiting + autenticación + input/output validation (Cap. 7), logging + auditoría (Cap. 8) — y Cap. 10 Sec. 03 finalmente sintetiza estas capas en un modelo formal de cuatro niveles. Esta pedagogía de "construir antes de nombrar" funciona bien para lectores que aprenden por acumulación.

### 1.6 El Cap. 9 (Cumplimiento regulatorio) tiene la postura correcta

La sección de cierre de Cap. 09 establece explícitamente que "el compliance es el piso mínimo, no el techo" y que los ataques más sofisticados no están cubiertos por las regulaciones actuales. Esta postura evita el error pedagógico frecuente de presentar el compliance como objetivo de seguridad, y posiciona correctamente la relación entre seguridad técnica y cumplimiento normativo.

---

## 2. Debilidades

### 2.1 Falta un puente explícito desde el Módulo 8 en el Cap. 01

El Módulo 8 cierra con arquitecturas híbridas de LLMs (local + nube), cubriendo vLLM, TGI, Ollama, MLflow, vectorstores, y serving layers como componentes de infraestructura. El Módulo 9 comienza directamente con "la superficie de ataque de los sistemas de IA" sin mencionar que exactamente esas componentes que el lector acaba de aprender a desplegar son las superficies de ataque que ahora se van a analizar. Cap. 1 Sec. 01 nombra "vectorstores como Pinecone o Weaviate" y el "pipeline de MLOps" como superficies de ataque, pero no conecta esto explícitamente con el serving layer (vLLM, TGI) ni con el MLflow que el lector acaba de configurar en el módulo anterior. El lector necesita un párrafo de contexto que funcione como transición: "Los sistemas de inferencia local que desplegamos en el Módulo 8 — el servidor vLLM, el pipeline de MLflow, el vectorstore — son exactamente las superficies de ataque que este módulo analiza".

### 2.2 Supply chain attacks: declarada en la taxonomía, ausente como tema

Cap. 1 Sec. 02 define explícitamente los "supply chain attacks" como una de las cuatro categorías de amenazas: descarga de modelos con pesos modificados via pickle exploitation, dependencias maliciosas en packages de ML, datasets adulterados. Esta categoría de amenaza es especialmente relevante para el perfil del lector que, habiendo aprendido en el Módulo 8 a descargar modelos de Hugging Face y a usar torch/transformers/accelerate, ahora necesita saber cómo hacerlo de forma segura. Sin embargo, ninguno de los 10 capítulos dedica una sección a supply chain security para ML: proveniencia de modelos, model signing, SBOM para IA, verificación de integridad de pesos, escaneo de dependencias de ML. Esta es la laguna conceptual más importante del módulo dado el perfil del lector objetivo.

### 2.3 Multi-agent security: ausente pese a la relevancia creciente

Cap. 5 cubre bien la seguridad de un agente único con herramientas. Sin embargo, la arquitectura de múltiples agentes colaborando (como en LangGraph multi-agent, CrewAI, AutoGen) introduce riesgos de seguridad específicos que no se abordan: delegación de privilegios entre agentes (¿qué trust level tiene el resultado de un sub-agente?), cascading compromise (un agente comprometido contamina al orquestador), y la arquitectura de "principal hierarchy" en sistemas multi-agente (quién tiene autoridad sobre quién). LangGraph, CrewAI y AutoGen ya son frameworks en uso en producción, y el Módulo 8 probablemente los cubre en el contexto de arquitecturas agénticas. Esta laguna es significativa para el 2025-2026.

### 2.4 NIST AI RMF aparece únicamente en el sumario de Cap. 09

El NIST AI Risk Management Framework aparece referenciado como "estándar de facto en EE.UU." en el bullet de cierre de Cap. 09, pero no tiene sección propia. Dado que el AI RMF (GOVERN-MAP-MEASURE-MANAGE) proporciona un vocabulario y un proceso de gestión de riesgos que estructuran prácticamente todo el módulo, merece al menos una sección dedicada dentro de Cap. 09 que explique sus cuatro funciones y cómo se mapean a los controles técnicos del módulo. Sin esa sección, el lector solo recibe un nombre sin contenido operacional.

### 2.5 Cap. 03 (Ataques adversariales en ML) tiene una tensión temática con el resto del módulo

Los Caps. 1-2 establecen el universo de ataques a tiempo de inferencia (prompt injection, jailbreaking). Cap. 03 introduce ataques de naturaleza diferente: ataques adversariales en texto (perturbaciones para evadir clasificadores), model extraction, membership inference, y data poisoning — conceptos del ámbito de la investigación en adversarial ML, más académicos que operacionales. El salto conceptual entre "jailbreaking" (Cap. 2) y "TextFooler/BERT-Attack" (Cap. 3 Sec. 01) es brusco para el lector. Cap. 03 Sec. 01 habla de ataques contra "clasificadores de contenido, detección de spam, detección de toxicidad" — aplicaciones que no son el foco del libro (que trata sistemas de LLM, no clasificadores convencionales de ML). La relevancia de los adversarial text attacks para un AI Engineer que despliega LLMs en producción es indirecta comparada con la relevancia de prompt injection o RAG poisoning.

### 2.6 Orden interno del Cap. 07 (Hardening del endpoint) no sigue el ciclo de vida de la request

Cap. 07 cubre: Sec. 01 Rate Limiting → Sec. 02 Autenticación y Autorización → Sec. 03 Input Validation → Sec. 04 Output Filtering → Sec. 05 (inferido: WAF) → Sec. 06 Cierre. El orden lógico para un practitioner es el ciclo de vida de una request: primero autenticación (¿quién eres?), luego autorización (¿qué puedes hacer?), luego rate limiting (¿cuánto puedes usar?), luego input validation, luego modelo, luego output filtering, finalmente WAF. Empezar con rate limiting antes de autenticación invierte la prioridad: el rate limit es irrelevante si no hay autenticación, porque un atacante sin autenticar ya está en el punto incorrecto del sistema.

### 2.7 El Cap. 10 no cierra el módulo con un documento de postura de seguridad sintetizable

Cap. 10 es el capítulo de síntesis arquitectónica y establece correctamente los principios de security by design, mínimo privilegio, defense in depth y threat modeling continuo. Sin embargo, el lector termina el módulo sin un artefacto de referencia accionable que consolide todos los controles de los 10 capítulos en una forma usable: un baseline de security posture, un checklist de revisión de diseño, o una matriz de control (control técnico → amenaza que mitiga → capítulo de referencia). El codex menciona que "se generaron 60 versiones corregidas" y la revisión técnica señala que se creó orientación sobre frecuencia basada en riesgo — sin un artefacto de síntesis, el lector debe mentalmente integrar 60 secciones por su cuenta.

### 2.8 Tratamiento desigual entre escenarios cloud y self-hosted

Las referencias a controles operacionales favorecen consistentemente AWS/Azure/GCP: S3 Object Lock COMPLIANCE, KMS para rotación de claves, Azure Immutable Blob, AWS Secrets Manager. Dado que el Módulo 8 cubre extensivamente modelos self-hosted (vLLM, TGI, Ollama), muchos lectores estarán operando en entornos on-premises o sin acceso a servicios cloud específicos. Los capítulos 7, 8 y 10 asumen implícitamente acceso a cloud, lo que puede dejar al lector de self-hosting sin alternativas concretas para implementar los mismos controles (logs inmutables, secrets management, WAF semántico).

---

## 3. Conceptos a ampliar

### 3.1 Supply chain security para ML (laguna crítica)

Ampliar Cap. 01 Sec. 02 o añadir una sección en Cap. 03 que desarrolle en profundidad:
- Verificación de integridad de pesos al descargar desde Hugging Face (hashes SHA256, model cards con proveniencia verificable).
- Mitigación de pickle exploits: `safetensors` como formato seguro vs. `.bin` / `.pkl`, herramientas como `modelscan`.
- SBOM (Software Bill of Materials) para ML: documentación de dependencias de modelos, datasets y librerías.
- Escaneo de seguridad de dependencias ML: `pip-audit`, `trivy` para imágenes Docker con librerías de ML.
- Proceso de aprobación de modelos antes de fine-tuning: qué verificar antes de usar un modelo base como punto de partida.

### 3.2 Trust hierarchy en sistemas multi-agente (laguna media)

Ampliar Cap. 05 o añadir una sección sobre seguridad multi-agente:
- Cómo establecer niveles de confianza entre un orquestador y sus sub-agentes (¿el resultado de un sub-agente es "trusted" o "untrusted"?).
- Sandboxing de comunicaciones inter-agente: por qué el output de un sub-agente debe tratarse como input externo no confiable.
- Cascading compromise: un sub-agente comprometido que inyecta instrucciones maliciosas en su output que el orquestador ejecutará.
- Frameworks específicos: cómo LangGraph, CrewAI y AutoGen manejan (o no manejan) la delegación de privilegios entre agentes.

### 3.3 NIST AI RMF como framework operacional (laguna media)

Dedicar al menos una sección completa de Cap. 09 al NIST AI Risk Management Framework:
- Explicar las cuatro funciones GOVERN-MAP-MEASURE-MANAGE con su significado práctico.
- Mapear cada función a capítulos específicos del módulo (GOVERN → Cap. 10, MAP → Cap. 1-3, MEASURE → Cap. 4 y 8, MANAGE → Caps. 5-9).
- Cómo se usa el AI RMF junto con el EU AI Act cuando una organización opera en ambas jurisdicciones.
- Diferencia entre AI RMF (voluntario en EE.UU.) y AI Act (regulación de cumplimiento obligatorio en UE).

### 3.4 Secure SDLC para sistemas de IA (laguna media)

Cap. 10 Sec. 06 menciona en un bullet "SAST + DAST + fuzzing de prompts + Garak integrados en CI/CD". Este tema merece una sección completa que desarrolle:
- Pipeline de CI/CD con gates de seguridad específicos para IA: cuándo corre Garak, cuándo corre el red teaming automatizado, cuándo se re-evalúa el threat model.
- Cómo integrar LlamaGuard y Prompt Guard como tests automatizados en el pipeline.
- Qué hace que un pull request "falle" desde la perspectiva de seguridad de IA.
- Diferencia entre gates pre-merge (testing de regresión de seguridad) y gates pre-deployment (red teaming completo).

### 3.5 Threat modeling como artefacto concreto (ampliar Cap. 10)

Cap. 10 Sec. 04 explica el proceso de threat modeling continuo muy bien, pero no muestra cómo se ve un threat model de un sistema de IA en formato documentable. Ampliar con:
- Ejemplo de DFD (Data Flow Diagram) de un sistema RAG con trust boundaries explícitos (sistema → LLM → vectorstore → herramientas → usuario).
- Fragmento de threat model en YAML (Threatspec o STRIDE-in-YAML) para un pipeline agéntico.
- Cómo el threat model evoluciona cuando se añade una herramienta nueva al agente (ejemplo concreto con antes/después).

---

## 4. Conceptos a resumir o eliminar

### 4.1 Ataques adversariales en texto (Cap. 03 Sec. 01): reducir o reorientar

Cap. 03 Sec. 01 cubre TextFooler, BERT-Attack, ataques de sustitución de caracteres, y ataques whitebox vs. blackbox. El nivel de detalle técnico es apropiado para un curso de adversarial ML research, pero para un AI Engineer que despliega LLMs en producción, el impacto práctico de estos ataques es limitado: los targets reales son clasificadores de contenido y moderación, no los LLMs conversacionales que son el foco del libro. Esta sección podría reducirse a un párrafo de contexto ("los clasificadores que usamos como guardrails — LlamaGuard, Azure Content Safety — son vulnerables a perturbaciones adversariales") y remitir a papers especializados para el lector interesado en profundizar.

La sección 03 de Cap. 03 (Model extraction) y la sección 04 (Membership inference) son más relevantes para el perfil del lector y deberían mantenerse con su profundidad actual.

### 4.2 Consolidar referencias repetidas a las mismas herramientas

A lo largo del módulo, LlamaGuard, Presidio, y las API keys de proveedores aparecen en múltiples secciones de capítulos diferentes con descripciones que parcialmente se solapan. Por ejemplo:
- LlamaGuard se describe brevemente en Cap. 02 Sec. 06 (cierre), en Cap. 07 Sec. 03, y en Cap. 10 Sec. 06. Cuando el texto completo sea desarrollado, el autor debería establecer una referencia canónica en el primer punto de aparición y usar referencias cruzadas en los demás.
- Presidio de Microsoft se presenta en Cap. 06 Sec. 01 y vuelve a aparecer en Cap. 07 y Cap. 08. Mismo principio.

Esto no es un problema en el esqueleto actual (donde cada sección es autocontenida), pero al expandir al texto completo puede generar repetición innecesaria que ralentiza al lector.

### 4.3 Reducir la duplicación conceptual entre Cap. 02 (Prompt injection indirecta) y Cap. 05 (RAG poisoning)

Cap. 02 Sec. 02 (inferida como prompt injection indirecta) y Cap. 05 Secs. 01 y 02 cubren el mismo vector de ataque desde ángulos complementarios: Cap. 02 desde la perspectiva del mecanismo del ataque, Cap. 05 desde la perspectiva del sistema RAG. Esta división es pedagógicamente válida, pero el autor debe asegurarse de que al expandir el texto completo no reescriba los mismos conceptos (cómo funciona el ataque, ejemplos de Rehberger) en ambos capítulos. Cap. 02 debe enfocarse en el mecanismo; Cap. 05 debe enfocarse en el vectorstore como superficie de ataque y en las mitigaciones arquitectónicas específicas de RAG.

---

## 5. Recomendaciones editoriales

Las siguientes recomendaciones están priorizadas por impacto pedagógico, de mayor a menor.

**1. Añadir un párrafo de transición en Cap. 01 Sec. 01 que conecte explícitamente con el Módulo 8.** El párrafo debe nombrar los componentes que el lector acaba de aprender a desplegar (vLLM, TGI, MLflow, vectorstores, pipelines de fine-tuning) y ubicarlos como superficies de ataque específicas en el mapa del módulo. Esta es la única forma de que el lector active el conocimiento previo antes de entrar al contenido del módulo.

**2. Desarrollar una sección completa sobre supply chain security para ML.** La ubicación más natural es Cap. 03 Sec. 05 (actualmente no revisada), añadiendo como nuevo contenido: verificación de integridad de pesos, safetensors vs. pickle, SBOM para ML, y escaneo de dependencias de librerías de ML. Si Cap. 03 ya tiene seis secciones completas, el tema puede moverse a Cap. 01 Sec. 02 como extensión de la taxonomía de supply chain attacks. Este tema no puede quedar en una taxonomía de tres líneas dado el perfil del lector.

**3. Ampliar Cap. 09 con una sección dedicada al NIST AI RMF.** Sustituir o complementar una de las secciones de Cap. 09 (posiblemente expandiendo la sección 04 o 05 que no se revisaron) con un tratamiento operacional del NIST AI RMF: las cuatro funciones, su relación con EU AI Act, y cómo el módulo las implementa técnicamente. El NIST AI RMF es el vocabulario que los equipos de seguridad en EE.UU. usarán para auditar los sistemas del lector.

**4. Añadir una sección sobre seguridad en sistemas multi-agente en Cap. 05.** La sección 05 de Cap. 05 (no revisada) podría expandir el contenido agéntico para cubrir arquitecturas multi-agente: trust delegation, cascading compromise, y sandboxing de comunicaciones inter-agente. LangGraph y CrewAI deben ser nombrados explícitamente dado que el libro probablemente los cubre en módulos anteriores de arquitecturas agénticas.

**5. Reordenar las secciones de Cap. 07 para seguir el ciclo de vida de la request.** El orden sugerido: Sec. 01 Autenticación y Autorización (¿quién accede?) → Sec. 02 Rate Limiting y Throttling (¿cuánto accede?) → Sec. 03 Input Validation (¿qué entra al modelo?) → Sec. 04 Output Filtering (¿qué sale del modelo?) → Sec. 05 WAF y capas de red → Sec. 06 Cierre. Este orden refleja la secuencia de procesamiento de cada request y hace más intuitiva la arquitectura de defensa para el lector.

**6. Añadir en Cap. 10 un artefacto de síntesis: tabla de control matrix del módulo.** La sección 05 de Cap. 10 (no revisada) podría contener una tabla o matriz que mapee: amenaza → control técnico recomendado → capítulo de referencia → herramienta de implementación. Este artefacto convierte el módulo en una referencia operacional que el lector puede usar después de terminar el libro, no solo durante la lectura. Sería el "quick reference" de AI Security Engineering para el lector en producción.

**7. Añadir alternativas on-premises a los controles cloud en Caps. 07, 08 y 10.** Para cada control que actualmente solo se documenta con servicios AWS/Azure/GCP, añadir la alternativa self-hosted: HashiCorp Vault para secrets (ya presente en Cap. 07), Wazuh o Graylog para SIEM on-premises (Cap. 08), MinIO con Object Locking para logs inmutables (Cap. 08), y OPA (Open Policy Agent) para autorización granular (Cap. 07). El lector que viene del Módulo 8 probablemente opera en entornos mixtos o puramente on-premises.

**8. Establecer una referencia canónica para herramientas reutilizadas a lo largo del módulo.** En el primer capítulo donde LlamaGuard, Presidio, PyRIT y Garak aparezcan con descripción completa, añadir una nota del tipo "esta herramienta se utiliza en múltiples capítulos del módulo — la descripción completa está en Cap. X Sec. Y". En los capítulos posteriores, solo hacer referencia cruzada. Esto evitará la repetición de descripciones técnicas al expandir el esqueleto a texto completo.

**9. Revisar Cap. 03 Sec. 01 (Adversarial text attacks) para ajustar su nivel de profundidad al perfil del lector.** La sección actualmente tiene el nivel de un survey académico de adversarial ML. Para el AI Engineer en producción que usa LLMs, el punto de relevancia práctica de TextFooler y BERT-Attack es: "los clasificadores que uso como guardrails son vulnerables a estas perturbaciones." Reducir la sección al punto de relevancia práctica (dos bullet points en lugar de cinco) y añadir un párrafo sobre qué sistemas de producción son targets reales de estos ataques y qué defensas concretas existen.

**10. Verificar todas las referencias normativas contra textos primarios antes de la publicación.** El codex señala que algunas frecuencias y mandatos fueron atribuidos a NIST y AISI sin referencia verificable. Cap. 10 Sec. 04 menciona "revisión trimestral del threat model" como "opcionalmente (pero recomendablemente) cada trimestre" — después de la corrección del codex, esta orientación parece derivarse de riesgo y no de mandato, lo cual es correcto. El autor debe hacer un pase final por todo el módulo revisando que ninguna afirmación normativa ("X requiere", "Y exige", "Z establece") esté atribuida a un organismo sin cita del texto primario específico.

---

## 6. Evaluación por criterio específico

### 6.1 ¿La secuencia de los 10 capítulos tiene progresión pedagógica correcta?

**Mayormente sí, con una observación.** La secuencia conceptual de Caps. 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 sigue la lógica: fundamentos → ataques de input → ataques de modelo → testing adversarial → seguridad de sistema → privacidad de datos → controles operacionales → trazabilidad → regulación → síntesis. Esta es una progresión pedagógicamente válida.

La única anomalía es Cap. 03 (Ataques adversariales en ML), que conceptualmente pertenece a la misma familia que los ataques de modelo y datos del Cap. 01 Sec. 02, pero se desarrolla después del estudio en profundidad de los ataques de input (Cap. 02). La posición es aceptable pero el puente entre Cap. 02 (ataques al comportamiento del modelo en runtime) y Cap. 03 (ataques a la robustez del modelo en evaluación) necesita una transición explícita.

### 6.2 ¿Los capítulos están bien conectados entre sí dentro del módulo?

**Sí en el nivel de conceptos, con un gap de conexión explícita entre capítulos.** Los conceptos se acumulan correctamente: Cap. 01 establece la taxonomía que Caps. 02-05 desarrollan en detalle; Cap. 07 usa LlamaGuard que se presentó en Cap. 02; Cap. 08 registra los tool calls que Cap. 05 describió como riesgo de seguridad. Sin embargo, estos vínculos son implícitos en el esqueleto actual. Al expandir a texto completo, cada capítulo debe tener al menos una referencia explícita al capítulo anterior que motive el salto temático.

### 6.3 ¿El módulo aterriza bien desde el Módulo 8 y prepara bien al lector para el Módulo 10?

**Aterrizaje desde Módulo 8: aceptable pero mejorable.** La transición existe conceptualmente (Module 8 = infraestructura de IA; Module 9 = seguridad de esa infraestructura) pero no está articulada explícitamente en Cap. 01. Ver Recomendación Editorial 1.

**Preparación para Módulo 10: correcta.** Module 10 abre con "plataformas de IA como infraestructura compartida" y gobernanza a escala. Module 9 cierra con security by design, threat modeling continuo, y security testing en CI/CD — principios que son prerequisitos para operar una plataforma de IA con múltiples equipos y sistemas. El Cap. 10 Sec. 04 ("threat model como código versionado en git") conecta naturalmente con la filosofía de infrastructure-as-code y platform-as-code que Module 10 probablemente desarrolla. La articulación con el módulo siguiente es el punto más fuerte de las conexiones entre módulos.

### 6.4 ¿Qué capítulos o secciones necesitan más desarrollo técnico?

En orden de prioridad:
1. **Cap. 09 Sec. 04 o 05 (NIST AI RMF):** actualmente solo una mención en bullet de cierre.
2. **Cap. 10 Sec. 05 (inferida: security testing pipeline):** el contenido sobre CI/CD con gates de seguridad para IA merece desarrollo completo, no solo un bullet en el cierre.
3. **Supply chain security (sin sección propia):** completamente ausente como desarrollo, solo en taxonomía de Cap. 01.
4. **Multi-agent security (Cap. 05 Sec. 05):** probablemente subdesarrollada dada la relevancia creciente del patrón.

### 6.5 ¿Hay lagunas conceptuales importantes en el temario?

Sí, tres lagunas significativas:

1. **Supply chain security para ML:** cómo asegurar el pipeline de obtención de modelos, datasets y dependencias. Completamente ausente como tema desarrollado.
2. **Seguridad en sistemas multi-agente:** trust delegation, cascading compromise, y sandboxing de comunicaciones inter-agente.
3. **Secure CI/CD específico para IA:** cómo integrar security gates en el pipeline de deployment de sistemas de IA — más allá de mencionar las herramientas.

Una cuarta laguna de menor prioridad: **evasión de WAF y LLM firewalls** — cómo los atacantes evaden los guardrails y WAFs semánticos, y qué implica esto para su configuración. Los guardrails se presentan como soluciones pero no se discute su elusibilidad, lo cual es importante para que el lector no los sobreestime.

### 6.6 ¿Qué temas están bien cubiertos y cuáles son superficiales?

**Bien cubiertos (pueden desarrollarse directamente al texto completo):**
- Prompt injection directa e indirecta (Cap. 02 y Cap. 05): excelente cobertura técnica.
- Jailbreaking con técnicas específicas (Cap. 02 Sec. 03): completo y actualizado.
- Red teaming manual y automatizado (Cap. 04): uno de los tratamientos más completos del módulo.
- RAG poisoning y seguridad agéntica (Cap. 05): técnicamente sólido.
- Differential privacy para fine-tuning (Cap. 06 Sec. 04): técnicamente preciso con valores orientativos de epsilon.
- Logging e inmutabilidad de eventos de seguridad (Cap. 08 Secs. 01-02): schema completo y justificación clara.
- EU AI Act y GDPR (Cap. 09 Secs. 01-02): bien fundamentados con referencias a artículos específicos.

**Superficiales (necesitan más desarrollo en el texto completo):**
- Supply chain attacks (mencionada en taxonomía, sin desarrollo).
- NIST AI RMF (solo en bullet de cierre de Cap. 09).
- Multi-agent security (no abordado explícitamente).
- Secure CI/CD para IA (bullet en cierre de Cap. 10, sin sección propia).
- Elusibilidad de guardrails y WAFs semánticos (ausente).

---

## 7. Valoración global

El Módulo 9 es un módulo bien estructurado con un esqueleto temático completo para los temas de mayor relevancia operacional en AI Security Engineering en 2024-2025. La precisión técnica es alta, las referencias son verificables, y la progresión de amenazas a controles a compliance es pedagógicamente correcta. El módulo puede expandirse directamente a texto completo sin cambios estructurales mayores, con las siguientes prioridades editoriales antes de publicar:

- **Imprescindible:** añadir supply chain security como tema desarrollado (Recomendación 2) y conectar explícitamente con Módulo 8 (Recomendación 1).
- **Importante:** ampliar NIST AI RMF (Recomendación 3) y multi-agent security (Recomendación 4).
- **Recomendable:** reordenar Cap. 07 (Recomendación 5), añadir tabla de control matrix (Recomendación 6), y alternativas on-premises (Recomendación 7).
- **Calidad editorial:** referencias canónicas de herramientas (Recomendación 8), ajuste de Cap. 03 Sec. 01 (Recomendación 9), y verificación de referencias normativas (Recomendación 10).

El módulo está a la altura del perfil declarado del lector — AI Engineer o Arquitecto de IA — y cubre el espectro de AI Security Engineering con la profundidad técnica que justifica su posición en un libro de ingeniería de IA avanzada.
