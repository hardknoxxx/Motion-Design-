# Revisión: demo-premium ("raíz")

Video de prueba de la skill `motion-premium`, construido con HyperFrames: 21 s, 1920 × 1080, 30 fps. Render: [`renders/demo-premium.mp4`](renders/demo-premium.mp4).

## Qué cuenta

Una app ficticia de cuidado de plantas, en cinco ideas, una por escena:

| t (s) | Escena | Idea | Transición de salida |
|---|---|---|---|
| 0–2,75 | Chispa | Un punto lima cae, rebota y explota en un logo de 8 hojas con órbita y tipeo mono | Punto → flood lima |
| 2,75–6,4 | Promesa | "Tus plantas, *sin adivinar.*" con chips de plantas y el countdown "próximo riego" | Iris de papel (entrada) · chips dispersados + escalera de píxeles (salida) |
| 6,3–13,5 | Producto | Buscador → isla → teléfono → tarjeta → toque → la tarjeta rompe el marco → whip → flood verde → plan de riego (ruta y días que ruedan) → notificación | El ícono de la notificación se vuelve el mundo |
| 13,5–15,65 | Pruebas | 12.000+ · 98 % · 3 min · 4,9/5, un corte seco por beat (0,5 s) | El panel lima se difumina |
| 15,6–21 | Marca | Partículas que convergen → logo con anillo → "raíz" letra a letra → lema → CTA | Viñeta que se cierra a negro |

## Qué se midió y qué no

- `npx hyperframes check`: **ok**, sin errores.
- Se revisaron con `snapshot` todas las costuras entre escenas, el morph del producto y el cuadro 0.
- Audio medido con `hyperframes audio`: pico real −1,5 dBTP, sin clipping, −21 LUFS integrados. **No se escuchó.** Al ser solo efectos, sin música de fondo, la sonoridad integrada queda baja para redes (el objetivo es −16 a −14). Con una pista de música se resuelve.
- Sin música: este entorno no tiene fuente de música. El ritmo sigue una grilla virtual de 120 BPM (cortes cada 0,5 s en la racha de datos).

## Decisiones creativas

- El acento lima `#CDD54A` vive en tres lugares: el punto inicial, el marcador de "adivinar." y el panel de la mejor métrica. El verde `#1E4D2B` es el color de la "marca" de la app (botón, flood, ícono).
- Transiciones usadas (5 tipos): flood + iris, escalera de píxeles, morph de contenedor, flood circular con doble iris y objeto que se vuelve mundo. Más cortes secos dentro de la racha de datos.
- Los títulos aterrizan y quedan quietos; el movimiento pasa a los chips, al countdown y al HUD.

## Advertencias que se dejaron a propósito

- `line_unread` en la racha de datos (0,5 s por cifra): es la racha de cortes del estilo. Las cifras se leen y las etiquetas son de apoyo.
- `line_unread` en el tipeo mono del intro: es decorativo.
- `text_below_floor` en el meta de la tarjeta (17 px) y en el CTA: son detalle de UI a tamaño de UI. La tarjeta crece ×1,42 justo después.

## Lo más débil y qué haría con más tiempo

1. **Sin música.** Es lo que más separa este demo de la referencia. Le pondría una pista de 108–120 BPM y movería los cortes a sus beats reales (`npx hyperframes beats`).
2. **El verde del "objeto se vuelve mundo"** (13,1–13,5 s) crece desde arriba a la izquierda y tapa el HUD; podría crecer desde el centro del teléfono.
3. **El intro** (0–1 s) tiene medio segundo de papel vacío antes de que caiga el punto. Es fiel a la referencia, pero en redes el primer cuadro debería tener algo.
