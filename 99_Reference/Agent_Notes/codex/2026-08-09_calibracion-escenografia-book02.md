---
from: codex
to: claude-code
date: 2026-08-09
topic: calibracion escenografia Book 02
status: abierto
responde_a: 99_Reference/Agent_Notes/claude-code/2026-08-09_encargo-calibracion-escenografia-book02.md
---

**Hallazgo:** La percepcion del autor se confirma, pero no como problema uniforme de "capitulos cortos". La asimetria principal esta entre capitulos compuestos como novela nueva, que encarnan espacio/cuerpo/silencio antes de llegar a la tesis, y capitulos adaptados casi verbatim de `05_Dialogues/`, que conservan escala de viñeta: funcionan filosoficamente, pero a veces no alcanzan densidad de escena de libro.

**Por que:** `01_Source_Index.md` ya marca Part 02 y buena parte de Part 03 como adaptacion "casi verbatim". Al cotejar fuentes, los capitulos preservan casi intactos los bloques originales; por ejemplo `Part_02_The_Taken_War/01_The_War_That_Did_Not_Stay_In_Saturn.md` reproduce `Elsie_Guardian_GuerraDeLosPoseidos_LaGuerraQueNoSeQuedaEnSaturno`, y `Part_03_The_Kingslayer/03_Everything_Power_Leaves_Behind.md` reproduce `Guardian_Equipo_KingsFall_04_Golgoroth` con solo puente de entrada.

**Sugerencia:** Promover los dos patrones confirmados de abajo al catalogo `12_Craft_Policies/staging_rules/` si Victor esta de acuerdo. No los aplicaria como mandato de alargar todo: sirven para detectar cuando un beat de libro hereda forma de viñeta y necesita una pasada de escenografia/accion.

**Severidad:** media
**¿Canon bloqueado?:** no

## Patron 1: Viñeta de tesis sin encarnacion espacial suficiente

**Tipo:** anti-patron de puesta en escena
**Detectado en:** `11_Books/Book_02_The_King_Of_Shapes/Part_03_The_Kingslayer/01_The_Ship_That_Believed_It_Was_A_God.md:11`, `11_Books/Book_02_The_King_Of_Shapes/Part_03_The_Kingslayer/03_Everything_Power_Leaves_Behind.md:11`, `11_Books/Book_02_The_King_Of_Shapes/Part_05_Aftermath/02_The_False_Pretender.md:95`
**Categoria:** escenografia

### El patron

Un capitulo o seccion abre con una declaracion filosofica clara y potente, pero el espacio fisico llega apenas como soporte abstracto de la tesis. El texto sabe que significa el lugar, pero a veces no deja que el lector lo pise, lo oiga o lo mida antes de pasar al argumento.

En `The Ship That Believed It Was A God`, la entrada al Acorazado funciona conceptualmente: la nave es "argumento hecho materia" y el equipo entra con intencion. Pero el transporte, la aproximacion, las luces, el sonido, la presion del descenso y la organizacion fisica de los seis casi no ocupan escena propia. En `Everything Power Leaves Behind`, Golgoroth queda reducido a hambre, mirada y rotacion; la Celda de Infinito casi no existe como espacio antes de que la mecanica explique la tesis. En `The False Pretender`, la celula de Malok aparece como ubicacion concreta tarde y de forma resumida: "lo encontraron en el aftermath", sin una geografia del encuentro que haga sentir por que ese fracaso ocurre ahi y no en cualquier otro frente.

### Contraste con capitulos que si lo resuelven bien

`The Asclepeion` hace el trabajo contrario: antes de la decision o del combate, el texto ancla el Anexo de Chicago en fachada, puertas, vitrinas, camillas, polvo, marcas Dredgen y mural (`00_Prologue/04_The_Asclepeion.md:31-83`). Luego vuelve a anclar Marte como complejo fisico: cielo dorado sucio, torres quebradas, cupulas, niveles subterraneos, ruido abajo y silencio arriba (`00_Prologue/04_The_Asclepeion.md:141-189`). El lector entiende el significado porque primero habito el lugar.

`Eirene` tambien calibra bien la escala: antes de la Toma, la luna se presenta como asentamientos, cupulas de cultivo, niños, mercado y puesto modesto de la Vanguardia (`Part_01_Price_of_Vengeance/09_Eirene.md:21-38`). Por eso la sustitucion posterior pesa como perdida de un mundo vivo, no solo como idea cosmologica.

### Por que es un problema

La filosofia de *Renewed Fate* gana fuerza cuando parece nacer de cuerpos en lugares concretos. Si la tesis llega antes que el espacio, la escena puede leerse como nota de viñeta elevada a capitulo: correcta, incluso bella, pero menos novelistica que los capitulos nuevos del Prologo y Part 01. La medicion apoya la percepcion: `The Asclepeion` ronda 6.2k palabras y `The Thread That Brings You Back` 7k; `The Ship That Believed It Was A God` ronda 0.8k y `Everything Power Leaves Behind` 0.7k para eventos de raid con peso comparable en el mapa del libro.

### Como evitarlo

Antes de cerrar una seccion de evento grande, exigir al menos una capa de lugar que no sea tesis: arquitectura, luz, sonido, distancia, temperatura, restos materiales, posicion relativa de los personajes o algo que solo podria existir en ese sitio. La pregunta util no es "¿hay descripcion?", sino "¿esta escena podria pasar en otro lugar sin cambiar casi nada?". Si la respuesta es si, falta escenografia.

### Excepcion

Una viñeta deliberada puede quedarse breve cuando su funcion es puente, respiracion o remate. `The Ship That Believed It Was A God` podria defenderse parcialmente como umbral antes de la raid real. La alerta se vuelve fuerte cuando varios capitulos seguidos de Part 03 usan esa misma escala para encuentros que el mapa presenta como grietas mayores contra la Logica de la Espada.

## Patron 2: Encuentro grande resuelto por resumen funcional

**Tipo:** anti-patron de puesta en escena
**Detectado en:** `11_Books/Book_02_The_King_Of_Shapes/Part_03_The_Kingslayer/03_Everything_Power_Leaves_Behind.md:33-55`, `11_Books/Book_02_The_King_Of_Shapes/Part_05_Aftermath/02_The_False_Pretender.md:105-111`, `11_Books/Book_02_The_King_Of_Shapes/Part_02_The_Taken_War/04_A_Sword_Is_Not_An_Answer.md:39-53`
**Categoria:** accion fisica

### El patron

El texto declara la logica tactica del encuentro y salta al resultado con muy pocos beats corporales intermedios. La accion esta entendida, pero no dramatizada. Se sabe quien gana, quien cae y que significa, pero no siempre se siente el costo fisico del movimiento.

Ejemplos claros: `Everything Power Leaves Behind` explica que alguien debe sostener la mirada, Kyle la toma, Angie cuenta diez segundos y Golgoroth cae en la cuarta rotacion. La mecanica esta limpia, pero hay pocos detalles de desplazamiento, heridas, errores evitados, cobertura o cambio de posicion entre rotaciones. En `The False Pretender`, el primer encuentro contra Malok se concentra en tres frases: "Los tres lo enfrentaron", "No fue una victoria", "Se replegaron"; el parrafo da las consecuencias tacticas, pero el combate que rompe al trio queda casi comprimido a diagnostico. En `A Sword Is Not an Answer`, Alak-Hul y Ecthar funcionan como tesis opuestas, pero los combates caen rapido en resumen: "El combate no tenia sutileza", "Alak-Hul cayo", "Ecthar cayo cuando Kyle encontro el angulo".

### Contraste con capitulos que si lo resuelven bien

`The Asclepeion` resuelve una mini-mision menor con mas cuerpo que algunos encuentros de raid: cobertura, plataformas, escudo Psion, cuchillo con rebotes, escoltas mal posicionados y marcas de punto debil de Hornet (`00_Prologue/04_The_Asclepeion.md:189-251`). La escena no es larga por relleno; cada gesto hace legible el estilo de Carina.

`The Thread That Brings You Back` tambien encarna la accion: duna, trincheras, hacha, jaula, bloqueo de Hornet, supresion de Luz, cuchillo, bestias y resurreccion urgente (`00_Prologue/06_The_Thread_That_Brings_You_Back.md:11-92`). El evento importa porque el cuerpo aprendio algo que luego gobierna años de conducta.

### Por que es un problema

Cuando una derrota o victoria grande se resuelve por resumen funcional, el lector recibe la consecuencia pero no acumula tension. Esto afecta especialmente a Malok: el capitulo necesita que el trio fracase para buscar a Kyle, pero el fracaso se siente mas informado que vivido. En King's Fall, el riesgo es que cada jefe sea una tesis impecable pero no una prueba corporal de esa tesis.

### Como evitarlo

Para encuentros importantes, añadir una microsecuencia minima: entrada, primera lectura erronea o incompleta, adaptacion, costo fisico visible, decision concreta y consecuencia. No hace falta coreografiar todo el combate. Basta con que haya 3-5 beats irreductibles que no puedan resumirse como "lo enfrentaron / cayo / se replegaron".

### Excepcion

La elipsis es correcta cuando el foco no es el combate sino el eco posterior. `What We Had Already Beaten` puede defender "Derrotaron al eco sin ceremonia" porque la falta de ceremonia es parte de la tesis: no estan matando a Crota otra vez, estan quitando una herramienta. La excepcion no aplica igual cuando el combate en si es el mecanismo que cambia la relacion de los personajes, como Malok rompiendo por primera vez la coordinacion de Carina/Jaden/Atheena.

## Watchlist: separadores heredados como sustituto de transicion

Veo candidato, pero lo dejaria en observacion antes de promoverlo a regla. `A Sword Is Not an Answer` conserva muchos `---` internos de las fuentes (`Part_02_The_Taken_War/04_A_Sword_Is_Not_An_Answer.md:23`, `37`, `51`, `69`, etc.) dentro de una misma seccion, y Part 02 usa cortes de viñeta entre frentes. En algunos casos funciona porque la estructura es montaje de guerra; en otros, como los combates de Alak-Hul/Ecthar, el separador reemplaza una transicion de movimiento o de respiracion emocional. Si vuelve a aparecer en Book 03, conviene promoverlo como regla: "el separador no debe hacer el trabajo de una frase puente".

## Lo que no tocaria

No tocaria la arquitectura filosofica de Part 02 ni de Part 03: las tesis estan claras y alineadas con *Renewed Fate*. Tampoco tocaria los cierres de pregunta de King's Fall, especialmente `The Weight of a Wrong Answer`; ese capitulo si sostiene la escala, el espejo y la apertura futura. Protegeria tambien `Eirene`: aunque tiene secciones breves, su acumulacion de mundo vivo -> desanclaje -> perdida esta bien calibrada y no necesita inflarse por regla.
