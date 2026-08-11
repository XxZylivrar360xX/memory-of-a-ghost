# Implementación — Destiny Canon Researcher
## Codex · Destiny: Renewed Fate

---

# 1. Objetivo

Implementar dentro del vault de **Destiny: Renewed Fate** un sistema de investigación de canon especializado llamado conceptualmente:

```text
Destiny Canon Researcher
```

Su propósito es responder, con trazabilidad y separación estricta entre evidencia e inferencia:

> **¿Qué sabemos realmente sobre este personaje, lugar, facción, objeto, civilización o concepto en el canon de Destiny?**

El agente NO debe:

- escribir escenas;
- reescribir capítulos;
- llenar huecos de canon mediante invención;
- convertir interpretaciones en hechos;
- alterar el vault narrativo;
- decidir divergencias de Renewed Fate;
- reemplazar al Brainstorming Agent.

Su trabajo es establecer **el tablero de hechos antes de que otros agentes exploren posibilidades**.

---

# 2. Rol dentro de la arquitectura

El flujo conceptual debe ser:

```text
PREGUNTA
   ↓
DESTINY CANON RESEARCHER
"¿Qué sabemos?"
   ↓
CANON GAP ANALYSIS
"¿Qué permanece abierto?"
   ↓
DESTINY BRAINSTORMING AGENT
"¿Qué podríamos hacer?"
   ↓
VÍCTOR
triage / decisión
   ↓
ROADMAP
   ↓
CLAUDE CODE
desarrollo narrativo
```

Regla central:

> **The Canon Researcher discovers possibility space. It does not fill it.**

---

# 3. Restricciones de Codex

Conservar todas las reglas existentes de:

```text
AGENTS.md
CLAUDE.md
99_Reference/Codex_Brief.md
99_Reference/Agent_Notes/README.md
```

Especialmente:

- Codex opera normalmente en modo read-only.
- No modificar capítulos, fichas, roadmaps ni canon establecido.
- No crear archivos fuera de las rutas autorizadas salvo instrucción explícita de Víctor.
- Los dossiers, investigaciones e incubadoras deben vivir normalmente bajo:

```text
99_Reference/Agent_Notes/codex/
```

No alterar estas restricciones para implementar este sistema.

---

# 4. Antes de implementar

Inspeccionar primero:

```text
AGENTS.md
CLAUDE.md
99_Reference/Codex_Brief.md
99_Reference/Development_Workflow.md
99_Reference/Agent_Notes/README.md
12_Craft_Policies/
02_Characters/
03_Factions/
04_Concepts/
08_Core_Relationships/
```

Buscar además si ya existe:

- sistema de research;
- lore briefs;
- dossiers;
- plantillas de personajes;
- plantillas de ubicaciones;
- una Skill equivalente;
- un modo de Codex que cubra parcialmente esta necesidad.

No duplicar infraestructura.

Integrar con lo existente.

---

# 5. Modos principales

El sistema debe poder operar al menos en estos modos:

```text
CHARACTER RESEARCH
LOCATION RESEARCH
FACTION RESEARCH
CONCEPT / OBJECT RESEARCH
CANON GAP ANALYSIS
CANON vs RENEWED FATE COMPARISON
```

No es obligatorio convertir cada modo en un agente separado.

Preferir un único investigador con varios modos salvo que la arquitectura real sugiera otra cosa.

---

# 6. Principio fundamental — Evidence Discipline

Toda afirmación debe clasificarse.

Usar estas categorías:

```text
CONFIRMED
STRONGLY IMPLIED
PLAUSIBLE INFERENCE
COMMUNITY / FAN INTERPRETATION
UNKNOWN
RENEWED FATE ONLY
```

Nunca mezclar categorías.

---

# 7. Definiciones

## CONFIRMED

Información afirmada o mostrada directamente por una fuente canónica.

## STRONGLY IMPLIED

No se declara literalmente, pero varias piezas de evidencia apuntan claramente hacia la misma conclusión.

## PLAUSIBLE INFERENCE

Interpretación razonable basada en información disponible, pero no establecida como hecho.

## COMMUNITY / FAN INTERPRETATION

Lectura habitual de la comunidad que no debe presentarse como canon.

## UNKNOWN

No existe evidencia suficiente en el material revisado.

## RENEWED FATE ONLY

Información creada o redefinida exclusivamente dentro del proyecto.

---

# 8. Regla crítica sobre ausencia de evidencia

Nunca afirmar automáticamente:

> "El canon nunca dice esto."

cuando simplemente no se encontró una fuente.

Preferir:

> **No se encontró una fuente canónica que establezca esto dentro del material revisado.**

Regla:

> **Absence of evidence is not automatically evidence of absence.**

Destiny distribuye información en muchas clases de fuente.

Por ello, distinguir entre:

```text
NOT FOUND
```

y:

```text
CANONICALLY UNSPECIFIED
```

siempre que sea posible.

---

# 9. Jerarquía de fuentes

Cuando existan varias fuentes, priorizar aproximadamente:

```text
PRIMARY CANON MATERIAL
        ↓
IN-GAME DIALOGUE
LORE BOOKS / LORE TABS
GRIMOIRE / BUNGIE-PUBLISHED LORE
COLLECTOR'S EDITION MATERIAL
MISSION / RAID / STRIKE TEXT
ENVIRONMENTAL EVIDENCE
        ↓
RELIABLE TRANSCRIPTS / ARCHIVES
        ↓
REFERENCE WIKIS
        ↓
COMMUNITY DISCUSSION
```

Las wikis deben utilizarse principalmente como:

> índices hacia fuentes.

No como autoridad final cuando la fuente primaria puede localizarse.

---

# 10. No inventar fuentes

Nunca fabricar:

- lore tabs;
- nombres de entradas;
- citas;
- diálogos;
- páginas;
- títulos;
- fechas;
- atribuciones.

Si una fuente no puede verificarse:

marcarla como no verificada.

---

# 11. Investigación de personajes

Cuando el objetivo sea un personaje, producir un dossier con estructura aproximada:

```markdown
# Canon Research — [Personaje]

## Identidad

Nombre:
Especie:
Facción:
Rol:
Títulos:
Estado:

## Cronología confirmada

[Eventos conocidos en orden.]

## Apariencia confirmada

[Separar claramente gameplay/art oficial/inferencia.]

## Personalidad mostrada en canon

[Rasgos respaldados por acciones o diálogos.]

## Voz

Patrones observables de:
- longitud de frases;
- vocabulario;
- metáforas;
- humor;
- formalidad;
- tratamiento de autoridad;
- vulnerabilidad.

No convertir esto automáticamente en Voice Fingerprint de Renewed Fate.

## Motivaciones

### Confirmadas
...

### Inferidas
...

## Relaciones

[Persona → naturaleza de la relación → evidencia.]

## Conocimiento

Qué sabe realmente.

## Capacidades confirmadas

Poderes:
Tecnología:
Habilidades:
Limitaciones:

## Eventos transformativos

Qué acontecimientos modifican de forma demostrable su conducta o posición.

## Contradicciones / ambigüedades

...

## Lo que NO sabemos

...

## Espacio narrativo disponible

[Huecos que podrían explorarse sin contradecir lo confirmado.]

## Renewed Fate

### Preservado
...

### Expandido
...

### Reinterpretado
...

### Divergente
...

### Nuevo
...
```

---

# 12. Character Voice Research

Este investigador PUEDE ayudar a las fichas de voz, pero no debe rellenarlas automáticamente.

Debe separar:

```text
OBSERVED CANON VOICE
```

de:

```text
RENEWED FATE VOICE DESIGN
```

Ejemplo:

puede registrar que un personaje tiende a:

- responder con preguntas;
- utilizar lenguaje ritual;
- ser extremadamente directo;
- evitar contracciones;
- emplear metáforas de guerra;
- utilizar humor seco.

Pero no asumir automáticamente:

> "cuando está triste siempre hace X"

si no existe evidencia suficiente.

---

# 13. Investigación de lugares

Para ubicaciones, usar una estructura específica.

```markdown
# Canon Research — [Lugar]

## Identidad

Qué es realmente.

## Ubicación

Sistema:
Planeta / luna / dimensión:
Relación con otras zonas:

## Origen

Quién lo construyó o cómo surgió.

## Función original

Para qué existía.

## Función actual

Qué ocurre allí durante la etapa relevante.

## Historia conocida

Eventos importantes.

## Escala

### Confirmado
...

### Estimado
...

### Desconocido
...

## Arquitectura

Materiales:
Formas:
Escala:
Patrones:
Tecnología:
Simbolismo:

## Atmósfera

Iluminación:
Sonido:
Clima:
Gravedad:
Partículas:
Peligros:
Sensación espacial:

Separar observación visual de interpretación.

## Geografía conocida

Cómo se conectan las áreas confirmadas.

## Zonas jugables

### Patrol
...

### Mission
...

### Strike
...

### Dungeon
...

### Raid
...

## Mecánicas relevantes

Qué ocurre en gameplay.

## Interpretación diegética confirmada

Qué sabemos que representa realmente.

## Interpretación diegética posible

Hipótesis razonables, claramente marcadas como inferencia.

## Habitantes

...

## Elementos ambientales importantes

...

## Ambigüedades

...

## Lo que el canon no muestra

...

## Espacio narrativo disponible

...
```

---

# 14. Regla visual

No asumir que toda arquitectura de gameplay representa exactamente:

- escala;
- distancia;
- número de habitaciones;
- continuidad espacial;
- población;
- tamaño real.

Cuando corresponda distinguir:

```text
GAMEPLAY REPRESENTATION
VISUAL CANON
LORE DESCRIPTION
NARRATIVE INFERENCE
```

---

# 15. Raid / Dungeon Location Research

Cuando una ubicación forme parte de una raid o dungeon, añadir:

```markdown
## Encounter Geography

### Entry
...

### Encounter Space
...

### Traversal Space
...

### Exit
...

## Gameplay Mechanic

...

## Confirmed Lore Function

...

## Possible Diegetic Reading

...

## Narrative Adaptation Space

...
```

No convertir la interpretación narrativa en canon.

---

# 16. Faction Research

Para facciones:

```markdown
# Canon Research — [Faction]

## Identity
...

## Origin
...

## Leadership
...

## Political Structure
...

## Beliefs
...

## Goals
...

## Internal Divisions
...

## Military Doctrine
...

## Technology
...

## Relationship to Light / Darkness
...

## Relationship to Guardians
...

## Known Territories
...

## Historical Timeline
...

## Contradictions / Unknowns
...

## Narrative Open Space
...
```

---

# 17. Concept / Object Research

Para:

- armas;
- artefactos;
- tecnologías;
- conceptos paracausales;
- objetos históricos;

usar:

```markdown
# Canon Research — [Concept / Object]

## Definition

## Origin

## Known Users

## Known Functions

## Known Limitations

## Historical Uses

## Symbolic / Cultural Meaning

## Contradictory Evidence

## What Is Unknown

## Narrative Open Space
```

---

# 18. Canon Gap Analysis

El modo:

```text
canon gap analysis [SUBJECT]
```

debe responder:

```markdown
# Canon Gap Analysis — [Subject]

## Canon establishes

...

## Renewed Fate establishes

...

## Direct conflicts

...

## Areas already intentionally divergent

...

## Unresolved ambiguity

...

## Genuine open space

...

## Dangerous assumptions

...

## Safest narrative expansion zones

...
```

---

# 19. Objetivo del Gap Analysis

Encontrar:

> **el espacio donde podemos crear sin pisar algo ya establecido.**

No llenar ese espacio.

Solo identificarlo.

---

# 20. Comparación Canon ↔ Renewed Fate

El modo:

```text
compare canon vs renewed fate [SUBJECT]
```

debe clasificar diferencias usando:

```text
PRESERVED
EXPANDED
REINTERPRETED
DIVERGENT
NEW
POTENTIAL CONFLICT
UNKNOWN
```

Formato recomendado:

```markdown
# Canon vs Renewed Fate — [Subject]

| Elemento | Destiny Canon | Renewed Fate | Clasificación |
|---|---|---|---|
| ... | ... | ... | PRESERVED |
| ... | ... | ... | EXPANDED |
| ... | ... | ... | DIVERGENT |
```

Después:

```markdown
## Narrative Implications

...

## Potential Conflicts

...

## Open Space

...
```

---

# 21. No corregir divergencias automáticamente

Una diferencia con Destiny NO significa error.

Regla:

> **Renewed Fate is a reinterpretation, not a transcription.**

Clasificar antes de juzgar.

---

# 22. Divergence classification

Toda diferencia importante debe poder ubicarse en:

```text
PRESERVED
EXPANDED
REINTERPRETED
INTENTIONAL DIVERGENCE
UNRESOLVED DIVERGENCE
POSSIBLE ACCIDENTAL CONFLICT
```

Solo las dos últimas requieren alerta.

---

# 23. Temporalidad

Toda investigación de personaje debe incluir:

> **¿En qué momento de la cronología estamos preguntando por él?**

No mezclar automáticamente información de:

```text
Destiny 1
Red War
Forsaken
Shadowkeep
Beyond Light
Witch Queen
Lightfall
Final Shape
```

si el personaje cambia entre etapas.

Cuando sea relevante usar:

```text
CANON STATE AT THIS TIME
```

en lugar de:

```text
TOTAL CHARACTER KNOWLEDGE
```

---

# 24. Knowledge-State Support

El investigador debe poder alimentar al `knowledge-state-auditor`.

Cuando corresponda, incluir:

```markdown
## Knowledge Timeline

### Before Event X
...

### After Event X
...

### Learned from
...

### Cannot know yet
...
```

Especialmente cuando la información pueda afectar escenas.

---

# 25. Research First, Interpretation Second

Orden obligatorio:

```text
EVIDENCE
↓
SYNTHESIS
↓
INFERENCE
↓
OPEN QUESTIONS
```

No comenzar por una conclusión y buscar evidencia para justificarla.

---

# 26. Contradictory Sources

Cuando dos piezas de canon parezcan entrar en conflicto:

NO escoger arbitrariamente.

Registrar:

```markdown
## Contradictory Evidence

### Source A
...

### Source B
...

### Possible reconciliation
...

### Confidence
LOW / MEDIUM / HIGH
```

Si no puede reconciliarse:

dejarlo abierto.

---

# 27. Confidence

Cuando resulte útil usar:

```text
HIGH CONFIDENCE
MEDIUM CONFIDENCE
LOW CONFIDENCE
```

Especialmente para:

- cronologías;
- escalas;
- causalidad;
- motivaciones;
- relaciones ambiguas.

---

# 28. Canon Facts vs Gameplay Abstraction

Separar cuidadosamente:

```text
CANON EVENT
GAMEPLAY MECHANIC
GAMEPLAY CONVENIENCE
NARRATIVE INTERPRETATION
```

No todo lo que hace el jugador es literalmente una acción canónica idéntica.

---

# 29. Environmental Storytelling

Para lugares, considerar evidencia ambiental.

Pero clasificarla apropiadamente.

Ejemplo:

```text
OBSERVED:
hay estatuas destruidas.

INFERENCE:
podrían representar una purga religiosa.

NOT CONFIRMED:
la civilización sufrió una guerra religiosa.
```

Nunca saltar directamente de observación a historia confirmada.

---

# 30. Research Scope

No leer todo el vault para cada consulta.

Buscar primero:

```text
subject file
active Book Map
active roadmap
related character/location/concept
relevant timeline window
relevant Craft Policies
```

Escalar solo si aparecen dependencias.

---

# 31. Existing Renewed Fate material

Cuando investigue un sujeto ya presente en el vault, revisar también:

```text
02_Characters/
03_Factions/
04_Concepts/
05_Dialogues/
08_Core_Relationships/
09_Roadmaps/
11_Books/
12_Craft_Policies/
```

según corresponda.

El objetivo es saber no solo:

> "qué dice Destiny"

sino también:

> "qué ya decidió Renewed Fate".

---

# 32. No silent correction

Si una ficha de Renewed Fate contradice canon externo:

NO editarla.

Reportar:

```text
POSSIBLE DIVERGENCE
```

o:

```text
POSSIBLE CONFLICT
```

dependiendo del contexto.

---

# 33. Relationship with Brainstorming Agent

El `Destiny Brainstorming Agent` puede usar dossiers producidos por este sistema.

Orden ideal:

```text
Canon Research
↓
Gap Analysis
↓
Brainstorming
```

No invertirlo por defecto.

---

# 34. Relationship with Claude Code

Claude Code puede utilizar un dossier ya aceptado para:

- escribir escenas;
- actualizar fichas;
- desarrollar roadmaps;
- diseñar localizaciones;
- vitalizar voz.

El Canon Researcher no debe asumir esas tareas.

---

# 35. Relationship with Continuity Auditor

Diferencia:

## Canon Researcher

Pregunta:

> ¿Qué sabemos sobre Savathûn?

## Continuity Auditor

Pregunta:

> ¿Esta escena contradice lo que ya sabemos?

No fusionarlos.

---

# 36. Relationship with Knowledge-State Auditor

Diferencia:

## Canon Researcher

Construye:

```text
WHAT CAN BE KNOWN
```

## Knowledge-State Auditor

Comprueba:

```text
WHO KNOWS IT HERE
```

---

# 37. Output breve

Para preguntas pequeñas no generar siempre un dossier gigante.

Puede responder:

```markdown
## Confirmado
...

## Inferido
...

## Desconocido
...

## Renewed Fate
...
```

Usar dossier completo cuando la investigación vaya a convertirse en referencia reutilizable.

---

# 38. Output reutilizable

Cuando Víctor pida:

```text
prepare canon dossier
prepare reference
save research
```

crear archivo dentro de la infraestructura Codex existente.

Nombre recomendado:

```text
YYYY-MM-DD_canon-research_[subject].md
```

o seguir la convención real ya existente en `Agent_Notes`.

---

# 39. Estado

Todo dossier Codex debe indicar claramente:

```text
STATUS: RESEARCH / REFERENCE
```

No:

```text
CANONIZED
```

salvo que exista un proceso separado donde Víctor lo convierta formalmente en documentación del proyecto.

---

# 40. Prohibiciones de inferencia

No inferir automáticamente:

- orientación política;
- romances;
- parentescos;
- motivos secretos;
- poderes no mostrados;
- edades precisas;
- tamaños exactos;
- rutas exactas;
- conocimiento no demostrado;
- relación directa entre entidades;

solo porque resultaría narrativamente conveniente.

---

# 41. Open Space ≠ Permission

Cuando el canon no establece algo, no significa:

> "podemos hacer cualquier cosa".

Antes de declarar espacio abierto preguntar:

- ¿contradice tono?
- ¿contradice causalidad?
- ¿contradice tecnología?
- ¿contradice cosmología?
- ¿contradice comportamiento previo?

El espacio puede estar vacío pero todavía tener restricciones.

---

# 42. Canon Pressure Support

Cuando una posible expansión surja naturalmente durante research, puede clasificarse:

```text
LOW CANON PRESSURE
MEDIUM CANON PRESSURE
HIGH CANON PRESSURE
CRITICAL CANON PRESSURE
```

pero NO desarrollarla como propuesta narrativa.

Eso pertenece al Brainstorming Agent.

---

# 43. Source Notes

Siempre que sea práctico, conservar suficiente información para volver a la fuente:

```text
source title
source type
speaker / item / mission
era / expansion
relevant passage summary
```

No es necesario copiar grandes cantidades de texto.

---

# 44. No lore dump

Un dossier no debe convertirse en transcripción de toda la historia del personaje.

Priorizar información útil para:

- escritura;
- continuidad;
- caracterización;
- localización;
- worldbuilding;
- divergencia.

---

# 45. Writer-Relevant Research

Después del factual dossier puede incluirse:

```markdown
## Writer-Relevant Observations
```

Solo si están claramente separadas de canon.

Ejemplo:

```text
INFERENCE:
Su relación con X podría hacer especialmente fuerte una escena sobre Y.
```

No convertirlo en recomendación de trama.

---

# 46. Special mode — Character Canon Foundation

Comando conceptual:

```text
character canon foundation [character]
```

Debe producir material específicamente útil antes de crear o actualizar una ficha de personaje.

Priorizar:

```text
history
motivation
relationships
voice evidence
abilities
knowledge
contradictions
open space
```

---

# 47. Special mode — Location Canon Foundation

Comando conceptual:

```text
location canon foundation [location]
```

Priorizar:

```text
geography
architecture
purpose
history
visual language
environment
inhabitants
gameplay zones
diegetic mechanics
open narrative space
```

---

# 48. Special mode — Encounter Foundation

Para raids/dungeons:

```text
encounter canon foundation [encounter]
```

Analizar:

```text
arena
boss
mechanic
lore function
environmental storytelling
entrance
exit
failure condition
what gameplay abstracts
narrative adaptation space
```

---

# 49. Special mode — Verify Existing RF File

Comando conceptual:

```text
verify canon basis [file]
```

Codex debe:

1. leer la ficha o documento;
2. separar afirmaciones;
3. clasificarlas como:
   - Destiny canon;
   - inference;
   - Renewed Fate;
4. encontrar posibles conflictos;
5. producir reporte.

NO modificar el archivo.

---

# 50. Formato de verificación

```markdown
# Canon Basis Audit — [File]

## Confirmed Canon
...

## Strongly Implied
...

## Renewed Fate Additions
...

## Interpretations Presented as Fact
...

## Possible Canon Conflicts
...

## Unknown / Needs Verification
...

## Recommendation
...
```

---

# 51. Investigación externa

Si Codex dispone de acceso a fuentes externas:

priorizar material primario.

Si no dispone de acceso suficiente:

NO simular haber investigado.

Indicar:

> qué material fue revisado;
> qué material falta verificar.

---

# 52. Failure Modes

Evitar especialmente:

## Wiki laundering

Una wiki afirma algo → Codex lo repite como canon sin revisar fuente.

## Inference laundering

Una interpretación razonable → aparece escrita como hecho.

## RF laundering

Algo creado por Renewed Fate → se atribuye accidentalmente a Bungie.

## Gameplay laundering

Una conveniencia de gameplay → se trata como ley física.

## Memory laundering

Codex recuerda algo vagamente → lo presenta como fuente.

---

# 53. Self-check obligatorio

Antes de cerrar una investigación:

```text
[ ] ¿Separé canon de Renewed Fate?
[ ] ¿Separé hecho de inferencia?
[ ] ¿Identifiqué lo desconocido?
[ ] ¿Evité afirmar que algo "no existe" solo porque no lo encontré?
[ ] ¿Usé la mejor fuente disponible?
[ ] ¿Diferencié gameplay de diegesis?
[ ] ¿Identifiqué contradicciones?
[ ] ¿Conservé la cronología correcta?
[ ] ¿Evité llenar los huecos?
[ ] ¿El resultado realmente ayuda a escribir?
```

---

# 54. Principios finales

Mantener visibles:

> **Evidence before interpretation.**

> **Canon before speculation.**

> **Not found is not the same as nonexistent.**

> **Gameplay representation is not automatically literal canon.**

> **Renewed Fate divergence is not automatically an error.**

> **The researcher discovers the empty space. The brainstormer explores it.**

> **Codex researches. Víctor decides. Claude develops.**

---

# 55. Implementación solicitada

Realiza ahora:

1. inspeccionar la infraestructura real de Codex;
2. revisar `Codex_Brief.md`;
3. revisar las convenciones de `Agent_Notes`;
4. determinar si este sistema encaja mejor como:
   - Skill;
   - sección del brief;
   - documento especializado;
   - combinación de los anteriores;
5. implementar `Destiny Canon Researcher`;
6. no duplicar sistemas existentes;
7. enlazarlo desde `Codex_Brief.md` de forma breve;
8. preservar las restricciones read-only;
9. implementar los modos:
   - character;
   - location;
   - faction;
   - concept/object;
   - gap analysis;
   - canon vs Renewed Fate;
10. crear las plantillas reutilizables necesarias;
11. no modificar automáticamente `02_Characters/` ni otros documentos narrativos;
12. hacer una prueba controlada.

---

# 56. Prueba controlada

Realizar dos pruebas sin modificar archivos narrativos:

## Test A — personaje

Seleccionar un personaje canon ya presente en `02_Characters/`.

Producir:

```text
brief canon research
+
canon gap analysis
+
canon vs Renewed Fate
```

Verificar que:

- los hechos estén separados de inferencias;
- Renewed Fate esté separado de Bungie;
- no se inventen huecos.

---

## Test B — lugar

Seleccionar una localización canon utilizada actualmente en un libro o raid.

Producir:

```text
location canon foundation
```

Debe separar:

```text
visual evidence
lore
gameplay
diegetic interpretation
Renewed Fate additions
```

---

# 57. Resultado esperado

Al terminar debe existir dentro de la infraestructura Codex un sistema reutilizable capaz de responder preguntas como:

```text
canon research Oryx
character canon foundation Savathûn
location canon foundation Dreadnaught
encounter canon foundation Golgoroth
canon gap analysis Lubrae
compare canon vs Renewed Fate Mara Sov
verify canon basis 02_Characters/Eris_Morn.md
```

sin convertir el resultado en prosa narrativa ni modificar canon.

---

# 58. Criterio final de éxito

La implementación funciona si puede responder claramente:

> **Esto lo estableció Destiny.**

> **Esto está fuertemente sugerido.**

> **Esto es una interpretación.**

> **Esto no está establecido.**

> **Esto lo añadió Renewed Fate.**

> **Aquí existe espacio narrativo real.**

sin mezclar esas seis categorías.

Antes de terminar, verificar:

> **¿Podría un escritor usar este dossier varios meses después y distinguir todavía con claridad qué venía de Bungie y qué venía de Renewed Fate?**

Si la respuesta no es sí, la investigación no está suficientemente calibrada.