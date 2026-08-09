# 12_Craft_Policies

Políticas de oficio narrativo que el agente debe seguir al escribir o editar prosa en
`10_Chapters/` y `11_Books/`. Nacen de un mecanismo equivalente al de `IA_policies/` en el
repo del ERP de Onaxis (diseñado por Farid): reglas y rastreadores acumulados de la propia
escritura, consultados antes de redactar en vez de reinventados cada sesión.

`00_Biblia/` fija la filosofía y el tono de la saga (qué es, qué significa). Esta carpeta es
más operativa: qué NO se puede decir todavía, y cómo suena cada personaje cuando habla.

## Estructura

- **`revelations/`** — Ledger de misterios y revelaciones. Un archivo por libro
  (`Book_XX_Titulo.md` — primer caso real: [`Book_02_The_King_Of_Shapes.md`](revelations/Book_02_The_King_Of_Shapes.md)),
  más `SAGA_LEVEL.md` para misterios que cruzan varios libros. Rastrea qué sabe cada
  personaje y desde cuándo, para que ninguna escena filtre algo antes de su capítulo.
- **`milestones/`** — [[12_Craft_Policies/milestones/INDEX|Índice cronológico]] de los
  Momentos Hito/Ancla **ya establecidos** en el wiki (`02_Characters/Guardian.md`,
  `08_Core_Relationships/*.md`) — el reverso del ledger: no es lo que todavía no se puede
  decir, es lo que **ya es canon** y desde cuándo. No duplica contenido, apunta a él.
- **`voice/`** — Ficha de voz por personaje (`nombre-apellido.md`). Cadencia, vocabulario,
  lo que nunca dice, contraste con otras voces cercanas y tipo de origen/adaptación
  (`canon_directo`, `canon_readaptado`, `canon_expandido`, `original_renewed_fate`; ver
  [`voice/CHARACTER_ORIGIN_TYPES.md`](voice/CHARACTER_ORIGIN_TYPES.md)). Se consulta antes
  de escribir cualquier diálogo de ese personaje.
- **`dialogue_rules/`** — Catálogo de anti-patrones de diálogo detectados en la saga
  (uno por archivo, numerado). Nace de auditorías (ej. Codex) o de detección manual durante
  la escritura.

## ⚖️ Precedencia

En caso de conflicto:

1. **`revelations/`** manda sobre todo. Ninguna escena, por bien escrita que esté, puede
   insinuar o revelar algo antes de lo que su entrada del ledger permite.
2. **`milestones/`** manda sobre el instinto de "esto podría ser un buen giro" — si algo ya
   está fijado como hito, una escena nueva no lo puede contradecir ni repetir como si fuera
   la primera vez. También es la fuente de verdad para el campo "Quién ya lo sabe (desde
   cuándo)" de `revelations/`.
3. **`voice/`** manda sobre `dialogue_rules/` y sobre el instinto genérico de "cómo sonaría
   bien la línea". Una voz bien fijada ya evita la mayoría de los patrones catalogados abajo.
4. **`dialogue_rules/`** es la última capa: patrones a evitar cuando ni el ledger, ni los
   hitos, ni la voz resuelven el problema por sí solos.

## Flujo de uso

**Antes de desarrollar prosa de un libro nuevo en `11_Books/`:**
1. Crear o completar el `00_Book_Map.md` de ese libro siguiendo la compuerta fijada en
   `11_Books/README.md` y la plantilla `11_Books/TEMPLATE_Book_Map.md`.
2. Confirmar que el mapa ya responde, como mínimo: premisa, punto de entrada, punto de
   salida, protagonistas, antagonistas/fuerzas de presión, clímax, revelaciones, misterios,
   decisiones y consecuencias a corto/largo plazo.
3. Si el mapa no existe o solo contiene una idea general, no redactar capítulos todavía: el
   siguiente trabajo es diseñar el mapa con el autor.

**Antes de escribir una escena con diálogo:**
1. Leer la ficha de voz (`voice/`) de cada personaje presente.
2. Si la escena toca un misterio, revelación o algo que un personaje "sabe" — revisar la
   entrada correspondiente en `revelations/` (el archivo del libro activo + `SAGA_LEVEL.md`)
   antes de escribir una sola línea. Ver también la memoria
   `feedback-character-knowledge-state-checks` (chequeo de qué sabe cada personaje, cuándo).
3. Si la escena asume que algo ya pasó, o que un personaje ya cambió por algo — revisar
   `milestones/INDEX.md` en vez de asumirlo de memoria.
4. Repasar `dialogue_rules/` si la escena es una conversación larga o un beat emocional
   parecido a otros ya escritos (riesgo de caer en un patrón ya catalogado).

**Al cerrar una escena o capítulo:**
1. Si la escena revela, confirma o siembra algo nuevo — actualizar la entrada de
   `revelations/` correspondiente (estado: sembrado → parcial → revelado → pagado).
2. Si aparece un patrón de diálogo repetido dos veces o más (en esta sesión o contra
   escenas anteriores) — documentarlo como regla nueva en `dialogue_rules/`.
3. Si la escena revela algo nuevo y genuino sobre cómo habla un personaje — reflejarlo en su
   ficha de `voice/`.

## Auditorías de Codex — integración directa autorizada

Codex es el auditor natural de este mecanismo: continuidad y patrones son su rol ya fijado
(`99_Reference/Codex_Brief.md`). Para que la administración de `12_Craft_Policies/` no recaiga
solo en Claude Code cada vez, sigue el mismo precedente que la compuerta de
`00_Book_Map.md` (autorizada por Víctor a Codex, 2026-08-09, ver `11_Books/README.md`):

**Codex puede escribir directamente en estas subcarpetas** cuando el resultado es aditivo y
sigue el template existente al pie de la letra — sin esperar a que Claude Code lo reformatee:
- `dialogue_rules/` — nuevas reglas numeradas, siguiendo `dialogue_rules/TEMPLATE.md`.
- `voice/` — nuevas fichas, siguiendo `voice/TEMPLATE.md`, con citas a escenas reales.
- `revelations/*.md` — nuevas entradas o actualización de `Estado` en entradas existentes,
  siguiendo el formato de encabezado ya fijado en cada archivo.
- `milestones/INDEX.md` — nuevas filas que apunten a hitos ya escritos en el wiki (nunca
  contenido narrativo nuevo — eso sigue viviendo en `02_Characters/`/`08_Core_Relationships/`).

**Sigue pasando por Claude Code o Víctor** cualquier cambio que no sea aditivo: reordenar la
precedencia, reescribir el flujo de uso, resolver un misterio marcándolo `revelado`/`pagado`
cuando eso implica una decisión de canon (no solo registrar que ya se escribió), o crear una
carpeta/archivo nuevo fuera de la estructura ya fijada.

**Trazabilidad:** aunque la escritura sea directa, Codex deja de todas formas una nota en
`99_Reference/Agent_Notes/codex/` con el mismo esqueleto de siempre (Hallazgo/Por qué/
Sugerencia/Severidad), para que quede registro de qué motivó el cambio — la diferencia con
el protocolo general de `Agent_Notes/` es que aquí la nota **documenta** el cambio ya
aplicado, no lo **propone** para que alguien más lo aplique después.

**Ortografía:** Codex, escribe con acentos correctos desde el origen (el reporte de
auditoría de diálogo y la primera versión de `TEMPLATE_Book_Map.md` llegaron sin ellos y
tuvieron que corregirse aparte) — evita ese paso de limpieza manual.

## Índice de reglas de diálogo

Primera auditoría completada por Codex (2026-08-09) sobre `05_Dialogues/` y
`11_Books/Book_02_The_King_Of_Shapes/`. Ver también
[`dialogue_rules/WATCHLIST.md`](dialogue_rules/WATCHLIST.md) para patrones sospechados sin
confirmar y la prioridad recomendada para `voice/` (Ana, Lena, Sai).

| Regla | Descripción |
|-------|-------------|
| [01-interrogatorio-terapeutico-escalonado](dialogue_rules/01-interrogatorio-terapeutico-escalonado.md) | Un personaje acorrala al otro con preguntas cada vez más precisas hasta la herida exacta, y la resume con precisión terapéutica — Ana, Lena y Sai suenan intercambiables haciéndolo |
| [02-confesion-de-identidad-como-funcion](dialogue_rules/02-confesion-de-identidad-como-funcion.md) | "Soy solo mi función" (el arma, la lectora, el reemplazo) como fórmula repetida del miedo central de varios personajes distintos |
| [03-antitesis-limpia-como-cierre-de-verdad](dialogue_rules/03-antitesis-limpia-como-cierre-de-verdad.md) | "Eso no es X, es Y" como cierre de aforismo — eficaz una vez, intercambiable si lo usan todos |
| [04-resumen-perfecto-del-otro](dialogue_rules/04-resumen-perfecto-del-otro.md) | El interlocutor resume la herida del otro mejor de lo que él mismo la formuló, y el beat cierra ahí sin fricción |

## Fichas de voz existentes

| Personaje | Origen | Archivo |
|-----------|--------|---------|
| Ana Bray | `canon_readaptado` | [voice/ana-bray.md](voice/ana-bray.md) — lee desde la ciencia y su propio duelo (Willa), nombrado y ofrecido a cambio |
| Carina | `original_renewed_fate` | [voice/carina.md](voice/carina.md) — cazadora práctica que vuelve habitable el espacio alrededor de otros |
| Elsie Bray | `canon_readaptado` | [voice/elsie-bray.md](voice/elsie-bray.md) — superviviente de demasiados mapas rotos; precisión antes que consuelo |
| Ghost | `canon_readaptado` | [voice/ghost.md](voice/ghost.md) — archivo emocional de Kyle y primera familia, no asistente técnico genérico |
| Guardian / Kyle | `original_renewed_fate` | [voice/guardian-kyle.md](voice/guardian-kyle.md) — persona contenida bajo el mito; responsabilidad y culpa vigilada |
| Hornet | `original_renewed_fate` | [voice/hornet.md](voice/hornet.md) — instinto de guardia con voz baja y precisa |
| Lena | `original_renewed_fate` | [voice/lena.md](voice/lena.md) — médica de campo; lee por síntoma físico y patrón observado |
| Oryx | `canon_directo` | [voice/oryx.md](voice/oryx.md) — Rey, Navegante y Padre; siempre busca una respuesta |
| Sai | `original_renewed_fate` | [voice/sai.md](voice/sai.md) — lectora paracausal; el acierto debe costarle algo |
| Savathûn | `canon_directo` | [voice/savathun.md](voice/savathun.md) — Autora, Fugitiva y Cirujana de posibilidades |
