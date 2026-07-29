# Capítulo 04 — Sección 03

# Arquitectura general de memoria

Un sistema de memoria en IA no es una base de datos con un modelo de lenguaje conectado. Es un conjunto de componentes que trabajan de forma coordinada para capturar, organizar, almacenar, recuperar e inyectar información en el momento correcto. Cuando uno de estos componentes falla o no existe, el sistema entero produce comportamientos degradados que suelen diagnosticarse erróneamente como problemas del modelo.

Esta sección presenta la arquitectura completa. Las secciones siguientes desarrollan cada componente con profundidad técnica.

## Los cinco componentes de un sistema de memoria

Un sistema de memoria bien diseñado tiene cinco componentes funcionales:

```
[ENTRADA / CONVERSACIÓN]
         |
         v
  [1. CAPTURA]
    ¿Qué vale la pena recordar?
         |
         v
  [2. PROCESAMIENTO]
    ¿Cómo se estructura y clasifica?
         |
         v
  [3. ALMACENAMIENTO]
    ¿Dónde y con qué formato?
         |
    ----+----
    |       |
    v       v
[Episódico] [Semántico] [Procedimental]
    |       |
    ----+----
         |
         v
  [4. RECUPERACIÓN]
    ¿Qué es relevante para esta consulta?
         |
         v
  [5. INYECCIÓN]
    ¿Cómo se incorpora al contexto activo?
         |
         v
[MODELO DE LENGUAJE / RESPUESTA]
```

### Componente 1: Captura

La captura es el momento en que el sistema decide qué información de la interacción actual merece ser almacenada para uso futuro. Este componente es el más crítico y el más descuidado en implementaciones ingenuas.

Una captura indiscriminada —guardar todo— produce bases de memoria ruidosas, costosas de consultar y propensas a recuperar información irrelevante. Una captura demasiado restrictiva produce sistemas que no aprenden nada útil de la interacción.

Los criterios de captura deben responder a preguntas como:
- ¿Esta información es relevante en conversaciones futuras o solo en esta sesión?
- ¿Es un hecho factual sobre el usuario, el dominio o la aplicación?
- ¿Hay una preferencia, restricción o acuerdo que el sistema debería recordar?
- ¿Esta información contradice o actualiza algo ya almacenado?

La captura puede ser **explícita** —el usuario o el agente indica deliberadamente que algo debe recordarse— o **implícita** —el sistema infiere qué vale la pena guardar basándose en criterios predefinidos.

### Componente 2: Procesamiento

Antes de almacenar, la información capturada necesita ser procesada: clasificada por tipo (episódica, semántica, procedimental), normalizada en formato, y potencialmente fusionada con registros existentes.

El procesamiento también incluye la **extracción de entidades y relaciones**: si el usuario menciona "mi cliente del sector energético en Buenos Aires", el procesamiento extrae "cliente", "sector energético" y "Buenos Aires" como entidades relacionadas, en lugar de guardar la frase literal. Esta representación estructurada habilita recuperaciones más precisas.

En sistemas avanzados, el procesamiento incluye un paso de **resolución de conflictos**: si la memoria existente dice que el usuario trabaja en el sector bancario y la nueva interacción dice que trabaja en energía, el sistema debe resolver la contradicción, no acumularla.

### Componente 3: Almacenamiento

El almacenamiento no es un componente único sino una capa con múltiples backends según el tipo de memoria:

- **Almacenamiento de memoria episódica:** bases de datos relacionales o documentales que registran eventos, conversaciones e interacciones con sus metadatos temporales (timestamp, sesión, usuario, herramientas usadas).

- **Almacenamiento de memoria semántica:** bases de datos vectoriales para recuperación por similitud semántica, bases de datos key-value para perfiles estructurados, o grafos de conocimiento para representar relaciones complejas entre entidades.

- **Almacenamiento de memoria procedimental:** generalmente archivos de configuración, system prompts versionados o repositorios de plantillas. En agentes avanzados, puede incluir bases de datos de flujos de trabajo.

La elección del backend depende de cómo se va a recuperar la información. Si la recuperación será por búsqueda exacta de un campo (el nombre del cliente, el ID de un proyecto), un key-value store es suficiente. Si la recuperación será por similitud conceptual ("algo parecido a lo que preguntó antes"), se necesita una base de datos vectorial. Si las relaciones entre entidades son parte del modelo de datos, un grafo de conocimiento puede ser la opción correcta.

### Componente 4: Recuperación

La recuperación es el proceso de encontrar, entre todo lo almacenado, lo que es relevante para la consulta o tarea actual. Es el componente que determina si el sistema produce respuestas contextualizadas o respuestas genéricas, aunque la memoria esté bien poblada.

Las estrategias de recuperación incluyen:

- **Recuperación por clave:** se sabe exactamente qué buscar (el perfil del usuario con ID específico, el resumen de la última sesión).
- **Recuperación semántica:** se busca por similitud con la consulta actual. Requiere embeddings y búsqueda vectorial.
- **Recuperación por tiempo:** se recuperan los N registros más recientes, o los registros dentro de una ventana temporal.
- **Recuperación híbrida:** combinación de criterios, por ejemplo, los registros más recientes y semánticamente más similares a la consulta actual.

Un sistema de recuperación mal diseñado puede recuperar información desactualizada, información de baja relevancia, o directamente no encontrar información relevante que sí existe en el almacenamiento.

### Componente 5: Inyección

La inyección es el acto de incorporar la memoria recuperada al contexto activo del modelo. No es trivial: la información recuperada compite por espacio en la ventana de contexto con las instrucciones del sistema, el historial de la conversación actual, los resultados de herramientas y la consulta del usuario.

Las decisiones de inyección incluyen:
- ¿Dónde en el contexto se coloca la memoria recuperada? (al inicio del system prompt, como bloque separado, intercalada con el historial)
- ¿En qué formato? (texto plano, JSON estructurado, bullets)
- ¿Cuánta memoria se inyecta? (los 3 registros más relevantes, los últimos 5 eventos, el perfil completo del usuario)
- ¿Cómo se indica al modelo qué es memoria y qué es contexto actual?

Una inyección bien diseñada hace que el modelo use la memoria sin esfuerzo. Una inyección mal diseñada produce confusión entre lo que pasó antes y lo que está pasando ahora, o simplemente consume tokens sin mejorar la respuesta.

## El ciclo completo en una interacción real

Para concretar la arquitectura, trazamos el ciclo completo en un ejemplo:

Un usuario de un asistente de análisis financiero pregunta: "¿Puedes preparar un borrador del informe de riesgo para este trimestre?"

1. **Captura previa:** En conversaciones anteriores, el sistema capturó que este usuario trabaja con tres fondos de inversión, que prefiere informes con resumen ejecutivo al inicio, y que el trimestre anterior señaló exposición al riesgo cambiario como prioridad.

2. **Recuperación:** Al recibir la nueva consulta, el sistema activa la recuperación semántica con "informe de riesgo" como ancla. Recupera: el perfil del usuario, el template de informe aprobado en la sesión anterior, y el registro del comentario sobre riesgo cambiario.

3. **Inyección:** Los tres elementos recuperados se incorporan al contexto activo como bloque de "contexto del usuario" antes del historial de la sesión actual.

4. **Respuesta:** El modelo genera un borrador que incluye la estructura preferida, los fondos relevantes y menciona el riesgo cambiario como ítem de atención prioritaria.

5. **Captura posterior:** El sistema registra que el usuario solicitó un informe de riesgo en este trimestre, qué draft se generó, y si el usuario lo aprobó o lo modificó. Este registro alimenta la memoria episódica para la próxima sesión.

---

*La siguiente sección profundiza en la memoria conversacional: el tipo de memoria más cercano a la ventana de contexto, sus estrategias de gestión, y las decisiones de diseño que determinan cuánto del historial de una conversación vale la pena mantener activo.*
