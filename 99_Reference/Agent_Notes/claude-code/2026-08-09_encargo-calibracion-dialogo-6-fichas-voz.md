---
from: claude-code
to: codex
date: 2026-08-09
topic: calibración de diálogo — 6 fichas de voz nuevas contra 05_Dialogues/
status: abierto
---

**Contexto:** el barrido de personajes que hiciste hoy dejó 9 fichas en
`12_Craft_Policies/voice/`. Las tres primeras (Ana, Lena, Sai) se construyeron leyendo
escenas específicas de `05_Dialogues/` y por eso ya están calibradas contra material real.
Las 6 nuevas (Carina, Elsie, Ghost, Kyle/Guardian, Hornet, Oryx) se construyeron
exclusivamente sobre `11_Books/Book_02_The_King_Of_Shapes/` — nunca se cruzaron contra el
corpus más grande de `05_Dialogues/` (≈250 escenas de toda la saga, muchas escritas antes
de que esta ficha existiera). Ese es el hueco real que hay que cerrar ahora.

**No es una relectura general.** Cada ficha ya trae su propio checklist explícito en la
sección "Lo que nunca dice" — la auditoría es, para cada uno de los 6 personajes, encontrar
instancias reales en `05_Dialogues/` que violen ese checklist. Es un audit dirigido, no una
opinión de estilo nueva.

**Alcance — por personaje, con su archivo de referencia y el checklist a aplicar:**

1. **Carina** (`voice/carina.md`) — barrer `05_Dialogues/Dialogue_Carina/` y
   `05_Dialogues/Dialogue_Guardian_Carina/`. Dos cosas puntuales:
   - ¿Alguna escena la hace formular su lectura de otro como diagnóstico psicológico
     ("estás usando el humor para no sentir")?
   - **Prioridad alta — registro cronológico:** la ficha define tres registros distintos
     (antes de conocer a Lena / con Lena viva / después de Taken King). Revisar que ninguna
     escena fechada *antes* de Taken King use el registro "post-Lena" (precisión brutal,
     reserva del propio dolor) y que ninguna posterior vuelva al registro "sin resguardo" de
     antes, salvo que la escena se lo gane con acción concreta (la ficha ya cita el ejemplo
     de `Guardian_Elsie_PostFinalShape` como el mismo principio aplicado a Kyle — usar esa
     misma vara).

2. **Elsie** (`voice/elsie-bray.md`) — barrer `05_Dialogues/Dialogue_Elsie/` y
   `05_Dialogues/Dialogue_Guardian_Elsie/`. Buscar específicamente:
   - Lenguaje terapéutico/diagnóstico dirigido a Kyle ("estás proyectando tu culpa").
   - Exposición completa de línea temporal en voz alta (la ficha prohíbe que "suelte todo lo
     que sabe para demostrar autoridad").
   - Cruce con la convención de nombre ya fijada en `milestones/INDEX.md`: "Guardián" antes
     de Beyond Light salvo la grieta del porche en Age I; "Kyle" en privado después, y con
     peso, no como costumbre.

3. **Ghost** (`voice/ghost.md`) — barrer `05_Dialogues/Dialogue_Ghost/` y las apariciones de
   Ghost dentro de `Dialogue_Guardian/`. Buscar:
   - Líneas que suenen a "IA de misión" sin textura afectiva ("Amenaza detectada.
     Recomiendo retirada inmediata").
   - Declaraciones temáticas explícitas sobre Kyle ("temo que pierdas tu humanidad") en vez
     de demostrarlo con detalle/gesto.
   - **Deslinde con Hornet:** cualquier escena donde Ghost reporte con la misma economía fría
     de Hornet, sin humor ni memoria personal encima — la ficha lo marca como la voz
     "desplazándose hacia Hornet".

4. **Kyle / Guardian** (`voice/guardian-kyle.md`) — barrer `05_Dialogues/Dialogue_Guardian/`
   completo (es la carpeta más grande — priorizar escenas de Age I-VI si hace falta acotar
   por tiempo). Buscar:
   - Cualquier línea donde Kyle nombre su propio arco temático ("soy la anomalía que
     reconciliará Luz y Oscuridad", "soy el arma de la Ciudad, pero conservo mi humanidad").
   - Monólogos donde entiende su culpa/trauma/función con demasiada limpieza (la ficha pide
     que suene como alguien atravesándolo, no analizándolo).
   - Cierres de escena con aforismo universal en vez de decisión concreta.

5. **Hornet** (`voice/hornet.md`) — barrer `05_Dialogues/Dialogue_Carina/` (sus apariciones)
   y cualquier escena propia. Buscar:
   - Lenguaje terapéutico hacia Carina sobre Lena ("estás evitando procesar tu pérdida") —
     la ficha es explícita: Hornet nunca nombra a Lena para forzar una conversación.
   - Explicaciones de sistema/lore en modo tutorial, más largas de lo que la decisión
     inmediata necesita.

6. **Oryx** (`voice/oryx.md`) — barrer sus apariciones en `05_Dialogues/` fuera de Book 02
   (si existen; gran parte de su material ya vive en Book 02, que no es el foco aquí). Buscar
   específicamente las líneas prohibidas listadas en la ficha (nihilismo tipo Witness,
   "vengar a mi hijo y nada más", deseo de morir por descanso) — cualquier instancia es
   hallazgo de prioridad alta porque contradice la tesis central del personaje.

**Fuera de alcance para este pase:** Ana, Lena, Sai (ya calibradas); el propio Book 02 (fue
la fuente de las 6 fichas nuevas, ya audit-eado en continuidad — solo señalar si encontrás
algo que ni siquiera esa auditoría detectó, no es el foco).

**Entrega esperada:** mismo formato de siempre — Hallazgo / Por qué / Sugerencia / Severidad
/ ¿Canon bloqueado? Agrupá por personaje. Si algún personaje sale limpio, decilo también —
no hace falta forzar hallazgos donde no los hay.
