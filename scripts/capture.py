"""Render the sample product interfaces in mockups/ to WebP screenshots in public/products.

Usage: python3 scripts/capture.py [petrapms petrapos ...]   (default: all)
Needs: pip install playwright pillow. Set CHROMIUM_PATH to use an existing Chromium binary instead of Playwright's own.
Each product is captured on a 1440x900 desktop viewport and on an iPhone 16 sized screen
(393x852 @3x, with a simulated status bar and tab bar).
"""
import io
import os
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "products"
OUT.mkdir(parents=True, exist_ok=True)

# product id -> views captured (the first view is the hero shot)
PRODUCTS = {
    "petrapms": ["dashboard", "rooms", "billing"],
    "petrapos": ["terminal", "analytics"],
    "petradms": ["dashboard", "inventory"],
    "website": ["editor", "sites"],
    "ecommerce": ["store", "products"],
}
DESKTOP = dict(viewport={"width": 1440, "height": 900}, device_scale_factor=1.5)
IPHONE16 = dict(viewport={"width": 393, "height": 852}, device_scale_factor=3, is_mobile=True, has_touch=True)


def save(page, name, quality):
    img = Image.open(io.BytesIO(page.screenshot(type="png"))).convert("RGB")
    img.save(OUT / f"{name}.webp", "WEBP", quality=quality, method=6)
    print("saved", name, img.size)


def capture(browser, pid, views, kind, opts, quality):
    ctx = browser.new_context(**opts)
    page = ctx.new_page()
    for view in views:
        page.goto((ROOT / f"mockups/{pid}.html").as_uri() + f"#{view}")
        page.reload()  # the hash is read once on load
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        save(page, f"{pid}-{view}-{kind}", quality)
    ctx.close()


if __name__ == "__main__":
    which = sys.argv[1:] or list(PRODUCTS)
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for pid in which:
            capture(browser, pid, PRODUCTS[pid], "desktop", DESKTOP, 88)
            capture(browser, pid, PRODUCTS[pid], "mobile", IPHONE16, 85)
        browser.close()
