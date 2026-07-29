# Módulo 12 – Capítulo 07 – Sección 06

## Cierre: la evaluación como infraestructura de aprendizaje continuo

El Capítulo 7 construyó el framework que convierte el sistema de IA en un sistema mejorable con evidencia. Sin él, el equipo opera con intuición — "parece que la calidad mejoró", "creo que la latencia aumentó". Con él, el equipo opera con datos — "faithfulness online cayó 0.05 puntos en los últimos 7 días, correlacionado con un incremento del 15% en el tiempo de first-token de GPT-4o según los spans de OpenTelemetry, posiblemente por una actualización del modelo del proveedor que aún no está documentada en el changelog de OpenAI". La diferencia entre esas dos posiciones no es solo de precisión — es de capacidad de acción: la primera no orienta ninguna decisión, la segunda tiene un diagnóstico preliminar y una hipótesis de causa.

El framework de evaluación continua también cierra la brecha entre el golden dataset estático y la realidad de producción. El golden dataset fue construido por ingenieros que anticiparon los tipos de preguntas que el sistema recibiría. La evaluación online sobre el 5% del tráfico real revela los tipos de preguntas que nadie anticipó: preguntas sobre incidentes recientes que no están en la documentación indexada, preguntas que mezclan terminología de dos dominios distintos de formas que el sistema no maneja bien, preguntas que requieren conocimiento sobre la versión específica del software que el usuario tiene instalado (que el agente no puede responder con certeza sin esa información). Cada uno de esos patrones de fallo es candidato a convertirse en nuevas entradas del golden dataset y en nuevos tipos de documentos a indexar.

La evaluación no es la fase final del ciclo de ingeniería de IA — es una fase permanente que coexiste con el desarrollo, el despliegue y la operación. El pipeline CI/CD del Capítulo 6 ya ejecuta evaluación RAGAS como gate de cada deploy; el framework de evaluación de este capítulo extiende esa práctica a la operación continua en producción. El ciclo completo es: evaluar → detectar degradación → diagnosticar causa → planificar mejora → implementar → evaluar de nuevo. Sin el primer paso, el ciclo no puede comenzar. Sin el último, no se puede saber si la mejora fue efectiva.

El Capítulo 8 construye sobre el framework de evaluación para implementar la observabilidad completa del sistema: las trazas distribuidas, el dashboard operativo y las alertas que convierten las métricas de evaluación en señales de operación en tiempo real.

## Lo que el Capítulo 7 implementó

- **Framework tri-capa**: evaluación RAG (offline con golden dataset + online con 5% del tráfico real), evaluación agéntica (task completion, hallucination, iterations, tool accuracy) y evaluación de sistema (latencia, costo, error rate, disponibilidad) en correlación.
- **Golden dataset con IAA**: construcción con muestreo estratificado, anotación con confidence score, Inter-Annotator Agreement > 80% como criterio de calidad, división 80/20 train/test, proceso de mantenimiento documentado.
- **Evaluación de calidad operativa**: faithfulness, answer relevance y completeness personalizada en perspectiva de diagnóstico — qué causa la caída de cada métrica y cómo correlacionar las señales para identificar la causa raíz.
- **Evaluación de rendimiento**: latencia por etapa con spans OTel (valores típicos por componente), benchmark Locust 50 usuarios concurrentes, costo por petición desagregado con atribución por equipo y alertas de presupuesto.
- **Evaluación de seguridad**: resultados del red teaming como baseline operativo, bypasses convertidos en regresiones permanentes, métricas de producción de rechazos y queries suspicious en Grafana.

> **Nota del Arquitecto**: El mayor error que he visto en frameworks de evaluación de IA es tratar el golden dataset como un artefacto que se construye una vez y se usa indefinidamente. El dominio de uso del sistema evoluciona: nuevos tipos de documentos, nuevas áreas de conocimiento, nuevos patrones de consulta de los usuarios. Un golden dataset que no evoluciona con el sistema produce métricas que se desconectan progresivamente de la calidad real en producción — el sistema puede tener faithfulness de 0.90 en el golden dataset de hace seis meses mientras la calidad en producción es 0.78 porque el dominio cambió. El proceso de mantenimiento del golden dataset — revisión trimestral, expansión con casos de producción, depreciación de preguntas obsoletas — debe ser tan parte del roadmap del equipo como el desarrollo de nuevas funcionalidades.

La evaluación es la capacidad que convierte un sistema de IA en un sistema de ingeniería — sin métricas cuantificables, no hay forma de demostrar mejora, detectar degradación ni tomar decisiones de arquitectura basadas en evidencia.

**Para recordar**: La evaluación es la capacidad que convierte un sistema de IA en un sistema de ingeniería — sin métricas cuantificables, no hay forma de demostrar mejora, detectar degradación ni tomar decisiones de arquitectura basadas en evidencia.

*"Without data, you're just another person with an opinion." — W. Edwards Deming*
