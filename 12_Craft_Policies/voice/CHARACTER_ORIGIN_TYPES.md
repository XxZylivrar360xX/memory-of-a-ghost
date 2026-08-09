# Character Origin Types

Esta política clasifica cada ficha de voz según la relación del personaje con el canon de
Destiny y con la adaptación propia de *Destiny: Renewed Fate / Memories of a Ghost*.

No es una jerarquía de importancia. Es una señal de escritura: indica cuánto peso tienen las
anclas externas de canon y cuánta libertad tiene la saga para definir voz, función y arco.

## Tipos

### canon_directo

Personaje canon de Destiny cuya continuidad, núcleo psicológico y función principal deben
preservarse con alta fidelidad. *Renewed Fate* puede ampliar, seleccionar énfasis o dramatizar
zonas no vistas, pero no sustituirlo por otro personaje.

**Uso típico:** Oryx, Savathûn, Mara Sov, Eris Morn, Zavala, Ikora, Saint-14.

**Regla de escritura:** antes de una escena importante, consultar su bible canónico/adaptado si
existe. Si la escena cambia un rasgo central del canon, debe estar justificado como desarrollo,
contradicción intencional o reinterpretación autorizada.

### canon_readaptado

Personaje canon cuya base se conserva, pero cuya función emocional, red de vínculos o arco
estructural cambia lo suficiente en *Renewed Fate* como para exigir reglas propias. No es
original, pero tampoco puede escribirse sólo desde la voz oficial de Destiny.

**Uso típico:** Elsie Bray, Ghost, Ana Bray, Crow, Osiris.

**Regla de escritura:** respetar el canon base, pero dar prioridad a las decisiones ya fijadas
en este vault: relaciones, hitos, consecuencias y voz local. La ficha debe explicar qué parte
es canon y qué parte es adaptación de *Renewed Fate*.

### canon_expandido

Personaje que existe en canon, pero con poca voz, poca interioridad o una función menor, y que
la saga convierte en personaje pleno. El canon fija existencia, nombre, rol o evento base; la
voz real depende mucho de *Renewed Fate*.

**Uso típico:** Malok, Catabasis, figuras de lore poco dramatizadas, aliados o antagonistas con
base canónica mínima.

**Regla de escritura:** no contradecir los datos canónicos disponibles, pero documentar con
claridad qué rasgos son extrapolación del vault.

### original_renewed_fate

Personaje creado para esta saga. Su fuente de verdad principal es el propio vault: capítulos,
diálogos, mapas, roadmaps, relaciones y fichas previas.

**Uso típico:** Kyle, Carina, Lena, Sai, Hornet, Eirene, Nemo, Atheena, Jaden si no posee base
canónica externa.

**Regla de escritura:** la libertad creativa es mayor, pero también lo es la obligación de
consistencia interna. La voz debe proteger lo que ya fue escrito, no copiar patrones de personajes
canon cercanos.

## Campo en frontmatter

Toda ficha nueva de `voice/` debe incluir:

```yaml
---
personaje: Nombre
origen: canon_directo
---
```

Valores permitidos:

- `canon_directo`
- `canon_readaptado`
- `canon_expandido`
- `original_renewed_fate`

Si el origen es discutible, usar el tipo más conservador y explicar la decisión en la nota inicial
de la ficha.

## Regla práctica

Antes de escribir diálogo, leer el campo `origen` como una advertencia de riesgo:

- `canon_directo`: riesgo de traicionar canon.
- `canon_readaptado`: riesgo de ignorar la adaptación local del vault.
- `canon_expandido`: riesgo de inventar sin anclar.
- `original_renewed_fate`: riesgo de volverlo intercambiable con voces ya existentes.

