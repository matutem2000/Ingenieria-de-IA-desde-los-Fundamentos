# Módulo 9 – Capítulo 04 – Sección 04

# Red teaming automatizado: PyRIT, Garak y LLM-as-Attacker

El red teaming automatizado usa software para generar, ejecutar y evaluar ataques adversariales contra sistemas de IA a una escala y velocidad imposibles para equipos humanos: donde un red teamer humano puede probar cientos de técnicas en una sesión, un sistema automatizado puede ejecutar decenas de miles de variaciones en minutos. Las herramientas más prominentes en 2024-2025 son PyRIT (Python Risk Identification Toolkit, Microsoft), Garak (Generative AI Red-teaming and Assessment Kit, NVIDIA), y el patrón LLM-as-Attacker donde se usa un LLM (frecuentemente GPT-4 o Claude) para generar prompts adversariales contra el modelo target. PyRIT es una librería Python que orquesta ataques contra endpoints de LLMs, gestiona conversaciones multi-turn y clasifica resultados; Garak es una herramienta de línea de comandos con más de 100 probes (pruebas) predefinidas para detectar vulnerabilidades conocidas; LLM-as-Attacker (implementado en marcos como PAIR —Prompt Automatic Iterative Refinement— de Chao et al., 2023) usa un LLM para refinar iterativamente prompts adversariales hasta que el modelo target produce el output deseado.

## Aspectos técnicos de las herramientas

- PyRIT (Microsoft, open-source): arquitectura modular con orchestrators (gestionan el flujo del ataque), targets (los sistemas de IA bajo prueba), converters (transforman prompts para evadir filtros: Base64, traducción, obfuscation), scorers (evalúan si un output es una vulnerabilidad exitosa) y memory (mantiene el historial de conversación para ataques multi-turn)
- Garak (NVIDIA, open-source): más de 100 probes organizadas en categorías como jailbreak, data leakage, hallucination, toxicity, RLHF bypass; genera un reporte estructurado con tasa de éxito por categoría de ataque; soporta múltiples modelos via plugins (OpenAI, Hugging Face, Anthropic, Replicate)
- PAIR (Prompt Automatic Iterative Refinement): un LLM "attacker" (usualmente GPT-4) recibe el objetivo del ataque y el output del intento anterior, y genera una nueva variación del prompt diseñada para ser más efectiva; el proceso itera hasta lograr el jailbreak o alcanzar un límite de intentos; efectividad demostrada de 60-80% en 20 iteraciones contra GPT-3.5 y Claude
- TAP (Tree of Attacks with Pruning, Mehrotra et al., 2023): variante de PAIR que usa tree search con beam search para explorar el espacio de prompts adversariales de forma más eficiente, reduciendo el número de queries necesarios para jailbreak exitoso en 4-10x respecto a PAIR
- Evaluación automatizada de éxito: el scorer es el componente más crítico del pipeline automatizado — un scorer impreciso (demasiado permisivo o demasiado estricto) invalida los resultados del ejercicio; los scorers más efectivos combinan clasificadores fine-tuned (LlamaGuard) con LLM-as-Judge (GPT-4 evaluando si el output viola las políticas)

## Para recordar

El red teaming automatizado con PyRIT, Garak y PAIR no reemplaza al red teaming humano sino que lo complementa: los sistemas automatizados proveen cobertura exhaustiva de variaciones de ataques conocidos a escala, liberando al equipo humano para enfocarse en las vulnerabilidades creativas y contextualmente sofisticadas que la automatización no puede descubrir.
