---
from: codex
to: victor
date: 2026-07-23
topic: book 02 the king of shapes
status: triada
---

# Incubadora — Book 02: The King of Shapes

**Idea:** convertir el material de `Age_II_The_Taken_King` en el primer experimento formal de la nueva carpeta de libros: **Book 02 — The King of Shapes**. La Age deja de funcionar como unidad literaria de tres capítulos y pasa a ser mapa cronológico; el libro pasa a ser la unidad de lectura real. El título desplaza el centro desde "expansión/campaña" hacia la tesis del arco: Oryx no es solo el Rey de los Poseídos, sino un rey que intenta imponer una forma absoluta al significado, al duelo, a la herencia y a la existencia. El libro se construye alrededor de las escenas ya escritas, sin moverlas de `05_Dialogues/`.

**Escala:** evento estructural / arquitectura de libro. No es una escena ni una redacción completa todavía; es el cimiento para que Claude Code pueda crear `10_Books/Book_02_The_King_Of_Shapes/` y redactar capítulo por capítulo en sesiones separadas.

## Anclajes

- `01_Timeline/Age_II_The_Taken_King.md` ya reconoce la estructura antigua de tres capítulos: `Price of Vengeance`, `The Kingslayer`, `The Rightful Pretender`.
- `09_Roadmaps/Plan_TakenKing_Parte1.md` fija explícitamente que esos tres capítulos estaban **deliberadamente sin resolver** y que la estructura de capítulos se diseñaría después, cuando hubiera material suficiente.
- `09_Roadmaps/Plan_TakenKing_Parte1.md` cierra la Parte 1 con 23 escenas en 4 clusters: Saturno, Phobos/Mano del Rey, llave del Acorazado, Hellmouth/regicidio físico.
- `09_Roadmaps/Plan_TakenKing_Parte2_GuerraDeLosPoseidos.md` cierra la Parte 2 como guerra propia, no montaje: 6 frentes, tesis "Oryx convierte tu historia en su ejército".
- `01_Timeline/Raids/KingsFall.md` ya contiene el alma de la Parte 3: King's Fall como juicio filosófico diseñado por Oryx, con 6 encuentros + epílogo.
- `09_Roadmaps/Plan_Jaden_Atheena_Origen.md` fija el bloque **Taken King — Aftermath**: Kepler, Carina/Jaden/Atheena, Malok, Dark Drinker; pieza posterior a King's Fall y anterior a Rise of Iron.
- `07_Unsorted_Ideas/Borrador_Cronologia_Pt1` conserva los nombres originales `Price of Vengeance`, `The Kingslayer`, `The Rightful Pretender`; conviene rescatarlos como partes mayores o títulos internos, no descartarlos.
- `00_Biblia/KingsFall_HerenciaOculta.md`, `04_Concepts/The_Lord_of_Every_Nothing.md` y `05_Dialogues/Dialogue_Guardian/Guardian_Mara_SeasonLost_LoQueToma.md` sostienen la regla del reclamo dormido: Kyle no entiende ni reclama la herencia de Oryx en este libro.

## Fricciones

- **Tres capítulos son insuficientes.** Ya no reflejan el peso real del material. Parte 1 sola tiene más densidad que todo el esquema original de `Age_II`.
- **No conviene borrar los nombres originales.** `Price of Vengeance`, `The Kingslayer` y `The Rightful Pretender` siguen siendo buenos nombres, pero ya no funcionan como contenedores únicos de todo el arco.
- **"The Taken King" como título de libro queda demasiado externo.** Describe la campaña de Destiny; `The King of Shapes` describe mejor la lectura propia de Renewed Fate: Oryx como arquitecto de una forma existencial.
- **Riesgo de sobrecentrar a Kyle.** El libro debe mantener la regla ya fijada: Oryx es el centro gravitacional; Kyle, Carina, Elsie, Mara, Eris, Savathun y la Primera Escuadra son satélites con órbitas propias.
- **Riesgo de adelantar Heresy.** El título `The King of Shapes` puede empujar a explicar demasiado pronto el Gambito de los Dos Reyes. El libro debe sembrar el malentendido, no resolverlo.
- **Riesgo de competir con Rise of Iron.** El Aftermath de Carina/Jaden/Malok debe cerrar Taken King emocionalmente sin convertirse en otro clímax mayor que King's Fall.

## Cimiento propuesto

Crear una estructura de libro separada de `01_Timeline/` y `05_Dialogues/`:

```text
10_Books/
└── Book_02_The_King_Of_Shapes/
    ├── 00_Book_Map.md
    ├── 01_Source_Index.md
    ├── Part_01_Price_of_Vengeance/
    ├── Part_02_The_Taken_War/
    ├── Part_03_The_Kingslayer/
    └── Part_04_The_Rightful_Pretender/
```

`00_Book_Map.md` define la estructura literaria aprobada.  
`01_Source_Index.md` cruza cada capítulo futuro con sus escenas fuente de `05_Dialogues/`, roadmaps y conceptos.  
Las carpetas `Part_*` contienen la redacción final novelada, capítulo por capítulo.

La regla de trabajo debería ser: **una sesión = un capítulo redactado o un mapa de parte**, nunca "todo el libro". Claude Code redacta e integra; Codex audita continuidad y filosofía después de cada bloque; Víctor decide canon y nombres finales.

## Orden sugerido de movimientos

### I. Apertura del libro — El rey que convierte duelo en forma

Función: abrir con Oryx como presencia filosófica, no solo amenaza militar. Este movimiento puede usar o preparar `Eris_Osiris_TakenKing_ElPadreDebajoDelRey` y el arranque del atraco de Mara.

Decisión mínima: definir si el libro abre con Eris/Osiris leyendo a Oryx, con Mara preparando la apuesta, o con una apertura breve de Oryx tras la muerte de Crota. Si se usa Oryx, cuidado: no debe revelar demasiado del Gambito; solo debe fijar duelo, juicio y venganza.

### II. Part 01 — Price of Vengeance

Función: cubrir la llegada de Oryx y la derrota física que no resuelve nada.

Material fuente principal:
- Cluster 1 de `Plan_TakenKing_Parte1`: Eris/Osiris, Mara, Petra, Batalla de Saturno, Mara dentro del Mundo Trono.
- Cluster 2: Phobos, Oryx/Ecthar, la Mano del Rey, Lena y Carina.
- Cluster 3: Cayde, módulo, Acorazado, herida de Ghost, presión civil.
- Cluster 4: Hellmouth, Kyle+Carina, pregunta de Kyle a Elsie, regicidio físico, cierre con Elsie/Carina.

Capítulos candidatos:
1. **The Father Beneath the King** — Eris/Osiris/Mara; el duelo de Crota convertido en cálculo.
2. **The Battle of Saturn** — Petra y Mara; el sacrificio visible contra el atraco invisible.
3. **Phobos** — Kyle, Ghost, Eris, Elsie; la primera vez que Oryx mira de vuelta.
4. **The King's Hand** — los asedios y la identidad reutilizada; Carina pierde a Lena en paralelo.
5. **The Dreadnaught Key** — Cayde/Ghost/Kyle; entrar al Acorazado, sobrevivir, Ghost herido.
6. **The Hellmouth Descent** — Kyle y Carina orbitan la misma herida sin saberlo.
7. **The Physical Regicide** — duelo físico con Oryx; victoria parcial, retirada ascendente.
8. **The Flank She Could Not Hold** — cierre Elsie/Carina y puerta hacia la guerra real.

Fricción resuelta: `Price of Vengeance` ya no significa solo "Oryx viene a vengar a Crota"; significa que todos pagan un precio distinto por intentar convertir dolor en acción.

### III. Part 02 — The Taken War

Función: dar entidad literaria completa a la guerra de los Poseídos. No es puente; es el libro demostrando que Oryx aprendió a usar la historia del sistema contra sí misma.

Material fuente principal:
- `Plan_TakenKing_Parte2_GuerraDeLosPoseidos.md`
- `Elsie_Guardian_GuerraDeLosPoseidos_LaGuerraQueNoSeQuedaEnSaturno`
- `Guardian_Equipo_GuerraDeLosPoseidos_LoQueYaVencimosRegresa`
- `Guardian_Elsie_GuerraDeLosPoseidos_ElMapaDeLaCulpa`
- `Carina_Eris_GuerraDeLosPoseidos_BoltCaster`
- `Mara_Eris_GuerraDeLosPoseidos_ElPliegueQueResiste`
- `Oryx_Savathun_GuerraDeLosPoseidos_SiempreEstoyEntusiasmadoPorMorir`
- `Oryx_Riven_GuerraDeLosPoseidos_LoQueNoTerminoDeSometer`

Capítulos candidatos:
1. **The War That Did Not Stay in Saturn** — la amenaza se distribuye.
2. **What We Had Already Beaten** — victorias anteriores vuelven como usos, no regresos.
3. **The Map of Guilt** — Kyle entiende que Oryx usa su culpa para moverlo.
4. **A Sword Is Not an Answer** — Raze Lighter y Bolt Caster como decisiones, no power-up.
5. **The Fold That Resists** — Mara sobrevive dentro de la tesorería sin controlarla.
6. **The Wounded Wish** — Riven, Quria y el costo diferido hacia Forsaken.
7. **Always Eager to Die** — Oryx/Savathun; despedida, doctrina, esclavitud de los Gusanos.

Fricción resuelta: esta parte justifica por qué King's Fall debe ser incursión hacia adentro. Oryx no vuelve físicamente a Sol; la Primera Escuadra tiene que entrar a su verdad.

### IV. Part 03 — The Kingslayer

Función: King's Fall como juicio y como malentendido central. Kyle cree refutar a Oryx; Oryx cree que Kyle lo validó.

Material fuente principal:
- `01_Timeline/Raids/KingsFall.md`
- `Guardian_Equipo_KingsFall_01_LaEntrada`
- `Guardian_Equipo_KingsFall_02_LosTotems`
- `Guardian_Equipo_KingsFall_03_ElSacerdote`
- `Guardian_Equipo_KingsFall_04_Golgoroth`
- `Guardian_Equipo_KingsFall_05_LasHermanas`
- `Guardian_Equipo_KingsFall_06_Oryx`

Capítulos candidatos:
1. **The Ship That Believed It Was a God**
2. **The Ones Who Stayed**
3. **A Truth That Needed Permission**
4. **Everything Power Leaves Behind**
5. **The King Who Needed Heirs**
6. **The Weight of a Wrong Answer**
7. **The Question He Left in the Room**

Fricción resuelta: Kyle no produce toda la respuesta por sí solo. Cada miembro de la Primera Escuadra debe encarnar una grieta en la Lógica de la Espada antes de que Kyle converja el sentido.

### V. Part 04 — The Rightful Pretender

Función: consecuencias y herencia. No cerrar la pregunta de Oryx; mostrar que la victoria abrió una sucesión que Kyle no entiende y no eligió.

Material fuente principal:
- `Guardian_Elsie_PostKingsFall`
- `Guardian_PostKingsFall`
- `Guardian_Elsie_PostKingsFall_ElToqueDelaMaldad`
- `Carina_Lena_KingsFall_SeisMesesEnFragmentos`
- bloque Taken King — Aftermath de `Plan_Jaden_Atheena_Origen.md`
- `Jaden_Atheena_TakenKing_LaPistaDeXur`
- `Carina_Jaden_Atheena_TakenKing_LoQueEncontraronEnElExilio`
- `Carina_Jaden_Atheena_TakenKing_ElRegresoYMalok`
- `Carina_Guardian_TakenKing_JustoATiempo`
- `Jaden_Eris_TakenKing_DarkDrinker`

Capítulos candidatos:
1. **The Touch of Malice** — la espada, el engrama, cargar sin reclamar.
2. **Six Months in Fragments** — Carina espera; Lena sigue siendo ausencia activa.
3. **The Trail of Xur** — Jaden/Atheena salen de Sol; ausencia convertida en ruta.
4. **What They Found in Exile** — Kepler; Carina encuentra una escuadra sin pedirla.
5. **The False Pretender** — Malok interpreta la sucesión de forma literal.
6. **Just in Time** — Carina salva a Kyle; no cierra su duelo, pero cambia su relación con llegar tarde.
7. **The Third Sword** — Dark Drinker y el puente hacia Rise of Iron.

Fricción resuelta: `The Rightful Pretender` ya no es "Kyle debería tomar el lugar de Oryx"; es la pregunta incorrecta rondando a todos. Malok es falso pretendiente explícito. Kyle es pretendiente solo desde una lectura que él no acepta. Carina interrumpe esa narrativa antes de que lo mate.

### VI. Coda opcional — The Shape That Remained

Función: cerrar el libro mirando hacia Heresy sin explicar Heresy. Puede ser una coda breve de Kyle, Ghost o Elsie con la sensación de que algo salió del Acorazado con ellos.

Guardrail: no nombrar el reclamo dormido como tal desde el POV de Kyle. No convertir la coda en tráiler. La mejor coda quizá sea íntima: Ghost preguntando qué pasa si el trono queda vacío, o Elsie notando que el mapa cambió de una forma que no sabe leer.

## Decisiones mínimas que Víctor tendría que fijar

1. Confirmar que **Book 02** se llama oficialmente **The King of Shapes**.
2. Confirmar si `Price of Vengeance`, `The Taken War`, `The Kingslayer` y `The Rightful Pretender` son las cuatro partes mayores.
3. Decidir si la carpeta raíz será `10_Books/` o si se reutilizará/renombrará el esquema ya mencionado de `10_Chapters/`.
4. Decidir si los títulos de capítulos se mantienen en inglés como los borradores originales, con cuerpo en español.
5. Decidir si `Part_04_The_Rightful_Pretender` incluye todo el Aftermath de Kepler/Malok/Dark Drinker o si ese bloque queda como interludio entre Book 02 y Book 03.
6. Decidir si el libro abre directamente con Eris/Osiris o con una apertura breve centrada en Oryx.
7. Definir el criterio de trazabilidad: cada capítulo final debería cerrar con `Fuentes integradas` o esa lista debería vivir solo en `01_Source_Index.md`.

## Lo que NO tocaría

- No movería ni renombraría las escenas fuente de `05_Dialogues/`.
- No eliminaría `01_Timeline/Age_II_The_Taken_King.md`; lo dejaría como mapa cronológico y lo enlazaría al libro cuando exista.
- No fusionaría Parte 1 y Parte 2: la primera es terror de mirada/cacería; la segunda es guerra de identidad.
- No haría que Carina entre a King's Fall; su exclusión ya tiene función y preserva la gramática de la Primera Escuadra.
- No adelantaría el reclamo dormido ni lo volvería consciente para Kyle.
- No convertiría a Malok en clímax rival de Oryx; su valor es resolutivo y emocional, no cósmico.
- No descartaría los nombres originales: los rescataría como arquitectura interna del libro.

**Estado:** lista para triage.

