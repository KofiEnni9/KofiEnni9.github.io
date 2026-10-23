# kofienni9.github.io

Personal site of Kofi A. Ennin, live at https://kofienni9.github.io.

- `index.html`: the whole site (single page, no build step).
- `cv.pdf`: downloadable CV linked from the site.
- `_cv/cv.html`: source for `cv.pdf`. Edit it, then rebuild with `python3 _cv/build.py` (needs Playwright with Chromium). Jekyll skips `_cv/`, so it isn't published.

To add a headshot, drop a `photo.jpg` in the repo root and add it to the hero in `index.html`.
