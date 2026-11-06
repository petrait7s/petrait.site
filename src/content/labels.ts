/** Label under product screenshots. Use `live` only for captures of the real, running product. */
export const screenLabel = {
  illustrative: { tag: "Product preview", note: (n: string) => `Interface shown for demonstration. ${n} screens use sample data.` },
  prototype: { tag: "Product preview", note: (n: string) => `Captured from the ${n} interface prototype. Sample data.` },
  live: { tag: "Live product", note: (n: string) => `Captured from ${n}.` },
} as const;
