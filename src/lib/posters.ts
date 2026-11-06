import type { ImageMetadata } from "astro";

const posters = import.meta.glob<{ default: ImageMetadata }>("../assets/posters/*.webp", { eager: true });

/** Pre-rendered poster for a 3D scene (see scripts/posters.py). Undefined until it has been generated. */
export function posterFor(scene: string): ImageMetadata | undefined {
  return posters[`../assets/posters/${scene}.webp`]?.default;
}
