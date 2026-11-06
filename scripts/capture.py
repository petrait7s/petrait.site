"""Render the sample interfaces in public/demo to WebP posters in src/assets/products.

Posters are what visitors see first, with JavaScript off, with reduced motion, and on cards. The live, moving
versions are the same pages shown in frames on the site.

Usage: python3 mockups/build.py          # (re)generate public/demo/*.html
       python3 scripts/capture.py        # all screens listed in src/content/data/products.json
       python3 scripts/capture.py petrapms-dashboard stores-fashion   # only some
Needs: pip install playwright pillow. Set CHROMIUM_PATH to use an existing Chromium binary.
Each screen is captured on a 1440x900 desktop viewport and on a 393x852 smartphone viewport.
"""
import functools
import http.server
import io
import json
import os
import sys
import threading
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "assets" / "products"
OUT.mkdir(parents=True, exist_ok=True)

DESKTOP = dict(viewport={"width": 1440, "height": 900}, device_scale_factor=1.25)
MOBILE = dict(viewport={"width": 393, "height": 852}, device_scale_factor=2, is_mobile=True, has_touch=True)


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve():
    handler = functools.partial(Quiet, directory=str(ROOT / "public"))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def screens():
    seen = []
    for p in json.loads((ROOT / "src/content/data/products.json").read_text()):
        for s in p["screens"]:
            key = f"{s['page']}-{s['view']}"
            if key not in [k for k, *_ in seen]:
                seen.append((key, s["page"], s["view"]))
    return seen


def capture(browser, base, kind, opts, quality, items):
    ctx = browser.new_context(**opts)
    for key, page_name, view in items:
        page = ctx.new_page()
        page.goto(f"{base}/demo/{page_name}.html?autoplay=0#{view}", wait_until="load")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(900)
        img = Image.open(io.BytesIO(page.screenshot(type="png"))).convert("RGB")
        img.save(OUT / f"{key}-{kind}.webp", "WEBP", quality=quality, method=6)
        print("saved", f"{key}-{kind}", img.size)
        page.close()
    ctx.close()


if __name__ == "__main__":
    wanted = sys.argv[1:]
    items = [s for s in screens() if not wanted or s[0] in wanted]
    srv = serve()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        capture(browser, base, "desktop", DESKTOP, 80, items)
        capture(browser, base, "mobile", MOBILE, 78, items)
        browser.close()
    srv.shutdown()
