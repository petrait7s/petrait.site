import { defineConfig } from "astro/config";
import tailwindcss from "@tailwindcss/vite";
import react from "@astrojs/react";

const site = (process.env.PUBLIC_SITE_URL || "http://localhost:4321").replace(/\/+$/, "");

if (!process.env.PUBLIC_SITE_URL && process.argv.includes("build")) {
  console.warn(
    "\n[petra] PUBLIC_SITE_URL is not set: canonical URLs, sitemap and Open Graph will use " + site + ".\n" +
      "        Production deploys must run `npm run verify:prod` first (see .env.example).\n",
  );
}

export default defineConfig({
  site,
  output: "static",
  integrations: [react()],
  vite: { plugins: [tailwindcss()] },
});
