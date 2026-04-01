# Codebase Testing

## Current State

No automated test suite was found in the repository.

## Evidence

- No `package.json`, `requirements.txt`, `pyproject.toml`, or similar test runner config exists.
- No `tests/`, `spec/`, or `__tests__/` directories were found.
- No GitHub Actions or other CI workflow files were found.
- No browser E2E tooling config such as Playwright or Cypress was found.

## Effective Validation Strategy Today

The project appears to rely on manual browser testing:

- Open each static page directly or through a local static server.
- Check desktop and mobile navigation.
- Verify hero media, images, and CTA links.
- Verify `?lang=en` swap behavior per page.
- Verify page-specific widgets only on pages that contain their required DOM.

## Areas That Need Manual Regression After Changes

- HTMX language toggles, especially nested product pages.
- Relative asset paths in root pages versus product pages.
- `projector.js` features after content swaps.
- Cookie consent rendering in Dutch and English.
- Footer links, contact CTAs, and anchor targets.
- Content consistency between full pages and corresponding partials.

## Content-Specific Risk

Because this site is content-heavy and duplicated, regression risk is largely editorial:

- A product name can be changed in one file but remain stale elsewhere.
- Numerical claims like `60+` or `100+` can drift across pages.
- Package labels and FAQ text can diverge between NL and EN partials.

## Suggested Future Test Baseline

- Add a minimal smoke-test pass that checks all pages load without 404 assets.
- Add assertions for every `?lang=en` route that should swap successfully.
- Add a content audit script for key phrases that must stay synchronized.
- Add a link checker for internal navigation and asset references.

## Until Automation Exists

Any substantive content or navigation change should be verified manually across homepage, affected product pages, and both language variants before release.
