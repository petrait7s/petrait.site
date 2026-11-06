"""Render the 3D scenes to poster images (src/assets/posters/<scene>.webp).

Posters are shown instantly while the 3D chunk loads and whenever 3D is off (no WebGL, reduced motion,
Save-Data, or a slow device). Regenerate them after changing a scene.

Usage:
  ENABLE_LAB=1 npm run build && npm run preview -- --port 4400     # in another terminal
  python3 scripts/posters.py [lab ...]
Needs: pip install playwright pillow. Set CHROMIUM_PATH to use an existing Chromium binary.
Env: BASE_URL (default http://localhost:4400).
"""
import io
import os
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "assets" / "posters"
OUT.mkdir(parents=True, exist_ok=True)
BASE = os.environ.get("BASE_URL", "http://localhost:4400")

# scene id -> lab page path (the element #stage-3d is captured)
SCENES = {"lab": "/lab/lab/"}
GL_ARGS = ["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"]
# Pretend to be a capable desktop so the full-quality scene is rendered.
HIGH_END = """
Object.defineProperty(navigator, 'hardwareConcurrency', { value: 16 });
Object.defineProperty(navigator, 'deviceMemory', { value: 8 });
"""


def capture(browser, scene, path):
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=1600 / 1024)
    ctx.add_init_script(HIGH_END)
    page = ctx.new_page()
    page.goto(BASE + path, wait_until="networkidle")
    page.locator("#stage-3d").scroll_into_view_if_needed()
    page.wait_for_selector('[data-tier="high"][data-ready="true"]', timeout=20000)
    page.wait_for_timeout(1500)
    img = Image.open(io.BytesIO(page.locator("#stage-3d").screenshot(type="png"))).convert("RGB")
    img = img.resize((1600, 1000), Image.LANCZOS)
    img.save(OUT / f"{scene}.webp", "WEBP", quality=88, method=6)
    print("saved", scene, img.size)
    ctx.close()


if __name__ == "__main__":
    which = sys.argv[1:] or list(SCENES)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None, args=GL_ARGS)
        for scene in which:
            capture(browser, scene, SCENES[scene])
        browser.close()
