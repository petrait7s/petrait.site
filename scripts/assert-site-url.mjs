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

const endpoint = process.env.PUBLIC_INQUIRY_ENDPOINT;
if (!endpoint) {
  console.warn(
    "\nWARNING: PUBLIC_INQUIRY_ENDPOINT is not set. The demo form will only open a pre-filled email instead of sending the request.\n" +
      "         Set it to your form service URL (see docs/DEPLOY.md) before you go live.\n",
  );
  if (process.env.REQUIRE_FORM_ENDPOINT === "1") process.exit(1);
} else if (!/^https:\/\//.test(endpoint)) {
  console.error(`PUBLIC_INQUIRY_ENDPOINT must be an https URL, got: ${endpoint}`);
  process.exit(1);
} else {
  console.log("PUBLIC_INQUIRY_ENDPOINT ok");
}
