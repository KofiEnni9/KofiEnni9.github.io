"""Rebuild cv.pdf from _cv/cv.html.

Usage (from the repo root):
    pip install playwright && playwright install chromium
    python3 _cv/build.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

here = Path(__file__).resolve().parent
src = here / "cv.html"
out = here.parent / "cv.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(src.as_uri())
    page.wait_for_timeout(300)
    page.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
    browser.close()

print(f"Wrote {out}")
