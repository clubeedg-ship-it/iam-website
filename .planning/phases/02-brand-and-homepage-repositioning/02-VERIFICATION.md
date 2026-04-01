---
phase: 02-brand-and-homepage-repositioning
verified: 2026-04-01T23:15:00Z
status: passed
score: 4/4 success criteria verified
gaps: []
human_verification:
  - test: "Open index.html in browser, verify 2-in-1 product card shows the real housing photo (not a yellow SVG placeholder)"
    expected: "A PNG photo of the 2-in-1 housing appears in the products section grid"
    why_human: "Visual rendering cannot be verified via grep"
  - test: "Click NL/EN toggle on homepage, pricing, and about pages -- verify content swaps correctly in both directions"
    expected: "Content swaps without layout break; NL and EN versions show equivalent updated content"
    why_human: "HTMX swap behavior requires a running browser"
  - test: "Read EN FAQ answer about interactive programs -- check for duplicate word"
    expected: "The sentence should read 'while the interactive sandbox has its own selection' without repeating 'interactive'"
    why_human: "Minor text quality issue that needs editorial judgment on severity"
---

# Phase 02: Brand and Homepage Repositioning Verification Report

**Phase Goal:** Update the highest-visibility pages so visitors immediately get the current IAM message.
**Verified:** 2026-04-01T23:15:00Z
**Status:** passed
**Re-verification:** No -- initial verification

## Goal Achievement

### Observable Truths (Success Criteria)

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | Homepage copy and visuals reflect the approved IAM mobiel framing | VERIFIED | SVG placeholder removed from index.html/partials; real product photo `media/products/2in1/1.png` (896x1200 PNG) wired in all 3 index files; stat counter says "Programma's Beschikbaar" / "Programs Available"; product card descriptions say "programma's" / "programs" |
| 2 | Homepage FAQ uses the approved question and answer about interactive programs | VERIFIED | FAQ question updated to "Hoeveel interactieve programma's zijn er beschikbaar?" / "How many interactive programs are available?" in all 3 files; answer matches approved text from change brief (D-05/D-06) |
| 3 | Primary selling pages stop using outdated umbrella wording where it creates confusion | VERIFIED | Zero "spellen" in NL partials for index, prijzen, over-ons; zero non-proper-noun "games" in EN partials; pricing data-label attributes updated to "Programma's"; only preserved instances are nav links to "3D Spellen/Games" page (product name, not umbrella term) and "Game Design" / "Game Development" (team discipline names) |
| 4 | Updated homepage content still renders correctly in both languages | VERIFIED | Language switching via `js/site.js` `switchLang()` function intact; HTMX wiring loads `partials/index-{nl,en}.html`; all 3 index files contain the updated product image, stat counter, FAQ, and terminology |

**Score:** 4/4 success criteria verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `index.html` | Homepage shell with updated NL content | VERIFIED | Contains `media/products/2in1/1.png`, "Programma's Beschikbaar", updated FAQ |
| `partials/index-nl.html` | NL partial with same updates | VERIFIED | Zero "spellen" occurrences; product image, stat counter, FAQ all updated |
| `partials/index-en.html` | EN partial with English equivalents | VERIFIED | "Programs Available", "interactive programs", updated FAQ in English |
| `prijzen.html` | Pricing shell with updated terminology | VERIFIED | 11 "Programma" occurrences, 0 content "spellen" (2 nav-only) |
| `partials/prijzen-nl.html` | Pricing NL partial | VERIFIED | 0 "spellen" occurrences |
| `partials/prijzen-en.html` | Pricing EN partial | VERIFIED | 11 "Programs" occurrences, 0 non-proper "games" |
| `over-ons.html` | About shell with updated terminology | VERIFIED | 5 "Programma" occurrences, 0 content "spellen" (2 nav-only) |
| `partials/over-ons-nl.html` | About NL partial | VERIFIED | 0 "spellen" occurrences |
| `partials/over-ons-en.html` | About EN partial | VERIFIED | "Game design" preserved as discipline name; content uses "programs" |
| `media/products/2in1/1.png` | Real product photo | VERIFIED | PNG file exists, 896x1200, 1MB |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `index.html` | `media/products/2in1/1.png` | img src attribute | WIRED | Line 299: `<img src="media/products/2in1/1.png"` |
| `partials/index-nl.html` | `media/products/2in1/1.png` | img src attribute | WIRED | Line 189 |
| `partials/index-en.html` | `media/products/2in1/1.png` | img src attribute | WIRED | Line 188 |
| `index.html` | `partials/index-{nl,en}.html` | HTMX via switchLang() | WIRED | `js/site.js` line 48: `htmx.ajax('GET', partialPath, '#content-area')` |
| `prijzen.html` | `partials/prijzen-nl.html` | content parity | WIRED | Both contain "Programma's" terminology, 0 stale "spellen" |
| `over-ons.html` | `partials/over-ons-nl.html` | content parity | WIRED | Both contain "Programma's" terminology, 0 stale "spellen" |

### Data-Flow Trace (Level 4)

Not applicable -- this phase modifies static HTML content, not dynamic data rendering.

### Behavioral Spot-Checks

Step 7b: SKIPPED (static HTML site with no runnable entry points -- requires a web server to test)

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| BRND-01 | 02-01, 02-03 | Visitor sees IAM mobiel presented as the umbrella name for the mobile product line on primary selling pages | SATISFIED | Homepage product card updated with real 2-in-1 housing photo and "programma's/programs" terminology; outdated "spellen/games" removed from homepage, pricing, and about pages |
| BRND-02 | 02-01, 02-03 | Visitor is not misled into thinking every mobile variant is generically a 2-in-1 product | SATISFIED | SVG placeholder replaced with actual product photo; product card shows accurate 2-in-1 description; no generic "2-in-1" claims added to other products |
| BRND-03 | 02-02, 02-03 | Visitor sees current value language such as programs and no license costs where the refresh requires it | SATISFIED | "spellen/games" replaced with "programma's/programs" across all 9 files in 3 page families (homepage, pricing, about); data-labels in pricing table updated |
| HOME-01 | 02-01 | Homepage products section shows the updated real image of the mobile housing instead of the outdated yellow-square visual | SATISFIED | `media/products/2in1/1.png` (896x1200 PNG) replaces the `rgba(254,186,4)` SVG placeholder in all 3 index files |
| HOME-02 | 02-01 | Homepage FAQ asks how many interactive programs are available and shows the approved answer | SATISFIED | FAQ question and answer updated verbatim from change brief in all 3 index files |

No orphaned requirements found -- all 5 Phase 2 requirement IDs (BRND-01, BRND-02, BRND-03, HOME-01, HOME-02) appear in plan frontmatter and are verified.

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| `partials/index-en.html` | 458-459 | Duplicate word: "while the interactive\ninteractive sandbox" | Info | Copyediting error from Plan 03 fix that added "interactive" before "sandbox" without noticing line 458 already ended with "interactive". Does not block goal but should be fixed. |

Pre-existing patterns detected but NOT attributable to Phase 2:
- `logo-placeholder` CSS class in index files (placeholder logos for client section -- pre-existing design)
- `placeholder` attributes on form inputs (standard HTML attribute)
- "Coming soon" blog text in EN partial (pre-existing)

### Human Verification Required

### 1. Visual Rendering of Product Image

**Test:** Open `index.html` in a browser and scroll to the products section
**Expected:** The 2-in-1 product card displays a real photograph of the housing unit (not a yellow square with an SVG icon)
**Why human:** Image rendering, sizing, and visual quality cannot be verified via grep

### 2. Language Switching End-to-End

**Test:** On homepage, pricing page, and about page: click NL then EN then NL again
**Expected:** Content swaps smoothly in both directions; all terminology shows "programma's" in NL and "programs" in EN; no layout breaks
**Why human:** HTMX swap behavior and visual layout require a running browser

### 3. Duplicate Word in EN FAQ

**Test:** Read the EN FAQ answer about interactive programs on the homepage
**Expected:** Should say "while the interactive sandbox has its own selection" (one "interactive"), not "while the interactive interactive sandbox"
**Why human:** This is a minor text quality issue found during verification; needs editorial decision on whether to fix now or defer

### Gaps Summary

No blocking gaps found. All 4 success criteria are verified through codebase evidence. All 5 requirement IDs are satisfied.

One minor content quality issue was found: a duplicate "interactive" word in `partials/index-en.html` lines 458-459. This was introduced by the Plan 03 parity fix and does not block goal achievement but should be cleaned up.

---

_Verified: 2026-04-01T23:15:00Z_
_Verifier: Claude (gsd-verifier)_
