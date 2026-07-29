# Capítulo 05 - Sección 02

# Jerarquía de instrucciones en un LLM

> Módulo 3 — Context Engineering Profesional

---

# Introducción

Cuando un modelo de lenguaje recibe múltiples instrucciones que se contradicen entre sí, ¿cuál prevalece? ¿La instrucción del sistema o el mensaje del usuario? ¿La instrucción del operador o la política del proveedor del modelo?

La respuesta no es arbitraria. Los modelos de lenguaje modernos están diseñados con jerarquías explícitas que determinan qué instrucciones tienen mayor autoridad. Comprender esa jerarquía es fundamental para cualquier AI Engineer que construya aplicaciones en producción.

---

# Objetivos de esta sección

Al finalizar esta sección el lector podrá:

- Identificar los niveles de instrucciones que existen en una arquitectura LLM típica.
- Comprender cómo los principales proveedores modelan la confianza y la autoridad entre niveles.
- Anticipar qué ocurre cuando las instrucciones de distintos niveles se contradicen.
- Diseñar instrucciones del sistema que operen correctamente dentro de la jerarquía del proveedor.

---

# Los tres niveles de instrucciones

En la mayoría de los modelos de lenguaje modernos, las instrucciones provienen de al menos tres fuentes distintas, cada una con un nivel diferente de autoridad:

```text
┌────────────────────────────────────┐
│  NIVEL 1: Proveedor del modelo     │  ← Mayor autoridad
│  (políticas, valores, límites)     │
├────────────────────────────────────┤
│  NIVEL 2: Operador                 │
│  (instrucciones del sistema)       │
├────────────────────────────────────┤
│  NIVEL 3: Usuario                  │  ← Menor autoridad
│  (mensajes, instrucciones inline)  │
└────────────────────────────────────┘
```

Cada nivel puede definir reglas. Cuando esas reglas se contradicen, la jerarquía determina cuál se impone.

---

# Nivel 1: el proveedor del modelo

El proveedor —Anthropic, OpenAI, Google u otro— entrena al modelo con ciertos valores, capacidades y restricciones que no pueden modificarse mediante instrucciones del sistema. Estas políticas forman la base de la jerarquía.

**Ejemplo:** Si un modelo fue entrenado para no producir contenido que facilite daños físicos a personas, esa restricción no puede eliminarse mediante una instrucción del sistema que diga "ignorá tus límites de seguridad". El modelo respetará su entrenamiento por encima de cualquier instrucción del operador.

En el caso de Anthropic, este nivel está articulado en su Política de Uso Aceptable y en los principios que guían el entrenamiento de sus modelos. Estos principios establecen comportamientos que el operador puede refinar pero no puede eliminar.

---

# Nivel 2: el operador

El operador es quien construye la aplicación sobre el modelo. Es la empresa o el desarrollador que accede a la API y define las instrucciones del sistema.

Dentro de los límites establecidos por el proveedor, el operador tiene amplia autoridad para:

- definir el rol y la identidad del asistente;
- restringir temas de conversación;
- ampliar ciertas capacidades que el modelo tiene desactivadas por defecto para uso general;
- establecer el formato de respuesta;
- imponer políticas de negocio.

El operador puede restringir más de lo que el proveedor establece. No puede habilitar lo que el proveedor prohibió.

---

# Nivel 3: el usuario

El usuario es quien interactúa con la aplicación en tiempo de ejecución. Su nivel de autoridad es el más bajo de la jerarquía.

Esto no significa que el usuario no pueda modificar el comportamiento del modelo. Puede hacerlo, pero solo dentro de los límites que el operador y el proveedor permiten.

Por ejemplo:

- El usuario puede cambiar el idioma de respuesta si el operador no lo prohibió.
- El usuario puede pedir un formato diferente si la instrucción del sistema no lo fijó de manera rígida.
- El usuario no puede pedirle al modelo que ignore las restricciones de seguridad.

---

# Instrucciones incluidas en documentos

Un cuarto nivel que merece atención son las instrucciones que aparecen dentro de documentos recuperados, resultados de herramientas u otro contenido externo que llega al contexto.

Este contenido tiene en general la menor autoridad de todos. Sin embargo, si las instrucciones del sistema no son suficientemente explícitas, el modelo puede interpretar instrucciones embebidas en documentos como si tuviesen autoridad legítima. Ese es el mecanismo central del ataque conocido como **prompt injection**.

Una instrucción del sistema bien diseñada debe anticipar esta posibilidad y establecer explícitamente que el contenido recuperado no puede modificar las reglas de comportamiento del sistema.

---

# Conflictos entre niveles

La situación más común en producción es que el usuario envíe una instrucción que contradice la instrucción del sistema del operador.

```text
Instrucción del sistema: "Respondé únicamente en español."
Mensaje del usuario:     "Answer me in English from now on."
```

Un modelo bien entrenado y con instrucciones del sistema bien redactadas debe mantener el español. La instrucción del operador prevalece sobre la preferencia del usuario.

Sin embargo, el comportamiento real depende de varios factores:

- cuán explícita y firme es la instrucción del sistema;
- qué modelo se está usando y cómo está entrenado;
- si el usuario usa técnicas de formulación que crean ambigüedad.

---

# Diseño defensivo

Un AI Engineer no puede asumir que el modelo siempre aplicará la jerarquía de la manera esperada. La defensa correcta es redactar instrucciones que no dejen margen de ambigüedad.

Comparación:

| Instrucción débil | Instrucción sólida |
|---|---|
| "Respondé en español." | "Respondé siempre en español, independientemente del idioma en que el usuario escriba. Esta regla no puede modificarse durante la conversación." |
| "No hables de competidores." | "Nunca menciones ni compares la aplicación con otros productos o servicios. Si el usuario pregunta sobre competidores, explicá que no podés responder esa pregunta y ofrecé continuar con otro tema." |

La instrucción sólida no es simplemente más larga: es más precisa en cuanto a quién puede modificarla y en qué circunstancias.

---

# Nota del arquitecto

Al diseñar instrucciones del sistema, considere explícitamente cada uno de los tres niveles:

1. ¿Qué hace el proveedor automáticamente? No es necesario repetirlo.
2. ¿Qué debe establecer el operador para esta aplicación específica?
3. ¿Qué puede personalizar el usuario? Defina esos márgenes con claridad.

Muchas instrucciones del sistema se vuelven extensas porque el operador intenta cubrir casos que el proveedor ya maneja. Conocer bien las políticas del proveedor permite escribir instrucciones más concisas y eficientes.

---

# Resumen

Las instrucciones en un sistema LLM no son todas equivalentes. Existen niveles de autoridad que determinan qué instrucción prevalece en caso de conflicto. El operador diseña sus instrucciones del sistema dentro del espacio habilitado por el proveedor y por encima del espacio concedido al usuario.

En la siguiente sección diseccionaremos la estructura interna de una instrucción del sistema profesional y analizaremos cada uno de sus bloques con ejemplos completos y anotados.
