---
from: codex
to: victor
date: 2026-08-09
topic: auditoria dialogos book02 part02
status: abierto
responde_a: encargo directo de Victor en chat 2026-08-09
---

# Auditoria de dialogos - Book 02, Part 02

## Alcance

Revisé la Part 02 completa de `Book_02_The_King_Of_Shapes`, capítulos 19-25:

- `01_The_War_That_Did_Not_Stay_In_Saturn.md`
- `02_What_We_Had_Already_Beaten.md`
- `03_The_Map_Of_Guilt.md`
- `04_A_Sword_Is_Not_An_Answer.md`
- `05_The_Fold_That_Resists.md`
- `06_The_Wounded_Wish.md`
- `07_Always_Eager_To_Die.md`

Contraste usado: `00_Book_Map`, `01_Source_Index`, `Plan_TakenKing_Parte2_GuerraDeLosPoseidos`, `Plan_TakenKing_Reimaginacion_TheKingOfShapes`, fichas de voz de Kyle, Ghost, Elsie, Carina, Hornet, Oryx, Riven y Savathûn, fichas de Eris/Mara/Osiris y `08_Core_Relationships/Primera_Escuadra`.

## Diagnostico general

No encontre ruptura de arquitectura mayor. Parte 2 cumple su tesis: Oryx convierte historia en ejercito. La guerra deja de ser geografia y se vuelve provocacion, memoria usada, identidad vaciada y respuesta forjada. Tambien se respetan los guardrails principales:

- Oryx no vuelve a presentarse ante Kyle/Carina despues del regicidio fisico de Parte 1.
- La excepcion de presencia fisica de Oryx ocurre en Ciudad Ensoñada, con Riven.
- Riven queda herida, no completamente tomada.
- Quria no se nombra en prosa; queda como `Mente Vex`.
- La caza de Elsie queda sembrada, no resuelta.
- El reclamo dormido de Kyle no entra en su POV consciente.
- Carina no entra al raid y no recibe cierre de duelo; sigue funcionando en el frente civil y en la forja de Bolt Caster.

El problema mas fuerte no es de estructura sino de superficie: Parte 2 viene de fuentes casi verbatim y eso deja algunos dialogos con registro dialectal mezclado (`vos`) y con demasiada formulacion conceptual. Varias escenas dicen exactamente lo que el roadmap queria que dijeran; el costo es que, por momentos, los personajes recitan el motor.

## Hallazgos

### 1. Discrepancia puntual: Tiago llama al Custodio Ciego "Guardián de Hierro"

Ubicacion: `02_What_We_Had_Already_Beaten.md`

Tiago dice:

- "la diferencia entre eso y lo que de verdad le hicimos a un Guardián de Hierro convertido en herramienta..."

En el mismo capítulo y en los roadmaps, el frente de Tiago/Angie está fijado como Zydron/Custodio Ciego: eco Vex, custodio de portal, función vaciada. No encontré soporte local para convertirlo en Guardián de Hierro/Iron Lord. Además, la frase viene justo después de que Tiago dice "esto no es Zydron", así que el lector recibe dos etiquetas incompatibles para el mismo enemigo.

Severidad: alta dentro de esta auditoria, porque es la única discrepancia concreta de canon/identidad detectada.

Propuesta: reemplazar por algo como "un custodio Vex convertido en herramienta" o "una forma que alguna vez custodió un portal por una razón propia". Si se queria aludir al Templario/Zydron como funcion fusionada, conviene explicitarlo sin introducir Iron Lords.

### 2. Voseo fuera de registro en Kyle, Ghost, Elsie, Eris y Carina

Ubicaciones principales:

- `03_The_Map_Of_Guilt.md`: "¿A qué te referís?", "dónde ibas a correr vos", "vos decidieras", "decidís".
- `04_A_Sword_Is_Not_An_Answer.md`: "Kyle no tiene eso. Kyle tiene paciencia... Vos no", "qué querés ser", "qué ya sos", "lo traés", "¿Qué le diste vos?", "¿Por qué vos?"

El `vos` funciona muy bien en `06_The_Wounded_Wish.md`, porque la ficha de Riven lo permite como trato formal/de reconocimiento y la ficha de Oryx lo marca como registro especial ante criaturas como Riven. El problema es su uso en personajes que, en el resto del vault, hablan mayormente con `tú`.

En Parte 2 el voseo parece venir de las fuentes casi verbatim, no de una decisión de voz nueva. Si se deja, convierte a Kyle/Ghost/Elsie/Eris/Carina en hablantes de una misma región verbal justo en escenas donde deberían distinguirse por precisión, sequedad o intimidad.

Severidad: media.

Propuesta: normalizar a `tú` en los personajes humanos/Guardianes de Parte 2, y reservar `vos` para Oryx/Riven cuando el registro tenga función deliberada.

### 3. Elsie nombra "amor" demasiado pronto y demasiado limpio en el mapa de culpa

Ubicacion: `03_The_Map_Of_Guilt.md`

La escena ya fue calibrada parcialmente en una nota al pie del propio capítulo, y se nota: el diálogo está más contenido que su versión probablemente anterior. Aun así, esta línea sigue siendo muy frontal para Elsie en Taken King:

- "La palabra que no quiero usar es amor. Pero es esa."

El beat correcto es que Kyle entiende que Oryx usa culpa y respuesta moral para moverlo. La ficha Guardian/Elsie todavía sitúa esta etapa como confianza incipiente, no como lenguaje emocional completamente disponible. "Amor" puede ser verdad en sentido amplio, pero dicho así suena más a diagnóstico temático que a la Elsie que prefiere patrón, consecuencia y datos.

Severidad: media-baja.

Propuesta: dejar el concepto sin nombrarlo o usar una formula menos desnuda: "lo que te importa", "el punto donde siempre respondes primero", "la gente que no puedes dejar fuera del mapa". La línea protegida de Kyle, "Oryx no está usando mi culpa...", sí conviene mantenerla intacta porque paga checklist explícito.

### 4. Ghost todavía sostiene una explicación muy completa del dilema

Ubicacion: `03_The_Map_Of_Guilt.md`

Ghost dice:

- "Seguir el patrón que Oryx te tiende puede salvar una vida real..."
- "Ignorarlo puede ganarte esa posición..."
- "No hay opción limpia."

La voz de Ghost permite mayor verbalización emocional que la de Kyle, y la escena necesita que él cargue consecuencia. El riesgo es de longitud: resume el dilema moral completo en una sola intervención. En vez de parecer archivo emocional, por momentos parece cierre de ensayo.

Severidad: baja-media.

Propuesta: conservar "No hay opción limpia" y la lealtad final, pero fragmentar el razonamiento. Que Ghost llegue por correcciones, no por una fórmula perfecta.

### 5. Eris define la identidad elemental de Kyle y Carina con demasiada certeza

Ubicacion: `04_A_Sword_Is_Not_An_Answer.md`

El capítulo de la forja está bien situado y cumple el roadmap: Raze Lighter y Bolt Caster no nacen como armas más fuertes, sino como decisiones. El problema es que Eris a veces explica demasiado exactamente qué es cada portador:

- Kyle: "Es violencia definida por amor."
- Carina: "Eso es lo que sos, con la frecuencia suficiente para que un núcleo lo reconozca."
- Carina: "el ángulo que no cubrís es el que te cuesta lo que más te importa."

Eris puede leer trauma y Colmena, pero la ficha la favorece cuando su conocimiento es preciso sin sonar terapéutico. En Carina, además, el duelo por Lena no debería volverse una ecuación tan clara para alguien externo.

Severidad: media.

Propuesta: mantener la lectura material del núcleo, pero reducir la sentencia sobre la persona. Para Kyle, "fuego que protege antes de consumir" comunica lo mismo con menos etiqueta emocional. Para Carina, que Eris nombre urgencia, ángulo y decisión; que no complete sola la herida.

### 6. Tiago funciona, pero la escena lo acerca a recitar su ficha

Ubicacion: `02_What_We_Had_Already_Beaten.md`

Tiago debe conservar diferencias y registrar lo que una victoria tiende a borrar. Esa función está perfectamente alineada con su ficha. La fricción está en que el diálogo lo declara de forma muy cerrada:

- "Alguien tiene que conservar la diferencia. Si no lo hago yo, no lo hace nadie."

No es incorrecto. Pero en una evacuación urgente, con Angie marcando que "ahora no es el momento", la línea puede sentirse demasiado acabada.

Severidad: baja.

Propuesta: hacerlo más Tiago literal y menos lema: que diga que está grabando el registro, que perder el dato falsifica el informe, y que después pelean. La función queda, con menos autoexplicación.

### 7. Oryx roza plan de derrota al entregar la Mente Vex a Savathûn

Ubicacion: `07_Always_Eager_To_Die.md`

La escena protege bien el punto mayor: Oryx no quiere dejar de existir; quiere una respuesta capaz de juzgarlo. Aun así, dos líneas empujan hacia una lectura de legado planificado:

- "Porque si voy a perder, prefiero que lo que queda de mí sirva para algo que yo mismo elegí soltar..."
- "Eso es exactamente lo que quiero que quede de mí, si esto termina como creo que va a terminar."

El roadmap exige que Oryx pelee para ganar y que su disposición a morir no suene suicida ni a plan de derrota. Estas frases no rompen la escena, pero acercan el gesto al testamento.

Severidad: media.

Propuesta: formularlo menos como predicción de derrota y más como gobierno de contingencia. Oryx puede decir que toda pregunta digna debe sobrevivir a quien la hizo, o que una herramienta no debe esperar a que el vencedor decida su uso. Eso mantiene agencia sin hacerlo sonar como si ya estuviera ordenando su herencia.

### 8. Savathûn se autoexplica demasiado al despedirse

Ubicacion: `07_Always_Eager_To_Die.md`

Savathûn dice:

- "Es que ya sé que tu ausencia va a confirmar, para mí, que ya empecé a separarme de la familia. Y de la doctrina. Vine a decírtelo en persona, en vez de dejar que lo descubrieras solo."

El contenido es correcto: ella entiende que se está separando de familia y doctrina. Pero la ficha de voz advierte contra vulnerabilidad directa y terapia explícita. Savathûn suele reformular, no confesarse entera.

Severidad: media.

Propuesta: dejar la verdad en ángulo. Algo como: "No vine a estar a tu lado cuando lleguen. Vine a asegurarme de que lo supieras antes de llamarlo traición." Así conserva filo, afecto y separación sin explicar su interior completo.

### 9. Notas narrativas con referencias desactualizadas

Ubicaciones:

- `01_The_War_That_Did_Not_Stay_In_Saturn.md`: la nota dice que el peso del reclamo dormido "es exclusivo del Cap. 22", pero por estructura actual el mapa de culpa es Cap. 21 y la forja es Cap. 22.
- `02_What_We_Had_Already_Beaten.md`: la nota dice que `The Map of Guilt` está "todavía sin escribir", aunque el capítulo 21 ya existe.

No afecta prosa viva ni diálogo, pero sí afecta el motor de fichas/notas de capítulo. Si alguien usa esas notas como guía, puede seguir una referencia ya vencida.

Severidad: baja.

Propuesta: actualizar metadata cuando Claude haga el pase de ajustes. No es prioridad narrativa, pero sí higiene del vault.

## Lineas y nucleos que no tocaria

- `01_The_War_That_Did_Not_Stay_In_Saturn` funciona como apertura de Parte 2: no repite villanos del Frente 2 y fija bien que herir a Oryx distribuyó la guerra.
- La herida de Ghost deja de ser detalle privado y se vuelve limitación táctica sin dramatizarse de más.
- Petra sostiene el Arrecife con media información; su diálogo evita convertirla en incompetente o ingenua.
- Carina en frentes civiles sigue salvando gente sin convertir cada civil en sustituto de Lena.
- Joe cumple su función: señala antes de que Kyle se pierda, sin reclamar autoridad emocional.
- Kevin/Resner están bien emparejados: ritmo contra disciplina, sin alivio cómico gratuito.
- El núcleo de `The Map of Guilt` sí debe permanecer: Oryx no castiga culpa, la usa para mover.
- `The Fold That Resists` protege muy bien el reclamo dormido: "variable no resuelta", no heredero.
- `The Wounded Wish` está muy fuerte de voz: Riven no es genio maligno y Oryx no es destructor plano.
- El uso de `vos` en Oryx/Riven conviene conservarlo; ahí sí tiene función de reconocimiento.
- `Sathona` en el cierre con Savathûn funciona y está protegido por ficha.
- El cierre directo hacia King's Fall queda claro: Parte 2 termina con los seis cruzando el umbral, no con otra batalla externa.

## Prioridad sugerida

1. Corregir "Guardián de Hierro" en Cap. 20.
2. Normalizar voseo en Kyle/Ghost/Elsie/Eris/Carina, conservándolo en Oryx/Riven.
3. Bajar la explicación identitaria de Eris en Cap. 22.
4. Ajustar las dos líneas de Oryx y la autoexplicación de Savathûn en Cap. 25 para evitar lectura de testamento.
5. Actualizar notas narrativas desfasadas en Caps. 19-20.

