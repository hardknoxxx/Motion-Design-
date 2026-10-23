---
name: motion-premium
description: Estilo de motion design premium y minimalista aprendido de dos referencias (reel editorial con HUD y anuncio de producto con UI animada): una idea por escena, mucho aire, papel cálido + tinta + un acento, títulos sans + serif itálica, transiciones con causa (flood de color, iris, escalera de píxeles, morph de contenedores, objeto que se vuelve mundo), cortes secos sobre el beat, números que ruedan, sombras suaves y reflejos sutiles. Úsala para cualquier video, reel, promo, anuncio de app o motion de UI que deba sentirse premium, junto con /hyperframes para producirlo.
---

# Motion premium minimalista

Este estilo sale de medir cuadro a cuadro dos referencias ([gramática medida](references/gramatica-medida.md)). Lo que lo hace "premium" no es ningún efecto, sino la **disciplina**:

1. **Una idea por escena.** 3–7 palabras o un solo objeto héroe. Si una escena necesita dos frases, son dos escenas.
2. **Mucho aire.** El héroe ocupa 40–60 % del ancho y el resto es fondo limpio. El texto secundario es diminuto (mono 11–13 px a 1080p) y se pega a los bordes, como un HUD.
3. **Tres colores y medio.** Papel cálido, tinta casi negra, **un** acento saturado, y un segundo acento solo para cortes de color. Nunca degradados de fondo.
4. **Todo se mueve con causa.** Cada transición nace de un objeto en pantalla: un punto que crece, una tarjeta que se agranda, un ícono que se vuelve el fondo. Nada aparece "porque sí".
5. **Rápido entrando, quieto al llegar.** Entradas de 0,2–0,6 s con ease-out largo y motion blur; luego el elemento queda **muerto de quieto**. Nada flota ni respira.
6. **Ritmo por contraste.** Escenas de 2–3 s con micro-movimiento interno, rachas de cortes secos cada 0,3–0,5 s (estadísticas, palabras) y una pausa de 0,3–0,7 s antes del remate.

## Tokens (medidos en la referencia)

```css
:root {
  --paper: #F3ECE4;      /* fondo cálido (no blanco puro) */
  --paper-2: #FCF4EC;    /* tarjetas sobre el papel */
  --ink: #070C0C;        /* tinta y paneles oscuros */
  --ink-soft: #3B4A3F;   /* serif itálica secundaria (gris verdoso) */
  --accent: #CDD54A;     /* chartreuse suave: marcador, anillos, panel */
  --accent-hot: #E6FC40; /* lima eléctrica: solo cortes cinéticos */
  --pop-1: #FC5C36;      /* tomate: flood / punto final */
  --pop-2: #2E3CFC;      /* cobalto: flood alternativo */
  --radius-card: 22px;   /* tarjetas */
  --radius-panel: 28px;  /* paneles de color insertados (margen 3 % del cuadro) */
  --shadow-soft: 0 1px 2px rgba(7,12,12,.06), 0 12px 32px -8px rgba(7,12,12,.18), 0 40px 80px -24px rgba(7,12,12,.22);
  --shadow-chip: 0 1px 1px rgba(7,12,12,.08), 0 6px 16px -6px rgba(7,12,12,.25);
}
```

- **Tipografía**: titular sans pesada con tracking −3 % a −4 % + segunda cláusula en **serif itálica** del mismo tamaño ("Harga dihitung, *bukan ditebak.*"); mono en caps con tracking +12 % para el HUD y las etiquetas; para palabras cinéticas, una sans **extendida** (ancho 125–150 %). En el repo: `tipografias/sans/Bricolage Grotesque` (tiene eje de ancho), `serif/Fraunces` o `Instrument Serif` (itálicas), `mono/JetBrains Mono`, `sans/Unbounded` (extendida).
- **Sombras suaves**: siempre en capas (`--shadow-soft`), nunca una sola sombra dura. En fondo oscuro no hay sombra: hay un borde interior de 1 px `rgba(255,255,255,.06)`.
- **Reflejos sutiles**: un brillo diagonal (`linear-gradient(115deg, transparent 40%, rgba(255,255,255,.35) 50%, transparent 60%)`) que cruza la tarjeta una sola vez en 0,6 s al llegar. Y un `inset 0 1px 0 rgba(255,255,255,.6)` en el borde superior de las píldoras.
- **Textura**: el papel lleva una retícula de 40 px a 4 % de opacidad, o un grano fino (`overlays/grano-pelicula/grano-pelicula-fino.mp4` en Superposición al 6 %). Nunca más.

## El marco HUD (firma del estilo)

Cuatro esquinas en L de 18 px y 1,5 px a 24 px del borde. Arriba a la izquierda va `MARCA / MOTION REEL '26`, arriba a la derecha `● TC 00:00:10:28` (punto rojo y timecode que corre de verdad), abajo a la izquierda `04 — SECCIÓN` (cambia con cada escena) y abajo a la derecha `1920 × 1080 · 60 FPS`. Abajo, una línea de 1 px recorre el ancho como barra de progreso del video. Todo en mono de 11 px al 55 % de opacidad. Plantilla: [`assets/hud.html`](assets/hud.html).

## Repertorio de transiciones

Usa **3–5 tipos por video** y nunca dos iguales seguidas. Código listo en [recetas](references/recetas.md).

| Transición | Cuándo | Medidas |
|---|---|---|
| **Punto → flood → iris** | Apertura y cierre de capítulos | Un punto de 24 px escala ×80 en 0,18 s (`power3.in`) y llena el cuadro con el acento; 2 frames después, un círculo de papel abre desde el centro (`clip-path: circle()` 0→75 %, 0,25 s, `expo.out`) |
| **Escalera de píxeles** | Cambio de tema o de sección | 6–8 franjas horizontales de tinta entran escalonadas (40 ms entre franjas) con el borde de ataque difuminado en 40 px; cubren todo en 0,35 s, aguantan 0,15 s y salen por el mismo lado |
| **Blur swap** | Entre dos titulares de la misma escena | Sale: sube 30 px, blur 0→12 px y opacidad 1→0 en 0,15 s. Entra: palabra por palabra desde y = 40 px con máscara, 0,35 s `expo.out`, 60 ms entre palabras |
| **Morph de contenedor** | Una cosa se convierte en otra (chip → tarjeta, buscador → teléfono) | Se tweenean ancho, alto y radio a la vez en 0,45 s `power3.inOut`, con blur de 0→8→0 px y el contenido viejo fuera en los primeros 30 % |
| **Objeto se vuelve mundo** | Ícono o tarjeta → siguiente escena | El objeto escala hasta pasar el cuadro en 0,6 s `power2.inOut`, con el radio bajando a 0; lo que lo rodea se difumina 15 px y se apaga; el contenido nuevo aparece cuando el objeto va al 70 % |
| **Corte seco con cambio de fondo** | Rachas de datos y palabras | Sin tween: `tl.set`. Cada corte cambia fondo (papel → panel tinta → papel → panel acento) y el número nuevo llega rodando |
| **Iris de viñeta a negro** | Final de pieza | Una elipse negra se cierra desde los bordes en 0,4 s (`power2.in`) y deja solo un punto de acento |
| **Dispersión con blur** | Salida de chips o partículas | Cada chip sale radialmente desde el centro 200–400 px en 0,25 s (`power3.in`) con blur direccional de 10 px; 20 ms de escalonado |

## Textos y números

- **Titular**: la cláusula sans entra palabra por palabra (máscara + subida); la serif itálica entra después (+0,15 s) con blur 8→0. Un marcador de acento barre **una sola palabra** de izquierda a derecha en 0,25 s (`power2.out`), 0,3 s después de que el titular aterriza.
- **Tipeo**: 10–14 caracteres por segundo con un cursor de bloque que parpadea a 2 Hz. El placeholder gris entra letra a letra (subida de 6 px y fade, 30 ms por letra), se borra rápido (40 ms por letra) y la consulta real se tipea.
- **Números**: ruedan de un valor cercano al valor final (de 238 a 420+) en 0,4–0,6 s `expo.out`, con blur vertical de 6 px mientras se mueven; aterrizan quietos. Detrás va el mismo número gigante al 5 % de opacidad. La etiqueta, en mono caps diminuta, va debajo.
- **Palabra cinética**: entra con `scaleX` 1,6→1 y blur horizontal 24→0 en 0,2 s, y el punto final en el color pop rebota con `back.out(2)`. Cada palabra dura **un beat**.
- **Countdown real**: un timecode o temporizador que corre de verdad (71:53:08 → 03:12:08) dice "urgencia" sin decir nada.

## UI animada (anuncio de producto)

1. Pantalla de producto **a 1,6–2× su tamaño real**, centrada y sin inclinación 3D (salvo una vista bento con `rotateX(8°) rotateZ(-4°)` como reveal final).
2. Cada estado nace del anterior: la barra de búsqueda se encoge y se vuelve la isla del teléfono; el resultado sube desde abajo con 2–3 capas escalonadas (foto, título, botón); el botón se presiona (escala 0,96, 80 ms) y su tarjeta crece fuera del teléfono.
3. Un flood circular del color de marca abre desde una esquina del teléfono hacia la siguiente pantalla (mapa, agenda, etc.). Las líneas de ruta se dibujan con `stroke-dashoffset` y el ETA rueda hacia abajo (12 → 6 → 1).
4. La notificación cae desde la isla con sombra suave mientras la cámara empuja (escala 1→1,12). Luego el ícono de la notificación crece hasta ser la pantalla de marca: logo y luego wordmark, con blur 10→0.

## Sonido

El sonido marca el ritmo: cada corte o llegada tiene un efecto y el remate tiene el golpe más fuerte. Un video premium **nunca suena vacío**, pero tampoco ruidoso: hay una cama continua muy baja y muchos detalles pequeños, cada uno pegado a algo que se ve. Los archivos están en este repo; los de `sfx-botanica/08-procesados/` ya vienen limpios.

| Acción en pantalla | Archivo | Volumen orientativo (`data-volume`) |
|---|---|---|
| Todo el video (cama) | `08-procesados/cama-botanica.wav` (−30 LUFS) | 1,0 |
| Flood de color, escalera, objeto→mundo | `sfx/whoosh-transiciones/swish-*.wav` (rotar 2–3) | 0,6–0,85 |
| Partículas que salen o convergen | `08-procesados/gota-1…5.wav`, una por partícula visible, escalonadas | 0,15–0,25 |
| Chip o badge que aterriza | `gota-*` + un solo `hojas-suave-*` para toda la cascada | 0,25–0,3 |
| Tipeo | `08-procesados/tecla-1…4.wav`, **una por carácter**, rotando | 0,35 (real) · 0,1 (placeholder) · 0,22 (decorativo) |
| Countdown o número que rueda | `reloj-tock` / `reloj-tick` alternados (ver abajo) | 0,2–0,3 |
| Marcador o subrayado | `08-procesados/marcador-suave.wav`, arrancando 0,1 s **antes** del trazo | 0,6 |
| Reflejo sobre una tarjeta | `08-procesados/brillo-gotas.wav` | 0,15 |
| Línea que se dibuja (ruta, riego) | `08-procesados/agua-corriente-corta.wav` | 0,5 |
| Toque de botón | `sfx/ui-interfaz/kenney-interface/click_002.wav` | 0,8 |
| Notificación | `sfx/campanas-acentos/bell_ding2.wav` | 0,25 |
| Logo (una vez) | `impactSoft_heavy` + `brillo-gotas` + `pajaro-canto-breve` 0,3 s después | 0,85 · 0,4 · 0,3 |
| Punto final | una `gota-*` | 0,4 |

- **Ticks de reloj que siguen la animación**: no los pongas a intervalo fijo. Pon un tick cada vez que el progreso del tween cruza k/N (N ≈ 24 para 2 s), calculado con la misma curva (`power2.inOut`): quedan densos donde los números corren y espaciados donde frenan. En un rodillo `expo.out` de 0,42 s van a 0,03 · 0,07 · 0,12 · 0,19 · 0,29 s, cada vez más suaves.
- **Nada áspero**: antes de usar un sonido, mide su centroide espectral. Por encima de ~5 kHz (raspones, siseos de hojas sin filtrar, `scratch_*`) suena barato; pásalo por un paso bajo a 3–5 kHz o cámbialo.
- **Sin repetición audible**: rota 3–5 variantes de cada sonido corto y baja un poco el volumen de cada repetición dentro de una ráfaga.
- **Master**: mide el render con `hyperframes audio`. Sube la mezcla a **−16 LUFS** con un limitador a −1,5 dBTP: `ffmpeg -i in.mp4 -af "volume=XdB,alimiter=limit=0.84:level=0" -c:v copy out.mp4`. Pon siempre `level=0`: si no, el limitador sube la ganancia por su cuenta. Y no normalices camas con `loudnorm` dinámico, porque mete pozos de volumen cerca del final.
- El pico del efecto va **un frame después** de la imagen. Si no hay música, el ritmo lo marca una grilla virtual de 108–120 BPM (un beat ≈ 15 frames a 30 fps): los cortes van sobre el beat y los cambios de escena sobre el compás.

## Lo que mata el estilo (prohibido)

- Fondos con degradado, glassmorphism, neón, sombras negras duras.
- Más de un acento por escena, o el acento en algo sin significado.
- Todo entrando con fade + slide-up igual; títulos que siguen moviéndose después de aterrizar; elementos que "respiran".
- Transiciones genéricas sin causa (crossfade entre mundos, zoom del template, spin).
- Llenar el espacio: si se te ocurre "agregar algo para que no quede vacío", no lo agregues.
- Bounce en la UI (el rebote solo en el punto final de una palabra o en el logo).

## Flujo de trabajo

1. Escribe la idea de cada escena en una línea y cuenta las palabras (≤ 7).
2. Elige el acento y en qué palabra u objeto vive.
3. Elige 3–5 transiciones de la tabla y asígnalas con su causa.
4. Construye con `/hyperframes`. Para efectos estándar, primero `npx hyperframes catalog`: sirven `grid-pixelate-wipe`, `iris-reveal`, `number-wheel`, `soft-blur-in`, `device-frame-stage`, `telemetry-hud` y `vignette`, ajustados a estos tokens.
5. Revisa con `snapshot --review` contra la [lista de control](references/gramatica-medida.md#lista-de-control).

Ejemplo completo, renderizado y comentado: [`videos/demo-premium/`](../../../videos/demo-premium/).
