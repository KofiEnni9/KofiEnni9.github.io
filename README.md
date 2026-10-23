# kofienni9.github.io

Personal site of Kofi A. Ennin, live at https://kofienni9.github.io.

## Layout

- `index.html`: home page (bio, selected work, publications, experience, skills).
- `projects/<slug>/index.html`: one deep-dive page per project. These are **generated**, so don't edit them directly.
- `assets/site.css`, `assets/site.js`: shared styles and the light/dark toggle.
- `assets/img/`: figures. The point-cloud, trajectory and arm images were rendered from data and CAD files in the project repositories.
- `cv.pdf`: downloadable CV, built from `_cv/cv.html`.

## Editing a project page

1. Edit the page body in `_build/pages/<slug>.html`, or its title, summary and facts in `_build/build.py`.
2. Run `python3 _build/build.py` from the repo root.
3. Commit both the fragment and the regenerated `projects/<slug>/index.html`.

To add a project, add an entry to `PAGES` in `_build/build.py`, write `_build/pages/<slug>.html`, rebuild, and add a row to the "Selected work" list in `index.html`.

## Rebuilding the CV

Edit `_cv/cv.html`, then run `python3 _cv/build.py` (needs Playwright with Chromium).

Jekyll skips folders that start with an underscore, so `_build/` and `_cv/` are never published.
