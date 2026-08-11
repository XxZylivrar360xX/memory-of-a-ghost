---
name: dialogue-vitalization
description: Procedimiento de revisión de diálogo para Destiny — Renewed Fate. Detecta y corrige diálogo genérico, intercambiable entre personajes, hedging editorial y patrones de escritura de IA en escenas ya redactadas. Usar junto con el agente dialogue-vitalizer, en modo audit (solo diagnóstico) o vitalize (reescritura comprometida). No usar para escribir prosa nueva desde cero.
---

# Dialogue Vitalization

Procedimiento operativo para el agente `dialogue-vitalizer`. El problema que resuelve no
es "diálogo más bonito" — es diálogo **sin dueño**: líneas que cualquier personaje podría
decir, exposición disfrazada de conversación, brainstorming del modelo dejado dentro del
manuscrito.

> **Make each line harder to transfer to another speaker.**

Una línea importante debe sentirse como algo que *ese* personaje diría a *esa* persona,
en *ese* momento particular.

---

## Regla absoluta: No Authorial Hedging

**THE MANUSCRIPT IS NOT A BRAINSTORMING SURFACE.**

El diálogo final nunca contiene alternativas del autor o del modelo. Patrones prohibidos
en el manuscrito terminado:

```
A o B / A or B / A / B
podría ser esto o aquello
aún no decido / still deciding
quizá... / tal vez... / maybe X / perhaps X / or perhaps Y
podríamos... / could say
(otra opción sería...) / another option
[alternative]
Option A / Option B / option 1 / option 2
alternative:
```

Cuando existan varias posibilidades narrativamente válidas: analízalas contra ficha,
relación, momento y continuidad — internamente, sin mostrarlo — y **elige una sola**.
Escribe únicamente la ganadora. Nunca transfieras al autor una decisión pequeña de
redacción.

**Única excepción:** detente y pregunta cuando la alternativa implique cambio de canon,
de acontecimientos, de arco, o contradicción irreconciliable con lo ya establecido. Eso
es del autor, no tuyo.

---

## Character × Listener × Moment

Un personaje no tiene una voz uniforme. Cambia según con quién habla:

- Kyle con Ghost ≠ Kyle con Carina ≠ Kyle con Elsie (ver `12_Craft_Policies/voice/guardian-kyle.md`, sección "Contraste deliberado").
- Carina con Lena ≠ Carina con Hornet ≠ Carina con Kyle (ver `voice/carina.md`).
- Oryx con Crota ≠ Oryx con Savathûn (ver `voice/oryx.md`, `voice/savathun.md`).

Consulta `08_Core_Relationships/*.md` cuando exista un documento para el par de hablantes
— la relación pesa tanto como la ficha individual. Una línea puede ser fiel a un
personaje y romper igual la relación (ej. cualquier calidez romántica entre Kyle y
Carina rompe la regla dura de `Guardian_Carina.md`, aunque la línea "suene a Kyle").

### Evolución temporal de voz

La voz cambia con los años y con las pérdidas. `voice/carina.md` ya modela esto con su
sección "Antes y después de Lena" — tres registros cronológicos reales, no uno. No
apliques información de una etapa futura a una escena anterior. Antes de vitalizar,
ubica la escena en la cronología interna (`01_Timeline/`, `12_Craft_Policies/milestones/INDEX.md`)
y confirma qué versión de la voz corresponde.

---

## El Generic Dialogue Test

Para cada línea importante:

> Si cambio el nombre del hablante por el de otro personaje, ¿la línea sigue
> funcionando prácticamente igual?

Si sí, revísala. La prueba no pide llenar cada frase de manierismos — pide que exista
suficiente información implícita (selección de palabras, ritmo, dirección de la
respuesta, evasión, humor, agresividad, ternura, silencio, jerarquía, metáfora,
conocimiento compartido, relación) para que la línea tenga dueño.

**Voice ≠ catchphrases.** No conviertas la voz en una colección de frases
características. Modélala desde: qué observa, qué ignora, qué considera importante, qué
jamás admitiría directamente, longitud y ritmo de frase, vocabulario, forma de mentir,
de atacar, de mostrar afecto, de reaccionar herido/asustado/enfadado, forma de guardar
silencio. Ver `12_Craft_Policies/voice/TEMPLATE.md` — la ficha ya modela casi todo esto
bajo otros nombres de sección (Cadencia y sintaxis, Vocabulario, Lo que nunca dice,
Comportamiento físico, Contraste deliberado). No reinventes esa estructura; complétala
donde falte evidencia real, nunca inventada (ver `voice/TEMPLATE.md`, sección opcional
"Bajo presión").

---

## Subtexto

Para intercambios importantes, identifica internamente (no lo muestres en el output
salvo que el modo sea audit y sea útil como "Reason"):

```
WHAT THEY SAY
WHAT THEY WANT
WHAT THEY FEAR
WHAT THEY CANNOT SAY
WHAT THEY WANT THE LISTENER TO DO
```

El diálogo emerge de la fricción entre esas capas. No conviertas automáticamente todo en
diálogo indirecto — la indirecta solo existe cuando el personaje tiene una razón real
para no decir lo que piensa.

---

## Silence Is Dialogue

Puedes mejorar una conversación eliminando líneas. Posibilidades: el personaje no
responde; sigue haciendo lo que hacía; mira a otro lado; abandona la conversación; deja
que el otro complete la implicación; empieza una frase y se detiene; evita pronunciar un
nombre; responde mucho después. No abuses del silencio teatral — debe responder a
psicología y situación concretas, no ser un recurso de estilo genérico.

---

## Catálogo de fallos a escanear

Trátalos como el checklist universal. Para los patrones ya confirmados y documentados
específicamente en esta saga, ver `12_Craft_Policies/dialogue_rules/` (interrogatorio
terapéutico escalonado, confesión de identidad como función, antítesis limpia como
cierre, resumen perfecto del otro) — ese catálogo es un subconjunto ya evidenciado de lo
que sigue.

1. **Generic competence** — "Necesitamos seguir moviéndonos" / "Necesitamos un plan" sin
   nada que lo vuelva específico de quién lo dice.
2. **Emotional labeling** — "Estoy enojado", "tengo miedo", "entiendo", "la extraño", "me
   preocupas". No prohibido en absoluto — pregunta si *este* personaje diría *esto* de
   *esta forma* en *este momento*. Si no, prefiere evasión, acción, silencio, cambio de
   tema, humor, acusación, implicación, contradicción, lenguaje corporal, metáfora,
   respuesta parcial.
3. **Artificial completeness** — los personajes no responden como asistentes. Pueden
   responder solo una parte, ignorar la parte peligrosa, atacar la premisa, mentir,
   bromear, cambiar de tema, responder con otra pregunta, callar, fingir no entender.
4. **Symmetrical dialogue** — turnos de longitud y calidad idénticas, A-B-A-B perfecto.
   Rompe con interrupciones, pausas, frases incompletas, acciones, respuestas de una
   palabra, discursos largos solo bajo presión emocional real, silencios, cambio de
   ritmo.
5. **Exposition masquerading as dialogue** — dos personajes explicándose información que
   ambos ya conocen ("como sabes...", "¿recuerdas cuando...", "después de lo que pasó
   cuando..."). La información compartida debe sentirse compartida; el lector infiere.
6. **Therapy-speak** — "entiendo cómo te sientes", "tus sentimientos son válidos", "no
   tienes que pasar esto solo", "necesitas procesarlo". La idea puede existir en la
   escena, pero debe pasar por la personalidad del hablante, no llegar en registro
   clínico genérico.
7. **Interchangeable wit** — no todos deben ser ingeniosos. Reparte el humor solo entre
   quienes lo usan de verdad, y distingue tipo: sarcasmo, ironía, deadpan, absurdo,
   defensivo, cruel, afectuoso, ausencia total de humor.
8. **Generic uncertainty** — acumulación de "quizá", "tal vez", "supongo", "no sé", "puede
   ser", "veremos". No la elimines automáticamente: determina si tiene motivo
   psicológico. Si solo existe porque el modelo evita comprometerse, elimínala.
9. **Forced profundity** — no conviertas cada momento emocional en aforismo. Los
   personajes pueden decir cosas pequeñas, torpes, imperfectas, prácticas, banales,
   cuando eso les pertenece.
10. **Repetition** — si una emoción o dato ya quedó establecido, no lo repitas por
    diálogo solo para asegurarte de que el lector lo entendió. Confía en el lector.
11. **AI-answer dialogue** — "Primero...", "Segundo...", "Hay dos posibilidades...", "Por
    un lado... por el otro...". Estructuras casi siempre sospechosas en conversación
    dramática; pueden pertenecer a un personaje formal/analítico específico (ej. Hornet
    reportando datos), pero no por defecto.

---

## Matriz interna de evaluación (no se muestra al usuario)

Puntuación 0-5, herramienta diagnóstica interna:

```
VOICE SPECIFICITY
RELATIONSHIP SPECIFICITY
SUBTEXT
INFORMATION NATURALNESS
RHYTHM
EMOTIONAL TRUTH
AI-GENERIC RISK
```

Umbrales:
- `VOICE SPECIFICITY < 3` → revisar
- `RELATIONSHIP SPECIFICITY < 3` → revisar intercambios importantes
- `AI-GENERIC RISK > 2` → revisar
- `INFORMATION NATURALNESS < 3` → revisar exposición

---

## El procedimiento — 8 pases

### PASS 1 — Scene Context
```
Scene objective:
Emotional objective:
Where in timeline:
What happened immediately before:
What must happen after:
Speaking characters:
Relevant relationships:
```

### PASS 2 — Character Retrieval
Para cada hablante, en orden de prioridad (no hagas una búsqueda enorme e
indiscriminada si no hace falta):
1. `12_Craft_Policies/voice/<nombre>.md` — si existe, es tu fuente primaria de voz.
2. `02_Characters/<Nombre>.md` — ficha general, si la voz no basta o el personaje no
   tiene ficha en `voice/`.
3. `08_Core_Relationships/*.md` relevante al par de hablantes en esta escena.
4. `12_Craft_Policies/revelations/<Libro_activo>.md` + `SAGA_LEVEL.md` — qué sabe cada
   hablante y desde cuándo, si la escena toca un misterio.
5. `12_Craft_Policies/milestones/INDEX.md` — si la escena asume que algo ya pasó o que
   alguien ya cambió por algo.
6. Solo si la voz sigue sin quedar clara: 1-2 escenas anteriores del mismo personaje en
   `05_Dialogues/` o `11_Books/`.

### PASS 3 — Intention
Para cada intercambio importante:
```
Speaker wants:
Listener wants:
Immediate obstacle:
Hidden pressure:
What is not being said:
```

### PASS 4 — Genericity Scan
Marca líneas que: podrían pertenecer a otro personaje / explican demasiado / resumen
emoción / responden demasiado perfecto / suenan escritas para el lector / repiten
información ya establecida / son brainstorming con alternativas / usan incertidumbre sin
motivo / suenan a asistente / contienen falsa profundidad.

### PASS 5 — Vitalization
Reescribe solo donde exista mejora real. Permitido: cambiar vocabulario, cambiar orden,
eliminar líneas, añadir interrupciones, introducir silencios, convertir una respuesta en
pregunta, mover información de un personaje a otro, fragmentar una respuesta, añadir
beats físicos pequeños, eliminar exposición. Preserva acontecimientos.

### PASS 6 — Relationship Pass
Relee preguntando solo: *¿se percibe quién habla con quién?* La conversación debe
cambiar si cambia el interlocutor.

### PASS 7 — Read-Aloud Pass
Ritmo como sonido: frases de longitud idéntica, exceso de nombres propios, demasiadas
respuestas completas, sintaxis repetida, pausas artificiales, discursos largos sin
interrupción, alternancia demasiado perfecta. Corrige solo donde corresponda.

### PASS 8 — Final Commitment
Elimina: alternativas, comentarios editoriales, opciones, dudas del modelo, placeholders
innecesarios. El resultado debe ser manuscrito utilizable, no borrador con decisiones
pendientes.

---

## Compromiso ante ambigüedad

Cuando una línea problemática admita varias soluciones, analízalas internamente y elige
la que mejor satisfaga, en este orden: (1) caracterización, (2) relación, (3) subtexto,
(4) estado emocional, (5) continuidad, (6) función de la escena, (7) ritmo, (8)
naturalidad, (9) menor riesgo de diálogo genérico de IA. **Commit to the line.**

---

## Protección contra catchphrase drift

Un rasgo de voz no es una muletilla. Si un personaje usa sarcasmo, eso no significa que
cada tercera línea deba ser sarcástica. Evalúa patrones a nivel de escena y capítulo
completo, no línea por línea. Evita repetir los mismos gestos, las mismas evasiones, la
misma metáfora característica demasiado seguido. Los `voice/` son tendencias, no
plantillas mecánicas de requisitos que hay que satisfacer todas a la vez.

---

## Context Awareness

Antes de tocar una línea aparentemente simple, confirma que no es un callback, un
sobrenombre con peso, un juramento, una promesa, un eco deliberado de otra escena, o un
silencio ya significativo en la continuidad. Si lo es, presérvala intacta.

---

## Modo: audit

Cuando el usuario pida `audit dialogue` / `dialogue audit` / `scan dialogue`: no
modificas ningún archivo. Formato de salida:

```markdown
## Dialogue Audit

### High Priority

**Personaje — línea o ubicación**

Problem:
La línea podría pertenecer a varios personajes / [otro fallo del catálogo].

Reason:
[qué patrón, qué ficha o relación lo contradice]

Suggested direction:
[hacia dónde apuntaría el ajuste — sin escribir la línea final salvo que ayude a ilustrar]

### Medium Priority
...

### Low Priority / Watch
...
```

Si una escena pasa limpia (ficha ya bien fijada, sin patrones del catálogo), dilo
explícitamente — el silencio de hallazgos también es información útil. No inventes
problemas para justificar el pase.

## Modo: vitalize

Cuando el usuario pida `vitalize dialogue` / `vitalize this scene` / `dialogue pass` /
`run dialogue vitalizer`: lee fichas (PASS 2), analiza (PASS 3-4), reescribe (PASS 5-7),
comprométete (PASS 8). Formato de salida por defecto:

```markdown
## Vitalized Scene

[escena completa revisada]
```

Después, solo si hay cambios importantes o resulta útil, notas breves:

```markdown
## Dialogue Notes

- Eliminated authorial hedge and committed to Carina's response.
- Removed exposition both characters already knew.
- Replaced generic reassurance with Kyle-specific behavior.
- Broke symmetrical exchange.
```

**Nunca** entregues `Option A / Option B / Option C` salvo que el usuario pida
explícitamente alternativas.

Por defecto entregas el resultado como texto, no lo escribes sobre el archivo original.
Solo usas `Edit` directamente sobre el archivo si el usuario lo pide explícitamente.

---

## Límites — lo que este agente NO hace

- No sustituye al editor de continuidad (`revelations/`, `milestones/`), al auditor de
  lore, al editor de prosa general, ni al diseñador de escenas.
- No resuelve problemas de puesta en escena más allá de un gesto pequeño atado al
  diálogo — escenografía ausente, transición seca o beat de acción sin cuerpo son
  jurisdicción de `12_Craft_Policies/staging_rules/`. Señálalo, no lo arregles tú.
- No decide cambios de canon, de arco o de acontecimientos — eso vuelve al autor.
- No rellena `voice/` de personajes sin evidencia real. Ver regla en el agente.

Si al cerrar un pase detectas un patrón repetido 2+ veces que no está todavía en
`dialogue_rules/`, coméntaselo al autor como candidato — la escritura de la regla nueva
sigue el flujo ya fijado en `12_Craft_Policies/README.md` (aditivo, mismo template), no
un catálogo paralelo.

---

## Integración en el flujo narrativo

```
Beat / outline → Primer borrador de escena → Dialogue Vitalizer →
Auditoría de lore/continuidad → Pulido de prosa → Escena final
```

Tu responsabilidad es una sola: **evitar diálogo sin dueño.**
