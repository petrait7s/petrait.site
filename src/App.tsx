import { useEffect, type ReactNode } from "react";

const SITE = {
  email: "letterbox5509@gmail.com",
  phone: "01609347600",
  phoneHref: "+8801609347600",
};

const NAV = [
  { label: "Products", href: "#products" },
  { label: "Deployment", href: "#deployment" },
  { label: "Industries", href: "#industries" },
  { label: "Contact", href: "#contact" },
];

const GLANCE = [
  { title: "Built for real operations", text: "Reservations, folios, orders, stock and dues." },
  { title: "Built in Bangladesh", text: "Designed and supported locally. Amounts in BDT (৳)." },
  { title: "Local-first", text: "PetraPMS runs over the property's own network." },
  { title: "Direct support", text: "One team builds, deploys and supports." },
];

const PRODUCTS = [
  {
    name: "PetraPMS",
    full: "Property Management System",
    image: "Dashboard screenshot",
    text: "Reservations, guest records, room inventory, housekeeping status, billing, check-in and check-out.",
    features: ["Reservations & front desk", "Room inventory & status", "Guest folios & billing", "Runs on the hotel LAN"],
  },
  {
    name: "PetraPOS",
    full: "Point of Sale System",
    image: "Terminal screenshot",
    text: "Restaurants, cafés and room service: orders, kitchen tickets, billing, stock control and sales reports.",
    features: ["Table & counter orders", "Kitchen tickets", "Billing & payments", "Room charge to PetraPMS (planned)"],
  },
  {
    name: "PetraDMS",
    full: "Distribution Management System",
    image: "Reports screenshot",
    text: "Sales and invoicing, purchasing, multi-unit stock, customer and supplier ledgers, expenses and reports.",
    features: ["Invoicing with due tracking", "Big box · small box · piece stock", "Customer & supplier ledgers", "Compact mode with calculator"],
  },
];

const LINKS = [
  { label: "Guest charges", text: "POS bills posted to the guest's room folio." },
  { label: "Inventory", text: "Stock received through distribution available to outlets." },
  { label: "Petra Core", text: "Shared data, one sign-in with roles, reports across the business." },
];

const DEPLOY = [
  { n: "01", title: "Property / office", text: "Front desk PCs, outlet terminals and back office." },
  { n: "02", title: "Petra server", text: "On your premises, with a local database." },
  { n: "03", title: "Petra products", text: "PMS, POS and DMS served over the local network." },
];

const INDUSTRIES = [
  { name: "Hotels", text: "Front desk, rooms and billing, with POS for the restaurant.", tag: "PMS · POS" },
  { name: "Resorts", text: "Rooms plus several food and beverage outlets.", tag: "PMS · POS" },
  { name: "Restaurants", text: "Tables, kitchen tickets and payments.", tag: "POS" },
  { name: "Tour operators", text: "Supplier and partner ledgers with dues.", tag: "DMS", planned: "PetraTour planned" },
  { name: "DMOs", text: "Tools for destination organizations.", tag: "", planned: "PetraDMO planned", wide: true },
];

const WHY = [
  { title: "Built for hospitality workflows", text: "Reservations, room status, folios, orders and kitchen tickets are core screens, not add-ons to a generic ERP." },
  { title: "Bangladesh-focused", text: "Amounts in BDT (৳), cash and bKash as payment methods in PetraDMS." },
  { title: "Local deployment", text: "PetraPMS runs on the property's own network with its database on a server you control." },
  { title: "Connected by design", text: "Each works on its own today; integrations are labelled until they ship." },
  { title: "Direct support", text: "You speak to the people who build the software. Bug-fix support is included for three months after go-live." },
  { title: "Practical tools", text: "Three-unit stock, a compact mode with calculator, and dues on every invoice." },
];

const PROCESS = [
  { n: "01", title: "Discover", text: "A call or site visit to map rooms, outlets, users and the tools you use today." },
  { n: "02", title: "Configure", text: "Products, users, roles and settings prepared before go-live." },
  { n: "03", title: "Deploy", text: "Installed on your server and terminals, connected over the local network." },
  { n: "04", title: "Support", text: "Staff training at handover, then bug-fix support for three months after go-live." },
];

const navLink = "text-[12px] sm:text-[14px] font-medium text-gray-700 hover:text-gray-900 transition-colors duration-200";
const eyebrow = "text-[11.5px] font-medium text-blue-500 mb-3";
const h2 = "text-[1.5rem] sm:text-[1.75rem] leading-[1.15] font-medium tracking-tight";
const pad = "px-6 sm:px-12 md:px-20 lg:px-28";
const arrow = "inline-block transition-transform duration-200 group-hover:translate-x-0.5";

function Logo({ size = 18 }: { size?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 256 256" fill="none">
      <path
        fill="rgb(84, 84, 84)"
        d="M 160 88 L 194 34 L 216 0 L 256 0 L 256 40 L 221.5 93.5 L 200 128 L 256 128 L 256 256 L 96 256 L 96 168 L 64.246 220 L 40 256 L 0 256 L 0 216 L 34 162 L 56 128 L 0 128 L 0 0 L 160 0 Z"
      />
    </svg>
  );
}

function Chip({ children, dashed }: { children: ReactNode; dashed?: boolean }) {
  return (
    <span
      className={`shrink-0 text-[10.5px] font-medium rounded-full px-2 py-0.5 border ${
        dashed ? "border-dashed border-gray-400 text-gray-500" : "border-gray-400 text-gray-600"
      }`}
    >
      {children}
    </span>
  );
}

function Heading({ label, title, children }: { label: string; title: string; children?: ReactNode }) {
  return (
    <div className="reveal mb-10 sm:mb-14 max-w-md">
      <p className={eyebrow}>{label}</p>
      <h2 className={h2}>{title}</h2>
      {children}
    </div>
  );
}

function Steps({ items, cols }: { items: { n: string; title: string; text: string }[]; cols: string }) {
  return (
    <ol className={`grid gap-8 ${cols}`}>
      {items.map((s) => (
        <li key={s.n} className="reveal border-t border-gray-300 pt-5">
          <span className="text-[11.5px] font-medium text-blue-500">{s.n}</span>
          <h3 className="text-[15px] font-medium mt-2">{s.title}</h3>
          <p className="text-[13px] text-gray-500 mt-2">{s.text}</p>
        </li>
      ))}
    </ol>
  );
}

export default function App() {
  // Fade sections in as they scroll into view.
  useEffect(() => {
    const els = document.querySelectorAll<HTMLElement>(".reveal");
    if (!("IntersectionObserver" in window)) {
      els.forEach((el) => el.classList.add("in"));
      return;
    }
    const io = new IntersectionObserver(
      (entries) =>
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        }),
      { threshold: 0.15 },
    );
    els.forEach((el) => io.observe(el));
    return () => io.disconnect();
  }, []);

  return (
    <div className="bg-[#f0f0ee] text-gray-900 antialiased">
      {/* HERO */}
      <header className="relative min-h-screen overflow-hidden bg-[#f0f0ee]">
        <div
          className="absolute inset-0"
          style={{
            background:
              "radial-gradient(60% 55% at 78% 30%, #cfe0ff 0%, rgba(207,224,255,0) 70%), radial-gradient(50% 50% at 15% 85%, #e3e6ea 0%, rgba(227,230,234,0) 70%), #f0f0ee",
          }}
        />
        <div
          className="absolute inset-0 opacity-[0.35]"
          style={{
            backgroundImage:
              "linear-gradient(to right, rgba(0,0,0,.05) 1px, transparent 1px), linear-gradient(to bottom, rgba(0,0,0,.05) 1px, transparent 1px)",
            backgroundSize: "64px 64px",
            WebkitMaskImage: "radial-gradient(ellipse 70% 70% at 70% 40%, #000 15%, transparent 72%)",
            maskImage: "radial-gradient(ellipse 70% 70% at 70% 40%, #000 15%, transparent 72%)",
          }}
        />

        <div className="relative z-10 flex flex-col min-h-screen">
          <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-center pt-4 sm:pt-6 px-4 sm:px-8 gap-2 sm:gap-3">
            <a
              href="#top"
              aria-label="PETRA home"
              className="flex items-center justify-center rounded-full w-10 h-10 sm:w-11 sm:h-11 shrink-0"
              style={{ backgroundColor: "#EDEDED" }}
            >
              <Logo />
            </a>
            <div
              className="flex items-center gap-4 sm:gap-10 rounded-xl px-4 sm:px-8 py-2.5 sm:py-3"
              style={{ backgroundColor: "#EDEDED" }}
            >
              {NAV.map((n) => (
                <a key={n.href} href={n.href} className={navLink}>
                  {n.label}
                </a>
              ))}
            </div>
          </nav>

          <div id="top" className={`flex-1 flex items-end pb-10 sm:pb-16 lg:pb-20 ${pad} pt-28`}>
            <div className="max-w-sm">
              <a
                href="#products"
                className="inline-flex items-center gap-1.5 text-[11.5px] font-medium text-blue-500 hover:text-blue-600 transition-colors mb-3 group"
              >
                PMS · POS · DMS, built in Bangladesh
                <span className={arrow}>→</span>
              </a>
              <h1 className="text-[1.5rem] sm:text-[1.75rem] leading-[1.15] font-medium text-gray-900 tracking-tight mb-3">
                Software that runs hospitality.
              </h1>
              <p className="text-[13px] text-gray-500 font-normal mb-3">
                Hospitality software for properties, outlets and distribution operations, built around real-world workflows.
              </p>
              <div className="flex flex-wrap gap-3">
                <a
                  href="#contact"
                  className="inline-flex items-center gap-2 text-[13px] font-medium text-blue-500 border border-blue-400 rounded-full px-5 py-2.5 hover:bg-blue-500 hover:text-white hover:border-blue-500 transition-all duration-200 group"
                >
                  Book a demo <span className={arrow}>→</span>
                </a>
                <a href="#products" className="inline-flex items-center gap-2 text-[13px] font-medium text-gray-700 hover:text-gray-900 px-3 py-2.5 transition-colors">
                  Explore products
                </a>
              </div>
            </div>
          </div>
        </div>
      </header>

      <main>
        {/* AT A GLANCE */}
        <section className={`${pad} py-10 bg-[#EDEDED]`}>
          <ul className="reveal max-w-5xl mx-auto grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
            {GLANCE.map((g) => (
              <li key={g.title}>
                <p className="text-[13px] font-medium">{g.title}</p>
                <p className="text-[12.5px] text-gray-500 mt-1">{g.text}</p>
              </li>
            ))}
          </ul>
        </section>

        {/* PRODUCTS */}
        <section id="products" className={`${pad} py-20 sm:py-28`}>
          <div className="max-w-5xl mx-auto">
            <Heading label="Products" title="Three products, one hospitality workflow.">
              <p className="text-[13px] text-gray-400 mt-3">
                All three are in preview and shown in demos on request. Screens here are illustrative.
              </p>
            </Heading>
            <div className="grid gap-4 md:grid-cols-3">
              {PRODUCTS.map((p) => (
                <article key={p.name} className="reveal rounded-2xl bg-[#EDEDED] p-6 flex flex-col">
                  <div className="h-36 rounded-xl bg-white/70 mb-5 grid place-items-center text-[11.5px] text-gray-400">{p.image}</div>
                  <div className="flex items-center justify-between">
                    <h3 className="text-[15px] font-medium">{p.name}</h3>
                    <Chip>Preview</Chip>
                  </div>
                  <p className="text-[12px] text-gray-400 mt-0.5">{p.full}</p>
                  <p className="text-[13px] text-gray-500 mt-3">{p.text}</p>
                  <ul className="mt-4 space-y-1.5 text-[12.5px] text-gray-600 flex-1">
                    {p.features.map((f) => (
                      <li key={f}>{f}</li>
                    ))}
                  </ul>
                  <a href="#contact" className="mt-5 inline-flex items-center gap-1.5 text-[12.5px] font-medium text-blue-500 hover:text-blue-600 group">
                    Request a {p.name} demo <span className={arrow}>→</span>
                  </a>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* ECOSYSTEM */}
        <section id="ecosystem" className={`${pad} py-20 sm:py-28 bg-[#EDEDED]`}>
          <div className="max-w-5xl mx-auto grid gap-10 md:grid-cols-[1fr_1.4fr] md:gap-16">
            <div className="reveal">
              <p className={eyebrow}>Ecosystem</p>
              <h2 className={h2}>Three products today. One shared core next.</h2>
              <p className="text-[13px] text-gray-500 mt-3">
                PetraPMS, PetraPOS and PetraDMS run independently today. Petra Core is the planned layer that connects them. Every link below is planned, not shipped.
              </p>
            </div>
            <ul className="reveal divide-y divide-gray-300 border-y border-gray-300 text-[13px]">
              {LINKS.map((l) => (
                <li key={l.label} className="flex items-start justify-between gap-4 py-3">
                  <div>
                    <p className="font-medium">{l.label}</p>
                    <p className="text-gray-500 text-[12.5px]">{l.text}</p>
                  </div>
                  <Chip dashed>Planned</Chip>
                </li>
              ))}
            </ul>
          </div>
        </section>

        {/* DEPLOYMENT */}
        <section id="deployment" className={`${pad} py-20 sm:py-28`}>
          <div className="max-w-5xl mx-auto">
            <Heading label="Deployment" title="Local-first when reliability matters.">
              <p className="text-[13px] text-gray-500 mt-3">
                PetraPMS is designed to run on the property's own network. Terminals talk to a Petra server on site, and the data stays on hardware you control.
              </p>
            </Heading>
            <Steps items={DEPLOY} cols="md:grid-cols-3" />
            <p className="reveal text-[12.5px] text-gray-400 mt-8 max-w-xl">
              Windows installer and PostgreSQL for larger deployments are planned. Deployment for PetraPOS and PetraDMS, backups and remote access are agreed per project.
            </p>
          </div>
        </section>

        {/* INDUSTRIES */}
        <section id="industries" className={`${pad} py-20 sm:py-28 bg-[#EDEDED]`}>
          <div className="max-w-5xl mx-auto">
            <Heading label="Industries" title="Built for the people who host, serve and move guests." />
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {INDUSTRIES.map((i) => (
                <div key={i.name} className={`reveal rounded-2xl bg-[#f0f0ee] p-6 ${i.wide ? "sm:col-span-2" : ""}`}>
                  <h3 className="text-[15px] font-medium">{i.name}</h3>
                  <p className="text-[13px] text-gray-500 mt-2">{i.text}</p>
                  <p className="text-[12px] mt-4">
                    {i.tag && <span className="text-blue-500">{i.tag}</span>}
                    {i.tag && i.planned && <span className="text-gray-400"> · </span>}
                    {i.planned && <span className="text-gray-400">{i.planned}</span>}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* WHY */}
        <section id="why" className={`${pad} py-20 sm:py-28`}>
          <div className="max-w-5xl mx-auto">
            <Heading label="Why Petra" title="Specific advantages, not slogans." />
            <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {WHY.map((w) => (
                <div key={w.title} className="reveal border-t border-gray-300 pt-5">
                  <h3 className="text-[14px] font-medium">{w.title}</h3>
                  <p className="text-[13px] text-gray-500 mt-2">{w.text}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* PROCESS */}
        <section id="process" className={`${pad} py-20 sm:py-28 bg-[#EDEDED]`}>
          <div className="max-w-5xl mx-auto">
            <Heading label="Implementation" title="What happens after you contact Petra." />
            <Steps items={PROCESS} cols="sm:grid-cols-2 lg:grid-cols-4" />
          </div>
        </section>

        {/* CONTACT */}
        <section id="contact" className={`${pad} py-20 sm:py-28`}>
          <div className="reveal max-w-5xl mx-auto rounded-3xl bg-gray-900 text-white px-6 sm:px-14 py-14 sm:py-20 grid gap-10 md:grid-cols-[1.2fr_1fr] md:items-end">
            <div className="max-w-md">
              <h2 className={h2}>See Petra running on your property.</h2>
              <p className="text-[13px] text-gray-400 mt-3">
                Tell us about your operation and the products you are considering. We will walk you through them live, on sample data. We reply within one working day. No commitment.
              </p>
            </div>
            <div className="flex flex-col gap-3 text-[13px]">
              <a
                href={`mailto:${SITE.email}`}
                className="inline-flex items-center justify-between gap-2 bg-blue-500 hover:bg-blue-600 rounded-full px-5 py-2.5 font-medium transition-colors duration-200 group"
              >
                Email us <span className={arrow}>→</span>
              </a>
              <a
                href={`tel:${SITE.phoneHref}`}
                className="inline-flex items-center justify-between gap-2 border border-gray-600 hover:border-gray-400 rounded-full px-5 py-2.5 font-medium transition-colors duration-200"
              >
                {SITE.phone}
              </a>
            </div>
          </div>
        </section>
      </main>

      {/* FOOTER */}
      <footer className={`${pad} pt-16 pb-10 bg-[#EDEDED]`}>
        <div className="max-w-5xl mx-auto grid gap-10 sm:grid-cols-2 md:grid-cols-[1.5fr_1fr_1fr_1fr]">
          <div>
            <div className="flex items-center gap-2.5">
              <span className="flex items-center justify-center rounded-full w-9 h-9 bg-[#f0f0ee]">
                <Logo size={16} />
              </span>
              <span className="text-[14px] font-medium tracking-wide">PETRA</span>
            </div>
            <p className="text-[12.5px] text-gray-500 mt-4 max-w-[30ch]">PETRA Software Solutions builds hospitality software in Bangladesh.</p>
          </div>
          <div>
            <h3 className="text-[11.5px] font-medium text-gray-400 mb-3">Products</h3>
            <ul className="space-y-2 text-[13px] text-gray-700">
              {PRODUCTS.map((p) => (
                <li key={p.name}>
                  <a href="#products" className="hover:text-gray-900 transition-colors">{p.name}</a>
                </li>
              ))}
            </ul>
          </div>
          <div>
            <h3 className="text-[11.5px] font-medium text-gray-400 mb-3">Company</h3>
            <ul className="space-y-2 text-[13px] text-gray-700">
              <li><a href="#why" className="hover:text-gray-900 transition-colors">Why Petra</a></li>
              <li><a href="#industries" className="hover:text-gray-900 transition-colors">Industries</a></li>
              <li><a href="#process" className="hover:text-gray-900 transition-colors">Implementation</a></li>
            </ul>
          </div>
          <div>
            <h3 className="text-[11.5px] font-medium text-gray-400 mb-3">Contact</h3>
            <ul className="space-y-2 text-[13px] text-gray-700 break-words">
              <li><a href={`mailto:${SITE.email}`} className="hover:text-gray-900 transition-colors">{SITE.email}</a></li>
              <li><a href={`tel:${SITE.phoneHref}`} className="hover:text-gray-900 transition-colors">{SITE.phone}</a></li>
              <li>Bangladesh</li>
            </ul>
          </div>
        </div>
        <div className="max-w-5xl mx-auto mt-12 pt-6 border-t border-gray-300 flex flex-wrap items-center justify-between gap-3 text-[12px] text-gray-400">
          <span>© 2026 PETRA Software Solutions. All rights reserved.</span>
          <span>Product screenshots are placeholders.</span>
        </div>
      </footer>
    </div>
  );
}
