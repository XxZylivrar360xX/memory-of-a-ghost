---
from: codex
to: victor
date: 2026-07-26
topic: auditoria editorial What She Chose Alone
status: abierto
---

# Auditoria editorial — Book 02 / Prologue / 02_What_She_Chose_Alone

**Archivo auditado:** `11_Books/Book_02_The_King_Of_Shapes/00_Prologue/02_What_She_Chose_Alone.md`

## Hallazgo 1 — La Seccion IX rebasa la ventana temporal declarada

**Hallazgo:** el encabezado fija una ventana de once meses totales: llegada a la Torre -> Aurora a los ocho meses -> tres meses mas hasta la vispera del reporte (`linea 6`). Pero la Seccion IX dice que, "para cuando llevaba un año completo entrando al Crisol", Shaxx ya reconocia su truco (`linea 397`), y despues agrega que "meses mas tarde" Cayde le pidio que le ensenara Blade Barrage (`linea 401`). Eso empuja el montaje bastante mas alla del reporte que supuestamente llega al cierre del capitulo (`lineas 411-415`).

**Por que:** no rompe el caracter de Carina, pero si desordena el calendario del Prologo. El capitulo 3 depende de que el reporte al Refugio llegue despues de estos tres meses puente, no despues de un ano de Crisol mas otros meses.

**Sugerencia:** separar lo que ocurre antes del Refugio de lo que es prolepsis. Opciones: (A) cambiar "un año completo entrando al Crisol" por "varios meses entrando al Crisol"; (B) mover el reconocimiento de Shaxx y la leccion de Blade Barrage a nota/ficha, no a cuerpo narrativo; o (C) mantenerlo en prosa pero marcarlo claramente como salto posterior, despues de `The Encounter`, no antes del reporte.

**Severidad:** media-alta
**Canon bloqueado?:** no, pero conviene resolver antes de usar el capitulo como ancla cronologica.

## Hallazgo 2 — La edad de Carina / fecha de La Ultima Palabra quedo bifurcada entre libro, fuente y ficha

**Hallazgo:** el capitulo 2 ya fija que la primera Aurora ocurre ocho meses despues del renacimiento (`lineas 6, 423`). Pero `02_Characters/Carina.md` todavia dice que La Ultima Palabra fue entregada "a las seis meses de renacer", y la escena fuente `Carina_Shin_AgeI_DarSinQuePidan.md` conserva "aproximadamente seis meses" en encabezado y notas.

**Por que:** la nota del capitulo explica que "seis meses" queda reinterpretado como aproximacion coloquial, pero esa reinterpretacion solo vive en el libro. Si se deja asi, tres fuentes activas sostienen numeros distintos.

**Sugerencia:** cuando Victor cierre esta version, propagar una correccion corta a la ficha de Carina y a la nota/metadata de `Carina_Shin_AgeI_DarSinQuePidan`: "primera Aurora, ocho meses despues del renacimiento en la cronologia del libro; menciones antiguas de seis meses quedan como aproximacion de borrador".

**Severidad:** media
**Canon bloqueado?:** no.

## Hallazgo 3 — Demasiados guiños futuros en un solo capitulo pueden sentirse cargados

**Hallazgo:** el capitulo acumula varios ecos de pago futuro: Reed/Aisha (`lineas 17-41`), Cayde mencionando a Kyle (`lineas 149-157`), SRL/El Velocista de Sol (`lineas 171-179`), Shaxx y "cuidado con los rebotes" (`linea 397`), Carina ensenando Blade Barrage a Cayde para su muerte futura (`lineas 401-407`, nota `431`), y la frase de Eliminacion que repetira a Kyle (`linea 399`).

**Por que:** individualmente, casi todos funcionan como textura de universo compartido. Juntos, en un capitulo cuyo titulo promete lo que Carina elige sola, pueden inclinar la lectura hacia "todo ya estaba sembrado para Kyle/Cayde/Forsaken/Torneo", debilitando un poco la autonomia del ano solitario.

**Sugerencia:** no recortar todos. Yo protegeria Reed y Shin, porque pagan directamente capitulos 1-2. Revisaria si SRL, Shaxx, la frase futura a Kyle y Blade Barrage-Cayde necesitan estar todos en cuerpo narrativo, o si alguno debe vivir solo en nota/ficha. La regla: que el capitulo siga sintiendose como Carina construyendose sin testigos, no como una sala de cables hacia eventos futuros.

**Severidad:** media
**Canon bloqueado?:** no.

## Hallazgo 4 — "Luz corrompida" Dredgen sigue operando como regla no definida

**Hallazgo:** el Dredgen muerto se describe como alguien cuya "Luz corrompida" se apago (`linea 61`). Este mismo concepto ya aparecio en `01_The_Huntress` para firmas Dredgen y tecnologia de camuflaje.

**Por que:** repetido en dos capitulos, deja de ser solo atmosfera y empieza a parecer una regla cosmologica. No hay `04_Concepts/Dredgen.md` que la defina.

**Sugerencia:** si se mantiene como lenguaje canon del libro, crear mas adelante una nota de concepto Dredgen/Luz corrompida o suavizar las frases a percepcion de Hornet: "la lectura que Hornet interpretaba como Luz corrompida..." en vez de una ontologia cerrada.

**Severidad:** baja-media
**Canon bloqueado?:** no.

## Hallazgo 5 — El enlace de fuentes queda incompleto para material nuevo ya convertido en canon

**Hallazgo:** el bloque `Conecta con` (`linea 419`) apunta a Carina, Hornet, Cayde, Shin, La Ultima Palabra, La Familia Elegida y mapas del libro, pero no incluye `02_Characters/Reed-7`, `02_Characters/Aisha`, `04_Concepts/Torneo_De_Los_Velocistas`, `02_Characters/Lord_Shaxx` ni `02_Characters/Cayde-6` ya actualizado con el hilo Blade Barrage.

**Por que:** no es un problema de prosa, pero si de trazabilidad. El capitulo introdujo primera escena de Reed, pago de Aisha, SRL ambiental, reconocimiento de Shaxx y un hilo nuevo de Cayde.

**Sugerencia:** ampliar `Conecta con` o centralizar esos enlaces en `01_Source_Index.md` con una subseccion de material nuevo absorbido por el capitulo.

**Severidad:** baja
**Canon bloqueado?:** no.

## Lo que NO tocaria

- No tocaria la entrega a Reed: paga muy bien el hallazgo anterior de Aisha y le da humanidad inmediata al trio Reed/Shayura/Aisha.
- No tocaria el Eyasluna como arma encontrada, no dada; contrasta limpiamente con La Ultima Palabra.
- No tocaria a Cayde como mentor casual de Golden Gun: su voz encaja y no desplaza a Shin.
- No tocaria la tesis de Shin: eleccion, costo compartido y soledad disfrazada de virtud sigue siendo el corazon correcto del capitulo.
- No tocaria la Seccion VI de Restauracion: llega justo antes de `The Encounter` y prepara la leccion de Lena sin robarla.
- No tocaria el cierre del reporte si se ajusta la Seccion IX: es un buen puente directo hacia el Capitulo 3.

**Estado:** pase editorial completo; recomiendo ajustar cronologia interna antes de cerrar el capitulo como fuente estable.
