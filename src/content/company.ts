/** Static company facts that are not repeated per item. Keep status labels honest. */
export const glance = [
  { title: "Built for real operations", text: "Reservations, folios, orders, stock and dues: the daily work of front desks, outlets and distributors." },
  { title: "Built in Bangladesh", text: "Designed, built and supported locally. Prices and amounts in BDT (৳)." },
  { title: "Local-first", text: "PetraPMS runs over the property's local network, with data on its own server." },
  { title: "Direct support", text: "One team builds, deploys and supports the software." },
] as const;

export const deployment = {
  tiers: [
    { n: "01", title: "Property / office", items: ["Front desk PCs", "Outlet terminals", "Back office"] },
    { n: "02", title: "Petra server", items: ["On your premises", "Local database"] },
    { n: "03", title: "Petra products", items: ["PMS", "POS", "DMS"] },
  ],
  traits: [
    { title: "Local network", text: "Terminals connect to the Petra server over the property LAN.", planned: false },
    { title: "Fast local response", text: "Requests stay inside the building instead of crossing the internet to a remote data centre.", planned: false },
    { title: "Centralised local data", text: "One database on the Petra server, stored on hardware you own.", planned: false },
    { title: "Windows installer", text: "PetraPMS packaged as a Windows installer for on-site setup.", planned: true },
    { title: "Larger deployments", text: "PostgreSQL for multi-property or cloud-hosted installations.", planned: true },
  ],
  note: "The model above is PetraPMS's design. Deployment for PetraPOS and PetraDMS, backups and remote access are agreed per project during Discover.",
} as const;

export const core = {
  name: "Petra Core",
  sub: "Shared data · sign-in · reports",
  role: "One data layer for all the products: shared customers and guests, one sign-in with roles, and reports across the business.",
  status: "planned",
} as const;

/** Modules PETRA builds for a client on request (in development now). Not off-the-shelf releases. */
export const requestModules = [
  { group: "Guest", name: "PetraBooking", role: "Direct booking engine", status: "onrequest" },
  { group: "Guest", name: "PetraTour", role: "Tours and packages", status: "onrequest" },
  { group: "Guest", name: "PetraCRM", role: "Guest relationships", status: "onrequest" },
  { group: "Operations", name: "PetraHouse", role: "Housekeeping and maintenance", status: "onrequest" },
  { group: "Operations", name: "PetraEvents", role: "Banquets and events", status: "onrequest" },
  { group: "Intelligence", name: "PetraChannel", role: "Channel connectivity", status: "onrequest" },
  { group: "Intelligence", name: "PetraRMS", role: "Revenue and pricing", status: "onrequest" },
  { group: "Intelligence", name: "PetraDMO", role: "Destination organization tools", status: "onrequest" },
] as const;

/**
 * The company story as a stack, bottom to top: trust first, then the four sectors.
 * Hospitality and Business list real products (all in preview). Marketing and Enterprise are
 * scoped per project: confirm the exact offering with the company before adding specifics.
 */
export const layers = [
  {
    id: "foundation",
    title: "Trust",
    line: "The base everything stands on.",
    items: [
      { label: "Local-first deployment" },
      { label: "One team builds, deploys and supports" },
      { label: "Three months of bug-fix support after go-live" },
      { label: "Honest status labels on every product" },
    ],
  },
  {
    id: "hospitality",
    title: "Hospitality",
    line: "Run hotels, resorts and restaurants.",
    items: [
      { label: "PetraPMS", href: "/products/petrapms", status: "preview" },
      { label: "PetraPOS", href: "/products/petrapos", status: "preview" },
      { label: "PetraDMS", href: "/products/petradms", status: "preview" },
    ],
  },
  {
    id: "business",
    title: "Business",
    line: "Websites and online stores that work for you.",
    items: [
      { label: "Website Build", href: "/products/website-build", status: "preview" },
      { label: "E-commerce Build", href: "/products/ecommerce-build", status: "preview" },
    ],
  },
  {
    id: "marketing",
    title: "Marketing",
    line: "Reach customers and tell your story.",
    items: [{ label: "Scope agreed per project", href: "/contact" }],
  },
  {
    id: "enterprise",
    title: "Enterprise",
    line: "Larger organisations with their own requirements.",
    items: [{ label: "Scope agreed per project", href: "/contact" }],
  },
] as const;

/** What "built on trust" means in practice. Only facts the company can stand behind. */
export const trustPrinciples = [
  { title: "Honest by default", text: "Every product, module and integration carries an honest status: available, preview, built on request or planned. We never show a feature as live before it is." },
  { title: "Your data stays yours", text: "PetraPMS is designed to run on the property's own network, with its database on a server you control." },
  { title: "One accountable team", text: "The people who build the software also deploy and support it. No hand-offs, no ticket maze." },
  { title: "Support after go-live", text: "Staff training at handover, then three months of bug-fix support." },
] as const;
