# Contexto

## Referencias analizadas

**Opal (16 s, 16:9).** Fondo negro con foco de luz y viñeta; gráfico de barras en 3D con la cámara que se
levanta; barra que se ilumina; píldoras de vidrio con contadores (sueño, foco, descanso) que se abren en un
puntaje; ícono de app que se disuelve en píxeles y se vuelve un candado con brillo rojo; panel de reglas;
botón con barrido de luz; logo desde desenfoque. Audio: música densa con un golpe en cada corte y un "zip".
→ Replicado en `PausaPromo` con una app ficticia ("Pausa") y una red social ficticia ("Scroll").

**Waves Studio (43 s, filmado sobre After Effects).** Degradados azules y blancos, una palabra por golpe con
desenfoque, mockups de laptop y celulares, cursor que escribe una URL, caja 3D con órbitas, lamparita que
ilumina una palabra, mapa, logo con brillo. Ritmo de 0,4–0,6 s por cambio.
→ Componentes `GradientBg`, `WordSwap`, `TypeOn`, `Pointer`, `Laptop`, `Phone`, `Orbit3D`; demo en `KeynoteDemo`.

**Duolingo (TikTok, 22 s).** Trazos de luz neón con cometa, chispas, marcos que se dibujan, contador con
llama, ranking, nodos que se ramifican, texto palabra por palabra, logo que se cierra en un punto.
→ Componentes en `src/motion/neon.tsx`; aplicado en el reel de H30 Puerto Iguazú.

Los videos de referencia no se guardan en el repo (son de terceros); solo el análisis.

## Decisiones

- Remotion en lugar de After Effects: todo es código, se puede versionar y lo puede editar Claude.
- La disolución en píxeles es propia (CSS + máscara) porque `<HtmlInCanvas>` necesita un flag experimental de Chrome.
- 3D con WebGL por software (`swangle` en `remotion.config.ts`) para renderizar en la nube sin GPU;
  en una PC con placa de video conviene `angle`.
- Música de Mixkit (licencia libre para redes y anuncios online, sin atribución); efectos de Pixabay.
- Fuentes locales (Inter) para que el render no dependa de Google Fonts.

## Conexiones y pendientes

- **ElevenLabs** (conectado, versión limitada a voz): voz en off y transcripción con tiempos por palabra.
  El conector completo (`https://api.elevenlabs.io/v1/mcp`) también genera música y efectos.
- **Higgsfield**: skills instaladas; el programa se instala con
  `curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh` (en la nube hace falta
  `--tag v1.2.3` porque la API de GitHub está bloqueada) y falta `higgsfield auth login` con una cuenta con créditos.
- **Alternativas gratis** (`scripts/ia/`): Piper (voz argentina), Whisper (tiempos por palabra), rembg
  (recortar fondos), Pollinations (imágenes). Instalar con `pip install -r scripts/ia/requirements.txt`.
- Video generado por IA gratis: no hay opción viable sin placa de video.
