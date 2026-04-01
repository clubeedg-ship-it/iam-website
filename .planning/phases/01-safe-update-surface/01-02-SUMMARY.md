---
phase: 01-safe-update-surface
plan: 02
subsystem: documentation
tags: [phrase-audit, route-dependencies, removal-planning, audit-tooling]

requires: [01-01]
provides:
  - "Reusable phrase audit script covering 9 legacy phrase patterns"
  - "Route dependency map for 4 removal candidates across 62 HTML files"
  - "Pre-existing broken link baseline (2 broken links found)"
affects: [02-*, 03-*, 04-*, 05-*]

tech-stack:
  added: []
  patterns:
    - "Bash grep-based audit script with family-grouped output"
    - "Clean URL dependency mapping via server.js route table"

key-files:
  created:
    - ".planning/phases/01-safe-update-surface/tools/phrase-audit.sh"
    - ".planning/phases/01-safe-update-surface/removal-deps.md"
  modified: []

key-decisions:
  - "Site uses clean URLs via server.js route table -- dependency mapping uses clean URL patterns"
  - "Found 2 pre-existing broken links (/horeca-events, /terms) as QLTY-01 baseline"
  - "interactieve-klimwand added as removal candidate based on spreadsheet row 46"

patterns-established:
  - "Audit script outputs both per-family detail and summary mode (--summary flag)"
  - "Route dependency map includes desktop nav, mobile nav, footer, and sitemap references"

requirements-completed: [QLTY-01, QLTY-02]

duration: 6min
completed: 2026-04-01
---

# Phase 01 Plan 02: Phrase Audit & Route Dependency Map Summary

**Reusable phrase audit script for 9 legacy patterns plus complete route dependency map for 4 removal candidates across 62 HTML files**

## Performance

- **Duration:** 6 min
- **Started:** 2026-04-01T18:25:00Z
- **Completed:** 2026-04-01T18:31:00Z
- **Tasks:** 2/2
- **Files created:** 2

## Accomplishments

### Task 1: Reusable Legacy Phrase Audit Script

Created `tools/phrase-audit.sh` — an executable bash script that greps for 9 legacy phrase patterns across all HTML files (excluding `.planning/`). Features:
- Groups results by file family using the inventory from Plan 01-01
- Supports `--summary` flag for quick pass/fail overview
- Covers: `games`, `spellen`, `free updates`, `gratis updates`, `100+`, `Choose Your Package`, `Kies Uw Pakket`, `Kies Jouw Pakket`, `2-in-1` (as marketing term)
- Output designed for re-running after each phase to track cleanup progress

**Commit:** `a41a661`

### Task 2: Route Dependency Map for Removal Candidates

Created `removal-deps.md` mapping every reference to 4 removal candidates:
1. **bouw-een-park** — 73 href references across 39 files, sitemap entry, server.js routes
2. **3d-spellen** — 73 href references across 39 files, sitemap entry, server.js routes
3. **interactieve-klimwand** — 73 href references across 39 files (added per spreadsheet row 46)
4. **"Choose Your Package" / "Kies Uw/Jouw Pakket" sections** — found in 8 product partials

Also documented:
- 2 orphaned partials (content-nl.html, content-en.html) confirmed safe to remove
- 2 pre-existing broken links found (/horeca-events, /terms) as QLTY-01 baseline
- Clean URL mapping via server.js route table

**Commit:** `514ee4e`

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Clean URLs instead of .html paths**
- **Found during:** Task 2
- **Issue:** Plan assumed `.html` file references. Site uses `server.js` with clean URL routing.
- **Fix:** Mapped dependencies using clean URL patterns (`/bouw-een-park`, `/3d-spellen`) alongside `.html` file paths.
- **Files modified:** `removal-deps.md`
- **Commit:** `514ee4e`

## Known Stubs

None — both artifacts are complete with no placeholders.

## Self-Check: PASSED

- tools/phrase-audit.sh: FOUND (executable)
- removal-deps.md: FOUND
- 01-02-SUMMARY.md: FOUND
- Commit a41a661: FOUND
- Commit 514ee4e: FOUND
