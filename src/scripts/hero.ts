/**
 * Hero switcher: a laptop and a phone show two different products at once. Switching wipes both screens with a
 * circular liquid reveal and moves the accent colour. Auto-plays only without reduced motion; pauses on hover,
 * focus and while the hero is off screen. Without JS the first pair simply stays on show.
 */
type Step = { l: number; p: number; cap: string };
const INTERVAL = 5200;

function init(root: HTMLElement) {
  if (root.dataset.bound) return;
  root.dataset.bound = "1";
  const steps: Step[] = JSON.parse(document.getElementById("hero-steps")?.textContent ?? "[]");
  const dI = [...root.querySelectorAll<HTMLElement>(".hx-d img")];
  const pI = [...root.querySelectorAll<HTMLElement>(".hx-p img")];
  const btns = [...root.querySelectorAll<HTMLButtonElement>(".hx-seg button")];
  const ind = root.querySelector<HTMLElement>(".hx-ind");
  const cap = root.querySelector<HTMLElement>("[data-cap]");
  const motion = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let cur = 0;
  let prevL = steps[0].l;
  let prevP = steps[0].p;
  let timer = 0;
  let hold = false;
  let visible = true;

  const wipe = (imgs: HTMLElement[], n: number, prev: number) => {
    imgs.forEach((im, i) => {
      if (i === n) {
        im.style.transition = "none";
        im.classList.remove("under", "off", "on");
        void im.offsetWidth;
        im.style.transition = "";
        im.classList.add("on");
      } else if (i === prev && prev !== n) {
        im.classList.remove("on", "off");
        im.classList.add("under");
      } else {
        im.classList.remove("on", "under");
        im.classList.add("off");
      }
    });
    setTimeout(() => {
      imgs.forEach((im, i) => {
        if (i !== n && im.classList.contains("under")) {
          im.classList.remove("under");
          im.classList.add("off");
        }
      });
    }, 1300);
  };

  const place = (n: number, instant = false) => {
    const b = btns[n];
    if (!ind || !b) return;
    if (instant) ind.style.transition = "none";
    ind.style.left = `${b.offsetLeft}px`;
    ind.style.width = `${b.offsetWidth}px`;
    if (instant) requestAnimationFrame(() => requestAnimationFrame(() => (ind.style.transition = "")));
  };

  const schedule = () => {
    clearTimeout(timer);
    if (motion && !hold && visible) timer = window.setTimeout(() => go((cur + 1) % steps.length), INTERVAL);
  };

  function go(n: number) {
    const { l, p } = steps[n];
    wipe(dI, l, prevL);
    wipe(pI, p, prevP);
    prevL = l;
    prevP = p;
    cur = n;
    root.dataset.p = String(l);
    btns.forEach((b, i) => b.setAttribute("aria-pressed", String(i === n)));
    place(n);
    if (cap) cap.innerHTML = steps[n].cap;
    schedule();
  }

  dI.forEach((im, i) => im.classList.add(i === steps[0].l ? "on" : "off"));
  pI.forEach((im, i) => im.classList.add(i === steps[0].p ? "on" : "off"));
  root.classList.add("hx-live");
  place(0, true);
  window.addEventListener("resize", () => place(cur, true), { passive: true });
  btns.forEach((b) =>
    b.addEventListener("click", () => {
      const i = Number(b.dataset.i);
      if (i !== cur) go(i);
      else schedule();
    }),
  );
  const stage = root.querySelector<HTMLElement>(".hx-stage");
  const pause = () => {
    hold = true;
    clearTimeout(timer);
  };
  const resume = () => {
    hold = false;
    schedule();
  };
  stage?.addEventListener("pointerenter", pause);
  stage?.addEventListener("pointerleave", resume);
  stage?.addEventListener("focusin", pause);
  stage?.addEventListener("focusout", resume);
  new IntersectionObserver((es) => {
    visible = es[0].isIntersecting;
    if (visible) schedule();
    else clearTimeout(timer);
  }).observe(root);
  schedule();
}

document.addEventListener("astro:page-load", () => document.querySelectorAll<HTMLElement>("[data-hero]").forEach(init));

export {};
