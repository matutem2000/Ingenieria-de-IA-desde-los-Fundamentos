# Módulo 7 – Capítulo 08 – Sección 05

# Sandboxing de herramientas: ejecución de código en entornos aislados

El sandboxing de herramientas es el mecanismo de aislamiento que permite al agente ejecutar código generado por el LLM o acceder a recursos externos sin que un fallo de la herramienta o un código malicioso pueda afectar al sistema host. La necesidad de sandboxing es especialmente crítica para herramientas que ejecutan código arbitrario (Python REPL, shell commands, JavaScript) donde el agente podría generar código que accede a rutas del sistema de archivos no autorizadas, establece conexiones de red no permitidas, consume recursos del sistema de forma descontrolada, o ejecuta operaciones de alto privilegio. Las soluciones de sandboxing para agentes van desde contenedores Docker con restricciones de red y filesystem (la opción más común y flexible) hasta plataformas cloud especializadas como E2B (e2b.dev) y Modal que proveen microVMs efímeras con API de alto nivel, y hasta WebAssembly runtimes (Wasmtime, WASInn) para casos donde se necesita sandboxing en proceso con overhead mínimo.

## Aspectos técnicos

- **Docker container sandbox**: ejecutar el código del agente en un contenedor Docker con: network mode `none` (sin acceso a red), filesystem read-only excepto un directorio de trabajo efímero, límites de CPU (cpus=0.5) y memoria (mem_limit=512m), timeout de ejecución (ulimit), y usuario sin privilegios (non-root)
- **E2B Sandbox**: plataforma cloud que provee microVMs Linux efímeras con API de Python (`sandbox = Sandbox()`, `sandbox.process.start_and_wait()`) con timeout configurable, acceso controlado a filesystem y soporte para múltiples lenguajes; ideal para agentes que necesitan ambientes de ejecución preconfigurados
- **Restricción de syscalls con seccomp**: en contenedores Docker, aplicar perfiles seccomp que limiten las llamadas al sistema disponibles para el código en el sandbox; bloquear syscalls como `mount`, `ptrace`, `unshare` que pueden usarse para escapar del contenedor
- **Filesystem isolation**: el código ejecutado en el sandbox debe tener acceso solo a un directorio de trabajo temporal efímero; cualquier archivo necesario para la tarea se copia al directorio de trabajo antes de la ejecución y los resultados se extraen después, sin acceso al filesystem del host
- **Output sanitization**: el output del código ejecutado en el sandbox debe sanitizarse antes de incorporarse al contexto del agente; limitar la longitud máxima (p.ej. 10K caracteres), filtrar contenido binario o caracteres de control, y verificar que el formato es el esperado (texto, JSON, imagen)

## Para recordar

El sandboxing es la defensa en profundidad que protege al sistema host cuando todas las otras defensas fallan: incluso si el agente es comprometido por prompt injection y genera código malicioso, el sandbox limita el daño al entorno aislado y previene que el ataque escape al sistema de producción.
