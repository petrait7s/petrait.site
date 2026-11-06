# PETRA Software Solutions: website

Built on trust. Static marketing site for PETRA (hospitality, business, marketing and enterprise software, Bangladesh).

**Stack:** Astro 5 (static output) · Tailwind CSS v4 · TypeScript · Vitest. No UI framework, no 3D, no third-party scripts, no cookies.

```bash
npm install
cp .env.example .env     # optional for local work
npm run dev              # http://localhost:4321
npm run check            # typecheck + lint + unit tests + production build (also run in CI)
npm run preview          # serve the production build
```

Node.js 20.9 or newer.

## Pages
`/` · `/products` · `/products/<petrapms|petrapos|petradms|website-build|ecommerce-build>` · `/ecosystem` · `/deployment` · `/industries` · `/why-petra` · `/implementation` · `/contact` (demo form) · `/privacy` · `/404`

## Where to edit
| What | File |
|---|---|
| Company name, email, phone, Facebook link | `src/content/site.ts` |
| Products, features, status (`preview`, `onrequest`, `available`) | `src/content/data/products.json` |
| Ecosystem links, industries, reasons, process steps | `src/content/data/*.json` |
| Sectors (Hospitality, Business, Marketing, Enterprise), trust principles, deployment text | `src/content/company.ts` |
| Colours and fonts | `src/styles/global.css` (`@theme`) |
| Demo form fields and validation | `src/lib/inquiry.ts`, `src/components/ui/InquiryForm.astro` |

Brand colours come from the logo: navy `#0c1d35`, teal `#038d91`, tint `#e6e9ef`.

## Honesty rules (enforced by tests)
Every product, module and connection carries a status: `available`, `preview` or `onrequest` (built for a client when needed, and in development now). No product may be marked `available`, and every connection and module must be `onrequest`, until a release really ships (`tests/unit/content.test.ts`). Nothing is labelled "planned". Change a status only when it is true.

## Images
- `src/assets/products/*.webp`: sample interface screenshots (desktop 1440x900 and iPhone 16 393x852). Regenerate with `python3 scripts/capture.py` from the HTML in `mockups/` (needs `pip install playwright pillow`).
- `public/og.png`: share image, regenerate with `python3 scripts/og.py`.
- Replace the samples with real captures when the products ship, and set `screenSource` to `live` in `products.json`.

## Going live
See [`docs/DEPLOY.md`](docs/DEPLOY.md): environment variables, form service, host settings and the pre-launch checklist.
