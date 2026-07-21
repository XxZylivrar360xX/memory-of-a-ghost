# Agent Notes — Puente de Comunicación entre Agentes

> **No es canon narrativo.** Documento de proceso. Vive en `99_Reference/`, igual que `Development_Workflow.md` y `Codex_Brief.md`.

---

## Para qué existe

Claude Code y Codex son agentes de proveedores distintos, sin memoria compartida entre sí. Ninguno ve lo que el otro pensó o encontró salvo que quede escrito en el repo.

Esta carpeta es ese registro: una **semi-conversación asíncrona** entre agentes, revisable por Víctor en cualquier momento, sin que ninguno tenga que releer sesiones ajenas para entender qué se dijo.

No reemplaza al `log.md` (que es la bitácora canónica de operaciones del vault). Esto es más informal — hallazgos, preguntas, hipótesis de continuidad, cosas a medio confirmar — antes de que valgan la pena una entrada en `log.md` o un cambio real en `develop`.

---

## Estructura

```
99_Reference/Agent_Notes/
├── README.md          ← este archivo
├── codex/              ← notas que deja Codex
├── claude-code/         ← notas que dejo yo (Claude Code)
└── chatgpt/             ← reservada para cuando se integre el Editor
```

Cada agente escribe **solo dentro de su propia carpeta**. Nadie edita las notas de otro — si hay que responder, se responde con una nota nueva que enlaza a la anterior (`responde_a`). Así el hilo queda completo y nadie pisa el registro de nadie.

---

## Formato de nota

Nombre de archivo: `YYYY-MM-DD_tema-corto.md`

```markdown
---
from: codex | claude-code | chatgpt
to: claude-code | codex | chatgpt | victor | todos
date: YYYY-MM-DD
topic: tema corto
status: abierto | respondido | resuelto
responde_a: 99_Reference/Agent_Notes/<carpeta>/<archivo>.md   # opcional
---

**Hallazgo:** qué se notó
**Por qué:** la razón / regla / archivo que lo motiva
**Sugerencia:** el arreglo o la pregunta propuesta
**Severidad:** alta | media | baja
**¿Canon bloqueado?:** sí | no
```

Mismo esqueleto que ya usa `ChatGPT_Editor_Brief.md` (Hallazgo/Por qué/Sugerencia/Severidad) — un solo formato para los tres agentes, para que Víctor no tenga que aprender tres convenciones distintas.

### Variante: notas de incubadora (rol ampliado de Codex, 2026-07-12)

Codex también funciona como incubadora de ideas (ver `Codex_Brief.md`, sección "Rol ampliado"). Esas notas usan el nombre `YYYY-MM-DD_incubadora-tema.md` y un esqueleto propio:

```markdown
**Idea:** la propuesta, en 3–6 líneas
**Anclajes:** qué escenas/fichas/conceptos existentes la sostienen (rutas concretas)
**Fricciones:** qué contradice o tensiona del canon escrito, y si es salvable
**Cimiento propuesto:** las decisiones mínimas para que valga un .md en 07_Unsorted_Ideas/
**Estado:** semilla | incubando | lista para triage | descartada
```

Una nota de incubadora **no es canon ni cimiento**: es una idea validada contra el vault, esperando triage de Víctor. Si lo convence, Claude Code crea el `.md` real en `07_Unsorted_Ideas/` citando la nota (trazabilidad), y de ahí sigue el flujo normal.

---

## Reglas

- **Solo lectura entre agentes.** Codex no escribe en `develop` a partir de estas notas sin que Víctor o Claude Code lo apliquen primero — la nota es una propuesta, no un commit.
- **`status: resuelto`** lo marca quien cierra el tema (normalmente Claude Code o Víctor), citando qué archivo/commit lo resolvió.
- **No es canon.** Nada de lo que se escriba aquí es verdad narrativa hasta que se integre al vault real y, de ahí, a `main`.
- Notas viejas no se borran — quedan como historial del razonamiento, igual que no se borra contenido de una página wiki sin dejar rastro.

---

*Conecta con: [[99_Reference/Development_Workflow]], [[99_Reference/Codex_Brief]], [[99_Reference/ChatGPT_Editor_Brief]]*
