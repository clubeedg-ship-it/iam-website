# Phase 2: Brand and Homepage Repositioning - Context

**Gathered:** 2026-04-01 (assumptions mode, auto)
**Status:** Ready for planning

<domain>
## Phase Boundary

Update the highest-visibility pages so visitors immediately get the current IAM message. Scope covers homepage (index), prijzen, and over-ons — not product detail pages (Phase 4). Changes must land in all three file-family members (shell + NL partial + EN partial) per page.

</domain>

<decisions>
## Implementation Decisions

### Homepage Product Image (HOME-01)
- **D-01:** Replace the inline SVG monitor icon in the 2-in-1 product card (yellow-tinted box) with an actual product photo of the 2-in-1 housing
- **D-02:** Candidate images exist at `media/products/2in1/1.png` through `4.png` — use whichever best shows the housing. If none are suitable, flag as blocked pending asset from stakeholder
- **D-03:** Apply the image change in all three files: `index.html` (~line 298), `partials/index-nl.html` (~line 188), `partials/index-en.html` (~line 187)

### Homepage FAQ (HOME-02)
- **D-04:** Replace the 4th FAQ item question from "Hoeveel spellen zijn er beschikbaar?" / "How many games are available?" to "Hoeveel interactieve programma's zijn er beschikbaar?" / "How many interactive programs are available?"
- **D-05:** Replace the 4th FAQ answer with the approved text from the change brief: "The number of available programs depends on the product and the selected package. Our interactive wall and floor offer a wide range of programs, while the interactive sandbox has its own selection. Please contact us for an overview that fits your situation."
- **D-06:** NL FAQ answer translation: "Het aantal beschikbare programma's hangt af van het product en het gekozen pakket. Onze interactieve wand en vloer bieden een breed scala aan programma's, terwijl de interactieve zandbak een eigen selectie heeft. Neem contact met ons op voor een overzicht dat past bij uw situatie."
- **D-07:** Apply FAQ changes in `index.html` (~line 574), `partials/index-nl.html` (~line 463), `partials/index-en.html` (~line 458)

### Brand Terminology — Homepage (BRND-01, BRND-02, BRND-03)
- **D-08:** On the homepage, change "Spellen Beschikbaar" → "Programma's Beschikbaar" / "Games Available" → "Programs Available" in the stat counter
- **D-09:** On the homepage product card description, replace "games/spellen" references with "programs/programma's"
- **D-10:** "free updates" / "gratis updates" does NOT appear on the homepage — no action needed for that phrase on this page

### Brand Terminology — Prijzen & Over Ons (BRND-03)
- **D-11:** On prijzen.html family (~11 "spellen" occurrences per partial), replace "spellen/games" with "programma's/programs" where it refers to the software offering
- **D-12:** On over-ons.html family (~5 "spellen" occurrences per partial), apply the same terminology shift
- **D-13:** Do NOT touch product detail pages (interactieve-vloer, interactieve-muur, etc.) — those belong to Phase 4

### NL/EN Sync Strategy
- **D-14:** Every content change applies to exactly 3 files per page family: shell (NL default) + NL partial + EN partial
- **D-15:** Shell page and NL partial must contain identical content — they are the same NL copy in two locations
- **D-16:** Plan 02-03 explicitly handles a final sync pass to verify no drift was introduced

### Claude's Discretion
- Exact image choice from the available 2in1 PNGs (or webp equivalents)
- Formatting and spacing adjustments in the FAQ section
- Minor wording polish in NL translation of FAQ answer if needed for natural Dutch

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Change brief
- `.planning/phases/01-safe-update-surface/change-brief.md` — Parsed spreadsheet with exact replacement text for homepage FAQ, product image instructions, and terminology changes
- `website-adjustments.xlsx` — Original source (change-brief.md is the structured derivative)

### Phase 1 inventory
- `.planning/phases/01-safe-update-surface/inventory.md` — File family listing with shell/NL/EN paths and drift flags

### Homepage files (primary edit targets)
- `index.html` — Shell page, NL default content
- `partials/index-nl.html` — NL partial for HTMX swap
- `partials/index-en.html` — EN partial for HTMX swap

### Secondary edit targets
- `prijzen.html`, `partials/prijzen-nl.html`, `partials/prijzen-en.html` — Pricing page family
- `over-ons.html`, `partials/over-ons-nl.html`, `partials/over-ons-en.html` — About page family

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `tools/phrase-audit.sh` — Can be run after edits to verify "games/spellen" removal progress on affected pages
- Phase 1 inventory confirms no structural drift exists, so file-by-file editing is safe

### Established Patterns
- Three-file family pattern: shell + NL partial + EN partial (shell == NL content)
- FAQ section uses `<details>` + `<summary>` elements with `faq-item` class
- Product cards use inline SVG icons with background-tinted containers
- Stat counters use JS-driven counter animation with data attributes

### Integration Points
- Homepage product card links to product detail pages — link targets must stay valid
- FAQ content is static HTML (no CMS or data source) — direct markup editing
- Stat counter numbers may need updating if "100+" changes to "60+" (but this is Phase 4 scope for product pages)

</code_context>

<specifics>
## Specific Ideas

- FAQ answer text is approved verbatim in the change brief — use exactly as specified
- "2-in-1" as a hardware description is preserved; "IAM mobiel" replaces it as the product line brand name
- The yellow-tinted SVG placeholder is the specific visual to replace with a real photo

</specifics>

<deferred>
## Deferred Ideas

- Product detail page terminology changes (interactieve-vloer, interactieve-muur, etc.) — Phase 4
- "free updates" / "gratis updates" removal on product pages — Phase 4
- "Choose Your Package" section removal — Phase 5
- Page deletions (bouw-een-park, 3d-spellen, interactieve-klimwand) — Phase 5
- Interactive floor movie change (row 41, blocked pending asset) — Phase 4

</deferred>

---

*Phase: 02-brand-and-homepage-repositioning*
*Context gathered: 2026-04-01*
