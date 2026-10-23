# Motion premium

Kit para hacer videos de producto y marketing con motion "premium" en [Remotion](https://remotion.dev):
librería de componentes, skill para Claude, scripts de sonido/IA y dos videos de prueba.

| Estilo | Referencia | Prueba |
|---|---|---|
| Producto oscuro (vidrio, 3D, contadores) | Comercial de Opal | `PausaPromo` → `videos/pausa-promo.mp4` |
| Keynote / agencia (degradados, palabra por palabra, mockups, 3D) | Reel de Waves Studio | `KeynoteDemo` → `videos/keynote-demo.mp4` |
| Neón (trazos de luz, nodos, chispas) | Motion de Duolingo | Reel de H30 (repo `hardknoxxx/H30`) |

## Uso

```bash
npm install
npm run dev                                   # Remotion Studio
scripts/render-master.sh PausaPromo out/pausa.mp4   # render + audio a -14 LUFS
scripts/revisar-cuadros.sh PausaPromo out/hoja.jpg 30 120 300   # hoja de cuadros para revisar
python3 scripts/analizar-audio.py public/musica/x.mp3           # tempo y drop de una pista
```

## Contenido

- `src/motion/` — componentes reutilizables (ver la tabla en `.claude/skills/motion-premium/SKILL.md`).
- `src/promo/` — los dos videos de prueba.
- `.claude/skills/motion-premium/` — skill con las recetas de cada estilo, sonido y análisis de referencias.
  También están instaladas las skills de Remotion, HyperFrames y Higgsfield (`.agents/skills`).
- `scripts/` — análisis de música, revisión de cuadros, render con master y `scripts/ia/` (voz, transcripción,
  recorte de fondos e imágenes gratis).
- `public/` — fuente Inter, efectos de sonido (Pixabay) y música (Mixkit); licencias en `public/musica/CREDITOS.md`
  y `public/sfx/CREDITS.md`.
- `videos/` — renders de prueba y una muestra de la voz gratuita.
- `CONTEXTO.md` — qué se analizó de cada referencia, decisiones tomadas y qué falta conectar.
