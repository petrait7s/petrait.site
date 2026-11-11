/** Progressive enhancement: scroll reveal, card spotlight and the aurora pause/resume. Pages are fully usable without it. */
const reduced = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const finePointer = () => window.matchMedia("(hover: hover) and (pointer: fine)").matches;

function initReveal() {
  const els = document.querySelectorAll<HTMLElement>("[data-reveal]");
  if (!("IntersectionObserver" in window) || reduced()) {
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
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" },
  );
  els.forEach((el) => io.observe(el));
}

function initSpot() {
  if (!finePointer()) return;
  document.querySelectorAll<HTMLElement>(".spot").forEach((el) => {
    let raf = 0;
    el.addEventListener(
      "pointermove",
      (e) => {
        if (raf) return;
        raf = requestAnimationFrame(() => {
          raf = 0;
          const r = el.getBoundingClientRect();
          el.style.setProperty("--mx", `${e.clientX - r.left}px`);
          el.style.setProperty("--my", `${e.clientY - r.top}px`);
        });
      },
      { passive: true },
    );
  });
}

/** Run the aurora animation only while its section is on screen. */
function initAurora() {
  const els = document.querySelectorAll<HTMLElement>(".aurora");
  if (!("IntersectionObserver" in window)) {
    els.forEach((el) => el.setAttribute("data-active", ""));
    return;
  }
  const io = new IntersectionObserver((entries) =>
    entries.forEach((e) => (e.isIntersecting ? e.target.setAttribute("data-active", "") : e.target.removeAttribute("data-active"))),
  );
  els.forEach((el) => io.observe(el));
}

/** Swipeable card rows (.hs): keyboard focus, a screen-reader name, and arrows plus dots so touch users see there is more. */
const ARROW = (d: string) => `<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="${d}"/></svg>`;

function buildControls(row: HTMLElement) {
  const cards = Array.from(row.children) as HTMLElement[];
  const bar = document.createElement("div");
  bar.className = "hs-ctl";
  bar.innerHTML = `<button type="button" class="hs-btn" data-dir="-1" aria-label="Previous">${ARROW("M15 5l-7 7 7 7")}</button><span class="hs-dots" aria-hidden="true">${cards.map(() => "<i></i>").join("")}</span><button type="button" class="hs-btn" data-dir="1" aria-label="Next">${ARROW("M9 5l7 7-7 7")}</button>`;
  const [prev, next] = Array.from(bar.querySelectorAll<HTMLButtonElement>(".hs-btn"));
  const dots = Array.from(bar.querySelectorAll("i"));
  const step = () => (cards[1] ? cards[1].offsetLeft - cards[0].offsetLeft : row.clientWidth);
  const update = () => {
    const max = row.scrollWidth - row.clientWidth;
    const i = Math.min(cards.length - 1, Math.round(row.scrollLeft / Math.max(step(), 1)));
    dots.forEach((d, n) => d.classList.toggle("on", n === (row.scrollLeft >= max - 4 ? cards.length - 1 : i)));
    prev.disabled = row.scrollLeft <= 4;
    next.disabled = row.scrollLeft >= max - 4;
  };
  let raf = 0;
  row.addEventListener("scroll", () => raf || (raf = requestAnimationFrame(() => ((raf = 0), update()))), { passive: true });
  bar.addEventListener("click", (e) => {
    const b = (e.target as HTMLElement).closest<HTMLButtonElement>(".hs-btn");
    if (b) row.scrollBy({ left: Number(b.dataset.dir) * step(), behavior: reduced() ? "auto" : "smooth" });
  });
  row.after(bar);
  update();
}

function initSwipeRows() {
  document.querySelectorAll(".hs-ctl").forEach((el) => el.remove());
  document.querySelectorAll<HTMLElement>(".hs").forEach((row) => {
    const scrolls = row.scrollWidth > row.clientWidth + 2;
    if (!scrolls) {
      row.removeAttribute("tabindex");
      row.removeAttribute("aria-label");
      return;
    }
    row.tabIndex = 0;
    const heading = row.closest("section")?.querySelector("h2")?.textContent?.trim();
    row.setAttribute("aria-label", heading ? `${heading}: swipe to see more` : "Swipe to see more");
    buildControls(row);
  });
  if (!resizeBound) {
    resizeBound = true;
    let t = 0;
    window.addEventListener(
      "resize",
      () => {
        clearTimeout(t);
        t = window.setTimeout(() => initSwipeRows(), 150);
      },
      { passive: true },
    );
  }
}
let resizeBound = false;

/** Liquid buttons flood from the point where the pointer enters or leaves. */
let liquidBound = false;
function initLiquid() {
  if (liquidBound) return;
  liquidBound = true;
  const set = (e: PointerEvent) => {
    const el = (e.target as HTMLElement | null)?.closest<HTMLElement>(".liquid");
    if (!el) return;
    const r = el.getBoundingClientRect();
    el.style.setProperty("--x", `${e.clientX - r.left}px`);
    el.style.setProperty("--y", `${e.clientY - r.top}px`);
  };
  document.addEventListener(
    "pointerdown",
    (e) => {
      if (e.pointerType === "mouse") return;
      const el = (e.target as HTMLElement | null)?.closest<HTMLElement>(".liquid");
      if (!el) return;
      set(e);
      el.classList.add("tap");
      setTimeout(() => el.classList.remove("tap"), 600);
    },
    { passive: true },
  );
  document.addEventListener("pointerover", set, { passive: true });
  document.addEventListener("pointerout", set, { passive: true });
}

document.addEventListener("astro:page-load", () => {
  initLiquid();
  initSwipeRows();
  initReveal();
  initSpot();
  initAurora();
});
