/** Site-wide constants. Confirm contact details with the owner before launch. */
export const site = {
  name: "PETRA",
  legalName: "PETRA Software Solutions",
  tagline: "Software that runs hospitality.",
  description:
    "PETRA builds hospitality software in Bangladesh: PetraPMS for hotel property management, PetraPOS for restaurant and outlet point of sale, and PetraDMS for distribution management.",
  email: "letterbox5509@gmail.com",
  phone: "01609347600",
  phoneHref: "+8801609347600",
  country: "Bangladesh",
} as const;

export const nav = [
  { label: "Products", href: "/products" },
  { label: "Ecosystem", href: "/ecosystem" },
  { label: "Deployment", href: "/deployment" },
  { label: "Industries", href: "/industries" },
  { label: "Contact", href: "/contact" },
] as const;

export const footerLinks = {
  products: [
    { label: "PetraPMS", href: "/products" },
    { label: "PetraPOS", href: "/products" },
    { label: "PetraDMS", href: "/products" },
  ],
  company: [
    { label: "Why Petra", href: "/why-petra" },
    { label: "Industries", href: "/industries" },
    { label: "Implementation", href: "/implementation" },
    { label: "Deployment", href: "/deployment" },
  ],
  legal: [{ label: "Privacy", href: "/privacy" }],
} as const;

/** Routes served by the temporary placeholder page until their real pages land (Phase 3+). */
export const placeholderPages: Record<string, { title: string; note: string }> = {
  products: { title: "Products", note: "PetraPMS, PetraPOS and PetraDMS detail pages arrive in Phase 3." },
  ecosystem: { title: "Ecosystem", note: "The Petra Core and planned integrations page arrives in Phase 3." },
  deployment: { title: "Deployment", note: "The local-first deployment page arrives in Phase 3." },
  industries: { title: "Industries", note: "The industries page arrives in Phase 3." },
  "why-petra": { title: "Why Petra", note: "This page arrives in Phase 3." },
  implementation: { title: "Implementation", note: "This page arrives in Phase 3." },
  contact: { title: "Contact", note: "The demo request form arrives in Phase 6. Until then, email or call us." },
  privacy: { title: "Privacy notice", note: "The privacy notice arrives with the demo form in Phase 6." },
};
