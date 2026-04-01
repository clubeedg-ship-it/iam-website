---
phase: 03-iam-mobiel-package-refresh
plan: 02
subsystem: ui
tags: [html, static-site, pricing, localization, iam-mobiel]
requires:
  - phase: 03-iam-mobiel-package-refresh
    provides: "IAM mobiel solo/duo/premium taxonomy and headings across pricing and product families"
provides:
  - "Approved IAM mobiel package pricing anchors across pricing and product families"
  - "Package-aware solo, duo, and premium value language with 60+ and 120+ counts"
  - "Removal of free-updates messaging from the mobile package story"
affects: [phase-03-validation, pricing, product-copy, bilingual-parity]
tech-stack:
  added: []
  patterns: [family-wide static HTML copy sync across shell, NL partial, and EN partial]
key-files:
  created: [.planning/phases/03-iam-mobiel-package-refresh/03-02-SUMMARY.md]
  modified:
    - prijzen.html
    - partials/prijzen-nl.html
    - partials/prijzen-en.html
    - products/2-in-1-vloer-muur.html
    - partials/products/2-in-1-vloer-muur-nl.html
    - partials/products/2-in-1-vloer-muur-en.html
key-decisions:
  - "Kept custom-quote wording only on the software row while fixing the IAM mobiel package ladder to explicit price anchors."
  - "Treated the 2-in-1 product page as a duo-led sales surface while preserving 2-in-1 as the hardware descriptor."
patterns-established:
  - "Pricing and product families must repeat the same package facts across shell, NL partial, and EN partial in the same execution pass."
  - "Mobile-line copy now uses included software and no-subscription language instead of free-updates messaging."
requirements-completed: [MOBL-01, MOBL-02, MOBL-03]
duration: 6m
completed: 2026-04-01
---

# Phase 3 Plan 02: IAM Mobiel Package Refresh Summary

**IAM mobiel pricing anchors and package-story copy now align across pricing and 2-in-1 product families with approved solo, duo, and premium distinctions**

## Performance

- **Duration:** 6m
- **Started:** 2026-04-01T23:31:05+02:00
- **Completed:** 2026-04-01T21:37:23Z
- **Tasks:** 2
- **Files modified:** 6

## Accomplishments

- Rewrote the pricing family so `IAM mobiel solo`, `IAM mobiel duo`, and `IAM mobiel premium` expose the approved package meanings and price anchors.
- Updated the `2-in-1-vloer-muur` family to sell the dual-use mobile offer with `120+` program counts, included-software language, and package-aware FAQ answers.
- Removed stale package-story wording such as `Op aanvraag / On request` on the mobile ladder and `gratis updates / free updates` on the product-family sales surfaces.

## Task Commits

Each task was committed atomically:

1. **Task 1: Apply approved package descriptions and price anchors on the pricing family** - `5e6f574` (feat)
2. **Task 2: Rewrite product-family value language, counts, and package details** - `b890199` (feat)

## Files Created/Modified

- `prijzen.html` - updated pricing shell comparison rows and package cards to the approved IAM mobiel ladder.
- `partials/prijzen-nl.html` - synchronized Dutch pricing partial with the same package facts and anchors.
- `partials/prijzen-en.html` - synchronized English pricing partial with matching package facts and EN number formatting.
- `products/2-in-1-vloer-muur.html` - rewrote hero, value language, specs, package cards, FAQ, and CTA support copy for the duo-led mobile story.
- `partials/products/2-in-1-vloer-muur-nl.html` - synchronized Dutch product partial with the corrected package story.
- `partials/products/2-in-1-vloer-muur-en.html` - synchronized English product partial with the corrected counts and no-subscription language.

## Decisions Made

- Kept tailored quote wording only for software/custom work, because the plan locks explicit pricing for the package ladder but still allows broader custom-solution language.
- Kept `2-in-1` in hardware-description positions while shifting commercial package surfaces to `IAM mobiel`, matching the Phase 3 context decisions.

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

None.

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Phase 3 now has both taxonomy and package-detail copy in place for the pricing and mobile-product families.
- `03-03` can focus on parity verification, stale-phrase audits, and any residual cleanup on the refreshed package surfaces.

## Self-Check: PASSED

---
*Phase: 03-iam-mobiel-package-refresh*
*Completed: 2026-04-01*
