# Codebase Stack

## Summary

This repository is a static marketing website for InterActiveMove / IAM. It is built from hand-authored HTML, one shared stylesheet, one shared JavaScript bundle, localized HTML partials, and a small Python helper script for i18n migration.

## Languages

- HTML is the primary implementation language across root pages, product pages, and localized partials.
- CSS lives in a single global stylesheet: `styles.css`.
- JavaScript lives in `projector.js` plus `js/cookie-consent.js`.
- Python is used once for content generation / migration in `tools/migrate_i18n.py`.

## Runtime Model

- No build step is present.
- No package manager manifest exists (`package.json`, `pyproject.toml`, `requirements.txt` are absent).
- Pages are expected to be served as static files by a generic web server.
- Frontend behavior runs fully in the browser.

## Frontend Libraries

- HTMX is vendored locally in `js/htmx.min.js` and loaded directly from HTML pages.
- No React, Vue, bundler, or module system is used.
- No CSS framework is present; styling is custom.

## Styling System

- Global design tokens are declared in `styles.css`.
- Self-hosted `Inter` font files are loaded from `media/fonts/*.woff2`.
- The stylesheet is monolithic at 5603 lines and covers shared components, page-specific sections, animations, cookie consent, and responsive behavior.

## Media and Assets

- Rich media is stored under `media/`, including logos, hero images, product images, videos, and font files.
- Additional video assets also exist under `aditionals/`, which is ignored in `.gitignore`.
- Root pages reference media directly with relative paths such as `media/hero-home-page.mp4` and `../media/products/mobiele-vloer.jpg`.

## Configuration Conventions

- Cache busting is done manually via query params in asset URLs, for example `styles.css?v=1.3`.
- Language switching relies on HTMX requests to files in `partials/`.
- Cookie consent state is stored in `localStorage` under `iam_consent`.

## Tooling State

- No automated linting, formatting, test, or CI config is checked in.
- No deployment config is present in the repo.
- The only repo-local automation is `tools/migrate_i18n.py`, which generates partials and patches original pages.

## Key Files

- `index.html` - homepage shell and primary navigation.
- `styles.css` - global styling and component/page rules.
- `projector.js` - interactive canvas, reveal effects, counters, ROI calculator, and utilities.
- `js/cookie-consent.js` - GDPR-oriented consent banner logic.
- `tools/migrate_i18n.py` - partial generation and translation helper.
