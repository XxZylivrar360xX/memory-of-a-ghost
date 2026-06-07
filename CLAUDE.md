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
│   └── Dialogue_Guardian_Elsie/  # Scenes developing the relationship as a character
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
