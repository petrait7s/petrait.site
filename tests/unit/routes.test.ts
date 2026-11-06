import { existsSync, readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { footerLinks, nav } from "../../src/content/site";

const hrefs = [...nav, ...footerLinks.products, ...footerLinks.company, ...footerLinks.legal, { href: "/contact" }].map((l) => l.href);

const productIds: string[] = JSON.parse(readFileSync("src/content/data/products.json", "utf8")).map((p: { id: string }) => p.id);

/** A route exists if it has its own page file or is a generated product page. */
const exists = (href: string) => {
  const slug = href.replace(/^\//, "");
  if (slug.startsWith("products/")) return productIds.includes(slug.slice("products/".length)) && existsSync("src/pages/products/[slug].astro");
  if (slug === "") return existsSync("src/pages/index.astro");
  return existsSync(`src/pages/${slug}.astro`) || existsSync(`src/pages/${slug}/index.astro`);
};

describe("navigation", () => {
  it.each([...new Set(hrefs)])("%s resolves to a page", (href) => {
    expect(exists(href)).toBe(true);
  });
});
