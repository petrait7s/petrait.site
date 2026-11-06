# Architecture (summary)

Astro 5 static site, Tailwind v4 tokens in `src/styles/global.css`, typed content in `src/content/data/*.json`
validated by `src/content/schemas.ts`. The full plan is in `PETRA_ARCHITECTURE_PROPOSAL.md`.

- `npm run check`: typecheck, lint, unit tests, build (also run in CI).
- `npm run verify:prod && npm run build`: production build; fails if `PUBLIC_SITE_URL` is missing or not public https.
- Honesty rule: product and link `status` values live in the JSON files; tests fail if a product is marked
  `available` or an integration link is not `planned`. Change them only when a release really ships.
