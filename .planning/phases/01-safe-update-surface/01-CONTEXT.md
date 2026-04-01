# Phase 1: Safe Update Surface - Context

**Gathered:** 2026-04-01 (assumptions mode)
**Status:** Ready for planning

<domain>
## Phase Boundary

Inventory all affected file families and establish a safe baseline for brownfield edits. This phase produces documentation and audit tooling — it does not modify the live site. Downstream phases (2–5) consume this inventory to make safe, coordinated edits.

</domain>

<decisions>
## Implementation Decisions

### Inventory Scope
- **D-01:** Inventory every page family on the site, not just the ones explicitly named in the spreadsheet — nav drift means any file could be affected by removal or restructuring
- **D-02:** Each file family entry captures: shell page path, NL partial path, EN partial path, and a flag noting whether nav/content has drifted between shell and partial
- **D-03:** Orphaned partials (`partials/content-nl.html`, `partials/content-en.html`) are flagged separately as cleanup candidates

### Legacy Phrase Audit
- **D-04:** Produce a reusable grep-based audit (shell script or markdown with grep commands) that can be re-run after each phase lands — not a one-shot snapshot
- **D-05:** Target phrases: `games`, `free updates` / `gratis updates`, `100+`, `Choose Your Package` / `Kies Uw Pakket` / `Kies Jouw Pakket`, `2-in-1`
- **D-06:** Audit output groups results by file family (not by phrase) so editors see all changes needed per file in one place

### Removal Planning
- **D-07:** Document removal candidates with their full dependency graph: which nav items, footer links, and sitemap entries reference them across all 48 HTML files
- **D-08:** Confirmed removal investigation targets: `bouw-een-park.html` family (3 files), `3d-spellen.html` family (3 files), "Choose Your Package" / "Kies Uw/Jouw Pakket" sections in 12 product partials — final removal decision deferred to Phase 5 after spreadsheet confirmation
- **D-09:** Orphaned partials (`content-nl.html`, `content-en.html`) are safe to remove since no shell page references them

### Spreadsheet Parsing
- **D-10:** Parse `website-adjustments.xlsx` into structured markdown during this phase so all downstream phases have a machine-readable change list — do not defer spreadsheet interpretation to later phases

### Claude's Discretion
- Output file format and naming for the inventory document
- Exact grep patterns and script structure for the phrase audit
- Level of detail in the route dependency map

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Change brief
- `website-adjustments.xlsx` — Authoritative source for all requested content changes, removals, and repositioning directives

### Codebase maps
- `.planning/codebase/STRUCTURE.md` — File layout and page family naming conventions
- `.planning/codebase/CONCERNS.md` — Content duplication risks and recommended attention order
- `.planning/codebase/CONVENTIONS.md` — Path conventions (root vs product vs partial relative paths)

### Requirements
- `.planning/REQUIREMENTS.md` — QLTY-01 and QLTY-02 acceptance criteria for this phase

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `tools/migrate_i18n.py` — Existing partial generation script; demonstrates how shell-to-partial extraction works, could inform inventory structure

### Established Patterns
- Three-file family pattern: shell page + NL partial + EN partial (e.g., `index.html` + `partials/index-nl.html` + `partials/index-en.html`)
- Product families add path depth: `products/mobiele-vloer.html` + `partials/products/mobiele-vloer-nl.html` + `partials/products/mobiele-vloer-en.html`
- Navigation is hand-duplicated in every file (desktop nav, mobile nav, footer) — no shared include mechanism
- Shell pages and partials have already drifted (e.g., `index.html` nav differs from `partials/index-nl.html` nav)

### Integration Points
- Legacy phrases are concentrated in partials (238 "games" occurrences across 26 files, "gratis updates" in 6 product partials)
- Navigation references span all 48 HTML files — removal of any page requires updating desktop nav, mobile nav, and footer in every file
- `sitemap.xml` and `robots.txt` reference routes that may change if pages are removed

</code_context>

<specifics>
## Specific Ideas

No specific requirements — open to standard approaches

</specifics>

<deferred>
## Deferred Ideas

None — analysis stayed within phase scope

</deferred>

---

*Phase: 01-safe-update-surface*
*Context gathered: 2026-04-01*
