/** Progressive enhancement: scroll reveal, card spotlight and device tilt. Pages are fully usable without it. */
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
    el.addEventListener("pointermove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.setProperty("--mx", `${e.clientX - r.left}px`);
      el.style.setProperty("--my", `${e.clientY - r.top}px`);
    });
  });
}

function initTilt() {
  if (!finePointer() || reduced()) return;
  document.querySelectorAll<HTMLElement>("[data-tilt]").forEach((host) => {
    const target = host.querySelector<HTMLElement>(".tilt");
    if (!target) return;
    host.addEventListener("pointermove", (e) => {
      const r = host.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - 0.5;
      const y = (e.clientY - r.top) / r.height - 0.5;
      target.style.setProperty("--ry", `${(x * 9).toFixed(2)}deg`);
      target.style.setProperty("--rx", `${(-y * 7).toFixed(2)}deg`);
    });
    host.addEventListener("pointerleave", () => {
      target.style.setProperty("--ry", "0deg");
      target.style.setProperty("--rx", "0deg");
    });
  });
}

document.addEventListener("astro:page-load", () => {
  initReveal();
  initSpot();
  initTilt();
});
