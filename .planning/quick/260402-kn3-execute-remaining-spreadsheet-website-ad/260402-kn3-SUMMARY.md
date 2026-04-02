---
phase: quick
plan: kn3
subsystem: website-content
tags: [content-correction, product-cleanup, climbing-wall-removal]
dependency_graph:
  requires: []
  provides: [accurate-product-claims, clean-navigation]
  affects: [all-site-pages, product-pages, pricing, partials]
tech_stack:
  added: []
  patterns: []
key_files:
  created: []
  modified:
    - partials/products/interactieve-vloer-en.html
    - partials/products/interactieve-vloer-nl.html
    - products/interactieve-vloer.html
    - partials/products/interactieve-muur-en.html
    - partials/products/interactieve-muur-nl.html
    - products/interactieve-muur.html
    - partials/products/interactieve-zandbak-en.html
    - partials/products/interactieve-zandbak-nl.html
    - products/interactieve-zandbak.html
    - partials/products/software-maatwerk-en.html
    - partials/products/software-maatwerk-nl.html
    - products/software-maatwerk.html
  deleted:
    - products/interactieve-klimwand.html
    - partials/products/interactieve-klimwand-en.html
    - partials/products/interactieve-klimwand-nl.html
decisions:
  - "Changed wall terminology from 'games/spellen' to 'programs/programma''s' for content-count references only, preserving metaphorical uses"
  - "Removed 'free updates' promises entirely rather than replacing with weaker claims"
  - "Stripped Klimwand from software compatibility lists to maintain accurate product catalog"
metrics:
  duration: ~13min
  completed: "2026-04-02T12:55:00Z"
  tasks: 2
  files: 67
---

# Quick Task kn3: Execute Remaining Spreadsheet Website Adjustments

Correct outdated product claims across 6 spreadsheet tasks, removing false "free updates" promises, fixing wall game counts from 100+ to 60+ with terminology change to "programs", deleting package sections from sandbox and software pages, and fully removing the discontinued climbing wall product with sitewide nav cleanup across 55+ files.

## Task Results

### Task 1: Fix product content (5d3b50a)

**A. Interactive Floor -- removed "free updates"**
- Deleted the "gratis updates" / "free updates" subtitle line from the Game Library Preview section in all 3 floor file variants (EN partial, NL partial, canonical)

**B. Interactive Wall -- 100+ to 60+ and free updates removal**
- Replaced all "100+" instances with "60+" across hero highlights, benefit badges, spec descriptions, spec tables, package features, and FAQ sections
- Removed all "free updates" / "gratis updates" / "& free updates" language from hero highlights, spec descriptions, and FAQ answers
- Changed the FAQ about new games/updates to a neutral statement about availability

**C. Interactive Wall -- games to programs terminology**
- Changed "games" to "programs" and "spellen" to "programma's" in all content-count/library references
- Updated headings: "Game Library" to "Program Library", "Spelbibliotheek" to "Programmabibliotheek"
- Updated spec labels: "Number of Games" to "Number of Programs", "Aantal Spellen" to "Aantal Programma's"
- Preserved metaphorical uses like testimonial quotes and generic marketing language

**D. Interactive Sandbox -- removed package section**
- Deleted the entire "Choose Your Package" / "Kies Uw Pakket" section (3 cards: Essential, Professional, Enterprise) from EN partial, NL partial, and canonical page

**E. Software & Custom -- removed package section**
- Deleted the identical package section from all 3 software-maatwerk file variants

### Task 2: Delete climbing wall and sitewide cleanup (54c4030)

**Deleted 3 files:**
- `products/interactieve-klimwand.html`
- `partials/products/interactieve-klimwand-en.html`
- `partials/products/interactieve-klimwand-nl.html`

**Removed references from 55 HTML files:**
- Desktop nav dropdown links (all root pages + product pages + partials)
- Mobile nav links (same scope)
- Footer product links (all pages with footers)
- Related product cards on wall and 2-in-1 pages (6 file variants)
- Software compatibility text: removed "Klimwand" / "Climbing Wall" from system lists in 6 file variants
- Build-a-park hotspot section and subtitle text (canonical + NL/EN partials)
- Park package examples: removed "1x Interactieve Klimwand" lines (canonical + NL/EN partials)
- Pricing table row: removed climbing wall product row (canonical + NL/EN partials)
- Homepage content cards: removed climbing wall product card (NL/EN partials)
- Inline copy: updated "vloeren, muren, zandbakken en klimwanden" to "vloeren, muren en zandbakken" (and EN equivalent)

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing content consistency] Additional wall terminology in FAQ and feature lists**
- **Found during:** Task 1
- **Issue:** The plan listed approximately 6 instances of "100+" and 3 of "free updates" in the EN wall file, but the NL partial and canonical page had additional instances in FAQ answers ("Krijg ik nieuwe games na aankoop?"), feature lists ("Regelmatig nieuwe spellen via updates"), and spec titles ("Spelbibliotheek")
- **Fix:** Applied the same games-to-programs and free-updates-removal treatment to all matching instances across all 3 wall file variants
- **Files modified:** All 3 wall files

**2. [Rule 2 - Content consistency] Software page Klimwand references in compatibility text**
- **Found during:** Task 2
- **Issue:** Software/custom pages had "Klimwand" in 3 inline text locations per file variant (spec description, spec table value, FAQ answer) beyond just nav/footer links
- **Fix:** Updated text to remove Klimwand from the product lists while maintaining grammatical correctness
- **Files modified:** products/software-maatwerk.html, partials/products/software-maatwerk-nl.html, partials/products/software-maatwerk-en.html

## Verification Results

All 5 verification checks passed:
1. Zero "free updates" / "gratis updates" in floor files
2. Zero "100+" in wall files
3. Zero "Choose Your Package" / "Kies Uw Pakket" in sandbox and software files
4. Zero climbing wall references in any live HTML file (excluding .claude/, .planning/, tools/)
5. Wall EN partial confirmed showing "60+ programs"

## Known Stubs

None -- all changes are content corrections and removals, no new data sources or UI components introduced.

## Self-Check: PASSED
