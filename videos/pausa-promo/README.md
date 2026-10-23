# pausa-promo

Promo de 16,5 s de "Pausa", una app ficticia para reducir el tiempo en pantalla, rehecha en [HyperFrames](https://hyperframes.heygen.com) con la skill [`motion-premium`](../../.agents/skills/motion-premium/SKILL.md).

- **Video final**: [`renders/pausa-promo.mp4`](renders/pausa-promo.mp4)
- **Revisión y cambios respecto del prototipo**: [`REVIEW.md`](REVIEW.md)

```bash
cd videos/pausa-promo
npx hyperframes preview
npx hyperframes check
npx hyperframes render --quality delivery --output renders/pausa-promo.mp4
```

| Archivo | Escena |
|---|---|
| `compositions/fondo.html` | Negro con foco de luz, viñeta y grano |
| `compositions/panel.html` | Panel 3D por hora → semana → el viernes se enciende → punto de luz |
| `compositions/bienestar.html` | Píldoras Sueño · Foco · Descanso y puntaje |
| `compositions/bloqueo.html` | Scroll se desintegra y se rearma como candado |
| `compositions/cierre.html` | Reglas → botón Empezar → ícono de Pausa → logo |
| `assets/musica.mp3` | "Trap Electro Vibes" (Mixkit, licencia libre para redes) |
| `assets/sfx/` | Efectos suaves: la mayoría de la biblioteca del repo, más golpe grave, pop, aire y campana del prototipo (Pixabay), todos filtrados |
