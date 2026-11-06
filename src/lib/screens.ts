import type { ImageMetadata } from "astro";

const images = import.meta.glob<{ default: ImageMetadata }>("../assets/products/*.webp", { eager: true });

export type ScreenKind = "desktop" | "mobile";

/** Resolve a captured product screenshot (see scripts/capture.py). Throws at build time if missing. */
export function screenImage(prefix: string, view: string, kind: ScreenKind): ImageMetadata {
  const found = images[`../assets/products/${prefix}-${view}-${kind}.webp`];
  if (!found) throw new Error(`Missing screenshot: ${prefix}-${view}-${kind}.webp`);
  return found.default;
}
