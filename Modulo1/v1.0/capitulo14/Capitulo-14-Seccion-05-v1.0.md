# Capitulo-14-Seccion-05-v1.0

# Capítulo 14 --- Casos de Estudio de Ingeniería de Inteligencia Artificial

**Versión:** 1.0\
**Estado:** Aprobado

> *"El valor de los datos aumenta cuando cualquier persona puede
> transformarlos en conocimiento para tomar decisiones."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Analizar un caso de estudio sobre analítica empresarial asistida por
    IA.
-   Comprender cómo transformar consultas en lenguaje natural en
    consultas sobre un Data Warehouse.
-   Identificar riesgos asociados a la generación automática de
    consultas.
-   Justificar una arquitectura segura y gobernada para analítica
    conversacional.

------------------------------------------------------------------------

# Caso de estudio 4 --- Analítica conversacional sobre un Data Warehouse

## Contexto

Una empresa dispone de un Data Warehouse con información financiera,
comercial y operativa. Aunque los datos están disponibles, la mayoría de
los usuarios depende del área de BI para obtener reportes.

La dirección busca reducir ese cuello de botella mediante un asistente
que permita formular preguntas en lenguaje natural y obtener respuestas
fundamentadas en los datos corporativos.

------------------------------------------------------------------------

# Restricciones

La solución debe cumplir los siguientes requisitos:

-   acceso respetando permisos del usuario;
-   generación exclusiva de consultas de solo lectura;
-   auditoría completa de todas las consultas;
-   validación antes de ejecutar sentencias complejas;
-   integración con herramientas existentes de BI.

------------------------------------------------------------------------

# Arquitectura propuesta

``` mermaid
flowchart LR
A[Usuario] --> B[Aplicación]
B --> C[LLM]
C --> D[Generador SQL]
D --> E[Validador]
E --> F[Data Warehouse]
F --> G[Resultados]
G --> H[Explicación]
```

------------------------------------------------------------------------

# Decisiones arquitectónicas

  -----------------------------------------------------------------------
  Decisión                                Motivo
  --------------------------------------- -------------------------------
  Generación de SQL restringido           Evitar modificaciones sobre los
                                          datos

  Validación sintáctica                   Reducir errores antes de
                                          ejecutar consultas

  Catálogo semántico                      Mejorar la interpretación del
                                          negocio

  Registro de consultas                   Auditoría y mejora continua

  Separación entre IA y base de datos     Mayor seguridad y
                                          mantenibilidad
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Resultados esperados

-   Mayor autonomía de los usuarios de negocio.
-   Reducción de solicitudes repetitivas al área de BI.
-   Acceso más rápido a indicadores relevantes.
-   Mayor trazabilidad en el uso de la información.

------------------------------------------------------------------------

# Buenas prácticas

-   Limitar el alcance del modelo al esquema autorizado.
-   Validar toda consulta antes de ejecutarla.
-   Mostrar la consulta generada cuando corresponda.
-   Mantener actualizado el catálogo de datos del negocio.

------------------------------------------------------------------------

# Ideas clave

-   La IA facilita el acceso a la información, pero no reemplaza el
    gobierno de datos.
-   La seguridad debe formar parte del diseño desde el inicio.
-   La calidad de las respuestas depende tanto del modelo como del
    conocimiento del dominio.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección estudiaremos un caso orientado al sector salud,
donde la Inteligencia Artificial actúa como herramienta de apoyo para el
análisis clínico y la toma de decisiones.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
