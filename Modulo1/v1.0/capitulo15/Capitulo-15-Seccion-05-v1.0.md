# Capitulo-15-Seccion-05-v1.0

# Capítulo 15 --- Evaluación Final y Proyecto Integrador

**Versión:** 1.0\
**Estado:** Aprobado

> *"Toda decisión arquitectónica implica aceptar restricciones y asumir
> responsabilidades."*

------------------------------------------------------------------------

# Objetivos de aprendizaje

-   Diseñar la arquitectura lógica del proyecto integrador.
-   Justificar la selección de cada componente.
-   Relacionar requisitos funcionales y no funcionales con la solución
    propuesta.
-   Comprender cómo construir una arquitectura desacoplada y evolutiva.

------------------------------------------------------------------------

# Arquitectura lógica

Una vez comprendido el problema de negocio, el siguiente paso consiste
en definir los componentes que conformarán la solución.

La arquitectura debe favorecer la evolución independiente de cada
módulo, minimizar el acoplamiento y facilitar la observabilidad.

``` mermaid
flowchart LR
U[Usuario] --> G[Gateway API]
G --> A[Aplicación]
A --> R[Motor RAG]
R --> V[Base Vectorial]
R --> L[LLM]
A --> O[Observabilidad]
A --> I[Identidad]
R --> D[Repositorio Documental]
```

------------------------------------------------------------------------

# Componentes principales

  Componente       Responsabilidad
  ---------------- ------------------------------
  Gateway          Punto único de entrada
  Aplicación       Orquestación de consultas
  Motor RAG        Recuperación de contexto
  Base vectorial   Búsqueda semántica
  LLM              Generación de respuestas
  Observabilidad   Métricas, logs y trazas
  Identidad        Autenticación y autorización

------------------------------------------------------------------------

# Principios de diseño

La arquitectura propuesta se apoya en los siguientes principios:

-   separación de responsabilidades;
-   independencia entre componentes;
-   reemplazo sencillo del modelo;
-   escalabilidad horizontal;
-   monitoreo desde el diseño;
-   seguridad por defecto.

Cada decisión debe responder a un requisito identificado durante el
análisis del problema.

------------------------------------------------------------------------

# Riesgos arquitectónicos

  Riesgo                        Mitigación
  ----------------------------- -----------------------------
  Acoplamiento excesivo         Interfaces bien definidas
  Dependencia de un proveedor   Componentes intercambiables
  Cuellos de botella            Escalado independiente
  Falta de observabilidad       Instrumentación completa

------------------------------------------------------------------------

# Buenas prácticas

-   Diseñar pensando en la evolución futura.
-   Evitar dependencias innecesarias entre módulos.
-   Mantener interfaces estables.
-   Incorporar monitoreo desde la primera versión.

------------------------------------------------------------------------

# Ideas clave

-   La arquitectura debe responder al negocio y no a una tecnología
    específica.
-   El desacoplamiento facilita la evolución de la solución.
-   La observabilidad forma parte del diseño, no del mantenimiento.

------------------------------------------------------------------------

# Transición hacia la siguiente sección

En la próxima sección se abordará la arquitectura física del proyecto,
analizando alternativas de despliegue, escalabilidad y operación.

------------------------------------------------------------------------

> **"Un arquitecto no memoriza respuestas. Comprende problemas para
> poder diseñar soluciones."**
