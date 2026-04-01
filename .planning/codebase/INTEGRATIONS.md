# Codebase Integrations

## Summary

This site has very few external integrations. The architecture is intentionally self-contained and file-based, with most behavior delivered from local assets.

## Browser APIs

- `localStorage` is used in `js/cookie-consent.js` to persist cookie consent state.
- `IntersectionObserver` is used in `projector.js` for scroll reveal and stat counter behavior.
- `requestAnimationFrame` is used heavily in `projector.js` for animation loops and number transitions.
- `matchMedia('(prefers-reduced-motion: reduce)')` is used for accessibility-aware motion handling.
- `<video>` playback is used for homepage and product hero media.

## HTMX Partial Loading

- HTMX is the main integration mechanism for language switching.
- Pages load local partials such as `partials/index-en.html` and `partials/products/mobiele-vloer-nl.html`.
- The partial swap target is usually `#page-wrapper`.
- Query params like `?lang=en` are pushed into browser history to preserve selected language.

## Contact and Lead Capture

- Calls to action frequently use `mailto:` links such as `mailto:info@interactivemove.nl`.
- Telephone links such as `tel:+31623998934` are used in contact sections.
- No backend form submission or CRM integration was found in the inspected files.

## Social and External Links

- Footer links point to Facebook, Instagram, and YouTube profiles.
- These are simple outbound links and do not imply embedded SDK usage.

## Search / Discovery Assets

- `robots.txt` is present.
- `sitemap.xml` is present.
- No structured-data generation tooling was found.

## Localization Integration

- English and Dutch content is implemented as separate partial files, not as translation keys.
- `tools/migrate_i18n.py` attempts to automate EN partial generation by replacing hard-coded Dutch strings.
- This is a repo-local content transformation, not a runtime translation service.

## Analytics / Tracking

- No Google Analytics, GTM, Meta Pixel, or similar third-party tracking script was observed in the inspected files.
- Cookie consent text also states that only necessary cookies are used.

## Payment / Auth / API Backends

- No payment provider integration was found.
- No authentication provider or user account system was found.
- No remote API client code, webhooks, or database access layer was found.

## Operational Implication

The low integration surface keeps the site simple, but most business content changes must be made directly in HTML files because there is no CMS or external content source.
