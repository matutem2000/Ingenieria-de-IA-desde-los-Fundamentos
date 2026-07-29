# Módulo 5 – Capítulo 06 – Sección 03

# Gestión de versiones de prompts, modelos y configuraciones

Los prompts son código: cambian el comportamiento del sistema tan significativamente como cualquier modificación de lógica de negocio, deben ser versionados con el mismo rigor que el código Python, y sus cambios deben ser revisados en PRs con las mismas herramientas de diff. La estrategia más simple y efectiva es almacenar los prompts como archivos de texto en el repositorio Git (`prompts/system_prompt_v1.jinja2`, `prompts/extraction_prompt_v2.txt`), con un archivo de configuración que mapea el nombre lógico a la versión activa: `{"system_prompt": "prompts/system_prompt_v2.jinja2"}`. El versionado semántico aplicado a prompts sigue la convención MAJOR.MINOR.PATCH: MAJOR cuando el prompt cambia el comportamiento observable del sistema (nueva tarea, nuevo formato de salida), MINOR cuando añade instrucciones sin cambiar el comportamiento principal, PATCH para correcciones ortográficas o de claridad sin cambio de comportamiento. Las configuraciones de modelo —`model_id`, `temperature`, `max_tokens`, `top_p`— deben vivir en archivos de configuración separados del código (`config/llm_config.yaml`) inyectados vía variables de entorno en producción, permitiendo cambiar el modelo sin tocar el código.

## Aspectos técnicos del versionado de prompts y modelos

- Almacenamiento en Git como archivos: prompts en `prompts/` como archivos `.jinja2` o `.txt`, versionados con Git; el diff de un cambio de prompt es visible en el PR con el mismo `git diff` que cualquier cambio de código
- Registro de prompts en base de datos (alternativa): herramientas como LangSmith Prompt Hub o Langfuse Prompt Management almacenan prompts con versiones, commits y rollback UI; útil cuando no-programadores (PMs, linguists) necesitan editar prompts sin acceso al repositorio
- Modelo pinado por identificador completo: usar siempre el identificador de modelo con fecha (`claude-3-5-sonnet-20241022`, `gpt-4o-2024-08-06`) en lugar del alias versionado (`claude-3-5-sonnet`, `gpt-4o`) para evitar cambios silenciosos de comportamiento cuando el proveedor actualiza el alias
- Config-as-code para parámetros de inferencia: `config/llm_config.yaml` con campos `model`, `temperature`, `max_tokens`, `top_p`, `system_prompt_version`; cargado al inicio de la aplicación y validado con Pydantic Settings antes de servir tráfico
- Changelog de prompts: mantener `prompts/CHANGELOG.md` con entradas por versión que documentan qué cambió, por qué, y cuál fue el impacto medido en la suite de evaluación; crea contexto histórico invaluable para el equipo

## Principio rector

Un prompt sin versión en un sistema de producción es un riesgo de debugging: cuando el comportamiento cambia inesperadamente, la incapacidad de correlacionar el cambio con un commit específico convierte el diagnóstico en arqueología.
