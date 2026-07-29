# Módulo 3 — Context Engineering

# Capítulo 06 — RAG (Retrieval-Augmented Generation) como componente del Context Engineering

## Sección 11 — Laboratorio práctico

> *"Un pipeline RAG mínimo viable enseña más en dos horas de práctica que diez horas de lectura. El objetivo no es el código: es observar cómo cada decisión de diseño afecta la calidad del resultado."*

---

## Objetivo del laboratorio

Construir un pipeline RAG mínimo viable que cubra la totalidad del ciclo: desde la ingesta de documentos hasta la evaluación de los fragmentos recuperados para una consulta dada. No se requiere experiencia previa con bases vectoriales ni APIs de LLM: el laboratorio usa componentes de código abierto ejecutables localmente.

Al finalizar el laboratorio, el estudiante habrá:
- Segmentado un conjunto de documentos usando dos estrategias de chunking distintas.
- Producido embeddings y almacenado los fragmentos en un índice vectorial local.
- Ejecutado consultas y recuperado fragmentos.
- Evaluado manualmente la calidad del retrieval.
- Comparado dos configuraciones distintas del mismo pipeline.

---

## Requisitos

- Python 3.10 o superior.
- Librerías: `chromadb`, `sentence-transformers`, `langchain-text-splitters` (o `nltk`).
- Acceso a un LLM: una cuenta en cualquier proveedor con API compatible (o un modelo local con Ollama).
- No se requiere GPU: los modelos de embedding de tamaño pequeño funcionan en CPU con latencia aceptable para este ejercicio.

Instalación:

```bash
pip install chromadb sentence-transformers langchain-text-splitters
```

---

## Corpus del laboratorio

Para mantener el foco en el pipeline y no en la adquisición de datos, el laboratorio usa un corpus de 10 documentos de texto libre sobre un tema acotado. Se sugiere usar artículos de la Wikipedia en español sobre un dominio de interés (por ejemplo: 5 artículos sobre contratos en derecho civil y 5 artículos sobre regulación financiera). El corpus debe guardarse como archivos `.txt` en un directorio `/corpus`.

El ejercicio puede repetirse con cualquier corpus de documentos internos, lo que lo convierte en un prototipo directo para aplicaciones reales.

---

## Paso 1: Segmentación con chunking fijo y chunking semántico

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Leer documentos
documentos = []
for filename in os.listdir("./corpus"):
    if filename.endswith(".txt"):
        with open(f"./corpus/{filename}", "r", encoding="utf-8") as f:
            documentos.append({"texto": f.read(), "fuente": filename})

# Chunking fijo: 500 tokens, solapamiento de 50
splitter_fijo = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len
)

# Chunking semántico por párrafo: se divide en "\n\n"
splitter_semantico = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ".", " "],
    chunk_size=600,
    chunk_overlap=80,
    length_function=len
)

# Producir chunks con ambas estrategias
chunks_fijos = []
chunks_semanticos = []

for doc in documentos:
    for chunk in splitter_fijo.split_text(doc["texto"]):
        chunks_fijos.append({"texto": chunk, "fuente": doc["fuente"]})
    for chunk in splitter_semantico.split_text(doc["texto"]):
        chunks_semanticos.append({"texto": chunk, "fuente": doc["fuente"]})

print(f"Chunks fijos: {len(chunks_fijos)}")
print(f"Chunks semánticos: {len(chunks_semanticos)}")
```

Observar la diferencia en el número de chunks y en la coherencia de los fragmentos generados. ¿Cuántos chunks del método fijo cortan ideas a mitad de oración?

---

## Paso 2: Embedding e indexación

```python
import chromadb
from sentence_transformers import SentenceTransformer

# Modelo de embedding (ejecuta en CPU, ~90MB)
modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# Cliente de ChromaDB (base vectorial local)
cliente = chromadb.Client()

# Crear dos colecciones: una para cada estrategia de chunking
coleccion_fija = cliente.create_collection("chunks_fijos")
coleccion_semantica = cliente.create_collection("chunks_semanticos")

def indexar_chunks(chunks, coleccion):
    textos = [c["texto"] for c in chunks]
    fuentes = [c["fuente"] for c in chunks]
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    
    # Generar embeddings en batch
    embeddings = modelo.encode(textos, batch_size=32, show_progress_bar=True)
    
    coleccion.add(
        documents=textos,
        embeddings=embeddings.tolist(),
        metadatas=[{"fuente": f} for f in fuentes],
        ids=ids
    )
    print(f"Indexados {len(chunks)} fragmentos en '{coleccion.name}'")

indexar_chunks(chunks_fijos, coleccion_fija)
indexar_chunks(chunks_semanticos, coleccion_semantica)
```

---

## Paso 3: Retrieval y comparación

```python
# Definir un conjunto de 5 consultas de prueba
consultas = [
    "¿Qué es un contrato de mutuo y cuáles son sus elementos esenciales?",
    "¿Cuáles son las sanciones por incumplimiento de normas de capital mínimo?",
    "¿En qué casos puede resolverse un contrato por causa de fuerza mayor?",
    "¿Qué diferencia hay entre una garantía personal y una garantía real?",
    "¿Cómo se regula la transparencia en los instrumentos financieros?"
]

def recuperar(consulta, coleccion, n_resultados=3):
    embedding_consulta = modelo.encode([consulta])[0].tolist()
    resultados = coleccion.query(
        query_embeddings=[embedding_consulta],
        n_results=n_resultados,
        include=["documents", "metadatas", "distances"]
    )
    return resultados

# Comparar para la primera consulta
for consulta in consultas[:2]:
    print(f"\n{'='*60}")
    print(f"CONSULTA: {consulta}")
    print(f"{'='*60}")
    
    print("\n--- Retrieval con chunking FIJO ---")
    res_fijo = recuperar(consulta, coleccion_fija)
    for i, (doc, dist) in enumerate(zip(res_fijo["documents"][0], res_fijo["distances"][0])):
        print(f"\n[{i+1}] Similitud: {1-dist:.3f}")
        print(doc[:200] + "...")
    
    print("\n--- Retrieval con chunking SEMÁNTICO ---")
    res_sem = recuperar(consulta, coleccion_semantica)
    for i, (doc, dist) in enumerate(zip(res_sem["documents"][0], res_sem["distances"][0])):
        print(f"\n[{i+1}] Similitud: {1-dist:.3f}")
        print(doc[:200] + "...")
```

---

## Paso 4: Evaluación manual de la calidad del retrieval

Para cada una de las 5 consultas, registrar:

| Consulta | Fragmento 1 relevante? | Fragmento 2 relevante? | Fragmento 3 relevante? | Estrategia ganadora |
|---|---|---|---|---|
| Consulta 1 | ✓/✗ (fijo) / ✓/✗ (sem) | ... | ... | fijo / semántico / empate |
| Consulta 2 | ... | ... | ... | ... |
| Consulta 3 | ... | ... | ... | ... |
| Consulta 4 | ... | ... | ... | ... |
| Consulta 5 | ... | ... | ... | ... |

La evaluación es manual en este laboratorio. En producción, esta tabla se construye con anotaciones del dominio y se calcula automáticamente como precision@3.

---

## Paso 5: Integración con LLM (opcional)

Si se dispone de acceso a una API de LLM, el pipeline puede completarse ensamblando el contexto y generando la respuesta:

```python
# Ejemplo conceptual con cualquier API compatible con OpenAI
from openai import OpenAI

cliente_llm = OpenAI(api_key="tu_api_key")

def rag_completo(consulta, coleccion, n_resultados=3):
    # Retrieval
    resultados = recuperar(consulta, coleccion, n_resultados)
    fragmentos = resultados["documents"][0]
    fuentes = [m["fuente"] for m in resultados["metadatas"][0]]
    
    # Ensamblado del contexto
    contexto = "\n\n".join([
        f"[Fragmento {i+1} — Fuente: {fuente}]\n{fragmento}"
        for i, (fragmento, fuente) in enumerate(zip(fragmentos, fuentes))
    ])
    
    # Prompt
    prompt = f"""Responde la siguiente consulta basándote únicamente en los
fragmentos proporcionados. Si la información no es suficiente, indícalo.

CONSULTA: {consulta}

FRAGMENTOS RECUPERADOS:
{contexto}

RESPUESTA:"""
    
    respuesta = cliente_llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return respuesta.choices[0].message.content

# Probar con la primera consulta
respuesta = rag_completo(consultas[0], coleccion_semantica)
print(respuesta)
```

---

## Preguntas para reflexionar después del laboratorio

1. ¿Qué diferencias observaste entre el chunking fijo y el semántico en la coherencia de los fragmentos? ¿Qué tipo de consulta favorece cada estrategia?

2. ¿Hubo alguna consulta donde ninguna estrategia recuperó un fragmento relevante en los top 3? ¿Qué podría explicarlo?

3. ¿Cómo cambiaría el pipeline si el corpus tuviera 50.000 documentos en lugar de 10? ¿Qué componentes deberían reemplazarse o ajustarse?

4. ¿Qué metadatos agregarías si este corpus fuera de documentos normativos de una organización real?

5. Si el modelo de embedding fuera reemplazado por uno más potente, ¿esperarías que el retrieval mejorara uniformemente para todas las consultas? ¿Por qué sí o por qué no?

---

## Variantes opcionales

**Variante A:** Implementar búsqueda híbrida (dense + BM25) usando la librería `rank_bm25` y comparar los resultados con el retrieval puramente vectorial.

**Variante B:** Agregar un modelo de cross-encoding para re-ranking usando `cross-encoder/ms-marco-multilingual-MiniLM-L12` de sentence-transformers y medir el cambio en precision@3.

**Variante C:** Agregar filtrado por metadatos: clasificar los documentos como "legal" o "financiero" durante la indexación y comparar el retrieval con y sin el filtro aplicado a la consulta.

---

> *"Un arquitecto no memoriza respuestas. Comprende problemas para poder diseñar soluciones."*
