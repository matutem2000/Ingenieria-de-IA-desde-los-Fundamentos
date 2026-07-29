# Módulo 7 – Capítulo 03 – Sección 04

# Herramientas de sistema: shell, filesystem, navegador web y code interpreter

Las herramientas de sistema son las más potentes —y potencialmente las más peligrosas— del arsenal de un agente: dan acceso directo al sistema operativo, al sistema de archivos, a la web y a la ejecución de código arbitrario. El intérprete de código (code interpreter) de OpenAI, el Python REPL de LangChain, o los sandboxes de E2B (e2b.dev) permiten al agente escribir y ejecutar código Python para manipular datos, realizar cálculos complejos o interactuar con librerías externas; la ejecución ocurre en un entorno aislado donde el código no puede afectar el sistema host. Las herramientas de navegador web (Playwright, Selenium, Puppeteer controlados por el agente mediante Computer Use de Anthropic o el patrón de scraping estructurado) permiten navegar, extraer contenido y rellenar formularios en páginas web dinámicas. El acceso al shell y al filesystem debe estar estrictamente acotado mediante principios de mínimo privilegio, rutas en lista blanca y revisión de comandos antes de ejecución.

## Componentes principales

- **Python REPL / Code interpreter**: permite al agente ejecutar código Python generado por el LLM en un sandbox aislado; E2B Sandbox, Modal y Daytona ofrecen entornos cloud con aislamiento de contenedor, timeout configurable y acceso controlado a filesystem
- **Herramienta de filesystem**: operaciones de lectura/escritura de archivos; debe restringirse a un directorio de trabajo definido (working directory) y rechazar rutas absolutas o traversal patterns como `../` antes de ejecutar
- **Shell tool**: ejecución de comandos del sistema operativo; la herramienta de mayor superficie de ataque en un agente; requiere lista blanca de comandos permitidos, timeout estricto (máximo 30 segundos) y nunca ejecutarse como root
- **Navegador web controlado**: Playwright headless permite al agente navegar páginas dinámicas que los scrapers HTTP simples no pueden acceder; debe implementarse con bloqueo de recursos (images, fonts, media) para reducir latencia y con timeout por página de 10-30 segundos
- **Herramientas de búsqueda web**: APIs como Tavily Search, SerpAPI o Bing Search API proveen resultados de búsqueda estructurados sin necesidad de renderizar páginas; preferibles al navegador completo cuando solo se necesita acceso a contenido indexado

## Buena práctica

Aplicar el principio de mínimo privilegio a cada herramienta de sistema: si el agente solo necesita leer archivos CSV de un directorio específico, la herramienta debe rechazar cualquier operación fuera de ese scope antes de enviarse al ejecutor, no después.
