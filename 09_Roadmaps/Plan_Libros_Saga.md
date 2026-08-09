# Plan — Arquitectura Completa de Libros de la Saga (2026-07-25)

*Documento de arquitectura, no canon de prosa. Nace de `99_Reference/Agent_Notes/codex/2026-07-25_incubadora-nombres-libros-saga.md`, triada punto por punto con el autor el 2026-07-25. Fija los 14 libros principales (0-13) de *Destiny: Renewed Fate* y su relación con `01_Timeline/` (Ages) y `10_Chapters/` (numeración de capítulos de la saga completa).*

---

## Qué es esto

`01_Timeline/` sigue siendo el mapa cronológico por Ages — no se toca, no se renombra. Los **libros** (`11_Books/`) son la unidad literaria de lectura: agrupan una o varias Ages según la lógica de expansión/evento de Destiny, siguiendo el precedente ya fijado por **Book 02 — The King of Shapes** (`09_Roadmaps/Plan_Book02_TheKingOfShapes.md`).

## Regla de agrupación

- **Destiny 1:** un libro por expansión/evento mayor.
- **Destiny 2:** un libro por expansión, incluyendo sus temporadas respectivas.
- **Final Shape:** excepción — se divide en 3 libros (campaña, Excision, cierre posterior).
- **Prólogo:** entra en la numeración como **Book 00** (decisión de esta sesión — tiene carpeta propia y capítulos independientes en `11_Books/`, igual que cualquier otro libro).
- **Epílogo:** queda como coda separada, fuera de la numeración 0-13 (Book 13, *The Last Shape*, ya cumple esa función de cierre).

## Lista completa — 14 libros (Book 00 - Book 13)

| # | Título | Contenido | Ages |
|---|--------|-----------|------|
| 00 | **The Flower Game** | Prólogo + material cosmológico previo al despertar | Prólogo |
| 01 | **New Beginnings** | Destiny 1 vanilla + Dark Below + House of Wolves, agrupados | Age I |
| 02 | **The King Of Shapes** | The Taken King expandido | Age II |
| 03 | **Evolution of Ashes** | Rise of Iron + Age of Triumph | Ages III-IV |
| 04 | **The False Gods** | Destiny 2 vanilla + Curse of Osiris + Warmind | Age V |
| 05 | **The Hollow Crown** | Forsaken + Annual Pass | Age VI |
| 06 | **Echoes of Salvation** | Shadowkeep — solo su propia Age, sin absorber el año siguiente | Age VII |
| 07 | **The Familiar Stranger** | Beyond Light + Hunt/Chosen/Splicer/Lost | Ages VIII-IX |
| 08 | **Labyrinth of Lies** | Witch Queen + Risen/Haunted/Plunder/Seraph | Ages X-XI |
| 09 | **The Wound in Heaven** | Lightfall + Defiance/Deep/Witch/Wish | Ages XII-XIII |
| 10 | **The Heart of Memory and Bone** | Final Shape, parte 1 — campaña / entrada al Corazón Pálido / preparación de Salvation's Edge | Age XIV |
| 11 | **A War of One and Many** | Final Shape, parte 2 — Excision y cierre inmediato del Testigo | Age XV |
| 12 | **The Gambit of the Two Kings** | Final Shape, parte 3 — Echoes/Revenant/Heresy y cierre del Gambito | Ages XVI-XVIII |
| 13 | **The Last Shape** | Coda final posterior a la saga | Epílogo |

## Decisiones fijadas en el triage del 2026-07-25

1. **Book 00 confirmado** — el Prólogo entra en la numeración principal, no queda suelto.
2. **Book 01 incluye los tres** — vanilla + Dark Below + House of Wolves en un solo libro, coherente con la regla D1=expansión agrupada y con Age I completa.
3. **Shadowkeep no absorbe el año de temporadas siguiente** — Book 06 (*Echoes of Salvation*) queda acotado a Age VII; Book 07 (*The Familiar Stranger*) conserva Hunt/Chosen/Splicer/Lost, preservando la continuidad emocional ya escrita del arco de Elsie/Kyle post-Shadowkeep pegado a Beyond Light.
4. **Cortes de Final Shape confirmados sin ajuste** — coinciden sin fricción con el Macroevento Tripartito ya fijado con Codex el 2026-07-12 (`project-finalshape-macroevento-tripartito`): Umbral/Campaña (Book 10), Excision (Book 11), cierre (Book 12).
5. **Apéndices quedan como colección paralela, sin novelar** — no se integran al índice principal de libros todavía.

## Apéndices y proyectos satélite (colección paralela, no numerada)

No son libros principales de la saga. Quedan listados y reconocidos, fuera de la numeración 0-13, activables solo si el autor decide escribirlos en el futuro:

- **The Prophecy of Doom** — apéndice/evento futuro tentativo para *Edge of Fate*.
- **The Prisoner of Fate** — apéndice/evento futuro tentativo para *Renegades*.
- **A History of Dead Futures** — libro/apéndice dedicado a los timelines de Elsie (`06_Timeline_Archives/`).
- **The Crownless Navigator** — libro/apéndice dedicado a Faris.
- **The Northless King** — libro/apéndice dedicado al Kyle Oscuro del Mandato Cero.
- **Futuras historias sin Kyle/Elsie/Ghost como centro** — carta abierta para un futuro lejano si surge suficiente material con autonomía narrativa real.

## Lo que esto NO hace

- No mueve ni renombra ninguna escena de `05_Dialogues/` ni ninguna Age de `01_Timeline/`.
- No reemplaza a Book 02 ya diseñado — este documento formaliza el resto de la colección alrededor de un precedente ya fijado.
- No asigna carpetas ni `00_Book_Map.md` a los libros 00, 01, 04-13 todavía — eso se hace libro por libro, cuando llegue su turno de diseño o redacción, siguiendo el mismo patrón que Book 02. **Excepción (2026-08-08): Book 03 — Evolution of Ashes ya tiene carpeta y `00_Book_Map.md` propios**, arrancado antes de tiempo porque tres capítulos de formación de Jaden (Suetake, Xûr, Dark Drinker) se reubicaron ahí desde Book 02 el mismo día que ese libro se terminó — ver `11_Books/Book_03_Evolution_Of_Ashes/00_Book_Map.md`. Su Prólogo (3 capítulos) está escrito; el resto del libro sigue sin diseñar.
- No fija fecha ni orden de redacción entre libros — Book 02 ya está completo (35 capítulos, 2026-08-08) y en proceso de auditoría con Codex; Book 03 tiene apenas su Prólogo escrito. Ninguno de los libros 00, 01, 04-13 tiene fecha de inicio todavía.
- No revela en los títulos que la respuesta de Kyle es una vida construida; eso se paga leyendo, no en la tabla de contenido.

## Próximo paso

Book 02 quedó completo el 2026-08-08 (35 capítulos) — el trabajo activo inmediato es su auditoría de continuidad/filosofía con Codex, no un libro nuevo. Book 03 (`11_Books/Book_03_Evolution_Of_Ashes/00_Book_Map.md`) tiene su Prólogo escrito por relocalización de material de Jaden, pero su diseño real (estructura de Partes, el arco de camaradería Kyle/Jaden) sigue sin empezar y no es urgente todavía.

---

*Conecta con: `99_Reference/Agent_Notes/codex/2026-07-25_incubadora-nombres-libros-saga.md`, `09_Roadmaps/Plan_Book02_TheKingOfShapes.md`, `11_Books/README.md`, `01_Timeline/`.*
