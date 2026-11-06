import { existsSync, readdirSync, readFileSync } from "node:fs";
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

  it("every ecosystem link is built on request (integrations do not ship yet)", () => {
    for (const l of load("links")) expect(l.status).toBe("onrequest");
  });

  it("ids are unique within each collection", () => {
    for (const name of ["products", "links", "industries", "reasons", "steps"]) {
      const ids = load(name).map((x: { id: string }) => x.id);
      expect(new Set(ids).size).toBe(ids.length);
    }
  });
});

describe("product screens", () => {
  it("every declared screen has a sample page with that view, and a desktop and a mobile poster", () => {
    for (const p of load("products")) {
      for (const s of p.screens) {
        const html = `public/demo/${s.page}.html`;
        expect(existsSync(html), html).toBe(true);
        expect(readFileSync(html, "utf8"), `${s.page} has view ${s.view}`).toContain(`data-v="${s.view}"`);
        for (const kind of ["desktop", "mobile"]) {
          const file = `src/assets/products/${s.page}-${s.view}-${kind}.webp`;
          expect(existsSync(file), file).toBe(true);
        }
      }
    }
  });
  it("every sample page is noindex and says it is sample data", () => {
    for (const f of readdirSync("public/demo").filter((n) => n.endsWith(".html"))) {
      const html = readFileSync(`public/demo/${f}`, "utf8");
      expect(html, f).toContain('name="robots" content="noindex"');
      expect(html, f).toMatch(/SAMPLE (DATA|WEBSITE)/);
    }
  });
  it("PetraPMS, PetraPOS and PetraDMS each have their own look", () => {
    const theme = (f: string) => readFileSync(`public/demo/${f}.html`, "utf8").match(/<body class="([^"]+)"/)![1];
    const themes = ["petrapms", "petrapos", "petradms"].map(theme);
    expect(new Set(themes).size).toBe(3);
  });
  it("the word iPhone never appears on the site or in the sample pages", () => {
    const walk = (dir: string): string[] => readdirSync(dir, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? walk(`${dir}/${e.name}`) : [`${dir}/${e.name}`]));
    for (const f of [...walk("src").filter((n) => /\.(astro|ts|json)$/.test(n)), ...walk("public/demo").filter((n) => /\.(html|css|js)$/.test(n)), "README.md", "docs/DEPLOY.md", "docs/ARCHITECTURE.md"]) {
      expect(readFileSync(f, "utf8"), f).not.toMatch(/iphone/i);
    }
  });
  it("the host headers allow the site to frame its own sample pages", () => {
    expect(readFileSync("public/_headers", "utf8")).toContain("X-Frame-Options: SAMEORIGIN");
    expect(readFileSync("vercel.json", "utf8")).toContain('"SAMEORIGIN"');
  });
});

describe("contact details", () => {
  const site = readFileSync("src/content/site.ts", "utf8");
  it("uses the current company contact details", () => {
    expect(site).toContain('email: "petrabd@gmail.com"');
    expect(site).toContain('phone: "016-16154320"');
    expect(site).toContain('phoneHref: "+8801616154320"');
    expect(site).toContain('facebook: "https://www.facebook.com/share/1DsiFUJeNB/"');
  });
  it("does not leave the old contact details anywhere in the source", () => {
    expect(site).not.toContain("letterbox5509");
    expect(site).not.toContain("01609347600");
  });
});

describe("company story", () => {
  const src = readFileSync("src/content/company.ts", "utf8");
  it("lists trust first, then the four sectors, in order", () => {
    const ids = [...src.matchAll(/^ {4}id: "(\w+)",$/gm)].map((m) => m[1]);
    expect(ids).toEqual(["foundation", "hospitality", "business", "marketing", "enterprise"]);
  });
  it("only links to product pages that exist", () => {
    const productIds = load("products").map((p: { id: string }) => p.id);
    for (const m of src.matchAll(/href: "\/products\/([\w-]+)"/g)) expect(productIds).toContain(m[1]);
  });
});

describe("ecosystem diagram data", () => {
  const modules = readFileSync("src/content/company.ts", "utf8");
  const productCodes = load("products").map((p: { code: string }) => p.code.toLowerCase());
  it("connects every product to the core, and nothing else is claimed as live", () => {
    const toCore = load("links").filter((l: { to: string }) => l.to === "core").map((l: { from: string }) => l.from);
    for (const code of productCodes) expect(toCore).toContain(code);
    for (const l of load("links")) expect(l.status).toBe("onrequest");
  });
  it("lists the eight modules built on request, none of them a current product name", () => {
    const names = [...modules.matchAll(/name: "(Petra\w+)", role:/g)].map((m) => m[1]);
    expect(names).toEqual(["PetraBooking", "PetraTour", "PetraCRM", "PetraHouse", "PetraEvents", "PetraChannel", "PetraRMS", "PetraDMO"]);
    expect([...modules.matchAll(/status: "onrequest" \}/g)].length).toBe(8);
    const productNames = load("products").map((p: { name: string }) => p.name);
    for (const n of names) expect(productNames).not.toContain(n);
  });
});

describe("custom software positioning", () => {
  const company = readFileSync("src/content/company.ts", "utf8");
  it("states that any type of software is built on client demand", () => {
    expect(company).toContain("export const customBuild");
    expect(company).toContain("Any kind of software, to your requirement");
  });
  it("offers custom software as a form interest and keeps the sector list at four", () => {
    expect(readFileSync("src/lib/inquiry.ts", "utf8")).toContain('"Custom software"');
    const ids = [...company.matchAll(/^ {4}id: "(\w+)",$/gm)].map((m) => m[1]);
    expect(ids).toHaveLength(5);
  });
});

describe("status wording", () => {
  it("never labels anything as planned", () => {
    const files = ["src/content/company.ts", "src/content/schemas.ts", "src/components/ui/Chip.astro", "src/components/sections/Ecosystem.astro", "src/components/sections/Deployment.astro", "src/pages/ecosystem.astro", "src/pages/products/[slug].astro"];
    for (const f of [...files, "src/content/data/links.json", "src/content/data/products.json", "src/content/data/reasons.json"]) {
      expect(readFileSync(f, "utf8"), f).not.toMatch(/planned/i);
    }
  });
});
