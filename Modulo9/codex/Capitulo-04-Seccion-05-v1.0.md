# Módulo 9 – Capítulo 04 – Sección 05

# Integración en el SDLC: cuándo y con qué frecuencia hacer red teaming

El red teaming de IA no es un evento único sino un proceso continuo que debe integrarse en el Software Development Lifecycle (SDLC) de sistemas de IA con la misma naturalidad que las pruebas de seguridad estáticas (SAST) y dinámicas (DAST) en desarrollo de software convencional. La frecuencia y profundidad del red teaming debe calibrarse según los cambios en el sistema: un cambio de modelo base (de GPT-3.5 a GPT-4o, de Claude 2 a Claude 3.5 Sonnet) requiere un red teaming completo porque el comportamiento adversarial puede cambiar radicalmente; un cambio en el system prompt requiere red teaming enfocado en las nuevas instrucciones; la adición de una herramienta a un agente requiere red teaming específico para esa herramienta. La frecuencia del red teaming debe derivarse del riesgo, las obligaciones aplicables y los cambios materiales del sistema. Conviene ejecutarlo antes de liberaciones significativas y repetirlo cuando cambien el modelo, las herramientas, los datos, la exposición o el perfil de amenazas. La integración en CI/CD mediante red teaming automatizado ligero (Garak en el pipeline de deployment) permite detectar regresiones de seguridad antes de que lleguen a producción.

## Aspectos técnicos de integración en SDLC

- Triggers de red teaming mandatorio: cambio de modelo base, cambio significativo en el system prompt, adición o modificación de herramientas en agentes, exposición del sistema a una nueva categoría de usuarios o casos de uso, y respuesta a un incidente de seguridad en producción
- Red teaming ligero en CI/CD: integrar Garak o un subconjunto de PyRIT probes en el pipeline de deployment para detectar regresiones de seguridad conocidas — no reemplaza el red teaming completo pero es un gate de calidad que previene que vulnerabilidades ya conocidas regresen al sistema
- Red teaming pre-release completo: ejercicio de 2-4 semanas que combina red teaming manual (expertos especializados) y automatizado (PyRIT + Garak + PAIR) con documentación completa de hallazgos y mitigaciones verificadas antes del puesta en producción
- Red teaming periódico en producción: con una frecuencia derivada del riesgo y activado también por cambios materiales o incidentes de seguridad; incluye la revisión de registros de producción para identificar intentos de ataque como insumo del modelo de amenazas actualizado
- Gestión de hallazgos: cada vulnerabilidad encontrada debe tener un owner, un SLA de mitigación basado en severidad (crítico: 24h, alto: 7 días, medio: 30 días), y un proceso de verificación de la mitigación (nueva prueba con el mismo ataque para confirmar que fue cerrada)

## Buena práctica

El red teaming debe tratarse como un proceso de ingeniería con artefactos reproducibles —no como un ejercicio artístico—: los prompts de ataque, los resultados, las mitigaciones aplicadas y los nuevas pruebas deben versionarse en el repositorio del proyecto para tener una historia auditable de la evolución del postura de seguridad del sistema.
