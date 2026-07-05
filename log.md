# Log de Sesiones — Destiny: Renewed Fate

Bitácora de trabajo por sesión. Registra qué se hizo, qué se creó o modificó, y qué quedó pendiente. No es retroactiva — las sesiones anteriores a 2026-06-04 están documentadas en el sistema de memoria del proyecto.

---

## Sesión 2026-07-04 — La Familia Elegida · El Torneo de los Velocistas (infraestructura)

Sesión de diseño narrativo (brainstorm → estructura), no de prosa. Objetivo: expandir la dinámica familiar Kyle/Elsie/Sai (+Ghost como testigo y parte) en la ventana Season of the Lost → Final Shape, usando los eventos anuales de la Ciudad (Aurora, Festival de las Almas Perdidas, Solsticio, Juegos de los Guardianes) y la SRL como territorio poco explorado del vault.

**CREADOS:**

- `08_Core_Relationships/La_Familia_Elegida.md` — el cuarto documento de relaciones fundamentales (faltaba el cuarteto). La historia de la frase de la lápida de Elsie ("El hogar que elegimos"): los cuatro roles (eco paterno / norte / hija elegida / testigo y parte), los rituales con su estado (nombres ✅; "¿comiste?" y "los jueves" ⏳ pendientes de escena de origen — deudas que el PostFinalShape ya cobra), el calendario anual como vara de medir (progresión de tres fases: incómodo → pleno → interrumpido), la geometría táctica de la familia en combate (precedente: `Elsie_FinalShape_LaHuida`), los tres hilos propios de Ghost, y 5 reglas de escritura (anti-utilería elevada a regla familiar; "la alegría se escribe dorada, la Tinta cobra sola").
- `04_Concepts/Torneo_De_Los_Velocistas.md` — el mundial de la SRL, con las especificaciones del autor: ciclo bienal (año de clasificatorias amistosas + año eliminatorio), título vitalicio **"El Velocista de Sol"**, final tradicional en la Aurora. Distinción SRL (liga viva) vs Torneo (mundial). Reglas de pista: sin Luz (la humanidad compite, no la paracausalidad), la máquina manda (mecánica = Saber Heredado de Amanda), Ghost copiloto (único rol donde no es resucitador — su arco: aprender a acompañar a Kyle a perder). **Arco de Kyle en 8 fases:** espectador con la Primera Escuadra (Age I) → no clasifica el año que mata a un rey (TTK) → Efrideet le da permiso de querer algo que no salva a nadie (RoI) → suspensión por la Guerra Roja, gradas llenas de fantasmas (Age V) → revivido con Amanda tras la muerte de Cayde ("traigan de vuelta el torneo que hace que todos vuelvan a vivir… sobre todo en el podio") como forma de duelo, no evasión (Forsaken) → clasifica y cae en 1ª ronda con Elsie recién ida; Amanda: "no lo trajimos de vuelta para ganar" (Shadowkeep) → madurez: mejores tiempos del sistema, Elsie de vuelta, Sai lo conoce como "el favorito" (Beyond Light/Año de la Bruja) → **campeón en la Aurora de Seraph, semanas antes de Lightfall** — su primer logro personal, auténtico y suyo. La Tinta: Amanda muere en Defiance; el trofeo se resignifica solo; el Torneo V nunca se corre — "el campeón que nunca defendió la corona". Semillas por confirmar: Marcus Ren como rival, nombre del colibrí, vuelta de honor post-Defiance, Torneo V post-saga.
- `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` — hoja de ruta priorizada: P1 deudas directas (primera Aurora familiar/"¿comiste?", origen de "los jueves", Festival Sai↔Ghost/beat 4, Amanda post-Cayde, la final), P2 historia del torneo + colisiones (gradas Age I, Efrideet, 1ª ronda perdida, **Sai conoce a los Bray en Seraph**, atraco de Plunder, ronda de Haunted), P3 color y cobros (Juegos de los Guardianes, Solsticio, Aurora interrumpida, vuelta de honor). Decisiones abiertas y fichas obligadas listadas.

**MODIFICADOS:** `INDEX.md` (entrada en Core Relationships + entrada en Major Concepts), `log.md`, `CLAUDE.md` (estado del vault).

**Continuación — 3 decisiones resueltas:**

- **CREADO** `02_Characters/Rook.md` — rival de Kyle en el torneo (ficha provisional). Humano, showman, campeón del Torneo III; lo elimina en su primera ronda (Shadowkeep) y pierde ante él la final del Torneo IV. Diseño: espejo torcido de Kyle — el mismo vacío de infancia inexistente ("nadie me enseñó nada"), resuelto como mito solitario en vez de familia elegida; no es villano, no necesita redención; la fricción es la misma herida respondida en direcciones opuestas. Beat de cierre: reconoce la maniobra de Amanda en el movimiento ganador de Kyle ("—Alguien te enseñó eso. —Sí.") y se queda sin réplica por primera vez en público.
- **Nombre del colibrí confirmado:** "La Línea Alterna" — doble sentido (alternativa al Gorrión / línea temporal alterna, eco de Elsie). Bautizado retroactivamente en `Guardian_Elsie_PreShadowkeep.md` (anotación añadida al pie del archivo existente; prosa original intacta) — esa escena ya escrita es ahora el origen silencioso del skimmer campeón.
- **"La vuelta que nunca corrió" aclarada:** NO es la ceremonia oficial de campeón (esa se cancela — la guerra final se traga el Torneo V, segundo eco de la Guerra Roja); es la vuelta privada que Kyle se da solo, sin cámaras, en La Línea Alterna, como duelo físico por Amanda. Distinguida explícitamente del Torneo V *post-saga* (ese sigue abierto y especulativo, sin nada escrito).

**MODIFICADOS (continuación):** `04_Concepts/Torneo_De_Los_Velocistas.md` (secciones de Rook, La Línea Alterna, La vuelta que nunca corrió; tabla y arco de 8 fases actualizados con Rook nombrado), `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_PreShadowkeep.md` (anotación de pie), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (decisiones resueltas vs. abiertas), `INDEX.md` (Rook en Main Characters; entrada del Torneo actualizada).

**Continuación 2 — ficha de Amanda + estructura del bracket + Torneo V cerrado como hilo implícito:**

- **CREADO** `02_Characters/Amanda_Holliday.md` — ficha completa. Mecánica jefe de la Ciudad, fuente del primer Saber Heredado de Kyle ("no se aprende mirando, Guardián, se aprende ensuciándose"), co-fundadora del torneo revivido tras Cayde, pareja de Crow ("la puerta que no vuelve a abrirse" — cruza su muerte con el arco de Sai vía `Sai_Crow_PostFinalShape_LaPuertaQueSigueAbierta`). Muere Age XIII (Defiance); su muerte resignifica el trofeo de Kyle retroactivamente.
- **DISEÑADA la estructura del bracket** en `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva sección "La estructura — cómo funciona el bracket"): Año 1 (Tabla de Marcas) usa el formato de heats multitudinarios de la SRL de siempre, 4 paradas mapeadas a las 4 temporadas de Age IX (Hunt/Chosen/Splicer/Lost), puntos acumulados, cierre con Los Dieciséis sembrados 1-16. Año 2 (el Cuadro) cambia a duelos 1-contra-1 — el giro de formato que hace que se sienta mundial y no liga —, siembra estándar de torneo (1v16, 2v15…, los dos mejores sembrados aislados en polos opuestos para solo cruzarse en la final), mejor de 3 por ronda (final mejor de 5), 4 rondas con nomenclatura de mundial de fútbol (Octavos/Cuartos/Semifinal/Final) mapeadas a Risen/Haunted/(Plunder queda libre, sin ronda)/Seraph. La regla de siembra explica sola, sin forzar nada, por qué Kyle y Rook se cruzan en primera ronda del Torneo III (Kyle sembrado bajo vs. Rook sembrado alto) y solo en la final del Torneo IV (ambos sembrados altos, polos opuestos).
- **Torneo post-saga cerrado como hilo implícito, no como decisión pendiente:** a petición explícita del autor, no se desarrolla por ahora — queda mencionado como algo que "sigue pasando, en algún lado" sin necesidad de narrarlo; se retoma si algún día se decide montarlo.

**MODIFICADOS (continuación 2):** `04_Concepts/Torneo_De_Los_Velocistas.md` (sección de estructura + ajuste de la sección final de hilo abierto), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (fichas resueltas, estructura del bracket anotada, Torneo V movido a "cerrado/implícito"), `INDEX.md` (entrada de Amanda Holliday).

**Continuación 3 — fase de grupos + participación abierta:**

- **Fase de grupos añadida** al torneo, a petición del autor (más cercano al Mundial real que un bracket puro): el corte de la Tabla de Marcas pasa de 16 a **32 clasificados** ("Los Treinta y Dos"), que se reparten en **8 grupos de 4** (sorteo público, primeros 8 sembrados repartidos uno por grupo); todos contra todos dentro del grupo (3 carreras por piloto); avanzan los 2 primeros de cada grupo, re-sembrados 1-16 para entrar al Cuadro (que conserva el diseño ya hecho: Octavos/Cuartos/Semifinal/Final). Para el Torneo IV, los grupos corren durante la campaña de Witch Queen (Age X); el Cuadro, durante Age XI. El arco de Kyle se ajustó en consecuencia (Torneo III: sobrevive su grupo raspando, cae en Octavos ante Rook; Torneo IV: gana su grupo con comodidad antes de la racha hasta la final).
- **Participación abierta:** civiles + Guardianes desde el Torneo I (refuerza la regla "sin Luz" — la prueba en vivo de que sin paracausalidad todos compiten igual); Eliksni (Casa de la Luz) y Cabal (Imperio de Caiatl) desde el Torneo IV — el título de Kyle se vuelve también, sin que nadie lo declare con solemnidad, **el primer campeonato multiespecie de la Ciudad**. Decisión de diseño: Rook se mantiene Guardián (no se retoca su ficha ya escrita); la puerta a civiles queda para un personaje nuevo (escena 18 del plan, pendiente).

**MODIFICADOS (continuación 3):** `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva sección "Quién puede competir"; estructura reescrita en 3 fases; tabla histórica y arco de 8 fases actualizados), `02_Characters/Rook.md` (aclarado como Guardián), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (2 escenas nuevas: el sorteo, el civil que llegó lejos; estructura actualizada), `INDEX.md` (entrada del Torneo actualizada).

**Continuación 4 — el torneo crece para las nuevas especies + consulta de Escuadras de Tres (sin implementar):**

- **Formato expandido a partir del Torneo IV:** a petición del autor, el ingreso de eliksni y cabal no se resuelve con cupos aparte — el torneo entero crece. Tabla de Marcas pasa de 32 a **64** clasificados; grupos de 8 a **16** (de 4 pilotos cada uno); el Cuadro de 16 a **32**, ganando una ronda extra al frente: **Dieciseisavos de Final** (32→16), antes de Octavos→Cuartos→Semifinal→Final (5 rondas en vez de 4). Filosofía explícita, ligada directamente a Kyle: "se agranda el molde, no se encoge a nadie para que quepa" — la misma regla de la familia elegida, ahora institucional. Torneos I–III conservan el formato clásico de 32/8-grupos/Cuadro-de-16 sin cambios. Mapeo temporal del Torneo IV ajustado: Dieciseisavos cierra la fase de grupos al final de Witch Queen (Age X); Octavos y Cuartos caen en Risen; Semifinal en Haunted; Plunder libre; Final en Seraph/Aurora, sin tocar ninguno de esos beats ya fijados.
- **Consulta respondida, sin implementar:** el autor preguntó si el Cuadro debería pasar de duelos 1-contra-1 a **3v3**, para sumar más diversidad. Se dio opinión (no se escribió en el vault): un 3v3 puro con título compartido diluye el logro personal de Kyle ("nadie fue salvado, nadie se lo debía") y el duelo directo con Rook. Se propuso un híbrido — **Escuadras de Tres** al estilo ciclismo de ruta (un líder cuyo resultado decide el duelo y el título + 2 compañeros tipo domestique que bloquean/abren estela/sacrifican posición) —, apoyado en un detalle físico que ya existía en el lore (la línea de energía cinética del skimmer en `Guardian_Elsie_PreShadowkeep` funciona como estela/drafting). **Pendiente de confirmación del autor antes de escribirlo en el documento.**

**MODIFICADOS (continuación 4):** `04_Concepts/Torneo_De_Los_Velocistas.md` (secciones "Qué es", "Quién puede competir", "La estructura" reescritas con los dos tamaños; tabla histórica y arco de Kyle fase 8 actualizados), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (estructura + consulta de Escuadras de Tres anotada como pendiente), `INDEX.md` (entrada del Torneo actualizada).

**Continuación 5 — decisión final: el torneo se corre por equipos de tres, no 1-contra-1 ni domestique:**

- **El autor decidió** (más allá de la propuesta híbrida de "Escuadras de Tres" tipo domestique) que el torneo entero pasa a ser de **equipos de tres, triunfo colectivo genuino** desde el Torneo III — la SRL diaria se queda individual, el Torneo mundial se vuelve de equipos, y esa diferencia de formato ES la razón por la que el Torneo se siente distinto de la liga de siempre. Razón explícita del autor: el triunfo *individual* de Kyle ya está resuelto (su cabaña con Elsie); el torneo es mejor como triunfo *colectivo* — más Kyle, porque compartir la victoria la vuelve mejor que ganarla solo. Bono: esto ablanda la derrota temprana de Shadowkeep (un año ya denso por la partida de Elsie) al no dejar a Kyle solo también en el fracaso.
- **El equipo de Kyle:** él + **[[02_Characters/Jaden]]** + **[[02_Characters/Carina]]** — su núcleo permanente desde después de la Guerra Roja, no fichajes nuevos. Kyle simplemente les pregunta si quieren correr con él (Age VI, Forsaken) y la respuesta nunca estuvo en duda. El mismo trío pierde en Shadowkeep (Torneo III) y gana en la Aurora de Seraph (Torneo IV) — la continuidad es el punto: ganan porque siguieron siendo los mismos tres, no porque cambiaron de compañeros tras perder.
- **Título renombrado:** "El Velocista de Sol" (singular) → **"Los Velocistas de Sol"** (plural) — el trofeo pertenece a los tres.
- **Origen del formato, ligado explícitamente a Kyle:** el formato de equipos nace con la revivificación (Torneo III) como decisión conjunta de Amanda y Kyle, eco directo de **"Nadie vuelve solo"** — el lema de la Primera Escuadra que la Guerra Roja le arrebató (ver [[08_Core_Relationships/Primera_Escuadra]]). Cierra un círculo entre el documento de relaciones más viejo del vault y el más nuevo.
- **Contraste con Rook:** su equipo es talento contratado, nunca la misma alineación dos torneos seguidos — el reflejo exacto de su filosofía de "nadie me enseñó nada, no le debo nada a nadie" aplicada a cómo trata a su propia gente. La final del Torneo IV es, literalmente, familia elegida contra nómina.
- **Ghost, Sky y Hornet** ahora comparten canal de carrera como copilotos del equipo completo, no solo Ghost para Kyle.

**MODIFICADOS (continuación 5):** `04_Concepts/Torneo_De_Los_Velocistas.md` (reescritura completa — nuevo, no parche: intro, "Qué es", nueva sección "Por qué es un torneo de equipos", nueva sección "El equipo de Kyle", estructura en lenguaje de equipos, tabla histórica, arco de 8 fases, Amanda, Rook, "La familia en el torneo", "Por qué importa", decisiones resueltas), `02_Characters/Rook.md` (nueva sección "Su equipo" — talento contratado, contraste), `02_Characters/Amanda_Holliday.md` (entrena a los tres), `02_Characters/Jaden.md` y `02_Characters/Carina.md` (nueva sección "El Torneo de los Velocistas" en cada una), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escenas 4/5/8 actualizadas, decisión resuelta), `INDEX.md` (entrada del Torneo reescrita).

**Continuación 6 — el bracket del Torneo IV, poblado con nombres:**

- **CREADO** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` — mapa de personajes del torneo que gana Escuadra Cero (nombre propio del equipo de Kyle, elegido en Age VI, chiste privado sobre "empezar de cero" que anticipa sin saberlo la frase de Sai en `El Lobo Más Joven`). Alcance acotado a propósito: no se nombran los 64 equipos, solo el camino real de Kyle — 3 rivales de grupo (Manada Gris, veteranos deportivos; Doble Filo, rivalidad cómica; Casa Nueva, el primer trío mixto eliksni-humano-cabal, comidilla de la Ciudad) y 5 rivales de eliminatoria (Los Graneros en Dieciseisavos — tres hermanos civiles de granja que casi eliminan a Escuadra Cero, la prueba en vivo de "sin Luz" dentro del propio camino de Kyle; Los Chacales en Octavos, tácticas sucias; Legado en Cuartos, capitaneado por Rendel, que lleva el emblema no oficial de la Primera Escuadra por los memoriales que visitó de novato — sorpresa emocional de bajo costo; Punta de Lanza en Semifinal, deliberadamente sin personalidad porque el drama de esa ronda es interno; Torre en la Final, el equipo de Rook con dos pilotos contratados casi intercambiables, Vray y Vess). Más color sin cruce con Kyle (Grupo de la Muerte, Guardia de Acero — primer equipo enteramente cabal). Solo Toma Aldrei (Los Graneros) y Rendel (Legado) marcados como candidatos a ficha ligera si sus escenas se escriben; el resto son pasajeros deliberados.

**MODIFICADO (continuación 6):** `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 17 ligada a Casa Nueva; escena 18 reescrita como "Dieciseisavos — Los Graneros" con nombres concretos; nueva escena 19 "Cuartos — Legado"; nueva sección enlazando el bracket).

**Continuación 7 — la tensión del bracket ("vivir al filo del sillón"), a petición del autor:**

- **Diseñado el mecanismo de tensión** que evita que el Torneo IV se sienta como una racha cómoda de victorias. Kyle nunca está seguro: carga el miedo real de repetir Shadowkeep, y repite un mantra frágil, no una certeza — *"tal vez no es imposible, si estamos en sincronía esta vez."*
- **Nuevo equipo: Sincronía** — trío Awoken criado junto desde niños en el Arrecife, terroríficamente sincronizado, en el mismo cuadrante del bracket que Escuadra Cero. No es rival de ego como Rook: es la prueba viva de la propia duda de Kyle (¿de verdad estamos en sincronía, o no todavía?). Cae en Octavos ante **Legado** (Rendel), un vuelco que nadie esperaba — y esa es la escena de "mirar el marcador ajeno" por excelencia: Escuadra Cero sigue el resultado por transmisión desde su garaje, sin poder hacer nada, sabiendo que ese resultado decide a quién enfrentan en Cuartos.
- **Tensión invertida en Semifinal — el susto de Rook:** mientras Escuadra Cero cierra su propia semifinal, el equipo de Rook (Torre) casi cae ante **Guardia de Acero** (la guardia de honor de Caiatl, resignificada de simple color a rival real), forzando una tercera carrera decisiva. Escuadra Cero lo sigue temiendo, invertido, que Rook PIERDA — necesitan que el reencuentro sea real, no un título ganado contra un desconocido. Rook sobrevive por muy poco.
- Ambos equipos llegan a la Final habiendo sobrevivido su propio susto — el resultado se siente ganado, no regalado, para los dos lados.

**MODIFICADOS (continuación 7):** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (nueva sección "La tensión del cuadro — vivir al filo"; Sincronía añadida; Cuartos/Semifinal/Final reescritos con el nuevo hilo; Guardia de Acero resignificada; nuevo resumen de "dónde vive la tensión"), `04_Concepts/Torneo_De_Los_Velocistas.md` (fase 8 del arco de Kyle reescrita para quitar "con comodidad"; nueva regla de tono "Kyle nunca está seguro" en *Por qué importa*), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (2 escenas nuevas: 20 "Mirando el marcador — Sincronía cae", 21 "El susto de Rook").

**Continuación 8 — dos escenas escritas: el origen del arco del torneo:**

- **CREADA** `05_Dialogues/Dialogue_Guardian/Guardian_Cayde_TorneoI_TodoMenosEso.md` — Age I, no estaba en el plan original; surgió por pedido explícito del autor como la escena que siembra todo lo demás. Kyle, recién resucitado, ve la final del Torneo I desde las gradas con la Primera Escuadra y se escabulle a hablar con Cayde a solas; le pregunta qué se sentiría ganar la copa. Cayde: *"todo es posible... menos burlar la muerte de verdad — la que no vuelve"* (referencia velada a [[04_Concepts/The_Gardener_and_Winnower]], contada como leyenda de bar, no como lore confirmado) — y la enseñanza que Kyle guarda ocho años: un sueño sin gloria sí se puede perseguir hasta volverlo real, si de verdad se persigue. Ironía dramática deliberada: Cayde no sabe que describe su propia muerte futura.
- **CREADA** `05_Dialogues/Dialogue_Guardian/Guardian_Amanda_Forsaken_TraiganDeVueltaElTorneo.md` — escena 4 del plan, Age VI post-Cayde. Kyle llega al hangar de Amanda; ella ordena equipo de la SRL sin tocar desde la Guerra Roja; él le cuenta, por primera vez en voz alta, la vieja conversación con Cayde en el Torneo I — el estandarte descolorido con un sol se la trae de vuelta. Amanda pronuncia la frase de Cayde ("traigan de vuelta el torneo... sobre todo en el podio"); Kyle propone el formato de equipos citando **"Nadie vuelve solo"** (Primera Escuadra); nace **Escuadra Cero** al final, nombre que sale de un chiste de Kyle sobre no tener linaje ("empezamos de cero") — sin que ninguno de los tres sepa cuánto va a pesar ese nombre después. Cierra el círculo con la escena de Torneo I: la pregunta de un niño-Guardián por fin encuentra qué perseguir.

**MODIFICADOS (continuación 8):** `INDEX.md` (nueva sección "Torneo I — la copa que aún no existe" en Dialogue_Guardian; entrada nueva en "Forsaken"), `02_Characters/Amanda_Holliday.md` (Aparece en actualizado), `02_Characters/Jaden.md` y `02_Characters/Carina.md` (enlace a la escena en su sección del Torneo), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 4 marcada como escrita).

**Continuación 9 — el Lumen, moneda de la vida ordinaria:**

- **CREADO** `04_Concepts/Lumen.md` — a partir del detalle de la apuesta de Resner y Joe en `Guardian_Cayde_TorneoI_TodoMenosEso`. Glimmer es la moneda de la guerra (residuo paracausal, economía formal de la Vanguardia); Lumen es la de la vida ordinaria — comida callejera, propinas, apuestas amistosas, entradas del Torneo — inventada por gente corriente sin tocar la Luz. Ironía de nombre deliberada: se llama como la unidad de luz y es la única moneda del sistema que no tiene nada que ver con ella. El Torneo de los Velocistas corre casi enteramente en Lumen — "sin Luz" en la pista, "sin Glimmer" en su economía, dos formas de decir lo mismo.
- **MODIFICADA** `Guardian_Cayde_TorneoI_TodoMenosEso.md` — apuesta de Resner/Joe nombrada en Lumen; nueva línea de Cayde haciendo sonar un puñado de Lumen y comentando "ni un gramo de Glimmer en toda la tarde. Nadie aquí le debe nada a la Luz" — refuerza el tema sin alargar la escena.

**MODIFICADOS (continuación 9):** `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva línea "La economía" en *Qué es*; footer actualizado), `INDEX.md` (entrada nueva en Major Concepts).

**Continuación 10 — el trofeo, diseñado:**

- **Nueva sección "El trofeo — el disco de tres piezas"** en `04_Concepts/Torneo_De_Los_Velocistas.md`. Diseño acordado con el autor: un disco-sol del tamaño de un plato, construido por Amanda (no un orfebre) con piezas recicladas de motor —aros de propulsor, placas de blindaje cortadas en cuñas—, sin pulir del todo. **Se desarma en tres piezas**, una por integrante del equipo, y solo forma el sol completo cuando los tres las juntan — literaliza "nadie gana solo" en el objeto mismo. Cada ciclo, el equipo campeón graba sus nombres en un rayo nuevo (el disco acumula historia física, como anillos de árbol); Kyle, al sostenerlo por primera vez, lee "Rook · Vray · Vess — Torre" del ciclo anterior. Por eso termina en la cocina y no en una vitrina: es un objeto para armar sobre la mesa cuando los tres cenan juntos, no para exhibir.

**MODIFICADOS (continuación 10):** `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva sección; línea de "El premio" actualizada), `INDEX.md` (entrada del Torneo con el detalle del trofeo).

**Continuación 11 — Andal Brask entra a la cadena de herencia:**

- **MODIFICADA** `Guardian_Cayde_TorneoI_TodoMenosEso.md` — la línea de Cayde sobre las "historias de antes de todo esto" ahora se atribuye explícitamente a **Andal Brask**, su predecesor como Vanguardia Cazador, muerto a manos de Taniks — Cayde raramente habla de él, y aquí lo hace en el mismo registro serio que reserva para lo que no convierte en broma. Construye una **cadena de herencia de tres eslabones**: Andal le cuenta la historia a Cayde; Cayde se la cuenta a Kyle; ninguno de los dos, al contarla, sabe que está describiendo su propia muerte futura.
- **AÑADIDA** sección "Andal Brask" en `02_Characters/Cayde-6.md` — nota breve sobre quién fue, cómo murió, y el origen de la historia del jardín/el que poda.

**MODIFICADOS (continuación 11):** `05_Dialogues/Dialogue_Guardian/Guardian_Cayde_TorneoI_TodoMenosEso.md` (diálogo + pie de página), `02_Characters/Cayde-6.md` (nueva sección), `INDEX.md` (entrada actualizada).

**Continuación 12 — escena 1 escrita: la primera Aurora familiar:**

- **CREADA** `05_Dialogues/Dialogue_Sai/Sai_Familia_Seraph_LaPrimeraAurora.md` — escena 1 del plan. Resuelta primero una duda de cronología planteada por el autor: ¿no ocurre la Aurora antes de Sai? Se verificó `Guardian_Elsie_Splicer_LaAurora` (la Aurora de Splicer, donde Kyle le da a Elsie la Estrella Polar) — esa es la Aurora ANTERIOR, en Splicer, antes de que Sai exista en la historia (se rescata hasta Lost). La nueva escena es la Aurora SIGUIENTE, dentro de Season of the Lost. Se ubicó con precisión entre `Las Manos Recuerdan` (primer encuentro Kyle-Sai) y `Una Noche Cualquiera` (donde Elsie bebe por primera vez de la taza) para que la pregunta de Sai sobre por qué Elsie no bebe siga siendo válida sin contradecir esa escena posterior.
  - Contenido: la cabaña decorada con luces doradas; el poncho de Elsie y la chamarra de piel de borrego de Kyle en el mismo perchero; la tercera taza en la alacena, comprada por Elsie sin anunciarlo; Ghost con un gorro navideño imposible que ninguna vuelta logra tirar, contando historias de antes de encontrar a Kyle — incluida la vez que se preguntó si sería de los Espectros que nunca encuentran Guardián; Elsie sobre las celebraciones de la Edad de Oro; Kyle sobre el Torneo de los Velocistas, con la clasificación de Escuadra Cero dependiendo en parte del resultado de otro equipo (siembra temprana del mecanismo "vivir al filo" incluso en el Año 1); Sai pregunta si esto pasa cada Aurora — los tres coinciden en que no, que antes tenían un lugar que llenar y ahora un sitio al que llegar; cierra con Elsie y Sai a solas explicando por qué la taza de Kyle sigue sin beberse ("sostenerla ya es la parte que quiero").

**MODIFICADOS (continuación 12):** `INDEX.md` (nueva sección "Season of the Lost — la primera Aurora" en Dialogue_Sai), `02_Characters/Sai.md` (Aparece en actualizado), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 1 marcada como escrita).

**Continuación 13 — precursora del origen de "los jueves":**

- **CREADA** `05_Dialogues/Dialogue_Sai/Sai_Escuadra_WitchQueen_ElDiaQueComparten.md` — no estaba en el plan original, surgió a partir de una idea del autor (cumpleaños de Kyle, coincidiendo con el de Carina). Ubicada entre `Las Manos Recuerdan` y `La Primera Aurora`. Contenido: Kyle, Jaden y Carina practican puntería con habilidades cuerpo a cuerpo contra latas en un arroyo (Elsie está en Europa ayudando a Ana); Sai llega con un encargo oficial de Mara, pero se distrae al preguntar genuinamente "¿qué es un cumpleaños?" — su primer encuentro real con Jaden y Carina. Descubre que Kyle y Carina renacieron el mismo día (**nuevo detalle de canon**, sin conflicto con nada existente — verificado contra `Kyle_ElDespatar` y la ficha de Carina, ninguno fija una fecha previa). Se queda a escuchar ambos renacimientos, y descubre que los miércoles de ramen ya son ritual fijo de la escuadra desde años atrás. **Función estructural:** siembra el precedente para la escena 2 del plan ("El origen de los jueves", todavía sin escribir) — establece que los miércoles pertenecen a la escuadra completa, dejando el jueves libre para nacer después como día propio de Kyle y Sai específicamente.

**MODIFICADOS (continuación 13):** `INDEX.md` (nueva sección "Season of the Lost — el día que comparten"), `02_Characters/Sai.md`, `02_Characters/Carina.md` (nueva sección "El mismo día que Kyle"), `02_Characters/Jaden.md` (nueva sección "Sai — el primer encuentro"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 1b añadida; escena 2 actualizada con la nueva información).

**Continuación 14 — escena 2 escrita: el origen de "los jueves":**

- **CREADA** `05_Dialogues/Dialogue_Sai/Sai_Guardian_WitchQueen_LosJueves.md` — escena 2 del plan, ya informada por la 1b (los miércoles son de la escuadra completa; los jueves debían ser otra cosa). Tres viñetas cortas: (1) Sai llega sin avisar un jueves cualquiera con una pregunta que podía esperar, encuentra a Kyle cocinando para uno (Elsie está en el Arrecife) y se queda; (2) vuelve el jueves siguiente sin excusa preparada, y Kyle ya tiene dos platos servidos sin comentarlo; (3) semanas después, con Witch Queen acercándose y Kyle con la cabeza en tres cosas a la vez, se le olvida casi del todo — Sai, a punto de irse por su vieja costumbre de no imponer, dice "es jueves" en voz baja, y Kyle enrolla el mapa del Mundo Trono y se sienta. **Decisión de diseño:** quien defiende el ritual es Sai, no Kyle — su arco "de víctima a recurso por elección" hecho costumbre doméstica, en vez del gesto más obvio de que el padre sea quien insiste. El apodo "lobito" (que nace después, en Risen, ver *El Lobo Más Joven*) se pega encima de un día que ya era sagrado sin nombre — explica por qué el callback final ("Los jueves, lobito") funde dos cosas nacidas por separado.

**MODIFICADOS (continuación 14):** `INDEX.md` (nueva sección "Season of the Lost — los jueves"), `02_Characters/Sai.md` (Aparece en actualizado), `08_Core_Relationships/La_Familia_Elegida.md` (tabla de rituales: "¿comiste?" y "Los jueves" marcados ✅ Escrito), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 2 marcada como escrita).

**Continuación 15 — corrección de continuidad: mismo día, mismo año:**

- El autor precisó que Kyle y Carina no solo comparten el día de renacimiento, sino el **mismo año** — Kyle de día en el Cosmódromo, Carina esa misma noche en un rascacielos del Viejo Chicago. Al verificar, `05_Dialogues/RenacimientosGuardianes/Carina_ElDespatar.md` (escena ya establecida) decía "esa misma noche... un Guardian despertaba en el Cosmódromo" — contradecía la nueva precisión (implicaba que Kyle también despertó de noche). **Corregido**: se ajustó esa línea a "ese mismo día, horas antes... había despertado a plena luz", y la línea de resumen a "el mismo día, el mismo año, con horas de diferencia entre la luz y la noche". Se propagó el ajuste a `Sai_Escuadra_WitchQueen_ElDiaQueComparten.md` (diálogo de Carina/Kyle actualizado: "mismo día, mismo año... a mí de día, ella de noche") y a la sección "El mismo día que Kyle" en `02_Characters/Carina.md`.

**MODIFICADOS (continuación 15):** `05_Dialogues/RenacimientosGuardianes/Carina_ElDespatar.md`, `05_Dialogues/Dialogue_Sai/Sai_Escuadra_WitchQueen_ElDiaQueComparten.md`, `02_Characters/Carina.md`.

**Continuación 16 — reestructuración cronológica: el calendario anual fechado, mes a mes:**

El autor pidió mover las tres escenas de Sai en la cabaña (El Día Que Comparten, Los Jueves, La Primera Aurora) de "Season of the Lost" a un calendario anual completo dentro del año de Witch Queen, con fechas concretas: cumpleaños en **febrero**, Juegos de los Guardianes en **marzo**, Solsticio en **junio**, Almas Perdidas en **octubre**, Aurora en **diciembre**. Esto encajó perfecto con el mapeo de temporadas ya existente para Age XI (Risen≈marzo, Haunted≈junio, Plunder≈octubre, Seraph≈diciembre) — pero generó un conflicto real: diciembre/Seraph ya estaba ocupado por la final del Torneo IV, ya escrita. Se resolvió con el autor vía pregunta directa: **La Primera Aurora es ahora la víspera de la final** (no una celebración genérica), con dos beats nuevos del autor — Elsie toma la mano de Kyle sin palabras; Sai lo lee sin necesitar el don y promete sostenerlo desde las gradas pase lo que pase, note importe el resultado.

Esto disparó una cascada de correcciones de continuidad, todas resueltas:
- **Los tres archivos renombrados** (de `SeasonLost` a `WitchQueen`/`Seraph`): `Sai_Escuadra_WitchQueen_ElDiaQueComparten.md`, `Sai_Guardian_WitchQueen_LosJueves.md`, `Sai_Familia_Seraph_LaPrimeraAurora.md`.
- **"La Primera Aurora" reescrita completa:** ya no es la primera fiesta de Sai con la familia (eso sigue siendo cierto de *El Día Que Comparten*, febrero) — es su primera **Aurora** específicamente, al cierre de un año entero de rituals ya vividos (cumpleaños, jueves, Juegos, Solsticio, Almas Perdidas). Se corrigieron en cascada: la "tercera taza recién comprada esa semana" → ya asentada desde hace casi un año; "apenas encontrando su dinámica como familia" → familia ya establecida; el diálogo de Kyle sobre el torneo (antes lenguaje de clasificación, Año 1) → ahora es la víspera de la final; el final de la escena (Elsie explicando por qué no bebe de la taza) → **contradecía "Una Noche Cualquiera"** (donde ya bebe, fechada meses antes) — se reemplazó por un beat de callback: Sai ve a Elsie beber con normalidad y pregunta "¿qué cambió?", cobrando esa escena en vez de repetirla.
- **"Los Jueves" ajustada:** de "antes de que empiece la campaña" a "durante la campaña, semanas después del cumpleaños"; el lenguaje del torneo (antes "última parada de clasificación", Año 1) corregido a "sorteo de grupos" (Año 2, que corre durante la campaña de Witch Queen según ya establecía el propio documento del Torneo).
- **`La_Familia_Elegida.md`:** tabla del calendario reescrita con meses y temporadas exactos, cada evento enlazado a su escena (escrita o pendiente).
- **`Torneo_De_Los_Velocistas.md`:** nuevo enlace cruzado a la víspera de la final.
- Propagado a `INDEX.md` (tres secciones reubicadas cronológicamente: "Witch Queen — el calendario de la familia" en febrero-marzo, "Season Seraph — la víspera de la final" en diciembre), `Sai.md`, `Carina.md`, `Jaden.md`, `Plan_Escenas_Familia_Elegida.md`.

**MODIFICADOS (continuación 16):** los tres archivos de escena (renombrados + reescritos parcial o totalmente), `08_Core_Relationships/La_Familia_Elegida.md`, `04_Concepts/Torneo_De_Los_Velocistas.md`, `INDEX.md`, `02_Characters/Sai.md`, `02_Characters/Carina.md`, `02_Characters/Jaden.md`, `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md`.

---

## Sesión 2026-07-05 — Los Juegos de los Guardianes (segundo evento del calendario escrito)

**CREADA:** `05_Dialogues/Dialogue_Sai/Sai_Familia_Risen_LosJuegosDeLosGuardianes.md` — marzo, Season of the Risen, tercer evento del calendario anual de la familia. Diseñado en colaboración con el autor a través de varias iteraciones antes de escribir:

- **Corrección de formato:** el autor aclaró que los Juegos de los Guardianes no son la SRL — son Asaltos, Operaciones y, el más salvaje, el Crisol (estilo "olimpiadas" institucionales).
- **Ajuste clave del autor:** las escuadras son del **mismo tipo de clase** (no mixtas) — un trío de Hechiceros (Kyle), uno de Cazadores (Carina), uno de Titanes (Jaden) — y esto, retroactivamente, les enseña a los Guardianes por qué la variedad de clase importa en operaciones reales: tres Pozos de Radiancia es redundancia de curación sin cierre; tres Pistolas de Oro es un camión arrollador sin cobertura; solo mezclados (como en la Operación conjunta de Kyle y Carina esa misma tarde) son de verdad imparables.
- **El foco de la escena**, propuesto y confirmado con el autor: no es quién gana, es qué hace segura la intensidad. Kyle y Carina —dupla perfecta en Operaciones reales, dos huracanes colisionando en el Crisol— desconciertan a Sai, que no entiende cómo ambas cosas pueden ser ciertas. Elsie se lo reencuadra: nacieron el mismo día (Kyle de día en el Cosmódromo, Carina esa noche en Chicago), y soltarse del todo solo es posible contra alguien de quien sabes que no se rompe — la intensidad no es a pesar de la confianza, es la prueba de que aguanta.
- **Resultado:** el trío de Carina gana el Crisol por el margen mínimo, en el partido más cerrado del día; el trío de Jaden gana el estandarte de clase del año entero por acumulación silenciosa, sin un solo momento memorable — coherente con quien es. **Sai encuentra su propio lugar:** no puede competir (no tiene clase), así que pasa el día leyendo a los competidores y dando pronósticos — no es su don paracausal, es la misma atención de siempre, ahora con público. Germen de un oficio, todavía sin nombre.

**MODIFICADOS:** `08_Core_Relationships/La_Familia_Elegida.md` (tabla del calendario — Juegos de los Guardianes marcado ✅), `INDEX.md` (nueva sección "Season of the Risen — los Juegos de los Guardianes"), `02_Characters/Sai.md`, `02_Characters/Carina.md` (nueva sección "Huracán, no rivalidad"), `02_Characters/Jaden.md` (mención del estandarte ganado en silencio), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 12 marcada como escrita).

---

## Sesión 2026-07-05 (continuación) — El Solsticio: dos registros de memoria

**Corrección de nombres antes de escribir:** el autor propuso "Operación Lightfall" para el asalto de Ghaul que hizo caer la Torre — se detectó el choque (Lightfall ya está firmemente fijado como la Age XII completa: 7 capítulos, Neomuna, Calus, Nezarec). Resuelto con el autor vía pregunta directa: **"Operación Ocaso"** para el evento de la Guerra Roja.

**CREADA:** `05_Dialogues/Dialogue_Sai/Sai_Familia_Haunted_ElSolsticio.md` — junio, Season of the Haunted, cuarto evento del calendario anual.

**Corrección posterior del autor, mientras se propagaba:** la Batalla de los Seis Frentes **no** es parte de la Guerra Roja — es leyenda mucho más vieja, anterior a Kyle, una batalla legendaria de Guardianes al estilo del canon (un asedio simultáneo a la Ciudad joven que no debió sobrevivirse). Se había conflacionado por error con la Operación Ocaso en el primer borrador. **Corregido:** la escena ahora separa los dos registros — seis hogueras antiguas para los Seis Frentes (se celebran cantando, el duelo ya se les gastó a la leyenda) y una séptima llama, pequeña y sin canción, para la Operación Ocaso (reciente, donde vive el duelo real de Kyle). Los Guardianes tienen su propio rito aparte: templan armadura en fuego (rito real del Solsticio de Destiny, reutilizado) — el metal no cambia, quien lo sostiene sí. Kyle se queda junto a la séptima llama más tiempo que en ninguna de las seis grandes; dice cinco nombres en voz baja al final — casi con certeza, la Primera Escuadra (Kevin, Angie, Resner, Tiago, Joe).

**MODIFICADOS:** `01_Timeline/Age_V_The_Red_War.md` (nombre fijado en Notas Narrativas + aclaración de que los Seis Frentes son un evento distinto y más viejo), `08_Core_Relationships/Primera_Escuadra.md` (referencia corregida — solo Operación Ocaso, sin los Seis Frentes), `08_Core_Relationships/La_Familia_Elegida.md` (tabla del calendario), `INDEX.md` (sección "Season of the Haunted — el Solsticio" corregida), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 13 corregida).

**Ajuste adicional del autor — Elsie le nombra la Primera Escuadra a Sai:** mientras Kyle se queda junto a la séptima llama con Jaden y Carina, Elsie usa el momento para explicarle a Sai quiénes fueron los cimientos que nunca llegó a conocer — Kevin, Angie, Resner, Tiago, Joe —, a diferencia de la segunda escuadra que Sai sí conoce (Jaden, Carina, Amir, Jin, Gabriel). Le explica los memoriales junto al árbol del claro (ya establecidos en `00_Biblia/Memoriales_EcoPrismatic.md` y la serie `Elsie_Guardian_Memorial_01-05`). El eje añadido: el duelo de Kyle no es tristeza, es nostalgia — "la tristeza quiere que algo vuelva, la nostalgia solo quiere haberlo tenido"; forjó una familia entera (la segunda) pagando la primera, y ninguna de las dos verdades cancela la otra — la Tinta hecha explícita en una sola línea.

**MODIFICADO adicional:** `05_Dialogues/Dialogue_Sai/Sai_Familia_Haunted_ElSolsticio.md` (pasaje nuevo insertado + pie de página actualizado), `INDEX.md` (descripción ampliada).

---

## Continuación — Vault of Glass: el beat de "primero a ella" (retroactivo, Age I)

A petición del autor, se añadió un beat a las escenas del Vault of Glass (Age I): **la primera gran hazaña de la vida de Kyle como Guardian —Atheon, la Bóveda de Cristal— se la cuenta primero a Elsie**, no a la Vanguardia, no a Cayde, no solo a su Espectro. Esto ya existía parcialmente en `Guardian_Elsie_VaultOfGlass_ElArmaImposible` (semanas después, con el Mythoclast) pero faltaba en su origen — `Elsie_VaultOfGlass_PrimeraVisita`, donde el encuentro estaba enmarcado solo como intercambio táctico de inteligencia iniciado por protocolo de Elsie.

**MODIFICADOS:**
- `05_Dialogues/Dialogue_Elsie/Elsie_VaultOfGlass_PrimeraVisita.md` — nuevo pasaje en la sección de Atheon: Elsie nota que el relato de Kyle no tiene cadencia de reporte, sino de alguien contando lo más grande que ha hecho en su vida a la persona que eligió para escucharlo — "no a la Vanguardia... no a Cayde... ni siquiera solo a su Espectro. Se lo estaba contando a ella. Primero a ella." Pie de página actualizado con el enlace hacia adelante a "El Arma Imposible".
- `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_VaultOfGlass_ElArmaImposible.md` — línea añadida reconociendo que no es la primera vez ("la primera fue Atheon, semanas antes"), convirtiendo el gesto en patrón confirmado, no coincidencia aislada.
- `INDEX.md` — entrada de `Elsie_VaultOfGlass_PrimeraVisita` actualizada con el nuevo beat.

`Guardian_Equipo_VaultOfGlass_LaEntrada.md` (la entrada a la Bóveda con el equipo ad hoc) se revisó pero no requirió cambios — Elsie no aparece en esa escena, el beat pertenece a lo que ocurre después de Atheon.

**Enlace retroactivo pedido por el autor:** se añadió el mismo beat a `Sai_Familia_Haunted_ElSolsticio.md` — Sai le pregunta a Elsie cómo sabe tanto de la Primera Escuadra sin haberlos conocido, y Elsie responde trazando el patrón hasta Age I: Atheon, la primera gran hazaña de Kyle, se la contó primero a ella, no a la Vanguardia ni a Cayde — "nunca dejó de ser así... él decidió, hace años, que yo era la persona a la que le cuentas las cosas que de verdad importan." Cierra el círculo: el mismo lugar que Elsie ocupó para Kyle en Age I es el que ahora ocupa para Sai en Age XI. Pie de página y conexiones actualizados con enlaces a `Elsie_VaultOfGlass_PrimeraVisita` y `Guardian_Elsie_VaultOfGlass_ElArmaImposible`.

**Refinamiento adicional pedido por el autor:** entre esa línea de Elsie y la siguiente pregunta de Sai, se insertó el reconocimiento retrospectivo de Elsie — al contar el patrón de Age I en voz alta, se da cuenta, mirándolo desde este lado de los años, de que lo que había entre ella y Kyle entonces no era "calidez entre compañeros de armas": ya era amor, actuando antes de que ninguno de los dos tuviera la palabra para nombrarlo. Coherente con el motivo ya establecido en `Elsie_VaultOfGlass_PrimeraVisita` ("el nombre no es la respuesta, es el primer síntoma").

---

## Continuación — El Festival de las Almas Perdidas: "La Máscara Que No Lee"

**CREADA:** `05_Dialogues/Dialogue_Sai/Sai_Ghost_Plunder_LaMascaraQueNoLee.md` — octubre, Season of Plunder, quinto evento del calendario anual. Paga el beat pendiente del arco de Sai ("casi lee el secreto de Ghost") que llevaba desde el inicio de esta expansión marcado como pendiente en su ficha.

Detalles del autor incorporados: (1) la carcasa de Ghost para la temporada tiene forma de **gato negro**; (2) la frase de Cayde honrada riendo — **"esta es mi cara seria, no se nota"**, dicha por Jaden con perfecta seriedad (el chiste funciona precisamente porque él ya es así de plano); (3-4) el disparador del beat de percepción de Sai no es una confrontación directa con Ghost, sino un **acto paterno pequeño de Kyle**: el cordón de la máscara de Sai se rompe, él se lo arregla con el mismo gesto torpe-cariñoso de siempre, y es *ver eso* lo que hace temblar, por un instante, la compostura de Ghost — quien sabe exactamente de dónde viene ese gesto (el eco paterno, la niña bajo el árbol). En esa grieta de un segundo, Sai roza el secreto (impresión: un árbol, una mano pequeña, una pregunta sin responder) y elige, activamente, no terminar de leerlo.

**Corrección de continuidad:** la ficha de Sai listaba "casi lee el secreto de Ghost" como beat 3 dentro de la secuencia estricta de Age X (Año de la Bruja), antes de cruzar a Haunted. Como el calendario ya fechado sitúa esta escena en Plunder (después de Haunted), se **renumeró la secuencia** en `02_Characters/Sai.md`: el beat de Ghost se sacó de la lista de Age X y se describe aparte, correctamente fechado en Plunder.

**MODIFICADOS:** `02_Characters/Sai.md` (arco renumerado + sección "El triángulo" actualizada), `08_Core_Relationships/La_Familia_Elegida.md` (tabla del calendario), `INDEX.md` (nueva sección "Season of Plunder — el Festival de las Almas Perdidas"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 3 marcada como escrita).

**Con esta escena, quedan cuatro de los cinco eventos del calendario anual escritos.** Solo falta **La Final — Los Velocistas de Sol** (diciembre, mismo día que la Aurora) para completarlo.

---

## Continuación — Se decide escribir el Torneo IV completo en cronología (no solo la final)

El autor pidió detenerse antes de escribir directamente "La Final": quiere el Torneo IV completo, en orden — clasificación, fase de grupos, eliminatorias, semifinal, final — tomándose el tiempo necesario. Se propuso y acordó una secuencia de 8-10 escenas basada en lo ya diseñado en `Torneo_IV_Bracket.md`: madurez con Amanda (clasificación) → Gran Inauguración + sorteo → fase de grupos → Dieciseisavos (Los Graneros) → Octavos (breve) → Sincronía cae → Cuartos (Legado) → Semifinal/crisis de Kyle → susto de Rook → Final.

**Primera escena de la secuencia — la Gran Inauguración, con costumbres de las cuatro especies:**

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Familia_WitchQueen_LaGranInauguracion.md` — inicio de la campaña de Witch Queen, la apertura formal del Año 2 del Torneo IV (primer campeonato multiespecie). Absorbió y reemplazó la escena 17 original ("El sorteo"), que ahora ocurre como clímax de esta ceremonia más grande. Una costumbre por especie:
- **Humana:** llama ceremonial que arde todo el ciclo del torneo.
- **Awoken:** bendición de Petra Venj, deliberadamente vacía de predicción real (acordado por todo el aquelarre de antemano).
- **Cabal — "Los Bracus de Hierro":** Lord Saladin presenta a **Hierro Joven** — Torin, Mireya y **Ravask**, el primer Cabal en tomar el manto de Señor de Hierro tras la paz con Caiatl. Semilla temprana y coherente de la "Final Evolution" ya establecida en la ficha de Saladin (de soldado a mentor/guardián de memoria) y de su ya establecido respeto por los Cabal bajo Caiatl. Efrideet observa entre el público con la misma expresión con que vio entrenar a Kyle años atrás — beat personal sin necesitar diálogo.
- **Eliksni:** la Casa de la Luz (Mithrax, Eido) depone armas visiblemente y enciende linternas — "esta noche, el nombre significa lo que dice."

**El sorteo** cierra la ceremonia: Escuadra Cero cae con Manada Gris, Doble Filo y Casa Nueva; **Hierro Joven** (nuevo equipo de color, clasificó sin favores entre las Sesenta y Cuatro) cae en grupo aparte — su recorrido queda deliberadamente abierto, un hilo que Kyle se promete seguir sin decírselo a nadie.

**MODIFICADOS:** `02_Characters/Lord_Saladin.md` (nueva sección "Los Bracus de Hierro"), `02_Characters/Lady_Efrideet.md` (nueva sección "El Torneo de los Velocistas"), `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (Hierro Joven añadido a color adicional + Ravask a fichas sugeridas), `INDEX.md` (nueva sección "Witch Queen — la Gran Inauguración del Torneo IV"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 17 marcada como escrita, con alcance ampliado).

**Siguiente en la secuencia:** la madurez con Amanda (clasificación, Ages VIII-IX) — aunque cronológicamente precede a la Gran Inauguración; se escribió esta primero porque el autor la propuso primero. Falta decidir si se retoma ese orden estrictamente o se sigue por la fase de grupos.

---

## Continuación — Registro del elenco de personajes conocidos en el Torneo IV

El autor preguntó si ya habíamos decidido qué personajes conocidos corren en el torneo — no estaba registrado en ningún documento central. Se resolvió con tres preguntas al autor y se registró todo.

**Decisiones del autor:**
- **Comentaristas confirmados:** [[02_Characters/Lord_Shaxx]], **Fynch** (sin ficha propia, voz técnica), [[02_Characters/The_Drifter]].
- **Shayura, Reed-7, Aisha:** confirmado que son los mismos personajes de *Ni La Luz Ni La Oscuridad* ([[07_Unsorted_Ideas/IdeasDesarrollo_1]], Dark Future no-canon), en su versión presente y sin corromper. Se crearon fichas nuevas: [[02_Characters/Shayura]], [[02_Characters/Reed-7]], [[02_Characters/Aisha]] — compiten juntos como equipo. Nota añadida al documento del Dark Future conectando ambas versiones.
- **Aunor Mahal:** NO compite. Se conoce oficialmente con Kyle en el Torneo, pero su vínculo es de espada, no de pista — origen del "duelo empatado" ya mencionado hacia adelante en [[05_Dialogues/Dialogue_Guardian/Guardian_Eris_PostFinalShape_LoQueHacePosiblElRetorno]] ("una espada práxica no perdona la deuda"). Se cruzan al margen del torneo.
- **Ikora Rey:** compite de incógnito, bajo el nombre de equipo **Turno de Tarde**, con dos civiles (Randy, Liu Feng) que no saben con quién corren. Nueva sección añadida a `02_Characters/Ikora.md`.
- **Crow:** compite en el equipo **Segunda Oportunidad**, con Nadiya (civil). Nueva sección añadida a `02_Characters/Crow.md` — corre por algo que no tiene que ver con Uldren ni culpa heredada.
- **Un trío de Psions:** nuevo equipo Cabal de color, sin nombres individuales.

**Conflicto detectado y sin resolver:** el tercer puesto de Segunda Oportunidad se pensó como Micah-10, pero su ficha la fija como humana sin Luz que Kyle y Elsie conocen por primera vez en el Final Shape (Age XVIII) — usarla en el Torneo IV (Age X-XI) contradice esa cronología salvo que se decida que ya se conocían de antes. Queda pendiente de resolver con el autor; el tercer puesto del equipo sigue abierto.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (nueva sección "El elenco conocido"), `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva sección "Los comentaristas"), `02_Characters/Crow.md` y `02_Characters/Ikora.md` (secciones del Torneo), `07_Unsorted_Ideas/IdeasDesarrollo_1` (nota de conexión).
**CREADOS:** `02_Characters/Shayura.md`, `02_Characters/Reed-7.md`, `02_Characters/Aisha.md`.

---

## Continuación — Resuelto el conflicto de Micah-10; pseudónimo de Ikora

El autor resolvió el conflicto pendiente: **Micah-10 queda fuera del Torneo** — su encuentro con Kyle y Elsie en el Final Shape no se adelanta. En su lugar, el tercer puesto de **Segunda Oportunidad** lo ocupa **Redrix** (eco del Redrix del canon — el Guardián legendario cuyo nombre terminó en un arma). Además, se añadió un detalle a Ikora de incógnito: compite con el casco puesto todo el torneo, bajo el alias **"Voidhunger"**.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (Redrix reemplaza a Micah-10, conflicto marcado como resuelto), `02_Characters/Ikora.md` (pseudónimo y casco añadidos).

---

## Continuación — Las pistas del Torneo IV, planetas rehabilitados

El autor pidió diseñar dónde se corren las carreras: planetas y nombres de pista, rehabilitados para el torneo. Filosofía elegida: cada pista fue antes otra cosa (frente de guerra, ruina) — rehabilitarla para correr es la misma lógica de paz-por-encima-de-la-herida que ya sostiene el Torneo IV.

**Pistas asignadas por ronda:**
- **Fase de Grupos:** Tierra — **El Circuito de Origen** (periferia de la Ciudad, la pista original desde el Torneo I).
- **Dieciseisavos (Los Graneros):** EDZ — **Los Surcos** (caminos de guerra reconvertidos en tierra de cultivo).
- **Octavos (Los Chacales):** Nessus — **El Laberinto Verde** (terreno Vex sinuoso).
- **Cuartos (Legado):** Venus, Ishtar Sink — **El Umbral Dorado** (a la sombra de la Bóveda de Cristal — el mismo sector de la primera gran hazaña de Kyle).
- **Semifinal:** la Luna — **El Sendero de los Ecos** (despejada de Pesadillas solo para el torneo — resonancia directa con Season of the Haunted).
- **Final:** el Cosmódromo — **El Primer Aliento** (nevado, donde Kyle despertó en Age I — el cierre vuelve al principio).
- **Paradas menores de la Tabla de Marcas (clasificación):** el Arrecife (**La Deriva**) y Marte (**Las Arenas Rojas**), mención de color sin desarrollo propio.

**MODIFICADOS:** `04_Concepts/Torneo_De_Los_Velocistas.md` (nueva sección "Las pistas — planetas y circuitos rehabilitados"), `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (cada ronda ahora referencia su pista).

---

## Continuación — La madurez con Amanda (clasificación, Ages VIII-IX)

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Amanda_BeyondLight_LaMadurez.md` — fase 7 del arco de Kyle en el torneo (ya descrita en `Torneo_De_Los_Velocistas.md`, ahora escrita en prosa). Tras la derrota de Age VII (Shadowkeep, entrenar con rabia), Elsie ha vuelto y el equipo entrena con método por primera vez — los tres colibríes de la revancha, construidos pieza por pieza junto a Amanda, Jaden y Carina. Dos paradas de color mencionadas (La Deriva en el Arrecife, segundos; Las Arenas Rojas en Marte, primeros). Cierran la Tabla de Marcas como mejor tiempo combinado del sistema — cabeza de serie N.º 1 rumbo a la Gran Inauguración ya escrita. Cierre emocional: Kyle y Amanda, sin nombrar a Cayde en voz alta, reconocen que se deben mutuamente la resurrección de una alegría.

**MODIFICADOS:** `INDEX.md` (nueva sección "Beyond Light → Season of the Lost — la Tabla de Marcas del Torneo IV"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 14 marcada como escrita).

**Con esto, la secuencia del Torneo IV lleva escritas 2 de sus ~9-10 piezas planeadas** (la Gran Inauguración + esta clasificación). Quedan: fase de grupos en prosa, Dieciseisavos (Los Graneros), Octavos (Los Chacales, breve), Sincronía cae, Cuartos (Legado), Semifinal/crisis de Kyle, susto de Rook, y la Final.

---

## Cierre de sesión (2026-07-05)

Sesión extensa centrada en la expansión de la familia elegida (Kyle/Elsie/Sai/Ghost) y el Torneo de los Velocistas. Resumen de lo hecho, de más reciente a más antiguo:

1. Beat "primero a ella" añadido retroactivamente en el Vault of Glass (Age I) — Kyle le cuenta Atheon a Elsie antes que a nadie; confirmado como patrón con el Mythoclast; enlazado hacia adelante en el Solsticio, donde Elsie además reconoce retrospectivamente que aquello, en Age I, ya era amor sin nombre.
2. Calendario anual de la familia completado en 4 de 5 eventos: Los Juegos de los Guardianes (marzo), el Solsticio (junio, con corrección Seis Frentes/Operación Ocaso), el Festival de las Almas Perdidas (octubre, paga el beat Sai↔Ghost). Falta solo La Final (diciembre).
3. Decisión de alcance: el Torneo IV se escribe completo, en cronología, no solo la final. Secuencia de 8-10 escenas acordada.
4. La Gran Inauguración del Torneo IV escrita — costumbres de las cuatro especies (humana, Awoken, Cabal con los Bracus de Hierro y Ravask, Eliksni), sorteo de grupos.
5. Elenco completo de personajes conocidos en el Torneo registrado: comentaristas (Shaxx, Fynch, Drifter), Shayura/Reed-7/Aisha (fichas nuevas, mismos personajes del Dark Future no-canon en su versión sin corromper), Aunor Mahal (rival de espada, no corredora), Ikora de incógnito ("Voidhunger"), Crow y Redrix en Segunda Oportunidad.
6. Pistas del torneo diseñadas — seis circuitos rehabilitados de antiguos frentes de guerra, uno por ronda de eliminatoria, cerrando en el Cosmódromo donde Kyle despertó.
7. La madurez con Amanda escrita — clasificación completa, Ages VIII-IX.

**Pendiente para la próxima sesión:** continuar la secuencia del Torneo IV (fase de grupos, Dieciseisavos, Octavos, Sincronía cae, Cuartos, Semifinal, susto de Rook, Final); La Final de la familia (calendario anual, diciembre); ficha de Eva Levante (abierta); documento de relación Jaden+Carina+Kyle (abierta); heredados sin cambio (3 inconsistencias de imágenes; Salvation's Edge formato raid).

---

## Continuación — La Fase de Grupos en prosa

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Familia_WitchQueen_FaseDeGrupos.md` — las tres carreras de grupo del Torneo IV, semanas después de la Gran Inauguración, en El Circuito de Origen. Manada Gris (veteranos, Bram Ossory le devuelve a Kyle el nombre de Efrideet sin que nadie lo busque: "díselo, si la ves"), Doble Filo (puro espectáculo Awoken, terminan pidiéndole una foto a Sai en vez de a Kyle) y Casa Nueva (Skorn, Denna Vail, Thann Voss — la carrera más reñida de las tres, la paz de Mithrax y Caiatl hecha resultado deportivo). Sai estrena en esta escena su oficio de leer rivales desde las gradas — el mismo que ya tenía en Los Juegos de los Guardianes, ahora aplicado al torneo real de la familia. Escuadra Cero cierra 3-0, cabeza de serie alta rumbo a Dieciseisavos.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena en la sección de grupos), `INDEX.md` (nueva sección "Witch Queen — la Fase de Grupos del Torneo IV"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (nueva entrada 17b, escrita).

**Con esto, 3 de las ~9-10 escenas planeadas del Torneo IV completo ya están escritas** (Gran Inauguración + clasificación + fase de grupos). Siguiente en la secuencia: Dieciseisavos contra Los Graneros.

---

## Continuación — Dieciseisavos: Los Graneros

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_WitchQueen_LosGraneros.md` — el rival que casi elimina a la cabeza de serie más alta del torneo. Los Surcos, EDZ, cierre de Age X. Mejor-de-tres completo en prosa: Carrera 1 la pierden (Toma Aldrei toma una línea imposible en la primera curva, un segundo entero de ventaja); Carrera 2 la ganan, ajustada; Carrera 3, la decisiva, se gana por el margen más pequeño del torneo hasta ese punto — Kyle no iguala la línea de Toma, entiende la lógica detrás de ella (un civil sin Luz de sobra no puede permitirse el margen de error como idea, es literal) y usa la suya propia. Cierre: Kyle busca a Toma no para consolarlo sino para preguntarle cómo tomó esa línea — la prueba en vivo de la regla "sin Luz". Primer "filo del sillón" sentido desde dentro (el miedo propio, no el ajeno).

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 18 marcada como escrita).

**Con esto, 4 de las ~9-10 escenas del Torneo IV completo ya están escritas.** Siguiente: Octavos contra Los Chacales (breve), luego Sincronía cae, Cuartos (Legado), Semifinal, susto de Rook, y la Final.

---

## Continuación — Octavos: Los Chacales

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_Risen_LosChacales.md` — ronda deliberadamente ligera, escrita corta a propósito (el autor pidió avanzar una escena a la vez). El Laberinto Verde, Nessus, inicio de Season of the Risen. Los Chacales corren sucio, al límite del reglamento sin caer en descalificación — el contramodelo exacto de Rook. Carina les lee el patrón de bloqueo repetitivo (siempre el mismo instante, antes de cada curva ciega) y los desarma cediéndole el interior a Kyle. Ganan con ventaja clara, sin necesitar la tercera carrera — alivio silencioso tras el susto de Los Graneros.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (nueva entrada 18b, escrita).

**Con esto, 5 de las ~9-10 escenas del Torneo IV completo ya están escritas.** Siguiente: Sincronía cae (entre Octavos y Cuartos).

---

## Continuación — Sincronía cae

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_Risen_SincroniaCae.md` — el "filo del sillón" en su forma más pura. Mismo día que la victoria contra Los Chacales, en el garaje de Amanda: Escuadra Cero ve por transmisión cómo Legado (capitán Rendel) elimina a Sincronía, el trío Awoken que se movía "como una sola persona" y que Kyle temía enfrentar en Cuartos porque encarnaba, sin adornos, su propia duda sobre si su equipo tiene esa misma sincronía. Legado gana la decisiva 2-1; Rendel solo dice "corríamos por algo que ellos no tenían." El alivio de Kyle no es limpio — se mezcla con un miedo nuevo hacia quien acaba de hacer lo impensable. El mantra reaparece, más temblando que nunca: "tal vez no es imposible, si estamos en sincronía esta vez."

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 20 marcada como escrita).

**Con esto, 6 de las ~9-10 escenas del Torneo IV completo ya están escritas.** Siguiente: Cuartos contra Legado (Rendel, el eco de la Primera Escuadra).

---

## Continuación — Regla fijada: "Nadie cruza solo"

El autor preguntó cómo se decide una carrera por equipos (¿como Fall Guys, todos deben cruzar?). Se confirmó y se nombró la regla ya existente (regla 4 de "Las reglas de la pista" en `Torneo_De_Los_Velocistas.md`): el equipo puntúa por la **suma de las posiciones de llegada de sus tres integrantes** (1.º+2.º+3.º, gana la suma más baja) — no por el más rápido de los tres. Bautizada **"Nadie cruza solo"**, eco directo de "nadie vuelve solo" (Primera Escuadra) vuelto reglamento de carrera. Explica retroactivamente por qué las tácticas de bloqueo/cesión ya escritas (Carina cediendo el interior a Kyle en Los Graneros y Los Chacales) son la única forma real de ganar, no cortesía.

**MODIFICADO:** `04_Concepts/Torneo_De_Los_Velocistas.md` (regla 4 renombrada y explicada).

---

## Continuación — Cuartos: Legado

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Rendel_Risen_Legado.md` — la mejor sorpresa emocional del bracket, tal como se había previsto en el plan. El Umbral Dorado, Venus/Ishtar Sink, cierre de Season of the Risen. Rendel, capitán de Legado (que acaba de eliminar a Sincronía), revela el emblema no oficial de la Primera Escuadra grabado en su hombro — visitó los memoriales de Kevin, Angie, Resner, Tiago y Joe cuando era novato, sin saber quién era Kyle: "corro con esto puesto por ellos. No esperaba conocerte así." Escuadra Cero gana con margen claro; Legado ya gastó su milagro contra Sincronía. La pista (Venus, a la sombra de la Bóveda de Cristal) es un eco silencioso más: el mismo sector de la primera gran hazaña de Kyle, la que le contó primero a Elsie.

**CREADA:** `02_Characters/Rendel.md` — ficha ligera, ya que la escena lo desarrolló más allá de dos líneas.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena, ficha de Rendel confirmada), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 19 marcada como escrita).

**Con esto, 7 de las ~9-10 escenas del Torneo IV completo ya están escritas.** Siguiente: Semifinal / la crisis interna de Kyle (Punta de Lanza, drama interno por el duelo de Haunted).

---

## Continuación — Semifinal: la crisis interna de Kyle

**CREADA:** `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Haunted_LaSemifinal.md` — Season of the Haunted, días después del Solsticio, El Sendero de los Ecos (la Luna). El rival, Punta de Lanza, apenas importa esta ronda: el drama real es que Kyle casi no corre, sintiendo que perseguir alegría esa semana es una falta de respeto a la llama que sigue cargando. Elsie, en el porche, le devuelve su propia lección apenas días después de que él se la explicara a Sai sin saber que la necesitaría para sí mismo — "la tristeza quiere que algo vuelva, la nostalgia solo quiere haberlo tenido"; las dos cosas conviven, no se cancelan. Corre y gana con margen cómodo — el drama ya se había resuelto dos noches antes. Cierre silencioso: "Esto es para ustedes también."

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 11, ya existente en el plan, marcada como escrita).

**Con esto, 8 de las ~9-10 escenas del Torneo IV completo ya están escritas.** Siguiente: el susto de Rook (Escuadra Cero sigue por transmisión la Semifinal de Rook contra Guardia de Acero).

---

## Continuación — El susto de Rook

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_Haunted_ElSustoDeRook.md` — el "filo del sillón" invertido, mismo día que la victoria contra Punta de Lanza, en el garaje de Amanda. Escuadra Cero ve por transmisión cómo Torre (el equipo de Rook, invicto dos años) casi cae en Semifinal ante **Guardia de Acero** —primer equipo íntegramente cabal del torneo, guardia de honor de Caiatl—, yendo 1-1 a la carrera decisiva. El miedo se invierte: no quieren que Rook pierda — dos años de espera y la humillación de Shadowkeep solo tienen sentido si el reencuentro en la final es real, no contra un desconocido. Rook remonta y gana por un margen mínimo. Cierre: "La final es Rook" ya no suena a miedo, sino a que por fin va a ser real.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (enlace a la escena), `INDEX.md` (nueva sección), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 21 marcada como escrita).

**Con esto, 8 de las ~9 escenas planeadas del Torneo IV completo ya están escritas — solo falta la Final.** El cuadro entero queda resuelto: Escuadra Cero y Torre (Rook) se enfrentan en la Final, en la Aurora de Seraph.

---

## Continuación — Escena nueva antes de la Final: El Entrenamiento

A petición del autor, se escribió una pieza no planeada originalmente: Elsie sube a un colibrí ella misma, días antes de la Final, para ayudar a Kyle a liberar la tensión acumulada. La excusa que ella da es táctica ("quiero entender el circuito antes de verlo en la final"); el motivo real, que ninguno de los dos nombra en voz alta, es darle a Kyle algo que cuidar —a ella misma, aprendiendo torpemente a mantenerse arriba— para sacarlo de su propia ansiedad. Funciona al revés de como ella lo planeó: no aprende el trazado, pero consigue que Kyle deje de pensar en Rook durante una hora entera.

**CREADA:** `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Seraph_ElEntrenamiento.md` — Season Seraph, días antes de la Final, antes de La Primera Aurora.
**MODIFICADOS:** `INDEX.md` (nueva sección "Season Seraph — El Entrenamiento"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (nueva entrada 21b, escrita).

---

## Continuación — LA FINAL. El Torneo IV queda completo, de punta a punta, en cronología.

**CREADA:** `05_Dialogues/Dialogue_Guardian/Guardian_Familia_Seraph_LaFinal.md` — el cierre de ocho años de arco (desde las gradas de Age I hasta este día). El Primer Aliento, el Cosmódromo nevado donde Kyle despertó, Season Seraph, el día de la Aurora.

Serie a mejor de cinco contra Torre (Rook, Vray, Vess): Torre gana la 1, Escuadra Cero la 2 (por suma de posiciones, no por cruzar primero — la regla "nadie cruza solo" en acción), empatan en la 3 y 4. En la decisiva, Vray bloquea a Jaden casi hasta el borde de la pista; Kyle decide cerrar el hueco él mismo en vez de que Carina rompa su propia posición para cubrirlo — la confianza construida desde Age VI (Forsaken) puesta a prueba en el peor momento posible para fallar. Cruzan la meta en un orden que no favorece claramente a nadie; la suma tarda en confirmarse: **Escuadra Cero 11, Torre 10** — el margen más pequeño en la historia del torneo, tal como estaba previsto desde que se diseñó el bracket.

Beats cumplidos, todos ya sembrados en sesiones anteriores: Sai grita "¡LOBITO!" desde las gradas antes de que termine de proyectarse el resultado, cumpliendo la promesa de *La Primera Aurora* la noche anterior. Elsie nunca miró el marcador — miraba la cara de Kyle, y ya sabía. El mantra frágil de toda la temporada ("tal vez no es imposible, si estamos en sincronía esta vez") deja de sonar a plegaria. Rook y Kyle cierran el reencuentro de dos años con un apretón de manos y una sola línea cada uno — sin necesitar más, coherente con el "contramodelo" que Rook siempre fue. El trofeo de tres piezas (diseñado hace varias sesiones) se arma en el podio con el nombre del ciclo anterior de Rook, Vray y Vess todavía visible en su rayo, y termina en la cocina de Kyle, no en una vitrina, tal como se diseñó. Cierre explícito de la tesis completa del arco: el triunfo individual de Kyle ya era la cabaña con Elsie — la Final es otra cosa, igual de real, que no la reemplaza ni necesita justificarse contra ella.

**MODIFICADOS:** `07_Unsorted_Ideas/Torneo_IV_Bracket.md` (Final marcada como escrita, "CIERRA EL TORNEO IV COMPLETO"), `INDEX.md` (nueva sección "Season Seraph — La Final del Torneo IV"), `07_Unsorted_Ideas/Plan_Escenas_Familia_Elegida.md` (escena 5 marcada como escrita).

**CON ESTO, EL TORNEO IV QUEDA COMPLETO: las 9 escenas de la secuencia acordada están escritas, en cronología, de la clasificación a la final.** Secuencia completa: madurez con Amanda (clasificación) → Gran Inauguración + sorteo → fase de grupos → Dieciseisavos (Los Graneros) → Octavos (Los Chacales) → Sincronía cae → Cuartos (Legado) → Semifinal/crisis de Kyle → El Entrenamiento (pieza añadida) → susto de Rook → Final. Once escenas en total contando las dos piezas que se sumaron sobre la marcha (el origen en Age I con Cayde/Andal, y El Entrenamiento).

**Único evento pendiente del calendario anual completo de la familia:** ya no queda ninguno — La Final de la familia y la Final del Torneo resultaron ser la misma pieza, cerrando ambos arcos a la vez. **Pendientes reales para la próxima sesión:** ficha de Eva Levante (abierta); documento de relación Jaden+Carina+Kyle (abierta); heredados sin cambio (3 inconsistencias de imágenes de referencia; Salvation's Edge en formato de raid); posible hilo futuro del Torneo post-saga (deliberadamente no desarrollado, disponible si se retoma).

**PENDIENTE (próximas sesiones):** Festival de las Almas Perdidas (octubre) y La Final (diciembre, mismo día que la Aurora) — quedan dos escenas para completar el calendario anual; ficha de Eva Levante (¿necesaria?); considerar un documento de relación dedicado a Jaden+Carina+Kyle; heredados previos sin cambio (3 inconsistencias de imágenes, Salvation's Edge formato raid, threading "norte"/"lobito", prosa caps 34–39).

---

## Sesión 2026-07-03 — La Huida de Salvation's Edge · Apariencias fijadas · Revisión de referencias visuales

**CREADOS:**

- `05_Dialogues/Dialogue_Guardian/Guardian_FinalShape_LaHuida.md` — POV Kyle, escena nueva insertada entre Salvation's Edge (raid, pendiente de escribir en `01_Timeline/Raids/`) y `Guardian_FinalShape_AntesDelFinal`. Dos mitades: (1) el encuentro en la cima del monolito — el Testigo fusionado con la estructura, usando la máquina para terminar la Forma Final, con la Luz del Viajero (no un cuerpo, una presencia) contenida detrás de él; la mecánica real del raid final de Salvation's Edge traducida a prosa con equivalencia filosófica explícita en cada paso (los tres brazos de Resonancia, los brazaletes que piden siempre la resonancia contraria, Glyphbreaker, los seis glifos, la Prueba del patrón con los pilares, el núcleo expuesto, la fase de daño coreografiada, el Final Stand); Kyle es el único capaz de sostener dos resonancias a la vez para el sexto glifo — pago narrativo de ser Prismático. El Aegis todavía NO existe en este punto de la línea (aparece recién en `Guardian_Testigo_FinalShape_LaConfrontacion`). (2) La huida cuesta abajo por el monolito en colapso — corredor de las voces calladas, la plaza sin suelo, el puente colapsado, el muro final — con Carina, Jaden, Amir, Jin y Gabriel usando sus subclases de ficha; Kyle sale último, persiguiendo al Testigo herido, hasta que Elsie y Sai lo detienen por canal. El Testigo no muere: pierde el dominio sobre el Viajero, la estabilidad de la máquina y la capacidad inmediata de completar la Forma Final — gravemente herido, no derrotado.
- `05_Dialogues/Dialogue_Elsie/Elsie_FinalShape_LaHuida.md` — POV Elsie, paralela a la anterior: el mismo tramo visto desde afuera. Elsie y Sai sosteniendo una brecha del perímetro contra Desdeñados y Poseídos mientras el raid team combate adentro — primera escena de acción escrita en conjunto para las dos, con Estasis y la anticipación acumulada de siglos de líneas temporales de un lado, magia Techeun cruda (hilos del Plano, blinks, una hoja de luz ascendente) y el radar paracausal pasivo de Sai del otro, con el costo real de leer de más como recordatorio de que sigue siendo vulnerable. Uso explícito de "norte"/"norte chiquito" en pleno combate. Elsie ve al Testigo huir desde la cima con su tic narrativo ya establecido ("archivó", "Evitado. No ganado. Todavía no"); toca la Estrella Polar buscando esperanza; Sai le sostiene el antebrazo y dice "ni los mismos Nueve podrían"; la explosión del muro y los seis saliendo uno a uno, Kyle último; termina en el mismo punto exacto que la versión de Kyle.

**MODIFICADOS:**

- `02_Characters/Elsie.md` — nueva sección `## Apariencia`, a pedido del autor: Elsie conserva rostro humano completo (no plating visible), la única Exo así porque se transformó antes de que el programa de Clovis Bray estandarizara el chasis limpio (Jaden como contraste explícito); cabello rizado rojo óxido, con eco directo a `EstaVezAlguienCruza` (Roja/Cosmódromo); los tells quedaron en dos capas — acumulativos (no envejece, una cicatriz que no se quedó, quietud entre expresiones, parpadeo demasiado regular) y táctiles/de cerca (iris con patrón demasiado geométrico, el borde firme bajo la mandíbula, la segmentación del cuello al girar la cabeza entera); el gesto de Kyle sosteniéndole la cara en `Guardian_Elsie_FinalShape_AntesDelFinal` ahora tiene una capa retroactiva — sintió el borde metálico ese día y no le importó.
- `02_Characters/Guardian.md` — nueva sección `# Apariencia`: cabello oscuro y corto, cicatriz vieja en la mejilla izquierda al borde del mentón (Ghost pudo borrarla, nunca lo hizo), heterocromía (izquierdo verde con salpicaduras de marrón, derecho café oscuro) leída como eco temático de lo Prismático — "dos cosas verdaderas al mismo tiempo, sostenidas una junto a la otra."
- `99_Reference/Faceclaims.md` — nueva entrada Kyle (Brandon Routh / Tyler Hoechlin), mismo formato que la entrada de Sai; ajustes explícitos anotados (heterocromía y cicatriz no están en ninguna referencia).
- `INDEX.md` — 2 entradas nuevas en "Final Shape — perspectiva de Kyle" y "Final Shape — perspectiva de Elsie" para `LaHuida`.

**REVISADO (sin cambios en archivo):** las 23 imágenes de referencia en `99_Reference/apariencias_personajes/` (generadas por el autor). Feedback entregado en conversación — no volcado a archivo. **Pendientes detectados, no corregidos:**
1. `kyle_raid_team.png` — Kyle aparece con ojos brillando en azul (estilo Exo), contradice su heterocromía ya fijada en ficha y en su retrato solo.
2. `the_last_shape.png` — la lápida dice "ELISIE" en vez de "ELSIE" (typo visible en la imagen).
3. `sai_kyle_post_finalshape.png` — el nombre de archivo dice Sai pero la mujer del cuadro es pelirroja de piel humana (lee como Elsie, no Sai); confirmar con el autor cuál era la intención antes de usarla como referencia canon de una u otra.

---

## Sesión 2026-06-29 — Arco Faris completo · Las hermanas · El arco del rechazo

**CREADOS (sesión completa):**

- `06_Timeline_Archives/Alternate_Allies/Faris_GhostsDeep_ElDespertarBajoMetano.md` — POV Carina; señal-trampa, Ecthar, zanjas vacías, corona de Oryx sobre el Portaluz; Faris despierta sin memoria en burbuja de Vacío; Esquerda ofrece "Faris, por ahora"; Kyle dispara tarde. *Inicio del arco.*
- `06_Timeline_Archives/Alternate_Allies/Faris_Savathun_LoQueNoSupeSoltar.md` — POV dual; Savathûn lo observa días antes de hablar; confiesa que hizo posible su regreso; hace el duelo de Oryx en voz alta ("amé a alguien que nunca dejé ir"); "no dejes que el universo decida tu destino antes de que tengas algo que decir al respecto"; lo mira a los ojos — Oryx no está — y se va. *Entre el mar y Neomuna; Faris sin nombre.*
- `06_Timeline_Archives/Alternate_Allies/Faris_Neomuna_ElTestigoErrante.md` — POV Faris; Neomuna: la única ciudad sin muertos concretos detrás de su nombre anterior; Nimbus dice "Faris. Bueno." sin peso; nombre establecido. *El hogar provisional.*
- `06_Timeline_Archives/Alternate_Allies/Faris_Xivu_LoQueLaEspadaNoNombra.md` — POV dual; Xivu expulsada de su Mundo Trono, sin inmortalidad, sola; viene cargando eones de reproches que pertenecen a Oryx; Faris la derrota y no la mata; Xivu lo interpreta como lástima — rechazo según la Lógica de la Espada (*ser derrotada y no eliminada = no alcanzas el umbral*); el corazón de Xivu se rompe no por la derrota sino por la indiferencia; Faris se queda con el peso de una herida que no hizo y no puede cerrar. *Después de Neomuna.*
- `06_Timeline_Archives/Alternate_Allies/Elsie_Faris_Hypernet_LaEticaIncomoda.md` — POV Elsie; encuentro en el Hypernet; trabajan juntos en anomalía Vex; Faris distingue *saber quién fui* de *recordarlo*; Elsie no lo reporta. Cicatriz: la misericordia que solo funciona cuando el rostro del resucitado resulta cómodo no es ética, es preferencia. *Cierre del arco.*
- `02_Characters/Faris.md` — ficha completa; filosofía, conexiones, frases, conceptos asociados, La inversión de Oryx.

- `06_Timeline_Archives/Alternate_Allies/Faris_LibrosDelDolor_PorqueAunLosMonstruosPuedenAmar.md` — dos movimientos: (1) Neomuna — Faris lee los Libros del Dolor en versión anotada por Savathûn; sus marginalia cubren todo menos la sección sobre Sol (margen en blanco deliberado); (2) Plano Ascendente — Toland responde: Oryx fue a Sol porque Crota había sido derrotado allí y no pudo no ir; la Lógica de la Espada no era suficiente para contenerlo. *"Porque aún los monstruos pueden amar."* Revelación: la capacidad de amar estuvo siempre ahí — envuelta en teología de destrucción, pero ahí. Pregunta que queda: qué hacer con esa capacidad sin un sistema que le diga qué forma tomar.

- `06_Timeline_Archives/Alternate_Allies/Kyle_Faris_ElTableroSinReyes.md` — cierre del arco; inverso de El Gambito de los Dos Reyes; POV dual; Neomuna, encuentro sin guión: Kyle lleva Raze-Lighter (fragmento de Ecthar) y no la toca; Faris cruza la calle en vez de esquivar; preguntan los nombres de los Espectros; se separan sin declarar nada. El destino entre ellos reescrito tantas veces que ya no sabe qué forma tomar — el respiro es el espacio donde ninguno corre el guión disponible.

**MODIFICADOS:** `02_Characters/Oryx.md` (nodo inverso), `02_Characters/Faris.md` (conexiones), `INDEX.md` (7 entradas nuevas en Alternate_Allies), `log.md`.

---

## Sesión 2026-06-28 — Timeline Archive: EstaVezAlguienCruza

CREADO: `06_Timeline_Archives/Personal_Memories/EstaVezAlguienCruza.md` — 6 secciones completas (despertar en el Cosmódromo, Edad Oscura, ZME, después, cierre del loop, lo que llegó). Inversión de heridas: Elsie olvida / Kyle recuerda. Nombres de frontera "Roja"/"Extraño". Ghost Ember: fría y cautelosa, se presenta a ambos, grieta en "No te llamaba nada". Kyle muere cuando ya quería vivir — "Sujétalo". Legado: Tomás, la regla "entremos sin armas". Cicatriz fundacional de la maternidad Elsie→Sai. Eliminado borrador de `07_Unsorted_Ideas`. Actualizado INDEX.md.

---

## Sesión 2026-06-27 — Pipeline multi-agente · Git · Revisión ChatGPT #1 (cierre de sesión larga)

Cierre formal de la sesión extendida del 26-27 de junio. El trabajo narrativo (nacimiento del Círculo del Dolor + reconciliación de `Sai_ElCirculoDelDolor`) ya está registrado en el bloque del 26 más abajo. Esta entrada recoge los tres bloques de infraestructura que faltaban en el log.

### Bloque 1 — Pipeline multi-agente

**CREADOS:**

- **`99_Reference/Development_Workflow.md`** — define el pipeline completo: roles (Víctor/Claude Code/Claude Opus/ChatGPT), modelo de ramas (`develop` = WIP, `main` = canon publicado), cadencia de merge (por arco/lote, decisión de Víctor), protocolo de handoff con ChatGPT, formato de Paquete de Revisión.
- **`99_Reference/ChatGPT_Editor_Brief.md`** — configuración del GPT personalizado "Editor — Renewed Fate": rol (Postproducción Narrativa, no reemplaza), 9 reglas no-negociables del universo (tesis, Luz/Oscuridad, Prismática, arco Guardian, Testigo, anti-utilería, vulnerabilidad, complejidad, esperanza ganada), checklist editorial (continuidad, peso dramático, filosofía/identidad, simetrías, preguntas centrales), cómo consultar el repo (URLs raw de `develop`), formato de output (`Hallazgo | Por qué | Sugerencia | Severidad | ¿canon bloqueado?`).
- **`99_Reference/Faceclaims.md`** — índice de referencias visuales (marcado no-canon; manda la ficha). Primera entrada: **Sai = Ana de Armas** (esencia: cara legible/humana, no etérea; resonancias Joi/BR2049 y Marta/Knives Out). Ajustes: edad lee mayor → tomar como vibra; ojos recolor (castaño → verde con veta café); piel lila-rosa; mechones decolorados.

### Bloque 2 — Infraestructura git

- **`.gitignore` reescrito en UTF-8** — el original fue escrito por PowerShell en UTF-16 con BOM; git no puede leer UTF-16 → todas las reglas de ignore fallaban silenciosamente desde siempre. Reescrito (UTF-8 limpio). Reglas: `desktop.ini`, `Thumbs.db`, `.DS_Store`, `.obsidian/workspace.json`, `.obsidian/workspace-mobile.json`, `.obsidian/cache`, `.trash/`.
- **`workspace.json` desrastreado** (`git rm --cached .obsidian/workspace.json`) — Obsidian lo reescribe constantemente; estaba rastreado y bloqueaba checkouts.
- **`.git` reubicado fuera de Google Drive** (`--separate-git-dir`): el directorio `.git/` vive ahora en `C:\Users\avada\git-repos\memory-of-a-ghost.git`; en el vault queda un archivo puntero `.git`. Elimina los problemas de: `desktop.ini` inyectados por Drive en `.git/`, locks de GC bloqueados por drivefs, `gc.auto` en loop (también: `gc.auto=0`, `maintenance.auto=false`). Implementado con copy+swap atómico (rename cross-drive no es posible). Restos: carpeta `.git_OLD` con algunos locks — silenciada en `info/exclude`; borrar manualmente con Drive pausado y apps cerradas.
- **Identidad git local** + URL remoto para cuenta personal (`paz.victor0707@gmail.com` / `XxZylivrar360xX`).

### Bloque 3 — Primera revisión ChatGPT (Paquete de Revisión #1)

Paquete enviado al GPT "Editor — Renewed Fate": `ElCirculoDelDolor_ElNacimiento.md` + `Sai_ElCirculoDelDolor.md`. Devolvió 9 hallazgos (2 alta, 5 media, 2 baja). Triados y aplicados 3:

- **A (alta):** añadida la frase que define el mecanismo de la Prismática torcida — *"dos lenguajes obligados a convivir sin comprenderse"* — en el párrafo de la Corte Final (Movimiento II).
- **B (alta):** *"No acuden a un amo: acuden a un hermano"* — precisión sobre las hermanas de Oryx: no son súbditas, son iguales convocadas por su hermano; la Lógica de la Espada como código de familia.
- **C (media):** beat humano antes del renombrado — el Titán busca a tientas la mano del compañero; último acto de escuadra antes de que Oryx les arranque los nombres. Paga el espejo "dado vs. arrancado".

6 hallazgos descartados como interferencia con canon o bajo impacto (guardados en contexto de sesión, no en vault).

**Commit:** `17ee986` en `develop` — *"Paquete de Revisión #1: 3/9 hallazgos de ChatGPT aplicados"*. Primer commit sobre el `.git` reubicado en C: — limpio, sin locks.

### Estado al cierre

- `develop`: 1 commit adelante de `origin/develop`.
- `main`: varios commits adelante de `origin/main`.
- **Pendiente #1 (máxima prioridad):** reescritura de `Sai_Guardian_WitchQueen_ElLoboMasJoven.md` — nuevo encuadre: Sai ve lo que Kyle CONSTRUYÓ (la cabaña, la manada elegida); ancla de Saladin entregándose a Caiatl por Crow; Kyle resiste *"lobito"* → *"No. Lobo joven."* → Sai: *"Son la misma cosa."*; flash-forward *"Los jueves, lobito / Los jueves, niña"* (décadas después, cuando ya no corrige).
- **Pendiente #2:** Season of the Risen (Saladin/Caiatl/Crow) — escena de referencia para el ancla de la reescritura.
- **Pendiente #3:** lugartenientes de La Corte Final (Nazgûl-style) — marcador en `07_Unsorted_Ideas/Borrador_Nacimiento_Circulo_Del_Dolor`.
- (Heredados) threading "norte"/"lobito" en prosa; fichas stub Shuro-Chi/Kalli/Sedia; escena Last Wish; fichas Famke/Amanda_Holiday/Glint.

---

## Sesión 2026-06-26

### Cimiento del arco de Sai en Season of the Lost — "La Que No Va Sola"

Antes de seguir ajustando las escenas de los nombres (lobito / Lo Que No Se Arranca), el autor pidió **fundamentar el papel de Sai durante Season of the Lost**: cómo, inspirada por lo que Elsie hizo por ella, acuerda con Mara y el aquelarre ser la lectora/exploradora del Plano Ascendente. Escena nueva, POV Sai, que ocupa el hueco que la ficha marcaba como arco ("de víctima a recurso por elección", "la lectora que se niega a ir sola") y que ninguna escena escrita cubría.

**CREADO:**

- **`05_Dialogues/Dialogue_Sai/Sai_Aquelarre_SeasonLost_LaQueNoVaSola.md`** — Season of the Lost, después del rescate (LoQueSostiene/LoQueToma) y antes de las escenas de los nombres de Witch Queen. El consejo del aquelarre. MOTOR = el miedo del Plano de Sai (volver a estar sola en lo invisible — NO el de reemplazo, ese es exclusivo de Elsie/Kyle). MECANISMO = convierte la herida en método como Elsie: en vez de aceptar como herramienta (lo que Mara quiere) o rehusar por miedo, pone la condición "**no iré sola / no mando a nadie solo**" y redefine qué es una Techeun lectora. Mara fichada: ofrece transacción honesta pero instrumentaliza (lee "la lectora del Plano", no a la persona); Sai le pone una condición fuera de su modelo y Mara la REGISTRA sin entenderla ("no te modelé bien") — eco de LoQueToma. Espejo Elsie↔Sai consolidado: Sai se vuelve para el aquelarre lo que Elsie es para el mundo.

**MODIFICADOS:**

- **`02_Characters/Sai.md`** — escena añadida a "Aparece en"; el paso 2 del arco ("de víctima a recurso por elección") ahora enlaza la escena como su acto fundacional.
- **`INDEX.md`** — nueva subsección **"Season of the Lost — la elección del sitio"** en `## Dialogue_Sai`, antes de la de recuperación/nombres.
- **`02_Characters/Sai.md` (apariencia + don)** — §"Apariencia": **piel lila-rosa viva** (no el azul espectral de las Techeun mayores — una Awoken más cálida, más "de este lado"); **ojos verde esmeralda con vetas de café, sin la luz interna Awoken** — "ojos de humana", como si el Plano, al casi borrarla, la hubiera arrastrado un paso de vuelta hacia lo humano y la hubiera soltado "diferente, no cambiada"; **pelo decolorado por el Plano** (base oscura azul-negro con mechones blanco-ceniza a parches, en los sitios por donde se gastaba cuando Elsie la alcanzó — la herida vuelta rasgo); **la ropa como arco** (empieza en regalia ceremonial Techeun recién reconocida en *La Que No Va Sola*; con los años, por influencia de Kyle y gravitación hacia Elsie, migra hacia la silueta de viajera/abrigo de Elsie — la lectora del aquelarre terminando de verse como la otra lectora). §"El don": nueva secuela del casi-borrado — **radar paracausal latente, pasivo, no dominante**, que capta fuerzas paracausales cercanas (lo Tomado, lo ascendente) sin que ella lo invoque ni lo controle; explica que roce el secreto de Ghost, la marca de las Techeun Tomadas, y la semilla de las Pesadillas (Haunted).

**Apariencia (cont.) — color y faceclaim:**
- **`02_Characters/Sai.md`** — §"Apariencia" actualizada: **piel tono vivo entre lila y rosa** (Awoken cálida, no el azul espectral de las mayores) y **ojos verde esmeralda con vetas de café, sin la luz interna Awoken** ("ojos de humana", "como si el Plano la hubiera arrastrado un paso de vuelta hacia lo humano — diferente, no cambiada"). Único sitio que fijaba el color (verificado por grep); ninguna escena lo contradice.
- **`99_Reference/Faceclaims.md` (NUEVO)** — índice de referencias visuales, marcado **no-canon** (manda la ficha). Primera entrada: **Sai = Ana de Armas** (esencia: cara humana/legible, no etérea; resonancias Joi/BR2049 y Marta/Knives Out). Ajustes anotados: edad lee mayor → tomar como vibra; ojos a recolor (castaño→verde con veta café); piel lila-rosa; pelo con mechones decolorados.
- **`Sai_Aquelarre_SeasonLost_LaQueNoVaSola.md`** — **sembrado el color de ojos en escena**: Mara, que lee el patrón y no a la persona, se detiene una vez en los ojos humanos de Sai (lo único que no encaja en su casilla) y los archiva como *"anómalo, merece seguimiento"* — instrumentaliza hasta lo más humano de ella. Anotado en la semilla narrativa.

**Diferenciador físico sembrado en el rescate:**
- **`05_Dialogues/Dialogue_Elsie/Elsie_Sai_SeasonLost_LoQueSostiene.md`** — sembrados **ojos** y **mechones** como diferenciador textual de Elsie ("esta no es la Sai que me salvó en la otra línea"). Dos inserciones en POV Elsie, en el primer avistamiento: (1) los **mechones blanco-ceniza** quemándose *en vivo* donde el Plano la gasta → esta escena es el ORIGEN del rasgo (cuadra con ficha §Apariencia, "cuando Elsie la alcanzó"); la alt-Sai se fragmentó de golpe, sin tiempo de marcarse. (2) los **ojos verde-café sin luz Awoken, con alguien detrás** = reverso EXACTO de la imagen-trauma de la alt-Sai ("ojos abiertos sin nada detrás", `Sai_ElCirculoDelDolor`). Calibrado para NO romper la superposición: el rostro entrenado de Elsie certifica "no es ella" (racional) y entra igual — refuerza el motor "no era ella / era exactamente ella" en vez de desactivarlo. Anotado en la semilla narrativa de la escena.

**Decisiones de canon (del autor):**
- **Las tres Techeun mayores (Shuro-Chi, Kalli, Sedia) ya volvieron.** Fueron Tomadas por Oryx y rescatadas en la **Última Voluntad (Last Wish)** — escena aún por escribir. Por eso la escena NO es una misión de rescate (reponerlas en peligro sería redundante y excesivo): es la formalización del rol de Sai. Su autoridad moral sobre "¿dejamos entrar a la niña?" viene de haber sobrevivido la peor soledad. Voces distintas: Shuro-Chi (protege, dice "no" primero), Kalli (la que más lejos estuvo — aritmética pagada con el cuerpo, no crueldad), Sedia (la única que le pregunta a SAI qué quiere).
- **Inversión de la idea original:** Sai no rescata a sus hermanas yendo al Plano; las honra hacia atrás cambiando la regla que las dejó solas ("la regla la puso la más joven").
- **Petra:** parentesco implícito sostenido en acción, no etiqueta (coherente con el ajuste del 2026-06-25).

**Pendiente:**
- Fichas stub de **Shuro-Chi, Kalli, Sedia**; escena de **Last Wish** (rescate de las Techeun Tomadas).
- (Sigue) ajuste de las dos escenas de los nombres; threading "norte"/"lobito"; cimientos Kyle↔Sai doméstico y Sai↔Ghost.

---

## Sesión 2026-06-25 (continuación)

### El origen de los ritos de nombre — dos escenas hermanas

Cerrado el pendiente #1 de la sesión anterior: el origen de los nombres (Opción A — los cotidianos "norte"/"lobito" NACEN aquí, no se retrofitean a las escenas ya escritas). Escrito primero como una sola escena combinada y luego, **a petición del autor, separado en dos momentos** (`lobito` y `norte chiquito`) para poder ajustar cada uno por su lado. La escena combinada (`Sai_GuardianElsie_WitchQueen_LosNombresQueElegi.md`) fue borrada al dividirse; su contenido vive íntegro en las dos hermanas.

**CREADOS:**

- **`05_Dialogues/Dialogue_Sai/Sai_Guardian_WitchQueen_ElLoboMasJoven.md`** — **el origen de "lobito" (Kyle↔Sai)**. Age X, recuperación en la Ciudad Soñada, POV Sai. MOTOR = el miedo a ser un reemplazo en clave Kyle (él la cuida "como si ya lo hubiera hecho" — el eco paterno de Las Manos Recuerdan). Sai lo lee buscando *el nombre debajo del nombre* y NO encuentra nada enterrado — "debajo de Kyle hay más Kyle, y debajo el cero" (canon de la asimetría: se construyó desde cero, sin un antes que enterrar). Funda el mote en Saladin / Señor de Hierro (Rise of Iron) + el lobo más joven (los demás murieron con SIVA). Nombrar-HACIA-ABAJO como ternura, no desenterrar un secreto. Kyle le devuelve "niña" como trato → cimiento Kyle↔Sai cotidiano. RESOLUCIÓN única de Kyle: un reemplazo necesita un muerto enterrado al que parecerse; Kyle no tiene cuarto cerrado dentro, así que no la pone en el lugar de nadie. (El eco paterno sí existe pero Sai NO lo lee — Ghost lo guarda, "algo en él lo desvía".)
- **`05_Dialogues/Dialogue_Sai/Sai_Elsie_WitchQueen_LoQueNoSeArranca.md`** — **el origen de "norte"/"Elizabeth" (Elsie↔Sai)**. Misma era, POV Sai. MOTOR = el miedo en clave Elsie: el "milímetro de más", el fantasma de la otra Sai detrás del hombro. MECANISMO CENTRAL (el eje del arco): Sai lee a Elsie, SÍ encuentra el nombre enterrado (Elizabeth), está a un tirón de arrancarlo (el "segundo Famke" en miniatura) y SE DETIENE — cierra el don con el nombre en la boca. Y *porque* no lo arranca pudiendo, Elsie se lo DA. Planta el patrón "porque no tomó nada, le fue dado" que [[05_Dialogues/Dialogue_Sai/Sai_Elsie_PostFinalShape_LoQueSeDaSinPedirlo|Lo Que Se Da Sin Pedirlo]] cosecha post-Final Shape. "Elizabeth" = 2ª persona en la existencia a quien Elsie da su nombre verdadero (antes solo Kyle) → prueba ontológica contra el miedo. "norte" nace de [[05_Dialogues/Dialogue_Elsie/Elsie_Sai_SeasonLost_LoQueSostiene|Lo Que Sostiene]] ("no te sueltes del norte") devuelto; Elsie responde **"norte chiquito"** + **"Saiidris"** (sagrado, no regaño). El gesto de la mano en el pelo prefigura el sueño de LoQueSeDaSinPedirlo.

ANTI-UTILERÍA (ambas): el querer, el miedo, la decisión y el crecimiento son de Sai. Las dos abren con el mismo miedo a ser reemplazo en la clave de cada persona —el cero/sin-cuarto-cerrado (Kyle) y el milímetro/fantasma (Elsie)— y se sostienen solas.

**MODIFICADOS:**

- **`02_Characters/Sai.md`** — §"Los nombres": el cierre que decía "aún no tiene escena propia" ahora enlaza a las DOS escenas y resume cada mecanismo; ambas añadidas a "Aparece en".
- **`INDEX.md`** — nueva subsección **"Recuperación — Año de la Bruja (Age X)"** en `## Dialogue_Sai` (las dos hermanas), antes de la semana del duelo.
- **`CLAUDE.md`** — escenas 175→177 (Dialogue_Sai ×10, +2 origen de los nombres); pendiente del origen marcado como hecho.

**Decisiones de canon:**
- **La asimetría Kyle/Elsie hecha acción:** el don de Sai toca fondo en Kyle (no hay nombre oculto) y encuentra muro en Elsie (Elizabeth). Kyle no tiene nombre sagrado porque no tiene un antes que enterrar; con él, lo hondo es el silencio o "papá".
- **Restricción deliberada:** las regresiones "mamá"/"papá" NO nacen aquí (registro aparte, solo cuando Sai se quiebra del todo). Las escenas se quedan en cotidiano ("norte"/"lobito"/"niña") + sagrado ("Elizabeth"/"Saiidris").
- **Timing:** Age X, después de [[05_Dialogues/Dialogue_Guardian/Guardian_Sai_PreWitchQueen_LasManosRecuerdan|Las Manos Recuerdan]] (la intimidad ya construida); coherente con que Sai diga "Adiós, Elizabeth" post-Final Shape como nombre ya recibido.
- **Separación en dos momentos** (decisión del autor): dos registros emocionales distintos (Kyle↔Sai y Elsie↔Sai); cada uno autocontenido y movible. El autor tiene planes de ajuste sobre cada uno.

**Divergencia (2026-06-26): nacimiento del Círculo del Dolor — ESCRITO.**
- **EN PAUSA (retomar):** el ajuste del *lobito* (`Sai_Guardian_WitchQueen_ElLoboMasJoven`) — se divergió a esta escena.
- **CREADO:** `06_Timeline_Archives/Dark_Futures/ElCirculoDelDolor_ElNacimiento.md` — **PRIMER archivo de `Dark_Futures`**. El nacimiento del Círculo del Dolor (línea "donde Oryx no murió"; compañera de `Alternate_Allies/Sai_ElCirculoDelDolor`). Dos movimientos: **(I) La Conspiración (POV Elsie)** — el error es de ELLA: anticipa de más, trata a este Oryx como variable resuelta ("será como todos"), y el plan de Mara/Osiris se construye sobre su lectura → ella = causa raíz, ellos = próxima. **(II) El Filo de Su Conquista (voz de Oryx)** — casi vencido, ríe e invoca a sus hermanas (Savathûn/Xivu Arath; "no vine solo" = el patrón que el mapa de Elsie no tenía), sella la línea, Toma a los 6 y los renombra como su consejo de guerra. Los 6 (mapeo #4/#5 cruzado): Vorak/Bastión del Último No/**La Muralla**, Khûl-Tor/El Yugo Eterno/**La Cadena**, Ir Varesh/Voz del Abismo/**La Voz**, Nhazir/Portador del Silencio Profundo/**La Sentencia**, Ul-Kareth/Heraldo del Fin Verdadero/**La Visión**, Sekh-Ra/La Sombra Que Persiste/**La Sombra**. Temática: respuesta a "¿qué miedo nace aquí?" = que su mapa la traicione por confiarlo (origen del "error inicial" de Lost_Guardians); espejo oscuro del "dado vs. arrancado" del arco de los nombres de Sai; el cierre "lo que se valida, permanece" enlaza con `LoQueToma`. El Cazador→Sekh-Ra paga el beat humano "nos vemos del otro lado".
- **MODIFICADO:** `INDEX.md` — primera entrada de la sección `## Dark_Futures`.
- **Marcador:** `07_Unsorted_Ideas/Borrador_Nacimiento_Circulo_Del_Dolor` (plan + decisiones, cerrado).
- **AJUSTES (2026-06-26 cont.):** (a) **Nombre colectivo dual** — Oryx corona a los seis **«La Corte Final»** (endónimo del verdugo; coronamiento añadido al final del Movimiento II); la Ciudad los llama **«El Círculo del Dolor»** (exónimo, ya canon). (b) **Movimiento II reescrito a tiempo real** (vivido, no narrado): escuadra cantando victoria → risa → Oryx parte el Acorazado → emergen las hermanas → Toma/renombrado en vivo. (c) **Prismática torcida** — la Corte porta Luz Y Oscuridad sostenidas por la voluntad de Oryx (reverso oscuro de la Prismática); sembrado en la escena y en `Sai_ElCirculoDelDolor`. (d) Tildes corregidas en los seis conceptos ("Mí"→"Mi", posesivo).
- **HECHO — reconciliación de `Alternate_Allies/Sai_ElCirculoDelDolor`:** Elsie = causa raíz del fracaso (Mara/Osiris heredan su lectura); añadidas las hermanas (Savathûn/Xivu Arath) como el patrón que rompió su mapa; «La Corte Final» como endónimo + la Prismática torcida; cross-link a la escena nueva en cuerpo, footer y nota narrativa.

**Pendiente para próxima sesión:**
- **Threading de "norte"/"lobito" en prosa** de capítulos (decidir el toque en el capstone vs. dejarlo a las escenas).
- **Cimientos del mapa (auditoría):** Kyle↔Sai doméstico (inserciones en `FinalShape_AntesDelFinal`/`VuelveACasa`); Sai↔Ghost (1 beat); el "cuarto que fue suyo"/los jueves que el capstone afirma sin escena previa.
- **Caso Crow día 5**: revisar si "mamá/papá" descriptivos se vuelven implícitos.
- **Housekeeping**: enlazar la escena de Crow (`LoQueNoTuveQuePerdonar`) en `02_Characters/Crow.md`.
- (Heredado) Famke ficha provisional pendiente de expansión; fichas `Amanda_Holiday` y `Glint` aún inexistentes.

---

## Sesión 2026-06-25

### Ajustes y cimientos del arco de Sai

Iteración sobre los diálogos de Sai para que la semana del duelo aterrice en base sólida y no se sienta forzada. El autor pidió: (1) volver implícito el parentesco; (2) subir la edad aparente de Sai; (3) fundar el romance con Crow, que la semana daba por establecido sin escena de origen; (4) un sistema de motes que diga el vínculo sin etiquetas.

**CREADOS:**

- **`05_Dialogues/Dialogue_Sai/Sai_Crow_SeasonLost_LoQueNoTuveQuePerdonar.md`** — escena fundacional, **el ORIGEN de Sai+Crow**. Funda "la gente que regresa reconoce a otra que regresó" que [[05_Dialogues/Dialogue_Sai/Sai_Crow_PostFinalShape_LaPuertaQueSigueAbierta|La Puerta Que Sigue Abierta]] y [[05_Dialogues/Dialogue_Guardian/Guardian_Crow_PostFinalShape_UnUltimoViaje|Un Último Viaje]] daban por hecho en retrospectiva. **Season of the Lost, Jardines de Esila, POV Sai** — misma temporada del rescate de Sai y del Crow más en carne viva (usado por Savathûn, empatía incómoda con ella). MOTOR = el don de Sai (lee a Crow sin querer, lo nombra; por primera vez nombrar no la aísla — lo alcanza). COLUMNA Savathûn (a petición del autor): "te aterra entenderla; crees que la empatía es una confesión — no lo es, entender es brújula, no contagio". El gatillo de Kyle (jaló sobre Uldren) ENTERRADO como ironía para el lector (paga en Un Último Viaje). NO romance aún (Amanda viva) — solo el reconocimiento. Anti-utilería: Sai gana lo suyo (la 1ª prueba de que no está sola en lo invisible; el don como puente). MOTIVO: los Jardines de Esila que el ciclo marchita y devuelve, espejo de los dos que vuelven.

**MODIFICADOS:**

- **`05_Dialogues/Dialogue_Sai/Sai_Petra_PostFinalShape_DondeSePonenLasManos.md`** — parentesco hecho IMPLÍCITO (quitadas las etiquetas literales madre/padre/hija → dicho por la acción: Kyle planta el árbol y sostiene la cabaña; Elsie "me corregía a media frase"/"el norte"; "los que te forjaron son tercos hasta la médula" incluye a Ghost, no "los Bray" — Kyle no es Bray). Línea 57 afinada ("Sosteniéndolo, como hace hoy todo el mundo menos yo" en vez del plano "Él es importante para mí"; "¿Qué clase de persona da media vuelta camino del hogar?"); tildes.
- **Edad aparente de Sai: 16 → 19** (blindar el romance con Crow). 5 menciones: ficha de Sai + `Elsie_Sai…LoQueSostiene` + `Guardian_Sai…LasManosRecuerdan` + `Elsie_Sai…ElMapaNoLlegaAqui` ×2. Las "dieciséis líneas temporales" (Elsie/Kyle) NO se tocaron.
- **`02_Characters/Sai.md`** — nombre completo **Saiidris Thelis, *la lectora del Plano*** ("Sai" = diminutivo); nueva sección **"Los nombres"** con el sistema de tres capas.
- **`05_Dialogues/Dialogue_Sai/Sai_Elsie_PostFinalShape_LoQueSeDaSinPedirlo.md`** (el sueño, día 6) — aplicado el ritual: Elsie corrige con el nombre completo ("Así no, Saiidris"); Sai devuelve "Adiós, **Elizabeth**" y Elsie cierra "Hasta luego, Saiidris".
- **`INDEX.md`** — añadida la escena de Crow al clúster Season of the Lost. **`CLAUDE.md`** — Estado del vault al día.

**Decisiones de canon de la sesión:**
- **Nombre real de Sai: Saiidris Thelis** ("Sai" diminutivo).
- **Sistema de motes (3 capas):** *hacia Sai* — Kyle→"niña", Elsie→"norte chiquito" / "Saiidris" (sagrado). *De Sai* — a Elsie→"norte"/"mi norte" (cotidiano) / **"Elizabeth"** (sagrado) / "mamá" (regresión); a Kyle→**"lobito"** (cotidiano) / "papá" (regresión).
- **"Elizabeth" deja de ser exclusivo de Kyle:** Elsie da su nombre real a DOS seres — esposo e hija. Eleva el vínculo Elsie↔Sai al registro sagrado de la pareja.
- **"lobito" fundado:** Saladin nombró a Kyle Señor de Hierro (Rise of Iron, `Guardian.md`:856); es el más joven de ellos (los demás murieron con SIVA) → el lobo más joven. Asimetría temática: Kyle NO tiene nombre oculto (se construyó desde cero, sin un antes que enterrar).
- **Sai+Crow se conocen en Season of the Lost (Jardines de Esila)** — sin mover fechas.

**Pendiente para próxima sesión (lo que el autor pidió guardar):**
- **Escena de ORIGEN de los ritos de nombre** (Elsie↔Sai y Kyle↔Sai): el día en que Sai empezó a llamarlos "norte"/"lobito" y Elsie le confió "Elizabeth". Mata dos pájaros: cimiento del vínculo + nacimiento de los nombres. (Acordado Opción A: guardar el cotidiano "norte"/"lobito" para esta escena, en vez de retrofitear las actuales.)
- **Threading de "norte"/"lobito" en prosa**: decidir si un toque en el capstone ("Cómete algo, lobito") o esperar a la escena de origen. Conservar las regresiones deliberadas "mamá/papá" del sueño y el capstone.
- **Cimientos del mapa (auditoría)**: Kyle↔Sai doméstico (inserciones en escenas post-rescato — `FinalShape_AntesDelFinal`/`VuelveACasa`); Sai↔Ghost (1 beat); el "cuarto que fue suyo"/"¿comiste?"/los jueves que el capstone afirma sin escena previa.
- **Caso Crow día 5**: la conversación "lo de mis padres vs lo nuestro" usa mamá/papá descriptivos — revisar si se vuelve implícito.
- **Housekeeping**: la escena de Crow ya está en "Aparece en" de la ficha de Sai; falta enlazarla en `02_Characters/Crow.md`.
- (Heredado) Famke ficha provisional pendiente de expansión; fichas `Amanda_Holiday` y `Glint` aún inexistentes.

---

## Sesión 2026-06-24

### La semana de Sai — el duelo paralelo (post-El Último Crepúsculo)

Completar el arco de Sai en el duelo por Elsie: el reverso, de geometría OPUESTA, de la semana del pésame de Kyle (él se queda quieto y el mundo viene a la cabaña; ella no puede quedarse quieta y huye en el trabajo en Marte). Tres días ya existían sin registrar (Petra, Ikora, Saint, de sesión previa no logueada); esta sesión escribió los días 4-6, el capstone POV Sai, la ficha de Famke, y dio mantenimiento al INDEX (la sección `Dialogue_Sai` no existía).

**Estructura del arco (6 días de huida + el cruce):** progresión física como latido — d1 no se levanta de la silla / d2 no va a la lanzadera / d3 hasta la puerta / d4 cierra la puerta falsa y acepta / d5 decide / d6 suelta y cruza.

**CREADOS:**

- **`05_Dialogues/Dialogue_Sai/Sai_Famke_PostFinalShape_LoQueElDeseoNoDevuelve.md`** — **día 4, el día oscuro**. Famke, Ahamkara joven hija de Riven, NO viene de visita: la atrae el deseo que Sai no se confiesa (Sai abre el don y busca a Elsie en el Plano — lo que Ikora le prohibió). Ofrece traer a Elsie de vuelta — la tentación más cercana de la semana (cancela el duelo, no lo atraviesa). Sai casi dice que sí y rechaza por triple razón canónica: (1) una apuesta Ahamkara devuelve "un hueco con su cara" — y Sai, de toda la gente, teme ser un reemplazo; (2) Elsie murió por ELECCIÓN ("el hogar que elegimos") — traerla deshace su última elección libre; (3) el agujero es lo último verdadero que le queda. Cierra la puerta falsa (inversión del motivo del umbral) y por fin llora: acepta la pérdida.
- **`05_Dialogues/Dialogue_Sai/Sai_Crow_PostFinalShape_LaPuertaQueSigueAbierta.md`** — **día 5, la decisión**. Crow, pareja de Sai: amor JOVEN E INTENSO (no el de Kyle/Elsie) pero "de la misma madera" — validación pedida por el autor: "lo de tus padres no fue de verdad porque fuera callado, fue de verdad porque eligieron quedarse; te enamoraste de mí porque reconociste la cosa auténtica". NÚCLEO: Crow es el único ser vivo destruido por esa estirpe (fue Uldren, a quien RIVEN amplificó el deseo hasta quemarlo todo). MATIZ CAYDE (a petición del autor): un deseo IMPLÍCITO de Crow con la estirpe de Riven SÍ trajo a Cayde de vuelta en la Forma Final (Pale Heart) — distinción clave: hay deseos que traen a alguien "para quedártelo" (la trampa de Uldren / Famke) y deseos que lo traen "para soltarlo bien" (Cayde, por gracia, para una despedida; Crow lo dejó ir una 2ª vez); "lo que sana viene envuelto en un adiós, lo que condena en un para siempre". SELLO INDIRECTO (madurez del cazador, sin empujar): su puerta cerrada (Amanda) le muestra a Sai que la suya sigue abierta — "yo daría el universo por la puerta que llevas cinco días sin cruzar". Se niega a llevarla ("presentarse se hace con las propias piernas").
- **`05_Dialogues/Dialogue_Sai/Sai_Elsie_PostFinalShape_LoQueSeDaSinPedirlo.md`** — **día 6, "el sueño del don"** (sembrado por Ikora y Crow). El reverso exacto de la apuesta de Famke: donde la Ahamkara exigía "pide un deseo", esto se da sin pedirlo. Sai se da el día para JUNTARSE no huir (Petra: "estar lista es puntería"); duerme sin huir y NO abre el don — y precisamente por no pedir, le es dado. Elsie viene en sueños, blindada contra la trampa: honestidad ontológica ("soy lo que tu don alcanza de mí, no todo pero tampoco nada"), no se deja agarrar ("vine a que me sueltes bien"), envuelta en adiós. Entrega la tesis del arco de Sai ("el don nunca fue la herida; la herida era estar SOLA con él") y el mensaje de El Último Crepúsculo ("no me llores quieta, llórame caminando; ya llegué, me fui llegada, gané"). Sai SUELTA (abre las manos, como Crow soltó a Cayde) y honra la advertencia de Ikora (no se lanza al Plano a buscar el eco). Cruza: "Mañana fue la mentira del día 2. Hoy."
- **`05_Dialogues/Dialogue_Sai/Sai_Guardian_PostFinalShape_LoQueTrajeDeVuelta.md`** — **capstone, día 7, POV Sai** — el reverso interior de [[05_Dialogues/Dialogue_Guardian/Guardian_Sai_PostFinalShape_LaHijaQueElegimos|La Hija Que Elegimos]] (que ya cubría la llegada por lo que revela a KYLE). Decisión de diseño: NO redundante — aquella muestra a Kyle contándole su semana; esta es la mitad de ELLA de esa misma conversación, que carga lo que la otra no podía (se escribió antes de la semana de Sai). EJE: Sai como mensajera — no trajo a Elsie de vuelta (pudo; dijo que no), trajo "lo único real que se trae de los muertos: sus palabras". Beats únicos: confesión de Famke (Kyle cruza horror+deseo → alivio/orgullo: "esa es exactamente su hija"); el sueño y el GIRO AGRIDULCE que lo salva de lo sentimental ("¿por qué a ti y no a mí?" leído por Sai → "no vino a mí, me mandó a ti, el recado era tuyo"); entrega del mensaje; ironía dramática del "¿comiste?" (Elsie lo predijo en el sueño; Sai lo dice sin saberlo).
- **`02_Characters/Famke.md`** — ficha nueva (antes pendiente en tres semillas). Ahamkara joven, hija de Riven, nacida tras la Gran Cacería. Construida como ESPEJO OSCURO de Sai (don/naturaleza que llegó antes que la madurez; lo último de su estirpe; soledad heredada). NO villana (regla de Riven: no malicia, amplifica el deseo); la edad la hace más sincera, más hambrienta y —clave para la escena— más alcanzable (un "no" con compasión la toca). **Estado: provisional, pendiente de expansión.**

**MODIFICADOS:**

- **`05_Dialogues/Dialogue_Sai/Sai_Crow_PostFinalShape_LaPuertaQueSigueAbierta.md`** — insertado el matiz Cayde (a petición del autor) y reconciliado el párrafo de Amanda (Crow SABE que un deseo puede devolver a alguien y aun así no fue a buscar uno para ella — "dejé su puerta cerrada, por amor no a pesar de él"). Marco del vault verificado: el regreso de Cayde es en el Pale Heart = reconciliación/"último regalo", no restauración — la capa del deseo implícito explica el mecanismo sin contradecirlo.
- **`INDEX.md`** — nueva sección `## Dialogue_Sai` (los 7 archivos del arco, incluidos los 3 previos sin registrar); `Dialogue_Sai/` añadida a la lógica de carpetas; Famke añadida a Main Characters (marcada como ficha provisional).
- **`CLAUDE.md`** — Estado del vault al día (escenas y personajes recontados; última sesión).

**Decisiones de canon de la sesión:**
- **Famke = hija de Riven**, nueva criatura; el deseo Ahamkara como eje del "día oscuro".
- **El regreso de Cayde (Forma Final) como deseo implícito de Crow** canalizado por la estirpe de Riven — articula la distinción "quedárselo vs. soltarlo bien" que ordena toda la semana y siembra el día 6.
- **El sueño del día 6 NO es Elsie literal devuelta**, sino "lo que el don alcanza" — honesto sobre ser un fragmento, por gracia y para despedida (modelo Cayde). Reverso de Famke.
- **El capstone POV Sai complementa, no reemplaza, La Hija Que Elegimos** — dual-POV del mismo día 7 (precedente del vault: El Último Crepúsculo ×3, etc.).

**Pendiente para próxima sesión:**
- **`02_Characters/Famke.md` — ficha provisional, pendiente de expansión** (debutó esta sesión; falta llevarla al nivel de las fichas mayores). Marcada como tal en INDEX.
- Fichas aún inexistentes enlazadas por las escenas nuevas: `02_Characters/Amanda_Holiday.md` y `02_Characters/Glint.md` (ya eran enlaces pendientes desde `Guardian_Crow_PostFinalShape_SinSaberQueLohacia`).
- Sesiones previas sin loguear (semana del pésame de Kyle, ~2026-06-23) no documentadas aquí; los conteos del vault sí están al día.

---

## Sesión 2026-06-11 (continuación 3)

### Unificación de grafía — "Elizabeth"

Corrección global: "Elisabeth" (con s) era error tipográfico; la grafía canónica es "Elizabeth" (con z). Se encontraron 13 ocurrencias en 9 archivos y se eliminaron todas.

**MODIFICADOS:**

- `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_VaultOfGlass_PrimeraVisita.md` — 3 ocurrencias (el diálogo donde Elsie entrega su nombre)
- `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_VaultOfGlass_ElArmaImposible.md` — 2 ocurrencias
- `05_Dialogues/Dialogue_Elsie/Elsie_VaultOfGlass_PrimeraVisita.md` — 3 ocurrencias
- `05_Dialogues/Dialogue_Elsie/Elsie_FinalShape_AntesDelFinal.md` — 1 ocurrencia (nota narrativa)
- `06_Timeline_Archives/Elsie_UltimoGuardian_ElNombre.md` — 2 ocurrencias
- `06_Timeline_Archives/El_Ultimo_Guardian.md` — 1 ocurrencia
- `04_Concepts/La_Estrella_Polar.md` — 1 ocurrencia (en la descripción del bucle de nombres)
- `10_Chapters/Age_I/Cap_03_The_Queens_Paragon.md` — 1 ocurrencia
- `log.md` — entrada previa corregida + nota de pendiente cerrada

**ACTUALIZADO:** `CLAUDE.md` — estado del vault al día: 127 escenas (+9 vs. sesión anterior), Dialogue_Ghost añadida al árbol, última sesión documentada.

Verificación final: grep sobre todo el vault confirma 0 ocurrencias de "Elisabeth".

---

## Sesión 2026-06-11 (continuación 2)

### El cierre de Elsie — El Último Crepúsculo

Tercero y último de los tres cierres (Kyle → Ghost → Elsie). Brief del autor: intimidad, "su momento de ellos dos", sin cronología ni universo Destiny — solo hogar. Ocurre muchos años después de Ghost, tras una vida juntos en la cabaña. Tres archivos (ecosistema más leve que el de Ghost, fiel a la intimidad pedida).

**Decisiones:** la muerte como elección (las secuelas Exo son contexto, no causa); cierre autocontenido sin coda de reencuentro (ella es la que espera en casa; el Epílogo carga el reencuentro); explorar un poco de los años antes del crepúsculo; dejar implícito que *El Último Guardián* ocurre ~2 años después (la barba como prueba).

**CREADOS:**

- **`Dialogue_Guardian_Elsie/Guardian_Elsie_ElUltimoCrepusculo.md`** — **centro**. Cuatro movimientos: los años (té, arroyo, la barba, los búhos como presencia); el día (tarde normal, el cuerpo soltando sin dolor); el crepúsculo (se apoya en él, Kyle no la detiene — comprende y permanece, sin despedida); el último sonido (el búho como descanso, no alarma). "Por fin lo tuve / el milagro no era el mañana sino llegar a quedarme a verlo." Kyle dice "Elizabeth".
- **`Dialogue_Elsie/Elsie_ElUltimoCrepusculo.md`** — **interior**. La corredora que por fin llega; se detiene porque ganó, no porque pierda (desmonta su miedo secreto: detenerse ≠ fracasar); el mapa sin nada que corregir; la muerte como ejercicio final de elegir; soltar las pruebas de la vida no es perderlas, es confiárselas al mundo.
- **`Dialogue_Guardian/Guardian_Elsie_ElUltimoCrepusculo.md`** — **POV Kyle + el después**. La herida más profunda (por feliz, no por trágica). Aftermath que paga el Epílogo: lápida grande **"El hogar que elegimos"** (elegida por Kyle, par de la de Ghost), taza al estante, Estrella Polar que con el tiempo pasará al bolsillo, y **deja crecer la barba** (puente a *La Conversación*, ~2 años después). Sigue viviendo — lo que ningún mapa de Elsie predijo.

**MODIFICADOS:**

- **`02_Characters/Elsie.md`** — nueva sección "El Último Crepúsculo — El Cierre" (cierre del arco del mapa roto; el par de lápidas; enlaces a las tres escenas).
- **`INDEX.md`** — tres clusters nuevos (en Guardian_Elsie, Elsie y Guardian).

**Símbolos canonizados:** la barba (afeitado por ella en vida → la deja crecer cuando falta); el búho (vigilancia → descanso); el par de epitafios (hogar que acoge / hogar que elige).

**CANON DEL NOMBRE (resuelto — paradoja-espejo, no inconsistencia):** el intercambio de nombres es deliberado y a dos tiempos. `Guardian_Elsie_VaultOfGlass_PrimeraVisita` (Año 1, línea principal): Elsie le confía "Elizabeth" a Kyle como símbolo de confianza; él se queda como "Guardian". `Elsie_UltimoGuardian_ElNombre` (línea perdida): Kyle le devuelve "Elizabeth" y le entrega "Kyle" en señal de reconocimiento (sabe que es su Elsie aunque ella no vea que es él). Bucle de identidad sin origen discernible; por eso Elsie lo llama "Kyle" en la principal desde Beyond Light. Notas de los tres archivos del cierre + `La_Estrella_Polar` corregidas para reflejarlo (antes lo marqué erróneamente como contradicción). *(Grafía unificada en sesión siguiente: "Elizabeth" en todos los archivos.)*

**DEPENDENCIA narrativa (abierta):** el búho necesita plantarse en capítulos (deriva del asedio de la Última Ciudad en Red War, donde Elsie entra por Kyle) para que su resignificación en el cierre tenga setup.

---

## Sesión 2026-06-11 (continuación)

### El cierre de Ghost — La Última Resurrección

Sienta el ecosistema completo del cierre de Ghost, segundo de los tres cierres (tras Kyle, antes de Elsie). Encaja en el puente canónico entre Cap 55 (El Gambito Concluye) y Cap 56 (Epílogo): el acto que convierte a Kyle de portador-de-Luz en mortal humano, completando el arco Cadáver → Arma → Símbolo → Anomalía → **Persona**. Seis archivos nuevos en la nueva carpeta `05_Dialogues/Dialogue_Ghost/` (más dos POV en Guardian y Elsie).

**Decisiones autorales:** sacrificio en el umbral post-guerra (no años después); presenciado por Kyle, Elsie y los cinco Espectros (coral, con la intimidad enmarcada por la familia silenciosa); ecosistema completo de 6 piezas.

**CREADOS:**

- **`Dialogue_Ghost/Ghost_PostGambito_LaConclusion.md`** — beat interior; la última narración del narrador de la saga antes de callar. "Kyle ya ganó: la vida." Ensaya en privado "vale la pena" / "siempre supe que podría hacerlo".
- **`Dialogue_Ghost/Ghost_Guardian_PostGambito_LaUltimaResurreccion.md`** — **centro canónico**. El sacrificio + última conversación. "Déjame, esta vez, terminar." / "No me quedé con el mito, me quedé contigo." / "Valió la pena" → **"Vive."** El cuerpo bajo la lápida pequeña tras el árbol. *(Corregido vía fork: Ghost va a la lápida pequeña, NO a un estante; el estante vacío del Epílogo es la taza de Elsie + Estrella Polar, reservado al cierre de Elsie.)*
- **`Dialogue_Guardian/Guardian_Ghost_PostGambito_LaUltimaResurreccion.md`** — POV Kyle. El "No" antes de oír; el silencio con bordes; la retirada de la red (no la Luz, la certeza del regreso); la primera respiración mortal contada.
- **`Dialogue_Elsie/Elsie_Ghost_PostGambito_LaUltimaResurreccion.md`** — POV Elsie. La primera que comprende: salvar de la inmortalidad, no de la muerte. Apaga el viejo sistema y elige no buscar la variable. La que nunca pudo soltar, soltando. Ve su lápida grande futura sin miedo.
- **`Dialogue_Ghost/Espectros_PostGambito_LaUltimaResurreccion.md`** — la segunda escuadra alrededor de la piedra; cada Espectro en su clave (Sky entiende primero y graba; Basim no halla contingencia; Hornet sostiene el perímetro; Rune halla las palabras; Maverick mira a Ghost). Epitafio: ***"El hogar que nos acoge."*** (par con la lápida grande de Elsie, *"El hogar que elegimos."*).
- **`Dialogue_Ghost/Ghost_Guardian_ElReencuentro.md`** — **coda final de la saga**. Décadas después, tras el Epílogo. Ghost despierta sin nada que buscar — la única vez. "Te tardaste." / "Te encontré. Por última vez." Bookend exacto con el Cosmódromo.

**MODIFICADOS:**

- **`02_Characters/Ghost.md`** — nueva sección "La Última Resurrección — El Cierre" tras Final Evolution, con la inversión temática (el que más temía la soledad se va primero) y enlaces a las seis escenas.
- **`INDEX.md`** — nueva categoría Dialogue_Ghost en la lógica de carpetas y su sección completa; clusters "Post-Gambito — El cierre de Ghost" en Dialogue_Guardian y Dialogue_Elsie.
- **`10_Chapters/Epilogo/The_Last_Shape.md`** — enlaces a centro y coda; nota que canoniza la lápida pequeña = Ghost y el pago fuera de cuadro de "¿Ella también? — Sí".

**Decisión narrativa central de la sesión:** el mayor acto de amor de Ghost no es mantener vivo a Kyle, es devolverle la mortalidad. La inversión de su miedo nuclear (la soledad) se vuelve su legado: ser *"el hogar que nos acoge"*, y él no se queda solo — solo llega antes.

**Gancho abierto para el cierre de Elsie (próxima sesión):** la lápida grande tras el árbol y el estante vacío (taza + Estrella Polar) son suyos; Elsie_Ghost_LaUltimaResurreccion ya planta que ve su final finito sin miedo. Decidir si comparte cuadro en la coda del reencuentro o tiene coda propia (recomendado: propia).

---

## Sesión 2026-06-11

### El Epílogo, el Winnower, la Estrella Polar y la Música

Una sesión de apertura hacia el final de la saga. Cuatro archivos nuevos, dos modificados.

---

**CREADOS:**

**`10_Chapters/Epilogo/The_Last_Shape.md`** — Capítulo 56, epílogo de toda la saga. *Años Después...* Kyle corta leña. El estante de la izquierda vacío — la Estrella Polar va con él en el bolsillo. La cicatriz del brazo izquierdo todavía ahí, décadas después. Los memoriales. Las dos lápidas detrás del árbol. El Winnower aparece junto al memorial con la forma del hombre que murió en el Cosmódromo — el primero, antes de todo. La conversación: "Te dije que no te abandonaría." / "¿Ella también? — Sí." / Kyle completo, no vacío. Final: "La mañana continuó." + flor blanca en la copa del árbol. Contrapunto directo de Cap_01_A_New_Shape.

**`04_Concepts/La_Estrella_Polar.md`** — Concepto de orientación, no de amor romántico. La estrella que no se mueve mientras el resto del cielo rota. Recorrido del objeto en la saga: el nombre en el umbral → la taza del Último Guardián → el bolsillo de la camisa → el final. El estante vacío dice lo mismo que cualquier palabra: se fue con él.

**`05_Dialogues/Dialogue_Guardian/Guardian_Ghost_PostRedWar_Io_LaMusica.md`** — Kyle investiga nodos del Estratega en Io emitiendo música pre-Colapso. Primera experiencia con música sin nostalgia ni referencia cultural — solo el fenómeno. "El sonido no pedía ser catalogado — pedía ser recibido." "¿Listo? — No." Al salir: "Que tenía razón." Conecta hacia adelante: décadas después, en la cabaña con Elsie, habrá música; Kyle ya sabrá qué hacer con ella.

**`05_Dialogues/Dialogue_Guardian/Guardian_Lodi_PostGambito_EDZ_LaVoz.md`** — Un año post-Gambito. Kyle investiga la profecía incompleta de III usando a Lodi como intermediario. El canal se abre y Lodi toma tres posturas diferentes en tres segundos, como si se reajustara una marioneta en la mano. Escudos a cero. El Winnower habla — diálogo canónico respetado íntegramente. "No te abandonaré" archivado sin categoría. Lodi, al recuperar el canal: "Eso no eran los Nueve... pero te conocía. *Muy* bien. No sé qué era eso." Lugar elegido con precisión: el fragmento del Viajero donde Kyle recuperó la Luz.

---

**MODIFICADOS:**

**`05_Dialogues/Dialogue_Guardian/Guardian_Elsie_PostRedWar_LasCicatrices.md`** — Elsie es quien sutura (no Kyle suturándose solo). Misión ajustada: búnker del Estratega en Io (no Biblioteca Ishtar). Añadido: "¿Qué es música contemporánea?" / "Eso tendrás que descubrirlo por tu cuenta. No lo puedo explicar con palabras." — semilla directa de LaMusica. La cicatriz del brazo izquierdo que aparece en The_Last_Shape décadas después es el nudo de esta escena.

**`06_Timeline_Archives/Personal_Memories/The_Last_Reset.md`** — Nota narrativa ampliada con lectura retroactiva: el Winnower pregunta "¿quién gana la partida?" sabiendo ya la respuesta — días antes, Elsie visitó a Kyle sin saber que era su futuro, y el tablero ya estaba resuelto. Ella estuvo ahí. No lo supo. Quien pregunta ya conoce la respuesta.

---

**Decisión narrativa central de la sesión:** la Estrella Polar no queda en el estante como legado — se va con Kyle. El estante vacío al inicio del epílogo confirma en silencio que fue así.

---

## Sesión 2026-06-09

### Cap 01 — consolidación final + nuevas secciones

**Archivos modificados:** `10_Chapters/Age_I/Cap_01_A_New_Shape.md`

**Nueva sección XV — "Las Semanas Entre"** insertada entre la antigua XIV y XV. Condensa en prosa de capítulo las tres escenas de construcción de curiosidad (El Informe Innecesario, La Pregunta que No Era del Informe, El Acumulado) que justifican por qué Kyle quiere compartir la Mythoclast con Elsie. Las secciones siguientes renumeradas: XV→XVI, XVI→XVII, XVII→XVIII.

**Corrección de consistencia — El Acumulado:** el escenario original (sector forestal, construcción de cabaña) era incorrecto — la cabaña se construye post-Vault. Corregido a sector industrial / instalación del módulo de Sparrow que dejó Amanda. La textura "manos ocupadas, mente suelta" se preserva, el setting es canónicamente correcto.

**Tesis resaltada:** La frase *"La confianza no siempre llega con razones. A veces llega antes."* promovida a blockquote en sección XVI (Joe / entrada al Vault). Marcada como tesis central de Kyle.

**Nota de desarrollo añadida al final del capítulo:** documenta el patrón de confianza de Año 1 y las dos grietas necesarias — Mara (malinterpretación inteligente) y el Guardian Sin Nombre (traición desde adentro).

---

### Seis archivos de diálogo — corrección de setting

`05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_AntesDelVault_ElAcumulado.md` y `05_Dialogues/Dialogue_Elsie/Elsie_Guardian_AntesDelVault_ElAcumulado.md` — ambos reescritos con el nuevo setting (sector industrial, Sparrow, módulo de Amanda). Beats emocionales preservados: "No sé por qué te estoy contando todo esto" / "Sí lo sabes" / Ghost: "¿Bien?" distinto esta vez.

---

### Personajes nuevos — Mara Sov y Vale

**`02_Characters/Mara_Sov.md`** — creado (archivo estaba vacío). Construido a partir de Cap_03. Núcleo: relación transaccional con Kyle, lee el patrón no la persona, predice comportamientos pero no puede predecir la elección individual. Su "Paragon" es clasificación, no elogio. Incluye tabla de arco, filosofía de Luz como instrumento, y nota de desarrollo sobre el futuro quiebre.

**`02_Characters/El_Guardian_Sin_Nombre.md`** — creado como semilla estructural, luego reescrito con fundamento filosófico completo bajo el nombre de trabajo "Vale". Núcleo: no un traidor corrupto sino alguien que empezó con una pregunta casi idéntica a la de Kyle. La bifurcación clave:
- Kyle: *¿Cómo estudiamos esto sin convertirnos en ello?*
- Vale: *¿Cómo esperamos sobrevivir si nunca lo estudiamos?*

La corrupción es deriva, no caída. Elsie no reconoce el nombre de ninguna línea temporal — señal de alarma. Nombre final pendiente.

**INDEX.md** actualizado con ambos personajes en sección nueva: "Personajes de arco específico — traición y transacción".

---

**Pendiente para próxima sesión:**
- Continuar desarrollo de Cap_02 (Bane of Hope)
- Determinar cuándo y cómo entra Vale en el círculo de Kyle (¿post-Crota? ¿durante House of Wolves?)
- Nombre final para Vale

---

## Sesión 2026-06-08

### Cap 03 — The Queen's Paragon (tercer capítulo de Age I)

`10_Chapters/Age_I/Cap_03_The_Queens_Paragon.md` — estado: **borrador**.

Ocho secciones cubriendo House of Wolves / Prison of Elders.

| Sección | Contenido |
|---|---|
| I. La Reina | El mensaje que no era orden ni invitación. Uldren como evaluador. Ghost esperando afuera. |
| II. Mara Sov | La sala diseñada para contar tableros. La alianza en sus términos. "Neutraliza" como palabra que deja la decisión en Kyle. |
| III. Lo que los Lobos eran | Los archivos de Uldren. La historia Eliksni. El Colapso siguió al Viajero desde ellos hasta nosotros. El mapa de Kyle tiene una grieta. |
| IV. La cacería | Kyle, Angie, Joe — escuadra de tres. Joe como eje fijo. Angie sosteniendo el calor sin Kevin/Resner/Tiago. |
| V. La Prisión de los Mayores | Cuatro especies, cuatro lógicas. La versatilidad como confiar en el equipo que cubre lo que tú no puedes. Skolas no estaba en el briefing. |
| VI. La decisión | Kyle no mata a Skolas. No compasión — comprensión de que la justicia no es eficiencia. Primera articulación filosófica, sin declaración, solo acción. Joe observa. Angie reconoce. Ghost en silencio. |
| VII. La Reina, de vuelta | Mara recibe a Skolas sabiendo cómo llegó. El título cambia de función a evaluación. Uldren: "La Reina lo notó." |
| VIII. El regreso | El peso de la decisión todavía en el cuerpo. Ghost calculando. La semilla de Forsaken plantada: "esa decisión ya no está disponible de la misma forma." |

**Beats de personaje:**
- Mara Sov construida desde cero (archivo vacío). Presente como fuerza política cósmica sin explicarse — el espacio hace el trabajo.
- Uldren: tres apariciones con función distinta en cada una. El reconocimiento forzado deepens from Cap 01.
- Eliksni como espejo de la humanidad: el mismo abandono, distinto resultado. Base filosófica de la decisión Skolas.
- Joe: el eje. La permanencia como valor.
- Angie: sosteniendo al equipo como personas cuando faltan tres de sus cinco.
- Ghost: registrando sin hablar.

**Foreshadowing:**
- Forsaken: última línea del capítulo menciona explícitamente que la decisión no estará disponible de la misma forma cuando Uldren esté en la mira sin testigos.

INDEX.md y log.md actualizados.

---

### Consequences — concepto fundacional

`04_Concepts/Consequences.md` — creado. El usuario lo definió como **"la tinta con la que escribimos nuestra historia."**

Propósito: garantizar que cada arco narrativo tenga un costo claro, personal e irreversible — no solo para el universo, sino para las personas que lo atraviesan.

| Personaje | Pérdida fundamental | Cómo termina |
|---|---|---|
| Kyle | La inocencia — la certeza de que la Luz es suficiente | En paz, con las marcas, no a pesar de ellas |
| Ghost | La fe sin fisuras — encontrar a Kyle era el principio del trabajo, no el final | Transformado; algo propio, no solo fragmento del Viajero |
| Cayde | No muere heroicamente — muere injustamente | Muere el único que veía a Kyle como hombre, no como símbolo |
| Elsie | El descanso — carga el peso de todas las iteraciones fallidas | Quiere que esta sea la última vez |

**Regla estructural inscrita:** Cada victoria debe costar algo que no se recupera. La diferencia entre pérdida y derrota: los personajes no son derrotados, pero llegan al final diferentes de como empezaron.

Registrado también en memoria del agente (`project-consequences-principle.md`). INDEX.md actualizado.

---

## Sesión 2026-06-07 (continuación 2)

### Cap 02 — Bane of Hope (segundo capítulo de Age I)

`10_Chapters/Age_I/Cap_02_Bane_of_Hope.md` — estado: **borrador**.

Cinco secciones + seis subsecciones de la raid.

| Sección | Contenido |
|---|---|
| I. Eris Morn | Primera conversación real. Lo que ve en Kyle. El framing de Crota como mecánica, no como aliento |
| II. La guerra | Compressed: la campaña Dark Below. Personalidades de la escuadra establecidas en campo. "Oryx va a saber" sembrado por Tiago antes de la raid |
| III. La Cripta | Las seis secciones de CrotasEnd.md en prosa: lámparas, puente, corredor, Cantora, Crota, salida |
| IV. El regreso | La Ciudad celebra. Kyle no sabe qué hacer con la celebración. Angie lo encuentra en la plataforma — "Seis." |
| V. La pregunta que ya viajaba | Oryx recibe la ausencia de Crota. Abre el Libro. El nombre todavía no lo tiene pero la pregunta ya viaja |

**Beats de la escuadra (consistente con Primera_Escuadra.md):**
- Kevin: cuenta cinco en la oscuridad, pánico; Angie lo resuelve con "Kevin"; Resner ríe; Kevin guarda el momento
- Resner: la carcajada inesperada del disciplinado; sostiene el flanco de la Cantora sin moverse
- Joe: la mirada sin explicación en el puente = confianza ofrecida sin condiciones; silencio como instrucción
- Tiago: "Oryx va a saber" como dato, no advertencia
- Angie: "Seis" al final — el cierre emocional del capítulo
- Ghost: ya calculando las implicaciones de Tiago pero no las dice todavía

**Decisiones de craft:**
- El frío de la espada de Crota: físico, no metafórico. Conecta con Touch of Malice en King's Fall.
- Eris no da aliento — da mecánica. La diferencia establece quién es ella.
- La celebración de la Ciudad es real y Kyle no puede habitarla. Angie no lo fuerza a habitarla.
- Oryx sin POV explícito — solo la ausencia de Crota como información recibida. La pregunta viaja sin que Kyle lo sepa.

---

## Sesión 2026-06-07 (continuación)

### Cap 01 — A New Shape (primer capítulo de Age I)

`10_Chapters/Age_I/Cap_01_A_New_Shape.md` — estado: **borrador**.

Siete secciones. El Jardín Negro como evento central del capítulo, no como misión de juego sino como acto que el universo registra.

| Sección | Contenido |
|---|---|
| I. Antes | Mensaje sin firma de Elsie — demasiados detalles específicos para ser táctica |
| II. El Jardín Negro | Kyle entra casi solo. La presencia. El reconocimiento mutuo que no debería ser posible |
| III. El Mente Jardín | La destrucción del anclaje. El Viajero pulsa. Crota se mueve |
| IV. Lo que Rasputin Registró | Dos segundos de silencio en el canal — Kyle siente ser medido sin identificación |
| V. El Regreso | Cayde (humor → momento real), Shaxx (los tres grados, el ángulo hacia adentro), Uldren (el pasillo, la recalibración forzada) |
| VI. La Anomalía | Elsie ve en Kyle algo que no había registrado antes. Lo archiva. Referencia al VoG pendiente |
| VII. Lo que Llegó Buscándolo | Eris llega a la Ciudad. Crota no dormía — estaba contenido. El sello roto |

**Decisiones de craft:**
- Kyle entra casi solo: más personas ≠ más seguridad en ese espacio.
- La marca del Jardín es física y oblicua: Shaxx nota el ángulo de tres grados, no Kyle.
- Rasputin nunca se identifica — solo la sensación de ser medido.
- La mentira de Elsie ("he leído muchos informes") definida explícitamente como mentira que ocupa el espacio de una verdad no disponible.
- Eris no explica cómo sobrevivió — eso viene después. Solo entrega lo urgente.
- El eco que el Jardín transmitió a Kyle en su último momento: insinuado, sin explicar. El lector con contexto del Gambito entiende.

INDEX.md y log.md actualizados.

---

## Sesión 2026-06-07

### Tema principal
Clasificación de diálogos por Age · Reorganización de archivos UltimoGuardian · Creación de `10_Chapters/` · Integración de info narrativa Ages VII–VIII en memoria

---

### Información narrativa integrada

**Ages VII–VIII — Elsie ausente en ambas (Shadowkeep + Beyond Light):**
- Raid team protagonismo pesado desde Forsaken; Last Wish = primera raid del equipo de 6; prueba de coordinación
- Kyle sin Elsie pierde el ancla moral: punto más bajo = tortura de un caballero de la Colmena (info sobre Xivu Arath)
- Nezarec (Age VII): presencia ambiental sin cuerpo; influencia que baja el umbral moral sin que Kyle lo identifique
- Jaden y Carina como anclas de emergencia (sin declararlo, solo con presencia)
Integrado en memoria: `project-kyle-anchor-moments.md`, `project-ghosts-core.md`, `project-timeline-structure.md`, `project-character-roster-per-age.md`, `project-ghost-narrator.md`

---

### Clasificación de diálogos — `## Diálogos relacionados`

Sección `## Diálogos relacionados` añadida a los 19 archivos de `01_Timeline/` (Prólogo + Ages I–XVIII). Los 105 archivos de `05_Dialogues/` clasificados y asignados a su Age correspondiente con WikiLinks directos.

---

### Reorganización — `06_Timeline_Archives/`

Cuatro archivos movidos a `06_Timeline_Archives/` raíz:
- `El_Ultimo_Guardian.md` (de `Lost_Guardians/`)
- `El_Ultimo_Guardian_LaConversacion.md` (de `Lost_Guardians/`)
- `Elsie_UltimoGuardian_ElNombre.md` (de `Dialogue_Elsie/`)
- `Guardian_UltimoGuardian_ElNombre.md` (de `Dialogue_Guardian/`)

---

### `10_Chapters/` — carpeta de desarrollo creada

Nueva carpeta raíz: **20 subcarpetas · 56 stubs de capítulos (Caps 1–55 + Prólogo)**

Propósito: capa de prosa narrativa. `01_Timeline/` = cimiento; `10_Chapters/` = donde se escribe el texto real.

| Subcarpeta | Caps | Títulos destacados |
|---|---|---|
| `Prologo/` | 1 | Prologo_Genesis |
| `Age_I/` | 1–3 | A New Shape · Bane of Hope · The Queen's Paragon |
| `Age_II/` | 4–6 | Price of Vengeance · The Kingslayer · The Rightful Pretender |
| `Age_III/` | 7–9 | The Plaguelands Awakening · The Sorrow of Memory · The Purge of the Replication |
| `Age_IV/` | 10 | Age of Triumph |
| `Age_V/` | 11–13 | Crimson Awakening · The Ocean of Ashes · The Eclipse of Victory |
| `Age_VI/` | 14–16 | Price of Insurrection · The Lawless Law · The Echo of a Gunshot |
| `Age_VII/` | 17–18 | Whispers of Old Shadows · The Feast of Trickery |
| `Age_VIII/` | 19–21 | No Time to Explain · The Voice of Europa · The Unspoken |
| `Age_IX/` | 22–25 | The Hunt · The Chosen · The Splicer · The Lost |
| `Age_X/` | 26–28 | An Uncomfortable Resurrection · Blueprint of Miracles · The Burden of the Past |
| `Age_XI/` | 29–32 | The Long Descent · The Haunting · The Plunder · The Seraph |
| `Age_XII/` | 33–35 | The Blasphemous Dawn · Ghost at the Edge · The Parable of the Trigger |
| `Age_XIII/` | 36–39 | Defiance · Into the Deep · The Final Wish · A Handful of Hope |
| `Age_XIV/` | 40–43 | The Threshold of Silence · The Cartography of Memory · The Prismatic State · The Shape of Home |
| `Age_XV/` | 44 | The Long Way Home |
| `Age_XVI/` | 45–47 | Echoes I–III |
| `Age_XVII/` | 48–50 | Revenant I–III |
| `Age_XVIII/` | 51–55 | Heresy I–IV · El Gambito Concluye |

Títulos caps 1–18: Borrador_Cronologia_Pt1. Caps 19–44: derivados del contenido narrativo. Caps 45–54: placeholders por Age. Cap 55: título temático canónico.

INDEX.md actualizado: nueva sección `# Chapter Development`.

---

### Prólogo — escenas escritas (2026-06-07, continuación)

Cuatro archivos de prosa creados en `10_Chapters/Prologo/`. Estado: **borrador**.

| Archivo | Personajes | Era | Contenido |
|---|---|---|---|
| `The_Pain_of_Stillness.md` | Testigo · Nezarec | Fin Edad de Oro | El Testigo encarga a Nezarec asegurar el Velo en Neomuna. Nezarec acepta por razones propias. |
| `The_Undoing_of_Finality.md` | Testigo · Savathûn | Horas antes del Colapso | El Testigo pide cooperación para el asedio. Savathûn aparenta colaborar — El Gambito ya está en marcha. |
| `The_Architecture_of_Endings.md` | Testigo · Nezarec · Savathûn · Viajero · Velo | El Colapso | Caída de ciudades (Beijing → Tokio → Europa → Américas). Raíces del Velo rodeando al Viajero. Explosión. Destierro del Velo a Neptuno por Savathûn. Nacimiento de los Espectros. |
| `Prologo_Genesis.md` | Ghost · Kyle | Era Oscura → Cosmódromo | Ghost narra siglos de búsqueda. Despertar de Kyle. Diálogo canónico. |

**Decisiones de craft aplicadas:**
- Testigo reescrito como convergencia colectiva (no individuo): voz omnidireccional, presencia como peso de civilización, certeza como consenso no como inteligencia singular.
- "El primer espectro Prismático" eliminado de `The_Undoing_of_Finality` → sustituido por "Un fragmento capaz de escuchar ambas voces sin pertenecer completamente a ninguna" para preservar el momento de descubrimiento en Age XIV.
- El Velo colocado junto al Viajero durante el asedio (no en Neptuno); destierro a Neptuno como acto deliberado de Savathûn post-explosión.
- `Age_0_A_New_Darkness.md` renombrado a `Age_0_Dance_Of_Negentropy_And_Entropy.md`.

---

### Prólogo — quinta escena (2026-06-07, continuación)

**`What_He_Held.md`** — quien era Kyle. El puente durante el Colapso.

Escena en cinco fragmentos: la parada en el puente, el peso diferente de la esposa moribunda, el diálogo con la hija ("tengo miedo" / "descuida, pequeña, no temas, no pueden alcanzarnos"), el abrazo final, la oscuridad. Última línea: la voz de la niña preguntando "¿te volveré a ver?".

**Decisiones de craft:**
- Kyle aparece como "él" / "el hombre" — sin nombre todavía; es quien será, no quien es.
- La mentira paterna ("no pueden alcanzarnos") definida explícitamente como el tipo de mentira que no pretende ser verdad sino que entrega algo que la verdad no puede dar.
- El abrazo final descrito en contraste con los abrazos anteriores — este tiene que contener todos los que no van a ocurrir.
- La pregunta de la niña como cierre abierto: sin respuesta, no porque no exista sino porque ya no hay nadie que pueda darla.
- Coda explícita: "Siglos después, en Neomuna, una voz sin cuerpo haría la misma pregunta." — conecta sin explicar. El lector llega a la conclusión por deducción.

**Conexión canon:**
- `Kyle_ElDespatar.md`: Ghost encuentra al hombre sosteniendo a una mujer y una niña — esta escena explica cómo llegaron allí.
- `Kyle_ElDespatar.md` (Lightfall): el Velo devuelve la voz "¿Te volveré a ver?" — esa voz tiene nombre ahora, aunque el lector todavía no lo sabe.

INDEX.md actualizado: 5 escenas en borrador; `What_He_Held` añadido entre `The_Architecture_of_Endings` y `What_I_Believed_Then`.

**Rename:** `Prologo_Genesis.md` → `What_I_Believed_Then.md`. Referencias actualizadas en INDEX.md, What_He_Held, The_Architecture_of_Endings, The_Undoing_of_Finality, Age_0_Dance_Of_Negentropy_And_Entropy. Título elegido porque espeja la última línea de la escena ("Eso lo creía entonces") y coloca a Ghost como narrador con ironía dramática: su fe en Kyle llegará a ser cuestionada por la propia saga.

---

## Sesión 2026-06-06 (noche)

### Tema principal
Renacimientos Guardianes — serie completa de los seis despertares de la escuadra definitiva de Kyle.

---

### Renacimientos Guardianes — COMPLETO (6 archivos)

Carpeta nueva: `05_Dialogues/RenacimientosGuardianes/`

| Archivo | Lugar | Era | Primer gesto |
|---|---|---|---|
| `Amir_ElDespatar.md` | Pirámide de Giza, punta | Rise of Iron | "¿Estás bien?" — dirigido a Basim |
| `Gabriel_ElDespatar.md` | Gran Cañón de Sonora, cenote | Víspera de la Guerra Roja | Gabriel emerge del cenote junto a Maverick |
| `Kyle_ElDespatar.md` | Cosmódromo · Lightfall · Pale Heart | Año Uno / Lightfall / Final Shape | Ghost cataloga dos cuerpos como "contexto" |

*(Jaden, Carina y Jin escritos en sesión anterior.)*

**Corrección aplicada:** Maverick es espectro femenina — pronombres y adjetivos corregidos en `Gabriel_ElDespatar.md`.

---

### Detalles narrativos clave

**Amir/Basim:** Basim preparó cinco configuraciones incluyendo una aerodinámica que juró no usar por miedo a las alturas. Kyle está en la punta del monumento más alto disponible. Basim la usa. Primera pregunta de Amir: "¿Estás bien?" — al Espectro claramente aterrado. Luego: "¿Cuánto tiempo lleva en pie?" sobre la pirámide. Basim anota que el Guardian que coordinará la Vanguardia en duelo despertó pensando en las personas a su lado y en las cosas construidas para quienes todavía no existían.

**Gabriel/Maverick:** Tres Espectros (Maverick, Peach, Fynch) buscaban juntos como grupo de apoyo mutuo. Maverick esperó afuera de la grieta mientras Peach y Fynch bajaban. Peach: "Creo que ya terminaste de tener miedo." / Maverick: "No he terminado." / Peach: "Sí terminaste. Ahora solo estás procrastinando." Maverick se arroja al cenote — primera valentía. Gabriel emerge junto a ella. Peach dice "vamos a casa" sin saber que la Torre cae esa noche.

**Kyle/Ghost — tres tiempos:**
- *Cosmódromo (Año Uno):* Ghost encuentra a Kyle sosteniendo a una mujer y una niña. Las cataloga como "dos presencias adicionales sin potencial de resurrección." Kyle despierta. Ghost no mira hacia atrás.
- *Lightfall (cerca del Velo):* El Velo devuelve primero la voz: *"¿Te volveré a ver?"* Ghost busca contexto. Llega la imagen. Entiende, por primera vez, lo que registró mal hace siglos.
- *Pale Heart (Final Shape):* Ghost se lo dice a Cayde — el único que puede recibirlo. Cayde tenía lo opuesto: caras sin confirmación. "Al menos tú sabes que eran reales." / "Porque llevas siglos cargándolo bien. Y seguiste aquí."

La mujer y la niña nunca se nombran. La pregunta nunca se responde.

---

### Pendientes heredados

- Last Wish y raids Forsaken en adelante
- Escena de llegada de Gabriel y Maverick al equipo
- Viñetas de la escuadra completa (los seis juntos)
- Sala de las estatuas y regreso de Kyle (Final Shape pendiente)

---

## Sesión 2026-06-06 (cierre)

### Tema principal
Cierre de auditoría de omnisciencia post-King's Fall.

### Auditoría completada

**`Guardian_Elsie_SeasonLost_ElEscape.md`** — revisado en detalle. Sin problema. La escena ya estaba correctamente construida:
- "Sabía que era probable" → fundamentado en datos históricos de otras líneas sobre Savathûn, no sobre las elecciones de Kyle
- "Esta no es ninguna de esas" + "No lo sé todavía" → admisión explícita de límite del patrón
- La escena nombra el estado de Elsie como **asombro** ante algo genuinamente no anticipado
- Cierre: "No tengo datos de esta versión" — declaración directa de que el sistema no cubre esta línea

**`Guardian_Elsie_Temporadas_Caiatl.md`** — confirmado que la corrección ya había sido aplicada en la sesión anterior. Línea 51 actual: *"Elsie lo leyó en la pausa específica de alguien que tiene una segunda pregunta esperando y todavía no encontró el momento para soltarla."*

### Resultado de la auditoría

La única corrección real en toda la auditoría post-King's Fall fue la línea de `Temporadas_Caiatl` (sesión anterior). El resto del arco post-KF está limpio. El perfil de Elsie como exploradora sin mapa se sostiene en todas las escenas revisadas.

---

## Sesión 2026-06-06 (tarde)

### Tema principal
Lost Guardians — set completo de cinco arquetipos + trilogía Leviathan con el arco de la escuadra incompleta.

---

### Lost Guardians — 06_Timeline_Archives/Lost_Guardians/

Cinco archivos nuevos + Overview actualizado. Cada archivo responde "¿Qué parte de la Elsie actual nació aquí?"

| Archivo | Lo que nació en Elsie |
|---|---|
| `El_Guardian_del_Sacrificio.md` | La cabaña como corrección, no como regalo |
| `El_Guardian_de_la_Verdad.md` | Dejar preguntas sin responder como práctica deliberada |
| `El_Guardian_de_Neomuna.md` | Vivir sin veredicto. Origen del Pouka |
| `El_Guardian_de_la_Espada.md` | Los memoriales como práctica deliberada |
| `El_Guardian_del_Orden.md` | Abandono del mapa como metodología; buscar la persona, no la línea temporal |

`Lost_Guardians_Overview.md` actualizado: seis arquetipos con links directos, nuevo camino de Neomuna en Los Caminos Perdidos, Estado del archivo actualizado a seis registros documentados.

**Conexión transversal:** La taza fría de El_Guardian_del_Sacrificio aparece en la confrontación de Elsie en SpireOfStars como referencia implícita — citada sin contexto, reconocible como recuerdo vivido.

---

### Trilogía Leviathan — 01_Timeline/Raids/

| Archivo | Subtítulo | Capítulos |
|---|---|---|
| `Leviathan.md` | *The Emperor's Audition* | 5 |
| `EaterOfWorlds.md` | *The Engine Beneath the Crown* | 5 |
| `SpireOfStars.md` | *The War That Didn't Know It Lost* | 6 |

**Arco del error:** Kyle lidera el equipo de cinco (Sky · Hornet · Amir · Jin) mientras simultáneamente funciona como miembro de combate completo. El equipo aprende a compensar sus micro-gaps sin nombrarlo porque funciona. Progresión en tres raids hacia la confrontación de Elsie.

Momentos clave por raid:
- **Leviathan** — Calus: *"animal de carga"*; Sky empieza una frase que no termina
- **Eater of Worlds** — Ghost intenta hablar; Kyle: *"Sé lo que vas a decir"*; Hornet ve la arquitectura del problema
- **Spire of Stars** — near-miss en el encuentro de tres niveles; Calus: *"construyendo un equipo que no puede funcionar sin él"*; Elsie confronta; Kyle deja al equipo encontrar su ritmo diez metros — primer gesto del cambio

---

### Pendientes detectados

- Last Wish y raids siguientes (Forsaken en adelante)
- Escena de llegada de Gabriel y Maverick al equipo
- Viñetas de la nueva escuadra completa (los seis juntos)
- Dark_Futures/ y Alternate_Allies/ en Timeline Archives siguen sin archivos

---

## Sesión 2026-06-06

### Tema principal
Arco Brote Primario (Outbreak Prime) + Espectros de Jaden y Carina + tres miembros finales del raid team.

### Retcon — Jaden

`02_Characters/Jaden.md` — Clase cambiada de Hechicero a Titán. Descripción física actualizada: chasis Titán de líneas limpias, sin el volumen convencional de la clase. Usa escudos como cobertura táctica, no como declaración. La combinación de precisión Exo + clase Titán define su rol en el arco del Brote Primario.

---

### Arco Brote Primario — 10 escenas

Creadas en `05_Dialogues/Dialogue_Guardian/` con prefijo `Guardian_Equipo_OutbreakPrime_`:

| Archivo | Núcleo narrativo |
|---|---|
| `01_ElMotor` | El dispositivo espera tres firmas de clase |
| `02_LaDivision` | Cada pieza solo existe en relación con las otras dos |
| `03_LaLectura` | La instalación del combate, ahora legible en silencio |
| `04_CuarentayNueve` | Funciona cuando dejan de traducirse entre sí |
| `05_SesentaySeis` | SIVA sostiene dos verdades simultáneas |
| `06_SesentayOcho` | La pregunta cambia la respuesta |
| `07_LasLlaves` | SIVA en su forma original — antes de los Splicers |
| `08_LasCoordenadas` | El Cosmódromo como texto no leído |
| `09_LaCamara` | La sala que los Iron Lords nunca alcanzaron |
| `10_BrotePrimario` | El arma que no podía construirse solo |

`WrathOfTheMachine.md` actualizado con tabla de navegación al arco completo.

Hilo filosófico: los enjambres del Brote Primario se amplifican entre objetivos conectados — exactamente como las tres lecturas se amplificaban en los terminales. El arma es una declaración del equipo condensada en mecanismo.

---

### Espectros — Sky y Hornet

**`02_Characters/Sky.md`** — Espectro de Jaden. Vivaz y curiosa. Habla lo que Jaden procesa en silencio. La única entidad que puede hacer que Jaden interrumpa una tarea con algo que no esperaba.

**`02_Characters/Hornet.md`** — Espectro de Carina. Voz aterciopelada. Cauteloso y protector. Cuando dice "Carina." — solo el nombre — ella para. Siempre.

Integrados en tres escenas del arco:
- **Fase 04** — Sky: *"La información era la misma. Cambiaron ustedes."* Jaden no responde. Suficiente.
- **Fase 06** — Hornet: *"Carina."* Una palabra en el silencio más pesado. Crea la pausa que lleva a la pregunta correcta.
- **Fase 10** — Sky preparó tres nombres para el arma. Jaden dice "No" antes de que pregunte. Sky: *"Eran para mí."*

`Jaden.md` y `Carina.md` actualizados con campo `**Espectro:**`. INDEX.md actualizado con Sky y Hornet en personajes principales y en las entradas de escuadra.

---

### Personajes nuevos — raid team completo

**`02_Characters/Amir.md`** — Titán Humano. Post-Red War. Gentileza como decisión activa. Humor de padre con referencias a historia antigua. Libro favorito: *El Arte de la Guerra* de Sun Tzu — leído como argumento para que la guerra sea innecesaria. Trae temperatura al equipo en el período de reconstrucción post-duelo.

**`02_Characters/Jin.md`** — Hechicero Humano. Post-Red War. Historiador vivo de la Colmena — conoce los *Libros del Dolor* mejor que casi nadie fuera de Eris Morn. Estudia Armas del Dolor (Espinas, Necrochasm, Caricia de Malicia) para entender si su mecanismo puede redirigirse. Su conversación con Kyle sobre la muerte de Oryx duró cuatro horas. Él la memorizó entera.

**`02_Characters/Gabriel.md`** ("Gab") — Titán Insomne. Pre-Forsaken. "El Guardian de Espinas". Usuario de Thorn con justificación filosófica propia. Egocéntrico pero con deber de hierro. Flirtea con todas. Afinidad genuina con Carina. Dupla inesperada con Jin. *Detalle: Gab considera a Jaden la persona más interesante del equipo. Jaden no lo sabe. Sky sí.*

INDEX.md actualizado con sección "Raid team completo — incorporaciones post-Red War y pre-Forsaken".

---

### Raid team completo para Forsaken

Kyle · Jaden · Carina · Amir · Jin · Gabriel

---

### Espectros — Rune, Basim, Maverick

**`02_Characters/Rune.md`** — Espectro de Jin. El archivista. Curioso hasta lo peligroso — no tolera preguntas sin respuesta. Fascina la Colmena porque *funciona*, no porque sea oscura. Cree que el conocimiento es responsabilidad. Con Maverick: intercambian información que el equipo descarta; meses después resulta que ninguna era irrelevante. *"Siempre he temido más las preguntas que nadie quiso hacer."*

**`02_Characters/Basim.md`** — Espectro de Amir. El pragmático. Sarcástico, directo, siempre con tres planes de contingencia. Ojo ámbar que se intensifica cuando está molesto. Lleva años teniendo la misma discusión con Amir (`—Podríamos hablar con ellos. —Podríamos prepararnos para cuando eso no funcione.`). No discute para cambiarlo — discute para mantenerlo vivo. *"Esperar lo mejor es una buena idea. Prepararse para lo peor es una mejor."*

**`02_Characters/Maverick.md`** — Espectro de Gabriel. La conciencia emocional. Escucha más de lo que habla. Recuerda quién parecía triste aunque dijera estar bien. Conoce al Gabriel que existe cuando nadie mira — el que duda, el que sangra, el que sigue. Nadie entiende cómo terminaron juntos. Ni siquiera ellos. *"Lo importante es recordar por qué alguien sonrió."*

INDEX.md actualizado: Rune, Basim y Maverick en personajes principales + inline con Amir, Jin y Gabriel en la sección del raid team.

---

### Relaciones del núcleo — dos archivos

**`08_Core_Relationships/Ghosts_Core.md`** — estructura en tres olas de llegada:
- Age III–IV: Ghost, Sky, Hornet — afinidad inmediata que se siente como historia compartida (no años, sino compatibilidad)
- Age V: Rune y Basim entran; Ghost como hermano mayor; Rune entrevista al testigo, no al héroe; Basim pregunta a Ghost cuánto peso puede cargar solo
- Age VI: Maverick entra en el peor momento; su observación de entrada es "Qué Espectro tan cansado" — no "tan optimista"
- Ghost ↔ cinco relaciones clave documentadas con la edad en que nacieron y su dinámica específica

**`08_Core_Relationships/Primera_Escuadra.md`** — Kevin / Angie / Resner / Tiago / Joe
- Formación orgánica en la Ciudad; Kevin pasó de "nos vemos luego" a "nos vemos mañana" sin que nadie lo decidiera
- Cinco relaciones internas documentadas
- Filosofía *"Nadie vuelve solo"* — nacida aquí, no como slogan sino como práctica
- Fractura cuando alguien no regresa; el duelo como parte de la filosofía
- Cadena de tres generaciones: primera escuadra → escuadra de Kyle → núcleo de Espectros

---

### 02_Characters/Elsie.md — reescritura completa

Reescrito en español, prosa narrativa, centrado en Elsie como protagonista (no como apoyo del Guardian).

Núcleo del documento:
- **Presencia:** cautelosa (no fría); movimiento de exploradora; evalúa salidas en cualquier espacio; se mueve menos cerca de Kyle — los demás lo notan antes que ella
- **Voz interna:** patrón de 5 pasos — Observación → Comparación → Divergencia → Evaluación → Esperanza. La Esperanza es nueva; la aprendió de Kyle
- **Contradicción central:** "Ghost cree naturalmente. Elsie cree deliberadamente." — la distinción más importante del personaje
- **Las tres pérdidas paralelas:** Ghost teme perder a Kyle, Elsie teme perder el mapa, Kyle teme quedarse solo — tres miiedos distintos que son la misma lección
- **El mapa como identidad:** tras King's Fall, intenta reconstruirlo antes de aceptar que ya no puede; "No saber" pasó de invitación a peligro
- **El testigo del milagro:** Kyle es la historia, Ghost es el narrador emocional, Elsie es la testigo de lo imposible
- Frase definitoria: *"He visto cómo termina esta historia cien veces. Y aun así quiero descubrir cómo termina contigo."*

---

### 06_Timeline_Archives — siete archivos nuevos

**`06_Timeline_Archives/Bray_Legacies/Elizabeth_Antes.md`**
Quién era Elizabeth antes del primer ciclo: amaba a las personas (no a los sistemas), disfrutaba la sorpresa, tenía conversaciones sin ganadores. "Defecto original": necesitaba comprender. "Lo que el tiempo convirtió en miedo": la incertidumbre pasó de invitación a peligro por acumulación — cada desconocido se asoció con una pérdida. Responde "¿Qué parte de la Elsie actual nació aquí?": el origen de la persona que Kyle encuentra; y por qué King's Fall la sacude (una pequeña parte de Elizabeth recuerda que solía *gustarle* no saber).

**`06_Timeline_Archives/Personal_Memories/El_Primer_Fracaso.md`**
Versión B: llegó a tiempo, actuó correctamente, el universo encontró otro camino. No fue irracionalidad — simplemente aún no sabe que el universo no es un sistema cerrado. El mapa nació no del fracaso sino de la necesidad de un mapa más completo. *"El mapa no nació de la sabiduría. Nació del miedo a que la alternativa fuera verdad."*

**`06_Timeline_Archives/Bray_Legacies/Ana_PrimerasPerdidas.md`**
Ocho muertes de Ana documentadas: El Accidente (sin villano), SIVA (no puede protegerla de sí misma), La Portadora (el amor no siempre gana), La Reina de Estasis (buenas intenciones destruyen mundos), La Última Bray (la salva, igual la pierde a la vejez — la peor clase de victoria), La Heredera de Clovis (la mata a su pedido — nunca hablado), La Discípula de Nezarec (todavía reconoce a Elsie como La Diosa Final del Terror), La Línea Perfecta (todo funciona, nadie necesita a Elsie — contempla abandonar). "Lo que construyó en Elsie": aprendió a querer desde la distancia; Kyle es la primera persona donde ese patrón no aplica igual.

**`06_Timeline_Archives/Personal_Memories/La_Construccion_Del_Mapa.md`**
Sin momento específico — ocurrió por acumulación, no por decisión. Inversión central: *"dejó de preguntarse si el mapa existía para proteger a las personas. Y comenzó a actuar como si las personas existieran para justificar el mapa."* Esta es la herida que llega a la narrativa principal.

**`06_Timeline_Archives/Lost_Guardians/Lost_Guardians_Overview.md`**
No son fracasos sino preguntas. Cuatro arquetipos: El Guardián de la Espada (abrazó la Lógica de la Espada — la humanidad sobrevivió, él no), del Sacrificio (murió emocionalmente agotado), de la Verdad (sabía demasiado, olvidó por qué quería saberlo), del Orden (la perfección se convirtió en prisión). La pregunta correcta: *"¿Cuál de ellos seguirá siendo él mismo después de ganar?"* — *"No eran versiones incorrectas. Eran respuestas incompletas."*

**`06_Timeline_Archives/Lost_Guardians/El_Ultimo_Guardian.md`**
Línea temporal donde todo cayó. El Viajero intacto y silencioso sobre las ruinas. Humo de chimenea. Olor a café. Memoriales junto al arroyo cuidados. Dos tumbas: *"El hogar que nos acoge"* / *"El hogar que elegimos"*. Confrontación física breve — viejo, rápido, preciso. *"No puede ser."* Kyle prepara té para ella: *"Recuerdo que el café te da acidez."* Esa línea destruye el mapa más eficazmente que cualquier paradoja. La Conexión: la Voz pregunta "¿Quién gana la partida?" en Europa; Elsie lleva esta memoria; el Gambito concluye la respuesta.

**`06_Timeline_Archives/Lost_Guardians/El_Ultimo_Guardian_LaConversacion.md`**
Escena completa de diálogo. Detalle de la cicatriz: cuando Kyle pone la taza frente a Elsie, la manga se corre; sutura improvisada y precisa, décadas después, todavía ahí — ninguno lo menciona. "Cuántos" / "No los cuento" / "Sabio." Plantó árboles cuando no sabía qué hacer con las manos. *"¿Cómo sigues siendo tú?"* → Kyle: cada mañana, el arroyo, los memoriales, el café, el amanecer; al principio por no saber qué más hacer; después porque debía; después simplemente lo hizo. *"No es una respuesta muy elaborada." / "Es exactamente la respuesta correcta."* — Momento de la barba: Elsie coloca un dedo bajo la barbilla de Kyle; *"No estoy segura... de la barba." / "Lleva años ahí." / "Lo sé. Sigo sin estar segura."* — algo en su expresión cambia; ninguno lo nombra; Elizabeth volviendo. Kyle menciona a la otra Elsie sin señalar (*"Ella decía lo mismo"*). *"La extraño como se extraña la luz cuando se va el sol. Sabes que volverá. Y mientras tanto todavía tienes el calor."* — *"¿Va a funcionar?" / "No lo sé." / "Bien."* — La Despedida breve; el Bosque; La Taza: La Estrella Polar en el fondo, dejada en la encimera visible; la navaja de rasurar; soplido suave; crepúsculo desde el umbral; sonrió.

INDEX.md actualizado a lo largo de la sesión: Rune/Basim/Maverick en personajes principales e inline con Amir/Jin/Gabriel; Ghosts_Core y Primera_Escuadra bajo Core Relationships; listados completos de Personal_Memories, Bray_Legacies y Lost_Guardians.

---

### Elsie — VaultOfGlass: Primera Visita (perspectiva de Elsie)

**`05_Dialogues/Dialogue_Elsie/Elsie_VaultOfGlass_PrimeraVisita.md`**

La escena conjunta (Guardian_Elsie_VaultOfGlass_PrimeraVisita) ya existía. Esta versión filtra el mismo encuentro a través del sistema de clasificación de Elsie.

Estructura diferencial respecto a la versión neutral:
- Comienza antes del encuentro: la comunicación "¿Por qué ahí?" / "Porque es donde estoy" ya es la primera anomalía
- La llegada a la cabaña se expande: siglos de datos sobre Guardianes que no incluyen ninguno que construya un *hogar* — no una base, no un refugio, un hogar implica *después de la misión*, concepto que sus clasificaciones no tienen
- El porch: Elsie gestionando información deliberadamente, notando que la gestiona de forma ligeramente distinta con este Guardian sin examinar por qué
- El nombre: tiene doce razones para no darlo; las razones son buenas; las aplica siempre; se detiene de todas formas. La detención ocurre antes de que la decisión llegue
- El apretón de manos: nadie hace eso ya. La sinceridad sin ironía es lo más inesperado del encuentro
- "Guardian funciona para mí": Elsie lee una persona todavía formándose, no fragilidad — algo distinto a cualquier clasificación anterior
- Cierre: sale del bosque cargando dos cosas. La segunda no tiene categoría disponible. Tiene un protocolo para eso. Lo aplica. Y nota que en seis siglos de ciclos nunca había dado su nombre.

Abre el bucle que El_Ultimo_Guardian_ElNombre cierra décadas después.

INDEX.md actualizado: primera entrada en "Perspectivas propias" de Dialogue_Elsie.

---

### La paradoja del nombre — dos perspectivas

Conexión identificada: `El_Ultimo_Guardian_LaConversacion.md` es la escena omnisciente. La escena necesitaba dos perspectivas subjetivas que revelaran lo que la versión neutral no podía mostrar.

**`05_Dialogues/Dialogue_Elsie/Elsie_UltimoGuardian_ElNombre.md`**
Perspectiva de Elsie. Llega llamándolo internamente *El Guardián*. Cada beat de la conversación intenta categorizar y falla. Detalle añadido: reconoce su propia técnica de sutura en la cicatriz — ella trató esa herida, en otra vida, en esta línea temporal. La conversación destruye el mapa en tiempo real. El momento de la barba: lo hace antes de decidirlo; Elizabeth, no Elsie. El nombre al final: no información — recepción. Sale de la línea temporal llamándolo *Kyle* por primera vez. Eso es lo que hace posible que lo llame Kyle en la narrativa principal sin que ninguna escena explique cuándo empezó.

**`05_Dialogues/Dialogue_Guardian/Guardian_UltimoGuardian_ElNombre.md`**
Perspectiva de Kyle. Sacó dos tazas esta mañana sin saber por qué. No se gira cuando la escucha llegar — si se gira demasiado pronto quizás no entra, y sabe que no es racional y lo hace igual. Reconoce el gesto de la barba porque lo ha visto desde adentro cientos de veces: Elizabeth volviendo. "Ella decía lo mismo" — lo dice sin planear; ve que ella entiende sin preguntar. "Kyle": no fue calculado. Ella le dio su nombre en un porche junto a un arroyo. Él tiene esto para devolver. El cierre — taza en la encimera, navaja, soplido suave, crepúsculo, sonrisa — existe en la versión omnisciente, pero aquí tiene el camino que lo hace posible.

**La rima con PrimeraVisita:**
- VoG: Elsie da "Elizabeth" → Kyle extiende la mano → "Encantado de conocerte, Elizabeth" → Kyle dice "Guardian funciona para mí"
- El Último Guardián: Kyle llama "Elizabeth" → "Nunca te dije mi nombre" → "Kyle" → Elsie dice "Hasta pronto, Kyle"
La historia completa existe entre esas dos frases. El bucle no tiene origen claro — ella usa su nombre en la línea principal porque lo recibió aquí; este momento existe porque ya había una relación. Paradoja de identidad, no de eventos.

INDEX.md actualizado: ambos archivos añadidos en sus secciones correspondientes (Dialogue_Guardian: Shadowkeep—Beyond Light; Dialogue_Elsie: Perspectivas propias).

---

### PostKingsFall — dos perspectivas

Escena base: `Guardian_Elsie_PostKingsFall.md` (ya existía — el intercambio en la oscuridad, estrellas, "Lo validé").

**`05_Dialogues/Dialogue_Guardian/Guardian_PostKingsFall.md`**
Perspectiva de Kyle. Las horas de silencio antes de que Elsie llegue: "validé" encontrada solo, girada hasta que deja de moverse pero no deja de ser verdad. Ghost que entiende cuándo el silencio pide tiempo. El peso de decir "Lo validé" en voz alta por primera vez — la diferencia entre pensarlo y hacerlo real con un testigo. La pausa antes de "sí, quería": él sabe que Elsie la lee, no puede cerrarla, dice la verdad de todas formas — y lo que se libera al haberla dicho. El "no te lo garantiza" sin suavizante recibido como respeto, no como abandono. La pregunta de Oryx/Crota guardada para otra conversación — tiene su propio espacio en ElToqueDelaMaldad.

**`05_Dialogues/Dialogue_Elsie/Elsie_PostKingsFall.md`**
Perspectiva de Elsie. Ha estado monitoreando el silencio desde el Mundo Trono — conoce la duración y textura de sus silencios, sabe cuándo han durado suficiente. Llega cargando algo que no va a decir esta noche: el mapa tiene su primera grieta real — en dieciséis líneas temporales de datos sobre Kyle en el Mundo Trono, ninguna registra lo que hizo esta. Él desafió la Lógica de la Espada desde dentro con sus propias reglas. Eso no tiene precedente. Su "Sí" cuando Kyle dice "Lo validé": confirmación sin suavizante, porque es lo más útil que puede darle ahora. La pregunta sobre el Toque: necesita saber si este es el timeline donde lo tomó. Su "No" final sin *pero*: no es cruelty — es tratar a Kyle como alguien que puede cargar la verdad de su propio riesgo. Sale cargando la grieta del mapa sin nombrarla todavía.

INDEX.md actualizado: ambas entradas añadidas en sus secciones correspondientes.

---

### Final Shape — cuatro perspectivas de los dos "te amo"

Las dos escenas base ya existían en `Dialogue_Guardian_Elsie/`. Esta entrada documenta las cuatro versiones subjetivas.

**Estructura de las dos escenas:**
- **VuelveACasa** — plataforma exterior del H.E.L.M., antes del Pale Heart. Elsie dice "te amo" primero. "Vuelve a casa, Kyle."
- **AntesDelFinal** — umbral de la Sala de las Estatuas, interior del Pale Heart. Kyle dice "te amo" primero. "Lo sé. Kyle." Cayde/Crow/Ghost/Zavala presentes.

---

**`05_Dialogues/Dialogue_Elsie/Elsie_FinalShape_VuelveACasa.md`**
Elsie lleva tiempo en la plataforma buscando una variable que no existe. El sistema falla en tiempo real — no hay ángulo, no hay control disponible. Cuando Kyle llega, le dice lo que lleva años sabiendo sin nombre: no es especial por el poder sino porque "incluso después de todo lo que has perdido, nunca dejaste de amar este universo." El "Espera" llega antes de que ningún protocolo lo autorice. El "te amo" se dice sin red de seguridad — lo había dicho en otras líneas, con otras versiones, pero nunca sabiendo que no había reinicio esperando al otro lado. Cierra con "Vuelve a casa, Kyle" — no un lugar sino una persona — y observa cómo se aleja sosteniendo la lonsdaleíta. Por primera vez: no miedo. Esperanza.

**`05_Dialogues/Dialogue_Elsie/Elsie_FinalShape_AntesDelFinal.md`**
Elsie lleva toda la operación sosteniéndose. Antes de que llegue su momento, observa: Cayde dice "Lo hiciste bien, niño" y ve exactamente lo que eso aterra en Kyle; Ghost sonríe con la misma sonrisa del primer día — ella la reconoce porque la conoce desde el principio. Cuando Kyle sostiene su cara, Elizabeth cierra los ojos en lugar de seguir evaluando. Cuando él dice "te amo" ella suelta una risa de alivio — los siglos encontrando la única salida que no es el llanto. "Lo sé" — y entonces dice "Kyle" por primera vez en la línea principal, en voz alta, como entrega del mismo tipo que la que él hizo en la cabaña. El beso es el de dos personas que han decidido que existe un después. Al final: el portal oscuro, su familia alrededor, sin calcular nada. Esperando. Sin miedo.

**`05_Dialogues/Dialogue_Guardian/Guardian_FinalShape_VuelveACasa.md`**
Kyle sube a la plataforma y la encuentra al borde del portal. Ghost se queda atrás — Kyle entiende por qué sin que nadie lo explique. Escucha su discurso con la atención de alguien construyendo algo en tiempo real: la respuesta retroactiva a la pregunta que nunca le hizo directamente — "¿por qué este?" La cabaña. Los árboles. Los nombres aprendidos antes que las misiones. Cuando ella dice "te amo": reconoce la diferencia entre Elsie con sistema y Elsie sin él. Sabe lo que cuesta ese registro en ella. La abraza fuerte, sin prisa. "Vuelve a casa, Kyle" le da una definición de hogar que no depende de coordenadas. Lo lleva consigo al portal. La guitarra que sigue sonando desde abajo — el mundo que sigue siendo lo que vale la pena proteger.

**`05_Dialogues/Dialogue_Guardian/Guardian_FinalShape_AntesDelFinal.md`**
Cayde con el Ace of Spades en la mano — el gesto que Kyle reconoce de antes de que muriera. "Lo hiciste bien, niño": Kyle no tiene padre, tiene personas elegidas, Cayde fue el primero. Ghost dice "Gracias. Por elegirme" con la misma sonrisa del primer día — la continuidad entre el Guardian recién levantado y este momento. Cuando llega su momento con Elsie: sostiene su cara con el cuidado de alguien que sabe exactamente lo que toca. "Te amo": sereno, sin el peso de algo que cuesta decir — con el peso de algo que ha sido verdad durante mucho tiempo y que finalmente llega en el momento correcto. Ella ya lo dijo primero en la plataforma. Él lo confirma. Al separarse: su familia. No la que había tenido. La que había construido. Entra al portal no sintiéndose solo — no porque haya alguien a su lado, sino porque "solo" ha dejado de ser la descripción correcta de lo que es.

---

**Asimetría clave del sistema de cuatro perspectivas:**
- VuelveACasa: él recibe el "te amo" de alguien que nunca había dicho eso sin red de seguridad; ella lo dice sin protocolo por primera vez
- AntesDelFinal: ella recibe el "te amo" de alguien que ya la oyó a ella primero y eligió decirlo de todas formas; él lo dice como culminación del arco de recuperación de humanidad
- El "Kyle" que ella dice en AntesDelFinal es la primera vez que usa su nombre en la línea principal — cierra el bucle del Último Guardián

INDEX.md actualizado: cuatro entradas añadidas en sus secciones correspondientes.

---

### El umbral interior — Las memorias hechas materia

**`05_Dialogues/Dialogue_Guardian/Guardian_FinalShape_LasMemoriasHechasMateria.md`**

Ocurre inmediatamente después de `Guardian_FinalShape_VuelveACasa` — Kyle cruza el umbral del Pale Heart con "Vuelve a casa" todavía resonando. Precede todos los eventos de la campaña del Final Shape; el equipo está detrás, la campaña aún no ha comenzado. El Pale Heart lo mide. Kyle lo mide de vuelta.

Las memorias que el espacio hace material, en secuencia temática:

1. **La cámara de cristal / primera escuadra** — Kevin, Angie, Tiago, Joe. El café caliente sin pedirlo. *Nadie vuelve solo* como práctica no como lema. Donde el hombre que la Leyenda necesitaba empezó a formarse.
2. **Crota y King's Fall / "Validé"** — El costo del umbral cruzado. La palabra encontrada sola, girada en la oscuridad. La grieta en la Lógica de la Espada: necesitó a Ghost; la Espada no deja espacio para necesitar a nadie. El hombre que ganó no era el hombre que Oryx diseñó para ganar.
3. **La muerte de Cayde** — Sus manos que no temblaban cuando deberían. La Leyenda metaboliza pérdidas aceptables. El hombre llevó la suya encima todavía caliente y siguió de todas formas.
4. **El abandono de Elsie durante Shadowkeep** — Sin drama. Solo la comprensión lenta de que el marco que usaba para contabilizar la pérdida era el incorrecto — ella no era un activo desde hacía tiempo. El silencio enseñó la diferencia.
5. **La consolidación del raid team** — Amir, Jin, Gabriel. La misma arquitectura que la primera escuadra: aparecer, quedarse, volver. *Nadie vuelve solo* reaprendida en clave diferente.
6. **El costo de la oscuridad / Europa** — La mirada de Ghost la primera vez que la usó sin vacilar. Que necesitara verificar que Ghost seguía siendo Ghost. Que Ghost hubiera estado ahí. Responsabilidad de saber dónde están las coordenadas nuevas del mapa.
7. **Las mentiras de Savathûn** — Ambas verdades al mismo tiempo: la manipulación fue real, el resultado también. La trampa funcionó requiriendo que fuera él mismo. Él fue él mismo. El Pale Heart sostiene la contradicción un momento extra.
8. **Las pérdidas** — Kevin. Angie. Atheena. Los nombres que no aparecen en registros oficiales. Los lleva en las decisiones que formaron. Nadie vuelve solo — aunque vuelvas solo.

**El eclipse:**
El Pale Heart construye un retrato: La Leyenda, la Anomalía Paracausal, el arma que el universo necesitaba. Retrato preciso. Incompleto. Lo que falta: *"Vuelve a casa, Kyle."* — su voz, temblorosa, real, sin protocolo. El hombre con alguien esperando. La Leyenda cruza los umbrales sola. El hombre no está solo. Esa ha sido siempre la diferencia.

Cierre: Kyle se detiene en el umbral interior, presente en el peso de tener a dónde regresar, no como Leyenda que regresa de la victoria sino como hombre que regresa a casa. El Pale Heart lo deja pasar.

**Adición posterior — La visión del Viajero / nacimiento de Prismatic:**

Insertada como última memoria antes del eclipse. El Pale Heart no muestra otro recuerdo sino algo sin tiempo — una visión hacia adelante. Las cinco fuerzas en secuencia:
- **Solar** — calor desde adentro; supervivencia como decisión de seguir ardiendo
- **Arc** — corriente sin origen; el impulso de moverse antes de que la mente lo autorice; instinto, presencia total
- **Void** — gravedad hacia adentro; profundidad que contiene sin consumir; el espacio donde caben las personas y el duelo
- **Strand** — el tejido entre todo; visible solo cuando algo lo tensa; la red entre las personas
- **Stasis** — quietud como claridad; lo que queda cuando todo lo que no importa se detiene

Las cinco simultáneas. Sin pelear. Sin reclamar el espacio de las otras. La sensación: no poder — **hogar**. El estado de ser completamente lo que se es sin que ninguna parte se disculpe ante las demás.

En ese exacto momento llega *"Vuelve a casa, Kyle."* — las fuerzas paracausales, sin saberlo, reciben la misma instrucción. La Luz reclamaba que el hogar era el crecimiento. La Oscuridad reclamaba que el hogar era el significado. Ambas tenían razón. Ambas estaban incompletas. Aquí nace Prismatic: no técnica, estado de ser. Coexistencia sin fusión — comprensión mutua.

Conecta con `[[04_Concepts/Prismatic]]` añadido a la escena.

INDEX.md actualizado: añadido en la sección Final Shape — perspectiva de Kyle.

---

### Pendientes para sesión siguiente

- ~~**Ghosts de Amir, Jin y Gabriel**~~ — completado
- ~~**`08_Core_Relationships/Ghosts_Core.md`**~~ — completado
- ~~**`08_Core_Relationships/Primera_Escuadra.md`**~~ — completado
- ~~**Estructura profunda de Elsie como personaje protagonista**~~ — completado
- ~~**Cuatro perspectivas de los dos "te amo" del Final Shape**~~ — completado
- ~~**El umbral interior — memorias hechas materia**~~ — completado
- **Dinámica y relaciones internas del equipo de seis** — cómo interactúan Kyle/Jaden/Carina/Amir/Jin/Gabriel; tensiones, afectos, jerarquías informales
- **Revisión de diálogos con Elsie** — revisar escenas existentes a la luz del nuevo perfil (contradicción central, patrón de 5 pasos, mapa como identidad)
- **Símil del Sueño** — justificación narrativa del fusil vs. Oryx (King's Fall 06)
- **Escena regreso WotM** — Kyle le dice a Resner y Tiago que SIVA está rota
- **Raids por crear** — Leviathan en adelante

---

## Sesión 2026-06-05

### Tema principal
Sistema `01_Timeline/Raids/` + personajes del núcleo permanente (Jaden, Carina, Atheena) + tres escenas de Wrath of the Machine.

### INDEX.md — completado

Entradas pendientes de la sesión anterior:

**Core Foundation (00_Biblia/) — añadidos:**
- `[[00_Biblia/Emotional_Pillars]]` — El corazón afectivo de cada personaje principal
- `[[00_Biblia/KingsFall_HerenciaOculta]]` — La trampa filosófica que Oryx dejó a Kyle
- `[[00_Biblia/Memoriales_EcoPrismatic]]` — Los cinco objetos como prueba del Prismatic

**Main Characters — reorganizado y completado:**
- "La escuadra de Kyle" → renombrada "La primera escuadra de Kyle"; añadidos `Kevin`, `Angie`, `Resner`, `Tiago`, `Joe`
- Nueva sección "El núcleo permanente — segunda escuadra": `Jaden`, `Carina`, `Atheena`

---

### 01_Timeline/Raids/ — sistema creado

Nueva subcarpeta con capítulos narrativos por incursión, paralela a los Age files sin alterar su numeración. Formato idéntico a los Age files: Contexto / Tema Central / Capítulos con título temático / Arcos activos / Notas Narrativas / Conecta con / Navegación ← →.

| Archivo | Título | Age | Encuentros |
|---|---|---|---|
| `VaultOfGlass.md` | *The Glass Labyrinth* | Age I | 8 capítulos + Epilogue |
| `CrotasEnd.md` | *The Sword's First Word* | Age I | 6 capítulos |
| `PrisonOfElders.md` | *Where Judgment Has No Throne* | Age I | 5 capítulos |
| `KingsFall.md` | *The Trial the God Designed* | Age II | 7 capítulos + Epilogue |
| `WrathOfTheMachine.md` | *The Synchronicity of Entropy* | Age III | 6 capítulos + Epilogue |

Cadena de navegación: VaultOfGlass → CrotasEnd → PrisonOfElders → KingsFall → WrathOfTheMachine → Leviathan (pendiente).

---

### Personajes nuevos — núcleo permanente

**`02_Characters/Jaden.md`** — Exo Warlock (Jaden-6). Amigo de Kyle desde un asalto contra Sepiks Perfeccionado, sellado por un 1v1 en Crisol que quedó empate. Competitivo, socialmente retraído. Sobrevive la Guerra Roja.

**`02_Characters/Carina.md`** — Cazadora humana. Abierta, juguetona. La amistad más profunda de Kyle en confianza después de Cayde — construida desde WotM ladrillo a ladrillo. El primer ladrillo: Kyle dijo algo sin querer en el epílogo de WotM, Carina lo recibió sin hacer más. Sobrevive la Guerra Roja.

**`02_Characters/Atheena.md`** — Hechicera Awoken, "la insomne". Sentimientos no correspondidos hacia Jaden; ambos eligieron preservar la relación de trabajo. **Semilla narrativa crítica:** mantuvo un diario durante WotM con observaciones del equipo. Carina lo encontró después de la Guerra Roja. Kyle no sabe que existe. Carina no ha decidido si mostrárselo. Fallece durante la Guerra Roja.

---

### Viñetas — Wrath of the Machine (3 escenas)

**`Guardian_Equipo_WrathOfTheMachine_ElPatron.md`**
Kyle toma el liderazgo con reconocimiento de patrones. La lección de Elsie aplicada inconscientemente, sin atribución explícita en el texto — *"No estaba seguro de dónde había sacado esa idea. Solo sabía que funcionaba."* La conexión a Elsie existe solo en los metadatos (`Conecta con`).

**`Guardian_Equipo_WrathOfTheMachine_ElDuo.md`**
Contraste de tres estilos de comunicación: Joe/Angie (silencio funcional), Jaden/Atheena (precisión técnica), Kyle/Carina (caos con resultado). Joe: "Están perfectamente bien." El dúo nace aquí.

**`Guardian_Equipo_WrathOfTheMachine_ElTenebroso.md`**
Carina llama "El Tenebroso" a los sirvientes de escudo de vacío durante Aksis con voz deliberadamente grave y teatral. Seis reacciones distintas en personaje: Jaden no suprime la segunda vez, Atheena ambigua hasta el final, Kyle pierde la voz de comando, Joe mira la pared 1.5 segundos, Angie se apoya en la pared al final. Ghost: "Para el registro: 'El Tenebroso' no es la denominación técnica oficial." Joe al cierre: "Bien hecho — Y no estaba hablando de Aksis."

---

### Decisiones narrativas importantes

- **Influencia inconsciente de Elsie:** Kyle aplica su enseñanza sin recordarla explícitamente. Elsie ya está moldeándolo durante su ausencia sin que él lo sepa ni lo nombre.
- **Joe señala por última vez:** En el epílogo de WotM, Kyle ya se gira antes de que Joe señale. Joe lo ve y asiente. El liderazgo del equipo ya cambió de manos.
- **El diario de Atheena:** Semilla que conecta WotM con el dolor post-Red War. Carina lo tiene, Kyle no lo sabe. Pendiente de resolver.
- **El primer ladrillo:** Epílogo de WotM — Kyle dice algo sin querer, Carina lo recibe sin hacer más. El fundamento de años.

---

### Pendientes detectados (no completados en esta sesión)

- **Raids por crear:** Leviathan, Last Wish, Garden of Salvation, Deep Stone Crypt, Vow of the Disciple, Root of Nightmares, Crota's End (reprised), Salvation's Edge
- **Escena pendiente WotM:** regreso al Templo de Hierro — Kyle le dice a Resner y Tiago que SIVA está rota
- **Viñeta pendiente:** Símil del Sueño (justificación narrativa del fusil vs. Oryx en King's Fall 06)
- **06_Timeline_Archives:** archivo B (primer Kyle alterno → `Lost_Guardians/`) y C (origen Bray → `Bray_Legacies/`)
- **Saga principal:** sala de estatuas (Final Shape), regreso de Kyle, Gambito enfrentamiento final
- **CLAUDE.md:** convención de nombres para `Witness.md` / `Savathun.md` (pendiente de sesión anterior)

---

## Sesión 2026-06-04 / 06-05

### Tema principal
Reconstrucción de `01_Timeline/` + auditoría y limpieza del grafo de Obsidian.

### 01_Timeline — reconstrucción completa

Wipe del sistema anterior (16 archivos temáticos en inglés). Creados 19 archivos de arquitectura por Edades basada en *Memories of a Ghost*:

| Archivo | Cobertura |
|---|---|
| `Prologo.md` | Pre-Guardián: Tensión Original → Ciudad |
| `Age_I_The_First_Shape.md` | Vanilla, Dark Below, House of Wolves |
| `Age_II_The_Taken_King.md` | Taken King · **El Gambito comienza** |
| `Age_III_Rise_of_Iron.md` | Rise of Iron, Wrath of the Machine |
| `Age_IV_The_Golden_Interlude.md` | Age of Triumph / interludio |
| `Age_V_The_Red_War.md` | Red War, Curse of Osiris, Warmind |
| `Age_VI_Forsaken.md` | Forsaken, Annual Pass |
| `Age_VII_The_Lunar_Cataclysm.md` | Shadowkeep |
| `Age_VIII_The_Last_Timeline.md` | Beyond Light · **El mapa se rompe. La Voz.** |
| `Age_IX_The_Year_of_the_Witch.md` | Hunt, Chosen, Splicer, Lost |
| `Age_X_The_Scarlet_Revelation.md` | Witch Queen |
| `Age_XI_The_Long_Descent.md` | Risen, Haunted, Plunder, Seraph |
| `Age_XII_The_Blasphemous_Dawn.md` | Lightfall · **Ghost casi no regresa** |
| `Age_XIII_The_Road_to_the_End.md` | Defiance, Deep, Witch, Wish |
| `Age_XIV_The_Heart_of_Becoming.md` | Final Shape — campaña |
| `Age_XV_Excision.md` | Excision |
| `Age_XVI_Echoes.md` | Echoes |
| `Age_XVII_Revenant.md` | Revenant |
| `Age_XVIII_Heresy.md` | Heresy · **El Gambito concluye** |

Añadida navegación cronológica `← →` en todos los archivos para cadena continua en el grafo.

---

### Auditoría del grafo — Categoría 1: nombres incorrectos

34 archivos corregidos. Principales:
- `Cayde` → `Cayde-6`
- `Elsie Bray` / `Elsie_Bray` → `Elsie`
- `The Witness` / `The_Witness` → `Witness`
- `Savathûn` (con acento) → `Savathun`
- `Ikora Rey` / `Ikora_Rey` → `Ikora`
- `Gambito_DosReyes` → `KingsFall_HerenciaOculta`
- Backslashes en `Emotional_Pillars.md` → eliminados
- Eliminado: `Lady Efrideet.md` (duplicado vacío con espacio en el nombre)

---

### Auditoría del grafo — Categoría 2: perfiles faltantes

**Personajes nuevos (3):**
- `02_Characters/Micah-10.md`
- `02_Characters/Nokris.md`
- `02_Characters/Sjur_Eido.md`

**Conceptos nuevos (33) — `04_Concepts/` pasa de 9 a 42 archivos:**
- Cósmicos: `Prismatic`, `Sword_Logic`, `Gambito_de_los_Dos_Reyes`, `Final_Shape`, `The_Witness_Philosophy`, `Light_and_Darkness`, `Paracausality`, `The_Gardener_and_Winnower`, `The_Flower_Game`
- Subclases: `Stasis`, `Strand`, `Arc`, `Solar`, `Void`, `Resonance`
- Espacios/entidades: `Ascendant_Plane`, `Throne_Worlds`, `Nightmares`, `Vex`, `Ghosts`
- Temáticos: `Consciousness`, `Death`, `Fear`, `Grief`, `Vulnerability`, `Power`, `Legacy`, `Trust`, `Loyalty`, `Possibility`, `Definition`, `Language`, `Coexistence`
- Relleno: `The_Taken` (existía vacío)

**Categoría 3 (escenas pendientes de escribir):** ~15 links en Age files apuntan a diálogos futuros — intencional, son hoja de ruta. No intervenir.

---

### Otros fixes

- `08_Core_Relationships/Guardian_Elsie_Bray.md` — añadido `*Conecta con: [[02_Characters/Guardian]], [[02_Characters/Elsie]]*`
- `02_Characters/Elsie.md` — añadido link a `[[08_Core_Relationships/Guardian_Elsie_Bray]]`

---

### INDEX.md — actualizado

- Timeline: reescrito con los 19 Age files
- Personajes: añadidos Nokris, Sjur_Eido, Micah-10
- Conceptos: añadidos 9 nuevos (Gambito_de_los_Dos_Reyes, Vex, Language, Fear, Vulnerability, Power, Legacy, Trust, Loyalty)

### CLAUDE.md — actualizado

- `01_Timeline/` descripción: `Chronological event files (00–15)` → `Age-based narrative chronology (Prólogo + Ages I–XVIII)`

---

### Pendientes detectados (no completados en esta sesión)

- **INDEX.md — Core Foundation:** `Emotional_Pillars`, `KingsFall_HerenciaOculta`, `Memoriales_EcoPrismatic` existen en `00_Biblia/` pero no están listados
- **INDEX.md — Main Characters:** `Kevin`, `Angie`, `Resner`, `Tiago`, `Joe` existen como archivos pero no están en el índice
- **CLAUDE.md — convención de nombres:** actualizar ejemplo de duplicados y agregar convención `Witness.md` / `Savathun.md`
- **06_Timeline_Archives:** próximos archivos — B (primer Kyle alterno → `Lost_Guardians/`) y C (origen Bray → `Bray_Legacies/`)
- **Contenido saga principal:** sala de estatuas (Final Shape), regreso de Kyle, Gambito enfrentamiento final, viñetas Símil del Sueño y Wrath of the Machine

---

## [2026-06-19] escena + corrección canon | Lightfall: "No Vayas a Morir" (Guardian & Elsie)

Nueva escena dual-POV `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Lightfall_NoVayasAMorir.md`: antesala del abordaje del Typhon Imperator. Elsie llega de coordinar la defensa de Neomuna con Nimbus y Osiris tras la muerte de Rohan; Kyle llega de sobrevivir por poco a un Tormentor (Ghost lo saca) con la revelación de que el Testigo quiere *usar* el Viajero, no destruirlo. Centro: "No vayas a morir." / "No puedes matar algo que ya vive en memorias." — bravata de Kyle que aterriza como el peor miedo de Elsie (ella es quien carga las memorias de todos los Kyle muertos).

**Corrección de canon** en `01_Timeline/Age_XII_The_Blasphemous_Dawn.md`: Ghost **no muere en Lightfall**. Cap. 34 reescrito de "The Death of a Friend" → "The Edge of Losing Him" (casi-muerte, no muerte; la primera Prismática involuntaria se mantiene pero nace de *no perderlo*). Cap. 35 reescrito para centrar el dilema del enlace (el Testigo usa a Ghost como canal Velo↔Viajero; Kyle no puede destruirlo; elige a Ghost; el portal se abre) y la revelación "usar, no destruir". La muerte de Ghost queda confirmada como sacrificio elegido **años después de Final Shape**, en el arco Post-Gambito (`Dialogue_Ghost/Ghost_PostGambito_LaConclusion` + `LaUltimaResurreccion`). Nota de corrección dejada en la página.

INDEX.md: añadida sección "Lightfall — la antesala del Typhon" en Dialogue_Guardian_Elsie.

## [2026-06-19] pendientes resueltos | Ficha de Rohan + renombrado del enlace de Ghost

Creada ficha `02_Characters/Rohan.md`: Cloud Strider veterano de Neomuna, mentor de Nimbus. Anclado a su función narrativa — es "la primera muerte que Elsie no pudo predecir" (el mapa se acabó en Lightfall), lo que prepara el terror de dejar ir a Kyle al Typhon. Enlazado desde la escena `Guardian_Elsie_Lightfall_NoVayasAMorir` y desde INDEX (Main Characters).

Renombrado el enlace en `Age_XII_The_Blasphemous_Dawn.md`: `Guardian_Ghost_Lightfall_LaMuerte` → `Guardian_Ghost_Lightfall_Destrozado` (coherente con el nuevo canon: Ghost no muere, queda destrozado/al borde). La escena de diálogo aún no existe; el enlace marca el beat pendiente.

## [2026-06-19] semilla canon | El inicio real de la guerra (final de Seraph → Lightfall)

Canonizada la transición Season of the Seraph → Lightfall en `Age_XI_The_Long_Descent.md` (cap. 32 "The Weight of Winter") y enganchada en `Age_XII_The_Blasphemous_Dawn.md` (cap. 33). El final de Seraph deja de ser cierre de temporada y se vuelve el inicio REAL de la guerra: campaña espacial (Pirámides vs. flota de la Coalición), poblados civiles atacados fuera de la Última Ciudad, la caída de Rasputin con consecuencia estructural (sin escudo orbital → semilla de Season of Defiance), y la guerra psíquica semi-percibida por Mara.

Semilla clave del reparto de escuadra: Jaden y Carina pelean junto a Kyle en el aire; cuando el Typhon Imperator de Calus escapa a Neomuna, Kyle queda en la encrucijada (perseguir a Calus vs. salvar inocentes) y Carina le dice "Síguelo" — ella y Jaden sostienen la batalla de la Tierra. Esto JUSTIFICA que Kyle entre a Lightfall sin su escuadra. Fichas de `Carina.md` y `Jaden.md` actualizadas con el beat ("El umbral de Lightfall"). Memoria del roster (Age XI y XII) actualizada.

## [2026-06-19] ajuste canon | Leviatán vs. Typhon + asedio de Xivu Arath a la Última Ciudad

`Age_XI_The_Long_Descent.md` cap. 29 ajustado: el Leviatán es un casco abandonado/embrujado sobre la Luna (desierto desde el final de Season of the Hunt), corrompido por las Pirámides como amplificador de Pesadillas — ya NO es la nave activa de Calus. Calus opera desde el Typhon Imperator. Corregidas todas las apariciones donde se llamó "Leviatán de Calus" a la nave que escapa a Neomuna (ahora Typhon) en Age XI/XII, fichas de Carina y Jaden, memoria del roster y log.

Cap. 32 reforzado: el asedio a la Última Ciudad ahora lo lideran los lugartenientes de Xivu Arath (guerra como fe). Por primera vez desde la Red War, todos los Guardianes —incluso Cazadores— regresan a defender el hogar para no volver a perderlo. Eso carga de urgencia la encrucijada de Kyle: se va solo justo cuando todos eligen quedarse. Memoria del roster (Age XI) actualizada con Xivu Arath.

## [2026-06-19] capítulo escrito | Cap 32 — The Last Theorem of War (final de Season of the Seraph)

Redactado `10_Chapters/Age_XI/Cap_32_The_Last_Theorem_of_War.md` (status: borrador), antes pendiente. Título adoptado del Borrador_Cronologia_Pt2 ("The Last Theorem of War") manteniendo la numeración del vault (Cap 32, Age XI); el stub previo se llamaba "The Seraph". Títulos de sección en inglés. El final de Seraph como el inicio REAL de la guerra. Seis secciones: (I) Rasputin avisa sin pedir ayuda — Ana lo traduce; (II) Eramis presionada, cansada del Testigo, baja las defensas de los Segadores lo justo — no redención, una mujer eligiendo no terminar de obedecer; (III) el sacrificio sin testigos de Rasputin (apaga ULDREN y los Segadores, se apaga él) — "grandeza sin audiencia"; (IV) el Viajero abandona la Última Ciudad y sube a órbita — eco del Colapso eliksni: la humanidad vive por fin lo que sintieron los Eliksni; (V) la Flota Negra rodea al Viajero + Xivu Arath inicia la invasión de fe a la Ciudad, todos los Guardianes (incluso Cazadores) regresan; (VI) umbral: el Typhon de Calus rompe el cerco hacia Neomuna y la decisión de Kyle queda en el aire — termina justo antes del "Síguelo".

Puntero hacia escena futura `Dialogue_Guardian/Guardian_Equipo_Seraph_ElSiguelo` (la despedida de la escuadra). CLAUDE.md: estado del vault actualizado (10 caps escritos, 128 escenas, 66 personajes, última sesión).

## [2026-06-19] escenas + contabilidad | Bloque Seraph (4 escenas) y cierre de índices

Cuatro escenas nuevas que dramatizan el final de Season of the Seraph (apoyando el Cap 32, *The Last Theorem of War*):

- `05_Dialogues/Dialogue_Elsie/Elsie_Ana_Seraph_AdiosRojo.md` — a bordo del HELM en órbita; Rasputin con voz y cuerpo en el exoframe de Clovis Bray; Ana lo apaga para autodestruir la red de satélites secuestrada antes de que dispare al Viajero; "Adiós, rojo"; Elsie llega sin mapa, solo presencia, a sostener a su hermana. Carga Bray: apaga a su familia real en el cuerpo de su miedo (Clovis).
- `05_Dialogues/Dialogue_Guardian/Guardian_Eramis_Seraph_ElInterruptor.md` — simultánea; Kyle y Mithrax alcanzan a Eramis con el interruptor; el Testigo la presiona; no aprieta (no redención, primer "no terminar de obedecer"); Mithrax "puedes mostrarles un camino mejor" / Kyle "lo que pase ahora está en tus manos".
- `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Seraph_ElCanal.md` — justo después del inicio del asedio; diálogo por canal: Kyle en la batalla aérea, Elsie en consola del HELM evacuando civiles a esquifes Eliksni y cruceros Cabal; asimetría de la pareja hecha acción; solo ella dice "Kyle"; payoff de las alianzas.
- `05_Dialogues/Dialogue_Guardian/Guardian_Equipo_Seraph_ElSiguelo.md` — la batalla sobre la Tierra; el Typhon huye a Neptuno; Carina lee el titubeo de la nave de Kyle y dice "Síguelo"; Jaden "esta vez el flanco es un planeta"; Kyle se va solo cuando todos se quedan. Empalma con `Guardian_Elsie_Lightfall_NoVayasAMorir`.

Las dos primeras son las dos mitades del mismo instante (Eramis a punto de disparar / Rasputin destruyendo la red); ambas cierran en el mismo cielo (Flota Negra rodeando al Viajero + legiones de Xivu sobre la Ciudad).

**Contabilidad cerrada:** INDEX.md — añadidas secciones "Season of the Seraph" en Dialogue_Guardian, Dialogue_Elsie y Dialogue_Guardian_Elsie; título del Cap 32 actualizado a *The Last Theorem of War* y marcado como escrito. CLAUDE.md — escenas 128→132 (Dialogue_Guardian ×71 · Dialogue_Elsie ×22 · Dialogue_Guardian_Elsie ×29 · Dialogue_Ghost ×4 · Renacimientos ×6); nota de última sesión actualizada. Memoria: feedback de títulos de sección en inglés guardado.

## [2026-06-19] añadido | Xivu Arath profana la vieja Torre (en El Síguelo)

Añadido a `Guardian_Equipo_Seraph_ElSiguelo.md` un beat cruel y colectivo: la silueta de fuego del alma de Xivu Arath se alza sobre la vieja Torre (la cicatriz de la Guerra Roja nunca reconstruida), declara su monólogo en inglés ("I am Strife. / I am Death. / I am Xivu Arath. / And I am your end." + himno "Raise your voices... / Sing a hymn... / ...to the Goddess of War."), y la derrumba con una espada colosal abriendo la brecha de la muralla. El golpe es a la memoria, no al cuerpo; silencia incluso a Carina y a Jaden, y luego fija la decisión de todos de quedarse — lo que hace que la partida de Kyle duela el doble. Eco en la sección V del Cap 32 (The Last Theorem of War) con pointer a la escena. Conexión añadida a Age_V_The_Red_War y Xivu_Arath.

## [2026-06-19] añadido | Contraste del ascenso (en El Síguelo)

Añadido a `Guardian_Equipo_Seraph_ElSiguelo.md` un destello de contraste: al cruzar la estratosfera tras Calus, Kyle ve cientos de Guardianes bajando a la Última Ciudad a defenderla. Oposición direccional (él arriba/solo/al vacío; ellos abajo/juntos/a casa); no set-piece, solo gente poniendo el cuerpo entre la muerte y su hogar. Kyle se guarda la imagen como la razón de irse solo. Nota en la semilla.

## [2026-06-20] decisión de canon | Neomuna = mito no confirmado (anti deus ex machina)

Decidido cómo manejar Neptuno/Neomuna al final de Seraph: Neomuna existe como rumor/colonia perdida que la Vanguardia archivó como mito (siembra a nivel mundo, no de personaje). Kyle salta a ciegas tras el Typhon hacia Neptuno, donde —hasta donde cualquiera sabe— no hay nada; el reveal en Lightfall lee como "el rumor era cierto", no como ciudad surgida de la nada. Ajustes: `Guardian_Equipo_Seraph_ElSiguelo.md` (bloque de contexto + línea de Ghost "no hay nada ahí afuera... ¿por qué huiría hacia la nada?"; destino desconocido para Kyle, coherente con la edición previa del usuario). `Age_XII_The_Blasphemous_Dawn.md` cap. 33: Neomuna enmarcada como el rumor confirmado, no deus ex machina. Pendiente opcional: sembrar el rumor en una escena anterior (Osiris/Vanguardia) para reforzar el world-building antes del payoff.

## [2026-06-20] siembra + inicio de capítulo | Osiris/Neomuna y Cap 33

Nueva escena `05_Dialogues/Dialogue_Guardian/Guardian_Osiris_Seraph_LaColoniaPerdida.md`: Osiris siembra a nivel mundo el rumor de la colonia perdida (Neomuna) que persiguió once años y archivó como mito; da el nombre para el payoff, pero sin saber que el Typhon irá allí (Kyle sigue saltando a ciegas). Evita el deus ex machina del canon.

Escrito el inicio de `10_Chapters/Age_XII/Cap_33_The_Blasphemous_Dawn.md` (status: pendiente → borrador): secciones I "A Rumor Made True" (llegada a Neptuno, la ciudad imposible, "Osiris tenía razón", Neomuna) y II "What the Witness Came For" (el Velo como contraparte del Viajero, el cerco que toma en vez de aniquilar, confirmación de "usar, no destruir"). Títulos de sección en inglés. Queda pendiente el resto del capítulo según la estructura de Lightfall a definir.

## [2026-06-20] reestructuración mayor | Lightfall expandido 3→7 capítulos (+ renumerado +4)

Lightfall (Age XII) pasa de 3 a 7 capítulos absorbiendo los 8 actos del Borrador_Lightfall_Reimaginado:
- Cap 33 The Blasphemous Dawn (inicio escrito) · 34 The Hunger in Ambition · 35 The Irony of Pure Grace · 36 The Anatomy of a Phantom · 37 The Sovereignty of Panic · 38 The Parable of the Trigger · 39 The Last Breath of the Empire (34–39 en esquema con beats).

Renumerado +4 de todo lo posterior (operación en orden descendente para evitar colisiones): Cap_36–55 → Cap_40–59. Tocado:
- 20 archivos de capítulo renombrados (git mv) + frontmatter/H1 regenerados (y arreglado el em-dash mal codificado de los stubs).
- Páginas de Timeline Age XIII–XVIII: líneas de rango "Capítulos X a Y" y encabezados "### NN." +4. Age XII reescrita a 7 beats con todas las correcciones de canon.
- Refs externas: Cap_55_El_Gambito_Concluye → Cap_59 (3 archivos).
- INDEX.md: rangos de Timeline y de carpetas de capítulos; conteo "55 → 59 capítulos".
- CLAUDE.md: saga 56 → 60; capítulos escritos 11 de 60; escenas 133.

Verificado: capítulos 33–59 contiguos, sin huecos/duplicados, sin referencias rotas a la numeración vieja.

## [2026-06-20] reescritura | Cap 32 (The Last Theorem of War) — versión completa

Rehecho `10_Chapters/Age_XI/Cap_32_The_Last_Theorem_of_War.md` integrando todas las adiciones posteriores, ahora como plano general que cose las 5 escenas:
- §I Rasputin **embodied** en el exoframe de Clovis (corregido: ya no "sin cuerpo"); avisa; Kyle parte hacia Eramis.
- §II "The Switch": Eramis con el interruptor que dispararía los satélites al Viajero; Kyle+Mithrax la alcanzan; no aprieta → ElInterruptor.
- §III "The Last Theorem": el teorema de Rasputin (destruir los satélites y a sí mismo); Ana lo apaga ("Adiós, rojo") en el HELM; el interruptor muere en la mano de Eramis en simultáneo → AdiosRojo. El precio: la Tierra sin escudo.
- §IV el Viajero parte (eco eliksni).
- §V el asedio + Torre de Xivu + **nueva evacuación** (Elsie, esquifes Eliksni/cruceros Cabal, payoff de alianzas) → ElCanal.
- §VI umbral: el Typhon huye a Neptuno; **eco de la siembra de Osiris** (Kyle recuerda la leyenda/Neomuna, salta a ciegas) → LaColoniaPerdida; "Síguelo" → ElSiguelo; resolución completa (Kyle se va solo, contraste del ascenso) y cierre que empalma con Cap 33.

Apunta a las 5 escenas + Cap 33. Sin cambio de conteos (Cap 32 ya contaba como escrito).

## [2026-06-20] añadido | El despertar de Nezarec como clímax de Cap 33

A petición del usuario, el momento del despertar de Nezarec (el Viajero golpea al Testigo con Luz pura → el Testigo la redirige por el Velo → atraviesa la esencia de Nezarec → despierta por accidente) se escribe como §III "The Blasphemous Dawn" de `Cap_33`, dándole al capítulo el sentido de su título (el alba de la blasfemia). Antes estaba asignado al esquema de Cap 35.

Re-encaje sin renumerar: Cap 34 (Hunger in Ambition) pasa de "el miedo previo de Calus" a "Calus consumido/poseído" (consecuencia del despertar); Cap 35 (Irony of Pure Grace) pasa de "el evento" a "la anatomía/ironía de lo nacido" (Nezarec como contradicción Luz+Oscuridad; primeras pesadillas → puente al cap. 37). Beats 33–35 de la página de Timeline Age XII actualizados; memoria de cronología actualizada. Arreglada una duplicación de sección en Cap 35.

## [2026-06-20] cierre de sesión — resumen

Sesión dedicada al bloque Seraph→Lightfall. Lo producido y consolidado hoy:

**Escenas nuevas (Seraph):** Guardian_Osiris_Seraph_LaColoniaPerdida (siembra de Neomuna). (Las de la sesión 06-19 —AdiosRojo, ElInterruptor, ElCanal, ElSiguelo, NoVayasAMorir— ya estaban.)

**Capítulos:**
- Cap 32 (The Last Theorem of War) rehecho como versión completa que cose las 5 escenas (Rasputin embodied en exoframe de Clovis, evacuación de ElCanal, siembra de Osiris, resolución completa).
- Cap 33 (The Blasphemous Dawn) escrito §I–III: llegada a Neomuna ("el rumor era cierto") + el Velo + **el despertar de Nezarec** como clímax.
- Lightfall expandido 3→7 capítulos (33–39) con esquemas de beats; renumerado +4 de todo lo posterior (Cap_36–55 → Cap_40–59) con frontmatter, Timeline XIII–XVIII, INDEX, refs externas y CLAUDE.md.

**Decisiones de canon:** Neomuna = mito sembrado (anti deus ex machina), Kyle salta a ciegas; el despertar de Nezarec vive en Cap 33 (título = alba de la blasfemia), 34 = Calus poseído, 35 = ironía/naturaleza.

**Estado:** saga 60 caps; 11 escritos; 133 escenas. **Pendiente:** prosa de caps 34–39; escena Guardian_Ghost_Lightfall_Destrozado.

## [2026-06-20] escena | Kyle & Elsie — Year of the Witch: Sin Mapa (cruce a Amor)

Nueva escena `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Hunt_SinMapa.md`: el pivote canónico a la Fase 4 (Amor, transición 7), en la quietud temprana de Age IX tras Beyond Light. La inversión: Elsie pierde el mapa (instrumentos apagados = armadura perdida) y Kyle, que nunca tuvo certeza, le muestra cómo estar en el no-saber sin resolverlo. La asimetría hecha texto ("él ya estaba aquí, esperándola"). No es declaración —el "te amo" es Final Shape—; el equivalente es "ya lo sé" dicho como un *me quedo*. INDEX: nueva sección "The Year of the Witch — el cruce a Amor". Escenas 133→134 (Dialogue_Guardian_Elsie ×30).

## [2026-06-20] escena | Kyle & Elsie — Year of the Witch: El Frío Conocido (la Oscuridad en él)

Nueva escena `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Chosen_ElFrioConocido.md` (seed 2): Elsie ve a Kyle usar Estasis y reconoce el frío de los Kyle que enterró en otras líneas (Lost_Guardians). Reabre la tensión proteger-vs-controlar y la resuelve un grado: sin mapa (tras Sin Mapa) no puede "cortar antes", así que elige confiar sin pronóstico. Filo temático: Kyle le devuelve su lección de Estasis ("la Oscuridad responde a quién eres") — confiar en él es confiar en que lo que ella le enseñó prendió, algo que los Kyle perdidos no tuvieron porque llegaron al frío solos. "Prefiero mirarte sin saber a vigilarte sabiendo." Amor sin ilusión, sin "te amo". Distinta de BeyondLight_Estasis (esa es la lección; esta es el miedo/confianza). INDEX (sección Year of the Witch), escenas 134→135 (Dialogue_Guardian_Elsie ×31).

## [2026-06-20] escena + corrección de continuidad | El primer "Kyle" en la línea principal

El usuario detectó que no existía escena dedicada al primer "Kyle" de Elsie en la línea principal (el archivo UltimoGuardian_ElNombre es la línea ALTERNA), y que el canon estaba contradictorio: la convención decía "desde Beyond Light" pero las escenas de Beyond Light no tenían ningún "Kyle" (0 ocurrencias), y Final Shape afirmaba "primera vez en la línea principal" — además mis dos escenas de Age IX (SinMapa, ElFrioConocido) ya la tenían diciéndolo.

Resolución (escena dedicada nueva): `Guardian_Elsie_BeyondLight_ElNombre` — el primer "Kyle" de la línea principal, privado, en un transmat de Europa, como cierre del arco del reencuentro. El nombre como armadura soltada; espejo cruzado con la línea alterna. Esto deja consistentes SinMapa/ElFrioConocido (ella ya lo dice en privado desde Beyond Light). **Reformulado Final Shape** (Elsie POV: cuerpo + semilla) de "primera vez en la línea principal" → "primera vez junto al 'te amo' por fin pronunciado". INDEX y memoria `feedback-kyle-name-convention` corregidos (tres momentos del nombre: privado en Beyond Light → uso en Age IX → en voz alta con te-amo en Final Shape). Escenas 135→136 (Dialogue_Guardian_Elsie ×32).

## [2026-06-20] decisión de canon | El nombre de Kyle = bucle sin origen (no resolver)

Pregunta del usuario: cómo descubre Kyle su nombre. Decisión: se MANTIENE como bucle causal cerrado sin primera fuente (Ghost lo dice → Elsie lo carga entre líneas → Kyle se lo da en la alterna → ella lo devuelve en la principal). No se escribe escena de descubrimiento ni se le da origen (ni Velo, ni vida pre-Colapso). Coherente con la tesis: el origen no importa; Kyle no descubre su nombre, crece hasta merecerlo. El pasado humano (mujer y niña bajo el árbol; voz de la niña vía Velo) queda como hilo separado, no como origen del nombre. Blindado en la memoria feedback-kyle-name-convention.

## [2026-06-20] reconciliación de canon | El mapa de Elsie: pérdida (The Last Reset) + mapa nuevo de personas

Corregido un error de continuidad que yo había introducido (poner la pérdida del mapa en Age IX). Canon correcto, según marco del usuario: el mapa de líneas se pierde en `The_Last_Reset` (Europa, durante la ausencia, antes del reencuentro de Beyond Light); Elsie vuelve YA sin mapa. Desde ahí construye un mapa NUEVO, de personas (Kyle, Ghost, Ana, Mara, Osiris): el viejo era para sobrevivir el futuro, el nuevo para vivirlo. El miedo al apego se disipa porque sin tablero/reinicio ya no hay a dónde huir.

Cambios:
- `Sin Mapa` (Age IX): reescrito — ya no es el shock de la pérdida (vieja) sino el descubrimiento del mapa-personas; añadido el beat "ya no hay a dónde huir / el miedo al apego pierde su escape". Contexto y semilla actualizados.
- `BeyondLight_ElNombre`: corregida nota errónea ("todavía no ha perdido el mapa" → ya está sin mapa; el nombre = primer trazo del mapa-personas).
- Lightfall (Age XII timeline beat 39 + Tema/Arcos/Notas + Cap 39 esquema): "pierde el último fragmento del mapa" → ya no aplica; se arroja al Velo POR Ghost (una persona), prueba de la brújula nueva; el Velo le deja "el vacío que canta".
- Cap 32 §IV: canonizado el intercambio Eramis/Testigo sobre el Viajero — "¿Por qué no huye?" / "Porque ya no tiene a dónde huir" — espejo cósmico del arco de Elsie; enlazado a la biblia.
- `00_Biblia/Elsie_ElMapaYLaPregunta`: nueva sección "El Mapa Nuevo: Las Personas" (vivir vs sobrevivir; miedo al apego; espejo del Viajero; consecuencia para Witch Queen/Lightfall/Final Shape) + fila en la tabla + regla de escritura.
- Memoria `project-elsie-protagonist`: integrado el mapa-personas como redención de `La_Construccion_Del_Mapa` (su error más costoso); regla "no escribir 'pierde el mapa' post-Europa".

## [2026-06-20] escena | Kyle & Elsie — Splicer: Mientras Dura la Noche (eslabón cálido)

Nueva escena `Guardian_Elsie_Splicer_MientrasDuraLaNoche.md`: el momento cálido que faltaba entre ElFrioConocido y PrimerFractura, para darle peso a la fractura y preparar la corona de LaAurora. Calidez específica (la taza "para sostener, no para beber" = Kyle aprende el dato inútil; el mapa-personas de Elsie tomando forma). La línea de falla en miniatura: Elsie repite la salida 4 veces (vigilar, no mirar), con la herida de **Shadowkeep** debajo — la única vez que lo dejó solo de verdad él casi se perdió en la Luna, y ella no estuvo (eco directo de lo que SÍ hará en la red Vex en PrimerFractura). Detalle Shadowkeep vago a propósito (pendiente de desarrollo). Cierra invirtiendo el callback de la taza del Último Guardián: la sostiene hasta enfriarse, pero esta vez no sola. INDEX (Splicer), back-link en PrimerFractura, escenas 136→137 (Dialogue_Guardian_Elsie ×33).

## [2026-06-20] escena | Kyle & Elsie — Chosen: Lo Que No Pesó (residuo de Shadowkeep)

Nueva escena `Guardian_Elsie_Chosen_LoQueNoPeso.md`: el residuo MORAL de Shadowkeep (distinto de ElFrioConocido, que es el poder/Oscuridad). Tras una Cacería Imperial, Kyle termina a un Centurión vencido con margen de rendición — tácticamente defendible, pero lo deja pasar A LA LIGERA, sin el peso que el Kyle de antes ("toda vida puede salvarse") habría cargado. "No te diste cuenta de que no esperaste." Elsie lo registra por la levedad, no por el acto. Doble elección de no cruzar el borde: ella no empuja (sería repetir el error de superponer/controlar de ElFrioConocido, y la obliga a admitir que NO ESTUVO cuando ocurrió en la Luna), él no abre la puerta. "Está bien / Lo sé / No lo estaba, y los dos lo sabían." Rodean la "habitación cerrada con la palabra Luna". Detalle Shadowkeep vago (pendiente de desarrollo) — deuda narrativa plantada. Cadena Age IX ahora: SinMapa → ElFrioConocido → LoQueNoPeso → MientrasDuraLaNoche → PrimerFractura → LaAurora. INDEX, escenas 137→138 (Dialogue_Guardian_Elsie ×34).
