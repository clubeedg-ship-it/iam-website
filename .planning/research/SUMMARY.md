# Project Research Summary

**Project:** IAM Website Repositioning
**Domain:** Brownfield bilingual marketing website refresh
**Researched:** 2026-04-01
**Confidence:** HIGH

## Executive Summary

This is not a stack-selection project. It is a brownfield website correction and repositioning effort on top of a static HTML/HTMX site that already works. The business need is to align the public website with the current product story, especially around `IAM mobiel`, while removing stale claims and keeping Dutch and English content synchronized.

The recommended approach is to keep the current stack, identify the affected file families, update high-visibility selling surfaces first, then propagate the changes through duplicated product and partial content. The main risk is not technical capability but inconsistent rollout across duplicated files, routes, and languages.

## Key Findings

### Recommended Stack

Keep the current static site architecture and use repo-local editing plus targeted audits as the delivery method.

**Core technologies:**
- HTML pages and partials: published content surface — already deployed and low-risk to retain
- CSS in `styles.css`: shared styling layer — sufficient for the refresh
- Vanilla JS + HTMX: interaction and language swapping — already integrated and proven in this codebase

### Expected Features

**Must have (table stakes):**
- Accurate homepage and product positioning
- Clear `IAM mobiel` package ladder
- Working bilingual parity on edited pages
- Valid contact paths, navigation, and media on all changed routes

**Should have (competitive):**
- Stronger package naming and cleaner value language
- More credible product visuals

**Defer (v2+):**
- CMS adoption
- major redesign
- broader content system refactor

### Architecture Approach

Work by content surface and file family: homepage and brand framing first, package/pricing content second, product-detail cleanup third, and bilingual hardening last. This order respects the current architecture, where the same public message is duplicated across entry pages and partials.

**Major components:**
1. Entry pages — root and `products/` HTML documents
2. Localized partials — HTMX swap content for NL/EN
3. Shared assets and scripts — styling, media, and global behavior

### Critical Pitfalls

1. **Partial update rollout** — audit every old phrase across file families before calling the refresh done
2. **Unclear package logic** — define `solo`, `duo`, and `premium` before broad copy cleanup
3. **Asset credibility gaps** — replace or remove weak housing photos instead of leaving them live
4. **Over-editing the stack** — keep this focused on content and safe structure
5. **Broken links after removals** — verify navigation and route references at the end

## Implications for Roadmap

### Phase 1: Safe Update Surface
**Rationale:** The repo duplicates content heavily; change safety comes first.
**Delivers:** A canonical change inventory and route/link safety baseline.
**Addresses:** content consistency and release risk.

### Phase 2: Brand and Homepage Repositioning
**Rationale:** Highest-visibility message correction should land early.
**Delivers:** Updated homepage framing, FAQ, and umbrella naming.

### Phase 3: IAM Mobiel Offer Refresh
**Rationale:** Package structure must be correct before supporting pages are polished.
**Delivers:** `solo`, `duo`, and `premium` product-story alignment.

### Phase 4: Product Cleanup
**Rationale:** Detailed claims, counts, and visuals can be updated once package framing is fixed.
**Delivers:** Corrected product-page messaging and image quality.

### Phase 5: Bilingual Sync and Release Hardening
**Rationale:** Final verification should catch stale copy, broken links, and unsynced language variants.
**Delivers:** Release-ready bilingual consistency.

### Phase Ordering Rationale

- The order reduces brownfield regression risk.
- Package positioning precedes detailed page cleanup.
- Final hardening is explicit because duplicate NL/EN content is the main failure mode.

### Research Flags

Phases likely needing deeper research during planning:
- **Phase 3:** exact approved package wording and price presentation if the spreadsheet is not the final commercial source
- **Phase 4:** available replacement imagery or retouch workflow for housing photos

Phases with standard patterns:
- **Phase 1:** file-family inventory and phrase audit
- **Phase 5:** route and bilingual regression verification

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack | HIGH | Fully visible in repo and stable for this scope |
| Features | MEDIUM | Spreadsheet is strong but still operational input, not a product spec |
| Architecture | HIGH | Brownfield file structure is well understood from codebase map |
| Pitfalls | HIGH | Risks are directly observable in duplicated content model |

**Overall confidence:** HIGH

### Gaps to Address

- Confirm final approved package wording if commercial text changes during execution
- Confirm replacement assets for image cleanup before committing to retouch vs removal

## Sources

### Primary (HIGH confidence)
- `.planning/codebase/STACK.md` — current implementation stack
- `.planning/codebase/ARCHITECTURE.md` — brownfield content structure
- `website-adjustments.xlsx` — requested business and content changes

### Secondary (MEDIUM confidence)
- Repository content audit via `rg` on legacy phrases and counts

---
*Research completed: 2026-04-01*
*Ready for roadmap: yes*
