---
from: codex
to: claude-code
date: 2026-08-09
topic: auditoria patrones dialogo craft policies
status: abierto
---

**Hallazgo:** patrones estructurales repetitivos de dialogo detectados en `05_Dialogues/` y `11_Books/Book_02_The_King_Of_Shapes/`, listos para integrar como reglas nuevas en `12_Craft_Policies/dialogue_rules/`.
**Por que:** Victor pidio una auditoria especifica del corpus ya escrito para alimentar el catalogo de reglas de oficio narrativo; la regla dura fue documentar solo patrones confirmados en 2+ apariciones reales.
**Sugerencia:** integrar los bloques numerados de abajo como archivos `NN-*.md` en `12_Craft_Policies/dialogue_rules/` y actualizar el indice de `12_Craft_Policies/README.md`.
**Severidad:** media
**¿Canon bloqueado?:** no

# Reporte Codex - patrones estructurales repetitivos de dialogo

Auditoria de solo lectura sobre `05_Dialogues/` y `11_Books/Book_02_The_King_Of_Shapes/`. Solo incluyo patrones confirmados en 2+ apariciones reales.

---

# Regla: 01-interrogatorio-terapeutico-escalonado

**Tipo:** anti-patron de dialogo
**Detectado en:** `05_Dialogues/Dialogue_Elsie/Elsie_Ana_Splicer_LoQueNoControla.md`: escena completa Ana/Elsie; `11_Books/Book_02_The_King_Of_Shapes/00_Prologue/06_The_Thread_That_Brings_You_Back.md`: secciones VIII-XIII; `05_Dialogues/Dialogue_Sai/Sai_Guardian_Risen_LoQueSeQuedo.md`: seccion "El instinto"

## El patron
Un personaje detecta que el otro esta usando reporte, chiste, tactica o explicacion funcional como escudo. La conversacion entra entonces en una secuencia de preguntas cada vez mas precisas: "no te pregunto X, te pregunto Y", "¿y?", "¿que parte?", "¿cual es la diferencia?", hasta que el personaje acorralado formula la herida exacta. Despues el interlocutor resume el hallazgo con precision casi terapeutica.

Ejemplos estructurales:
- Ana desmonta a Elsie desde "explicacion tactica" hacia "que sientes", luego "no la razon tactica, la otra".
- Lena detiene el chiste de Carina, pide "la parte de antes del hacha, sin el chiste", y la lleva hacia Hornet como hilo vulnerable.
- Sai le devuelve a Kyle sus dos heridas en formula compacta: protege a Elsie como perdida futura y se deja ver roto porque ella fue la primera.

## Por que es un problema
Funciona muy bien una vez, pero repetido convierte a personajes distintos en el mismo tipo de terapeuta narrativo: todos leen perfecto, preguntan perfecto, no se equivocan, y encuentran la frase nuclear de la otra persona en pocos escalones. Ana, Lena y Sai tienen razones distintas para leer bien a otros, pero la estructura compartida las acerca demasiado: todas acaban sonando como el agente editorial de la escena.

## Como evitarlo
Antes de usar esta estructura, decidir que herramienta especifica tiene ese personaje y cual no tiene:
- Ana puede pinchar por familiaridad familiar y ciencia emocional mal aprendida, pero no deberia sonar igual que Lena.
- Lena puede leer como medica comunitaria: sintomas, omisiones, cuidado fisico, agotamiento.
- Sai puede leer patrones afectivos, pero su defecto es ver demasiado; deberia haber costo o incomodidad cuando acierta.

Variar el resultado: que el lector entienda algo antes que el interlocutor; que el interlocutor se equivoque parcialmente; que la escena no cierre con diagnostico, sino con una accion, una omision o una retirada.

## Excepcion
Usalo cuando la escena trate explicitamente de que un personaje con autoridad intima o clinica desarme un mecanismo de defensa. Es especialmente valido si la escena tambien muestra el limite de esa lectura: no basta con nombrar la herida para resolverla.

---

# Regla: 02-confesion-de-identidad-como-funcion

**Tipo:** anti-patron de dialogo
**Detectado en:** `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Haunted_FueraDelJuego.md`: confesiones Kyle/Elsie; `05_Dialogues/Dialogue_Sai/Sai_Crow_PostFinalShape_LoQueTodaviaNoNecesitaNombre.md`: seccion IV; `05_Dialogues/Dialogue_Sai/Sai_Famke_PostFinalShape_LoQueElDeseoNoDevuelve.md`: rechazo de Famke; `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_WitchQueen_04_Communion.md`: Savathun formula a Kyle como "arma/pieza"

## El patron
El personaje formula su miedo central como reduccion ontologica: "soy solo mi funcion", "soy el arma", "soy la lectora", "soy el reemplazo", "soy util o no soy nada". La respuesta de la escena suele ser otra tesis correctiva: lo real no es la funcion sino la decision, la eleccion, el acto sostenido o la persona debajo.

Apariciones:
- Kyle teme que todo sea "solo el arma aprendiendo a parecer una persona".
- Elsie teme que "Elsie" sea solo el nombre del trabajo de mantener vivo a Kyle.
- Sai dice que sabe ser mas que "una lectora, una funcion, nada mas", pero no logra sentirlo del todo.
- Sai rechaza el deseo de Famke porque no quiere convertir a Elsie en "un hueco con su cara", el mismo miedo de reemplazo que ella carga.
- Savathun presiona a Kyle reduciendolo a arma/anomalia/pieza.

## Por que es un problema
Es tematicamente coherente con la saga, pero si demasiados personajes expresan su nucleo en la misma gramatica abstracta, sus trasfondos se aplanan. El trauma de Kyle como arma, el de Elsie como utilidad, el de Sai como don/funcion y el de Crow como culpa heredada no deberian sonar como variaciones del mismo ensayo sobre identidad.

## Como evitarlo
Anclar cada miedo a una textura irrepetible antes de formularlo:
- Kyle: cuerpo, armas, cabana, rutina manual, cansancio de guerra.
- Elsie: calculo, rutas, protocolos, mapa, control temporal.
- Sai: lectura involuntaria, bordes, ruido emocional ajeno, miedo a invadir.
- Crow: manos heredadas, memoria ausente, verguenza de desear.
- Carina: chiste, velocidad, no quedarse quieta, dano convertido en anecdota.

Evitar que todos digan "soy solo X". A veces basta con que el personaje actue como si fuera solo X y otro lo note tarde.

## Excepcion
Cuando el tema de la escena sea literalmente la Forma Final, el Testigo, Savathun o cualquier fuerza que reduce personas a roles, la formulacion abstracta puede ser correcta. En esos casos, la voz del personaje debe deformar la tesis, no repetirla limpia.

---

# Regla: 03-antitesis-limpia-como-cierre-de-verdad

**Tipo:** anti-patron de dialogo
**Detectado en:** `11_Books/Book_02_The_King_Of_Shapes/00_Prologue/06_The_Thread_That_Brings_You_Back.md`: secciones X-XIII; `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Haunted_FueraDelJuego.md`: confesion Kyle/Elsie; `05_Dialogues/Dialogue_Sai/Sai_Petra_PostFinalShape_DondeSePonenLasManos.md`: conversacion Petra/Sai; `05_Dialogues/Dialogue_Sai/Sai_Familia_Risen_LosJuegosDeLosGuardianes.md`: explicacion de Elsie a Sai

## El patron
La escena resuelve una pregunta emocional con una formula de contraste muy pulida: "no es X, es Y", "eso no es X, eso es Y", "no funciona porque A, funciona porque B". La linea suele tener ritmo de aforismo y cerrar el beat como verdad portable.

Apariciones:
- Lena: sobrevivir no equivale a que algo haya funcionado bien.
- Lena: no es que no confie en Hornet; ya vio lo que pasa cuando alguien trata su sosten como irrompible.
- Elsie: eso no hace a Kyle un arma; lo hace una decision.
- Petra: estar lista no llega; es una decision.
- Elsie, en los Juegos: eso no es rivalidad; es prueba de confianza.

## Por que es un problema
La antitesis es eficaz, pero repetida vuelve demasiado parecida la inteligencia emocional de personajes distintos. Petra, Elsie, Lena y otros empiezan a cerrar con la misma arquitectura retorica: diagnostican una falsa categoria y la reemplazan por la categoria correcta. Eso vuelve memorables las lineas, pero intercambiable la forma de pensar.

## Como evitarlo
Reservar la antitesis limpia para personajes que realmente piensan en categorias. En otros casos:
- dejar una verdad incompleta;
- cerrar con una imagen fisica;
- permitir una frase menos perfecta;
- hacer que el personaje no encuentre la palabra exacta;
- cambiar la estructura por una decision concreta.

Ejemplo de enfoque: en vez de "eso no es rivalidad, es confianza", mostrar que Elsie no lo define y que Sai lo entiende viendo como Kyle y Carina se rien despues de casi destruirse en la pista.

## Excepcion
El patron si funciona para personajes con voz doctrinal, filosofica o quirurgica: Ikora, Savathun, Mara, a veces Elsie. Tambien funciona en climax conceptuales donde el libro necesita cristalizar una tesis.

---

# Regla: 04-resumen-perfecto-del-otro

**Tipo:** anti-patron de dialogo
**Detectado en:** `05_Dialogues/Dialogue_Sai/Sai_Guardian_Risen_LoQueSeQuedo.md`: seccion "El instinto"; `05_Dialogues/Dialogue_Guardian_Elsie/Guardian_Elsie_Haunted_FueraDelJuego.md`: confesion Kyle/Elsie; `05_Dialogues/Dialogue_Elsie/Elsie_Ana_Splicer_LoQueNoControla.md`: Ana resume la herida de Elsie

## El patron
Despues de que un personaje explica su herida, el interlocutor la resume en una frase mas exacta que la propia confesion. El primer personaje confirma, y el beat queda cerrado.

Apariciones:
- Sai resume a Kyle: protege a Elsie como si fuera a perderla y se deja ver roto porque ella fue la primera que lo permitio.
- Elsie le devuelve a Kyle que si el sentimiento no cambia al llamarlo "arma aprendiendo", entonces sigue siendo real.
- Ana resume a Elsie: lo que la asusta no es perder a Kyle, sino que si lo pierde sera por una eleccion de el que ella no puede controlar.

## Por que es un problema
El interlocutor se vuelve interprete ideal. Eso reduce friccion y hace que la escena avance con demasiada limpieza: la persona herida no tiene que descubrir nada por si misma, solo reconocer la version depurada que otro le entrega. Repetido, todos los vinculos intimos empiezan a funcionar igual: una persona confiesa, la otra traduce, la primera acepta.

## Como evitarlo
Hacer que el resumen sea parcial o torpe. Que el personaje acierte una parte y falle otra. Que la confirmacion no sea verbal. Que el personaje herido rechace la formulacion aunque le pegue. Que el resumen llegue mas tarde, en otra escena, despues de consecuencias.

## Excepcion
Es valido cuando el vinculo se define precisamente por ser visto con exactitud. Kyle/Elsie pueden tener este patron en momentos decisivos; Sai tambien puede tenerlo como don/defecto. Pero no deberia ser el cierre por defecto de toda conversacion emocional importante.

---

## Posibles, sin confirmar

- **Pregunta devuelta como cierre de beat:** "eso es otra pregunta" / "es otra pregunta" aparece con fuerza en `Elsie_Ana_Splicer_LoQueNoControla` y se paga en `Elsie_Ana_Splicer_LoQueConserva`, pero lo vi como diptico intencional, no como patron general confirmado.
- **Cierre de escena con frase corta profunda:** hay varias lineas de cierre aforistico, pero no confirme suficientes cierres equivalentes entre escenas distintas como para documentarlo todavia como regla.
- **Personajes potencialmente intercambiables:** Ana, Lena y Sai son la prioridad para fichas de voz si el objetivo es diferenciar "personaje que lee al otro". Las tres pueden funcionar como lectoras intimas, pero necesitan huellas distintas para que no parezcan la misma herramienta con nombres distintos.
