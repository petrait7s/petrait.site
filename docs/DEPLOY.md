# Going live

The site is static: any static host works (Vercel, Netlify, Cloudflare Pages, GitHub Pages, or your own server).

## 1. Build settings
| Setting | Value |
|---|---|
| Install command | `npm ci` |
| Build command | `npm run verify:prod && npm run build` |
| Output directory | `dist` |
| Node version | 20.9 or newer (22 recommended) |

`verify:prod` stops the build if `PUBLIC_SITE_URL` is missing, not https, or points to localhost, so the site can never ship with wrong canonical, sitemap or share URLs. Both variables below are read at **build time**: set them in the host's build environment, then rebuild after changing them.

## 2. Environment variables
| Variable | Required | What it does |
|---|---|---|
| `PUBLIC_SITE_URL` | yes | Final public address, for example `https://www.petra-bd.com` (no trailing slash). Used for canonical links, sitemap, robots.txt, share image and structured data. |
| `PUBLIC_INQUIRY_ENDPOINT` | strongly recommended | URL that receives the demo form as a JSON POST. Without it the form only opens a pre-filled email. |

`verify:prod` warns when `PUBLIC_INQUIRY_ENDPOINT` is empty. Set `REQUIRE_FORM_ENDPOINT=1` to make that a hard failure.

## 3. Make the demo form deliver to petraitbd@gmail.com
Simplest option, no code: create a free form at [Formspree](https://formspree.io), set its notification email to `petraitbd@gmail.com`, copy the form URL (looks like `https://formspree.io/f/xxxxxxxx`) and use it as `PUBLIC_INQUIRY_ENDPOINT`. Any service that accepts a JSON POST and emails or stores it will also work.

The form sends: `ref`, `_subject`, `source`, `name`, `email`, `phone`, `company`, `businessType`, `interests`, `message`, `callDate`. The visitor gets a reference like `INQ-261106-ABCD`, which is also in the email subject.

Behaviour you can rely on:
- Nothing is lost silently. If the service is down or the network fails, the visitor sees "Not sent yet" and a button that opens an email to the company with every field filled in.
- Bots: a hidden honeypot field and a minimum fill time are checked in the browser, and your form service should add its own spam filter and rate limit.
- After going live, send a real test request and confirm it arrives.

## 4. Security headers
`public/_headers` (Netlify, Cloudflare Pages) and `vercel.json` (Vercel) already set `X-Content-Type-Options`, `Referrer-Policy`, `X-Frame-Options`, `Permissions-Policy`, HSTS and long cache for built assets. On GitHub Pages or a plain server, add the same headers in the host or web server config. Optional later: a Content-Security-Policy (the site has no third-party scripts, but the form endpoint host must be allowed in `connect-src`).

## 5. Pre-launch checklist
- [ ] `PUBLIC_SITE_URL` set to the real https address; `view-source` shows it in `<link rel="canonical">`
- [ ] `PUBLIC_INQUIRY_ENDPOINT` set; a real test request arrived at petraitbd@gmail.com
- [ ] `https://your-domain/robots.txt` and `/sitemap-index.xml` open and show the real domain
- [ ] Share the home page in Facebook or WhatsApp and check the preview image and text
- [ ] Open the site on a real phone: menu, form, links, `tel:` and Facebook buttons
- [ ] HTTPS works and `http://` redirects to `https://`; HSTS header present
- [ ] Confirm the facts on the site with the owner: Marketing and Enterprise are described as "scope agreed per project"; product status labels (all `preview`); three months of bug-fix support; email, phone and Facebook link
- [ ] Have the privacy notice (`/privacy`) reviewed by someone qualified
- [ ] Submit the sitemap in Google Search Console

## 6. Known: dependency advisories
`npm audit` reports advisories against Astro 5.x and its build tools. This site is static: no server, no server islands, no MDX or JSX, no user input rendered at build time, and images are our own WebP files, so the reported issues (mostly server-rendering and dev-server problems) do not apply to the deployed files. The fix is Astro 7.4 or newer, which needs Node 22.23.4 or newer; upgrade when your host and CI use that Node version, then run `npm run check` and the pre-launch checklist again.

## 7. Updating later
Edit the content files (see README), run `npm run check`, push; the host rebuilds. CI (`.github/workflows/ci.yml`) runs `npm run check` on every push and pull request.
