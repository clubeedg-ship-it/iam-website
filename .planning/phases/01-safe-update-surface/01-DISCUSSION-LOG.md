# Phase 1: Safe Update Surface - Discussion Log (Assumptions Mode)

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions captured in CONTEXT.md — this log preserves the analysis.

**Date:** 2026-04-01
**Phase:** 01-Safe Update Surface
**Mode:** assumptions
**Areas analyzed:** File Family Structure, Legacy Phrase Distribution, Route and Navigation Dependencies, Removal Targets

## Assumptions Presented

### File Family Structure
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Each routable page follows a three-file family pattern (shell + NL partial + EN partial), with nav drift already present between shell and partials | Confident | `index.html` desktop nav differs from `partials/index-nl.html` nav (klimwand vs tekeningen, Prijzen placement, Verhuur link). `partials/content-nl.html` and `partials/content-en.html` are orphaned. |

### Legacy Phrase Distribution
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Legacy phrases are concentrated in partials (not shell pages): 238 "games" across 26 files, "gratis updates"/"free updates" in 6 product partials, "100+" in 14 files, "Choose Your Package" in 6 EN partials | Confident | Grep results across all HTML files |

### Route and Navigation Dependencies
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| `bouw-een-park.html` and `3d-spellen.html` appear in desktop nav, mobile nav, and footer across all 48 HTML files (266 total references) — removal requires coordinated update everywhere | Confident | Navigation is hand-duplicated in every file with no shared include mechanism |

### Removal Targets
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Removal candidates include `bouw-een-park` family (3 files), `3d-spellen` family (3 files), "Choose Your Package" sections in 12 product partials, and 2 orphaned content partials | Likely | PROD-03 requirement + grep results; final confirmation needs spreadsheet parsing |

## Corrections Made

No corrections — user requested autonomous execution with all decisions delegated to Claude.

## External Research

- Spreadsheet `website-adjustments.xlsx` needs parsing during execution to confirm removal targets against codebase inventory.
