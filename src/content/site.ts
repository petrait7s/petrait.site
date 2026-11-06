/** Site-wide constants. Confirm contact details with the owner before launch. */
export const site = {
  name: "PETRA",
  legalName: "PETRA Software Solutions",
  tagline: "Software that runs hospitality.",
  description:
    "PETRA builds hospitality software in Bangladesh: PetraPMS for hotel property management, PetraPOS for restaurant and outlet point of sale, and PetraDMS for distribution management.",
  email: "petrabd@gmail.com",
  phone: "016-16154320",
  phoneHref: "+8801616154320",
  facebook: "https://www.facebook.com/share/1DsiFUJeNB/",
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
    { label: "PetraPMS", href: "/products/petrapms" },
    { label: "PetraPOS", href: "/products/petrapos" },
    { label: "PetraDMS", href: "/products/petradms" },
    { label: "Website Build", href: "/products/website-build" },
    { label: "E-commerce Build", href: "/products/ecommerce-build" },
  ],
  company: [
    { label: "Why Petra", href: "/why-petra" },
    { label: "Industries", href: "/industries" },
    { label: "Implementation", href: "/implementation" },
    { label: "Deployment", href: "/deployment" },
  ],
  legal: [{ label: "Privacy", href: "/privacy" }],
} as const;

/** Routes served by the temporary placeholder page until their real pages land. */
export const placeholderPages: Record<string, { title: string; note: string }> = {
  privacy: { title: "Privacy notice", note: "The privacy notice arrives together with the demo request form." },
};
