# Phase 2: Brand and Homepage Repositioning - Research

**Researched:** 2026-04-01
**Domain:** Static HTML content editing -- brownfield terminology replacement and image swap
**Confidence:** HIGH

## Summary

Phase 2 is a targeted content editing phase across 9 HTML files (3 page families x 3 files each). The work involves: (1) replacing an SVG placeholder with a real product image on the homepage, (2) updating the homepage FAQ question and answer, (3) replacing "spellen/games" with "programma's/programs" in stat counters and product descriptions across homepage, prijzen, and over-ons page families.

All edit targets have been verified in the current codebase. The 2-in-1 product images exist at `media/products/2in1/1.png` through `4.png` and are suitable -- image 1 (3/4 angle view of the white housing on casters) is the best choice for the product card. There is no structural complexity; every change is a text or markup replacement in static HTML with no build step, no templating engine, and no data layer.

**Primary recommendation:** Execute changes file-family-by-file-family (index first, then prijzen, then over-ons), verifying NL/EN parity after each family. Use `grep` audits before and after to confirm all targeted occurrences are addressed without touching out-of-scope references (nav links to "3D Spellen" page, product detail pages).

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Replace the inline SVG monitor icon in the 2-in-1 product card (yellow-tinted box) with an actual product photo of the 2-in-1 housing
- **D-02:** Candidate images exist at `media/products/2in1/1.png` through `4.png` -- use whichever best shows the housing. If none are suitable, flag as blocked pending asset from stakeholder
- **D-03:** Apply the image change in all three files: `index.html` (~line 298), `partials/index-nl.html` (~line 188), `partials/index-en.html` (~line 187)
- **D-04:** Replace the 4th FAQ item question from "Hoeveel spellen zijn er beschikbaar?" / "How many games are available?" to "Hoeveel interactieve programma's zijn er beschikbaar?" / "How many interactive programs are available?"
- **D-05:** Replace the 4th FAQ answer with the approved text from the change brief: "The number of available programs depends on the product and the selected package. Our interactive wall and floor offer a wide range of programs, while the interactive sandbox has its own selection. Please contact us for an overview that fits your situation."
- **D-06:** NL FAQ answer translation: "Het aantal beschikbare programma's hangt af van het product en het gekozen pakket. Onze interactieve wand en vloer bieden een breed scala aan programma's, terwijl de interactieve zandbak een eigen selectie heeft. Neem contact met ons op voor een overzicht dat past bij uw situatie."
- **D-07:** Apply FAQ changes in `index.html` (~line 574), `partials/index-nl.html` (~line 463), `partials/index-en.html` (~line 458)
- **D-08:** On the homepage, change "Spellen Beschikbaar" to "Programma's Beschikbaar" / "Games Available" to "Programs Available" in the stat counter
- **D-09:** On the homepage product card description, replace "games/spellen" references with "programs/programma's"
- **D-10:** "free updates" / "gratis updates" does NOT appear on the homepage -- no action needed for that phrase on this page
- **D-11:** On prijzen.html family (~11 "spellen" occurrences per partial), replace "spellen/games" with "programma's/programs" where it refers to the software offering
- **D-12:** On over-ons.html family (~5 "spellen" occurrences per partial), apply the same terminology shift
- **D-13:** Do NOT touch product detail pages (interactieve-vloer, interactieve-muur, etc.) -- those belong to Phase 4
- **D-14:** Every content change applies to exactly 3 files per page family: shell (NL default) + NL partial + EN partial
- **D-15:** Shell page and NL partial must contain identical content -- they are the same NL copy in two locations
- **D-16:** Plan 02-03 explicitly handles a final sync pass to verify no drift was introduced

### Claude's Discretion
- Exact image choice from the available 2in1 PNGs (or webp equivalents)
- Formatting and spacing adjustments in the FAQ section
- Minor wording polish in NL translation of FAQ answer if needed for natural Dutch

### Deferred Ideas (OUT OF SCOPE)
- Product detail page terminology changes (interactieve-vloer, interactieve-muur, etc.) -- Phase 4
- "free updates" / "gratis updates" removal on product pages -- Phase 4
- "Choose Your Package" section removal -- Phase 5
- Page deletions (bouw-een-park, 3d-spellen, interactieve-klimwand) -- Phase 5
- Interactive floor movie change (row 41, blocked pending asset) -- Phase 4
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| BRND-01 | Visitor sees `IAM mobiel` presented as the umbrella name for the mobile product line on primary selling pages | D-09: Homepage product card description updates. Note: The homepage flagship card heading says "2-in-1 Interactieve Vloer & Muur" which is the hardware description, not the brand name. Full IAM mobiel branding is Phase 3 scope (MOBL-*). Phase 2 addresses terminology shift (spellen->programma's) which supports the rebranding groundwork. |
| BRND-02 | Visitor is not misled into thinking every mobile variant is generically a `2-in-1` product | D-01/D-02/D-03: Replacing the generic SVG icon with a real product photo shows the actual housing rather than an abstract icon. The "2-in-1" label under it remains accurate as a hardware description per the change brief. |
| BRND-03 | Visitor sees current value language such as `programs` and `no license costs` where the refresh requires it | D-08 (stat counter), D-09 (product card), D-11 (prijzen ~11 occurrences), D-12 (over-ons ~5 occurrences): systematic "spellen/games" to "programma's/programs" replacement across homepage, pricing, and about pages. |
| HOME-01 | Homepage products section shows the updated real image of the mobile housing instead of the outdated yellow-square visual | D-01/D-02/D-03: Replace SVG+yellow-bg container with `<img>` tag referencing `media/products/2in1/1.png`. Verified image exists (1MB PNG, shows white housing on casters at 3/4 angle). |
| HOME-02 | Homepage FAQ asks how many interactive programs are available and shows the approved answer | D-04/D-05/D-06/D-07: Exact replacement text is approved and locked. Apply to 3 files in the index family. |
</phase_requirements>

## Architecture Patterns

### Three-File Family Pattern
Every page change must be applied to exactly 3 files:

| Role | Path Pattern (root) | Path Pattern (products) | Content Language |
|------|---------------------|------------------------|-----------------|
| Shell | `{page}.html` | `products/{page}.html` | NL (default) |
| NL Partial | `partials/{page}-nl.html` | `partials/products/{page}-nl.html` | NL |
| EN Partial | `partials/{page}-en.html` | `partials/products/{page}-en.html` | EN |

Shell and NL partial contain identical NL content. The shell includes the full HTML document wrapper (`<head>`, scripts, canvas). The partial contains only the `#page-wrapper` inner content.

### Line Number Offsets Between Shell and Partial
Because shells contain ~110 lines of document head/wrapper before content begins, the same content block appears at different line numbers:

| Content Block | Shell (index.html) | NL Partial | EN Partial |
|--------------|-------------------|------------|------------|
| Stat counter ("Spellen Beschikbaar") | ~line 151 | ~line 41 | ~line 41 |
| Product card SVG placeholder | ~line 298-305 | ~line 188-196 | ~line 187-195 |
| Product card description ("spellen") | ~line 293 | ~line 183 | ~line 182 |
| Software card ("spellen") | ~line 366-367 | ~line 256-257 | ~line 253 |
| FAQ 4th item | ~line 573-579 | ~line 462-468 | ~line 457-463 |

### Image Path Convention
Root pages use `media/...` paths. Product pages use `../media/...`. Since all edits in this phase target root pages, the correct image path is:
```
media/products/2in1/1.png
```

### FAQ Markup Pattern
```html
<details class="accordion-item">
    <summary>Question text here</summary>
    <div class="accordion-content">
        Answer text here.
    </div>
</details>
```

### Product Card Image Replacement Pattern
The current SVG placeholder block (lines 298-305 in index.html):
```html
<div style="padding: 2rem; display: flex; align-items: center; justify-content: center;">
    <div style="background: rgba(254,186,4,0.1); border-radius: 16px; padding: 2.5rem; text-align: center;">
        <svg width="80" height="80" fill="var(--color-primary)" viewBox="0 0 24 24">
            <path d="M3 5v14h18V5H3zm16 12H5V7h14v10z"/>
        </svg>
        <div style="color: var(--color-primary); font-weight: 800; margin-top: 0.5rem">2-in-1</div>
        <div style="color: #999">Vloer + Muur</div>
    </div>
</div>
```

Should be replaced with an `<img>` tag. The existing container's dark gradient background (1d1e22 to 2a2b30) will work well with the product photo which has a light/white background, so the image needs appropriate styling to fit the grid cell.

### Anti-Patterns to Avoid
- **Blind find-and-replace on "spellen":** The word "spellen" appears in nav links to the "3D Spellen" page -- those must NOT be changed (that page's name is out of scope, Phase 5 removal candidate). Also "bewegingsspellen" (compound word in FAQ answer) will be removed entirely by the new FAQ text.
- **Changing "Game Editor" references:** The Software & Maatwerk card mentions "Game Editor" -- this is a product name, not a generic term. Do not change it to "Program Editor".
- **Touching shell document head:** Only edit within the `#page-wrapper` content area. Never modify `<head>`, `<script>` tags, or document structure.

## Exact Edit Inventory

### Homepage Family (index) -- 3 files

#### Edit A: Stat Counter Label
| File | Line | Current | New |
|------|------|---------|-----|
| `index.html` | 151 | `Spellen Beschikbaar` | `Programma's Beschikbaar` |
| `partials/index-nl.html` | 41 | `Spellen Beschikbaar` | `Programma's Beschikbaar` |
| `partials/index-en.html` | 41 | `Games Available` | `Programs Available` |

#### Edit B: Product Card Image (SVG to real photo)
Replace the entire `<div style="padding: 2rem; ...">` container (containing SVG + "2-in-1" + "Vloer + Muur" labels) with an `<img>` element.

| File | Lines | Action |
|------|-------|--------|
| `index.html` | 298-306 | Replace SVG container with product image |
| `partials/index-nl.html` | 188-196 | Same replacement |
| `partials/index-en.html` | 187-195 | Same replacement (NL label "Vloer + Muur" becomes "Floor + Wall" in EN -- but since replacing with an image, text labels are removed) |

#### Edit C: Product Card Description Text
| File | Line | Current | New |
|------|------|---------|-----|
| `index.html` | 293 | `interactieve spellen` | `interactieve programma's` |
| `partials/index-nl.html` | 183 | `interactieve spellen` | `interactieve programma's` |
| `partials/index-en.html` | 182 | `interactive games` | `interactive programs` |

#### Edit D: Software Card Description
| File | Lines | Current | New |
|------|-------|---------|-----|
| `index.html` | 366-367 | `interactieve spellen` | `interactieve programma's` |
| `partials/index-nl.html` | 256-257 | `interactieve spellen` | `interactieve programma's` |
| `partials/index-en.html` | 253 | `interactive games` | `interactive programs` |

#### Edit E: FAQ Question and Answer
| File | Lines | Action |
|------|-------|--------|
| `index.html` | 573-579 | Replace question + answer with approved text (NL) |
| `partials/index-nl.html` | 462-468 | Same NL replacement |
| `partials/index-en.html` | 457-463 | Replace with approved EN text |

### Prijzen Family -- 3 files

Each file has ~11 occurrences of "spellen/games". These fall into categories:

| Category | NL Current | NL New | EN Current | EN New | Occurrences per file |
|----------|-----------|--------|-----------|--------|---------------------|
| Table header | `Spellen` | `Programma's` | `Games` | `Programs` | 1 |
| Table cells (data-label) | `data-label="Spellen"` | `data-label="Programma's"` | `data-label="Games"` | `data-label="Programs"` | 6 |
| Table cell values | `60+ spellen`, `spellen` | `60+ programma's`, `programma's` | `60+ games`, `games` | `60+ programs`, `programs` | 4 |
| Package features | `interactieve spellen` | `interactieve programma's` | `interactive games` | `interactive programs` | 3 |
| FAQ answers | `extra spellen` | `extra programma's` | `extra games` | `extra programs` | 2 |

**Exception to watch:** "Klim Games" (climbing games) in the table is a product category label for the climbing wall -- change to "Klim Programma's" / "Climbing Programs" per the systematic replacement, but note the climbing wall page itself is Phase 5 scope.

### Over-Ons Family -- 3 files

Each file has ~5 occurrences of "spellen/games":

| Location | NL Current | NL New | EN Current | EN New |
|----------|-----------|--------|-----------|--------|
| Timeline item label | `Interactieve Spellen` | `Interactieve Programma's` | `Interactive Games` | `Interactive Programs` |
| Game development description | `spellen die zowel leuk als leerzaam` | `programma's die zowel leuk als leerzaam` | `games that are both fun` | `programs that are both fun` |
| Innovation paragraph | `functies, spellen en toepassingen` | `functies, programma's en toepassingen` | `features, games, and applications` | `features, programs, and applications` |
| Passion paragraph | `creativiteit van onze spellen` | `creativiteit van onze programma's` | `creativity of our games` | `creativity of our programs` |
| Updates card | `nieuwe spellen` | `nieuwe programma's` | `new games` | `new programs` |

**Exception:** The "Game Development" section heading/label on over-ons is a department/discipline name, not a product term. This can stay as-is (Claude's discretion: the heading "Game Development" describes the team's discipline, similar to "Game Editor" being a product name).

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| NL/EN parity checking | Manual line-by-line comparison | `grep -c "spellen\|games" FILE` before/after counts | Counting occurrences is faster and catches missed edits |
| Finding all replacement targets | Reading full files | `grep -n "spellen\|Spellen\|games\|Games" FILE` | Precise line numbers for each occurrence |
| Verifying no broken links after image swap | Manual browser testing | `grep -rn "yellow\|rgba(254,186,4" FILE` to confirm SVG removal | Confirms the old visual is fully gone |

## Common Pitfalls

### Pitfall 1: Shell/Partial Content Drift
**What goes wrong:** Editing the shell page but forgetting the NL partial (or vice versa), creating a state where language switching shows different content.
**Why it happens:** Shell and NL partial have identical NL content at different line numbers. Easy to think "I already changed the NL" when you only changed one copy.
**How to avoid:** Always edit in triplets. After each page family, diff shell NL content against NL partial content to confirm they match.
**Warning signs:** `diff <(sed -n '/header/,/footer/p' shell.html) partial-nl.html` showing unexpected differences.

### Pitfall 2: Over-Replacing "spellen" in Navigation Links
**What goes wrong:** The nav bar contains `<a href="/3d-games">3D <span class="lang-nl">Spellen</span><span class="lang-en">Games</span></a>` -- changing this breaks the nav link text for a page that still exists.
**Why it happens:** Blind find-and-replace on "Spellen" catches nav links too.
**How to avoid:** Only replace within identified content sections (stat counter, product cards, FAQ, package features, body copy). Never touch `<nav>` or `<footer>` link text. The shell pages have these nav links at lines 46 and 96; partials do NOT have nav links (they are swapped into an existing shell).
**Warning signs:** `grep -n "Spellen" FILE` returning results from nav/header area (lines <120 in shell files).

### Pitfall 3: Image Size and Layout Breaking
**What goes wrong:** The SVG is 80x80px inline. Replacing with a 1MB PNG without size constraints blows up the grid layout or causes slow loading.
**Why it happens:** Product photos are large files (1-1.6MB) meant for product detail pages, not card thumbnails.
**How to avoid:** Set explicit `width`, `max-width`, `height: auto`, and `object-fit` on the `<img>` tag. Consider `loading="lazy"`. The container is roughly 400px wide in the grid -- the image should be constrained to that.
**Warning signs:** Grid layout breaking on mobile, page load time increasing noticeably.

### Pitfall 4: Compound Words Containing "spellen"
**What goes wrong:** Words like "bewegingsspellen" (movement games) contain "spellen" as a suffix -- blind replacement creates "bewegingsprogramma's" which is incorrect Dutch.
**Why it happens:** Dutch compound words incorporate root words.
**How to avoid:** In this phase, the FAQ answer containing "bewegingsspellen" is being fully replaced with new approved text, so this is naturally handled. For other pages, use targeted replacements on exact phrases rather than regex on the word "spellen" alone.

### Pitfall 5: data-label Attribute Mismatch
**What goes wrong:** On the pricing page, table cells have `data-label="Spellen"` attributes used for responsive table display. If you change the `<th>` text but not the `data-label`, mobile views show mismatched labels.
**Why it happens:** The `data-label` is a separate HTML attribute not adjacent to the visible cell text.
**How to avoid:** When changing `<th>Spellen</th>` to `<th>Programma's</th>`, also change all corresponding `data-label="Spellen"` to `data-label="Programma's"` in the same table.

## Code Examples

### Image Replacement (verified pattern from codebase)
```html
<!-- BEFORE: SVG placeholder -->
<div style="padding: 2rem; display: flex; align-items: center; justify-content: center;">
    <div style="background: rgba(254,186,4,0.1); border-radius: 16px; padding: 2.5rem; text-align: center;">
        <svg width="80" height="80" fill="var(--color-primary)" viewBox="0 0 24 24">
            <path d="M3 5v14h18V5H3zm16 12H5V7h14v10z"/>
        </svg>
        <div style="color: var(--color-primary); font-weight: 800; margin-top: 0.5rem">2-in-1</div>
        <div style="color: #999">Vloer + Muur</div>
    </div>
</div>

<!-- AFTER: Real product photo -->
<div style="padding: 2rem; display: flex; align-items: center; justify-content: center;">
    <img src="media/products/2in1/1.png"
         alt="IAM 2-in-1 interactieve vloer en muur behuizing"
         style="max-width: 100%; height: auto; border-radius: 16px;"
         loading="lazy">
</div>
```

Note: EN partial uses `alt="IAM 2-in-1 interactive floor and wall housing"`.

### FAQ Replacement
```html
<!-- NL version (shell + NL partial) -->
<details class="accordion-item">
    <summary>Hoeveel interactieve programma's zijn er beschikbaar?</summary>
    <div class="accordion-content">
        Het aantal beschikbare programma's hangt af van het product en het gekozen pakket.
        Onze interactieve wand en vloer bieden een breed scala aan programma's, terwijl de
        interactieve zandbak een eigen selectie heeft. Neem contact met ons op voor een
        overzicht dat past bij uw situatie.
    </div>
</details>

<!-- EN version (EN partial) -->
<details class="accordion-item">
    <summary>How many interactive programs are available?</summary>
    <div class="accordion-content">
        The number of available programs depends on the product and the selected package.
        Our interactive wall and floor offer a wide range of programs, while the interactive
        sandbox has its own selection. Please contact us for an overview that fits your
        situation.
    </div>
</details>
```

### Stat Counter Replacement
```html
<!-- NL -->
<div class="stat-label">Programma's Beschikbaar</div>

<!-- EN -->
<div class="stat-label">Programs Available</div>
```

## Verification Strategy

### Pre-Edit Baseline
Run before any edits to establish occurrence counts:
```bash
# Homepage family
grep -c "spellen\|Spellen" index.html partials/index-nl.html
grep -c "games\|Games" partials/index-en.html

# Prijzen family  
grep -c "spellen\|Spellen" prijzen.html partials/prijzen-nl.html
grep -c "games\|Games" partials/prijzen-en.html

# Over-ons family
grep -c "spellen\|Spellen" over-ons.html partials/over-ons-nl.html
grep -c "games\|Games" partials/over-ons-en.html
```

### Post-Edit Verification
1. Confirm remaining "spellen/games" occurrences are ONLY in nav links (shell files only, not in partials since partials have no nav).
2. Confirm SVG placeholder markup is fully removed (no orphaned `rgba(254,186,4` references in product card).
3. Confirm shell and NL partial match for each family.
4. Confirm `<img>` tag points to existing file: `ls media/products/2in1/1.png`.
5. Confirm FAQ approved text is verbatim (no paraphrasing).

## Validated Image Asset

| File | Size | Dimensions | Suitability |
|------|------|-----------|-------------|
| `media/products/2in1/1.png` | 1.0 MB | Shows 3/4 angle of white housing on wheeled base | BEST -- clearly shows the product form factor |
| `media/products/2in1/2.png` | 1.3 MB | Front-facing view | Good but less dynamic |
| `media/products/2in1/3.png` | 1.6 MB | Not reviewed | Backup option |
| `media/products/2in1/4.png` | 1.6 MB | Not reviewed | Backup option |

**Recommendation:** Use `1.png` -- it shows the housing at an angle that reveals the form factor clearly, which is the purpose of the image replacement (showing a "real image of the 2-in-1 housing" per the change brief).

## Scope Boundaries -- What NOT to Touch

| Item | Why Not | When |
|------|---------|------|
| Nav links containing "3D Spellen" / "3D Games" | Page still exists; nav text matches page name | Phase 5 (page deletion) |
| "Game Editor" in Software card | Product name, not generic term | Never -- it's a proper noun |
| Product detail pages | D-13 explicitly excludes them | Phase 4 |
| "free updates" / "gratis updates" | D-10 confirms not on homepage; other pages are Phase 4 | Phase 4 |
| Stat counter number (60+) | Number stays the same on homepage | Phase 4 for product pages |

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | Manual HTML verification (no automated test framework in project) |
| Config file | None |
| Quick run command | `grep -c "spellen\|Spellen\|games\|Games" {file}` |
| Full suite command | `bash -c 'for f in index.html partials/index-nl.html partials/index-en.html prijzen.html partials/prijzen-nl.html partials/prijzen-en.html over-ons.html partials/over-ons-nl.html partials/over-ons-en.html; do echo "$f:"; grep -n "spellen\|Spellen\|games\|Games" "$f"; done'` |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| HOME-01 | Product card shows real image, not SVG | grep/manual | `grep -c "svg.*80.*80\|rgba(254,186,4" index.html` (should be 0 in product section) | N/A -- grep check |
| HOME-02 | FAQ uses approved question and answer | grep | `grep -c "interactieve programma" index.html partials/index-nl.html` (should be >=1 each) | N/A -- grep check |
| BRND-01 | Primary selling pages use current framing | manual | Visual check that homepage no longer has generic SVG | N/A |
| BRND-02 | Not misled about 2-in-1 being generic | manual | Verify real product photo is shown | N/A |
| BRND-03 | "programs" terminology in place | grep | `grep -c "Programma" index.html prijzen.html over-ons.html` (should match expected counts) | N/A -- grep check |

### Sampling Rate
- **Per task commit:** Run grep occurrence count on edited files
- **Per wave merge:** Run full grep audit across all 9 target files
- **Phase gate:** Zero unexpected "spellen/games" remaining outside nav links

### Wave 0 Gaps
None -- no test framework to set up. Verification is grep-based occurrence counting on static HTML files.

## Open Questions

1. **Image file size for web performance**
   - What we know: `1.png` is 1.0 MB, which is large for a card thumbnail
   - What's unclear: Whether the site has any image optimization pipeline
   - Recommendation: Use the image as-is with `loading="lazy"`. The site has no build step or image optimization. If performance matters later, the image can be converted to WebP or resized -- but that is beyond this phase's scope.

## Sources

### Primary (HIGH confidence)
- Direct codebase inspection of all 9 target files -- verified line numbers, exact current text, and markup patterns
- `media/products/2in1/` directory -- confirmed 4 PNG images available, visually reviewed 1.png and 2.png
- `02-CONTEXT.md` -- locked decisions with approved replacement text
- `change-brief.md` -- original source of approved FAQ text and terminology changes

### Secondary (MEDIUM confidence)
- None needed -- all research is codebase-internal

### Tertiary (LOW confidence)
- None

## Project Constraints (from CLAUDE.md)

- **Tech stack**: Keep current static HTML + CSS + HTMX + vanilla JS -- no new frameworks, no build step
- **Content consistency**: Changes must be applied across full pages and partials
- **Path safety**: Root pages use `media/...` paths, product pages use `../media/...` -- this phase only touches root pages so all paths use `media/...`
- **Brownfield safety**: Existing nav, routes, and contact flows must keep working

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH -- no libraries involved, pure HTML editing
- Architecture: HIGH -- three-file family pattern verified with exact line numbers
- Pitfalls: HIGH -- all edge cases identified through grep analysis of actual codebase

**Research date:** 2026-04-01
**Valid until:** 2026-05-01 (stable -- static HTML codebase with no external dependencies)
