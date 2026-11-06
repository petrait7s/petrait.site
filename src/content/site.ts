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
