# Codebase Conventions

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
