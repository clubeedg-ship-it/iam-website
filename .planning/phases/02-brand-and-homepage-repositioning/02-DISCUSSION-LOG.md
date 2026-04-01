# Phase 2: Brand and Homepage Repositioning - Discussion Log (Assumptions Mode)

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions captured in CONTEXT.md — this log preserves the analysis.

**Date:** 2026-04-01
**Phase:** 02-Brand and Homepage Repositioning
**Mode:** assumptions (auto)
**Areas analyzed:** Homepage Product Image, Homepage FAQ, Brand Terminology, NL/EN Sync

## Assumptions Presented

### Homepage Product Image Update
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Replace inline SVG monitor icon in yellow-tinted box with real 2-in-1 housing photo from media/products/2in1/*.png | Likely | index.html:298-305, partials/index-nl.html:188-195, partials/index-en.html:187-194, change-brief.md row 0 |

### Homepage FAQ Replacement
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Replace 4th FAQ item (question + answer) in all 3 homepage files with approved text from change brief | Confident | index.html:574, partials/index-nl.html:463, partials/index-en.html:458, change-brief.md lines 89-93 |

### Brand Terminology Corrections
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Phase 2 scope limited to homepage + prijzen + over-ons; product pages deferred to Phase 4 | Likely | ROADMAP Phase 2 vs Phase 4 scoping, grep: ~10 homepage hits, ~11 prijzen hits, ~5 over-ons hits, zero "free updates" on homepage |

### NL/EN Sync Strategy
| Assumption | Confidence | Evidence |
|------------|-----------|----------|
| Apply every change to 3 files per family (shell + NL + EN), shell and NL must stay identical | Confident | Phase 1 inventory: NO drift across 20 families, visible duplication in index.html vs partials/index-nl.html |

## Corrections Made

No corrections — auto mode selected recommended defaults for all assumptions.

## Auto-Resolved

- Homepage Product Image: auto-selected recommended approach (use existing media/products/2in1/ assets)
- Brand Terminology scope: auto-selected homepage + prijzen + over-ons only (defer product pages to Phase 4)
