import { Canvas, useFrame } from "@react-three/fiber";
import { Suspense, lazy, useCallback, useEffect, useRef, useState, type ComponentType } from "react";
import { detectEnv } from "./detect";
import { chooseTier, downgrade, isTooSlow, tierSettings, type Tier } from "./tier";

export interface SceneProps {
  tier: Exclude<Tier, "off">;
  pointer: boolean;
}

/** One lazy chunk per scene, so a page only downloads the scenes it shows. */
const scenes = {
  lab: lazy(() => import("./scenes/LabScene")),
} satisfies Record<string, React.LazyExoticComponent<ComponentType<SceneProps>>>;

export type SceneId = keyof typeof scenes;

interface Props {
  scene: SceneId;
  /** Text alternative: the canvas is decorative, this describes what it shows. */
  description: string;
  /** Pre-rendered image shown first and whenever 3D is off. */
  poster?: string;
  aspect?: string;
  className?: string;
}

/**
 * Measures frame rate after a short warm-up and reports once if the device cannot keep up.
 * Time is summed from frame deltas (long gaps from paused rendering are ignored), so scrolling
 * the scene off screen mid-probe cannot cause a false "slow" result.
 */
function FpsProbe({ onSlow }: { onSlow: () => void }) {
  const s = useRef({ frames: 0, seconds: 0, done: false });
  useFrame((_, delta) => {
    const st = s.current;
    if (st.done) return;
    st.frames += 1;
    if (st.frames <= 15) return; // warm-up: shader compile, texture upload
    if (delta < 0.25) st.seconds += delta;
    if (st.frames >= 90) {
      st.done = true;
      if (isTooSlow(st.frames - 15, st.seconds)) onSlow();
    }
  });
  return null;
}

function FirstFrame({ onFrame }: { onFrame: () => void }) {
  const fired = useRef(false);
  useFrame(() => {
    if (!fired.current) {
      fired.current = true;
      onFrame();
    }
  });
  return null;
}

export default function Canvas3D({ scene, description, poster, aspect = "16 / 10", className = "" }: Props) {
  const [tier, setTier] = useState<Tier | "pending">("pending");
  const [ready, setReady] = useState(false);
  const [inView, setInView] = useState(true);
  const [tabVisible, setTabVisible] = useState(true);
  const host = useRef<HTMLDivElement>(null);

  // Decide the tier once on the client, and drop to the poster if the visitor turns on reduced motion later.
  useEffect(() => {
    setTier(chooseTier(detectEnv()));
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const onChange = () => mq.matches && setTier("off");
    mq.addEventListener("change", onChange);
    return () => mq.removeEventListener("change", onChange);
  }, []);

  // Stop rendering while the scene is off screen or the tab is hidden.
  useEffect(() => {
    if (!host.current || !("IntersectionObserver" in window)) return;
    const io = new IntersectionObserver(([e]) => setInView(e.isIntersecting), { threshold: 0 });
    io.observe(host.current);
    const onVis = () => setTabVisible(!document.hidden);
    document.addEventListener("visibilitychange", onVis);
    return () => {
      io.disconnect();
      document.removeEventListener("visibilitychange", onVis);
    };
  }, []);

  const slow = useCallback(() => {
    setReady(false);
    setTier((t) => (t === "pending" ? t : downgrade(t)));
  }, []);

  const Scene = scenes[scene] as ComponentType<SceneProps>;
  const live = tier !== "pending" && tier !== "off";
  const settings = live ? tierSettings[tier] : null;

  return (
    <div
      ref={host}
      role="img"
      aria-label={description}
      data-tier={tier}
      data-ready={ready}
      className={`relative overflow-hidden ${className}`}
      style={{ aspectRatio: aspect }}
    >
      {poster && (
        <img
          src={poster}
          alt=""
          width={1600}
          height={1000}
          decoding="async"
          className="absolute inset-0 h-full w-full object-cover transition-opacity duration-700"
          style={{ opacity: live && ready ? 0 : 1 }}
        />
      )}
      {live && settings && (
        <div className="absolute inset-0" aria-hidden="true">
          <Canvas
            key={tier}
            frameloop={inView && tabVisible ? "always" : "never"}
            dpr={settings.dpr}
            gl={{ antialias: settings.antialias, alpha: true, powerPreference: "high-performance" }}
            camera={{ position: [0, 0, 10.8], fov: 38 }}
            onCreated={({ gl }) => {
              gl.domElement.addEventListener("webglcontextlost", (e) => {
                e.preventDefault();
                setReady(false);
                setTier("off");
              });
            }}
          >
            <Suspense fallback={null}>
              <Scene tier={tier} pointer={settings.pointer} />
              <FirstFrame onFrame={() => setReady(true)} />
            </Suspense>
            <FpsProbe onSlow={slow} />
          </Canvas>
        </div>
      )}
    </div>
  );
}
