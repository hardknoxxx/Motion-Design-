# Motion Design: biblioteca de recursos

Recursos libres para motion design (After Effects, Premiere, DaVinci, Cinema 4D, Blender, Figma). Todo es **de uso comercial libre**: CC0 / dominio público, salvo las tipografías, que son OFL o Apache (también de uso comercial libre; ver abajo).

| Carpeta | Qué hay | Formato |
|---|---|---|
| [`sfx-botanica/`](sfx-botanica/) | 30 sonidos de naturaleza: hojas, madera, agua, aves, viento, grillos, ambientes de parque | WAV / MP3 48 kHz |
| [`sfx/`](sfx/) | ~840 efectos de sonido: whooshes, pops, UI, impactos, digital/sci-fi, jingles, foley de papel y oficina, agua, fuego | WAV 48 kHz 16-bit |
| [`texturas/`](texturas/) | 178 texturas 2K: papel, cartón, corteza, musgo, pasto, hojas, mimbre, madera, tela, yeso, piedra… | JPG 2048 px |
| [`elementos-png/`](elementos-png/) | 325 recortes con transparencia: hojas, follaje, flores, ramas, conchas, agujas de pino, cinta adhesiva, cartón | PNG con alfa |
| [`overlays/`](overlays/) | Grano de película, light leaks, bokeh, polvo y rayas, imperfecciones (huellas, manchas, rayones) | MP4 1080p / JPG |
| [`particulas/`](particulas/) | Sprites de partículas (chispas, humo, destellos, estrellas, círculos) y manchas de pintura | PNG con alfa / SVG |
| [`luts/`](luts/) | 10 looks de color: botánico verde, cálido dorado, película desvanecida, teal-naranja… | `.cube` 33³ |
| [`tipografias/`](tipografias/) | 25 familias: serif editoriales, sans modernas, manuscritas, mono | TTF (muchas variables) |

## Skills y videos

| Carpeta | Qué hay |
|---|---|
| [`.agents/skills/motion-premium/`](.agents/skills/motion-premium/SKILL.md) | **Estilo premium minimalista** aprendido de dos referencias medidas cuadro a cuadro: tokens de color y tipografía, repertorio de transiciones con sus tiempos, recetas de código, sonido mapeado a esta biblioteca y lista de control |
| `.agents/skills/hyperframes*`, `media-use`, `figma`, `slideshow`, `remotion-to-hyperframes` | Skills de [HyperFrames](https://hyperframes.heygen.com) (HTML → video), instaladas con `npx skills add heygen-com/hyperframes` |
| [`videos/demo-premium/`](videos/demo-premium/) | Spot de 21 s hecho con la skill y HyperFrames, con el render en `renders/demo-premium.mp4` y su revisión |
| [`videos/pausa-promo/`](videos/pausa-promo/) | Promo de 16,5 s de la app "Pausa", rehecha con la skill a partir del prototipo en Remotion |

## Cómo usar cada cosa

### `sfx/`
| Subcarpeta | Para qué |
|---|---|
| `whoosh-transiciones/` | Transiciones, textos que entran volando, cambios de escena |
| `pops-burbujas/` | Íconos que aparecen, bullets, burbujas |
| `ui-interfaz/` | Clicks, toggles, notificaciones, mockups de apps |
| `campanas-acentos/` | Logo reveals, "éxito", remates |
| `impactos/` | Golpes secos para kinetic typography |
| `digital-tech/` | Glitches, bleeps, HUDs, sci-fi |
| `jingles-stingers/` | Remates musicales cortos (8-bit, pizzicato, saxo, steel drum, hits) |
| `foley-papel-oficina/` | Pasar páginas, lápiz escribiendo y borrando, máquina de escribir, obturador de cámara |
| `agua-splash/`, `fuego/` | Elementos naturales |
| `varios-cc0/` | Packs grandes surtidos: puertas, vidrio, platos, pasos, metal, madera, truenos, loops de ambiente |

### `texturas/`
Fondos y materiales. En After Effects van bien como capa de fondo, o encima en modo **Multiplicar / Superposición / Luz suave** a 10–40 % de opacidad para que un diseño plano tenga "papel" o materia.

### `elementos-png/`
Cada hoja, flor o tira de cinta viene recortada sola, con fondo transparente. Sirven para collage, para animar hojas cayendo o para armar marcos botánicos. `hojas/` tiene 200 hojas distintas.

### `overlays/`
| Subcarpeta | Modo de fusión sugerido |
|---|---|
| `grano-pelicula/` (fino, medio, grueso) | **Superposición** o **Luz suave**, en loop. El fondo es gris 50 %, así que no altera los tonos. |
| `light-leaks/` (6 colores) | **Pantalla** o **Añadir**. Son loops de 8 s. |
| `bokeh/` (dorado, verde, blanco) | **Pantalla**. Loops de 8 s. |
| `polvo-y-rayas/` | **Pantalla**. Polvo, pelusas y rayas de película sobre negro. |
| `imperfecciones/` | Grises: huellas, manchas, rayones, suciedad. Úsalos en **Pantalla / Superposición**, o como mate de luminancia. |

### `luts/`
- **After Effects / Premiere:** efecto *Lumetri Color* → *Básico* → *Entrada LUT* → *Examinar*, o el efecto *Apply Color LUT*.
- **DaVinci:** copia los `.cube` a la carpeta de LUTs y actualiza la lista.
- Todos esperan material en Rec.709 (no LOG).

### `particulas/`
`kenney-particulas/` trae chispas, humo, fuego, estrellas, círculos, luces y trazos de magia, en blanco para colorear con *Tint* o *Fill*. `humo/` tiene secuencias de humo y destellos, y `manchas-pintura/` 36 salpicaduras más un SVG vectorial con todas.

### `tipografias/`
Instala los `.ttf`. Los archivos con corchetes, como `Inter[opsz,wght].ttf`, son **fuentes variables**: un solo archivo trae todos los pesos, y el peso se puede animar en After Effects.
- **serif:** Fraunces, Cormorant Garamond, Playfair Display, DM Serif Display, Gloock, Young Serif, Instrument Serif, Libre Caslon Text
- **sans:** Inter, DM Sans, Manrope, Space Grotesk, Syne, Outfit, Plus Jakarta Sans, Bricolage Grotesque, Unbounded
- **manuscritas:** Caveat, Homemade Apple, Reenie Beanie, La Belle Aurore, Dancing Script, Pinyon Script
- **mono:** JetBrains Mono, Space Mono

## Licencias y créditos

| Recurso | Fuente | Licencia |
|---|---|---|
| `texturas/`, `elementos-png/`, `overlays/imperfecciones/` | [ambientCG.com](https://ambientcg.com) (Lennart Demes) | CC0 |
| `particulas/`, `sfx/ui-interfaz/kenney-*`, `sfx/impactos/`, `sfx/digital-tech/`, `sfx/jingles-stingers/` | [Kenney.nl](https://kenney.nl) | CC0 |
| `sfx/varios-cc0/pack-1`, `pack-2`, `sfx/agua-splash/` (40 sonidos) | rubberduck, OpenGameArt | CC0 |
| `sfx/ui-interfaz/menu`, `sfx/varios-cc0/verano`, `espacio`, `industria`, `sfx/agua-splash/agua-*` | qubodup, OpenGameArt (*Atmospheric Interaction Sound Pack*) | CC0 |
| `sfx/whoosh-transiciones/` | pyranostudios (*Air whoosh*), artisticdude (*Swishes*), ezduzziteh (*Slide pop*), OpenGameArt | CC0 |
| `sfx/pops-burbujas/` | wubitog, trezegames, farfadet46, bmaczero, OpenGameArt | CC0 |
| `sfx/campanas-acentos/` | pwl, OpenGameArt | CC0 |
| `sfx/foley-papel-oficina/` | starninjas (páginas), antumdeluge (lápiz), cassie-orbitgames (máquina de escribir), themightyglider (cámara), OpenGameArt | CC0 |
| `sfx/fuego/` | antumdeluge, OpenGameArt | CC0 |
| `sfx-botanica/` | Ver [`sfx-botanica/README.md`](sfx-botanica/README.md) | CC0 |
| `overlays/grano-pelicula`, `light-leaks`, `bokeh`, `polvo-rayas`, `luts/` | Generados para este repo (scripts en [`_herramientas/`](_herramientas/)) | CC0 |
| `tipografias/` | [Google Fonts](https://github.com/google/fonts) | SIL OFL 1.1 (Homemade Apple: Apache 2.0). La licencia va dentro de cada carpeta. |

CC0 no exige atribución, pero si quieres agradecer, "Texturas de ambientCG.com · Sonidos de Kenney.nl y OpenGameArt.org" es suficiente.

## Formatos
- Los sonidos están en WAV 48 kHz porque After Effects y Premiere no importan OGG. Los originales venían en OGG, FLAC o WAV.
- Las texturas son el mapa de color en 2K. Si necesitas normal, roughness o displacement para 3D, búscalas por su nombre (p. ej. `Bark007`) en ambientCG.
- Los loops de video son H.264 1080p 24 fps.
