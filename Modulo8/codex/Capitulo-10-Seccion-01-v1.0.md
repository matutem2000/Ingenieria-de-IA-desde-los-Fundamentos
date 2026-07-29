# Módulo 8 – Capítulo 10 – Sección 01

# Cuándo usar local y cuándo usar nube: privacidad, latencia, costo y capacidad

La decisión de procesar una petición de LLM localmente o delegarla a un servicio en la nube es una función de cuatro dimensiones que frecuentemente tienen tensiones entre sí: privacidad del dato (qué información puede salir del perímetro de la organización), latencia aceptable (cuánto tiempo puede esperar el usuario o el sistema), costo por petición (qué presupuesto de cómputo existe) y capacidad del modelo requerida (qué nivel de inteligencia o especialización necesita la tarea). La privacidad es el criterio excluyente más frecuente en entornos regulados: datos de salud (HIPAA), datos financieros (PCI-DSS), información personal identificable bajo GDPR o información legalmente privilegiada no pueden enviarse a APIs de terceros sin controles específicos; en estos casos el procesamiento local no es una opción de costo sino un requisito legal. La latencia favorece a los modelos locales para casos de uso edge o embedded (procesamiento en el dispositivo, aplicaciones offline, entornos con conectividad limitada) pero perjudica a los modelos locales en hardware de consumo respecto a servicios de nube que operan en H100 con decenas de usuarios en batch: la latencia de una API de OpenAI o Anthropic desde una conexión de baja latencia puede ser inferior a la de un modelo 7B local en CPU. El costo favorece a los modelos locales para volúmenes altos de peticiones una vez amortizado el hardware, pero la nube es más económica para volúmenes bajos o intermitentes donde el costo fijo del hardware no se amortiza.

## Marco de decisión local vs nube

- Datos clasificados o regulados: procesamiento local es el default no negociable; los datos de salud, financieros, legales o con PII clasificada requieren infraestructura con controles de datos específicos que las APIs de terceros no garantizan universalmente
- Tareas simples de alto volumen (clasificación, resumen corto, extracción de entidades): modelos locales de 3B-7B fine-tuneados son más económicos y suficientemente capaces; APIs de nube son más caras por millón de tokens para volúmenes altos
- Tareas complejas de bajo volumen (razonamiento multi-paso, análisis jurídico complejo, generación de código avanzada): modelos de frontera en la nube (GPT-4o, Claude Opus, Gemini Ultra) ofrecen calidad superior que modelos locales de 7B-13B; el costo por petición es alto pero el volumen bajo hace la factura total aceptable
- Latencia crítica (<100ms TTFT): solo posible localmente con modelos 1B-3B en GPU de alta velocidad o en memoria unificada; cualquier API pública añade como mínimo 50-150ms de latencia de red que puede ser inaceptable para aplicaciones de tiempo real
- Disponibilidad y SLA: APIs de nube de proveedores tier-1 ofrecen SLA del 99.9% o superior con fallback automático entre regiones; infraestructura local requiere inversión explícita en alta disponibilidad (N+1 hardware, UPS, redundancia de red) para alcanzar SLAs equivalentes

## Para recordar

El framework de decisión más útil es: si los datos son sensibles, comienza con local; si la tarea requiere inteligencia excepcional, comienza con nube; en todos los demás casos, calcula el costo total de propiedad de ambas opciones con el volumen esperado real.
