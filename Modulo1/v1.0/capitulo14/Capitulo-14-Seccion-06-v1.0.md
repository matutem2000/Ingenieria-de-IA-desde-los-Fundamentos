# Capitulo-14-Seccion-06-v1.0

# Capítulo 14 --- Casos de Estudio de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"En los dominios de alta criticidad, la IA debe aumentar la capacidad
> de los profesionales, nunca reemplazar su juicio."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar un caso de estudio aplicado al sector salud.
-   Comprender el papel de la IA como sistema de apoyo a la decisión
    clínica.
-   Identificar restricciones éticas, regulatorias y técnicas.
-   Diseñar una arquitectura que priorice seguridad, trazabilidad y
    supervisión humana.

------------------------------------------------------------------------

# Caso de estudio 5 --- Asistente clínico para apoyo al diagnóstico

## Contexto

Una red de centros médicos busca reducir el tiempo necesario para
analizar antecedentes clínicos y estudios complementarios antes de la
consulta.

El objetivo consiste en asistir al profesional de la salud mediante un
sistema capaz de resumir información relevante, identificar posibles
diagnósticos diferenciales y sugerir estudios complementarios, sin
reemplazar la decisión médica.

La organización entiende que el valor de la IA reside en acelerar el
análisis de información, no en automatizar el acto médico.

------------------------------------------------------------------------

# Restricciones

El equipo de arquitectura identifica requisitos no negociables:

-   cumplimiento de la normativa sobre protección de datos personales;
-   acceso únicamente a historias clínicas autorizadas;
-   registro completo de todas las recomendaciones generadas;
-   posibilidad de justificar cada sugerencia mediante evidencia
    clínica;
-   validación obligatoria por un profesional antes de cualquier
    decisión.

Estas restricciones condicionan tanto la arquitectura como la selección
del modelo.

------------------------------------------------------------------------

# Arquitectura propuesta

``` mermaid
flowchart LR
A[Médico] --> B[Aplicación Clínica]
B --> C[Motor RAG]
C --> D[Historia Clínica]
C --> E[Guías Médicas]
C --> F[LLM]
F --> G[Sugerencias]
G --> H[Validación Profesional]
H --> I[Registro Clínico]
```

------------------------------------------------------------------------

# Decisiones arquitectónicas

  -----------------------------------------------------------------------
  Decisión                     Justificación
  ---------------------------- ------------------------------------------
  Arquitectura RAG             Basar las respuestas en evidencia clínica
                               actualizada

  Acceso mediante permisos     Proteger información sensible

  Explicabilidad               Permitir justificar cada recomendación

  Auditoría completa           Cumplimiento normativo

  Validación humana            Reducir riesgos clínicos
  obligatoria                  
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Resultados esperados

La solución busca obtener beneficios concretos sin comprometer la
seguridad del paciente:

-   reducción del tiempo de revisión documental;
-   mayor acceso a evidencia científica relevante;
-   disminución de omisiones durante el análisis inicial;
-   mejora en la consistencia de la información presentada al
    profesional.

En ningún caso el sistema reemplaza el criterio del médico.

------------------------------------------------------------------------

# Riesgos identificados

El análisis arquitectónico identifica varios riesgos potenciales.

  -----------------------------------------------------------------------
  Riesgo           Estrategia de mitigación
  ---------------- ------------------------------------------------------
  Alucinaciones    RAG y referencias obligatorias
  del modelo       

  Información      Actualización continua de fuentes
  clínica          
  desactualizada   

  Exceso de        Interfaces que distingan recomendaciones de decisiones
  confianza del    
  usuario          

  Accesos          Autenticación y autorización estrictas
  indebidos        
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Buenas prácticas

-   Utilizar únicamente fuentes médicas verificadas.
-   Mostrar siempre la evidencia utilizada para generar una
    recomendación.
-   Registrar todas las interacciones con fines de auditoría.
-   Mantener procesos permanentes de evaluación clínica del sistema.

------------------------------------------------------------------------

# Ideas clave

-   La IA constituye un sistema de apoyo, no un sustituto del
    profesional.
-   La explicabilidad adquiere especial importancia en dominios
    críticos.
-   La arquitectura debe equilibrar innovación, seguridad y cumplimiento
    regulatorio.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección analizaremos un caso de estudio correspondiente al
sector público, donde la Inteligencia Artificial se utiliza para asistir
procesos administrativos de gran escala manteniendo transparencia,
trazabilidad y control institucional.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
