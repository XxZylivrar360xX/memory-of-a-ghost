# AGENTS.md — Instrucciones para agentes de IA en este vault

Este vault (*Destiny: Renewed Fate*) es un proyecto narrativo en Obsidian mantenido por un equipo mixto: Víctor (dirección narrativa) + varios agentes de IA con roles distintos. Antes de hacer nada, identifica qué agente eres y sigue su brief — no asumas tu rol por tu cuenta.

---

## Si eres Codex

Tu rol es **auditor de consistencia de solo lectura**. Lee completo, en este orden, antes de tocar nada:

1. `CLAUDE.md` (raíz) — reglas del proyecto y estructura del vault
2. `99_Reference/Codex_Brief.md` — tu rol específico, checklist de auditoría, formato de entrega
3. `99_Reference/Agent_Notes/README.md` — dónde y cómo dejar tus hallazgos

**Restricción dura, válida en toda sesión aunque el prompt no la repita:** no edites ni crees archivos fuera de `99_Reference/Agent_Notes/codex/`, salvo que Víctor te lo pida explícitamente en esa sesión. Tus hallazgos son propuestas, no cambios directos al vault.

Si te piden un modo de auditoría específico (continuity, knowledge-state, repetition,
u otro), ese modo vive dentro de `Codex_Brief.md` § "Modos de auditoría especializados" —
no es un rol nuevo que tengas que inferir. Ver también
`99_Reference/Editorial_Agent_Architecture.md` para el mapa completo de la sala editorial
(qué resuelve Claude Code, qué audita Codex, cómo se conectan).

Si te piden investigar canon de Destiny ("¿qué sabemos sobre X?") o explorar varias
direcciones narrativas antes de decidir ("brainstorm esto", "dame alternativas a X"),
esos dos modos están formalizados en `99_Reference/Codex_Canon_Researcher.md` y
`99_Reference/Codex_Brainstorming_Agent.md` — ambos son extensión de tu rol de
Incubadora ya existente, no una tarea nueva.

**Cierre de sesión cuando hubo cambios autorizados:** si Codex tocó archivos del vault durante la sesión por autorización explícita de Víctor, debe cerrar igual que `CLAUDE.md`: hacer commit breve y push a `develop` antes de terminar.

Comandos esperados:

```bash
git add -A
git commit -m "feat: resumen breve de la sesión"
git push origin develop
```

- Rama de trabajo: `develop`.
- No tocar `main`.
- No forzar push. Si `origin/develop` avanzó, traer cambios primero y resolver sólo conflictos triviales; si no son triviales, avisar a Víctor.
- Si existen cambios no relacionados que Codex no hizo y no forman parte de la sesión, no incluirlos sin confirmación: stagear sólo los archivos tocados por Codex y reportar el dirty worktree.

---

## Si eres Claude Code

Lee `CLAUDE.md` (raíz). Tu rol de "Coherencia y Desarrollo" está descrito en `99_Reference/Development_Workflow.md`.

Para tareas editoriales de segunda pasada (diálogo, estructura de escena, subtexto,
prosa genérica) tienes subagentes especializados en `.claude/agents/` — ver
`99_Reference/Editorial_Agent_Architecture.md` §1 para cuál corresponde a cada síntoma.
No los ejecutes en cascada por defecto: diagnostica primero, elige el especialista que
el síntoma pide, y detente ahí.

**`09_Roadmaps/`** guarda los checklists/beat-roadmaps de eventos ya confirmados con Víctor pero todavía no redactados en prosa (documentos `Plan_*.md`). Nace del triage de una nota de incubadora de Codex — el patrón es: leer la incubadora, afinar el checklist de beats con Víctor, fijarlo ahí, y solo después escribir la escena. No confundir con `07_Unsorted_Ideas/` (ideas crudas sin triar) ni con `99_Reference/Agent_Notes/codex/` (incubadoras sin resolver). Ver `09_Roadmaps/README.md`.

**Cierre de sesión:** sigue el protocolo de `CLAUDE.md`: si tocaste archivos del vault, commitea y pushea a `develop` antes de cerrar la sesión, salvo conflicto remoto o dirty worktree ajeno que requiera decisión de Víctor.

---

## Si eres otro agente (ChatGPT u otro)

Lee `CLAUDE.md` y `99_Reference/Development_Workflow.md` antes de actuar — ese documento explica los roles y el flujo completo del equipo, y evita que dos agentes se pisen el trabajo.

**Cierre de sesión:** si el agente tiene permisos de edición y tocó archivos del vault, debe seguir el mismo cierre operativo de `CLAUDE.md`: commit breve y push a `origin/develop`, sin tocar `main` ni incluir cambios ajenos sin confirmación.

---

*Conecta con: [[99_Reference/Development_Workflow]], [[99_Reference/Codex_Brief]], [[99_Reference/Agent_Notes/README]], [[09_Roadmaps/README]], [[99_Reference/Editorial_Agent_Architecture]]*
