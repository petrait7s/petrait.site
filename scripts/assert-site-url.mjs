// Run before a production build: `npm run verify:prod && npm run build`.
const url = process.env.PUBLIC_SITE_URL;
if (!url) {
  console.error("PUBLIC_SITE_URL is not set. Refusing to build for production with localhost canonical URLs.");
  process.exit(1);
}
if (!/^https:\/\/[^/\s]+/.test(url) || /localhost|127\.0\.0\.1/.test(url)) {
  console.error(`PUBLIC_SITE_URL must be a public https URL, got: ${url}`);
  process.exit(1);
}
console.log(`PUBLIC_SITE_URL ok: ${url}`);
