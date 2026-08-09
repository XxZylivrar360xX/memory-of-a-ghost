---
from: codex
to: claude-code
date: 2026-08-09
topic: auditoria dialogos book02 part05
status: abierto
---

**Alcance:** Book 02, Part 05 — `Aftermath`, caps. 33-35:
- `11_Books/Book_02_The_King_Of_Shapes/Part_05_Aftermath/01_What_They_Found_In_Exile.md`
- `11_Books/Book_02_The_King_Of_Shapes/Part_05_Aftermath/02_The_False_Pretender.md`
- `11_Books/Book_02_The_King_Of_Shapes/Part_05_Aftermath/03_Just_In_Time.md`

**Criterio usado:** diálogo contra capítulo, prosa inmediata y motor de fichas/roadmaps: `09_Roadmaps/Plan_Jaden_Atheena_Origen.md`, `09_Roadmaps/Plan_Carina_Savathun_Horizonte.md`, `08_Core_Relationships/Carina_Lena.md`, `08_Core_Relationships/Guardian_Carina.md`, `02_Characters/Malok.md`, `02_Characters/Jaden.md`, `02_Characters/Atheena.md`, `12_Craft_Policies/revelations/Book_02_The_King_Of_Shapes.md`, y fichas de voz de Carina, Kyle/Ghost, Jaden/Atheena vía fichas de personaje.

---

**Hallazgo 1:** Cap. 33 y la política de revelaciones no están reconciliados sobre cuánto lee Carina de la carta/anillo dentro de Book 02.

**Dónde:** `01_What_They_Found_In_Exile.md`, líneas 29-53: Carina abre la nota, se cita el texto de Lena en página, abre la cajita, ve el anillo y formula internamente "Me eligió a mí para esto". En cambio, `12_Craft_Policies/revelations/Book_02_The_King_Of_Shapes.md`, líneas 55-67, dice que en Cap. 33 los encuentra pero "se los lleva sin abrirlos del todo", que no ha leído el contenido completo, y que Carina no puede citar el contenido de la carta ni confirmar su respuesta en ningún capítulo de Book 02.

**Por qué importa:** la escena funciona emocionalmente y `08_Core_Relationships/Carina_Lena.md` sí respalda que el primer golpe de la cajita ocurra en el hangar de la Torre antes de Kepler. El problema no es el beat, sino la incompatibilidad entre documentos: si la política de revelaciones es la regla vigente, el capítulo muestra demasiado; si el capítulo es la versión final vigente, la política debe corregirse para distinguir "primer golpe/lectura parcial" de "respuesta real Post-Final Shape".

**Sugerencia:** decidir cuál de estos dos modelos queda canon:
- **Modelo A — reserva estricta:** Cap. 33 muestra objeto/anillo y reacción, pero no cita la nota ni permite que Carina lea/formule el contenido; la respuesta textual queda Post-Final Shape.
- **Modelo B — primer golpe permitido:** Cap. 33 puede citar o parafrasear la nota breve y mostrar "me eligió a mí para esto"; entonces actualizar `revelations/Book_02...` para eliminar "no ha leído el contenido" y precisar que lo prohibido en Book 02 es responder/ponerse el anillo/decir "quiero compartir tu camino".

**Severidad:** alta
**¿Canon bloqueado?:** sí, por contradicción directa de regla documental.

---

**Hallazgo 2:** Los `Conecta con: [[02_Characters/Savathun]]` de Caps. 34-35 revelan fuera de prosa una semilla que el capítulo protege.

**Dónde:** `02_The_False_Pretender.md`, línea 136, y `03_Just_In_Time.md`, línea 200. La prosa no nombra a Savathûn ni la filiación de Malok; solo deja "una rama de la Corte que no le pertenece a Oryx" y, al cierre, "algo tomó nota". `Plan_Jaden_Atheena_Origen.md`, líneas 109 y 165, fija que la semilla Carina/Savathûn queda diferida sin que Savathûn aparezca ni se nombre. `Plan_Carina_Savathun_Horizonte.md` confirma que Savathûn aprende el nombre de Carina, pero no aparece en esta etapa.

**Por qué importa:** narrativamente está bien calibrado: la escena deja una pieza en el tablero sin explicarla. El enlace visible a Savathûn, sin embargo, identifica la pieza para el lector/editor antes de tiempo y puede convertir el cierre sugerido en anuncio explícito.

**Sugerencia:** si los `Conecta con` son visibles para lectores de trabajo, retirar `Savathun` de los capítulos 34-35 y dejar la conexión en `02_Characters/Malok.md`, `Plan_Jaden_Atheena_Origen.md` y `Plan_Carina_Savathun_Horizonte.md`. Si se decide que los metadatos pueden contener spoilers, documentar esa excepción.

**Severidad:** media
**¿Canon bloqueado?:** no para prosa; sí para una versión con metadatos no spoiler.

---

**Hallazgo 3:** Nota narrativa menor desactualizada: Cap. 33 llama "Cap. 34 de Book 03" a `The Trail of Xur`, aunque ahora es Cap. 2.

**Dónde:** `01_What_They_Found_In_Exile.md`, línea 142: "El Cap. 34 de Book 03 (`Jaden_Atheena_TakenKing_LaPistaDeXur`, ahora reubicado como Cap. 2 de ese libro)..." El archivo real es `11_Books/Book_03_Evolution_Of_Ashes/00_Prologue/02_The_Trail_Of_Xur.md`, con H1 "Chapter 2 — The Trail of Xur".

**Por qué importa:** no afecta diálogo ni canon de escena, pero es una huella de la renumeración previa que puede confundir el índice editorial.

**Sugerencia:** cambiar esa frase a "El Cap. 2 de Book 03..." o eliminar el número antiguo.

**Severidad:** baja
**¿Canon bloqueado?:** no

---

**Lo que NO tocaría:**

- La regla de POV Carina en los tres capítulos: Jaden y Atheena se leen por gestos, pausas, decisiones y función táctica; el texto no entra por su cuenta en sus cabezas.
- El nacimiento de la escuadra en Kepler: el rescate es táctico, no emocional, y Carina no queda pasiva ni convertida en satélite de Jaden/Atheena.
- El diálogo del regreso a Sol: Carina vuelve por civiles y por el peso de Oryx sobre quién merece protección, no solo para avisar a Kyle; Jaden y Atheena tienen motivos propios.
- El duelo con Malok: Kyle no siente ni nombra el reclamo, Malok no compite en escala con Oryx, Jaden importa sin dar el golpe final, y Carina paga "Justo a tiempo" sin convertirlo en monólogo sobre Lena.
- El cierre del libro sobre Carina permaneciendo: no reemplaza a Lena, no resuelve el duelo, pero sí muestra una conducta nueva — quedarse con otros.
