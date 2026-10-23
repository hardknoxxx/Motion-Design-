# Gramática medida de las referencias

Medido a 10 fps sobre las dos referencias, con detección de beat con librosa. Lo que está marcado *(estimado)* se dedujo de la imagen y no se midió.

## Referencia A: reel editorial con HUD (16:9, 33,6 s)

Son dos reels encadenados: "Otak Rental" (servicio) y "Claude, motion designer" (portafolio). El HUD declara 1920 × 1080 a 60 fps; el archivo recibido es de 30 fps.

**Música**: ~108 BPM medidos (el HUD dice 120 BPM), es decir un beat cada 0,556 s. Los cambios de escena caen sobre el beat (5,55 · 8,85 · 11,05 · 12,72 s) y la segunda mitad, la cinética, corta en corcheas (≈0,28 s). La sonoridad es pareja de punta a punta, sin silencios, con una subida en el logo final.

### Escena por escena

| t (s) | Escena | Qué pasa | Transición de salida |
|---|---|---|---|
| 0,0–0,3 | Vacío | Papel `#F3ECE4` con el HUD solamente | — |
| 0,3–0,9 | Chispa | Cae un punto lima de 24 px y rebota con squash, con sombra de contacto | — |
| 1,0–1,4 | Big bang | Un anillo lima se expande de 40 px a tamaño de cuadro y se desvanece; 8 puntos negros orbitan y forman un asterisco; aparecen partículas sueltas | — |
| 1,5–2,2 | Logo vivo | Una elipse de órbita se dibuja alrededor; debajo, mono que se tipea: `> sewa otak teknis — initializing█` | — |
| 2,3–2,5 | Colapso | El asterisco se contrae a un punto y el punto crece a 70 px | **Punto → flood lima (2,6) → iris de papel (2,7)** |
| 2,8–5,2 | Deadline | "Deadline" en serif itálica gigante (≈13 % de la altura) entra con blur; debajo, una píldora negra con countdown real (71:53:08 → 03:12:08); 8 chips de tareas con sombra suave flotan alrededor y van apareciendo | Los chips se dispersan con blur radial (0,1–0,2 s) |
| 5,0–5,5 | Claim | **Blur swap**: "Deadline" sale hacia arriba; entra "Sewa otak teknis," (sans negra) y luego "*sebelum deadline mencekik.*" (serif itálica gris verdosa); el marcador lima barre "mencekik." en 0,2 s | **Escalera de píxeles** negra en diagonal (5,6–6,3; 0,2 s en negro total) |
| 6,3–8,4 | Fórmula | "Harga dihitung, *bukan ditebak.*" y 5 chips de valores (20 × 25rb × 1,5x × 1,4x + 50rb) entran en cascada; curvas finas bajan a una píldora negra con el total, que rueda (Rp 1.069.795 → 1.100.000) | Los chips bajan, la píldora se difumina y un chip **morfa** en tarjeta oscura (8,9–9,3) |
| 9,0–11,4 | Servicios | La tarjeta oscura "Development Project" (código con sintaxis) se inclina y se vuelve la pieza grande de un **bento en perspectiva** (`rotateX` ≈ 8°, `rotateZ` ≈ −4° *(estimado)*); 5 tarjetas claras entran escalonadas (≈80 ms) con mini-gráficos, sombras largas y suaves | Corte seco |
| 11,4–13,0 | Pruebas | **Racha de cortes secos** cada 0,3–0,5 s: 420+ (papel), 99 % (panel negro), 100 %, 5 % → 0 % (papel), 4,9/5 (panel lima). Cada número rueda con blur vertical; detrás, el mismo número gigante al 5 % | Panel lima → blur out (13,0) |
| 13,1–13,6 | Reensamble | Partículas con estela de movimiento convergen en un anillo de 8 puntos y colapsan al centro | — |
| 13,6–14,4 | Marca | Aparece el logo (cerebro + órbita + destellos) dentro de un anillo lima que pulsa; el logo sube y debajo se tipea el wordmark "Otak Rental" letra a letra; tagline itálica y CTA en píldora negra con ícono | **Iris de viñeta a negro** (14,6) |
| 14,7–16,3 | Reel 2: arranque | En fondo negro, un asterisco naranja gira dentro de un anillo de texto mono | **Flood naranja** `#FC5C36` |
| 16,3–18,0 | Nombre | "CLAUDE" en sans **extendida** entra con `scaleX` y estela; debajo "*motion designer*" en serif | Corte |
| 18,0–20,0 | Easing | "*Six ways to get from A to B.*": seis pelotas con linear, ease-in-out, expo-out, back-out, elastic y bounce; cada una con su curva dibujada y motion blur según su velocidad | Corte a cobalto `#2E3CFC` |
| 20,0–22,0 | Morfología | Una forma blanca muta círculo → blob → estrella → cuadrado con partículas orbitando | Corte |
| 22,0–24,0 | Patrón | Mosaico truchet en negro, blanco y coral cuyas piezas rotan; luego una esfera de puntos en 3D | Corte |
| 25,8–27,8 | Cinética | EASE · IN. · OUT. · NEVER · LINEAR., una palabra por corchea, cada una con su fondo (naranja, negro, papel, cobalto, lima eléctrica `#E6FC40`); entran con estela horizontal, el punto final siempre en otro color y "NEVER" se repite como marquesina | **Punto → anillo → asterisco** |
| 27,8–29,5 | Firma | Asterisco + "CLAUDE" + "*motion designer*" + línea de datos mono | Fin |

### Constantes de A
- El HUD está siempre presente (esquinas, TC que corre, sección `0N — NOMBRE`, resolución y fps). Le da "producto terminado" a todo.
- El papel lleva una retícula muy tenue y nunca es blanco puro.
- Los paneles de color van insertados, con margen ≈3 % y radio ≈28 px, no a sangre. El flood a sangre se reserva para las transiciones.
- Un solo acento por escena. El lima (`#CDD54A`) significa la idea clave: el marcador, el anillo, el panel de la mejor métrica.
- Los titulares combinan sans negra con tracking cerrado y serif itálica en la misma línea; el contraste de familias reemplaza al contraste de tamaño.

## Referencia B: anuncio de producto con UI (9:16, 17 s; filmado de un monitor)

Concepto de app de delivery. El audio es casi silencio (teclado, ambiente) hasta un golpe fuerte en la revelación de marca (~13 s); el ritmo lo lleva la imagen.

| t (s) | Qué pasa | Técnica |
|---|---|---|
| 2,5–3,3 | Pantalla crema cálida; aparece una píldora de búsqueda con sombra suave | Fade + leve subida |
| 3,3–4,0 | El placeholder "¿Qué te provoca hoy?" entra letra a letra (gris, ~30 ms por letra, cada letra sube 6 px) | Tipeo con entrada por letra |
| 4,0–4,3 | El placeholder se borra rápido | Borrado ~40 ms por letra |
| 4,3–5,1 | Se tipea "pollo a la brasa" a ~10–12 caracteres por segundo con cursor | Tipeo |
| 5,1–5,6 | La píldora se encoge y se vuelve la isla del teléfono; el contorno del teléfono (línea negra de 3 px, radio ~18 %) se dibuja desde ahí | **Morph de contenedor** |
| 5,8–6,3 | Una tarjeta de resultado (foto, nombre, rating, precio, botón rojo "Agregar") sube desde abajo, con las capas escalonadas | Slide-up con escalonado |
| 6,7–7,1 | La tarjeta crece ×1,4 y **rompe el marco del teléfono** | Objeto se vuelve héroe |
| 7,2 | Se presiona el botón (punto de toque) | Escala 0,96, 80 ms |
| 7,3–7,6 | La tarjeta sale hacia arriba con blur vertical fuerte | **Whip** vertical |
| 7,7–8,0 | Un círculo rojo de marca se expande desde la esquina superior derecha del teléfono y revela el mapa | **Flood circular** con causa |
| 8,0–10,0 | La ruta se dibuja en ortogonales con flecha; el ETA rueda 12 → 6 → 1 min y la barra de progreso avanza | `stroke-dashoffset` + número que rueda |
| 10,2–10,9 | La notificación "Tu pedido llegó" baja desde la isla; el teléfono baja y la cámara empuja | Slide-down + push de cámara |
| 11,1–11,8 | El ícono de la app en la notificación crece hasta cubrir el teléfono: panel rojo de marca con el bigote | **Objeto se vuelve mundo** |
| 12,0–12,4 | El wordmark "Rappi" aparece con blur sobre el bigote | Blur in |
| 12,4–13,0 | Hold de la marca y golpe sonoro | Hold |

### Constantes de B
- Crema cálido, rojo de marca y tinta. **Nada más**.
- No hay cortes: es una sola toma continua donde cada pantalla nace de la anterior. Esa continuidad es lo que lo hace "premium".
- La UI se muestra grande, plana, sin perspectiva, con un solo foco a la vez.
- Las sombras son tan suaves que solo se notan porque los objetos "se despegan" del fondo.

## Lista de control

Revisa esto antes de entregar (en `snapshot --review`):

- [ ] Cada escena se describe en una frase de ≤ 7 palabras.
- [ ] Hay un solo acento por escena y está en la palabra u objeto clave.
- [ ] El héroe ocupa 40–60 % del ancho; el resto respira.
- [ ] Cada transición tiene una causa visible y hay 3–5 tipos, sin repetir dos seguidos.
- [ ] Los títulos aterrizan y quedan quietos; nada flota.
- [ ] Hay al menos una racha de cortes secos y al menos una pausa antes del remate.
- [ ] Los números ruedan y aterrizan; los countdowns corren de verdad.
- [ ] Las sombras van en capas y son suaves; no hay degradados de fondo.
- [ ] Cada corte o llegada lleva un sonido, sin repetir el mismo whoosh dos veces seguidas.
- [ ] El logo llega en el último 10 % y aguanta ≥ 1,5 s.
