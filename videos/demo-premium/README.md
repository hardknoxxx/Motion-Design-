# demo-premium

Video de ejemplo de la skill [`motion-premium`](../../.agents/skills/motion-premium/SKILL.md), hecho con [HyperFrames](https://hyperframes.heygen.com). Es un spot de 21 s de una app ficticia de cuidado de plantas, "raíz".

- **Video final**: [`renders/demo-premium.mp4`](renders/demo-premium.mp4)
- **Revisión** (qué se midió, decisiones, puntos débiles): [`REVIEW.md`](REVIEW.md)

## Editar y volver a renderizar

```bash
cd videos/demo-premium
npx hyperframes preview          # vista previa en el navegador
npx hyperframes check            # validación
npx hyperframes render --quality delivery --output renders/demo-premium.mp4
```

## Estructura

| Archivo | Qué es |
|---|---|
| `index.html` | Raíz: monta las escenas, el HUD y la mezcla de sonido. Los colores y la marca son variables editables. |
| `compositions/intro.html` | Chispa → logo de hojas → flood lima |
| `compositions/claim.html` | Titular sans + serif itálica, chips, marcador y countdown |
| `compositions/escalera.html` | Transición de escalera de píxeles |
| `compositions/app.html` | Anuncio de producto: buscador → teléfono → tarjeta → plan → notificación |
| `compositions/datos.html` | Racha de cifras con cortes secos |
| `compositions/marca.html` | Logo, wordmark, CTA y viñeta final |
| `compositions/hud.html` | Marco HUD con timecode real y sección |
| `assets/` | Tipografías (Bricolage Grotesque, Fraunces), hojas recortadas y SFX, todo tomado de la biblioteca de este repo |
