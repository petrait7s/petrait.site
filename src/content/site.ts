/** Site-wide constants. Confirm contact details with the owner before launch. */
export const site = {
  name: "PETRA",
  legalName: "PETRA Software Solutions",
  tagline: "Built on trust.",
  description:
    "PETRA Software Solutions builds software in Bangladesh: products for hospitality and business, and custom software of any type built to client demand. Built on trust.",
  email: "petrabd@gmail.com",
  phone: "016-16154320",
  phoneHref: "+8801616154320",
  facebook: "https://www.facebook.com/share/1DsiFUJeNB/",
  instagram: "https://www.instagram.com/petraitbd",
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

