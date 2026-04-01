# Codebase Architecture

## Overall Pattern

This is a static multi-page website with shared assets and a partial-based localization layer. The architecture is file-oriented rather than component-oriented.

## Main Building Blocks

- Full page entry points at repo root such as `index.html`, `prijzen.html`, and `zorg-revalidatie.html`.
- Product entry points under `products/` such as `products/interactieve-vloer.html` and `products/mobiele-vloer.html`.
- Localized partial content under `partials/` and `partials/products/`.
- Shared presentation layer in `styles.css`.
- Shared interaction layer in `projector.js`.
- Auxiliary compliance script in `js/cookie-consent.js`.

## Page Composition Model

- A full page includes document head, fixed background canvas, `#page-wrapper`, header, mobile nav, main content, footer, and scripts.
- Language switching swaps only the inner HTML of `#page-wrapper`.
- Partial files contain page wrapper content fragments, not full HTML documents.
- Original pages also contain bootstrapping logic that checks `?lang=en` on load and fetches the English partial via HTMX.

## Data Flow

1. Server returns a static HTML page.
2. Browser loads `styles.css`, `js/htmx.min.js`, shared JS, and media assets.
3. On `DOMContentLoaded`, `projector.js` initializes canvas effects and page widgets.
4. If `?lang=en` is present, HTMX requests the matching English partial and swaps the page content.
5. After HTMX swaps, selected JS initializers rerun through `htmx:afterSwap` listeners.

## Shared Behavior Model

- `projector.js` centralizes multiple independent concerns:
- Background canvas particle simulation.
- Scroll reveal animations.
- Stat counters.
- ROI calculator.
- Back-to-top button.
- Scroll-driven roadmap animation.

This is convenient for static delivery but couples unrelated features into one global script.

## Navigation Model

- Navigation is duplicated across root pages, product pages, and partials.
- Desktop and mobile navigation markup is hand-authored in each page family.
- Language toggle buttons are also repeated and rely on HTMX attributes that differ by relative path depth.

## Content Architecture

- Content is stored directly in HTML, including pricing, FAQs, package information, and product claims.
- There is no schema, data layer, or content abstraction.
- The spreadsheet `website-adjustments.xlsx` indicates business content changes are currently managed outside the codebase and then applied manually.

## Localization Architecture

- Localization is implemented as separate NL and EN HTML partials.
- The Python migration script can extract header-to-footer content from full pages, create `-nl` partials, generate rough `-en` partials via string replacement, and patch original pages.
- Because translation is content-copy based, structural divergence between languages is possible.

## Important Constraints

- Any structural page change often requires synchronized edits in multiple files.
- Any JS that depends on swapped DOM must tolerate re-initialization after HTMX updates.
- Relative paths differ between root pages and nested product pages, which makes copy-paste changes error-prone.
