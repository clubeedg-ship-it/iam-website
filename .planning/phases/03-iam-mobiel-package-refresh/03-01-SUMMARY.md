---
phase: 03-iam-mobiel-package-refresh
plan: 01
subsystem: pricing-and-mobile-taxonomy
tags: [iam-mobiel, package-taxonomy, pricing, product-page, bilingual]
dependency_graph:
  requires: []
  provides: [iam-mobiel-package-taxonomy, duo-highlighted, product-family-reframed]
  affects:
    - prijzen.html
    - partials/prijzen-nl.html
    - partials/prijzen-en.html
    - products/2-in-1-vloer-muur.html
    - partials/products/2-in-1-vloer-muur-nl.html
    - partials/products/2-in-1-vloer-muur-en.html
tech_stack:
  added: []
  patterns: [three-file-family-sync, taxonomy-first-package-refresh]
key_files:
  created:
    - ".planning/phases/03-iam-mobiel-package-refresh/03-01-SUMMARY.md"
  modified:
    - "prijzen.html"
    - "partials/prijzen-nl.html"
    - "partials/prijzen-en.html"
    - "products/2-in-1-vloer-muur.html"
    - "partials/products/2-in-1-vloer-muur-nl.html"
    - "partials/products/2-in-1-vloer-muur-en.html"
decisions:
  - "Used `IAM mobiel` / `IAM mobile` in package-story headings while preserving `2-in-1` for hardware references"
  - "Replaced legacy package-tier names before touching detailed pricing/count copy"
metrics:
  completed: "2026-04-01T21:18:49Z"
  tasks_completed: 2
  tasks_total: 2
  files_modified: 6
---

# Phase 03 Plan 01: Package Taxonomy and Heading Refresh Summary

Reframed the pricing and `2-in-1-vloer-muur` families around `IAM mobiel solo`, `IAM mobiel duo`, and `IAM mobiel premium` so the mobile line now has a visible package taxonomy before the detailed commercial rewrite.

## Tasks Completed

### Task 1: Replace legacy package taxonomy on pricing page family
- Updated the pricing package section heading from a generic included-features framing to `IAM mobiel pakketten` / `IAM mobile packages`
- Renamed package cards from `Essential`, `Professional`, and `Enterprise` to `IAM mobiel solo`, `IAM mobiel duo`, and `IAM mobiel premium`
- Rewrote the package taglines to reflect the approved single-surface, dual-use, and personalized-package framing
- Kept the featured-card emphasis on the middle option so `duo` remains the most-selected package
- Updated the pricing testimonial to reference the `IAM mobiel duo` package instead of the removed `Professional` tier

### Task 2: Reframe the current 2-in-1 product page family around IAM mobiel package headings
- Changed the product badge to `IAM mobiel` / `IAM mobile`
- Renamed the package section to `Kies uw IAM mobiel pakket` / `Choose your IAM mobile package`
- Replaced the package card names with `solo`, `duo`, and `premium`
- Updated the package subtitles so the section now reads as an `IAM mobiel` offer ladder while still keeping `2-in-1` in the section subtitle as a hardware reference
- Updated the installation FAQ answer and sticky CTA label so they no longer refer back to removed package-tier names

## Verification Results

- `rg -n "IAM mobiel solo|IAM mobiel duo|IAM mobiel premium|IAM mobile solo|IAM mobile duo|IAM mobile premium"` returns expected matches across both refreshed families
- `rg -n "Essential|Professional|Enterprise|Kies Uw Pakket|Choose Your Package"` returns no matches in the refreshed pricing and product surfaces
- Product-family badge, package heading, and sticky CTA now use `IAM mobiel` / `IAM mobile`
- No route or file naming changes were introduced; `2-in-1` remains in hardware-facing contexts

## Deviations from Plan

### [Rule 1 - Bug] Removed legacy audit collisions from footer comments and English feature labels
- **Found during:** Acceptance-criteria verification
- **Issue:** The legacy-tier audit still matched `Professional` in footer comments and generic English feature labels, causing the automated plan verification to fail even though the package headings were updated
- **Fix:** Renamed footer comments to `Site Footer` and changed English feature text from `Professional installation` to `Installed by IAM specialists`
- **Files modified:** `prijzen.html`, `partials/prijzen-nl.html`, `partials/prijzen-en.html`, `partials/products/2-in-1-vloer-muur-en.html`
- **Verification:** Re-ran the legacy-tier grep and confirmed zero remaining matches

**Total deviations:** 1 auto-fixed  
**Impact:** Low. The deviation only aligned support text and comments with the plan's verification rules.

## Known Stubs

- Detailed price anchors, `60+ / 120+` counts, and `gratis updates / free updates` removal are intentionally deferred to `03-02`
- Human visual verification is deferred to `03-03`

## Self-Check: PASSED
