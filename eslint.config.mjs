import js from "@eslint/js";
import tseslint from "typescript-eslint";
import astro from "eslint-plugin-astro";

const nodeGlobals = { process: "readonly", console: "readonly" };
const browserGlobals = { document: "readonly", location: "readonly" };

export default [
  { ignores: ["dist/", "node_modules/", ".astro/"] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...astro.configs.recommended,
  { files: ["astro.config.mjs", "scripts/**/*.mjs"], languageOptions: { globals: nodeGlobals } },
  { files: ["mockups/**/*.js"], languageOptions: { globals: browserGlobals } },
];
