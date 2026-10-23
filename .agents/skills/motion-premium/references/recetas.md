# Recetas (HyperFrames + GSAP)

Cada receta está probada en [`videos/demo-premium`](../../../../videos/demo-premium/). Cumple el contrato de HyperFrames: timeline pausado, nada aleatorio sin semilla, `fromTo` dentro de las escenas y transformaciones en vez de `left`/`top`. Los tiempos son locales a la escena.

## Base de una escena

```html
<template>
  <style>
    @font-face { font-family: "Bricolage Grotesque"; src: url("assets/fonts/bricolage.ttf"); font-weight: 200 800; }
    @font-face { font-family: "Fraunces"; src: url("assets/fonts/fraunces-italic.ttf"); font-style: italic; font-weight: 100 900; }
    #root {
      position: absolute; inset: 0; overflow: hidden;
      background-color: var(--color-paper, #F3ECE4);
      /* retícula de papel al 3,5 % */
      background-image:
        linear-gradient(rgba(7,12,12,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(7,12,12,.035) 1px, transparent 1px);
      background-size: 40px 40px;
    }
  </style>
  <div id="root" data-composition-id="mi-escena" data-width="1920" data-height="1080">…</div>
  <script>
    (function () {
      const tl = gsap.timeline({ paused: true });
      let s = 7; const rnd = () => ((s = (s * 16807) % 2147483647) / 2147483647); // azar con semilla
      // …
      window.__timelines["mi-escena"] = tl;
    })();
  </script>
</template>
```

Los estados iniciales ocultos van con `gsap.set(...)` **fuera** del timeline, no con `tl.set(..., 0)`.

**Cuidado con `fromTo` tardíos**: un `fromTo` aplica su estado `from` en cuanto se crea (`immediateRender`). Si el `from` es visible (anillo con `opacity: 1`, cursor, chispa en el centro), aparece desde el cuadro 0 aunque el tween empiece en 1 s. Ocúltalo con `gsap.set(..., { opacity: 0 })` y agrega `immediateRender: false` a ese `fromTo`. Revisa siempre el cuadro 0 y los primeros 0,5 s con `snapshot --at 0,0.4`.

## Punto → flood → iris

```js
// escena A: el punto crece hasta llenar el cuadro
tl.to("#punto", { scale: 3, duration: 0.15, ease: "expo.out" }, 2.4);
tl.to("#punto", { scale: 90, duration: 0.18, ease: "power3.in" }, 2.55);
// escena B (fondo del color del acento): el papel abre como iris desde el centro
tl.fromTo("#papel", { clipPath: "circle(0% at 50% 46%)" },
  { clipPath: "circle(75% at 50% 46%)", duration: 0.3, ease: "expo.out" }, 0);
```

## Titular sans + serif itálica + marcador

```html
<div class="l1"><span class="mask"><span class="w">Tus</span></span> <span class="mask"><span class="w">plantas,</span></span></div>
<div class="l2" id="l2">sin <span id="hl"><i id="marcador"></i>adivinar.</span></div>
```
```css
.mask { display:inline-block; overflow:hidden; vertical-align:top; padding:0 .04em .14em; margin-bottom:-.14em; }
.w { display:inline-block; }
#hl { position:relative; display:inline-block; isolation:isolate; }
#marcador { position:absolute; left:-.06em; right:-.06em; top:.36em; height:.62em; background:#CDD54A; transform-origin:left center; z-index:-1; }
```
```js
tl.fromTo(".w", { yPercent: 110 }, { yPercent: 0, duration: 0.5, ease: "expo.out", stagger: 0.07 }, 0.32);
tl.fromTo("#l2", { opacity: 0, filter: "blur(10px)", y: 10 }, { opacity: 1, filter: "blur(0px)", y: 0, duration: 0.3, ease: "power3.out" }, 0.55);
tl.fromTo("#marcador", { scaleX: 0 }, { scaleX: 1, duration: 0.25, ease: "power2.out" }, 1.28);
```

## Chips con sombra suave, entrada y dispersión

```css
.chip { border-radius:18px; background:#FCF4EC;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7), 0 1px 1px rgba(7,12,12,.08), 0 10px 24px -8px rgba(7,12,12,.28); }
```
```js
tl.fromTo(chip, { opacity: 0, scale: 0.86, y: 18, filter: "blur(6px)" },
  { opacity: 1, scale: 1, y: 0, rotation: (rnd() - 0.5) * 7, filter: "blur(0px)", duration: 0.4, ease: "expo.out" }, t);
// salida radial desde el centro del cuadro
const d = Math.hypot(cx, cy);
tl.to(chip, { x: cx / d * 380, y: cy / d * 380, opacity: 0, filter: "blur(10px)", duration: 0.25, ease: "power3.in" }, tSalida + i * 0.02);
```

## Countdown o timecode que corre de verdad

```js
const o = { seg: 71 * 3600 + 53 * 60 + 8 };
const pinta = () => (el.textContent = fmt(o.seg)); pinta();
tl.to(o, { seg: 2 * 3600, duration: 2.0, ease: "power2.inOut", onUpdate: pinta }, 0.9);
```

## Escalera de píxeles (escena de transición propia, encima de todo)

```css
.banda { position:absolute; left:0; width:1920px; height:156px; background:#070C0C; }
.banda::after { content:""; position:absolute; top:0; right:-70px; width:70px; height:100%;
  background: linear-gradient(90deg, #070C0C, rgba(7,12,12,.5) 45%, rgba(7,12,12,0)); }
```
```js
for (let i = 0; i < 7; i++) {
  const k = 6 - i; // la de abajo primero
  tl.fromTo("#b" + i, { x: -2010 }, { x: 0, duration: 0.3, ease: "power3.in" }, 0.08 + k * 0.03);
  tl.to("#b" + i, { x: 2010, duration: 0.36, ease: "power3.out" }, 0.64 + k * 0.03);
}
```
La escena siguiente arranca **cuando las bandas ya cubrieron todo** (~0,56 s), nunca antes.

## Morph de contenedor con `clip-path` (sin animar ancho/alto)

La sombra va en un envoltorio con `filter: drop-shadow(...)`, porque `clip-path` recorta el `box-shadow`.

```js
tl.to("#contenido", { opacity: 0, filter: "blur(6px)", duration: 0.12 }, 2.75);       // primero se va el contenido
tl.fromTo("#pildora", { clipPath: "inset(0px 0px 0px 0px round 48px)" },
  { clipPath: "inset(28px 320px 28px 320px round 20px)", duration: 0.45, ease: "power3.inOut" }, 2.8);
tl.to("#pildora-env", { y: -367, duration: 0.45, ease: "power3.inOut" }, 2.8);          // viaja a su destino
tl.to("#pildora", { backgroundColor: "#070C0C", duration: 0.3, ease: "power2.in" }, 2.95); // y toma el color del destino
tl.set("#pildora-env", { opacity: 0 }, 3.25);
tl.set("#telefono-env", { opacity: 1 }, 3.25);                                            // el siguiente nace de ahí
tl.fromTo("#telefono", { clipPath: "inset(18px 150px 842px 150px round 20px)" },
  { clipPath: "inset(0px 0px 0px 0px round 66px)", duration: 0.38, ease: "power3.inOut" }, 3.25);
```
**Error común**: abrir el destino mientras el origen todavía viaja. Se leen dos objetos en vez de uno que se transforma.

## Tarjeta que sube, reflejo, toque, crece y sale en whip

```js
tl.fromTo("#tarjeta-env", { y: 520 }, { y: 0, duration: 0.5, ease: "expo.out" }, t);
tl.fromTo("#foto", { scale: 1.15, rotation: -8 }, { scale: 1, rotation: 0, duration: 0.7, ease: "expo.out" }, t);
tl.fromTo(".fila", { y: 18, opacity: 0 }, { y: 0, opacity: 1, duration: 0.4, ease: "expo.out", stagger: 0.05 }, t + 0.1);
// reflejo: banda diagonal en soft-light que cruza una sola vez
tl.fromTo("#brillo", { xPercent: -120 }, { xPercent: 120, duration: 0.6, ease: "power2.inOut" }, t + 0.5);
// toque
tl.to("#boton", { scale: 0.96, duration: 0.08 }, t + 0.7); tl.to("#boton", { scale: 1, duration: 0.14 }, t + 0.78);
// rompe el marco, el entorno se difumina
tl.to("#tarjeta-env", { scale: 1.42, y: -30, duration: 0.45, ease: "power2.inOut" }, t + 0.9);
tl.to("#telefono-env", { filter: "blur(10px)", opacity: 0.55, duration: 0.35 }, t + 0.95);
// whip vertical
tl.to("#tarjeta-env", { y: -1150, filter: "blur(22px)", duration: 0.22, ease: "power3.in" }, t + 1.45);
```
```css
#brillo { position:absolute; inset:0; mix-blend-mode:soft-light;
  background: linear-gradient(115deg, transparent 38%, rgba(255,255,255,.55) 50%, transparent 62%); }
```

## Flood circular con causa + pantalla nueva detrás (doble iris)

```js
tl.fromTo("#flood", { scale: 0 }, { scale: 13, duration: 0.32, ease: "power2.inOut" }, t);  // círculo de 160 px en la esquina
tl.fromTo("#pantalla-nueva", { clipPath: "circle(0% at 92% 4%)" },
  { clipPath: "circle(150% at 92% 4%)", duration: 0.38, ease: "power2.inOut" }, t + 0.14);
```

## Ruta que se dibuja y número que rueda en columna

```js
tl.fromTo("#ruta", { strokeDasharray: 720, strokeDashoffset: 720 }, { strokeDashoffset: 0, duration: 0.6, ease: "power2.inOut" }, t);
[1, 2, 3].forEach((k, i) => {   // columna 7/5/3/1 en una ventana de 96 px de alto
  tl.to("#col", { y: -96 * k, duration: 0.16, ease: "power3.out" }, t + 0.07 + i * 0.18);
  tl.fromTo("#ventana", { filter: "blur(0px)" }, { filter: "blur(4px)", duration: 0.06, yoyo: true, repeat: 1 }, t + 0.07 + i * 0.18);
});
```

## Racha de datos con cortes secos

```js
capas.forEach((c, i) => {           // un corte por beat, sin tween
  gsap.set(c, { opacity: i === 0 ? 1 : 0 });
  if (i > 0) tl.set(c, { opacity: 1 }, i * 0.5);
  if (i < capas.length - 1) tl.set(c, { opacity: 0 }, (i + 1) * 0.5);
});
const rueda = (el, desde, hasta, fmt, t) => {
  const o = { v: desde }; const p = () => (el.textContent = fmt(o.v)); p();
  tl.to(o, { v: hasta, duration: 0.42, ease: "expo.out", onUpdate: p }, t);
  tl.fromTo(el, { filter: "blur(10px)", y: -18 }, { filter: "blur(0px)", y: 0, duration: 0.34, ease: "expo.out" }, t);
};
```
Paneles insertados con `left/right: 58px; top/bottom: 74px; border-radius: 28px`; detrás, el número fantasma a 520 px y 3,5 % de opacidad.

## Objeto se vuelve mundo

```js
// un duplicado del ícono, fuera de la "cámara" y en su posición final en pantalla
tl.set("#mundo", { opacity: 1 }, t);
tl.fromTo("#mundo", { scale: 1.08 }, { scale: 48, duration: 0.45, ease: "power2.inOut" }, t);
tl.to("#camara", { filter: "blur(15px)", duration: 0.3, ease: "power2.in" }, t);
```

## Partículas que convergen con estela, logo con anillo y wordmark

```js
const ang = Math.atan2(ty - fy, tx - fx) * 180 / Math.PI;     // orientar la estela hacia su destino
tl.fromTo(p, { x: fx, y: fy, rotation: ang, scaleX: 4, filter: "blur(4px)" },
  { x: tx, y: ty, scaleX: 1, filter: "blur(0px)", duration: 0.42, ease: "expo.out" }, i * 0.015);
tl.to(p, { x: 0, y: 0, scale: 0.4, duration: 0.15, ease: "power3.in" }, 0.47);   // colapso
tl.fromTo("#logo", { scale: 0, rotation: -50 }, { scale: 1, rotation: 0, duration: 0.42, ease: "back.out(1.8)" }, 0.6);
tl.fromTo("#anillo", { scale: 0.25, opacity: 1 }, { scale: 1.35, opacity: 0, duration: 0.7, ease: "expo.out" }, 0.6);
tl.fromTo("#palabra span", { opacity: 0, y: 24, filter: "blur(10px)" },
  { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.3, ease: "expo.out", stagger: 0.08 }, 1.38);
```

## Viñeta que se cierra a negro

```css
#vineta { position:absolute; inset:0; --r:140;
  background: radial-gradient(ellipse 62% 78% at 50% 50%, transparent calc(var(--r)*1%), #070C0C calc(var(--r)*1% + 14%)); }
```
```js
gsap.set("#vineta", { opacity: 0 });               // invisible hasta que actúa (si no, `check` la marca como oclusión)
tl.set("#vineta", { opacity: 1 }, 4.55);
tl.to("#vineta", { "--r": -16, duration: 0.45, ease: "power2.in" }, 4.55);
```

## Sonido en la raíz

Cada `<audio>` lleva `id`, `data-duration` (la duración real del archivo; sin ella, `lint` lo extiende hasta el final del video) y su propio `data-track-index`. Ubica el pico un frame (≈0,03 s) después de la imagen.

```html
<audio id="sfx-flood" src="assets/sfx/swish-6.wav" data-start="2.56" data-duration="0.14" data-volume="0.9" data-track-index="13"></audio>
```
