# Módulo 7 – Capítulo 10 – Sección 06

# Cierre: medir agentes es la única forma de mejorarlos sistemáticamente

El capítulo final sobre evaluación y métricas establece la verdad operativa que cierra el módulo de ingeniería de agentes: sin un sistema de medición riguroso y continuo, cualquier mejora al agente es intuición, no ingeniería. Los cambios de prompt que "parecen mejores" pero no se miden contra un test set pueden mejorar un caso de uso al tiempo que degradan diez; los upgrades de modelo que "deberían funcionar mejor" pueden alterar comportamientos específicos del dominio que solo son detectables con tests de regresión; las nuevas herramientas que "amplían las capacidades" del agente pueden introducir conflictos de selección que reducen la precisión en tareas que ya funcionaban bien. La evaluación de agentes no es una actividad de final de proyecto sino una disciplina continua que se ejecuta en cada cambio significativo del sistema —modelo, prompts, herramientas, configuración de memoria— con métricas que se acumulan en el tiempo y permiten ver tendencias, no solo snapshots. Un equipo de AI Engineering que no mide sus agentes sistemáticamente no tiene ingeniería; tiene artesanía, y la artesanía no escala.

## Para recordar

La diferencia entre un agente de investigación y un agente de producción es la misma que entre un experimento científico y un producto: ambos requieren hipótesis y resultados, pero solo el segundo requiere que esos resultados sean reproducibles, medibles y mejorables de forma sistemática y continua.

*"Without data, you're just another person with an opinion."* — W. Edwards Deming, pionero de la gestión de calidad y el ciclo de mejora continua (PDCA); aplicado a sistemas agénticos: sin métricas de evaluación estructuradas, todas las decisiones de diseño del agente son opiniones, no ingeniería basada en evidencia.
