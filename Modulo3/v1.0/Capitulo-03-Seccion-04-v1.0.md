# La evolución de las ventanas de contexto

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Las primeras generaciones de modelos de lenguaje podían procesar únicamente pequeñas cantidades de texto. Esto obligaba a resumir conversaciones, dividir documentos y fragmentar problemas complejos.

En pocos años, las ventanas de contexto crecieron desde unos pocos miles de tokens hasta cientos de miles e incluso millones en algunos modelos. Este cambio modificó profundamente la forma de diseñar aplicaciones basadas en IA.

---

# Una breve evolución

De forma general, la evolución ha seguido esta tendencia:

- **Primeros modelos:** ventanas reducidas, adecuadas para tareas simples y consultas cortas. Las aplicaciones debían fragmentar cualquier documento antes de enviarlo.
- **Segunda generación:** capacidad suficiente para documentos extensos y conversaciones prolongadas. Aparece la posibilidad de enviar contratos, artículos o sesiones de soporte completas en una sola solicitud.
- **Modelos actuales:** procesamiento de grandes bases documentales, múltiples archivos y sesiones de trabajo complejas. Algunos modelos superan el millón de tokens de contexto.

Más importante que el número absoluto de tokens es la posibilidad de mantener información relevante durante más tiempo sin necesidad de reconstruir el estado de la conversación en cada solicitud.

---

# ¿Más contexto siempre es mejor?

No necesariamente.

Una ventana más grande ofrece ventajas evidentes:

- menos necesidad de resumir;
- mayor continuidad conversacional;
- posibilidad de analizar documentos completos;
- mejor soporte para tareas complejas.

Sin embargo, también introduce desafíos:

- mayor costo por consulta;
- incremento de la latencia;
- más información irrelevante compitiendo por la atención del modelo;
- mayor complejidad para construir un contexto de calidad.

El objetivo del AI Engineer no es llenar la ventana, sino utilizarla de manera inteligente.

---

# El fenómeno "lost in the middle"

Ampliar la ventana de contexto no garantiza que el modelo utilice toda la información con la misma eficacia.

Investigaciones recientes han documentado un fenómeno conocido como **"lost in the middle"**: los modelos tienden a prestar mayor atención a la información ubicada al principio y al final del contexto, mientras que los datos situados en el centro del documento reciben menos peso durante el razonamiento.

Las consecuencias prácticas son significativas:

- colocar instrucciones críticas a mitad del system prompt puede degradar los resultados;
- insertar los documentos más relevantes en el centro de un contexto muy largo puede hacer que el modelo los subutilice;
- una conversación extensa puede provocar que el modelo "olvide" compromisos asumidos en turnos intermedios aunque estos sigan siendo parte del contexto visible.

La respuesta arquitectónica al "lost in the middle" es diseñar el orden del contexto de forma deliberada: las instrucciones más importantes van al principio, los documentos más relevantes al inicio o al final, y la información de menor prioridad en el centro.

---

# Calidad antes que cantidad

Agregar información indiscriminadamente rara vez mejora los resultados.

Por ejemplo, incorporar cien páginas de documentación cuando solo dos contienen la respuesta puede dificultar el razonamiento del modelo: introduce ruido, aumenta el costo y, combinado con el fenómeno "lost in the middle", puede hacer que el modelo produzca respuestas menos precisas que si hubiera recibido solo las dos páginas relevantes.

Una arquitectura madura prioriza:

- información pertinente;
- contexto actualizado;
- datos sin duplicación;
- instrucciones claras ubicadas en posiciones privilegiadas.

---

# Impacto en la arquitectura

La ampliación de las ventanas de contexto permitió construir soluciones que antes eran impracticables:

- asistentes empresariales con acceso a grandes manuales;
- análisis de contratos extensos;
- revisión de repositorios de código;
- agentes que coordinan múltiples herramientas;
- procesamiento de informes completos.

No obstante, estas aplicaciones siguen necesitando mecanismos como RAG, memoria y filtrado de contexto para mantener un buen rendimiento. Una ventana grande sin estrategia de selección convierte el problema de la capacidad en un problema de calidad.

---

# Buenas prácticas

- Diseñar para la calidad del contexto, no para su tamaño.
- Colocar las instrucciones y los documentos más importantes al principio del contexto.
- Medir el costo asociado a ventanas extensas antes de adoptar modelos con mayor capacidad.
- Recuperar únicamente la información necesaria para cada consulta.
- Combinar ventanas amplias con estrategias de Context Engineering.

---

# Resumen

La evolución de las ventanas de contexto amplió enormemente las capacidades de los modelos de lenguaje. Sin embargo, una ventana mayor no elimina la necesidad de diseñar cuidadosamente el contexto: fenómenos como el "lost in the middle" demuestran que el orden y la selección importan tanto como la capacidad total. La diferencia entre una aplicación correcta y una excelente continúa estando en la arquitectura que construye el AI Engineer.

En la próxima sección analizaremos qué ocurre cuando el contexto supera la capacidad del modelo y qué estrategias permiten administrar esa limitación.
