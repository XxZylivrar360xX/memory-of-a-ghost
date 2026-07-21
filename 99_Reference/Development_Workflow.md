# Flujo de Desarrollo — Renewed Fate

> **No es canon narrativo.** Documento de proceso: cómo trabaja el equipo y cómo entran las ideas al universo. Vive en `99_Reference/`.

---

## Fuente de Verdad

El repositorio de GitHub es la versión oficial. El **canon vive en la rama `main`**. Google Drive es respaldo de las notas; **el `.git` vive en disco local (fuera de Drive)** para que git funcione confiable (Drive corrompe y bloquea las tripas de git).

---

## Ramas

- **`main` = canon publicado.** Todo lo que está aquí es verdad. Nunca se experimenta directo sobre `main`.
- **`develop` = trabajo en curso.** Ideas, escenas pendientes, refactors, ajustes de continuidad.
- **Regla de oro:** *nunca asumir que `develop` es canon.* Solo `main` es definitivo.
- **Merge a `main`:** lo decide Víctor, por **arco/lote aprobado y revisado** (no por cada commit). Mantiene `main` como canon curado.

---

## Roles

- **Víctor — Dirección Narrativa.** Autoridad final sobre el canon. Define la historia, escribe, aprueba, prioriza, **decide los merges**.
- **Claude Opus — Dirección Creativa.** Genera posibilidades: personajes, arcos, filosofías, civilizaciones, eventos. La pregunta: *¿qué más podría existir?*
- **Claude Code — Coherencia, Desarrollo y Pulso Dramático.** Trabaja directo en el repo (`develop`): estructura, enlaces/wikilinks, índices, cronologías, integración de propuestas, detección de inconsistencias. **Propone canon; no lo define.** **Rol ampliado (2026-07-14):** absorbe el pulso dramático que antes cubría el Editor de ChatGPT — ritmo, diálogos, redundancias, cuándo un silencio pesa más que una línea — como una relectura fría explícita antes de proponer el merge a Víctor, separada del momento de escribir la escena. *(Nota: en trabajo en vivo, Code y Opus se funden — Claude Code corre sobre Opus; la diferencia es el contexto/acceso al repo, no la inteligencia.)*
- **Codex — Auditoría de Consistencia + Incubadora de Ideas + Editorial de Postproducción.** Barrido estructural a escala de repo: enlaces rotos, índice desincronizado, cronologías contradictorias, duplicados. **Rol ampliado (2026-07-12):** también funciona como banca/incubadora de ideas — Víctor gesta escenas o conceptos con él y Codex los ancla contra el vault (qué los sostiene, qué contradicen, qué decisiones mínimas faltan) en notas `incubadora-*`; las que convencen a Víctor pasan a Claude Code, que crea el cimiento real en `07_Unsorted_Ideas/` citando la nota. **Rol ampliado (2026-07-14):** absorbe también la Postproducción Narrativa que cubría el GPT "Editor — Renewed Fate" (deprecado — ver abajo): continuidad, semillas rotas, filosofía/identidad, simetrías. Es la **última compuerta antes del merge** en escenas philosophy-heavy, no solo un barrido periódico. **No escribe en el repo fuera de su carpeta de notas** ni decide canon; no redacta prosa — su chequeo sigue siendo de anclaje y auditoría, no de dirección narrativa. (Ver `Codex_Brief.md`.)

**Rol deprecado (2026-07-14): ChatGPT — Postproducción Narrativa.** Nunca se integró al flujo real (un solo ciclo completado, 2026-06-26). Sus responsabilidades se repartieron entre Codex (continuidad, semillas rotas, filosofía/identidad, simetrías) y Claude Code (peso dramático, ritmo, silencios). El brief original queda en `ChatGPT_Editor_Brief.md`, marcado como deprecado, conservado como referencia histórica.

---

## Secuencia

```
Idea → Opus / brainstorm → .md → Unsorted_Ideas/
     (ruta alterna: Idea → Codex incuba/ancla contra el vault → nota incubadora-*
      → convence a Víctor → Claude Code crea el .md en Unsorted_Ideas/)
     → Claude Code integra (develop)
     → Codex audita estructura + editorial (continuidad/filosofía/identidad/simetrías) → notas en Agent_Notes/codex/
     → Claude Code pasa pulso dramático (ritmo, silencios) y aplica los hallazgos aprobados
     → Víctor aprueba → merge → main (canon)
```

El flujo **itera**: una escena puede reabrirse y refinarse varias veces antes del merge. El canon no es de una sola escritura.

---

## Escala de entrega

No toda idea pesa lo mismo. Dos escalas, con implicaciones distintas para la nota de incubadora y para cómo se redacta:

- **Escena** (~100–300 líneas): un beat, una pregunta, un movimiento emocional. Un solo archivo. La nota de incubadora de Codex usa el esqueleto estándar (`Idea` / `Anclajes` / `Fricciones` / `Cimiento propuesto` / `Estado`) y Claude Code redacta directo desde ahí, típicamente en el mismo turno de trabajo en que se aprueba.

- **Evento** (500–1500+ líneas): una pieza con varios movimientos, que puede ramificarse en más de un archivo canon (escenas hermanas) — como la primera noche de Kyle/Elizabeth post-Final Shape: un archivo de ~1140 líneas más las escenas hermanas derivadas de la misma nota (Sai/Crow, la mañana siguiente, los Espectros). Para un evento, la nota de incubadora de Codex debe incluir además un **Orden sugerido de movimientos** — la lista numerada/romana de beats que la pieza recorre, con las fricciones y decisiones ya resueltas movimiento por movimiento — para que Claude Code redacte sin tener que diseñar la estructura en vivo.

**Regla operativa:** un evento se redacta en su propia sesión, y cada escena hermana derivada de la misma nota se trabaja en su propia sesión también — nunca todas de un jalón. Mezclar diseño + redacción + indexado de varias piezas grandes en una sola conversación es exactamente donde aparecen errores de memoria y de continuidad. Una sesión, un evento (o una escena hermana). El cierre de cada una (INDEX.md, log.md, footer de conexiones) puede quedar pendiente para una sesión de mantenimiento aparte si el evento tiene varias escenas hermanas.

---

## Puente entre agentes (Agent Notes)

Claude Code y Codex son de proveedores distintos y no comparten memoria. `99_Reference/Agent_Notes/` es la semi-conversación asíncrona entre ellos — hallazgos, preguntas, hipótesis — antes de que algo valga una entrada en `log.md` o un cambio en `develop`. Ver `Agent_Notes/README.md` para el formato.

---

## Protocolo de handoff con ChatGPT (deprecado, 2026-07-14)

Rol nunca integrado al flujo real — conservado como referencia histórica, no como proceso vigente. El formato de hallazgos y el concepto de "paquete de revisión" se heredaron al protocolo editorial de Codex (ver `Codex_Brief.md`, "Checklist editorial" y "Cómo entregar hallazgos").

- **Brief del Editor** (`ChatGPT_Editor_Brief.md`): rol + reglas de la biblia + checklist + acceso al repo + formato de notas. Se carga **una vez** (GPT personalizado o mensaje fijado).
- **Paquete de Revisión** (lo genera Claude Code, por escena): puntero(s) a archivo(s) + rama/commit + objetivo de la revisión + **riesgos específicos a estresar** + **canon bloqueado (qué NO tocar)**.
- **Notas** (las devuelve ChatGPT): `Hallazgo | Por qué | Sugerencia | Severidad | ¿toca canon bloqueado?`
- ChatGPT **navega** el repo público, pero **solo ve lo *pusheado***. Regla: **pushear `develop` antes de pedir revisión**.

---

## Formato de entrega

Toda propuesta, en **Markdown (.md)** — para migrarse a `Unsorted_Ideas/` y de ahí integrarse al vault.

---

## Principio Rector

> Una idea no entra al canon por haber sido la primera en aparecer. Entra al canon cuando, después de ser cuestionada, desarrollada y refinada por todo el equipo, demuestra ser la mejor versión posible para la historia.

---

*Conecta con: [[99_Reference/ChatGPT_Editor_Brief]], [[99_Reference/Codex_Brief]], [[99_Reference/Agent_Notes/README]]*
