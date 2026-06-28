# Capítulo 5 --- Sección 07 de 10

# Seguridad y Gobierno en Plataformas de IA

**Versión:** 1.0\
**Estado:** FINAL

------------------------------------------------------------------------

> *"La potencia de una plataforma de IA se mide por lo que puede hacer.
> Su madurez se mide por aquello que decide no permitir."*

## Objetivos de aprendizaje

Al finalizar esta sección podrás:

-   Comprender los principios de seguridad aplicados a plataformas de
    IA.
-   Diferenciar autenticación, autorización y gobierno.
-   Diseñar mecanismos para proteger modelos, datos y herramientas.
-   Incorporar controles de cumplimiento y uso responsable desde la
    arquitectura.

------------------------------------------------------------------------

# Introducción

La adopción de modelos fundacionales introduce nuevos riesgos.

Un agente puede acceder a sistemas corporativos.

Un asistente puede consultar documentación confidencial.

Un modelo puede invocar herramientas capaces de modificar información
crítica.

En consecuencia, la seguridad deja de limitarse a la infraestructura.

Debe extenderse al comportamiento completo de la plataforma.

------------------------------------------------------------------------

# Seguridad por diseño

Los controles de seguridad no deberían añadirse al finalizar el
proyecto.

Deben formar parte de la arquitectura desde el primer día.

Esto implica definir:

-   identidades;
-   permisos;
-   límites operativos;
-   políticas de uso;
-   mecanismos de auditoría;
-   controles sobre modelos y herramientas.

Cada componente debe operar bajo el principio del **menor privilegio**.

------------------------------------------------------------------------

# Autenticación y autorización

Es importante distinguir ambos conceptos.

**Autenticación**

Responde a la pregunta:

> ¿Quién realiza la solicitud?

**Autorización**

Responde a una pregunta diferente:

> ¿Qué operaciones puede realizar ese usuario?

En plataformas de IA ambas verificaciones deben realizarse antes de
acceder a modelos, herramientas o repositorios documentales.

------------------------------------------------------------------------

# Gestión de secretos

Los agentes suelen consumir múltiples servicios.

Por ejemplo:

-   APIs externas;
-   bases de datos;
-   servicios de correo;
-   proveedores de modelos;
-   almacenamiento en la nube.

Las credenciales nunca deberían incorporarse en prompts, código fuente o
archivos de configuración sin protección.

La plataforma debe utilizar mecanismos centralizados de gestión de
secretos.

------------------------------------------------------------------------

# Protección de datos

No toda la información puede tratarse del mismo modo.

Una arquitectura empresarial debería contemplar:

-   clasificación de datos;
-   cifrado en tránsito;
-   cifrado en reposo;
-   anonimización cuando corresponda;
-   políticas de retención;
-   eliminación segura.

Además, el acceso mediante RAG debe respetar exactamente las mismas
reglas que el resto de la organización.

La búsqueda semántica no debe convertirse en un mecanismo para eludir
permisos.

------------------------------------------------------------------------

# Gobierno de modelos

Una plataforma madura administra el uso de modelos mediante políticas.

Entre ellas:

-   modelos autorizados;
-   versiones aprobadas;
-   límites de contexto;
-   proveedores habilitados;
-   restricciones regulatorias;
-   criterios de actualización.

Estas decisiones pertenecen al gobierno tecnológico y no a cada
aplicación individual.

------------------------------------------------------------------------

# Gobierno de herramientas

Las herramientas representan uno de los puntos de mayor riesgo.

Por ello conviene definir:

-   catálogo autorizado;
-   permisos por herramienta;
-   límites de ejecución;
-   validación de parámetros;
-   aprobación humana cuando corresponda;
-   auditoría de todas las invocaciones.

La plataforma controla las herramientas.

El modelo únicamente solicita su utilización.

------------------------------------------------------------------------

# Arquitectura de referencia

``` mermaid
flowchart LR

U[Usuario]
--> IAM[Identidad]

IAM --> AUTH[Autorización]

AUTH --> ORQ[Orquestador]

ORQ --> POL[Políticas]

POL --> LLM[Modelo]
POL --> TOOLS[Herramientas]
POL --> RAG[RAG]

TOOLS --> AUD[Auditoría]
RAG --> AUD
LLM --> AUD
```

La seguridad atraviesa toda la arquitectura.

No constituye un componente aislado.

------------------------------------------------------------------------

# Cumplimiento normativo

Dependiendo del sector, la plataforma puede estar sujeta a requisitos
adicionales.

Algunos ejemplos incluyen:

-   protección de datos personales;
-   conservación de registros;
-   explicabilidad de decisiones;
-   auditorías externas;
-   segregación de funciones;
-   trazabilidad completa.

El diseño debe contemplar estas obligaciones desde el inicio.

------------------------------------------------------------------------

# Caso de estudio

Una entidad financiera desarrolla un agente para asistir a los analistas
de riesgo.

El agente puede consultar información de clientes, pero no modificarla.

Cuando una solicitud requiere actualizar un registro, el orquestador
bloquea la operación y genera un flujo de aprobación para un usuario
autorizado.

La restricción no depende del modelo.

Forma parte de la política de gobierno de la plataforma.

------------------------------------------------------------------------

# Buenas prácticas

-   Aplicar el principio del menor privilegio.
-   Centralizar identidades y permisos.
-   Gestionar secretos mediante servicios especializados.
-   Auditar todas las operaciones sensibles.
-   Mantener un catálogo controlado de modelos y herramientas.
-   Incorporar revisiones periódicas de seguridad y cumplimiento.

------------------------------------------------------------------------

# Ideas clave

-   La seguridad debe diseñarse como una capacidad transversal.
-   Modelos, herramientas y datos requieren controles independientes.
-   Gobierno y cumplimiento son responsabilidades de la plataforma.
-   Las políticas deben implementarse en la arquitectura y no en los
    prompts.

------------------------------------------------------------------------

## Próxima sección

En la siguiente sección estudiaremos la escalabilidad y resiliencia de
plataformas de IA, analizando estrategias para operar modelos, agentes y
servicios de inferencia bajo alta demanda sin comprometer disponibilidad
ni costos.

------------------------------------------------------------------------

> **Un arquitecto no memoriza respuestas. Comprende problemas para poder
> diseñar soluciones.**
