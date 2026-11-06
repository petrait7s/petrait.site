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

/** Swipeable card rows (.hs) must be reachable by keyboard and named for screen readers while they scroll. */
function initSwipeRows() {
  const rows = document.querySelectorAll<HTMLElement>(".hs");
  const mark = () =>
    rows.forEach((row) => {
      if (row.scrollWidth > row.clientWidth + 2) {
        row.tabIndex = 0;
        const section = row.closest("section");
        const heading = section?.querySelector("h2")?.textContent?.trim();
        row.setAttribute("aria-label", heading ? `${heading}: swipe to see more` : "Swipe to see more");
      } else {
        row.removeAttribute("tabindex");
        row.removeAttribute("aria-label");
      }
    });
  mark();
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

document.addEventListener("astro:page-load", () => {
  initSwipeRows();
  initReveal();
  initSpot();
  initAurora();
});
