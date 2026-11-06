import { existsSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { footerLinks, nav, placeholderPages } from "../../src/content/site";

const hrefs = [...nav, ...footerLinks.products, ...footerLinks.company, ...footerLinks.legal, { href: "/contact" }].map((l) => l.href);

/** A route exists if it has its own page file or a placeholder entry. */
const exists = (href: string) => {
  const slug = href.replace(/^\//, "");
  if (slug === "") return existsSync("src/pages/index.astro");
  return existsSync(`src/pages/${slug}.astro`) || existsSync(`src/pages/${slug}/index.astro`) || slug in placeholderPages;
};

describe("navigation", () => {
  it.each([...new Set(hrefs)])("%s resolves to a page", (href) => {
    expect(exists(href)).toBe(true);
  });
});
