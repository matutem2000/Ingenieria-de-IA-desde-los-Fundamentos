# Capítulo 07 — Herramientas, MCP e Integración con Sistemas Externos

## Sección 14 — Autoevaluación

Las siguientes preguntas permiten verificar la comprensión de los conceptos centrales del capítulo. Para cada pregunta de opción múltiple hay una respuesta correcta. Las preguntas abiertas no tienen una respuesta única: están diseñadas para estimular el análisis de situaciones de diseño reales.

---

### Preguntas de opción múltiple

**1.** Un desarrollador define una herramienta llamada `gestionar_cliente` con un parámetro `accion` que acepta los valores "consultar", "actualizar" y "eliminar". ¿Cuál es el principal problema de este diseño?

a) El nombre de la herramienta es demasiado largo.  
b) La herramienta combina múltiples responsabilidades, lo que dificulta que el modelo elija correctamente cuándo invocarla.  
c) El esquema JSON Schema no soporta parámetros de tipo `enum`.  
d) El modelo no puede invocar herramientas que modifiquen datos.

---

**2.** ¿Cuál es el propósito principal del campo `description` en la definición de una herramienta?

a) Documentar la herramienta para que otros desarrolladores entiendan su código.  
b) Proveer metadatos para el sistema de logs y observabilidad.  
c) Instruir al modelo sobre qué hace la herramienta y cuándo invocarla.  
d) Describir el formato de retorno para que el cliente de la API valide la respuesta.

---

**3.** Un asistente tiene las siguientes herramientas disponibles: `consultar_pedido`, `cancelar_pedido` y `listar_pedidos_cliente`. El usuario dice "muéstrame mis pedidos". El modelo invoca las tres herramientas. ¿Cuál es la causa más probable de este comportamiento?

a) El loop de ejecución tiene un error en el enrutamiento.  
b) Las descripciones de las tres herramientas son semánticamente solapadas.  
c) El modelo siempre invoca todas las herramientas disponibles cuando hay más de una.  
d) El parámetro `tool_choice` está configurado como "any".

---

**4.** ¿En cuál de los siguientes casos NO se recomienda la confirmación humana antes de ejecutar una herramienta?

a) Cancelar un pedido que ya fue enviado.  
b) Consultar el stock disponible de un producto.  
c) Eliminar el registro de un cliente.  
d) Procesar un reembolso de alto valor.

---

**5.** Un resultado de herramienta incluye el siguiente texto: `"sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused"`. ¿Por qué esto es un anti-patrón?

a) Porque el modelo no puede parsear mensajes de error.  
b) Porque el error expone detalles del stack técnico que el modelo no puede usar de forma útil, y que pueden filtrar información sensible sobre la arquitectura del sistema.  
c) Porque los errores de herramientas deben devolver un código HTTP, no un mensaje de texto.  
d) Porque el error está en inglés y el sistema debería operar en español.

---

**6.** ¿Cuál es la diferencia principal entre MCP (Model Context Protocol) y la integración directa de herramientas?

a) MCP es más rápido porque usa un protocolo binario.  
b) MCP permite que el modelo ejecute herramientas sin pasar por la aplicación.  
c) MCP centraliza la lógica de integración en servidores especializados que múltiples clientes pueden usar a través de un protocolo estándar.  
d) MCP solo funciona con modelos de Anthropic.

---

**7.** En el loop de ejecución, ¿cuántas veces puede el modelo invocar herramientas antes de generar la respuesta final?

a) Exactamente una vez por interacción.  
b) Una vez por cada mensaje del usuario.  
c) Hasta el límite máximo de iteraciones configurado en el loop, que puede ser varias veces.  
d) Dos veces como máximo, según el protocolo de la API.

---

**8.** ¿Cuál es el riesgo específico de una herramienta que ejecuta SQL arbitrario generado por el modelo?

a) El modelo puede generar SQL sintácticamente incorrecto.  
b) Expone el sistema a inyección SQL y permite al modelo (o a un atacante que lo manipula) acceder a cualquier dato sin restricciones de autorización.  
c) El SQL generado por el modelo tiene latencia mayor que el SQL predefinido.  
d) Los modelos de lenguaje no pueden generar SQL correcto para bases de datos en español.

---

### Preguntas abiertas

**9.** Un equipo está diseñando un asistente para un banco que puede: consultar el saldo de una cuenta, realizar transferencias entre cuentas propias del usuario, y bloquear una tarjeta de crédito. Para cada una de estas tres operaciones, ¿qué nivel de control de ejecución recomendarías y por qué? Considera: ejecución automática, confirmación del usuario, o confirmación con segundo factor.

---

**10.** Un sistema tiene una herramienta `buscar_en_documentos` que busca en los documentos internos de la empresa. El sistema procesa solicitudes de usuarios externos (clientes) y de usuarios internos (empleados). ¿Qué cambios haría en el diseño del sistema para garantizar que los usuarios externos no puedan acceder a documentos confidenciales internos a través de esta herramienta?

---

**11.** Un asistente de ventas tiene acceso a doce herramientas de diferentes dominios: pedidos, clientes, inventario, precios, logística y facturación. El equipo observa que el modelo frecuentemente invoca herramientas de múltiples dominios incluso para solicitudes simples que solo requieren un dominio. Propón dos estrategias de diseño para reducir este comportamiento, explicando cómo funcionaría cada una.

---

**12.** Un equipo implementa una herramienta `enviar_notificacion_sms` que envía un SMS al cliente. Después de desplegarla en producción, descubren que en algunas interacciones el modelo la invoca dos o tres veces para el mismo cliente dentro de la misma sesión, causando que el cliente reciba múltiples SMS idénticos. Identifica la causa del problema y describe cómo lo resolverías.

---

### Respuestas a las preguntas de opción múltiple

1 → b | 2 → c | 3 → b | 4 → b | 5 → b | 6 → c | 7 → c | 8 → b
