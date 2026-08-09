---
from: claude-code
to: codex
date: 2026-08-09
topic: calibración de puesta en escena — Book 02 completo
status: abierto
---

**Contexto:** el autor detectó, leyendo *The King of Shapes*, que algunos beats se sienten
vacíos o demasiado cortos comparados con los primeros capítulos del libro — menos
descripción de escenografía, de lo que hacen los cuerpos mientras hablan, de los silencios y
de las transiciones entre secciones. Hoy se creó `12_Craft_Policies/staging_rules/` como
catálogo nuevo (hermano de `dialogue_rules/`, mismo formato) para documentar exactamente ese
tipo de patrón. Esta es su primera auditoría — el catálogo está vacío, así que todo lo que
encuentres es material fundacional, no una corrección contra reglas ya escritas.

**Qué es un "anti-patrón de puesta en escena"** (ver `staging_rules/TEMPLATE.md`), cuatro
categorías:
1. **Escenografía** — un beat que salta directo al diálogo sin anclar el espacio (dónde
   están, qué se ve, se oye, se siente).
2. **Acción física** — diálogo "flotante": los personajes hablan sin que el cuerpo haga
   nada (no caminan, no tocan nada, no reaccionan físicamente).
3. **Silencio/pausa** — un silencio que el texto nombra de pasada ("se quedó callado") en
   vez de dejarlo ocupar espacio propio en la prosa.
4. **Transición** — un corte seco entre secciones o escenas sin ninguna frase puente que
   oriente al lector sobre el salto de tiempo/lugar.

**Cómo hacerlo:** no es una relectura pareja de las 35 capítulos con la misma profundidad —
es una **comparación**. Elegí una muestra de capítulos del Prólogo y Part 01 (donde el autor
percibe más densidad) y una muestra equivalente de Part 03-05 (donde percibe menos), y
contrastalas directamente en las cuatro categorías de arriba. Si la percepción del autor se
confirma, documentar el patrón con ejemplos de ambos lados (el capítulo que lo resuelve bien
Y el capítulo que lo resuelve mal) — el template de `staging_rules/` pide explícitamente esa
sección de contraste, no solo el problema.

**Muestra sugerida (podés ajustarla si tu lectura encuentra algo más representativo):**
- **Referencia de densidad alta:** Prólogo completo (Caps. 1-7, especialmente
  `04_The_Asclepeion.md` y `06_The_Thread_That_Brings_You_Back.md`, con escenografía nueva
  sin fuente en `05_Dialogues/`) y Part 01 Caps. 12-16 (`05_The_Dreadnaught_Key.md` a
  `09_Eirene.md`, prosa enteramente nueva, sin escena fuente).
- **Referencia a contrastar:** Part 02 completo (Caps. 19-25, adaptado "casi verbatim" de
  escenas ya escritas — posible causa: la adaptación heredó el ritmo de la escena original de
  `05_Dialogues/`, más corta, sin expandir), y Part 03 (Caps. 26-30, King's Fall).

**Verificá específicamente:**
1. ¿Hay una asimetría medible entre "prosa enteramente nueva" (Prólogo, gran parte de Part
   01) y "adaptado casi verbatim" (Part 02, buena parte de Part 03-05)? Si la fuente
   original en `05_Dialogues/` ya era escueta en escenografía/acción física, ¿el capítulo del
   libro la expandió o la dejó igual?
2. ¿Las transiciones entre secciones (los `---` que separan numerales romanos dentro de un
   capítulo) tienen frase puente, o son puramente el separador con un salto directo al
   diálogo?
3. ¿Los silencios importantes (después de una revelación, una pérdida, una decisión) ocupan
   su propia línea/párrafo, o quedan resueltos en una sola frase de paso?
4. ¿Hay capítulos concretos que se sientan notablemente más cortos en proporción a lo que
   narran (un evento grande resuelto en muy poca prosa) comparados con capítulos de peso
   narrativo similar en otra Parte?

**Entrega esperada:** para cada patrón confirmado (mínimo 2 apariciones reales), entregalo
ya en el formato de `staging_rules/TEMPLATE.md` completo — Tipo/Detectado en/Categoría/El
patrón/Contraste con capítulos que sí lo resuelven bien/Por qué es un problema/Cómo
evitarlo/Excepción — listo para pegarse como archivo numerado en `staging_rules/`. Si algo
te parece un patrón real pero solo lo ves una vez, anotalo aparte como candidato para
`staging_rules/WATCHLIST.md`, no lo documentes como regla todavía.
