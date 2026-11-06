// Shared by every mockup: show the view named in the URL hash and mark the matching nav items.
const views = [...document.querySelectorAll("[data-v]")].map((e) => e.dataset.v);
const view = location.hash.slice(1) || views[0];
document.querySelectorAll("[data-v]").forEach((e) => (e.hidden = e.dataset.v !== view));
document.querySelectorAll("[data-nav]").forEach((e) => e.classList.toggle("on", e.dataset.nav === view));
