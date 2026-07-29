# Módulo 12 – Capítulo 05 – Sección 04

# Input validation y output filtering: sanitización en los boundaries del sistema

La validación de inputs opera en el boundary de entrada del sistema: el endpoint `/query` de FastAPI recibe la petición del usuario, el middleware de autenticación verifica el JWT, y antes de pasar la query al agente, el InputValidator aplica tres capas de validación. La primera valida el schema con Pydantic: tipo string, longitud máxima 2000 caracteres, encoding UTF-8 sin caracteres de control. La segunda aplica la lista negra de patrones de injection. La tercera ejecuta un clasificador de intent que etiqueta la query como `safe`, `suspicious` o `malicious`; las queries `malicious` se rechazan con HTTP 400 y se registran en el audit log con el patrón detectado. El output filtering opera en el boundary de salida: antes de devolver la respuesta al usuario, el OutputFilter escanea el texto generado en busca de PII (emails, números de teléfono, tokens de API con regex), strings que parecen credenciales (AWS keys, GitHub tokens) y contenido que replica patrones de injection embebidos en documentos.

## Controles de validación y filtrado

- Input schema validation: Pydantic con max_length=2000, pattern exclusion para caracteres de control y validación de encoding
- Lista negra de injection: 200 patrones en español e inglés actualizados con cada sesión de red teaming
- Clasificador de intent: modelo de clasificación binaria (safe/unsafe) fine-tuned sobre dataset de ataques conocidos
- Output PII scanning: regex para emails, teléfonos, tarjetas; NER para nombres propios en contextos sensibles
- Credential detection: patrones de AWS keys, GitHub tokens, API keys con formato regex aplicados al output antes de envío

## Buena práctica

La validación de inputs y el filtrado de outputs son controles complementarios, no alternativos — un sistema que filtra el output pero no valida el input puede ser explotado para extraer información sensible mediante técnicas de jailbreak.
