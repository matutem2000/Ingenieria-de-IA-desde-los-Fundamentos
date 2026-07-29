# Módulo 12 – Capítulo 07 – Sección 04

# Evaluación de rendimiento: latencia end-to-end, throughput y costo por petición

La evaluación de rendimiento del sistema integrador mide la latencia en cada etapa del pipeline para identificar cuellos de botella: embedding de query (típicamente 50-100ms), búsqueda en Qdrant (20-80ms), reranking con Cohere (200-400ms), razonamiento del agente y generación LLM (1000-2000ms) y compresión de contexto (100-300ms). Los instrumentos de medición son spans OpenTelemetry exportados a Grafana Tempo, con histogramas de latencia en percentiles P50/P90/P95/P99 por etapa y por pipeline completo. El benchmark de throughput se ejecuta con Locust, simulando una rampa de 10 usuarios/segundo hasta alcanzar 50 usuarios concurrentes, midiendo req/s sostenidos y tiempo de degradación de P95 al aumentar la carga. El costo por petición se calcula combinando: tokens de embedding (query + chunks), tokens del LLM principal (input = contexto + query, output = respuesta), tokens del reranker de Cohere y tokens del LLM de evaluación si se usa LLM-as-judge.

## Métricas de evaluación de rendimiento

- Latencia por etapa: spans OpenTelemetry para embedding (P50 ~75ms), Qdrant (P50 ~40ms), Cohere rerank (P50 ~280ms), LLM (P50 ~1.2s)
- Latencia end-to-end: P50 < 1.8s, P95 < 3s, P99 < 5s bajo carga de 50 usuarios concurrentes con ramp-up de 30s
- Throughput: benchmark Locust con escenarios de 10, 25 y 50 usuarios concurrentes, midiendo req/s en steady state
- Costo por petición: suma de costos de OpenAI embedding, Cohere rerank y GPT-4o generation (input + output tokens)
- Costo proyectado mensual: costo_por_peticion × volumen_mensual_estimado con breakdown por componente

## Para recordar

La latencia de un sistema RAG agéntico es la suma de latencias de sus componentes — el cuello de botella típico es la generación LLM, pero el reranking con modelos externos puede ser el segundo mayor contribuidor y debe incluirse en el análisis de rendimiento.
