/* Shared by every demo page: pick the view from the hash, mark the nav, and gently auto-scroll the content
   so the interface looks alive. ?autoplay=0 turns the motion off (used when capturing still images). */
(function () {
  var qs = new URLSearchParams(location.search);
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var root = document.documentElement;
  function views() { return Array.prototype.map.call(document.querySelectorAll("[data-v]"), function (e) { return e.dataset.v; }); }
  function current() { return location.hash.slice(1) || views()[0]; }
  function show() {
    var v = current();
    document.querySelectorAll("[data-v]").forEach(function (e) { e.hidden = e.dataset.v !== v; });
    document.querySelectorAll("[data-nav]").forEach(function (e) { e.classList.toggle("on", e.dataset.nav === v); });
    document.title = (document.querySelector("[data-v]:not([hidden]) [data-title]") || { textContent: v }).textContent + " (sample interface)";
    play();
  }
  function play() {
    root.classList.remove("autoplay");
    if (qs.get("autoplay") === "0" || reduce) return;
    requestAnimationFrame(function () {
      var sec = document.querySelector("[data-v]:not([hidden])") || document;
      var vp = sec.querySelector(".viewport");
      var sc = sec.querySelector(".scroller");
      if (!vp || !sc) return;
      var travel = sc.scrollHeight - vp.clientHeight;
      if (travel < 24) return;
      var secs = Math.max(18, Math.min(70, travel / 22 + 10));
      sc.style.setProperty("--travel", travel + "px");
      sc.style.setProperty("--dur", secs + "s");
      document.querySelectorAll(".scroller").forEach(function (s) { s.style.setProperty("--travel", travel + "px"); s.style.setProperty("--dur", secs + "s"); });
      void sc.offsetWidth;
      root.classList.add("autoplay");
    });
  }
  addEventListener("hashchange", show);
  addEventListener("resize", play);
  addEventListener("load", show);
  /* the host page can pause the motion while a visitor points at the frame */
  addEventListener("message", function (e) {
    if (e.origin !== location.origin || !e.data || e.data.type !== "petra-demo") return;
    root.classList.toggle("paused", !!e.data.pause);
  });
  show();
})();
