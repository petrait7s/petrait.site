/**
 * Hero product switcher: the sample screen changes with a circular liquid wipe, the blobs take the product's colour
 * and the floating cards show that product's sample numbers. Auto-plays only for visitors without reduced motion;
 * pauses on hover, focus, and while the hero is off screen. Without JS the first product simply stays on show.
 */
type Slide = { name: string; f: [[string, string], [string, string], string] };
const INTERVAL = 5200;

function init(root: HTMLElement) {
  if (root.dataset.bound) return;
  root.dataset.bound = "1";
  const slides: Slide[] = JSON.parse(document.getElementById("hero-slides")?.textContent ?? "[]");
  const stacks = [...root.querySelectorAll<HTMLElement>(".hx-stack")].map((s) => [...s.querySelectorAll<HTMLElement>("img")]);
  const btns = [...root.querySelectorAll<HTMLButtonElement>(".hx-sw button")];
  const cap = root.querySelector<HTMLElement>("[data-cap]");
  const sectors = [...root.querySelectorAll<HTMLElement>(".hx-sector span")];
  const motion = !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  let cur = 0;
  let timer = 0;
  let hold = false;
  let visible = true;

  const text = (key: string, value: string) => {
    const el = root.querySelector<HTMLElement>(`[data-f="${key}"]`);
    if (!el) return;
    el.style.opacity = "0";
    setTimeout(() => {
      el.textContent = value;
      el.style.opacity = "1";
    }, 220);
  };

  const schedule = () => {
    clearTimeout(timer);
    if (motion && !hold && visible) timer = window.setTimeout(() => go((cur + 1) % slides.length), INTERVAL);
  };

  function go(n: number) {
    const prev = cur;
    cur = n;
    stacks.forEach((imgs) => {
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
        stacks.forEach((a) =>
          a.forEach((im, i) => {
            if (i !== cur && im.classList.contains("under")) {
              im.classList.remove("under");
              im.classList.add("off");
            }
          }),
        );
      }, 1300);
    });
    root.dataset.p = String(n);
    btns.forEach((b, i) => {
      b.setAttribute("aria-pressed", String(i === n));
      const pg = b.querySelector<HTMLElement>(".pg");
      if (pg) {
        pg.style.animation = "none";
        void pg.offsetWidth;
        pg.style.animation = "";
      }
    });
    const f = slides[n].f;
    text("f1b", f[0][0]);
    text("f1s", f[0][1]);
    text("f2b", f[1][0]);
    text("f2s", f[1][1]);
    text("f3s", f[2]);
    if (cap) cap.textContent = slides[n].name;
    schedule();
  }

  // initial state: mark slide 0 explicitly so the others are hidden by class, not by position
  stacks.forEach((imgs) => imgs.forEach((im, i) => im.classList.add(i === 0 ? "on" : "off")));
  root.classList.add("hx-live");
  btns[0]?.classList.add("on");
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

  // sector line
  if (motion && sectors.length > 1) {
    let si = 0;
    setInterval(() => {
      if (!visible) return;
      const o = sectors[si];
      o.classList.remove("on");
      o.classList.add("out");
      setTimeout(() => o.classList.remove("out"), 800);
      si = (si + 1) % sectors.length;
      sectors[si].classList.add("on");
    }, 2600);
  }

  // gentle parallax on the desktop frame (fine pointers only)
  const desk = root.querySelector<HTMLElement>(".hx-desk");
  if (desk && motion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    root.addEventListener(
      "pointermove",
      (e) => {
        const r = root.getBoundingClientRect();
        desk.style.setProperty("--ry", `${-4 + ((e.clientX - r.left) / r.width - 0.5) * 6}deg`);
        desk.style.setProperty("--rx", `${2 - ((e.clientY - r.top) / r.height - 0.5) * 5}deg`);
      },
      { passive: true },
    );
  }
  schedule();
}

document.addEventListener("astro:page-load", () => document.querySelectorAll<HTMLElement>("[data-hero]").forEach(init));

export {};
