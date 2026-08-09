# Codex — Craft Policies: origen de personajes y ficha de Savathûn

**Fecha:** 2026-08-09

## Hallazgo

Las fichas de voz necesitaban distinguir entre personajes canon, personajes canon readaptados,
personajes canon expandidos y personajes originales de *Renewed Fate*. Sin esa marca, agentes
futuros pueden tratar a Oryx, Ghost y Carina como si tuvieran el mismo margen de libertad.

También quedó listo el bible de Savathûn en `07_Unsorted_Ideas/`, equivalente al de Oryx, y era
momento de fijar su voz antes de continuar con personajes relacionados.

## Por qué

El riesgo de voz no es el mismo por origen:

- en `canon_directo`, el peligro es traicionar canon;
- en `canon_readaptado`, el peligro es ignorar la adaptación local del vault;
- en `canon_expandido`, el peligro es inventar sin anclar;
- en `original_renewed_fate`, el peligro es volver al personaje intercambiable con otros.

## Cambio aplicado

- Creado `12_Craft_Policies/voice/CHARACTER_ORIGIN_TYPES.md`.
- Actualizado `12_Craft_Policies/voice/TEMPLATE.md` con frontmatter obligatorio `origen`.
- Actualizado `12_Craft_Policies/README.md` para enlazar la política y listar fichas existentes.
- Agregado `origen` al frontmatter de las fichas ya creadas.
- Creada `12_Craft_Policies/voice/savathun.md` con `origen: canon_directo`.

## Severidad

Media. No bloqueaba la escritura inmediata, pero sí afectaba la consistencia futura de voces y
el margen de adaptación autorizado para personajes canon.

