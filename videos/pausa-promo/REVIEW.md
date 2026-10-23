# Revisión: pausa-promo (v2)

Reconstrucción en HyperFrames del prototipo "Pausa", que estaba hecho en Remotion en la rama `ccr-279eddb0-rrprmk` (`motion-premium/src/promo/PausaPromo.tsx`; esa versión no se tocó). Se aplicaron las mismas reglas que al demo de Raíz (skill `motion-premium`). Dura 16,5 s, 1920 × 1080, 30 fps. Render: [`renders/pausa-promo.mp4`](renders/pausa-promo.mp4).

## Qué cambió respecto del prototipo

| Aspecto | Prototipo (Remotion) | v2 (HyperFrames) |
|---|---|---|
| Transiciones | Las seis eran el mismo fundido con desenfoque, salvo la disolución en píxeles | Cada una nace de algo en pantalla: la cámara se aplana y el panel se encoge al gráfico semanal → la barra del viernes se vuelve un punto de luz → el punto se abre en la primera píldora → salida en blur y Scroll entra en whip → disolución en 100 teselas y otras 100 que convergen en el candado → el candado viaja a su lugar en la tarjeta, que se arma alrededor → la tarjeta se contrae en el botón → al presionarlo, ▶ se vuelve ⏸ y el botón se vuelve el ícono de Pausa |
| Ritmo | 2 de 6 cortes en el beat | Todos los cambios caen en beats de la música (≈139 BPM): 2,58 · 3,01 (drop) · 3,86 · 4,30 · 4,74 · 5,59 · 6,90 · 8,62 · 9,48 · 9,92 · 10,36 · 11,21 · 11,64 · 12,07 · 12,50 · 13,37 · 13,79 |
| Sonido | Música + 19 efectos, algunos ásperos (`glitch-3` con centroide de ~8 kHz, `key-press` y `sparkle` de ~6 kHz) | Música + 89 efectos suaves (todos por debajo de ~3,6 kHz): ticks que siguen la curva de cada contador (con 45 ms mínimo entre ticks), vidrio por cada barra, racimos de partículas para la disolución, succión grave antes del candado, candado, interruptor, reflejo del botón, clic, golpe grave y campana en el logo |
| Mezcla | Sin medir | Master a −16,1 LUFS, pico −1,3 dBTP, sin clipping ni silencios |
| Primer cuadro | Vacío | El panel ya se ve (es la miniatura en redes) |
| Cierre | El lema se veía ~1 s | El lema se ve ~1,9 s; el video dura lo que la música |

## Qué se midió

- `npx hyperframes check`: ok, sin errores.
- `snapshot` en todas las costuras y en el render final, cuadro a cuadro.
- Audio con `hyperframes audio` y `ebur128`. No se escuchó.

## Problemas encontrados y corregidos en la revisión

- La píldora de Sueño se superponía con la de Foco mientras se corría → Foco entra 0,2 s después.
- Un reflejo blanco quedaba visible fuera de la tarjeta (11,6–12,2 s) → solo existe mientras cruza el botón.
- El morph tarjeta → botón mostraba un bloque gris → el color cambia recién cuando la forma ya es una píldora.
- Los ticks de los contadores `expo.out` caían a 10 ms entre sí (zumbido) → separación mínima de 45 ms.

## Advertencias que quedan a propósito

- `line_unread` en "Viernes, 4 de septiembre" y "Bloqueada": son falsos positivos (están en pantalla 2,3 s y 0,85 s; el chequeo los cuenta desde el corte de escena).
- `text_below_floor` en "prom. 6 h" (26 px): es una etiqueta de apoyo del gráfico.

## Lo más débil

1. La marca Pausa usa Inter, como el prototipo. Una tipografía propia le daría más carácter.
2. El ícono de Pausa del logo podría tener un brillo propio; ahora el brillo es un halo detrás.
