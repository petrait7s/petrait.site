/**
 * Live sample interfaces. Each [data-live] box holds a poster image; when it scrolls into view we load the
 * matching page from /demo in an iframe, scale it to the box, and fade it in over the poster. The page scrolls
 * itself (see public/demo/app.js). Skipped for reduced motion and Save-Data: the poster stays.
 */
const motionOk = () => {
  const nav = navigator as Navigator & { connection?: { saveData?: boolean } };
  return !window.matchMedia("(prefers-reduced-motion: reduce)").matches && !nav.connection?.saveData;
};

function mount(box: HTMLElement) {
  if (box.dataset.mounted) return;
  box.dataset.mounted = "1";
  const w = Number(box.dataset.w);
  const h = Number(box.dataset.h);
  const frame = document.createElement("iframe");
  frame.src = box.dataset.src ?? "";
  frame.title = `${box.dataset.title ?? "Sample interface"} (live sample interface)`;
  frame.setAttribute("aria-hidden", "true"); // the poster image already carries the description
  frame.setAttribute("sandbox", "allow-scripts allow-same-origin");
  frame.tabIndex = -1;
  frame.style.cssText = `position:absolute;left:0;top:0;width:${w}px;height:${h}px;border:0;transform-origin:0 0;pointer-events:none;opacity:0;transition:opacity .7s ease`;
  const fit = () => (frame.style.transform = `scale(${box.clientWidth / w})`);
  fit();
  new ResizeObserver(fit).observe(box);
  frame.addEventListener("load", () => (frame.style.opacity = "1"));
  box.appendChild(frame);
  // let the visitor read a screen: pause its motion while the pointer is over it
  const send = (pause: boolean) => frame.contentWindow?.postMessage({ type: "petra-demo", pause }, window.location.origin);
  box.addEventListener("pointerenter", () => send(true));
  box.addEventListener("pointerleave", () => send(false));
}

function init() {
  if (!motionOk()) return;
  const io = new IntersectionObserver(
    (entries) =>
      entries.forEach((e) => {
        const box = e.target as HTMLElement;
        if (e.isIntersecting && box.offsetParent !== null) {
          mount(box);
          io.unobserve(box);
        }
      }),
    { rootMargin: "200px" },
  );
  document.querySelectorAll<HTMLElement>("[data-live]").forEach((el) => io.observe(el));
}

document.addEventListener("astro:page-load", init);
