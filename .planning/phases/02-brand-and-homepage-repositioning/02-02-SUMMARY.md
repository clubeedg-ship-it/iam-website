---
phase: 02-brand-and-homepage-repositioning
plan: 02
subsystem: content
tags: [terminology, bilingual, pricing, about, branding]

# Dependency graph
requires:
  - phase: 01-safe-update-surface
    provides: file-family inventory and drift detection baseline
provides:
  - "programma's/programs terminology on pricing and about page families"
  - "data-label attributes matching updated table headers on prijzen pages"
affects: [03-product-page-refresh, 04-mobile-line-repositioning]

# Tech tracking
tech-stack:
  added: []
  patterns: [shell-partial-parity, nav-link-preservation]

key-files:
  created: []
  modified:
    - prijzen.html
    - partials/prijzen-nl.html
    - partials/prijzen-en.html
    - over-ons.html
    - partials/over-ons-nl.html
    - partials/over-ons-en.html

key-decisions:
  - "Replaced Klim Games/Climbing Games with Klim Programma's/Climbing Programs in pricing table despite climbing page being Phase 5 scope"
  - "Preserved Game Development heading as proper noun describing team discipline"

patterns-established:
  - "Nav-link preservation: shell files contain nav links with Spellen/Games that reference the 3D page -- these must never be changed during content terminology updates"
  - "data-label parity: responsive table data-label attributes must match their column th text"

requirements-completed: [BRND-03]

# Metrics
duration: 5min
completed: 2026-04-01
---

# Phase 02 Plan 02: Pricing & About Terminology Summary

**Replaced spellen/games with programma's/programs across 6 files in the prijzen and over-ons page families, including table headers, data-labels, feature lists, and FAQ text**

## Performance

- **Duration:** 5 min
- **Started:** 2026-04-01T20:32:05Z
- **Completed:** 2026-04-01T20:36:49Z
- **Tasks:** 2
- **Files modified:** 6

## Accomplishments
- Replaced 11 occurrences per file across the 3-file prijzen family (shell, NL partial, EN partial)
- Replaced 5 occurrences per file across the 3-file over-ons family (shell, NL partial, EN partial)
- Preserved nav links to 3D Spellen/Games page and Game Development proper noun
- Updated data-label attributes on pricing table to match new column header

## Task Commits

Each task was committed atomically:

1. **Task 1: Replace spellen/games terminology on prijzen page family** - `54805d5` (feat)
2. **Task 2: Replace spellen/games terminology on over-ons page family** - `47b99c2` (feat)

## Files Created/Modified
- `prijzen.html` - Pricing shell: 11 content occurrences updated, nav links preserved
- `partials/prijzen-nl.html` - Pricing NL partial: all 11 spellen replaced with programma's
- `partials/prijzen-en.html` - Pricing EN partial: all 11 games replaced with programs
- `over-ons.html` - About shell: 5 content occurrences updated, nav links preserved
- `partials/over-ons-nl.html` - About NL partial: all 5 spellen replaced with programma's
- `partials/over-ons-en.html` - About EN partial: all 5 games replaced with programs, Game Development preserved

## Decisions Made
- Replaced "Klim Games" with "Klim Programma's" and "Climbing Games" with "Climbing Programs" in pricing table even though the climbing wall product page is Phase 5 scope -- the pricing table label should use current terminology now
- Preserved "Game Development" heading in over-ons-en.html as a proper noun describing the team's discipline

## Deviations from Plan

None - plan executed exactly as written.

Note: Plan estimated 6 data-label occurrences per prijzen file but actual count was 5 (the table has 5 product rows, not 6). All 5 were updated. This is a plan estimation variance, not a deviation.

## Issues Encountered
None

## User Setup Required
None - no external service configuration required.

## Next Phase Readiness
- Pricing and about pages now use current "programma's/programs" terminology
- Shell and partial content matches for both page families
- Ready for remaining Phase 02 plans and subsequent product page refreshes

---
*Phase: 02-brand-and-homepage-repositioning*
*Completed: 2026-04-01*
