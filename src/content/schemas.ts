import { z } from "astro/zod";

/**
 * Release status. Drives every status chip. Keep it honest.
 * onrequest: built for a client when they need it (and in development now); not an off-the-shelf release.
 */
export const status = z.enum(["available", "preview", "onrequest"]);
export type Status = z.infer<typeof status>;

export const screenSource = z.enum(["illustrative", "prototype", "live"]);

export const productSchema = z.object({
  id: z.string(),
  code: z.enum(["PMS", "POS", "DMS", "WEB", "SHOP"]),
  name: z.string(),
  full: z.string(),
  /** Two or three words, for tight spaces such as the ecosystem diagram. */
  short: z.string(),
  category: z.string(),
  status,
  statusNote: z.string(),
  problem: z.string(),
  description: z.string(),
  features: z.array(z.object({ title: z.string(), onRequest: z.boolean().default(false) })),
  workflow: z.array(z.string()),
  screenSource,
  /** `page` is a file in public/demo (page.html), `view` a data-v section in it. Posters: src/assets/products/<page>-<view>-desktop|mobile.webp */
  screens: z.array(z.object({ page: z.string(), view: z.string(), label: z.string(), alt: z.string() })).min(1),
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
