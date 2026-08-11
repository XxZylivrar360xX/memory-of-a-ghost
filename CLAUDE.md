# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

*Destiny: Renewed Fate* is a philosophical fan fiction saga reinterpreting the Destiny 2 universe. It is managed as an **Obsidian vault** — all files are Markdown, interlinked with Obsidian's `[[WikiLink]]` syntax. There are no build commands, tests, or code to run.

Primary language for narrative and character documents: **Spanish**. Document titles and folder names are in English.

## Idioma de respuesta del agente

**Responde siempre en español (México), nunca en inglés por defecto.** El usuario entiende inglés pero no lo quiere como idioma de respuesta — usa "tú", nunca voseo rioplatense ("vos sentís/querés"). Esto aplica a todo el texto conversacional dirigido al usuario: resúmenes, preguntas, actualizaciones de estado, mensajes de cierre de turno — todo, sin excepción, incluso cuando el trabajo técnico (nombres de archivo, código, headers en inglés por convención del vault) se mantenga en inglés donde corresponda. No confundir con el idioma del contenido narrativo en `05_Dialogues/`, `11_Books/`, etc., que sigue sus propias convenciones ya fijadas arriba y en cada carpeta.

## Vault Structure

```
Memories Of A Ghost/
├── INDEX.md                  # Master navigation index — start here
├── 00_Biblia/                # Core creative bible (read this first)
│   ├── Vision.md             # Story overview and emotional core
│   ├── Themes.md             # 12 thematic pillars
│   ├── Cosmic_Rules.md       # Cosmological and ontological framework
│   └── Narrative_Principles.md  # 17 rules that govern all storytelling decisions
├── 01_Timeline/              # Age-based narrative chronology (Prólogo + Ages I–XVIII)
├── 02_Characters/            # One file per character
├── 03_Factions/              # Faction profiles
├── 04_Concepts/              # Thematic concepts (Light, Darkness, Taken, etc.)
├── 05_Dialogues/             # Written scenes — organized by emotional protagonist
│   ├── Dialogue_Guardian/    # Scenes where Kyle's arc is primary
│   ├── Dialogue_Elsie/       # Scenes where Elsie's arc is primary
│   ├── Dialogue_Guardian_Elsie/  # Scenes developing the relationship as a character
│   ├── Dialogue_Guardian_Carina/ # Scenes developing the Kyle+Carina relationship as a character (Taken King Parte 1 origin)
│   ├── Dialogue_Ghost/       # Scenes where Ghost's arc is primary (closure + coda)
│   ├── Dialogue_Sai/         # Scenes where Sai's arc is primary
│   ├── Dialogue_Carina/      # Scenes where Carina's arc is primary (her own "before," Elenna "Lena" Lekareva)
│   ├── Dialogue_Eris/        # Scenes where Eris Morn's arc is primary
│   ├── Dialogue_Osiris/      # Scenes where Osiris's arc is primary
│   ├── Dialogue_Mara/        # Scenes where Mara Sov's arc is primary
│   ├── Dialogue_Oryx/        # Scenes where Oryx's arc is primary
│   └── Dialogue_Comentaristas/  # Torneo de los Velocistas commentary booth (Shaxx, Fynch, Drifter) — same races, outside view
├── 06_Timeline_Archives/     # Elsie's alternate timeline memories — canon support material
│   ├── Dark_Futures/         # Timelines where humanity lost — Elsie's fears
│   ├── Lost_Guardians/       # Versions of Kyle that failed, left, or fell — explains her attachment
│   ├── Bray_Legacies/        # Ana, Rasputin, Clovis in alternate paths — Elsie's family wounds
│   ├── Personal_Memories/    # Small, intimate moments that only changed Elsie
│   └── Alternate_Allies/     # People who existed in other realities and left a mark on her
├── 07_Unsorted_Ideas/        # Raw ideas, seeds, fragments
├── 08_Core_Relationships/    # Deep-dive files on the three central relationships
├── 09_Roadmaps/              # Checklists/beat-roadmaps for events confirmed but not yet written (Plan_*.md)
├── 12_Craft_Policies/        # Craft rules for prose drafting: spoiler/revelations ledger, character voice fingerprints, dialogue anti-patterns
└── 99_Reference/             # External reference material
```

## Timeline Archives — Guiding Rule

Every file in `06_Timeline_Archives/` must answer one question:

> **¿Qué parte de la Elsie actual nació aquí?**

These are not "what if" stories. They are emotional scars, memories, and lessons that continue to shape Elsie's decisions in the main narrative. If a timeline does not illuminate something about the Elsie we already know — a fear, a hope, a relationship, a philosophy — it should not exist.

## Core Creative Framework

**Central thesis:** The universe didn't need perfection — it needed someone capable of loving it despite its imperfection.

**Light vs. Darkness** are not good vs. evil. They are incomplete languages:
- Light = possibility, growth, transformation, creation
- Darkness = consciousness, identity, memory, meaning
- Neither is evil; the danger is when either claims to be absolute truth

**Prismatic** = the first state of true harmony between Light and Darkness — not fusion, but simultaneous understanding.

**The Guardian's arc:** Corpse with no identity → Weapon → Symbol → Cosmic anomaly → *Person*. The saga ends not with godhood but with the recovery of humanity.

**The Witness** is not a villain but the inevitable culmination of a civilization that couldn't endure the chaos of existence — seeks a static Final Shape to eliminate suffering, but would also eliminate all that makes life valuable.

**Antagonists as mirrors:** Every major antagonist represents a path the Guardian could have taken — Oryx (identity defined by conflict), the Witness (rejection of suffering), Savathûn (survival through manipulation), Xivu Arath (existence as eternal war).

## Narrative Rules (from Narrative_Principles.md)

When writing or editing any scene, verify it against these principles:
- **Spectacle never overrides emotion** — battles are philosophical conversations disguised as war
- **Characters over lore** — even cosmic entities must feel emotionally comprehensible
- **Philosophy must feel human** — express through real relationships, not monologues
- **The Guardian never becomes emotionally hollow** — power grows, humanity must survive
- **Vulnerability is strength** — the "I love you" carries more narrative weight than any paracausal explosion
- **No character is entirely correct** — all have wounds, contradictions, partial truths
- **Tragedy must transform** — grief without consequence empties emotional weight
- **Hope must feel earned** — it emerges after loss, failure, and despair

Every important scene should answer at least one of: *What does it mean to exist? What makes someone human? How do we continue after pain? What is worth protecting? Can someone truly change? How do you love something knowing it can disappear?*

## Obsidian Conventions

- Internal links use `[[Folder/Filename]]` format (without `.md`)
- The INDEX.md is the canonical navigation document and should be updated when new files are added
- Duplicate files exist (e.g., `Mara_Sov.md` and `Mara _Sov.md`) — prefer the correctly named file and clean up duplicates when found
- **Language convention:** File names and folder names in English. Section headers within documents in Spanish. Body content always in Spanish.

## Craft Policies (`12_Craft_Policies/`)

Reglas de oficio narrativo acumuladas de la propia escritura — equivalente prosa del
mecanismo `IA_policies/` que Farid usa en el repo del ERP de Onaxis. Documento raíz:
[`12_Craft_Policies/README.md`](12_Craft_Policies/README.md) (estructura, precedencia y
flujo completos).

**Antes de desarrollar prosa de un libro nuevo en `11_Books/`:** compuerta obligatoria
(autorizada por Víctor a Codex, 2026-08-09) — el libro necesita un `00_Book_Map.md`
completo (plantilla en `11_Books/TEMPLATE_Book_Map.md`) antes de redactar un solo capítulo.
Ver `11_Books/README.md`.

**Antes de escribir cualquier escena con diálogo:**
1. Leer la ficha de voz (`12_Craft_Policies/voice/`) de cada personaje presente, si existe.
2. Si la escena toca un misterio, revelación o algo que un personaje "sabe" — revisar
   `12_Craft_Policies/revelations/` (el archivo del libro activo + `SAGA_LEVEL.md`) **antes**
   de escribir una sola línea.
3. Si la escena asume que algo ya pasó o que un personaje ya cambió por algo — revisar
   `12_Craft_Policies/milestones/INDEX.md` (índice cronológico de hitos ya establecidos)
   antes de asumirlo de memoria.
4. Repasar `12_Craft_Policies/dialogue_rules/` si la escena es un beat emocional parecido a
   otros ya escritos.
5. Repasar `12_Craft_Policies/staging_rules/` antes de cerrar la escena — escenografía,
   acción física, silencios y transiciones tienen su propio catálogo, separado del diálogo.

**Al cerrar una escena o capítulo:** actualizar la entrada del ledger si algo se sembró,
reveló o pagó; documentar como regla nueva cualquier patrón de diálogo o de puesta en escena
(beats vacíos, sin acción física, sin transición) repetido 2+ veces.

**Después de un borrador, si algo se siente genérico:** hay especialistas de segunda pasada
en `.claude/agents/` — `dialogue-vitalizer` (diálogo intercambiable/hedging),
`scene-doctor` (¿la escena cambia algo?), `subtext-editor` (narración+diálogo dicen lo
mismo), `prose-degenericizer` (narración con muletillas de IA). Mapa completo, cuándo usar
cada uno y por qué **no** son compuerta obligatoria (son *symptom-driven*, no automáticos)
en `99_Reference/Editorial_Agent_Architecture.md`. Si una pregunta necesita anclarse en
canon real de Destiny o explorar varias direcciones antes de decidir, esos dos modos viven
en Codex (`99_Reference/Codex_Canon_Researcher.md`, `99_Reference/Codex_Brainstorming_Agent.md`)
— pedírselo a Codex, o aplicar la misma disciplina de evidencia si no está disponible.

## EPUB Build (`11_Books/`)

Cada vez que se escribe o edita un capítulo dentro de `11_Books/` — al cerrar la sesión, o al terminar/tocar un capítulo — correr:

```
python tools/epub-build/build_epub.py
```

- Regenera `tools/epub-build/output/King_of_Shapes.epub` (por default apunta a Book 02; usar `--book`/`--title`/`--cover` para otro libro) recorriendo cada carpeta `Part_XX_.../` en orden y concatenando sus capítulos.
- Antes de publicar cada capítulo, el script le quita automáticamente: (1) el bloque de encabezado (subtítulo en cursiva + Protagonistas/Ventana temporal/Lugar) y (2) el bloque de cierre — todo lo que empieza en una línea `*Conecta con:` o `*Pilares activos:` (wikilinks + nota narrativa editorial). Nada de eso debe llegar al lector.
- **Si una sesión de escritura introduce un nuevo tipo de línea de cierre en cursiva** (además de esas dos), hay que sumar su prefijo a `TRAILER_RE` en `tools/epub-build/build_epub.py` — si no, esa línea se cuela cruda al EPUB. Verificar después de correr el script que no queden `[[wikilinks]]` en `tools/epub-build/output/` (descomprimir el `.epub` y grepear `text/*.xhtml`).
- El vault sincroniza por Google Drive Desktop bajo la cuenta `vpaz@onaxis.mx`. El agente no necesita tocar nada del lado de Drive/tablet — el autor baja el `.epub` actualizado a mano cuando quiere leer la versión nueva.

## Cierre de sesión — commit y push

Al terminar cualquier sesión que haya tocado archivos del vault (capítulos, roadmaps, fichas, herramientas, etc.), antes de cerrar, sin pedir confirmación:

```
git add -A
git commit -m "..."
git push origin develop
```

- Rama de trabajo: **`develop`**. No tocar `main` — se mergea a mano cuando el autor decida; queda 10 commits atrás a propósito hasta ese momento.
- Mensaje de commit: resumen breve de lo que cambió en la sesión, mismo estilo que el historial existente (`feat: ...`, `fix: ...`).
- Este commit+push a `develop` queda **autorizado de antemano** — no es necesario preguntar cada vez, a diferencia de la regla general de git.
- Si `git push` falla porque `origin/develop` avanzó desde otro lado (edición manual, otro dispositivo), **no forzar el push**: traer los cambios remotos primero (`git pull --rebase origin develop` o equivalente), resolver cualquier conflicto, y recién entonces pushear. Si el conflicto no es trivial, parar y avisar al autor en vez de decidir por él.

## Estado del vault

- **Saga:** *Destiny: Renewed Fate* — 60 capítulos (Prólogo + Ages I–XVIII + Epílogo); Lightfall expandido a 7 capítulos (33–39), todo lo posterior corrido +4
- **Capítulos escritos:** 11 de 60 — Prólogo ×5 · Age I ×3 · Age XI ×1 (Cap 32) · Age XII ×1 (Cap 33, inicio) · Epílogo ×1 · (Lightfall caps 34–39 en esquema; resto: stubs)
- **Libros (`11_Books/`):** arquitectura completa de 14 libros fijada (Book 00-13, ver `09_Roadmaps/Plan_Libros_Saga.md`); **Book 02 — The King of Shapes queda TERMINADO — 37/37 capítulos (2026-08-08, expandido dos veces el 2026-08-10).** Prólogo completo 7/7 (*The Huntress* → *The Last Line in the Ledger*) · Part 01 — Price of Vengeance completa 11/11 + interludio (Caps. 8-18) · Part 02 — The Taken War completa **8/8** (Caps. 19-26 — suma *The Ascending Regicide*, la Primera Escuadra reuniéndose desde sus frentes separados y el consejo de guerra con Eris y un Echo de Osiris, con Mara ausente, antes de cerrar con *The Wounded Wish* y *Always Eager to Die* — la última conversación Oryx/Savathûn) · Part 03 — The Kingslayer completa **6/6** (Caps. 27-32 — dos fusiones aplicadas al redactar: Tótems+Sacerdote de Guerra colapsan en *The Ones Who Stayed*, con Carina infiltrándose por separado para rematar al Sacerdote y despedirse consolidando "Chispitas"/"Pistolera"; Oryx+Epílogo colapsan en *The Weight of a Wrong Answer*; **repasada de King's Fall del 2026-08-10** sumó un capítulo nuevo, *Everything That Isn't Solid Ground* (Hall of Souls, The Crux, The Portico), y antepuso Golgoroth's Cellar y The Transept a los capítulos ya existentes, más la mecánica de revivir-en-oscuridad —canalizar la Luz de los demás a través de la firma del Ghost del caído— en tres momentos crecientes: Resner, Angie, Kevin) · Part 04 — The Rightful Pretender completa 2/2 (Caps. 33-34 — *Six Months in Fragments* suma el reencuentro real Kyle/Carina y el regreso al Refugio) · Part 05 — Aftermath completa **3/3** (Caps. 35-37 — el exilio de Carina en Kepler, Malok, "Justo a tiempo", cierre del libro). **Regla dura de perspectiva:** Book 02 nunca entra en la cabeza de Jaden ni de Atheena por su cuenta — todo lo que el lector sabe de ellos pasa por Carina conociéndolos; por eso tres capítulos sin ninguna escena suya (origen de Jaden/Suetake, Xûr, forja de Dark Drinker) se reubicaron el mismo día a la apertura de **Book 03 — Evolution of Ashes**, primer libro después de Book 02 con carpeta y `00_Book_Map.md` propios. Tesis fijada por el autor para Book 03: Rise of Iron reimaginado como *space western* fusionado con filosofía samurái, donde la tecnología NO es la respuesta a SIVA; arco central por construir: la camaradería intermitente Kyle/Jaden, de respeto mutuo a hermandad de armas — Prólogo (formación de Jaden) completo, resto del libro sin diseñar. **Pendiente real de Book 02: auditoría de continuidad/filosofía con Codex sobre el libro completo (el cotejo estructural previo, 35/35, quedó desactualizado por las dos expansiones y debe repetirse sobre los 37 capítulos actuales), después ajuste capítulo por capítulo del autor.**
- **Escenas escritas:** 243 (+22 sesión 2026-07-13/14: 21 de la Parte 1 de Taken King + 1, Seis Meses en Fragmentos) — Dialogue_Guardian ×120 (origen del arco del Torneo — Cayde en Torneo I, Amanda en Forsaken, la Gran Inauguración del Torneo IV, la madurez con Amanda en Beyond Light, la fase de grupos, Dieciseisavos contra Los Graneros, Octavos contra Los Chacales, Sincronía cae, Cuartos contra Legado, el susto de Rook, la Final; +14 del retratamiento de Parte 1 de Final Shape y los orígenes propios de Carina/Jaden — ver sesión 2026-07-11) · Dialogue_Elsie ×28 (+2: La Coalición, Lo Que Queda Afuera) · Dialogue_Guardian_Elsie ×51 (+1: Dos Frentes; +5: la Semifinal/crisis interna de Kyle, El Entrenamiento antes de la Final, el cierre doméstico Liviano tras la integración de las Pesadillas, Siete Veces Sin Decirlo — el hueco de la mudanza a la cabaña, Fuera del Juego — el casi-beso, Season of the Haunted, antes de Plunder) · Dialogue_Ghost ×4 · Dialogue_Sai ×19 (+9: la primera Aurora familiar + el día que comparten Kyle/Carina + el origen de los jueves + los Juegos de los Guardianes + el Solsticio + el Festival de las Almas Perdidas + Lo Que Casi Vio — origen del "vi que por fin lo hiciste, lobito" de Final Shape + Las Versiones Perdidas / Lo Que Se Quedó — escenas hermanas donde Sai entiende, desde Elsie y desde Kyle, que su vínculo es "un plano entero de hechos y circunstancias") (7 de la semana del duelo + 1 origen Season of the Lost + 2 origen de los nombres + 1 primera Aurora + 1 el día que comparten + 1 los jueves + 1 los Juegos + 1 el Solsticio + 1 Almas Perdidas + 1 Lo Que Casi Vio + 2 Versiones Perdidas/Lo Que Se Quedó) · RenacimientosGuardianes ×6 · **Dialogue_Carina ×9** (7 migradas de Dialogue_Guardian el 2026-07-13 + 2 nuevas: La Presión Civil, Seis Meses en Fragmentos) · **Dialogue_Eris ×3** (carpeta nueva 2026-07-13) · **Dialogue_Mara ×3** (carpeta nueva) · **Dialogue_Oryx ×1** (carpeta nueva) · **Dialogue_Osiris ×0** (carpeta nueva, sin escena propia todavía) · **Dialogue_Guardian_Carina ×3** (carpeta nueva 2026-07-14, el nacimiento del vínculo Kyle+Carina)
- **Timeline Archives:** 19 archivos — 4 raíz · Lost_Guardians ×6 · Bray_Legacies ×2 · Personal_Memories ×5 · Alternate_Allies ×1 · Dark_Futures ×1
- **Conceptos:** 47 archivos en `04_Concepts/` (+1 sesión 2026-08-02: `Fragmentos_Calcificados_Libros_Del_Dolor`, la Fase I completa — 24 versos de los Libros del Dolor de Oryx expandidos a prosa mítica, 3 ya dramatizados en Book 02 más 21 nuevos sembrados como lore disponible)
- **Personajes:** 84 archivos en `02_Characters/` (+1 sesión 2026-08-03: `Banshee-44`, armero de la Torre, ficha ligera nacida de su escena nueva en el Cap. 8 de Book 02; +1 sesión 2026-08-02: `Avarra, la Voluntad Inconclusa`, Ángel de Guerra del Ecúmene parcialmente Tomada, guardiana del ancla de Eirene; +1 sesión 2026-07-18: `Nemo`, General Vex divergente de Kepler, primer aliado Vex de la saga — ficha completa aportada por el autor; +2 sesión 2026-07-14: `Lena` y `Suetake`, fichas propias creadas — existían solo dentro de sus escenas hasta ahora; +4 heredado: Shayura, Reed-7, Aisha, Rendel)
- **Relaciones principales:** 8 archivos en `08_Core_Relationships/` (+1: `Guardian_Carina`, sesión 2026-07-14; el conteo previo de "6" en el snapshot anterior no incluía `Guardian_Ghost` y `Ghosts_Core`, ya existentes — corregido al conteo real verificado por `ls`)
- **Última sesión:** 2026-08-10 (g) — **Dos incubadoras de Codex ejecutadas sobre Caps. 14-15** (origen de "Pistolera" y despertar de poderes nuevos), con un giro de guion en el camino: la primera versión del despertar (Vex Poseídos infectando el Jardín Negro, Carina/Kyle probando poderes en combate) se escribió siguiendo instrucción directa del autor en el chat, pero mientras se escribía, Víctor agregó al archivo de la incubadora una puesta en escena mucho más específica y distinta — sin combate en el Jardín, despertar de Kyle en la azotea de **Vigilancia Ciega** (Bahía Meridiana, Marte, referencia al mapa de Crisol de Destiny 1). Consultado, el autor eligió esa versión; la del Jardín Negro se descartó por completo. Cap. 14 (`07_The_Second_Seat.md`): origen de "Pistolera" reescrito — ya no nace de "nunca fallas", nace de que Carina contiene el disparo sobre un nodo Poseído fundido a la consola que sostiene el mapa hacia Eirene, y solo dispara el instante exacto en que el tiro deja de costar la lectura; Kyle nombra el juicio, no la puntería. Suma también un combate de salida donde ganan cada intercambio y aun así no ganan terreno ("estamos empujando agua"), sembrando la necesidad de otro lenguaje táctico. Cap. 15 (`08_The_Third_Element.md`, capítulo pasa de 9 a 12 secciones): el Jardín Negro vuelve a su forma original sin combate; en Vigilancia Ciega, Kyle falla dos veces forzando el Arco, Carina lo corrige ("no agarres la tormenta, déjala pasar"), al tercer intento nace Stormtrance de verdad y ella lo nombra "Chispitas"; como espejo, un dron Cabal corrompido resiste a Última Palabra hasta que Kyle le devuelve a Carina la misma lección (detente, ata los hilos sueltos, suelta con tu propia dirección) y ella encuentra/corta la conexión real que lo sostenía — germen crudo de Shadowshot, sin nombrarlo. Reglas duras preservadas: Chaos Reach no aparece, Shadowshot/Nightstalker formado sigue reservado a Season of the Seraph, nada de lenguaje de Estasis ni de Hebra/Strand. Ambas incubadoras marcadas resueltas, con nota explícita documentando la versión descartada. Detalle completo en `log.md`, sesión "2026-08-10 (f)" (numeración de sesión en log.md, distinta de la letra de este resumen). EPUB reconstruido tres veces y verificado limpio.
- **Sesión anterior:** 2026-08-10 (f) — **Pase editorial sobre Caps. 13-14 de Part 01 (Hellmouth/Acorazado) a partir de un handoff de Codex** (`99_Reference/Agent_Notes/codex/2026-08-10_handoff-notas-edicion-book02-part01-hellmouth-acorazado.md`, marcado resuelto). Ocho notas de Víctor aplicadas en un solo pase, con lectura previa de `12_Craft_Policies/voice/` (Kyle, Ghost, Carina, Elsie, Hornet) y los ledgers de revelaciones: Cap. 13 — Kyle ya no entra al Hellmouth sabiendo que es un duelo activo (lo entiende gradualmente); el escape tras tomar la esencia de Crota cambia de "corren mientras el lugar despierta" a un ascenso por la escalera hacia el templo con tensión de confianza/orientación bajo información incompleta; el primer encuentro con Carina deja de sentirse deus ex machina (ella y Hornet ya iban hacia la Tumba del Mundo por su cuenta) y suma reconocimiento de armas (Última Palabra/Predestinador), el intercambio "¿Eres Dredgen?" y Luz parcial de Kyle a mitad de combate; la pregunta de Kyle a Elsie sobre "convertirse en Oryx" se afina hacia confundir proteger con someter. Cap. 14 — Hornet ya no habla del Acorazado como si lo recordara en persona (ahora es simulación/registros de Eris), se suma la reacción de Carina/Hornet a los restos de la Batalla de Saturno, y una escena nueva (nave Cabal estrellada con mapa Ascendente parcial) siembra a Eirene como objetivo estratégico de Oryx sin nombrar "Lubrae". Además: una línea de `05_The_Dreadnaught_Key.md` que adelantaba la trama romántica de Elsie ("la persona que ella amaba") se corrigió a un registro más analítico, acorde a su ficha de voz. Detalle completo en `log.md`, sesión "2026-08-10 (e)". EPUB reconstruido y verificado limpio (sin wikilinks ni bloques de cierre colados).
- **Sesión previa:** 2026-08-10 (continuación, terminada la repasada de King's Fall de la otra sesión activa) — **Escena puente nueva en Part 02, "The Ascending Regicide" (Cap. 25), a pedido del autor.** Dramatiza por primera vez cómo se reunió la Primera Escuadra completa antes de entrar a King's Fall: Kyle (con Joe, ya emparejado con él por el Frente 2) recoge a Kevin+Resner en Marte y a Tiago+Angie en la Luna, cada uno todavía en su propio frente de la Guerra de los Poseídos; los seis juntos por primera vez en semanas; consejo de guerra con Eris — Osiris presente solo como **Echo** (fragmento de su consciencia, concepto de canon de Curse of Osiris usado aquí por primera vez, nunca en persona con Kyle, preservando intacto el hito futuro "el mito y el hombre") — que fija equipo, logística y motivo para la incursión final, con Mara ausente (Eris y el Echo comparten un silencio no explicado que Ghost nota) y sin nombrar la frase "regicidio ascendente" en la prosa (reservada al título). Cierra con la línea de Kyle pedida verbatim por el autor: "Bien. Es hora... de la caída del rey." Escrita primero como borrador en `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_KingsFall_00_AntesDeEntrar.md` (2026-08-09) para cerrar un hueco que `09_Roadmaps/Plan_TakenKing_Parte2_GuerraDeLosPoseidos.md` dejaba abierto a propósito; integrada al libro una vez que la otra sesión activa (repasada de King's Fall, ver entrada anterior) cerró y estabilizó la numeración de Part 03. Cascada de +1 aplicada a Part 03 (27-32), Part 04 (33-34) y Part 05 (35-37) — libro completo sube de 36 a 37 capítulos. Se agregó también `12_Craft_Policies/voice/osiris.md` (ficha de voz nueva) durante esta misma sesión, usada para calibrar el diálogo del Echo.
- **2026-08-10** — Repasada pesada de King's Fall (Part 03 completa): capítulo nuevo *Everything That Isn't Solid Ground* cierra el hueco geográfico entre la entrada al Acorazado y el Santuario (Part 03 de 5 a 6 capítulos); mecánica de revivir-en-oscuridad (canalizar la Luz de los demás a través del Ghost del caído) en tres momentos crecientes: Resner, Angie, Kevin. Restricciones respetadas: nadie de la Primera Escuadra muere en Part 03; lo ya auditado por Codex el 2026-08-09 no se tocó.
- **2026-08-08 (continuación)** — Pase de ajustes del autor sobre Part 01, Caps. 11-13, ya con Book 02 terminado: nueva escena de confrontación colectiva en la evacuación del Refugio (Cap. 11); Eris guía el primer Fragmento Calcificado, batería como ciudadela de tres alas, nave de rescate pasa a ser Duality, escena privada Kyle/Ghost sobre el porche (Cap. 12); recorrido ambiental completo del descenso al Hellmouth (Cap. 13). Patrón detectado: personajes sabiendo/nombrando algo antes de tiempo (corregido de nuevo, con más ejemplos, en la sesión del 2026-08-10 (e) — ver arriba).
- **2026-08-08** — Reubicación de Jaden a Book 03 (`11_Books/Book_03_Evolution_Of_Ashes/`, tesis space western + filosofía samurái) y Book 02 recortado de 38 a 35 capítulos, con Part 05 reescrita para POV estricto de Carina. Antes de eso, en la misma tarde: Book 02 — The King of Shapes quedó TERMINADO por primera vez, 17 capítulos en una sola sesión extendida.

## Historial de sesiones (condensado)

*Detalle completo de cada sesión en `log.md` — aquí solo quedan hitos de una línea, de más reciente a más antigua. Podado el 2026-08-04 (el archivo superaba el límite de 150k caracteres).*

- **2026-08-04** — Cap. 8 de Book 02: escenografía de la cabaña, apariencia física de Kyle y Elsie, llegada de Elsie reencuadrada (pretexto de trabajo de campo); beat de las armas con Banshee reescrito de mantenimiento a nombrado en vivo (Predestinador, Martillo Negro, Gjallarhorn).
- **2026-08-03** — Corrección de ritmo en el Cap. 12 de Book 02: el caballo y la limpieza de armas trasladados al Cap. 8, con una escena nueva de Banshee-44; sesión de reestructuración quirúrgica, sin prosa nueva salvo esa escena.
- **2026-08-02** — Sesión más productiva registrada hasta la fecha: Book 02 Part 01 queda COMPLETA (11/11 caps + interludio); diseño de Eirene/Lubrae y personaje nuevo Avarra; origen de "Chispitas"/"Pistolera"; auditoría de Codex resuelta (4 hallazgos); Fase I de Fragmentos Calcificados expandida a prosa (21 nuevos).
- **2026-08-01** — Diseño puro, cero prosa: Aspect of Glass fijada como llave del Acorazado; Part 01 crece a 10→11 capítulos; el caballo (elemento nuevo, arco a Rise of Iron); Elsie sustituye a Ana Bray en la crisis de SIVA.
- **2026-07-31** — Cap. 9 (Phobos) pulido en cascada (9 ajustes); Cap. 11 reestructurado y renombrado "What the Ledger Kept" — el anillo de Lena se muda a escena futura.
- **2026-07-29/30** — Cap. 6 reescrito completo (nuevo conflicto: Legionario de Calus/Catabasis); horizonte de némesis Carina/Savathûn consolidado (5 etapas); Cap. 7 expandido; interludio de la Batalla de Saturno; naves de la escuadra fijadas.
- **2026-07-26/27** — Prólogo de Book 02 cerrado (7/7); Part 01 arrancada (caps. globales 8-11); numeración de capítulos vuelta global y continua para todo el libro.
- **2026-07-25/26** — Arquitectura completa de los 14 libros de la saga fijada (Book 00-13); Prólogo reestructurado en 7 capítulos independientes; Caps. 1-3 escritos y auditados.
- **2026-07-21** — Retratamiento sensorial del Cluster 4 de Taken King Parte 1 con referencias visuales; corrección de especie de Ecthar (Cabal→Colmena); escena nueva Ghost↔Hornet.
- **2026-07-20** — Matriz de mazmorras como pruebas personales triada completa (11 filas, raid team de Kyle) — infraestructura de roadmap, cero prosa.
- **2026-07-19** — Sesión más extensa hasta esa fecha: retratamiento de terror en los 4 clusters de Taken King Parte 1; Guerra de los Poseídos (Parte 2) diseñada y escrita completa (6 frentes); King's Fall retratado; Aftermath completo — Taken King queda cerrado de punta a punta.
- **2026-07-18** — Kepler/Malok fijado (Decisión 3 de Plan_Jaden_Atheena_Origen); horizonte Carina/Savathûn auditado por Codex (doble protagonista propuesto para Witch Queen, sin triar); Plan_RiseOfIron_Nemo.md fijado, ficha de Nemo creada.
- **2026-07-15** — `Carina_Lena.md` (documento rector de la relación) creado; triage de Age I ("tres caras del nacimiento moral de Kyle"); triage del hueco P0 de Shadowkeep.
- **2026-07-14** — Auditoría de Codex sobre Taken King Parte 1 resuelta; rol de Editor de ChatGPT repartido entre Codex y Claude Code; primer retratamiento de terror (Phobos).
- **2026-07-13/14** — Carpeta propia para Carina/Lena; decanonización del origen Kyle-Carina en Wrath of the Machine; Parte 1 completa de Taken King escrita (23 escenas, 4 clusters).
- **2026-07-12** — Riesgos del rediseño de Parte 1 de Final Shape resueltos; arranque de la redacción del Hilo A; Codex ampliado a incubadora de ideas.
- **2026-07-11** — Retratamiento completo de la apertura de Parte 1 de Final Shape; orígenes propios de Carina (Lena) y Jaden (Suetake) — 17 escenas nuevas.
- **2026-07-08** — Cinco escenas nuevas cerrando el arco romántico lento de Kyle/Elsie y el arco de comprensión de Sai.
- **2026-07-05** — Los Juegos de los Guardianes y el Solsticio escritos (calendario anual de la familia); beat retroactivo "primero a ella" en Age I.
- **2026-07-04** — La Familia Elegida / Torneo de los Velocistas diseñado; calendario anual fechado mes a mes; Torneo IV completo escrito (11 escenas, clasificación→final).
- **2026-07-03** — La Huida de Salvation's Edge (dos escenas); apariencias de Elsie y Kyle fijadas en ficha; 3 inconsistencias de imágenes detectadas (sin resolver).
- **2026-06-28** — Timeline Archive completo: `EstaVezAlguienCruza` (Ghost nueva: Ember).
- **2026-06-27** — Pipeline multi-agente formalizado + Git saneado + Revisión ChatGPT #1; sistema de nombres de Sai; nacimiento del Círculo del Dolor.
- **2026-06-24** — La semana de Sai completada (arco del duelo); Famke (Ahamkara) creada, ficha provisional.
- **2026-06-20 (heredado)** — pendiente: prosa de caps. 34-39 de Lightfall; escena `Guardian_Ghost_Lightfall_Destrozado`.
