# Research: Architecture

**Project:** IAM Website Repositioning
**Domain:** Brownfield static site maintenance
**Researched:** 2026-04-01
**Confidence:** HIGH

## Recommended Architecture Approach

Treat the work as a safe content-release pipeline over an existing static site:

1. Identify every route and partial affected by the requested messaging changes
2. Update the highest-visibility canonical surfaces first
3. Propagate changes to corresponding partials and secondary pages
4. Validate links, assets, and language swaps before release

## Major Components

1. **Entry pages** — full HTML documents at repo root and under `products/`
2. **Localized partials** — HTMX-loaded NL/EN content fragments under `partials/`
3. **Shared presentation layer** — `styles.css`, image/video assets, and page-specific inline styles
4. **Shared behavior layer** — `projector.js`, cookie consent, and inline page bootstraps

## Data / Content Flow

- Browser loads a static page shell
- User may switch language, which swaps `#page-wrapper` with a localized partial
- Business content therefore exists in both the full-page shell family and the partial family
- Any product-story update must account for both storage locations

## Build Order Guidance

- First map change hotspots for homepage, pricing, mobile-product pages, and removable sections
- Then update `IAM mobiel` package framing and terminology in the core selling pages
- Then remove stale sections and resolve image issues
- Finish with bilingual parity and regression checks

## Architecture Risks

- Relative path mistakes between root pages and nested product pages
- Structural divergence between full pages and partials
- Global JS re-initialization issues after HTMX swaps if markup changes unexpectedly

## Roadmap Implications

- A dedicated cleanup / release phase is justified
- Requirements should map by content surface, not by technical subsystem
