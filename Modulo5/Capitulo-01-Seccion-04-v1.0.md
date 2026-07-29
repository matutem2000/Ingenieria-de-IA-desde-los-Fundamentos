# Módulo 5 – Capítulo 01 – Sección 04

# Gestión de credenciales, variables de entorno y seguridad básica

Las API keys de modelos fundacionales son credenciales de alto valor que conceden acceso irrestricto a la cuota de gasto del proyecto; una key filtrada en un repositorio público puede generar cargos de miles de dólares antes de ser detectada, como muestran incidentes documentados en GitHub en 2023 y 2024. La práctica estándar es almacenar credenciales exclusivamente en variables de entorno (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) y nunca en código fuente, archivos de configuración versionados ni logs de aplicación. En entornos de desarrollo local se usa un archivo `.env` ignorado por `.gitignore` y cargado con `python-dotenv` (`load_dotenv()`); en producción las credenciales se inyectan desde un gestor de secretos como AWS Secrets Manager, HashiCorp Vault, Google Secret Manager o las variables de entorno del CI/CD. La rotación periódica de keys y el uso de keys con permisos mínimos (scoped API keys donde el proveedor lo permite) son prácticas de hardening fundamentales para cualquier sistema que exponga capacidades de IA.

## Puntos críticos de seguridad en credenciales de IA

- Regla de oro: nunca hardcodear API keys en código fuente; usar `os.environ.get("API_KEY")` o `os.getenv("API_KEY")` como única forma de acceso dentro del código de la aplicación
- Archivo `.env` local: usar `python-dotenv` (`pip install python-dotenv`) para cargar variables desde `.env` en desarrollo, con `.env` y `.env.local` siempre presentes en `.gitignore` desde el inicio del proyecto
- Gestores de secretos en producción: AWS Secrets Manager, Azure Key Vault o Google Secret Manager proveen rotación automática, auditoría de accesos y acceso controlado por IAM roles sin hardcodear credenciales en el runtime de la aplicación
- Pre-commit hooks de detección: herramientas como `detect-secrets`, `truffleHog` o `gitleaks` como hooks de pre-commit detectan patrones de API keys antes de que lleguen al repositorio
- Scoped keys y proyectos separados: OpenAI permite crear keys por proyecto con límites de gasto independientes; Anthropic permite crear múltiples API keys con nombres descriptivos para separar ambientes de desarrollo, staging y producción

## Idea central

Una credencial de API de modelo fundacional comprometida no solo expone gasto monetario sino potencialmente datos sensibles del contexto; la gestión segura de secretos no es opcional sino un requisito de producción desde el primer día.
