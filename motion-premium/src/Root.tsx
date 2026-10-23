import { Composition, Folder } from "remotion";
import { KeynoteDemo, KEYNOTE_DURATION } from "./promo/KeynoteDemo";
import { PausaPromo, PAUSA_DURATION } from "./promo/PausaPromo";

export const RemotionRoot: React.FC = () => {
  return (
    <Folder name="Pruebas">
      <Composition
        id="PausaPromo"
        component={PausaPromo}
        durationInFrames={PAUSA_DURATION}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="KeynoteDemo"
        component={KeynoteDemo}
        durationInFrames={KEYNOTE_DURATION}
        fps={30}
        width={1920}
        height={1080}
      />
    </Folder>
  );
};
