# Módulo 12 – Capítulo 06 – Sección 01

# Containerización: Dockerfile del sistema, dependencias y configuración de producción

El sistema integrador se containeriza con una imagen Docker multi-stage que separa el entorno de build del entorno de runtime para minimizar el tamaño de la imagen final y reducir la superficie de ataque. El primer stage usa `python:3.11-slim` como base, instala las dependencias del sistema necesarias (build-essential para compilar paquetes nativos) y ejecuta `pip install` sobre el `requirements.txt` con hash verification (`--require-hashes`) para garantizar la reproducibilidad e integridad de las dependencias. El segundo stage copia únicamente los artefactos compilados y el código de la aplicación, configura un usuario no-root con uid:gid 1000:1000, y establece el `ENTRYPOINT` como `uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4`. Las variables de entorno sensibles (OPENAI_API_KEY, QDRANT_API_KEY, DATABASE_URL) no se incluyen en la imagen — se inyectan en tiempo de ejecución mediante Kubernetes Secrets o Docker secrets.

## Aspectos técnicos de la containerización

- Multi-stage build: stage builder con build-essential + pip install, stage runtime con artefactos compilados únicamente
- Usuario no-root: usuario con uid 1000 sin privilegios de sistema para reducir impacto de vulnerabilidades de contenedor
- Dependencias con hash verification: pip install --require-hashes para detectar tampering de paquetes en el registry
- Health check integrado: HEALTHCHECK con curl al endpoint /health cada 30s, con timeout 5s y 3 intentos antes de unhealthy
- Configuración de producción: uvicorn con --workers 4, --access-log deshabilitado (logs via OpenTelemetry), --timeout-keep-alive 30

## Para recordar

Un Dockerfile de producción no es el Dockerfile de desarrollo con CMD diferente — requiere multi-stage build, usuario no-root, hash verification de dependencias y configuración explícita del runtime para ser seguro y reproducible.
