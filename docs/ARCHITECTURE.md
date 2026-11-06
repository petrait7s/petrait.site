# Architecture

Astro 5 static site. Content is typed data, pages are Astro components, interactivity is a few small scripts (no UI framework).

```
src/
  pages/            index, products/index, products/[slug], ecosystem, deployment, industries,
                    why-petra, implementation, contact, privacy, 404, 500, robots.txt.ts
  layouts/          BaseLayout: head (meta, Open Graph, JSON-LD), skip link, navbar, footer, view transitions
  components/
    layout/         Navbar (accessible mobile menu), Footer, Logo
    sections/       Hero, Glance, Sectors, ProductCards, Trust, Ecosystem, Deployment, Industries, Why, Steps, CtaBlock, PageHero
    ui/             Aurora (animated background), Button, Chip, SectionHead, DeviceFrame, Showcase (tabs), FacebookLink, InquiryForm
  content/          site.ts, company.ts, labels.ts, schemas.ts (zod), data/*.json (Astro content collections)
  lib/              inquiry.ts (validation, reference, mailto), screens.ts (screenshot lookup)
  scripts/fx.ts     scroll reveal, card spotlight, aurora pause when off screen
  assets/products/  sample interface screenshots (optimised by astro:assets)
public/             brand logos, og.png, _headers
mockups/            HTML sources of the screenshots and og.png
scripts/            capture.py, og.py (image generation), assert-site-url.mjs (production guard)
tests/unit/         content honesty rules, routes, form logic
```

Data flow: `content/data/*.json` (validated by `schemas.ts`) → pages → HTML. The only runtime code is the navbar menu, the product tabs, the reveal/spotlight/aurora helpers and the demo form, all progressive: content is visible without JavaScript and with reduced motion.

Decisions: static output (cheap, fast, any host); no cookies or analytics; form posts to an external endpoint set at build time, with an email fallback so no request is lost silently; honest status labels enforced by tests.
