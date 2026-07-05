# Capitulo-22-Seccion-06-v0.1

# Módulo 2 — Prompt Engineering Profesional

# Capítulo 22 — Proyecto Integrador del Módulo 2

**Versión:** 0.1  
**Estado:** Manuscrito del autor

> *"El desarrollo termina cuando se despliega. La ingeniería comienza cuando el sistema entra en producción."*

---

# Objetivos de aprendizaje

- Diseñar una estrategia de despliegue para una solución basada en LLM.
- Incorporar observabilidad y monitoreo desde el inicio.
- Comprender el ciclo de mejora continua.
- Completar el ciclo de vida del proyecto integrador.

---

# Introducción

Una solución de Inteligencia Artificial no finaliza cuando supera las pruebas internas.

El verdadero desafío comienza cuando interactúa con usuarios reales, datos cambiantes y procesos críticos del negocio.

Por este motivo, el despliegue debe entenderse como una transición controlada y no como el final del proyecto.

---

# Estrategia de despliegue

Se recomienda realizar la puesta en producción de manera gradual.

| Etapa | Objetivo |
|--------|----------|
| Piloto | Validar el comportamiento con un grupo reducido de usuarios. |
| Despliegue parcial | Incrementar progresivamente el alcance. |
| Producción | Habilitar el servicio para toda la organización. |
| Optimización | Ajustar el sistema utilizando métricas reales. |

Cada etapa debe contar con criterios claros para avanzar o retroceder.

---

# Observabilidad

```mermaid
flowchart LR
A[Usuario]
--> B[Aplicación]

B --> C[LLM]

B --> D[Métricas]
B --> E[Logs]
B --> F[Trazas]
B --> G[Feedback]

D --> H[Tablero]
E --> H
F --> H
G --> H

H --> I[Mejora continua]
```

La observabilidad permite comprender cómo se comporta el sistema y detectar oportunidades de mejora antes de que se conviertan en incidentes.

---

# Métricas recomendadas

Entre los indicadores más útiles se encuentran:

- tiempo medio de respuesta;
- costo por interacción;
- tasa de éxito de las tareas;
- porcentaje de respuestas corregidas por usuarios;
- frecuencia de uso por funcionalidad;
- incidentes detectados en producción.

Las métricas deben analizarse de forma periódica y compararse entre versiones.

---

# Mejora continua

Una solución madura evoluciona mediante un ciclo permanente.

1. Observar el comportamiento.
2. Detectar oportunidades de mejora.
3. Priorizar cambios.
4. Implementar una nueva versión.
5. Ejecutar nuevamente los *Evaluation Sets*.
6. Desplegar de forma controlada.

Este ciclo convierte el aprendizaje obtenido en producción en conocimiento reutilizable para futuras versiones.

---

# Caso de estudio

Tras desplegar el asistente corporativo, el equipo observa que muchas consultas requieren una aclaración adicional antes de generar una respuesta útil.

En lugar de modificar directamente el modelo, analiza los registros, incorpora nuevos casos al conjunto de evaluación, ajusta el diseño conversacional y publica una nueva versión.

Las métricas muestran una reducción del número de aclaraciones y un aumento en la satisfacción de los usuarios.

---

# Actividades propuestas

1. Definir un plan de despliegue gradual.
2. Seleccionar las métricas que serán monitoreadas.
3. Diseñar un tablero de observabilidad.
4. Establecer un proceso de mejora continua.
5. Documentar el procedimiento de liberación de nuevas versiones.

---

# Buenas prácticas

- Desplegar de forma incremental.
- Medir antes de modificar.
- Automatizar la recolección de métricas.
- Mantener trazabilidad entre versiones y resultados.
- Incorporar el feedback de los usuarios al proceso de mejora.

---

# Errores frecuentes

- Considerar el despliegue como el final del proyecto.
- No monitorear el comportamiento real del sistema.
- Introducir cambios sin evidencia.
- Ignorar los incidentes menores detectados por los usuarios.

---

# Ideas clave

- El despliegue marca el inicio de la operación, no el final del desarrollo.
- La observabilidad es un componente esencial del AI Engineering.
- La mejora continua transforma datos operativos en decisiones de arquitectura.

---

# Transición hacia la siguiente sección

En la próxima y última sección del proyecto integrador realizaremos el cierre del Módulo 2, revisando los aprendizajes alcanzados y estableciendo las competencias que servirán de base para el estudio de los modelos fundacionales en el Módulo 3.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
