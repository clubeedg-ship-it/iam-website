# Codebase Structure

## Top-Level Layout

- `index.html` - homepage.
- Root `*.html` pages - top-level marketing, policy, and sector pages.
- `products/` - full product pages.
- `partials/` - localized page fragments for HTMX swaps.
- `partials/products/` - localized product page fragments.
- `media/` - images, videos, product assets, and fonts.
- `js/` - vendored HTMX and cookie consent script.
- `tools/` - one-off migration helper.
- `.planning/codebase/` - generated codebase map documents.

## Root Pages

Representative root pages:

- `index.html`
- `prijzen.html`
- `over-ons.html`
- `onderwijs.html`
- `parken-speelhallen.html`
- `zorg-revalidatie.html`
- `3d-spellen.html`
- `bouw-een-park.html`

These pages act as browser entry points and include full `<html>` documents.

## Product Pages

Files under `products/` are also full entry points:

- `products/interactieve-vloer.html`
- `products/interactieve-muur.html`
- `products/interactieve-zandbak.html`
- `products/interactieve-klimwand.html`
- `products/interactieve-tekeningen.html`
- `products/mobiele-vloer.html`
- `products/software-maatwerk.html`

## Partial Files

- `partials/index-nl.html` and `partials/index-en.html` mirror homepage body content.
- `partials/products/*-nl.html` and `partials/products/*-en.html` mirror product page body content.
- Root partials and nested partials use different relative path prefixes.

## Shared Asset Files

- `styles.css` - global stylesheet for all pages.
- `projector.js` - shared behavior for the entire site.
- `js/cookie-consent.js` - shared compliance UI.
- `js/htmx.min.js` - vendored library.

## Supporting Files

- `robots.txt`
- `sitemap.xml`
- `cookiebeleid.html`
- `privacybeleid.html`
- `toegankelijkheid.html`
- `website-adjustments.xlsx`

## Naming Conventions

- Dutch slugs are used for URLs and file names.
- English variants are generally expressed as `-en` partials, not separate English entry pages.
- Product and sector file names are kebab-case.
- Shared JS uses browser-global functions instead of modules.

## Structural Implications

- Content duplication is the dominant structural pattern.
- A change to one concept often touches the root page, the NL partial, the EN partial, and sometimes product pages as well.
- There is no separation between content source and rendered output, so repository structure mirrors site IA directly.
