# Módulo 5 – Capítulo 10 – Sección 01

# Patrones de entrada: validación, normalización y pre-procesamiento de prompts

El pre-procesamiento de la entrada del usuario antes de enviarlo al LLM es una capa crítica de defensa de calidad y seguridad que reduce alucinaciones, previene prompt injection, y normaliza el input para que el modelo lo procese de forma consistente. La validación de entrada verifica que el input cumple con los requisitos mínimos: longitud dentro del rango válido (rechazar inputs vacíos y inputs que excedan el presupuesto de tokens del sistema), ausencia de patrones de prompt injection conocidos (intentos de sobrescribir el system prompt con frases como "ignora las instrucciones anteriores"), y adecuación al dominio del sistema (detectar y rechazar o redirigir queries fuera de scope usando un clasificador de primer paso). La normalización prepara el input para el procesamiento consistente: normalizar encoding de caracteres (UTF-8), remover caracteres de control invisibles que confunden a algunos tokenizadores, normalizar espacios y saltos de línea, y opcionalmente expandir abreviaciones o corregir errores ortográficos evidentes en dominios donde la ortografía correcta mejora la recuperación en RAG. El pre-procesamiento de prompts también incluye la inyección de contexto dinámico: insertar la fecha y hora actuales, el perfil del usuario, el idioma detectado, y otros datos del contexto de negocio que el model necesita para responder correctamente.

## Componentes principales del pre-procesamiento de entrada

- Validación de longitud y tokens: `token_count = count_tokens(user_input); if token_count > MAX_INPUT_TOKENS: raise InputTooLongError(token_count, MAX_INPUT_TOKENS)` previene prompts que excedan el budget antes de hacer la llamada al LLM
- Detección de prompt injection: lista de patrones regex y clasificador ligero que detecta intentos de "jailbreak" o de sobrescribir instrucciones del sistema; los inputs detectados se loggean, se rechazan con mensaje de error apropiado, y opcionalmente se escalan a revisión humana
- Sanitización de encoding: `text = text.encode('utf-8', errors='replace').decode('utf-8')` elimina caracteres inválidos; `unicodedata.normalize('NFC', text)` normaliza representaciones equivalentes; `re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)` remueve caracteres de control
- Enriquecimiento de contexto dinámico: en el template del prompt, incluir variables como `{current_date}`, `{user_name}`, `{user_plan}`, `{detected_language}` que se rellenan en el pre-procesamiento con datos del contexto de la sesión antes de construir el mensaje final
- Clasificación de intent de primer paso: un modelo ligero (`text-embedding-3-small` + clasificador KNN o `claude-3-haiku` con prompt de clasificación de 2 tokens) determina si la query es in-scope antes de gastar los tokens del modelo principal en una query out-of-scope

## Principio rector

El pre-procesamiento de entrada es la primera línea de defensa de la calidad del sistema; un input malformado, malicioso o out-of-scope que llega al LLM principal es más caro de manejar (tokens desperdiciados, respuesta incorrecta, posible daño) que rechazarlo o corregirlo en esta etapa.
