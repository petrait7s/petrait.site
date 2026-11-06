/**
 * Quality tiers for the 3D layer. Pure functions, so the rules are unit-tested.
 *  off  poster image only (no WebGL, reduced motion, Save-Data, or too slow)
 *  low  reduced scene: fewer objects, no pointer parallax, capped pixel ratio (phones, weak devices)
 *  high full scene
 */
export type Tier = "off" | "low" | "high";

export interface Env {
  width: number;
  reducedMotion: boolean;
  saveData: boolean;
  webgl: boolean;
  cores: number;
  memoryGb: number;
  coarsePointer: boolean;
}

export function chooseTier(e: Env): Tier {
  if (!e.webgl || e.reducedMotion || e.saveData) return "off";
  if (e.width < 640) return "low";
  if (e.coarsePointer && e.width < 1024) return "low";
  if (e.cores <= 4 || e.memoryGb <= 4) return "low";
  return "high";
}

export interface TierSettings {
  dpr: [number, number];
  antialias: boolean;
  pointer: boolean;
  /** Background particle count. */
  particles: number;
  /** Segment count for round geometry. */
  segments: number;
}

export const tierSettings: Record<Exclude<Tier, "off">, TierSettings> = {
  low: { dpr: [1, 1.5], antialias: false, pointer: false, particles: 60, segments: 12 },
  high: { dpr: [1, 2], antialias: true, pointer: true, particles: 220, segments: 32 },
};

export const downgrade = (t: Tier): Tier => (t === "high" ? "low" : "off");

/** Frame-rate probe: below this average the tier is lowered. */
export const MIN_FPS = 28;

export function isTooSlow(frames: number, seconds: number): boolean {
  if (seconds <= 0) return false;
  return frames / seconds < MIN_FPS;
}
