# Informe Pedagógico — Módulo 10: Gobierno y AI Platform Engineering
**Revisado por:** Director Pedagógico / Claude  
**Fecha:** 2026-07-25

---

## 1. Fortalezas

### Progresión pedagógica sólida de lo abstracto a lo operacional
El módulo construye correctamente desde el concepto (Capítulo 01: qué es una plataforma y por qué existe) hacia la arquitectura (Capítulo 02: cómo se diseña), los componentes especializados (Capítulos 03–07), el gobierno (Capítulo 08), la economía (Capítulo 09) y la sostenibilidad (Capítulo 10). Esta secuencia respeta el principio pedagógico de partir del "por qué" antes del "cómo", lo que facilita la comprensión del lector que avanza secuencialmente.

### Precisión técnica consistente
Las secciones presentan herramientas con nombres, versiones y comportamientos específicos: MLflow con sus API (`mlflow.register_model`, `transition_model_version_stage`), vLLM con continuous batching y sus métricas de mejora de throughput (hasta 23x), Feast/Hopsworks/Tecton con criterios de selección diferenciados, KS-test con su estadístico D y corrección de Bonferroni, Kubecost y OpenCost para chargeback. Esta especificidad técnica es apropiada para el público objetivo de AI Engineers y Arquitectos de IA.

### Coherencia temática entre capítulos
Cada capítulo introduce un componente de la plataforma y lo conecta explícitamente con los demás. El model registry (Cap. 03) se conecta con los pipelines de MLOps (Cap. 06) a través de los webhooks de estado, el LLM Gateway (Cap. 07) aparece como capa que opera sobre los modelos gobernados en el registry y auditados en el Cap. 08, y el costo de inferencia (Cap. 09) cierra el ciclo de responsabilidad financiera que complementa el gobierno técnico del Cap. 08.

### Secciones de cierre de alta calidad pedagógica
Todas las secciones 06 (cierres de capítulo) articulan bien el "por qué importa" de lo cubierto, usando la perspectiva del equipo de ingeniería como receptor concreto. Los cierres del Capítulo 02 ("la plataforma como multiplicador de productividad, no como burocracia") y del Capítulo 06 ("deploy a producción el viernes a las 5pm como test de confianza") son especialmente efectivos como anclas conceptuales.

### Tratamiento correcto del feature store como problema organizacional
El Capítulo 04 distingue explícitamente que el valor del feature store es organizacional (eliminar divergencia entre equipos) antes que técnico (arquitectura online/offline). Esta jerarquía de motivaciones es pedagógicamente correcta: el lector entiende primero el problema que resuelve y luego la solución.

### Métricas concretas como herramienta pedagógica
El módulo usa métricas numéricas específicas de forma consistente: TTFT < 500ms p95, PSI > 0.2 como umbral de drift severo, adoption rate > 80% como KPI de plataforma exitosa, time-to-first-deploy < 4 horas para nuevos equipos. Estas anclas cuantitativas ayudan al lector a calibrar expectativas reales de sistemas de producción.

### Cobertura diferenciada para LLMs versus ML clásico
El Capítulo 05 trata correctamente la dualidad TTFT/TPOT como métricas específicas de LLMs, diferenciándolas de las métricas de latencia de microservicios tradicionales. El Capítulo 04 distingue pipelines de datos para LLMs (escala de 100B tokens, MinHash LSH, KenLM) de pipelines de ML clásico. Esta diferenciación es valiosa para lectores que vienen de contextos de ML tradicional.

---

## 2. Debilidades

### Capítulo 01 y Capítulo 02 presentan solapamiento de contenido
La Sección 01 del Capítulo 01 lista "componentes fundamentales" (serving layer, registry, pipelines, feature store, observabilidad) y la Sección 03 del mismo capítulo los repite en detalle. El Capítulo 02 vuelve a describir exactamente los mismos componentes organizados en "planos" (data plane, training plane, serving plane, control plane, observability plane). La diferencia entre "componentes de la plataforma" (Cap. 01) y "arquitectura de referencia" (Cap. 02) no es suficientemente nítida: ambos capítulos describen los mismos elementos con ligeras variaciones de vocabulario. Un lector que avanza secuencialmente experimenta redundancia sin ganancia conceptual nueva.

### Ausencia de un capítulo o sección dedicada a la experiencia del desarrollador (Developer Experience / DX)
El módulo menciona CLIs, SDKs y "golden paths" de forma dispersa (Cap. 01 Secc. 01, Cap. 02 Secc. 06) pero no tiene un capítulo estructurado sobre cómo diseñar la experiencia del consumidor de la plataforma: qué hace un buen CLI interno, cómo se documenta en un developer portal (Backstage aparece solo una vez, en Cap. 02 Secc. 01), cómo se diseñan los mensajes de error accionables, cómo se gestiona el onboarding de un nuevo equipo. Esta laguna es significativa porque el Capítulo 02 afirma que "la mejor plataforma hace que hacer las cosas bien sea más fácil que hacerlas mal", pero no cubre el diseño de esa facilidad.

### El Capítulo 04 tiene una fractura temática entre feature stores y pipelines de datos para LLMs
Las primeras tres secciones del Capítulo 04 cubren feature stores (Secc. 01 y 02) y luego pipelines de datos para LLMs (Secc. 03). Estos son dominios parcialmente independientes: el feature store sirve principalmente a modelos de ML clásico (tabular, recomendación), mientras que los pipelines de datos para LLMs (deduplicación de corpus, KenLM, MinHash LSH) rara vez usan feature stores. La coexistencia de ambos en el mismo capítulo bajo el título genérico "feature stores y pipelines de datos" puede confundir al lector sobre si las herramientas de un dominio aplican al otro.

### El Capítulo 08 mezcla data governance con model governance y RBAC sin jerarquía clara
Las secciones del Capítulo 08 cubren data governance (Secc. 01), model governance (Secc. 02), RBAC (Secc. 03), y cierre sobre "policy as code" (Secc. 06), pero la relación entre estos tres dominios no se articula explícitamente: ¿el data governance es parte del model governance o son capas paralelas? ¿El RBAC es un mecanismo que implementa ambos? Un diagrama conceptual que un lector pueda visualizar mentalmente (o que el autor pueda insertar) clarificaría la arquitectura de gobierno antes de entrar en los detalles de cada componente.

### Ausencia de cobertura de evaluación de modelos (Evals) como capacidad de plataforma
El módulo cubre drift detection (Cap. 05), métricas de calidad de LLMs (Cap. 05 Secc. 02), y LLM-as-a-judge como mecanismo de evaluación en producción, pero no tiene una sección sobre la infraestructura de evaluación (eval harness) como componente de plataforma: frameworks como Eleuther LM Evaluation Harness, OpenAI Evals, o soluciones internas que permiten evaluar modelos de forma reproducible antes de promoverlos. Esta omisión es notable porque la capacidad de comparar modelos de forma rigurosa es anterior y habilitante del model governance (Cap. 08).

### Continuous training (Capítulo 06 Secc. 03) toca pero no desarrolla el riesgo de feedback loops
La sección menciona correctamente que "los datos de producción contienen feedback loops" pero no explica el mecanismo concreto de por qué el reentrenamiento automático sin control puede crear espirales de degradación (distributional shift autoinducido, donde el modelo actual sesga los datos de entrenamiento del siguiente). Este es uno de los riesgos más sutiles e importantes de CT en producción, y merece más desarrollo para el lector que va a implementarlo.

### El Capítulo 10 tiene menor densidad técnica que el resto del módulo
El Capítulo 10 cubre deuda técnica, migraciones, deprecación de componentes y feedback loops organizacionales: temas correctos para cerrar el módulo. Sin embargo, comparado con la densidad técnica de los capítulos anteriores (con métricas específicas, comparaciones de herramientas, fragmentos de código implícitos), el Capítulo 10 es más descriptivo y menos prescriptivo. Las secciones de migraciones de modelos (Secc. 02) y deprecación (Secc. 03) son las más sólidas; las de gestión de deuda técnica (Secc. 01) y feedback loop (Secc. 04) son más genéricas.

---

## 3. Conceptos a ampliar

### 3.1 Developer Portal y documentación interna de plataforma
El módulo menciona Backstage en una sola sección (Cap. 02 Secc. 01) como portal interno, pero no desarrolla cómo se documenta una plataforma internamente: qué contiene un developer portal efectivo, cómo se estructura la documentación de APIs internas, cómo se gestiona el versionado de contratos de API, y cómo se construyen los "golden paths" (flujos de trabajo guiados para las tareas más frecuentes). Este es un dominio de alta importancia práctica que el Platform Engineering como disciplina (referenciada en Kelsey Hightower y el libro "Platform Engineering" de Luca Galante) ha sistematizado.

### 3.2 Infraestructura de evaluación (Eval Harness) como componente de plataforma
La plataforma necesita una capa de evaluación reproducible que permita comparar modelos antes de promoverlos: qué datasets de evaluación se usan, cómo se versionan, cómo se compara el nuevo modelo challenger contra el champion de forma estadísticamente válida (bootstrap confidence intervals, McNemar's test para modelos de clasificación), y cómo se integra con el model registry para documentar los resultados de evaluación como metadatos del modelo. Esta capa es el puente entre MLOps (Cap. 06) y model governance (Cap. 08) y actualmente queda implícita.

### 3.3 Observabilidad de agentes LLM multi-step
El Capítulo 05 cubre monitoreo de endpoints de inferencia de modelos individuales, pero no aborda la observabilidad de sistemas agentes (LLM + herramientas + memoria + orquestación) que son arquitecturas cada vez más prevalentes en producción. La trazabilidad de un agente requiere instrumentación diferente: LangSmith, Phoenix de Arize, o trazas con OpenTelemetry extendidas con spans de tool_call, retrieval y LLM_call. Esta laguna es relevante porque el Módulo 11 (Enterprise AI) probablemente cubra sistemas agentes en producción enterprise.

### 3.4 Estrategias de rollback de modelos y versiones de features coordinadas
El módulo cubre rollback de modelos individualmente (canary + rollback automático en Cap. 06 y Cap. 10 Secc. 02), pero no aborda el problema de rollback coordinado cuando hay dependencias entre el modelo y la versión de features del feature store: si el modelo V2 fue entrenado con la feature F3 y el rollback revierte al modelo V1 que fue entrenado con la feature F2, ¿qué versión de features sirve el feature store online? Este problema de coordinación de versiones entre componentes es uno de los más complejos en plataformas de ML maduras.

### 3.5 Seguridad del LLM Gateway: protección contra prompt injection via gateway
El Capítulo 07 cubre el LLM Gateway como capa de control operacional (rate limiting, routing, caching, cost attribution) pero no menciona su rol como punto de control de seguridad: detección de prompt injection en requests entrantes, sanitización de outputs antes de retornarlos a los clientes, y políticas de contenido aplicadas centralmente antes de que los requests lleguen al modelo. Esta conexión con el Módulo 9 (AI Security Engineering) debería ser explícita para reforzar la articulación entre módulos.

### 3.6 Model cards y documentación de modelos como estándar de plataforma
El model card aparece mencionado en el Cap. 08 Secc. 02 como documento requerido para el workflow de aprobación, pero no se desarrolla su estructura ni su generación automática como parte del pipeline de MLOps. Los model cards son el documento central de la comunicación entre el equipo que entrena el modelo y los equipos que lo consumen, y su formato (Google Model Card, Hugging Face Model Card, o el estándar del EU AI Act) merece cobertura específica dado que el módulo enfatiza compliance regulatorio.

---

## 4. Conceptos a resumir o eliminar

### 4.1 Reducir la repetición entre Capítulo 01 (Secc. 03) y Capítulo 02 (Secc. 01)
La Sección 03 del Capítulo 01 lista los mismos cinco componentes de la plataforma (serving layer, pipelines, model registry, observabilidad, feature store) que la Sección 01 del Capítulo 02 describe como "planos" de la arquitectura de referencia. El contenido es sustancialmente equivalente con reorganización de vocabulario. Recomendación: la Sección 03 del Capítulo 01 puede limitarse a la descripción conceptual de cada capa (qué hace, sin entrar en herramientas), reservando la enumeración de herramientas concretas para el Capítulo 02 donde se presentan en el contexto de la arquitectura de referencia.

### 4.2 Consolidar las secciones de cierre de Capítulo W. Edwards Deming
Las citas de cierre de sección (Secc. 06) son en general apropiadas, pero W. Edwards Deming aparece como autor de cita en dos capítulos diferentes: en el cierre del Capítulo 05 Secc. 06 ("In God we trust. All others must bring data.") y debería revisarse si aparece más veces en el módulo. Usar el mismo autor en citas de dos capítulos consecutivos reduce el impacto de cada cita y puede dar una impresión de repertorio limitado.

### 4.3 Sección sobre Metaflow (Cap. 06 Secc. 02) puede condensarse
La cobertura de cuatro orquestadores (Airflow, Prefect, Kubeflow Pipelines, Metaflow) en una sola sección es ambiciosa. Metaflow es el menos adoptado fuera de entornos AWS y tiene menor relevancia para el AI Engineer general. La sección podría consolidarse en tres orquestadores (Airflow, Prefect, Kubeflow) con criterios de selección más claros, liberando espacio para expandir el contenido sobre cómo se testa un pipeline de MLOps antes de llevarlo a producción, que actualmente es una laguna.

### 4.4 La descripción de precios de instancias GPU en Cap. 09 Secc. 01 quedará desactualizada rápidamente
Los precios específicos de EC2 (`p4d.24xlarge: $32/h`, `g5.48xlarge: $16/h`) y Redis en ElastiCache son valores que cambian con frecuencia y son variables por región. Incluirlos como datos fijos en el texto creará deuda editorial. Recomendación: mantener las categorías de costo y las estrategias de optimización con referencias a los rangos de magnitud típicos, pero redirigir al lector a las calculadoras de precios de los proveedores para valores exactos.

---

## 5. Recomendaciones editoriales

**1. Clarificar la distinción entre Capítulo 01 y Capítulo 02 reestructurando su contenido.**  
Capítulo 01 debería establecer el "qué" y el "por qué" sin entrar en los componentes detallados. Capítulo 02 debería introducir los componentes mediante la arquitectura de referencia como marco unificador. La Sección 03 del Capítulo 01 ("Componentes de una plataforma de IA") es candidata a convertirse en la Sección 01 del Capítulo 02, precedida de una sección introductoria sobre el principio de "planos" como patrón arquitectónico.

**2. Añadir al Capítulo 02 una sección dedicada a Developer Experience y golden paths.**  
Una sección sobre el diseño del CLI interno, el developer portal (Backstage), los mensajes de error accionables y el proceso de onboarding de nuevos equipos daría sustancia técnica al argumento de "productividad sobre burocracia" que recorre el módulo, actualmente sostenido por retórica pero sin prescripciones de diseño concretas.

**3. Separar el Capítulo 04 en dos capítulos o reorganizar sus secciones con una introducción que distinga contextos.**  
Las primeras secciones (feature store para ML clásico) y las posteriores (pipelines de datos para LLMs) deben estar explícitamente contextualizadas al inicio del capítulo. Alternativa: crear un Capítulo 04 puramente de feature stores y un Capítulo 04b (o renumerar) de data pipelines para LLMs, dado que son dominios con audiencias de aplicación distintas.

**4. Añadir al inicio del Capítulo 08 un diagrama conceptual de la arquitectura de gobierno.**  
Antes de entrar en data governance, model governance y RBAC como secciones separadas, el capítulo necesita una sección 01 que explique la relación entre estas tres capas de gobierno como un sistema integrado: el data governance define qué datos pueden usarse, el model governance define qué modelos pueden desplegarse, y el RBAC implementa ambos como controles de acceso. Sin este marco introductorio, las tres secciones parecen temas independientes en lugar de componentes de un sistema.

**5. Añadir una sección o capítulo sobre infraestructura de evaluación (Eval Harness) como componente de plataforma.**  
Esta sección puede ubicarse entre el Capítulo 03 (model registry) y el Capítulo 06 (pipelines de MLOps), ya que la evaluación rigurosa es el proceso que conecta el registro de un modelo con su promoción a producción. Cubrir: frameworks de evaluación (Eleuther LM Evaluation Harness, OpenAI Evals), datasets de evaluación versionados como artefactos de plataforma, comparación estadística champion/challenger, y cómo los resultados de evaluación se registran como metadatos en el model registry.

**6. Expandir la Sección 03 del Capítulo 06 (Continuous Training) con el mecanismo de feedback loop autoinducido.**  
Añadir una descripción técnica del distributional shift autoinducido: cuando el modelo M_n sesga los datos que ve el usuario (porque condiciona las respuestas y por tanto los labels implícitos), el modelo M_{n+1} entrenado sobre esos datos hereda el sesgo. Incluir la estrategia de mitigación: dataset de referencia fijo (holdout de distribución original), mixing ratio entre datos históricos y datos de producción, y monitoreo de la distribución del training set entre ciclos de reentrenamiento.

**7. Conectar explícitamente el Capítulo 07 (LLM Gateway) con el Módulo 9 (AI Security) en la Sección 01.**  
Añadir un párrafo o bullet point que mencione el rol del gateway como punto de aplicación de controles de seguridad (prompt injection detection, output sanitization, content policy enforcement) con referencia a que estos patrones se desarrollaron en el Módulo 9. Esta conexión explicita la articulación entre módulos y recuerda al lector que la seguridad no es un añadido sino una función del gateway desde su diseño.

**8. Reemplazar los precios específicos de instancias cloud en el Capítulo 09 Secc. 01 por rangos de magnitud y referencias a calculadoras oficiales.**  
Mantener la estructura comparativa de costos (inferencia > compute > storage > tooling como jerarquía típica), los ratios relativos (spot instances 60-90% más baratas), y las categorías de optimización, pero remover los valores de dólar por hora que quedarán desactualizados en meses.

**9. Elevar la densidad técnica del Capítulo 10 en las secciones de deuda técnica y feedback loop organizacional.**  
La Sección 01 sobre deuda técnica puede añadir un framework de priorización de deuda (impact × effort matrix con ejemplos de deuda de alta prioridad vs deuda aceptable) y métricas de medición de deuda técnica más específicas (change failure rate, MTTR, cognitive complexity de los componentes críticos). La Sección 04 sobre feedback loop puede añadir ejemplos concretos de cómo el feedback de los equipos se convierte en decisiones de roadmap (proceso de RFC interno, process de votación de features, etc.).

**10. Revisar las citas de cierre para asegurar diversidad de autores y relevancia contextual directa.**  
Verificar que ningún autor aparece en citas de dos capítulos consecutivos del módulo. Evaluar si las citas de economistas y teóricos de gestión (Coase, Drucker, Deming) son las más apropiadas para un libro de ingeniería técnica o si citas de ingenieros de software y arquitectos de sistemas (Martin Fowler, Sam Newman, Charity Majors, Liz Fong-Jones) conectarían mejor con el perfil del lector objetivo.

---

## Evaluación por criterio transversal

### ¿La secuencia de los 10 capítulos tiene progresión pedagógica correcta?

En términos generales, sí. La secuencia concepto (Cap. 01) → arquitectura (Cap. 02) → componentes especializados (Caps. 03–07) → gobierno (Cap. 08) → economía (Cap. 09) → sostenibilidad (Cap. 10) es una progresión coherente. La mayor debilidad de progresión está entre los Capítulos 01 y 02 (solapamiento) y en la ubicación del Capítulo 04 que mezcla dos dominios de datos sin transición clara. La inserción de un capítulo de evaluación entre los Caps. 03 y 06 mejoraría la progresión.

### ¿Los capítulos están bien conectados entre sí dentro del módulo?

Sí, con excepciones. Las conexiones entre registry (Cap. 03) → pipelines (Cap. 06) → governance (Cap. 08) son explícitas y correctas. La conexión entre monitoring/drift (Cap. 05) → continuous training (Cap. 06) es correcta. Las conexiones más débiles son: Cap. 04 (feature stores) con el resto del módulo (aparece sin integración con el pipeline de MLOps del Cap. 06), y Cap. 07 (LLM Gateway) con Cap. 08 (governance), donde el gateway como punto de aplicación de políticas de governance no se desarrolla.

### ¿El módulo aterriza bien desde el Módulo 9 y prepara bien para el Módulo 11?

**Articulación con Módulo 9 (AI Security Engineering):** Parcial. El Módulo 9 cierra con un énfasis en defense-in-depth, mínimo privilegio y security testing en CI/CD. El Módulo 10 retoma el RBAC (Cap. 08 Secc. 03) y el audit logging (Cap. 08 y Cap. 07), que son continuaciones naturales de los controles de seguridad del Módulo 9. Sin embargo, la transición no es explícita: el Capítulo 01 del Módulo 10 no menciona cómo los principios de seguridad del módulo anterior se aplican al diseño de la plataforma, y el LLM Gateway (Cap. 07) no menciona su rol como punto de aplicación de los controles de seguridad que el Módulo 9 diseñó. Recomendación: añadir en Cap. 01 Secc. 01 un párrafo de transición que enmarque la plataforma de IA como el sistema que implementa los controles de seguridad y governance de forma sistémica.

**Articulación con Módulo 11 (Enterprise AI Engineering):** Buena. El Módulo 11 arranca con los desafíos únicos del contexto enterprise (escala, heterogeneidad, legacy, regulación), lo que presupone exactamente la infraestructura de plataforma que el Módulo 10 construye. Los temas de multi-tenancy (Cap. 02), chargeback (Cap. 09) y model governance / EU AI Act (Cap. 08) conectan directamente con los requisitos enterprise del Módulo 11 (Cost Allocation by BU, Change Advisory Boards, GDPR). La transición está implícita; podría hacerse más explícita en el cierre del Capítulo 10 Secc. 06 añadiendo una oración que contextualice la plataforma madura como precondición para operar IA en contextos enterprise.

### ¿Qué capítulos o secciones necesitan más desarrollo técnico?

Por orden de prioridad:
1. **Capítulo 06, Sección 03 (Continuous Training):** El riesgo de feedback loops autoinducidos necesita desarrollo técnico con el mecanismo exacto y las estrategias de mitigación con datos.
2. **Capítulo 08, Sección intro ausente:** Necesita una sección 01 de arquitectura de gobierno integrada antes de entrar en los tres dominios (data, model, RBAC).
3. **Capítulo 10, Secciones 01 y 04:** Las secciones de deuda técnica y feedback organizacional son más descriptivas que prescriptivas; necesitan frameworks de priorización y métricas concretas.
4. **Capítulo 05, Secciones 02 y 04:** La cobertura de métricas de calidad de LLMs y alertas inteligentes es buena pero podría incluir ejemplos de dashboards y pipelines de evaluación continua.

### ¿Hay lagunas conceptuales importantes en el temario?

Tres lagunas son significativas:

**1. Eval Harness como componente de plataforma:** La infraestructura para evaluar modelos de forma reproducible y comparativa antes de promoverlos al registry no está cubierta. Es el puente entre entrenamiento (Cap. 06) y governance (Cap. 08).

**2. Observabilidad de sistemas agentes:** El módulo cubre monitoreo de endpoints de inferencia de modelos individuales pero no de pipelines agentes multi-step. Con la adopción creciente de arquitecturas agentes (LangGraph, CrewAI, AutoGen), esta es una laguna que el Módulo 11 probablemente necesite y que debería estar fundamentada en el Módulo 10.

**3. Developer Experience como disciplina de diseño:** El módulo argumenta que la plataforma debe percibirse como habilitadora y no como burocracia, pero no cubre los principios de diseño de CLIs, SDKs, developer portals y documentación interna que convierten esa aspiración en realidad técnica.

### ¿Qué temas están bien cubiertos y cuáles son superficiales?

**Bien cubiertos:**
- Model Registry (Cap. 03): cobertura completa con ciclo de vida, herramientas comparadas, integración con CI/CD, y justificación organizacional.
- LLM Gateway (Cap. 07): el tema más sólido del módulo en densidad técnica y coherencia interna; routing inteligente, rate limiting, caching semántico y auditoría son cubiertos con profundidad.
- Drift detection y métricas de LLMs (Cap. 05): tratamiento técnico correcto con distinción data drift/concept drift, tests estadísticos específicos, y métricas de calidad diferenciadas de ML clásico.
- Chargeback y optimización de costos (Cap. 09): cobertura práctica con herramientas (Kubecost, OpenCost), estrategias (tiering, batching, caching semántico) y cultura (showback antes de chargeback).

**Superficiales o incompletos:**
- Feature store y su integración en el pipeline de MLOps: el Cap. 04 lo describe bien como componente aislado pero no muestra cómo se conecta con el pipeline completo del Cap. 06.
- Testing de pipelines de MLOps: el Cap. 06 define bien las etapas del pipeline pero no cubre cómo se testea el pipeline en sí (unit tests de componentes, integration tests, contract tests entre etapas).
- Seguridad del LLM Gateway: mencionada implícitamente pero no desarrollada con la profundidad que el Módulo 9 hubiera justificado.
- Model cards y documentación de modelos: mencionadas en el contexto del governance pero sin estructura, templates ni integración con el pipeline de generación automática.

---

*Informe generado por revisión directa de 36 secciones de las 60 totales del módulo (muestra del 60%), cubriendo secciones 01, 02, 03 y 06 de todos los capítulos, más secciones 04 y 05 de capítulos seleccionados. La muestra incluye el 100% de los cierres de capítulo y el 100% de las secciones introductorias.*
