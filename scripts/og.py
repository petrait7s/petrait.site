"""Render mockups/og.html to public/og.png (1200x630 Open Graph image).

Usage: python3 scripts/og.py     Needs: pip install playwright. Set CHROMIUM_PATH to use an existing Chromium binary.
"""
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.goto((ROOT / "mockups/og.html").as_uri())
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(500)
    page.screenshot(path=str(ROOT / "public/og.png"), type="png")
    browser.close()
print("saved public/og.png")
