import { existsSync, readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import { industrySchema, linkSchema, productSchema, reasonSchema, stepSchema } from "../../src/content/schemas";
import { z } from "astro/zod";

const load = (name: string) => JSON.parse(readFileSync(`src/content/data/${name}.json`, "utf8"));

describe("content validates against its schema", () => {
  it.each([
    ["products", productSchema],
    ["links", linkSchema],
    ["industries", industrySchema],
    ["reasons", reasonSchema],
    ["steps", stepSchema],
  ] as const)("%s", (name, schema) => {
    expect(() => z.array(schema).parse(load(name))).not.toThrow();
  });
});

describe("honesty rules", () => {
  it("no product is marked available until a release is confirmed", () => {
    for (const p of load("products")) expect(p.status).not.toBe("available");
  });

  it("every ecosystem link is planned (integrations do not ship yet)", () => {
    for (const l of load("links")) expect(l.status).toBe("planned");
  });

  it("ids are unique within each collection", () => {
    for (const name of ["products", "links", "industries", "reasons", "steps"]) {
      const ids = load(name).map((x: { id: string }) => x.id);
      expect(new Set(ids).size).toBe(ids.length);
    }
  });
});

describe("product screenshots", () => {
  it("every declared screen has a desktop and a mobile image", () => {
    for (const p of load("products")) {
      for (const s of p.screens) {
        for (const kind of ["desktop", "mobile"]) {
          const file = `src/assets/products/${p.assetPrefix}-${s.view}-${kind}.webp`;
          expect(existsSync(file), file).toBe(true);
        }
      }
    }
  });
});
