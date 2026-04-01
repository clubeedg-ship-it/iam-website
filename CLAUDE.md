<!-- GSD:project-start source:PROJECT.md -->
## Project

**IAM Website Repositioning**

This project turns the existing InterActiveMove marketing website into a cleaner, more accurate bilingual sales site for the current product story. The immediate focus is repositioning the mobile product line around `IAM mobiel`, correcting outdated claims and visuals, and making sure Dutch and English pages stay aligned across the brownfield HTML/HTMX codebase.

**Core Value:** Prospective customers should immediately understand what IAM sells now, what the `IAM mobiel` options are, and how to contact the team without being confused by outdated names, package structures, or duplicated copy.

### Constraints

- **Tech stack**: Keep the current static HTML + CSS + HTMX + vanilla JS stack — the request is to update the existing site safely, not to rebuild it
- **Content consistency**: Changes must be applied across full pages and partials — otherwise NL/EN and canonical/partial variants will drift
- **Path safety**: Root pages and nested product pages use different relative paths — content reuse must preserve working asset and partial links
- **Brownfield safety**: Existing published routes, navigation, and contact flows must keep working during the refresh
<!-- GSD:project-end -->

<!-- GSD:stack-start source:codebase/STACK.md -->
## Technology Stack

## Summary
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
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

## Authoring Style
- Markup is handwritten HTML with inline comments used sparingly.
- Styling mixes reusable classes with extensive inline `style` attributes in page files.
- JavaScript is written as plain browser script loaded with `<script>` tags.
## File and Path Conventions
- Root pages reference shared assets with paths like `media/...` and `/js/...`.
- Product pages use `../media/...` for nested assets but still use `/js/...` for shared scripts.
- Partial file names follow `name-nl.html` and `name-en.html`.
## CSS Conventions
- `styles.css` defines CSS custom properties in `:root`.
- The file is organized by large comment banners rather than separate modules.
- Component classes are descriptive and page-specific classes are mixed into the same file.
- Visual behavior often relies on utility-like classes plus inline overrides from markup.
## JavaScript Conventions
- Shared logic is global and imperative.
- Initialization is commonly attached to `DOMContentLoaded`.
- HTMX-aware reinitialization is done with `document.body.addEventListener('htmx:afterSwap', ...)`.
- Small page helpers such as `toggleMobileNav()` are sometimes defined inline inside individual pages.
## Content Conventions
- The site uses marketing-heavy copy embedded directly in HTML.
- Product claims such as package counts and number of games/programs are hard-coded in multiple places.
- Dutch appears to be the source language; English content is partly generated and partly manually edited.
## Localization Conventions
- Language switches do not change the document shell, only `#page-wrapper`.
- Original pages retain Dutch defaults and optionally load English partials based on query params.
- The migration script assumes it can extract content from `<header>` through `</footer>` and regenerate partials.
## Accessibility / UX Conventions
- Skip links and reduced-motion handling exist in the codebase.
- Some controls use `aria-label`, especially navigation and cookie consent elements.
- Accessibility quality varies because much UI behavior is still custom and duplicated.
## Error Handling
- Browser-side failures are usually ignored or logged with `console.warn`.
- There is no centralized error reporting.
- Missing DOM nodes are typically handled with early returns in JS initializers.
## Maintenance Pattern
- Broad site changes are currently managed through manual HTML edits and one-off scripts.
- The spreadsheet `website-adjustments.xlsx` is effectively part of the operational workflow for pending content changes.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

## Overall Pattern
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
## Shared Behavior Model
- `projector.js` centralizes multiple independent concerns:
- Background canvas particle simulation.
- Scroll reveal animations.
- Stat counters.
- ROI calculator.
- Back-to-top button.
- Scroll-driven roadmap animation.
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
<!-- GSD:architecture-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd:quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd:debug` for investigation and bug fixing
- `/gsd:execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd:profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
