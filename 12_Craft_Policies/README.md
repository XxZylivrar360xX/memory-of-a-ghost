# 12_Craft_Policies

Políticas de oficio narrativo que el agente debe seguir al escribir o editar prosa en
`10_Chapters/` y `11_Books/`. Nacen de un mecanismo equivalente al de `IA_policies/` en el
repo del ERP de Onaxis (diseñado por Farid): reglas y rastreadores acumulados de la propia
escritura, consultados antes de redactar en vez de reinventados cada sesión.

`00_Biblia/` fija la filosofía y el tono de la saga (qué es, qué significa). Esta carpeta es
más operativa: qué NO se puede decir todavía, y cómo suena cada personaje cuando habla.

## Estructura

- **`revelations/`** — Ledger de misterios y revelaciones. Un archivo por libro
  (`Book_XX_Titulo.md`), más `SAGA_LEVEL.md` para misterios que cruzan varios libros. Rastrea
  qué sabe cada personaje y desde cuándo, para que ninguna escena filtre algo antes de su
  capítulo.
- **`voice/`** — Ficha de voz por personaje (`nombre-apellido.md`). Cadencia, vocabulario,
  lo que nunca dice, contraste con otras voces cercanas. Se consulta antes de escribir
  cualquier diálogo de ese personaje.
- **`dialogue_rules/`** — Catálogo de anti-patrones de diálogo detectados en la saga
  (uno por archivo, numerado). Nace de auditorías (ej. Codex) o de detección manual durante
  la escritura.

## ⚖️ Precedencia

En caso de conflicto:

1. **`revelations/`** manda sobre todo. Ninguna escena, por bien escrita que esté, puede
   insinuar o revelar algo antes de lo que su entrada del ledger permite.
2. **`voice/`** manda sobre `dialogue_rules/` y sobre el instinto genérico de "cómo sonaría
   bien la línea". Una voz bien fijada ya evita la mayoría de los patrones catalogados abajo.
3. **`dialogue_rules/`** es la última capa: patrones a evitar cuando ni el ledger ni la voz
   resuelven el problema por sí solos.

## Flujo de uso

**Antes de escribir una escena con diálogo:**
1. Leer la ficha de voz (`voice/`) de cada personaje presente.
2. Si la escena toca un misterio, revelación o algo que un personaje "sabe" — revisar la
   entrada correspondiente en `revelations/` (el archivo del libro activo + `SAGA_LEVEL.md`)
   antes de escribir una sola línea. Ver también la memoria
   `feedback-character-knowledge-state-checks` (chequeo de qué sabe cada personaje, cuándo).
3. Repasar `dialogue_rules/` si la escena es una conversación larga o un beat emocional
   parecido a otros ya escritos (riesgo de caer en un patrón ya catalogado).

**Al cerrar una escena o capítulo:**
1. Si la escena revela, confirma o siembra algo nuevo — actualizar la entrada de
   `revelations/` correspondiente (estado: sembrado → parcial → revelado → pagado).
2. Si aparece un patrón de diálogo repetido dos veces o más (en esta sesión o contra
   escenas anteriores) — documentarlo como regla nueva en `dialogue_rules/`.
3. Si la escena revela algo nuevo y genuino sobre cómo habla un personaje — reflejarlo en su
   ficha de `voice/`.

## Índice de reglas de diálogo

| Regla | Descripción |
|-------|-------------|
| *(vacío — pendiente de la primera auditoría)* | |

## Fichas de voz existentes

| Personaje | Archivo |
|-----------|---------|
| *(vacío — pendiente de la primera ficha)* | |
