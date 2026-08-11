# Arquitectura Editorial Multiagente — Documento Rector

> **No es canon narrativo.** Documento de proceso, vive en `99_Reference/` junto con
> `Development_Workflow.md`, `Codex_Brief.md` y `Agent_Notes/README.md`. Nace de
> `99_Reference/Agent_Notes/victor-agents/Arquitectura Editorial Multiagente.md` (nota de
> Víctor, 2026-08-10) — es la implementación real de esa propuesta, adaptada a la
> infraestructura que el vault ya tenía (`12_Craft_Policies/`, `Codex_Brief.md`,
> `Development_Workflow.md`, `Agent_Notes/`), no una segunda infraestructura paralela.

---

## Qué es esto y qué no es

`Development_Workflow.md` fija los **roles** (Víctor, Opus, Claude Code, Codex) y el
pipeline general de una idea. `Codex_Brief.md` fija **el brief completo de Codex**. Este
documento vive un nivel más abajo: es el mapa de **qué agente o modo específico** resuelve
qué síntoma concreto de prosa, y cómo se conectan entre sí sin pisarse. No repite el
contenido de esos documentos — los enlaza.

> **Claude Code transforma. Codex audita. Víctor decide canon y dirección narrativa.**

Esta frase ya gobernaba el vault antes de este documento (ver `Development_Workflow.md`,
`Codex_Brief.md`). Aquí se operacionaliza en agentes y modos nombrados.

---

## 0. Regla de no duplicación

Nunca crear un agente de Claude y un modo de Codex con la misma responsabilidad. La
división general:

> **Codex encuentra. Claude resuelve.**

```
Codex (read-only, salvo excepción ya fijada en Codex_Brief.md §11_Books)
  → produce hallazgo en Agent_Notes/codex/
Víctor
  → acepta / modifica / rechaza
Claude Code
  → integra la corrección aprobada
```

Ningún agente transformativo (Claude) decide canon. Ningún modo de auditoría (Codex)
reescribe silenciosamente un capítulo.

---

## 1. Agentes de Claude Code

Todos viven en `.claude/agents/`, consumen `12_Craft_Policies/` y demás fuentes de verdad
ya existentes (ver §3), y devuelven por defecto texto — no editan el archivo original
salvo que se pida explícitamente.

| Agente | Tipo | Pregunta / función central | Estado |
|---|---|---|---|
| [`dialogue-vitalizer`](../.claude/agents/dialogue-vitalizer.md) | Transformativo | Evitar diálogo sin dueño — `Character × Listener × Moment` | **Implementado** (2026-08-10, auditado contra esta arquitectura) |
| [`scene-doctor`](../.claude/agents/scene-doctor.md) | Diagnóstico + transformación estructural local | ¿Esta escena cambia algo? | **Implementado** |
| [`subtext-editor`](../.claude/agents/subtext-editor.md) | Transformativo | ¿Narración y diálogo explican lo mismo? | **Implementado** |
| [`prose-degenericizer`](../.claude/agents/prose-degenericizer.md) | Transformativo | ¿La narración pertenece al POV y a la escena, o podría estar en cualquier novela? | **Implementado** |
| `exposition-surgeon` | Transformativo | Poner cada pieza de lore en la forma narrativa correcta | Fase 2 — no construido |
| `relationship-editor` | Transformativo, conservador | ¿Esta relación ya se ganó este momento? | Fase 2 — no construido |
| `action-choreographer` | Transformativo | Legibilidad y causalidad en combate/persecución/infiltración | Fase 2 — no construido |
| `raid-narrativizer` | Especializado | Gameplay → causalidad diegética/paracausal | Fase 3 — posible Skill de `action-choreographer` en vez de agente propio |
| `chapter-closer` | Ligero, opcional | Apertura/cierre de capítulo | Fase 3 — opcional, baja prioridad |

Fase 2 y 3 quedan documentadas aquí como destino, no como trabajo pendiente urgente — ver
§9 "Agents are symptom-driven". No se construyen hasta que un síntoma real las requiera.

---

## 2. Modos de auditoría de Codex

Codex sigue siendo **read-only** fuera de la excepción ya fijada en `Codex_Brief.md`
("Escritura directa permitida en `11_Books/`"). Sus modos no son subagentes técnicos
separados — son secciones/checklists dentro de `Codex_Brief.md`, porque Codex es un
agente distinto que lee su propio brief completo, no el mecanismo `.claude/agents/` de
Claude Code.

| Modo | Función central | Ubicación |
|---|---|---|
| `continuity-auditor` | Fechas, viajes, ubicaciones, heridas, objetos, muertes, resurrecciones, orden de acontecimientos | Ya cubierto — `Codex_Brief.md`, "Checklist de auditoría" + "Checklist editorial" #1 |
| `knowledge-state-auditor` | ¿Quién sabe qué, cuándo y por qué? | **Nuevo** — `Codex_Brief.md`, "Modos de auditoría especializados" |
| `repetition-hunter` | Repetición superficial (palabras/gestos) y, sobre todo, semántica (misma emoción/descubrimiento/beat repetido sin información nueva) | **Nuevo** — `Codex_Brief.md`, "Modos de auditoría especializados" |
| `character-arc-auditor` | ¿Este personaje ya se ganó psicológicamente esta conducta? | Fase 2 — no construido |
| `setup-payoff-tracker` | Setup sin payoff, payoff sin setup, callback roto — apoyado en `12_Craft_Policies/revelations/` | Fase 2 — no construido |
| `pacing-auditor` | Distribución de acción/conversación/introspección a escala de capítulo/Part/libro | Fase 2 — no construido |
| `canon-divergence-auditor` | Clasificar divergencias de Destiny canon (consistente / intencional / documentada / posible sin documentar / contradicción real) | Fase 3 — no construido |
| `theme-drift-auditor` | ¿Las decisiones del libro siguen dramatizando la tesis prometida? — baja frecuencia, por Part/libro | Fase 3 — no construido |

---

## 3. Fuente de verdad editorial (precedencia)

Ningún agente inventa su propia biblia interna. Orden de precedencia — ya existente en el
vault, aquí solo consolidado para que todo agente transformativo lo consulte en el mismo
orden:

```
decisión explícita actual de Víctor
        ↓
00_Biblia/
        ↓
00_Book_Map.md del libro activo
        ↓
09_Roadmaps/ confirmados (Plan_*.md)
        ↓
12_Craft_Policies/  (revelations/ > milestones/ > voice/ > dialogue_rules/ + staging_rules/)
        ↓
02_Characters/
        ↓
08_Core_Relationships/
        ↓
01_Timeline/
        ↓
escenas/capítulos ya canonizados
        ↓
material de referencia (99_Reference/)
```

Si un documento del vault ya fija una precedencia más específica para su propio dominio
(ej. `12_Craft_Policies/README.md` § Precedencia), esa precedencia local manda dentro de
ese dominio.

---

## 4. Pipelines

### 4.1 Idea nueva

Ya documentado completo en `Development_Workflow.md` § Secuencia — no se duplica aquí.
Para preguntas de canon de Destiny o que requieren explorar varias direcciones antes de
decidir, esta etapa se apoya en dos roles de Codex, formalizados 2026-08-10:
`Codex_Canon_Researcher.md` (¿qué sabemos?) y `Codex_Brainstorming_Agent.md` (¿qué
podríamos hacer?) — ambos anteceden a esta arquitectura editorial, no forman parte de
ella: la sala editorial (este documento) transforma y audita prosa ya escrita; esos dos
roles exploran antes de que exista prosa.

### 4.2 Escena nueva

```
Roadmap confirmado / beat aprobado
        ↓
Claude Code — construcción de la escena
        ↓
diagnose: ¿qué síntoma concreto tiene, si tiene alguno?
        ↓
especialista(s) elegido(s) según síntoma (§9 — nunca la cascada completa por defecto)
        ↓
ESCENA
```

### 4.3 Capítulo terminado

```
CAPÍTULO TERMINADO
        ↓
Codex — continuity + knowledge-state + repetition (Fase 1 ya disponible)
        ↓
hallazgos → 99_Reference/Agent_Notes/codex/
        ↓
VÍCTOR TRIAGE
        ↓
Claude Code integra los hallazgos ACCEPTED
```

Pacing puede correrse cuando sea útil una vez implementado (Fase 2).

### 4.4 Part / Libro terminados

Mismo patrón que 4.3, escalado. `setup/payoff`, `character-arc`, `canon-divergence` y
`theme-drift` son el destino final de este pipeline a nivel Part/libro, pero **no están
implementados todavía** (Fase 2/3) — hasta entonces, un cierre de Part o libro se apoya
solo en los tres modos de Fase 1 más la Checklist editorial ya existente de
`Codex_Brief.md`.

---

## 5. Handoffs y trazabilidad

Formato ya fijado — no se duplica: `99_Reference/Agent_Notes/README.md`. Todo hallazgo de
Codex sigue ese esqueleto (`Hallazgo / Por qué / Sugerencia / Severidad / ¿Canon
bloqueado?`) y todo cierre lo marca quien resuelve, citando qué archivo/commit lo
resolvió.

---

## 6. Triage síntoma → especialista (router editorial diferido)

Sección 33 de la nota original propone un agente `editorial-router` cuyo único trabajo
sería diagnosticar y recomendar especialista, sin editar. Se decide **no construirlo
todavía** — sería un salto adicional sin beneficio probado mientras la tabla siguiente
sea suficiente para que quien conduce la sesión (Claude Code o Víctor) elija a mano:

| Síntoma detectado | Especialista |
|---|---|
| Diálogo genérico, intercambiable, hedging editorial | `dialogue-vitalizer` |
| La escena no cambia nada / objetivo o giro confuso | `scene-doctor` |
| Narración y diálogo explican exactamente lo mismo | `subtext-editor` |
| Prosa con muletillas de IA, metáfora intercambiable, falsa profundidad | `prose-degenericizer` |
| Posible fuga de conocimiento (personaje sabe algo que no debería, todavía) | Codex — `knowledge-state-auditor` |
| Posible contradicción fáctica/cronológica | Codex — `continuity-auditor` |
| Beat/emoción/lore repetido sin información nueva | Codex — `repetition-hunter` |
| Sin síntoma detectable | No ejecutar nada (§9) |

Si este triage se vuelve mecánico y se repite sesión tras sesión de forma idéntica,
**entonces** vale la pena promoverlo a agente real. No antes — construirlo ahora sería
resolver un problema que todavía no existe.

---

## 7. Qué nunca se automatiza

Ningún agente decide unilateralmente:

- muerte de personaje;
- romance;
- separación;
- canon nuevo;
- cosmología;
- retcon;
- identidad;
- motivación central;
- outcome de un arco;
- solución de misterio;
- cambio de POV estructural;
- cambio de `00_Book_Map.md`;
- eliminación de setup importante.

Eso requiere decisión de Víctor, igual que ya fija `Codex_Brief.md` y
`Development_Workflow.md` para el canon en general.

---

## 8. Principios universales para todo agente transformativo

Cualquier agente `.claude/agents/` de tipo transformativo, existente o futuro, respeta:

> **Diagnose before rewriting.** La pregunta no es "¿puedo mejorarlo?", es "¿existe un
> problema concreto que justifique intervenir?"

> **Do not fix what already has a voice.**

> **Character before eloquence. Specificity before prettiness. Causality before
> spectacle.**

> **Subtext before explanation — solo cuando el personaje tiene razón para ocultarlo.**

> **Do not confuse clarity with overexplanation. Do not confuse restraint with vagueness.
> Do not confuse complexity with depth.**

> **Do not make everyone witty. Do not make everyone emotionally articulate. Do not make
> every paragraph profound.**

> **Do not solve what the story deliberately leaves unresolved.**

> **Agents are symptom-driven, not mandatory gates.** Si una escena tiene diálogo
> excelente, no correr `dialogue-vitalizer`. Si no hay acción compleja, no correr
> `action-choreographer`. Si un arco recién empieza, un audit de setup/payoff
> probablemente no aporta nada todavía. Si solo se corrigieron tres frases, no disparar
> una auditoría completa de libro.

---

## 9. Evitar cascada de sobreedición

Nunca encadenar automáticamente `scene-doctor → dialogue-vitalizer → subtext-editor →
relationship-editor → prose-degenericizer → exposition-surgeon → chapter-closer` sobre
cada escena — homogeniza la voz. El patrón correcto:

```
diagnose → select specialist → edit → stop
```

---

## 10. Prueba de separación

La arquitectura falla si Codex y Claude Code producen ambos algo del tipo *"encontré esta
contradicción y ya reescribí el capítulo."* El comportamiento correcto:

**Codex:** Encontré esta contradicción. Aquí está la evidencia. Aquí está el riesgo. Aquí
hay una dirección posible.

**Claude Code**, tras aprobación de Víctor: Integré la resolución aceptada preservando
voz, continuidad y escena.

---

## 11. Context budget

Cada especialista lee solo lo necesario para el síntoma que investiga — no cargar las 84
fichas de `02_Characters/` para una escena de tres personas. Orden mínimo: hablante(s) →
relación relevante → libro/Part activo → hito relevante → revelación relevante →
contexto local de la escena. Escalar a búsquedas mayores solo cuando aparezca una
contradicción real.

---

## Estado de implementación (2026-08-10)

**Fase 1 — completa:**
- Claude Code: `dialogue-vitalizer`, `scene-doctor`, `subtext-editor`, `prose-degenericizer`.
- Codex: `continuity-auditor` (ya existía), `knowledge-state-auditor` y
  `repetition-hunter` (nuevos, ver `Codex_Brief.md`).

**Fase 2 / Fase 3 — diferidas.** No construir hasta que un síntoma real las requiera (ver
§9). Este documento es el punto donde se registraría su implementación cuando llegue el
momento.

---

*Conecta con: [[AGENTS.md]], [[99_Reference/Development_Workflow]], [[99_Reference/Codex_Brief]], [[99_Reference/Agent_Notes/README]], [[12_Craft_Policies/README]], [[99_Reference/Codex_Canon_Researcher]], [[99_Reference/Codex_Brainstorming_Agent]]*
