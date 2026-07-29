# Capítulo 04 — Sección 12

# Laboratorio práctico

## Objetivo del laboratorio

Implementar un sistema de memoria persistente funcional usando JSON como backend de almacenamiento. El sistema debe ser capaz de: capturar información relevante de una conversación, persistirla entre sesiones, recuperar memorias relevantes para una consulta nueva, y eliminar la memoria de un usuario.

Al finalizar este laboratorio, habrás construido el esqueleto de un sistema de memoria que puede ser extendido con un backend más robusto (Redis, Qdrant) sin cambiar la lógica de negocio.

## Prerrequisitos

- Python 3.10 o superior
- Un cliente de API de LLM con acceso a un modelo que soporte function calling (Claude, GPT-4, etc.)
- Instalación: `pip install anthropic` (o el cliente de tu proveedor de API)

## Estructura del proyecto

```
memoria_lab/
├── memoria.py          # Motor de memoria
├── extractor.py        # Extracción de hechos memorables
├── asistente.py        # Integración con el LLM
├── datos/
│   └── memorias.json   # Base de datos de memoria (creada automáticamente)
└── main.py             # Punto de entrada
```

## Paso 1: El motor de memoria (memoria.py)

```python
import json
import os
from datetime import datetime
from pathlib import Path

RUTA_MEMORIAS = Path("datos/memorias.json")

def cargar_memorias() -> dict:
    """Carga la base de datos de memoria desde disco."""
    if not RUTA_MEMORIAS.exists():
        RUTA_MEMORIAS.parent.mkdir(exist_ok=True)
        return {}
    with open(RUTA_MEMORIAS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_memorias(memorias: dict):
    """Persiste la base de datos de memoria en disco."""
    with open(RUTA_MEMORIAS, "w", encoding="utf-8") as f:
        json.dump(memorias, f, ensure_ascii=False, indent=2)

def guardar_hecho(user_id: str, hecho: str, tipo: str):
    """
    Guarda un hecho sobre el usuario.
    Verifica duplicados antes de insertar.
    """
    memorias = cargar_memorias()
    
    if user_id not in memorias:
        memorias[user_id] = {"hechos": [], "perfil": {}}
    
    # Verificar duplicado simple (comparación de texto)
    existentes = [h["contenido"] for h in memorias[user_id]["hechos"]]
    if hecho not in existentes:
        memorias[user_id]["hechos"].append({
            "id": f"{user_id}_{len(memorias[user_id]['hechos'])}",
            "contenido": hecho,
            "tipo": tipo,
            "creado": datetime.now().isoformat(),
            "ultimo_uso": datetime.now().isoformat()
        })
        guardar_memorias(memorias)
        return True
    return False  # Ya existía

def recuperar_memorias(user_id: str) -> list[dict]:
    """
    Recupera todos los hechos de un usuario.
    (En producción: recuperación semántica por similitud)
    """
    memorias = cargar_memorias()
    if user_id not in memorias:
        return []
    return memorias[user_id]["hechos"]

def eliminar_memoria_usuario(user_id: str) -> int:
    """
    Elimina toda la memoria de un usuario.
    Retorna el número de registros eliminados.
    """
    memorias = cargar_memorias()
    if user_id not in memorias:
        return 0
    
    count = len(memorias[user_id]["hechos"])
    del memorias[user_id]
    guardar_memorias(memorias)
    return count

def eliminar_hecho(user_id: str, hecho_id: str) -> bool:
    """Elimina un hecho específico por ID."""
    memorias = cargar_memorias()
    if user_id not in memorias:
        return False
    
    antes = len(memorias[user_id]["hechos"])
    memorias[user_id]["hechos"] = [
        h for h in memorias[user_id]["hechos"] if h["id"] != hecho_id
    ]
    if len(memorias[user_id]["hechos"]) < antes:
        guardar_memorias(memorias)
        return True
    return False
```

## Paso 2: El extractor de memorias (extractor.py)

```python
import json

PROMPT_EXTRACCION = """Analiza la conversación y extrae los hechos que vale la pena recordar sobre el usuario para sesiones futuras.

Solo extrae:
- Preferencias explícitas del usuario (formato, herramientas, idioma, etc.)
- Hechos sobre su trabajo, empresa o proyectos
- Decisiones o acuerdos relevantes para trabajo futuro
- Restricciones o limitaciones expresadas

NO extraigas:
- Preguntas exploratorias sin conclusión
- Contenido relevante solo para esta sesión
- Saludos o frases rutinarias

Responde SOLO con JSON válido, sin texto adicional:
{{
  "hechos": [
    {{"contenido": "descripción del hecho", "tipo": "preferencia|trabajo|decision|restriccion"}}
  ]
}}

Si no hay nada que valga la pena recordar, responde: {{"hechos": []}}

Conversación:
{conversacion}"""

def extraer_hechos_memorables(conversacion: list[dict], llm_client) -> list[dict]:
    """
    Usa el LLM para identificar qué información de la conversación
    merece ser persistida en memoria.
    """
    if not conversacion:
        return []
    
    texto_conversacion = "\n".join([
        f"{'Usuario' if m['role'] == 'user' else 'Asistente'}: {m['content']}"
        for m in conversacion
    ])
    
    respuesta = llm_client.completar(
        prompt=PROMPT_EXTRACCION.format(conversacion=texto_conversacion)
    )
    
    try:
        datos = json.loads(respuesta)
        return datos.get("hechos", [])
    except json.JSONDecodeError:
        return []
```

## Paso 3: El asistente con memoria (asistente.py)

```python
from memoria import recuperar_memorias, guardar_hecho
from extractor import extraer_hechos_memorables

SYSTEM_PROMPT_BASE = """Eres un asistente de análisis. Ayudas al usuario con su trabajo.

{bloque_memoria}

Usa el contexto de memoria para dar respuestas personalizadas y relevantes.
Si la memoria está vacía, trata la sesión como la primera vez que hablas con este usuario."""

def construir_bloque_memoria(user_id: str) -> str:
    """Construye el bloque de contexto de memoria para inyectar en el prompt."""
    hechos = recuperar_memorias(user_id)
    
    if not hechos:
        return "### Memoria del usuario\n(Sin memorias previas)"
    
    lineas = ["### Memoria del usuario"]
    for hecho in hechos[-10:]:  # Máximo 10 hechos para este laboratorio
        lineas.append(f"- [{hecho['tipo']}] {hecho['contenido']}")
    
    return "\n".join(lineas)

class AsistenteConMemoria:
    def __init__(self, user_id: str, llm_client):
        self.user_id = user_id
        self.llm = llm_client
        self.historial = []
    
    def responder(self, mensaje_usuario: str) -> str:
        """Procesa un mensaje del usuario y produce una respuesta."""
        # Construir el contexto con memoria
        bloque_memoria = construir_bloque_memoria(self.user_id)
        system_prompt = SYSTEM_PROMPT_BASE.format(bloque_memoria=bloque_memoria)
        
        # Agregar mensaje al historial
        self.historial.append({"role": "user", "content": mensaje_usuario})
        
        # Llamar al LLM
        respuesta = self.llm.chat(
            system=system_prompt,
            messages=self.historial
        )
        
        # Agregar respuesta al historial
        self.historial.append({"role": "assistant", "content": respuesta})
        
        return respuesta
    
    def cerrar_sesion(self):
        """
        Al finalizar la sesión, extrae y persiste los hechos memorables.
        """
        print("\n[Sistema] Guardando memorias de la sesión...")
        hechos = extraer_hechos_memorables(self.historial, self.llm)
        
        guardados = 0
        for hecho in hechos:
            exito = guardar_hecho(
                user_id=self.user_id,
                hecho=hecho["contenido"],
                tipo=hecho["tipo"]
            )
            if exito:
                guardados += 1
                print(f"  + Guardado: {hecho['contenido']}")
        
        print(f"[Sistema] {guardados} memorias nuevas guardadas.")
```

## Paso 4: Punto de entrada (main.py)

```python
from asistente import AsistenteConMemoria
from memoria import recuperar_memorias, eliminar_memoria_usuario
# Importar tu cliente de LLM aquí

USER_ID = "usuario_demo"

def main():
    # Inicializar el cliente LLM (reemplazar con tu implementación)
    llm = TuClienteLLM()
    
    asistente = AsistenteConMemoria(user_id=USER_ID, llm_client=llm)
    
    print("=== Asistente con Memoria ===")
    print("Comandos especiales: /memoria, /olvidar-todo, /salir\n")
    
    while True:
        entrada = input("Tú: ").strip()
        
        if not entrada:
            continue
        
        # Comandos especiales
        if entrada == "/salir":
            asistente.cerrar_sesion()
            print("Hasta luego.")
            break
        
        elif entrada == "/memoria":
            hechos = recuperar_memorias(USER_ID)
            if not hechos:
                print("[Memoria vacía]")
            else:
                print(f"[{len(hechos)} hechos guardados sobre ti:]")
                for h in hechos:
                    print(f"  [{h['id']}] ({h['tipo']}) {h['contenido']}")
            continue
        
        elif entrada == "/olvidar-todo":
            confirmacion = input("¿Seguro? Esto eliminará toda tu memoria. (sí/no): ")
            if confirmacion.lower() == "sí":
                eliminados = eliminar_memoria_usuario(USER_ID)
                print(f"[{eliminados} registros eliminados]")
            continue
        
        # Respuesta normal
        respuesta = asistente.responder(entrada)
        print(f"Asistente: {respuesta}\n")

if __name__ == "__main__":
    main()
```

## Ejercicios de extensión

Una vez que el sistema base funciona, los siguientes ejercicios aumentan su sofisticación:

**Ejercicio 1 — TTL automático:** modificar `guardar_hecho` para aceptar un parámetro `ttl_dias`. Modificar `recuperar_memorias` para filtrar automáticamente los hechos cuya fecha de creación supera el TTL.

**Ejercicio 2 — Recuperación semántica:** reemplazar la recuperación simple (todos los hechos del usuario) por recuperación semántica usando la API de embeddings de tu proveedor y búsqueda por similitud coseno. Implementar la función `recuperar_hechos_relevantes(user_id, consulta, top_k)`.

**Ejercicio 3 — Detección de contradicciones:** modificar `guardar_hecho` para detectar contradicciones usando el LLM. Si el hecho nuevo contradice a uno existente, actualizar el existente en lugar de insertar uno nuevo.

**Ejercicio 4 — Migración a Qdrant:** reemplazar el backend JSON por Qdrant (instalable con `pip install qdrant-client`). La interfaz de `memoria.py` debería permanecer igual —solo cambia la implementación interna.

---

*La siguiente sección presenta el checklist del AI Engineer: las preguntas que todo diseñador de sistemas con memoria debería responder antes de ir a producción.*
