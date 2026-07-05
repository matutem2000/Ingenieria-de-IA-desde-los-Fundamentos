# Capitulo-21-Seccion-02-v0.1

# Módulo 2 — Prompt Engineering Profesional

# Capítulo 21 — Laboratorios de Prompt Engineering

**Versión:** 0.1  
**Estado:** Manuscrito del autor

> *"Un laboratorio no busca demostrar que una idea funciona. Busca descubrir por qué funciona y cómo mejorarla."*

---

# Objetivos de aprendizaje

- Aplicar un proceso sistemático de diseño de prompts.
- Construir un laboratorio de clasificación de información.
- Evaluar resultados mediante criterios objetivos.
- Introducir la iteración basada en evidencia.

---

# Introducción

La clasificación es una de las tareas más frecuentes en aplicaciones empresariales basadas en LLM.

Asignar una categoría a un correo electrónico, identificar el tipo de incidente de una mesa de ayuda o determinar el área responsable de un expediente son ejemplos habituales.

Aunque estas tareas parecen sencillas, representan un excelente escenario para practicar Prompt Engineering porque permiten medir fácilmente el impacto de pequeños cambios en el diseño del prompt.

---

# El problema

Una organización recibe cientos de consultas diarias.

Cada mensaje debe clasificarse en una de las siguientes categorías:

- Recursos Humanos
- Finanzas
- Tecnología
- Compras
- Legal

El objetivo consiste en diseñar un prompt capaz de asignar correctamente cada consulta a su categoría correspondiente.

---

# Metodología

```mermaid
flowchart LR
A[Analizar requerimiento]
--> B[Diseñar Prompt]
--> C[Ejecutar Casos]
--> D[Evaluar]
--> E[Refinar]
--> F[Nueva versión]
```

Cada iteración modifica un único aspecto del prompt para poder evaluar su impacto.

---

# Conjunto de pruebas

El laboratorio debe contemplar diferentes tipos de consultas.

| Tipo de caso | Ejemplo |
|--------------|----------|
| Directo | "Necesito actualizar mis datos bancarios." |
| Ambiguo | "Tengo un problema con un pago." |
| Múltiple | "No cobré el sueldo y además mi notebook no funciona." |
| Incompleto | "Necesito ayuda urgente." |
| Fuera de alcance | "¿Cómo está el clima?" |

La diversidad del conjunto de pruebas resulta tan importante como el número de ejemplos.

---

# Criterios de evaluación

Cada ejecución puede evaluarse mediante indicadores como:

- clasificación correcta;
- consistencia entre ejecuciones;
- cumplimiento del formato solicitado;
- cantidad de aclaraciones requeridas;
- consumo aproximado de tokens.

Estos indicadores permiten comparar distintas versiones del prompt de forma objetiva.

---

# Caso de estudio

El equipo desarrolla una primera versión del prompt y obtiene buenos resultados con consultas simples.

Sin embargo, las consultas que contienen más de un tema producen clasificaciones inconsistentes.

En lugar de modificar completamente el prompt, se incorpora una regla para detectar múltiples intenciones y solicitar una aclaración cuando corresponda.

La nueva versión reduce significativamente los errores sin aumentar la complejidad general.

---

# Buenas prácticas

- Cambiar una sola variable por iteración.
- Registrar los resultados de todas las pruebas.
- Conservar versiones anteriores del prompt.
- Incorporar nuevos casos cuando aparezcan errores reales.

---

# Errores frecuentes

- Evaluar únicamente consultas favorables.
- Optimizar sin métricas.
- Reemplazar completamente el prompt ante un fallo menor.
- No documentar las decisiones tomadas.

---

# Ideas clave

- La clasificación constituye un excelente laboratorio para practicar Prompt Engineering.
- La mejora continua depende de la evidencia obtenida durante las pruebas.
- Un prompt evoluciona mediante iteraciones controladas.

---

# Transición hacia la siguiente sección

En la próxima sección desarrollaremos un laboratorio dedicado a la extracción estructurada de información, incorporando formatos de salida, validaciones y criterios de calidad propios de aplicaciones empresariales.

---

> **"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."**
