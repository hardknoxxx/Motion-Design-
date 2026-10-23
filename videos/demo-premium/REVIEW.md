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
- Audio medido con `hyperframes audio`, sin escucharlo. El master final queda en −16,5 LUFS integrados con pico real de −1,4 dBTP, sin clipping y sin huecos de silencio después de los 0,2 s.
- Sonido (segunda pasada): 139 eventos sobre una cama ambiental botánica (viento suave y aves lejanas a −30 LUFS). Hay gotas de agua para las partículas y los chips, una tecla suave por carácter y ticks de reloj que siguen la curva del countdown y de los números que ruedan. El subrayado de "adivinar." ahora suena como un barrido de aire con un roce de papel, con el centroide en ~1,1 kHz (el raspón anterior estaba en ~7,5 kHz). La ruta de riego suena a agua y el logo cierra con un canto de pájaro breve. Se verificó que los golpes caen sobre su imagen (onsets del render contra la hoja de cues).
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

1. **Sin música.** La cama ambiental llena el espacio, pero una pista de 108–120 BPM con los cortes en sus beats reales (`npx hyperframes beats`) lo acercaría más a la referencia.
2. **El verde del "objeto se vuelve mundo"** (13,1–13,5 s) crece desde arriba a la izquierda y tapa el HUD; podría crecer desde el centro del teléfono.
3. **El intro** (0–1 s) tiene medio segundo de papel vacío antes de que caiga el punto. Es fiel a la referencia, pero en redes el primer cuadro debería tener algo.
