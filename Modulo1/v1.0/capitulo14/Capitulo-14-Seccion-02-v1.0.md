# Capitulo-14-Seccion-02-v1.0

# Capítulo 14 --- Casos de Estudio de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"Una buena arquitectura comienza comprendiendo el negocio antes que
> la tecnología."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar un caso empresarial completo basado en Retrieval-Augmented
    Generation (RAG).
-   Comprender el proceso de toma de decisiones arquitectónicas.
-   Evaluar alternativas de implementación considerando restricciones
    reales.
-   Justificar cada componente de la solución propuesta.

------------------------------------------------------------------------

# Caso de estudio 1 --- Asistente corporativo basado en documentación interna

## Contexto

Una organización con más de 2.000 empleados dispone de miles de
documentos distribuidos entre manuales, procedimientos, políticas
internas y normativa técnica.

Los usuarios invierten una cantidad significativa de tiempo buscando
información que ya existe, pero se encuentra dispersa en múltiples
repositorios.

La dirección propone incorporar un asistente conversacional para
responder consultas utilizando exclusivamente la documentación oficial.

El objetivo no consiste en reemplazar a los especialistas, sino en
reducir el tiempo dedicado a localizar información.

------------------------------------------------------------------------

# Restricciones

El equipo de arquitectura identifica las siguientes restricciones:

-   La información contiene datos confidenciales.
-   No puede enviarse documentación a servicios públicos.
-   Los documentos cambian semanalmente.
-   Las respuestas deben indicar la fuente utilizada.
-   El tiempo máximo aceptable de respuesta es de cinco segundos.

Estas condiciones descartan varias alternativas inicialmente
consideradas.

------------------------------------------------------------------------

# Alternativas evaluadas

  -----------------------------------------------------------------------
  Alternativa               Ventajas            Desventajas
  ------------------------- ------------------- -------------------------
  LLM sin contexto          Implementación      Baja precisión documental
                            simple              

  Fine-tuning               Especialización del Alto costo de
                            modelo              mantenimiento

  Arquitectura RAG          Información         Mayor complejidad inicial
                            actualizable y      
                            trazable            
  -----------------------------------------------------------------------

Tras evaluar costos, mantenibilidad y calidad de respuesta, el equipo
selecciona una arquitectura basada en Retrieval-Augmented Generation.

``` mermaid
flowchart LR
A[Empleado] --> B[Aplicación]
B --> C[Motor RAG]
C --> D[Índice vectorial]
D --> E[Documentación]
C --> F[LLM]
F --> G[Respuesta con referencias]
```

------------------------------------------------------------------------

# Decisiones arquitectónicas

El diseño incorpora los siguientes componentes:

-   modelo ejecutado dentro de la infraestructura corporativa;
-   índice vectorial actualizado automáticamente;
-   control de acceso según permisos del usuario;
-   registro de consultas para auditoría;
-   monitoreo de latencia y calidad de respuesta.

Cada componente responde a un requisito concreto del negocio.

------------------------------------------------------------------------

# Resultados esperados

La organización espera obtener:

-   reducción del tiempo de búsqueda de información;
-   menor carga sobre especialistas internos;
-   respuestas consistentes y trazables;
-   actualización continua del conocimiento sin reentrenar el modelo.

------------------------------------------------------------------------

# Buenas prácticas

-   Mantener sincronizada la documentación.
-   Mostrar siempre la fuente de la respuesta.
-   Medir la calidad antes del despliegue general.
-   Implementar una prueba piloto con un área reducida.

------------------------------------------------------------------------

# Ideas clave

-   RAG resulta especialmente adecuado cuando el conocimiento cambia con
    frecuencia.
-   La arquitectura debe responder a restricciones de negocio además de
    requisitos técnicos.
-   La trazabilidad incrementa la confianza en las respuestas generadas.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos un caso de estudio orientado al
desarrollo de software, donde un asistente de IA participa activamente
en el ciclo de vida de una aplicación empresarial.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
