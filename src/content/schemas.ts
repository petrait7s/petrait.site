import { z } from "astro/zod";

/**
 * Release status. Drives every status chip. Keep it honest.
 * onrequest: built for a client when they need it (and in development now); not an off-the-shelf release.
 */
export const status = z.enum(["available", "preview", "planned", "onrequest"]);
export type Status = z.infer<typeof status>;

export const screenSource = z.enum(["illustrative", "prototype", "live"]);

export const productSchema = z.object({
  id: z.string(),
  code: z.enum(["PMS", "POS", "DMS", "WEB", "SHOP"]),
  name: z.string(),
  full: z.string(),
  category: z.string(),
  status,
  statusNote: z.string(),
  problem: z.string(),
  description: z.string(),
  features: z.array(z.object({ title: z.string(), planned: z.boolean().default(false) })),
  workflow: z.array(z.string()),
  screenSource,
  /** Files in src/assets/products are named `<assetPrefix>-<view>-desktop.webp` and `-mobile.webp`. */
  assetPrefix: z.string(),
  screens: z.array(z.object({ view: z.string(), label: z.string(), alt: z.string() })).min(1),
});

export const linkSchema = z.object({
  id: z.string(),
  from: z.string(),
  to: z.string(),
  label: z.string(),
  detail: z.string(),
  status,
});

export const industrySchema = z.object({
  id: z.string(),
  name: z.string(),
  line: z.string(),
  products: z.array(z.enum(["PMS", "POS", "DMS", "WEB", "SHOP"])),
  /** A PETRA module built on request for this industry. */
  module: z.string().optional(),
});

export const reasonSchema = z.object({ id: z.string(), title: z.string(), text: z.string() });

export const stepSchema = z.object({ id: z.string(), n: z.string(), title: z.string(), line: z.string(), detail: z.string() });
