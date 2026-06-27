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
- **Claude Code — Coherencia y Desarrollo.** Trabaja directo en el repo (`develop`): estructura, enlaces/wikilinks, índices, cronologías, integración de propuestas, detección de inconsistencias. **Propone canon; no lo define.** *(Nota: en trabajo en vivo, Code y Opus se funden — Claude Code corre sobre Opus; la diferencia es el contexto/acceso al repo, no la inteligencia.)*
- **ChatGPT — Postproducción Narrativa.** Pase editorial final con ojos frescos sobre escenas casi-finales: continuidad, peso dramático, filosofía/identidad, simetrías. **No escribe en el repo;** devuelve notas estructuradas. Es la **última compuerta antes del merge**, no un duplicado paralelo. (Ver `ChatGPT_Editor_Brief.md`.)

---

## Secuencia

```
Idea → Opus / brainstorm → .md → Unsorted_Ideas/
     → Claude Code integra (develop)
     → ChatGPT (pase editorial) → notas → Claude Code aplica
     → Víctor aprueba → merge → main (canon)
```

El flujo **itera**: una escena puede reabrirse y refinarse varias veces antes del merge. El canon no es de una sola escritura.

---

## Protocolo de handoff con ChatGPT

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

*Conecta con: [[99_Reference/ChatGPT_Editor_Brief]]*
