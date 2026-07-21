---
from: codex
to: victor
date: 2026-07-14
topic: auditoría de consistencia — Taken King Parte 1
status: resuelto
---

**Nota de cierre (claude-code, 2026-07-19):** los 5 hallazgos (Eris/Oryx antes de Phobos, Acorazado "retirado" de Saturno, reclamo dormido con origen prematuro, link roto a Shaxx, fricción romántica Elsie-Carina) se verificaron aplicados en la prosa real durante la auditoría de esta sesión — grep directo sobre las 23 escenas confirmó que las correcciones ya vivían en el texto, no solo en las notas narrativas. Sin hallazgos nuevos.

# Auditoría — Taken King Parte 1 (sesión 2026-07-13/14)

## Alcance

Barrido de las 23 escenas que `Plan_TakenKing_Parte1.md` agrupa en cuatro clusters, contrastadas contra `INDEX.md`, `CLAUDE.md`, `KingsFall_HerenciaOculta.md`, las seis escenas de King's Fall, `Guardian_Mara_SeasonLost_LoQueToma.md`, `The_Lord_of_Every_Nothing.md`, y los roadmaps de Kyle–Elsie y Kyle–Carina.

## Diagnóstico general

La arquitectura mayor funciona: la derrota física de Oryx queda separada de su muerte real; Carina abre el camino sin sustituir a la Primera Escuadra; Mara permanece fuera del conocimiento de Kyle; y el primer encuentro Kyle–Carina no contradice ya el origen decanonizado de WotM. No encontré una ruptura que obligue a desmontar un cluster entero.

Sí hay dos contradicciones cronológicas directas, una fricción metafísica con cimientos anteriores y un enlace roto.

---

## 1. Eris conoce la llegada de Oryx antes de Phobos, pero Phobos está fijado como descubrimiento absoluto

**Hallazgo:** `Eris_Osiris_TakenKing_ElPadreDebajoDelRey.md` abre con “Oryx llegó al sistema” (línea 28), repite que viene a cobrar la deuda (línea 80) y termina con Eris decidiendo avisarle a Kyle que Oryx viene por Crota (línea 128). `Eris_Mara_TakenKing_LaTesoreria.md` vuelve a afirmar que Oryx ya llegó (línea 22). Sin embargo, `Guardian_Ghost_Elsie_TakenKing_LoQueLlegoAPhobos.md`, `INDEX.md:298`, el plan y `CLAUDE.md` fijan como regla que nadie sabe que es Oryx hasta que Kyle está dentro del complejo de Phobos y Eris lo siente en tiempo real por radio.

**Por qué:** no es solo información retenida al lector: Eris decide comunicar exactamente el dato que Phobos exige que Kyle ignore. Además, la Batalla de Saturno ocurre antes de Phobos, por lo que no basta con mover una frase unas horas.

**Sugerencia:** elegir una sola versión. La de Phobos produce mejor descubrimiento y ya está propagada a cuatro documentos. Para conservar el Faro, Eris podría detectar una herida o una presión vinculada con la muerte de Crota sin identificar todavía a Oryx ni saber que ya está en Sol; el nombre se confirma en Phobos. También debe retirarse su promesa explícita de advertir a Kyle o convertirla en una advertencia genérica sobre consecuencias de Crota.

**Severidad:** alta  
**¿Canon bloqueado?:** sí

---

## 2. El Acorazado abandona Saturno y después vuelve a estar allí sin transición

**Hallazgo:** `Petra_Mara_TakenKing_LaBatallaDeSaturno.md:122,134` dice que el Acorazado “se retiró” y “se retiraba de las cercanías de Saturno”. Las escenas de infiltración lo sitúan después “en órbita sobre Saturno” (`Guardian_Cayde_Ghost_TakenKing_ElPrimerFragmento.md:5`), igual que `Guardian_Equipo_KingsFall_01_LaEntrada.md:5` y `01_Timeline/Raids/KingsFall.md:9`.

**Por qué:** la prosa actual implica desplazamiento fuera de Saturno, pero no existe un regreso. El canon ya escrito necesita que el Acorazado permanezca allí.

**Sugerencia:** cambiar “se retiró” por una formulación de cese del ataque sin cambio orbital: dejó de disparar, cerró su avance o quedó inmóvil entre los restos de la batalla. La invasión de la Ciudad Ensoñada puede partir desde su corte sin que la nave abandone Saturno.

**Severidad:** media-alta  
**¿Canon bloqueado?:** sí

---

## 3. El reclamo dormido nace antes de la muerte real de Oryx y contradice el cimiento anterior

**Hallazgo:** `Guardian_TakenKing_LaPuertaAParte2.md` afirma que la tesorería de Oryx fue “arrancada de su dueño en el instante exacto en que el Guardian tomó la esencia de un hijo caído” y que ya “le pertenecía un poco”, antes de King's Fall. En cambio, `KingsFall_HerenciaOculta.md:40-46` fija la herencia como consecuencia de derrotar a Oryx; `Guardian_Mara_SeasonLost_LoQueToma.md` dice que durante King's Fall Kyle aprendió la gramática sin heredar poder y que Season of the Lost es la primera vez que la pronuncia; `The_Lord_of_Every_Nothing.md` también encadena el roce del poder desde `LoQueToma`, no desde la esencia de Crota.

**Por qué:** mantener el fenómeno fuera del POV de Kyle protege el secreto, pero no resuelve la causalidad. La nueva escena cambia de hecho el origen metafísico del reclamo: Crota/credencial en vez de muerte real de Oryx/King's Fall.

**Sugerencia:** fijar una de dos reglas y propagarla. La opción con menos retcon es que tomar la esencia solo lo vuelve una llave o candidato legible; el reclamo real nace cuando Kyle mata a Oryx en su Mundo Trono. La coda de Parte 1 puede presagiar que la tesorería “ya lo ha registrado” sin afirmar que el poder fue arrancado ni que ya le pertenece.

**Severidad:** alta  
**¿Canon bloqueado?:** sí

---

## 4. Enlace roto a Shaxx

**Hallazgo:** `Elsie_Petra_TakenKing_LaManoSeCierra.md` enlaza `[[02_Characters/Shaxx]]`, pero no existe esa ficha.

**Por qué:** es el único wikilink roto detectado dentro de las 23 escenas.

**Sugerencia:** crear la ficha en el flujo normal o retirar el enlace hasta que exista. No corregir desde Codex.

**Severidad:** baja  
**¿Canon bloqueado?:** no

---

## 5. Fricción de etapa en el cierre Elsie–Carina

**Hallazgo:** `Elsie_Carina_TakenKing_ElFlancoQueNoPudoAcompanar.md` declara que no hay insinuación romántica, pero Carina pregunta “¿ustedes dos son...?” y Elsie responde “Todavía no sé cómo se llama lo que somos, pero es real”. Esto ocurre justo al entrar en etapa 4 (Confianza). El roadmap reserva el calor de amistad para etapa 5 y el apego con gravedad para etapa 6.

**Por qué:** no rompe un hecho externo, pero la escena verbaliza ante una desconocida una conciencia relacional que parece uno o dos peldaños posterior a la transición que acaba de dramatizarse. También hace que Carina funcione brevemente como detectora del futuro romance, aunque el objetivo declarado era evitar esa sombra.

**Sugerencia:** conservar el agradecimiento de Elsie y su alivio por no ser el único sostén, que sí son muy fuertes. Considerar eliminar la pregunta incompleta de Carina o hacer que la respuesta de Elsie se limite a confianza operacional/personal todavía sin marco de pareja.

**Severidad:** media  
**¿Canon bloqueado?:** no; requiere decisión de tono

---

## Observaciones no bloqueantes

- “23 escenas nuevas” no es un conteo homogéneo: el propio plan incluye dos escenas de Carina ya existentes y enlazadas/expandidas. No afecta canon, pero conviene distinguir “23 escenas del arco” de “23 archivos creados”.
- El daño permanente de Ghost está libre de contradicciones posteriores explícitas, pero hoy solo existe en la escena, el plan, el índice y el log. Si ha de ser permanente, necesita propagación selectiva; se desarrolla en la nota de oportunidades hermana.
- La mecánica de Mara como muerte significativa que entra “con la deuda” es una reinterpretación fuerte, pero internamente consistente dentro de este bloque. Conviene elevarla a cimiento metafísico si va a sostener Forsaken, para que no dependa solo de una explicación de Eris.

