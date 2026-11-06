import { defineCollection } from "astro:content";
import { file } from "astro/loaders";
import { industrySchema, linkSchema, productSchema, reasonSchema, stepSchema } from "./content/schemas";

const data = (name: string) => `./src/content/data/${name}.json`;

export const collections = {
  products: defineCollection({ loader: file(data("products")), schema: productSchema }),
  links: defineCollection({ loader: file(data("links")), schema: linkSchema }),
  industries: defineCollection({ loader: file(data("industries")), schema: industrySchema }),
  reasons: defineCollection({ loader: file(data("reasons")), schema: reasonSchema }),
  steps: defineCollection({ loader: file(data("steps")), schema: stepSchema }),
};
