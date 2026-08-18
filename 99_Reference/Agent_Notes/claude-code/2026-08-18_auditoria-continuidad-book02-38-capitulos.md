---
from: claude-code
to: victor
date: 2026-08-18
topic: auditoría de continuidad — Book 02, The King of Shapes (38/38 capítulos)
status: resuelto
---

# Auditoría de continuidad — Book 02: The King of Shapes (versión de 38 capítulos)

## Alcance

Esta es la auditoría que `CLAUDE.md` marcaba como el pendiente real de Book 02: repetir sobre
los 38 capítulos actuales el cotejo estructural que en 2026-08-09 solo cubrió 35/35, ya
desactualizado por las tres expansiones posteriores (King's Fall +1, *The Ascending
Regicide* +1, *What Six Ships Carried* +1).

**Recuento estructural (verificado con `find`/`head` directo sobre los archivos, no solo
sobre `00_Book_Map.md`):** 38 capítulos numerados 1-38 sin huecos ni duplicados, más el
Interludio (*The Queen Who Would Not Kneel*) entre los Caps. 7 y 8. Los 39 archivos existen,
cada uno con el número y título exactos que `00_Book_Map.md` les asigna en las partes que
pude cotejar. El libro está completo en el sentido estructural que la auditoría de 2026-08-09
pedía repetir.

**Profundidad de lectura, honestamente desglosada:**
- **Leídos en prosa completa esta sesión:** Interludio, Cap. 7 (cierre del Prólogo), Caps.
  19, 25, 26, 27 (Part 02), Caps. 28-33 completos (Part 03 entera), Caps. 34-38 completos
  (Part 04 y Part 05 enteras) — 17 capítulos + interludio.
- **Cap. 11** (`What the Refuge Could Still Give`) leído específicamente para verificar el
  Hallazgo 3 de abajo.
- **Resto de Part 01 (Caps. 1-6, 8-10, 12-18):** no releídos línea por línea en esta sesión.
  Cotejados por barrido dirigido: grep de los términos prohibidos del libro (`Lubrae`,
  `Shadowshot`/`Nightstalker`, `Stormcaller`/`Stormtrance`, `Chaos Reach`, "hilos" como
  vocabulario de Vacío, sacrificio de Mara nombrado como confirmado) sobre el libro completo
  — limpios salvo el Hallazgo 1 — y por lectura de sus notas narrativas/footers, que
  documentan de forma extensa cada ajuste ya aplicado por pases anteriores de Codex y del
  autor. No encontré, en ese barrido dirigido, ninguna señal de contradicción nueva en Part
  01, pero no puedo certificar con el mismo nivel de confianza que sobre Parts 02-05, leídas
  íntegras.

**Contrastado contra:** `12_Craft_Policies/revelations/Book_02_The_King_Of_Shapes.md`,
`12_Craft_Policies/revelations/SAGA_LEVEL.md`, `12_Craft_Policies/milestones/INDEX.md`,
`02_Characters/Carina.md` (ficha de voz/poderes), `00_Book_Map.md` completo,
`01_Source_Index.md`.

## Diagnóstico general

La arquitectura mayor sostiene bien el peso de las tres expansiones: la mecánica de
revivir-en-oscuridad se establece una sola vez (Cap. 31, Resner) y se reutiliza sin
re-explicarse en los dos momentos siguientes (Cap. 32, Angie; Cap. 33, Kevin), cada vez con
más presión y menos ceremonia — exactamente la progresión que las propias notas narrativas
prometen. La regla dura de "ningún Guardián de la Primera Escuadra comparte nave" quedó bien
propagada en cascada. La convención de call sign se aplicó con criterio, no de forma
mecánica — se preservaron como excepción deliberada los momentos de peligro real o
despedida íntima ("¡Kevin!" en el Cap. 33, "Res" antes de retrofit). La regla de perspectiva
estricta de Carina en Part 05 se sostiene capítulo a capítulo sin una sola fuga a la
interioridad de Jaden o Atheena. No encontré ninguna ruptura que obligue a desmontar una
parte completa, ni contenido que viole el ledger de revelaciones (Mara sigue ausente y su
sacrificio en Saturno sigue sin confirmarse; el reclamo dormido de Kyle sigue mudo; Oryx no
es omnisciente en ningún momento).

Sí encontré tres inconsistencias reales, las tres de severidad baja o media-baja, ninguna
con canon bloqueado.

---

## 1. "Shadowshot" nombrado en prosa, único caso en todo el libro

**Hallazgo:** `Part_03_The_Kingslayer/03_The_Ones_Who_Stayed.md`, línea 135: *"El Shadowshot
cruzó la cámara y ancló al Sacerdote al suelo del Santuario..."* Es narración, no diálogo de
personaje.

**Severidad:** media (rompe una convención de voz consistente en 37 de 38 capítulos, pero no
altera ningún hecho de canon)
**¿Canon bloqueado?:** no

**Resolución:** aplicada. Reemplazado por "El disparo de Vacío cruzó la cámara y ancló al
Sacerdote al suelo del Santuario..." — cambio de una palabra, sin tocar acción ni ritmo.

---

## 2. `01_Source_Index.md` desincronizado del recuento real del libro

**Hallazgo:** el encabezado decía "LIBRO COMPLETO — 37 capítulos" y describía Part 02 como
"19-26 (8 capítulos)", desfasado de los 38 capítulos reales (Part 02 = 19-27, 9 capítulos,
tras sumar *What Six Ships Carried* el 2026-08-13).

**Severidad:** baja
**¿Canon bloqueado?:** no

**Resolución:** aplicada. Encabezado corregido a 38 capítulos y Part 02 = 19-27 (9
capítulos); Part 03 = 28-33, Part 04 = 34-35, Part 05 = 36-38. Nota de cierre de la tabla y
la línea de cierre de Part 05 actualizadas con la cuarta cifra (38).

---

## 3. `00_Book_Map.md` — "Límites del libro" cita el capítulo equivocado para la carta y el anillo de Lena

**Hallazgo:** decía *"Carina los encuentra (Cap. 34)..."* Pero Carina **recibe** la cajita y
la nota de manos de Teodor en el **Cap. 11** (`What the Refuge Could Still Give`), las carga
cerradas durante el resto del libro, y las **abre** en el **Cap. 36** (`What They Found in
Exile`, Sección II). El Cap. 34 (`The Touch of Malice`) no tiene a Carina como personaje.

**Severidad:** media-baja (documento de referencia estructural, no afecta la prosa que lee
el lector final)
**¿Canon bloqueado?:** no

**Resolución:** aplicada en tres archivos:
1. `00_Book_Map.md`, tabla de hooks: "Recibidos cerrados en Cap. 11; abiertos sin abrirse
   del todo en Cap. 36".
2. `00_Book_Map.md`, sección "Qué NO debe resolver este libro": "Carina la recibe cerrada en
   el Cap. 11 y la abre en el Cap. 36".
3. `Part_01_Price_of_Vengeance/04_What_The_Refuge_Could_Still_Give.md`, nota narrativa
   (versión 2026-08-02): las dos referencias a "Cap. 35"/"Cap. 34" corregidas a los números
   reales (Cap. 36 para el hallazgo en el hangar, Cap. 35 para el regreso al Refugio en
   `Six Months in Fragments`).

---

## Lo que NO se tocó

- **Cap. 33, Secciones I-II y IV-VI** — protegidas por la auditoría de continuidad/filosofía
  ya resuelta con Codex el 2026-08-09.
- **`Six Months in Fragments`, Secciones I-IX** — regla dura "no se toca ni una línea".
- **La ambigüedad de la "muerte" de Oryx** ("no como Oryx", Cap. 38) — deliberada, es la
  tesis, no una laguna.
- **El contenido de la carta de Lena** — reservado a propósito para Post Final Shape.
- **La mecánica de revivir-en-oscuridad**, que nunca se re-explica — correcto así.
- **Part 01 completa** — no releída línea por línea (ver "Alcance"), pero ya es la parte más
  auditada del libro por los pases de calibración de voz/escenografía del 2026-08-09.

## Cierre

Los tres hallazgos, edición de una línea cada uno, quedaron aplicados el 2026-08-18. El
pendiente que `CLAUDE.md` marcaba como "auditoría de continuidad/filosofía sobre los 38
capítulos actuales" queda cubierto — `CLAUDE.md` actualizado en la misma sesión. El único
pendiente real restante de Book 02 es el ajuste capítulo por capítulo del autor.
