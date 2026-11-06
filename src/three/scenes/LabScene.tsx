import { useFrame } from "@react-three/fiber";
import { useMemo, useRef } from "react";
import * as THREE from "three";
import { tierSettings } from "../tier";
import type { SceneProps } from "../Canvas3D";

const NAVY2 = "#14284a";
const TEAL = "#038d91";
const GLOW = "#3fd0d3";

const panels = [
  { code: "PMS", name: "PetraPMS", pos: [-3.4, -1.3, 0.2] as const },
  { code: "POS", name: "PetraPOS", pos: [0, -1.7, 1.1] as const },
  { code: "DMS", name: "PetraDMS", pos: [3.4, -1.3, 0.2] as const },
];

/** Procedural "screen" texture: no image downloads. */
function useScreenTexture(code: string, name: string) {
  return useMemo(() => {
    const c = document.createElement("canvas");
    c.width = 512;
    c.height = 320;
    const g = c.getContext("2d")!;
    const bg = g.createLinearGradient(0, 0, 512, 320);
    bg.addColorStop(0, "#102640");
    bg.addColorStop(1, "#0b1a30");
    g.fillStyle = bg;
    g.fillRect(0, 0, 512, 320);
    g.fillStyle = "rgba(63,208,211,0.9)";
    g.font = "700 88px system-ui, sans-serif";
    g.fillText(code, 34, 130);
    g.fillStyle = "rgba(255,255,255,0.75)";
    g.font = "500 26px system-ui, sans-serif";
    g.fillText(name, 38, 172);
    [0.45, 0.7, 0.55, 0.85, 0.6, 0.95, 0.5].forEach((v, i) => {
      g.fillStyle = i === 5 ? "#3fd0d3" : "rgba(255,255,255,0.18)";
      g.fillRect(36 + i * 64, 296 - v * 90, 44, v * 90);
    });
    const tex = new THREE.CanvasTexture(c);
    tex.colorSpace = THREE.SRGBColorSpace;
    return tex;
  }, [code, name]);
}

function Panel({ code, name, pos, index }: { code: string; name: string; pos: readonly [number, number, number]; index: number }) {
  const ref = useRef<THREE.Group>(null);
  const tex = useScreenTexture(code, name);
  const edges = useMemo(() => new THREE.EdgesGeometry(new THREE.BoxGeometry(2.7, 1.7, 0.09)), []);
  useFrame(({ clock }) => {
    if (ref.current) ref.current.position.y = pos[1] + Math.sin(clock.elapsedTime * 0.9 + index * 1.7) * 0.12;
  });
  return (
    <group ref={ref} position={[pos[0], pos[1], pos[2]]}>
      <mesh>
        <boxGeometry args={[2.7, 1.7, 0.09]} />
        <meshStandardMaterial color={NAVY2} metalness={0.4} roughness={0.35} transparent opacity={0.92} />
      </mesh>
      <mesh position={[0, 0, 0.051]}>
        <planeGeometry args={[2.5, 1.5]} />
        <meshBasicMaterial map={tex} toneMapped={false} />
      </mesh>
      <lineSegments geometry={edges}>
        <lineBasicMaterial color={GLOW} transparent opacity={0.7} />
      </lineSegments>
    </group>
  );
}

/** Dashed core-to-product link. Every link is planned, so every link is dashed. */
function PlannedLink({ to }: { to: readonly [number, number, number] }) {
  const line = useMemo(() => {
    const geo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, 1.1, 0), new THREE.Vector3(to[0], to[1] + 0.9, to[2])]);
    const mat = new THREE.LineDashedMaterial({ color: GLOW, dashSize: 0.18, gapSize: 0.14, transparent: true, opacity: 0.85 });
    const l = new THREE.Line(geo, mat);
    l.computeLineDistances();
    return l;
  }, [to]);
  useFrame((_, delta) => {
    (line.material as THREE.LineDashedMaterial & { dashOffset: number }).dashOffset -= delta * 0.5;
  });
  return <primitive object={line} />;
}

function Particles({ count }: { count: number }) {
  const ref = useRef<THREE.Points>(null);
  const positions = useMemo(() => {
    const arr = new Float32Array(count * 3);
    for (let i = 0; i < count; i++) {
      const r = 5 + Math.random() * 5;
      const th = Math.random() * Math.PI * 2;
      const ph = Math.acos(2 * Math.random() - 1);
      arr.set([r * Math.sin(ph) * Math.cos(th), r * Math.sin(ph) * Math.sin(th) * 0.6, r * Math.cos(ph) - 2], i * 3);
    }
    return arr;
  }, [count]);
  useFrame((_, delta) => {
    if (ref.current) ref.current.rotation.y += delta * 0.03;
  });
  return (
    <points ref={ref}>
      <bufferGeometry>
        <bufferAttribute attach="attributes-position" args={[positions, 3]} />
      </bufferGeometry>
      <pointsMaterial color={GLOW} size={0.045} sizeAttenuation transparent opacity={0.65} depthWrite={false} />
    </points>
  );
}

export default function LabScene({ tier, pointer }: SceneProps) {
  const cfg = tierSettings[tier];
  const rig = useRef<THREE.Group>(null);
  const core = useRef<THREE.Group>(null);

  useFrame(({ clock, pointer: p }, delta) => {
    const t = clock.elapsedTime;
    if (rig.current) {
      const ty = pointer ? p.x * 0.28 : Math.sin(t * 0.25) * 0.14;
      const tx = pointer ? -p.y * 0.14 : 0;
      rig.current.rotation.y = THREE.MathUtils.damp(rig.current.rotation.y, ty, 3, delta);
      rig.current.rotation.x = THREE.MathUtils.damp(rig.current.rotation.x, tx, 3, delta);
    }
    if (core.current) {
      core.current.rotation.y = t * 0.5;
      core.current.rotation.x = t * 0.2;
    }
  });

  return (
    <>
      <ambientLight intensity={0.9} />
      <directionalLight position={[3, 5, 6]} intensity={1.6} color="#ffffff" />
      <pointLight position={[0, 2, 4]} intensity={30} color={GLOW} />
      <group ref={rig}>
        <group ref={core} position={[0, 1.1, 0]}>
          <mesh>
            <octahedronGeometry args={[0.85, 0]} />
            <meshBasicMaterial color={GLOW} wireframe />
          </mesh>
          <mesh>
            <icosahedronGeometry args={[0.42, 1]} />
            <meshStandardMaterial color={TEAL} emissive={TEAL} emissiveIntensity={0.9} metalness={0.2} roughness={0.3} />
          </mesh>
        </group>
        <mesh position={[0, 1.1, 0]} rotation={[Math.PI / 2.4, 0, 0]}>
          <torusGeometry args={[1.35, 0.012, 8, cfg.segments * 3]} />
          <meshBasicMaterial color={GLOW} transparent opacity={0.55} />
        </mesh>
        {panels.map((p, i) => (
          <group key={p.code}>
            <Panel code={p.code} name={p.name} pos={p.pos} index={i} />
            <PlannedLink to={p.pos} />
          </group>
        ))}
        <Particles count={cfg.particles} />
      </group>
    </>
  );
}
