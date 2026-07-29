# Módulo 9 – Capítulo 04 – Sección 02

# Metodología: scoping, threat modeling, ejecución y reporte

Un ejercicio de red teaming sin metodología estructurada produce resultados inconsistentes, difíciles de comparar entre iteraciones y con cobertura de amenazas incompleta. La metodología de red teaming de IA se articula en cuatro fases: scoping (definir el sistema target, el threat model y los criterios de éxito), threat modeling (identificar las categorías de ataque relevantes para el sistema específico), ejecución (el ejercicio adversarial propiamente dicho, manual y/o automatizado), y reporte (documentación de hallazgos, severidad, reproducibilidad y recomendaciones de mitigación). Microsoft, en su guía de red teaming para LLMs (2023), y Anthropic, en sus publicaciones sobre evaluación de seguridad de Claude, han publicado metodologías detalladas que son la referencia del estado del arte. La fase de scoping es la más subestimada: un scope mal definido produce ejercicios que encuentran vulnerabilidades irrelevantes (fuera del threat model real) o que dejan sin cubrir las amenazas más críticas.

## Aspectos técnicos de cada fase

- Scoping: definir el threat model con personas adversariales específicas (¿quién ataca: un usuario frustrado, un competidor, un actor estatal?), el perfil de capacidades del adversario (¿tiene acceso whitebox al sistema de prompts? ¿puede hacer fine-tuning de modelos open-source?), y los harm criteria (¿qué outputs constituyen una vulnerabilidad reportable?)
- Threat modeling para red teaming: priorizar categorías de ataque usando OWASP LLM Top 10 y MITRE ATLAS; crear una harm taxonomy que incluya seguridad (bypasses, exfiltración), safety (contenido dañino, desinformación), privacidad (PII, datos de entrenamiento) y alineación (el sistema hace cosas que el operador no pretendía)
- Ejecución estructurada: asignar roles especializados al equipo (expertos en jailbreaking, en ataques de privacidad, en sistemas agénticos); mantener un log detallado de cada attempt (prompt enviado, respuesta recibida, clasificación de éxito/fallo); usar un sistema de tracking de hallazgos (Jira, GitHub Issues) para asegurar reproducibilidad
- Criterios de severidad: adaptar CVSS para IA evaluando: probabilidad de explotación en producción, impacto del comportamiento adversarial obtenido, facilidad de reproducción sin capacidades especializadas, y alcance del daño (un usuario vs. todos los usuarios del sistema)
- Reporte de hallazgos: cada hallazgo debe incluir el prompt o técnica exacta que reproduce la vulnerabilidad, el output observado, la clasificación de severidad, el harm scenario concreto (quién se daña, cómo), y recomendaciones específicas de mitigación con evidencia de efectividad

## Buena práctica

La metodología de red teaming debe producir un hallazgo reproducible por cualquier miembro del equipo usando solo la documentación del reporte: si un hallazgo no puede reproducirse con las instrucciones del reporte, no puede verificarse ni mitigarse, y no tiene valor de seguridad.
