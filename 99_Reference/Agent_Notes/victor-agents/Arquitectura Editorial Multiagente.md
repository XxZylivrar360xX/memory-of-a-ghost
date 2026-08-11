# Arquitectura Editorial Multiagente
## Destiny: Renewed Fate — Claude Code + Codex

### Propósito

Implementar y documentar una arquitectura editorial especializada para **Destiny: Renewed Fate** que aproveche las fortalezas y responsabilidades ya establecidas de:

- **Claude Code**
- **Codex**

El objetivo NO es crear una colección de agentes que hagan todos lo mismo.

El objetivo es construir una **sala editorial con separación estricta de responsabilidades**, donde:

> **Claude Code transforma.  
> Codex audita.  
> Víctor decide canon y dirección narrativa.**

La arquitectura debe integrarse con el sistema que ya existe en el vault.

No crear una segunda infraestructura paralela.

---

# 0. Autoridad y precedencia

Antes de implementar nada, leer completos y respetar, como mínimo:

```text
AGENTS.md
CLAUDE.md
INDEX.md
00_Biblia/
99_Reference/Development_Workflow.md
99_Reference/Codex_Brief.md
99_Reference/Agent_Notes/README.md
12_Craft_Policies/README.md
09_Roadmaps/README.md
11_Books/README.md
```

Inspeccionar además:

```text
.claude/
.claude/agents/
.claude/skills/
12_Craft_Policies/
99_Reference/
99_Reference/Agent_Notes/
```

si existen.

No asumir que la arquitectura descrita aquí debe imponerse literalmente si el repositorio ya tiene una convención equivalente.

Integrar.

No duplicar.

---

# 1. División fundamental de responsabilidades

## Claude Code

Claude Code es el lado:

```text
DEVELOPMENT
EDITORIAL TRANSFORMATION
PROSE
SCENE CONSTRUCTION
CHARACTER PERFORMANCE
ACTIVE REVISION
```

Claude puede:

- escribir;
- reescribir;
- editar;
- vitalizar;
- reestructurar escenas;
- integrar notas aprobadas;
- desarrollar roadmaps;
- aplicar correcciones;
- actualizar Craft Policies cuando emerge una regla establecida;
- modificar el vault dentro de sus permisos normales.

---

## Codex

Codex es el lado:

```text
AUDIT
CROSS-FILE ANALYSIS
CONSISTENCY
INDEXING
DIAGNOSTICS
RISK DETECTION
```

Codex NO debe convertirse en segundo escritor.

Sus hallazgos son propuestas.

Debe permanecer read-only salvo autorización explícita y conservar la regla ya existente:

```text
99_Reference/Agent_Notes/codex/
```

como área normal de escritura.

Codex puede:

- señalar contradicciones;
- detectar repetición;
- rastrear setups y payoffs;
- comprobar cronología;
- comprobar conocimiento de personajes;
- encontrar drift de caracterización;
- detectar divergencias de canon no documentadas;
- analizar pacing;
- encontrar huecos estructurales;
- generar incubadoras.

Pero NO debe arreglar silenciosamente esos problemas dentro de los capítulos.

---

# 2. Regla de no duplicación

Nunca crear un agente de Claude y un agente de Codex con exactamente la misma responsabilidad.

Ejemplo incorrecto:

```text
Claude:
continuity-auditor

Codex:
continuity-auditor
```

Esto genera:

- trabajo duplicado;
- diagnósticos contradictorios;
- sobreedición;
- pérdida de trazabilidad;
- gasto innecesario de contexto.

En cambio:

```text
Codex:
continuity-auditor
        ↓
produce hallazgo

Víctor:
acepta / modifica / rechaza
        ↓
Claude:
integra la corrección
```

La división general es:

> **Codex encuentra. Claude resuelve.**

---

# 3. Fuente de verdad editorial

Los agentes NO deben inventar sus propias biblias internas cuando el vault ya posee información equivalente.

Prioridad general:

```text
decisión explícita actual de Víctor
        ↓
00_Biblia/
        ↓
00_Book_Map.md del libro activo
        ↓
09_Roadmaps/ confirmados
        ↓
12_Craft_Policies/
        ↓
02_Characters/
        ↓
08_Core_Relationships/
        ↓
01_Timeline/
        ↓
escenas / capítulos ya canonizados
        ↓
material de referencia
```

La precedencia exacta existente en documentos del vault debe conservarse si es más específica.

---

# 4. `12_Craft_Policies/` es infraestructura compartida

No crear otra carpeta paralela con:

```text
voice rules
dialogue rules
staging rules
revelation ledgers
milestones
```

si estas categorías ya existen en `12_Craft_Policies/`.

Los agentes deben consumir:

```text
12_Craft_Policies/voice/
12_Craft_Policies/dialogue_rules/
12_Craft_Policies/staging_rules/
12_Craft_Policies/revelations/
12_Craft_Policies/milestones/
```

según corresponda.

Si una revisión descubre un nuevo patrón repetido, debe seguirse la política ya establecida para convertirlo en Craft Policy solo cuando realmente corresponda.

---

# 5. Principio editorial universal

Todos los agentes transformativos deben respetar:

> **Diagnose before rewriting.**

No tocar algo solo porque existe una manera diferente de escribirlo.

La pregunta no es:

> "¿Puedo mejorarlo?"

La pregunta es:

> "¿Existe un problema concreto que justifique intervenir?"

Otra regla universal:

> **Do not fix what already has a voice.**

---

# PARTE I — AGENTES DE CLAUDE CODE

---

# 6. Claude Agent — `dialogue-vitalizer`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo.

## Función

Detectar y corregir diálogo:

- genérico;
- intercambiable;
- excesivamente explícito;
- expositivo;
- simétrico;
- demasiado completo;
- lleno de lenguaje de asistente;
- lleno de authorial hedging;
- sin relación específica con el interlocutor.

Debe leer obligatoriamente los voice fingerprints existentes.

---

## Filosofía

> **A line that could belong to five characters belongs to none of them.**

> **Character × Listener × Moment.**

> **The manuscript is not a brainstorming surface.**

> **Commit to one line.**

---

## Restricción crítica

Nunca dejar dentro del manuscrito:

```text
A o B
A / B
maybe X
perhaps Y
another option
could say
aún no decido
option 1
option 2
[alternative]
```

cuando esa indecisión pertenece al modelo y no al personaje.

Si existen varias soluciones:

analizar internamente y escoger una.

---

## Contexto mínimo

Antes de intervenir leer:

```text
voice fingerprint del hablante
voice fingerprint del interlocutor
relación relevante
milestones relevantes
revelation ledger si corresponde
dialogue rules
```

---

## Permisos

Puede modificar diálogo y pequeños beats necesarios para su entrega.

No debe convertir un dialogue pass en reescritura completa de la escena.

---

# 7. Claude Agent — `scene-doctor`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Diagnóstico + transformación estructural local.

## Pregunta central

> **¿Esta escena cambia algo?**

---

## Busca

- escenas donde suceden cosas pero nada cambia;
- objetivos poco claros;
- escenas sin resistencia;
- conversaciones sin giro;
- escenas que empiezan y terminan emocionalmente igual;
- entradas demasiado tempranas;
- salidas demasiado tardías;
- escenas construidas únicamente para entregar información;
- beats sin consecuencia;
- escenas que deberían fusionarse;
- escenas que contienen dos centros dramáticos incompatibles.

---

## Modelo mínimo

Para cada escena:

```text
WHO WANTS WHAT?
WHY NOW?
WHAT RESISTS THEM?
WHAT CHANGES?
WHAT DOES IT COST?
WHY DOES THE SCENE END HERE?
```

---

## Puede modificar

- orden de beats;
- entrada;
- salida;
- pequeños elementos de staging;
- distribución de información;
- ubicación del giro;
- estructura local.

No debe cambiar acontecimientos mayores sin indicarlo.

---

# 8. Claude Agent — `subtext-editor`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo.

## Función

Detectar cuando:

```text
narración
+
diálogo
```

explican exactamente lo mismo.

---

## Busca

- emociones nombradas después de haber sido mostradas;
- personajes explicando lo que claramente sienten;
- narrador interpretando un gesto que ya era suficiente;
- simbolismo explicado;
- relaciones verbalizadas innecesariamente;
- tensión resuelta mediante explicación;
- subtexto convertido en texto.

---

## Regla

No convertir todo en misterio.

La claridad directa puede ser correcta.

Solo eliminar explicitud cuando exista una capa que el personaje:

- no pueda;
- no quiera;
- no sepa;
- o no necesite

decir directamente.

---

# 9. Claude Agent — `prose-degenericizer`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo.

## Función

Es el equivalente narrativo del Dialogue Vitalizer.

Su trabajo NO es:

> "hacer la prosa más bonita".

Su trabajo es:

> **hacer que la narración pertenezca al POV y a la escena.**

---

## Busca

Patrones como:

```text
algo en su voz
por primera vez
como si
no era X, era Y
algo dentro de él
el peso de...
una parte de...
de alguna manera
por un momento
no supo qué decir
más de lo que quería admitir
```

cuando aparecen como automatismos.

También:

- abstracciones emocionales;
- metáforas intercambiables;
- falsa profundidad;
- frases que podrían estar en cualquier novela;
- redundancia poética;
- sobreexplicación de imagen;
- ritmo excesivamente uniforme;
- cierre artificial de cada párrafo con "línea importante".

---

## Regla

No eliminar patrones solo porque aparezcan en una lista.

Determinar primero si su uso concreto funciona.

---

# 10. Claude Agent — `exposition-surgeon`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo.

## Especial importancia

Destiny contiene:

- cosmología;
- facciones;
- historia;
- mecánicas paracausales;
- Lógica de la Espada;
- Vex;
- Ascendant Plane;
- Darkness;
- Traveler;
- Witness;
- Hive;
- Ahamkara;
- Nine;
- raids.

La exposición es inevitable.

El objetivo NO es eliminarla.

El objetivo es:

> **poner cada pieza de información en la forma narrativa correcta.**

---

## Clasifica información como

```text
NEEDS EXPLICIT EXPLANATION
CAN BE INFERRED
SHOULD BE DELAYED
SHARED KNOWLEDGE
CHARACTER DISCOVERY
ENVIRONMENTAL INFORMATION
ACTION-BASED INFORMATION
UNNECESSARY
```

---

## Busca

- "como sabes";
- personajes recordándose información compartida;
- párrafos que detienen la escena;
- explicación anterior a la necesidad dramática;
- respuestas enciclopédicas;
- personajes actuando como Wiki.

---

# 11. Claude Agent — `relationship-editor`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo, pero conservador.

## Unidad de análisis

NO:

```text
Character A
Character B
```

sino:

```text
A ↔ B
```

La relación es tratada como una entidad narrativa con estado propio.

---

## Examina

- confianza;
- intimidad;
- distancia;
- resentimiento;
- deuda;
- autoridad;
- contacto físico;
- lenguaje privado;
- sobrenombres;
- humor compartido;
- secretos;
- heridas;
- promesas;
- límites;
- formas exclusivas de silencio;
- cómo cambia una interacción después de cada milestone.

---

## Pregunta fundamental

> **¿Esta relación ya se ganó este momento?**

---

## Uso

Especialmente útil para relaciones de largo desarrollo.

No debe inventar romanticismo, familiaridad o conflicto que el arco todavía no haya ganado.

---

# 12. Claude Agent — `action-choreographer`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Transformativo.

## Función

Mantener legibilidad y causalidad durante:

- combates;
- persecuciones;
- infiltraciones;
- raids;
- escapes;
- enfrentamientos multi-personaje.

---

## Mantiene mentalmente un estado

```text
WHO
WHERE
CAN SEE WHAT
HAS WHAT
CAN DO WHAT
IS INJURED HOW
WHAT CHANGED AFTER THE LAST ACTION
```

---

## Busca

- teleportación accidental de personajes;
- ataques sin origen;
- enemigos olvidados;
- heridas que desaparecen;
- orientación espacial incomprensible;
- habilidades disponibles demasiado pronto;
- personajes reaccionando a algo que no pueden ver;
- acción sin coste;
- espectáculo sin causalidad.

---

## Regla

La espectacularidad nunca justifica romper geografía ni causalidad.

---

# 13. Claude Agent — `raid-narrativizer`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Especializado.

Puede ser Skill especializada de `action-choreographer` si la arquitectura existente lo hace más limpio.

---

## Función

Traducir mecánicas de Destiny de:

```text
GAMEPLAY LOGIC
```

a:

```text
DIEGETIC / PARACAUSAL CAUSALITY
```

sin perder la identidad del encounter.

---

## Pregunta central

Nunca:

> "¿Cómo reproduzco exactamente la mecánica?"

Sino:

> "¿Qué realidad física, tecnológica, ritual o paracausal experimentan los personajes que en gameplay se representa mediante esta mecánica?"

---

## Debe preservar

- geografía;
- identidad visual;
- función dramática;
- escalada;
- firma del boss;
- condiciones de éxito;
- condiciones de fracaso.

---

# 14. Claude Agent — `chapter-closer`

## Propietario

```text
CLAUDE CODE
```

## Tipo

Ligero y opcional.

No debe ejecutarse automáticamente siempre.

---

## Examina

### Apertura

- orientación;
- situación;
- tensión;
- impulso.

### Cierre

Debe producir al menos uno de:

```text
RESOLUTION
TRANSFORMATION
PROPULSION
REVELATION
DREAD
```

---

## Busca

cierres genéricos como:

```text
y se marcharon
mañana sería otro día
todavía quedaba trabajo
solo el tiempo diría
```

cuando no están dramáticamente justificados.

---

# PARTE II — ROLES DE AUDITORÍA DE CODEX

---

# 15. Filosofía de Codex

Codex no necesita necesariamente "subagentes" técnicos si la infraestructura actual no los soporta o no los necesita.

Pueden implementarse como:

- audit modes;
- briefs;
- checklists;
- Skills;
- instrucciones nombradas;
- plantillas de handoff;

según la arquitectura real.

Lo importante es la separación conceptual.

---

# 16. Codex Audit — `continuity-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

## Función

Auditor factual cross-vault.

---

## Rastrea

- fechas;
- viajes;
- ubicaciones;
- heridas;
- armas;
- objetos;
- naves;
- muertes;
- resurrecciones;
- relaciones;
- estados de mundo;
- presencia de personajes;
- nombres;
- títulos;
- apodos;
- edades;
- orden de acontecimientos;
- conocimiento adquirido.

---

## Output

Hallazgos.

Nunca corrección silenciosa.

---

# 17. Codex Audit — `character-arc-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

## Diferencia respecto a `relationship-editor`

Claude pregunta:

> "¿Cómo hago funcionar esta interacción?"

Codex pregunta:

> "¿Es coherente que esta interacción ocurra aquí?"

---

## Busca

- evolución emocional prematura;
- regresiones no justificadas;
- duelo resuelto demasiado pronto;
- intimidad no ganada;
- cambio ideológico sin antecedente;
- competencias adquiridas antes de tiempo;
- conocimiento futuro filtrándose hacia atrás.

---

## Pregunta central

> **¿Este personaje ya se ganó psicológicamente esta conducta?**

---

# 18. Codex Audit — `repetition-hunter`

## Propietario

```text
CODEX
```

## Tipo

Read-only, cross-file.

---

## Busca dos clases de repetición

### Repetición superficial

- palabras;
- estructuras;
- gestos;
- metáforas;
- fórmulas.

### Repetición semántica

Mucho más importante:

```text
la misma emoción explicada varias veces
el mismo descubrimiento repetido
el mismo conflicto resuelto nuevamente
el mismo lore reexplicado
la misma función de escena
el mismo beat emocional
```

---

## Ejemplo conceptual

No basta reportar:

> "aparece 'como si' 14 veces."

Debe poder reportar:

> "Kyle llega tres veces a la misma conclusión sobre proteger vs controlar sin que entre ellas exista nueva información que justifique reabrir el descubrimiento."

---

# 19. Codex Audit — `setup-payoff-tracker`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

---

## Mantiene conceptualmente registros de

```text
SETUP
PROMISE
QUESTION
OBJECT
WOUND
MYSTERY
PROPHECY
RELATIONSHIP BEAT
THREAT
DEBT
CALLBACK
PAYOFF
```

---

## Detecta

- setup sin payoff;
- payoff sin setup suficiente;
- setup repetido innecesariamente;
- payoff demasiado temprano;
- promesa olvidada;
- objeto cargado narrativamente que desaparece;
- misterio resuelto sin escalada;
- callback roto.

---

## Integración

Debe apoyarse en los revelation ledgers existentes en vez de sustituirlos.

Si descubre algo ausente del ledger:

reportarlo.

No modificarlo directamente salvo autorización.

---

# 20. Codex Audit — `knowledge-state-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

## Función

Especializado en:

> **¿Quién sabe qué, cuándo y por qué?**

---

## Comprobar contra

```text
12_Craft_Policies/revelations/
12_Craft_Policies/milestones/
timeline
capítulos previos
```

---

## Busca

- personajes nombrando conceptos antes de conocerlos;
- información conocida sin fuente;
- revelaciones anticipadas;
- secretos olvidados;
- conocimiento del lector trasladado al personaje;
- consecuencias psicológicas de eventos todavía no ocurridos.

Este audit es especialmente importante porque ya existe evidencia histórica de este tipo de error dentro del proyecto.

---

# 21. Codex Audit — `canon-divergence-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

---

## Clasificación obligatoria

Toda diferencia respecto al canon externo debe clasificarse como:

```text
DESTINY CANON CONSISTENT
INTENTIONAL RENEWED FATE DIVERGENCE
DOCUMENTED DIVERGENCE
POSSIBLE UNDOCUMENTED DIVERGENCE
ACTUAL INTERNAL CONTRADICTION
UNKNOWN / NEEDS AUTHOR DECISION
```

---

## Regla crítica

No asumir:

> "esto contradice Destiny, por lo tanto está mal."

Renewed Fate es una reinterpretación.

El problema real es:

> "¿La divergencia está decidida, documentada y sostenida?"

---

# 22. Codex Audit — `pacing-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only.

## Escala

Capítulo, Part o libro.

No línea individual.

---

## Examina distribución de

- acción;
- conversación;
- introspección;
- exposición;
- viaje;
- revelación;
- combate;
- recuperación;
- transición.

---

## Busca

- escenas acumuladas con idéntica intensidad;
- demasiada resolución seguida;
- falta de respiración;
- respiración excesiva;
- conflicto que tarda demasiado en llegar;
- clímax mal colocado;
- capítulo con múltiples finales;
- largos segmentos procesando la misma emoción.

---

# 23. Codex Audit — `theme-drift-auditor`

## Propietario

```text
CODEX
```

## Tipo

Read-only y de baja frecuencia.

No ejecutar por escena.

Usar por Part o libro.

---

## Función

Contrastar el texto con:

```text
00_Biblia/Vision.md
00_Biblia/Themes.md
00_Biblia/Narrative_Principles.md
tesis del libro
00_Book_Map.md
```

---

## Busca

NO:

> "¿Aparece el tema suficientes veces?"

Sino:

> "¿Las decisiones y consecuencias del libro todavía dramatizan la tesis prometida?"

---

## Prohibición

Nunca recomendar meter monólogos filosóficos solo para reforzar tema.

La filosofía debe emerger de:

- decisiones;
- pérdidas;
- relaciones;
- consecuencias.

---

# PARTE III — FLUJO ENTRE AMBOS SISTEMAS

---

# 24. Pipeline — Idea nueva

Para una idea todavía no canonizada:

```text
IDEA
  ↓
Codex incubator / análisis de riesgos
  ↓
99_Reference/Agent_Notes/codex/
  ↓
TRIAGE CON VÍCTOR
  ↓
si se acepta
  ↓
09_Roadmaps/Plan_*.md
  ↓
CLAUDE CODE
  ↓
desarrollo
```

Preservar el sistema existente.

---

# 25. Pipeline — Escena nueva

```text
ROADMAP CONFIRMADO
        ↓
Claude — scene construction
        ↓
Dialogue Vitalizer
        ↓
Subtext Editor
        ↓
Staging / Action pass si aplica
        ↓
Prose Degenericizer solo si hace falta
        ↓
ESCENA
```

No todos los agentes son obligatorios.

El agente principal o Víctor elige según síntomas.

---

# 26. Pipeline — Capítulo terminado

```text
CAPÍTULO TERMINADO
        ↓
Codex — continuity
Codex — knowledge state
Codex — character arc
Codex — repetition
        ↓
hallazgos
        ↓
VÍCTOR TRIAGE
        ↓
Claude integra hallazgos aceptados
```

Pacing puede ejecutarse cuando sea útil.

---

# 27. Pipeline — Part terminada

```text
PART
  ↓
Codex — pacing
Codex — setup/payoff
Codex — repetition
Codex — continuity
  ↓
Claude — correcciones aprobadas
```

---

# 28. Pipeline — Libro terminado

```text
BOOK COMPLETE
     ↓
CODEX
     ├── continuity audit
     ├── character arc audit
     ├── knowledge-state audit
     ├── setup/payoff audit
     ├── repetition audit
     ├── pacing audit
     ├── canon-divergence audit
     └── theme-drift audit
     ↓
MASTER HANDOFF
     ↓
VÍCTOR
     ↓
CLAUDE CODE
     ↓
surgical revisions
     ↓
FINAL AUTHOR PASS
```

---

# 29. No ejecutar todo siempre

Crear explícitamente una política:

> **Agents are symptom-driven, not mandatory gates.**

Ejemplos:

Si una escena tiene diálogo excelente:

```text
skip dialogue-vitalizer
```

Si una escena no contiene acción compleja:

```text
skip action-choreographer
```

Si acaba de comenzar un arco:

```text
setup-payoff audit probablemente innecesario
```

Si solo se corrigieron tres frases:

```text
no ejecutar auditoría completa de libro
```

---

# 30. Evitar cascada de sobreedición

Nunca hacer automáticamente:

```text
scene-doctor
↓
dialogue-vitalizer
↓
subtext-editor
↓
relationship-editor
↓
prose-degenericizer
↓
exposition-surgeon
↓
chapter-closer
```

sobre cada escena.

Esto probablemente homogenizaría la voz.

Preferir:

```text
diagnose
↓
select specialist
↓
edit
↓
stop
```

---

# 31. Handoffs entre Codex y Claude

Los hallazgos de Codex deben conservar trazabilidad.

Formato recomendado:

```markdown
## Hallazgo

### Severidad
High / Medium / Low

### Tipo
Continuity / Character / Knowledge / Repetition / Setup-Payoff / etc.

### Ubicación
archivo + sección/capítulo

### Evidencia
qué documentos entran en conflicto

### Problema
descripción concreta

### Riesgo narrativo
qué rompe o debilita

### Dirección sugerida
qué debe revisarse

### Estado
OPEN / ACCEPTED / REJECTED / RESOLVED
```

Codex no necesita escribir la solución final.

Claude recibe hallazgos `ACCEPTED`.

---

# 32. Incubadora ≠ auditoría

No mezclar:

```text
IDEA INCUBATOR
```

con:

```text
ERROR AUDIT
```

Una incubadora puede explorar una dirección.

Un audit identifica un problema existente.

Usar nombres y carpetas que permitan distinguirlos claramente.

---

# 33. Editorial Director

NO implementar todavía un agente con autoridad para editar automáticamente mediante todos los demás.

Sí puede ser útil crear un:

```text
editorial-router
```

o equivalente cuyo único trabajo sea:

1. inspeccionar el texto;
2. identificar síntomas;
3. recomendar qué especialista ejecutar.

NO debe:

- editar;
- lanzar veinte agentes;
- tomar decisiones de canon;
- reemplazar el triage de Víctor.

---

## Ejemplo

```text
Dialogue genericity detected
→ dialogue-vitalizer

No staging issues
→ skip staging

Possible knowledge leak
→ recommend Codex knowledge-state audit

Strong existing voice
→ do not run prose-degenericizer
```

---

# 34. Qué NO debe automatizarse

Nunca permitir que un agente decida unilateralmente:

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
- cambio de Book Map;
- eliminación de setup importante.

Eso requiere decisión de Víctor.

---

# 35. Skills compartidas vs agentes

Regla conceptual:

> **Agent = profesión.  
> Skill / Craft Policy = método o conocimiento.**

Ejemplo:

```text
dialogue-vitalizer
```

puede consumir:

```text
voice fingerprints
dialogue rules
relationship docs
milestones
revelation ledger
```

No copiar toda esa información dentro de su system prompt.

---

# 36. Context budget

Cada especialista debe leer solo el contexto necesario.

No cargar 84 fichas de personajes para una escena con tres personas.

Preferir:

```text
speaker
listener
relationship
current book
relevant milestone
relevant revelation
local scene context
```

Escalar a búsquedas mayores cuando aparezca una contradicción.

---

# 37. Temporalidad

La caracterización debe modelarse como:

```text
CHARACTER
×
ERA
×
LISTENER
×
CURRENT EMOTIONAL STATE
```

Nunca importar automáticamente la versión final de un personaje hacia una etapa temprana.

---

# 38. POV

Todos los agentes transformativos deben respetar reglas de POV del libro activo.

Antes de introducir:

- pensamientos;
- certezas;
- información;
- sensaciones internas;

comprobar quién posee la perspectiva.

No "arreglar" una escena violando la perspectiva establecida.

---

# 39. Filosofía de edición

Añadir estas reglas comunes:

> **Character before eloquence.**

> **Specificity before prettiness.**

> **Causality before spectacle.**

> **Subtext before explanation — when the character has reason to hide.**

> **Do not confuse clarity with overexplanation.**

> **Do not confuse restraint with vagueness.**

> **Do not confuse complexity with depth.**

> **Do not make everyone witty.**

> **Do not make everyone emotionally articulate.**

> **Do not make every paragraph profound.**

> **Do not solve what the story deliberately leaves unresolved.**

---

# PARTE IV — IMPLEMENTACIÓN

---

# 40. Trabajo que Claude Code debe realizar ahora

## Paso 1

Inspeccionar:

```text
.claude/
99_Reference/Development_Workflow.md
99_Reference/Codex_Brief.md
12_Craft_Policies/
99_Reference/Agent_Notes/
```

y determinar qué infraestructura ya existe.

---

## Paso 2

Crear un documento rector, si no existe uno equivalente:

```text
99_Reference/Editorial_Agent_Architecture.md
```

o una ubicación mejor según las convenciones reales.

Debe documentar:

- Claude vs Codex;
- propietarios;
- agentes;
- audits;
- flujos;
- handoffs;
- permisos.

---

## Paso 3

Implementar primero los agentes Claude de mayor valor:

```text
dialogue-vitalizer
scene-doctor
subtext-editor
prose-degenericizer
```

Prioridad 1.

Después:

```text
exposition-surgeon
relationship-editor
action-choreographer
```

Prioridad 2.

`raid-narrativizer` puede ser agente o Skill según la infraestructura existente.

`chapter-closer` es opcional y baja prioridad.

---

# 41. Dialogue Vitalizer existente

Si ya existe un `dialogue-vitalizer` creado a partir de instrucciones previas:

NO recrearlo desde cero.

Auditarlo contra esta arquitectura.

Debe:

- consumir `12_Craft_Policies/voice/`;
- respetar revelation ledger;
- respetar milestones;
- respetar dialogue rules;
- respetar staging rules cuando sea necesario;
- prohibir authorial hedging;
- trabajar como segunda pasada;
- producir una sola versión comprometida.

---

# 42. Integración Codex

NO alterar la restricción read-only de Codex.

Actualizar `99_Reference/Codex_Brief.md` únicamente si hace falta para añadir los modos especializados:

```text
continuity
character arc
repetition
setup/payoff
knowledge state
canon divergence
pacing
theme drift
```

Estos pueden ser:

- secciones;
- checklists;
- briefs;
- perfiles;
- Skills;

según la arquitectura que mejor encaje con Codex.

No asumir que deben implementarse exactamente como subagentes técnicos.

---

# 43. AGENTS.md

Actualizar `AGENTS.md` solo si resulta necesario para referenciar el nuevo documento rector.

No inflarlo con toda esta especificación.

`AGENTS.md` debe seguir siendo routing.

La documentación detallada debe vivir en el documento editorial correspondiente.

---

# 44. Development Workflow

Revisar `99_Reference/Development_Workflow.md`.

Integrar esta arquitectura allí solo en la medida necesaria para explicar:

```text
Codex finds
Víctor triages
Claude develops / repairs
```

No duplicar todo el documento rector.

---

# 45. Craft Policies

No modificar masivamente Craft Policies.

Solo crear una nueva policy cuando:

- resuelve una necesidad real;
- no existe equivalente;
- es reutilizable;
- no pertenece exclusivamente al prompt de un agente.

---

# 46. Prueba controlada

Después de implementar:

seleccionar UNA escena ya existente con diálogo.

No sobrescribirla durante la prueba inicial.

Ejecutar conceptualmente:

```text
editorial diagnosis
→ dialogue-vitalizer si aplica
→ scene-doctor si aplica
```

Mostrar:

```text
qué problema encontró
qué agente corresponde
por qué
cómo lo cambiaría
```

Después seleccionar UN capítulo y demostrar qué encontraría Codex conceptualmente:

```text
continuity
knowledge state
repetition
```

No realizar una auditoría completa del libro como prueba.

---

# 47. Prueba de separación

La arquitectura falla si Claude y Codex producen ambos algo como:

```text
"Encontré esta contradicción y ya reescribí el capítulo."
```

El comportamiento correcto es:

### Codex

```text
Encontré esta contradicción.
Aquí está la evidencia.
Aquí está el riesgo.
Aquí está una dirección posible.
```

### Claude

tras aprobación:

```text
Integré la resolución aceptada preservando voz, continuidad y escena.
```

---

# 48. Estado y trazabilidad

Cuando Claude resuelva una nota de Codex:

marcarla según las convenciones existentes del vault.

No borrar el historial de razonamiento editorial útil.

Debe poder reconstruirse:

```text
qué detectó Codex
qué decidió Víctor
qué aplicó Claude
```

---

# 49. Prioridad recomendada de implementación

## FASE 1 — ahora

```text
Dialogue Vitalizer
Scene Doctor
Subtext Editor
Prose Degenericizer

Codex:
Continuity Audit
Knowledge-State Audit
Repetition Audit
```

---

## FASE 2

```text
Relationship Editor
Exposition Surgeon
Action Choreographer

Codex:
Character Arc Audit
Setup/Payoff Audit
Pacing Audit
```

---

## FASE 3

```text
Raid Narrativizer
Chapter Closer

Codex:
Canon Divergence Audit
Theme Drift Audit
```

No hace falta construir toda Fase 3 si todavía no existe una necesidad real.

---

# 50. Arquitectura final esperada

Conceptualmente:

```text
                         VÍCTOR
                    Dirección narrativa
                          /   \
                         /     \
                        /       \
                 CODEX           CLAUDE CODE
                AUDITORÍA        DESARROLLO
                    │                │
        ┌───────────┼───────┐        ├── Dialogue Vitalizer
        │           │       │        ├── Scene Doctor
 Continuity      Knowledge  Repetition
        │           │       │        ├── Subtext Editor
 Character Arc   Setup/Payoff        ├── Prose Degenericizer
        │           │                ├── Exposition Surgeon
     Pacing      Canon Drift         ├── Relationship Editor
        │                            ├── Action Choreographer
    Theme Drift                      └── Raid Narrativizer
        │
        ▼
   Agent Notes
        │
        ▼
      VÍCTOR
      triage
        │
        ▼
   Roadmap / decisión
        │
        ▼
    CLAUDE CODE
      integra
```

---

# 51. Principio rector final

Esta arquitectura existe para impedir dos fallos opuestos:

## Fallo 1 — Generación sin vigilancia

Claude escribe rápido pero introduce:

- diálogo genérico;
- repetición;
- conocimiento prematuro;
- pequeños conflictos de continuidad;
- psicología adelantada.

## Fallo 2 — Auditoría que se vuelve autoría

Codex encuentra un problema y comienza a reescribir la historia según su propia interpretación.

Ambos son indeseables.

El sistema correcto es:

> **Claude crea y transforma.**

> **Codex observa y cuestiona.**

> **Víctor conserva la autoridad narrativa.**

---

# 52. Instrucción final de implementación

No respondas únicamente con recomendaciones.

Realiza la implementación en el vault:

1. inspecciona la infraestructura real;
2. adapta esta arquitectura a las convenciones existentes;
3. crea el documento rector;
4. implementa los agentes Claude de Fase 1;
5. integra los modos Codex de Fase 1 en el lugar correspondiente;
6. enlaza la arquitectura desde la documentación existente sin duplicarla;
7. conserva las restricciones read-only de Codex;
8. reutiliza `12_Craft_Policies/`;
9. no dupliques voice fingerprints;
10. no reestructures el vault innecesariamente;
11. ejecuta una prueba controlada;
12. documenta qué archivos creaste o modificaste;
13. si tocaste archivos del vault, sigue el protocolo normal de commit y push a `develop`.

Antes de cerrar, verifica especialmente:

> **¿Puede distinguirse claramente qué encuentra Codex y qué arregla Claude?**

Si no, la separación todavía no está suficientemente definida.