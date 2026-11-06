import type { Env } from "./tier";

function hasWebGL(): boolean {
  try {
    const canvas = document.createElement("canvas");
    return Boolean(canvas.getContext("webgl2") || canvas.getContext("webgl"));
  } catch {
    return false;
  }
}

/** Read the visitor's environment. Browser only. */
export function detectEnv(): Env {
  const nav = navigator as Navigator & { deviceMemory?: number; connection?: { saveData?: boolean } };
  return {
    width: window.innerWidth,
    reducedMotion: window.matchMedia("(prefers-reduced-motion: reduce)").matches,
    saveData: Boolean(nav.connection?.saveData),
    webgl: hasWebGL(),
    cores: nav.hardwareConcurrency || 8,
    memoryGb: nav.deviceMemory ?? 8,
    coarsePointer: window.matchMedia("(pointer: coarse)").matches,
  };
}
