# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

*Destiny: Renewed Fate* is a philosophical fan fiction saga reinterpreting the Destiny 2 universe. It is managed as an **Obsidian vault** — all files are Markdown, interlinked with Obsidian's `[[WikiLink]]` syntax. There are no build commands, tests, or code to run.

Primary language for narrative and character documents: **Spanish**. Document titles and folder names are in English.

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
│   └── Dialogue_Ghost/       # Scenes where Ghost's arc is primary (closure + coda)
├── 06_Timeline_Archives/     # Elsie's alternate timeline memories — canon support material
│   ├── Dark_Futures/         # Timelines where humanity lost — Elsie's fears
│   ├── Lost_Guardians/       # Versions of Kyle that failed, left, or fell — explains her attachment
│   ├── Bray_Legacies/        # Ana, Rasputin, Clovis in alternate paths — Elsie's family wounds
│   ├── Personal_Memories/    # Small, intimate moments that only changed Elsie
│   └── Alternate_Allies/     # People who existed in other realities and left a mark on her
├── 07_Unsorted_Ideas/        # Raw ideas, seeds, fragments
├── 08_Core_Relationships/    # Deep-dive files on the three central relationships
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

## Estado del vault

- **Saga:** *Destiny: Renewed Fate* — 60 capítulos (Prólogo + Ages I–XVIII + Epílogo); Lightfall expandido a 7 capítulos (33–39), todo lo posterior corrido +4
- **Capítulos escritos:** 11 de 60 — Prólogo ×5 · Age I ×3 · Age XI ×1 (Cap 32) · Age XII ×1 (Cap 33, inicio) · Epílogo ×1 · (Lightfall caps 34–39 en esquema; resto: stubs)
- **Escenas escritas:** 177 — Dialogue_Guardian ×87 · Dialogue_Elsie ×25 · Dialogue_Guardian_Elsie ×45 · Dialogue_Ghost ×4 · Dialogue_Sai ×10 (7 de la semana del duelo + 1 origen Season of the Lost + 2 origen de los nombres) · RenacimientosGuardianes ×6
- **Timeline Archives:** 19 archivos — 4 raíz · Lost_Guardians ×6 · Bray_Legacies ×2 · Personal_Memories ×5 · Alternate_Allies ×1 · Dark_Futures ×1
- **Conceptos:** 44 archivos en `04_Concepts/`
- **Personajes:** 69 archivos en `02_Characters/`
- **Relaciones principales:** 5 archivos en `08_Core_Relationships/`
- **Última sesión:** 2026-06-28 — **Timeline Archive completo: EstaVezAlguienCruza.** Desarrollo íntegro de la idea desde borrador en `07_Unsorted_Ideas` hasta archivo final en `Personal_Memories`. 6 secciones en prosa: (I) despertar en el Cosmódromo — primer encuentro Kyle/Elsie-Roja, nacimiento de Ember y los nombres de frontera "Roja"/"Extraño"; (II) la Edad Oscura — cuatro momentos que contextualizan la época y el duelo congelado de Kyle; (III) ZME — el refugio, el niño Tomás y Gris (oso sin oreja), "Entremos sin armas", muerte de Kyle ("Sujétalo"); (IV) el legado — Roja continúa la regla sin bandera ni nombre; (V) cierre del loop — Tomás adulto riendo sin poner el ojo en la salida; (VI) lo que llegó — los impactos que transfiere a la Elsie principal. Ghost nueva: **Ember** (femenina, fría y cautelosa, se presenta a ambos, grieta en "No te llamaba nada"). Cicatriz fundacional de la maternidad Elsie→Sai: *proteger no es poseer*. **Pendientes heredados:** reescritura de `ElLoboMasJoven`; threading "norte"/"lobito"; cimientos Kyle↔Sai doméstico y Sai↔Ghost; fichas Amanda_Holiday, Glint, Famke; prosa caps 34–39 Lightfall; escena `Guardian_Ghost_Lightfall_Destrozado`. — *(Heredado 2026-06-27: pipeline multi-agente + Git + Revisión ChatGPT #1; sistema de nombres Sai; Círculo del Dolor.)*
- **Última sesión:** 2026-06-27 — **Pipeline multi-agente + Git + Revisión ChatGPT #1.** Sesión extendida 26-27/jun: (1) cimiento del arco de Sai en Season of the Lost (`LaQueNoVaSola`); (2) apariencia de Sai fijada en ficha (piel lila-rosa, ojos verde-café sin luz Awoken, mechones decolorados) + faceclaim Ana de Armas (`99_Reference/Faceclaims.md`); (3) diferenciador físico sembrado en `LoQueSostiene`; (4) nacimiento del Círculo del Dolor (`Dark_Futures/ElCirculoDelDolor_ElNacimiento.md`, primer archivo de la carpeta) + reconciliación de `Alternate_Allies/Sai_ElCirculoDelDolor`; (5) pipeline multi-agente formalizado (`99_Reference/Development_Workflow.md` + `ChatGPT_Editor_Brief.md`); (6) git saneado (`.gitignore` UTF-8, `workspace.json` desrastreado, `.git` reubicado a `C:` vía `--separate-git-dir`); (7) Paquete de Revisión #1 con ChatGPT (9 hallazgos, 3 aplicados A/B/C, commit `17ee986` en `develop`). **Pendiente #1:** reescritura de `ElLoboMasJoven` con nuevo encuadre (Saladin/Caiatl, "lobo joven"→flash-forward "Los jueves"). Parentesco hecho implícito en `Sai_Petra` (acción, no etiqueta); edad aparente de Sai 16→19 (blindar el romance con Crow). **Sistema de nombres** (ficha de Sai · "Los nombres"): nombre real **Saiidris Thelis**; Sai↔Elsie "norte"/"Elizabeth" (Elsie da su nombre real a dos: esposo e hija), Sai↔Kyle "lobito"/"papá" (Kyle = Señor de Hierro más joven). Nueva escena fundacional **`Sai_Crow_SeasonLost_LoQueNoTuveQuePerdonar`** (origen de Sai+Crow en los Jardines de Esila). **Hecho (cont. 2026-06-25):** escrito el origen de los ritos de nombre, en **dos escenas hermanas** (separadas a petición del autor para ajuste independiente): `Sai_Guardian_WitchQueen_ElLoboMasJoven` (nace "lobito"/"niña") y `Sai_Elsie_WitchQueen_LoQueNoSeArranca` (nacen "norte"/"norte chiquito"/"Saiidris"/"Elizabeth"; eje "dado vs. arrancado"). **Pendiente:** threading "norte"/"lobito" en prosa; cimientos Kyle↔Sai doméstico y Sai↔Ghost; enlazar la escena de Crow en ficha de Crow. Detalle en `log.md`. — *(Heredado 2026-06-24: la semana de Sai; Famke provisional pendiente de expansión; fichas Amanda_Holiday y Glint.)* — **[entrada previa]** 2026-06-24: **La semana de Sai completada** (arco del duelo de Sai por Elsie, reverso de geometría opuesta a la semana del pésame de Kyle). Nueva carpeta-arco **`Dialogue_Sai`** registrada en INDEX (7 escenas; lógica de carpetas actualizada). Escritos los días 4-6 — `Sai_Famke…LoQueElDeseoNoDevuelve` (Famke ofrece traer a Elsie; rechazada), `Sai_Crow…LaPuertaQueSigueAbierta` (amor joven; el matiz Cayde), `Sai_Elsie…LoQueSeDaSinPedirlo` ("el sueño del don") — más el **capstone POV Sai** `Sai_Guardian…LoQueTrajeDeVuelta` (reverso interior de `La Hija Que Elegimos`, complementario no sustituto). Nueva criatura: **Famke**, Ahamkara hija de Riven (ficha provisional). Canon: el regreso de Cayde en la Forma Final como **deseo implícito de Crow** (Pale Heart) → distinción "quedárselo vs. soltarlo bien". Pendiente: **expandir ficha de Famke**; fichas de `Amanda_Holiday` y `Glint`. — *(Heredado de 2026-06-20, aún pendiente: prosa de caps 34–39 de Lightfall; escena `Guardian_Ghost_Lightfall_Destrozado`.)*
