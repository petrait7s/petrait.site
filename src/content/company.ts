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
  role: "One data layer for the three products: shared customers and guests, one sign-in with roles, and reports across the business.",
  status: "planned",
} as const;

/** Modules from the Petra roadmap. None of these are built yet. */
export const plannedModules = [
  { group: "Guest", name: "PetraBooking", role: "Direct booking engine" },
  { group: "Guest", name: "PetraTour", role: "Tours and packages" },
  { group: "Guest", name: "PetraCRM", role: "Guest relationships" },
  { group: "Operations", name: "PetraHouse", role: "Housekeeping and maintenance" },
  { group: "Operations", name: "PetraEvents", role: "Banquets and events" },
  { group: "Intelligence", name: "PetraChannel", role: "Channel connectivity" },
  { group: "Intelligence", name: "PetraRMS", role: "Revenue and pricing" },
  { group: "Intelligence", name: "PetraDMO", role: "Destination organization tools" },
] as const;
