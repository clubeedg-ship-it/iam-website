# File-Family Inventory

**Generated:** 2026-04-01
**Total HTML files:** 62
**Method:** Automated scan of all `*.html` files excluding `.planning/`

> **Note:** The original plan estimated 49 HTML files based on earlier codebase analysis. The actual count is 62 due to additional pages (`blog`, `maak-je-spel`, `word-partner`) gaining partials, legal pages (`cookiebeleid`, `privacybeleid`, `toegankelijkheid`) gaining partials, and the `mobiele-vloer` product being replaced by `2-in-1-vloer-muur`. Two previously listed products (`mobiele-vloer`, `interactieve-tekeningen`) have been fully removed (shell + partials).

## File Families

### Root Families (14)

| Family | Shell | NL Partial | EN Partial | Drift? | Notes |
|--------|-------|------------|------------|--------|-------|
| index | `index.html` | `partials/index-nl.html` | `partials/index-en.html` | NO | Homepage; primary entry point |
| prijzen | `prijzen.html` | `partials/prijzen-nl.html` | `partials/prijzen-en.html` | NO | Pricing page |
| over-ons | `over-ons.html` | `partials/over-ons-nl.html` | `partials/over-ons-en.html` | NO | About us |
| onderwijs | `onderwijs.html` | `partials/onderwijs-nl.html` | `partials/onderwijs-en.html` | NO | Education sector page |
| parken-speelhallen | `parken-speelhallen.html` | `partials/parken-speelhallen-nl.html` | `partials/parken-speelhallen-en.html` | NO | Parks and arcades sector page |
| zorg-revalidatie | `zorg-revalidatie.html` | `partials/zorg-revalidatie-nl.html` | `partials/zorg-revalidatie-en.html` | NO | Healthcare sector page |
| 3d-spellen | `3d-spellen.html` | `partials/3d-spellen-nl.html` | `partials/3d-spellen-en.html` | NO | 3D games page -- removal candidate |
| bouw-een-park | `bouw-een-park.html` | `partials/bouw-een-park-nl.html` | `partials/bouw-een-park-en.html` | NO | Build a park page -- removal candidate |
| blog | `blog.html` | `partials/blog-nl.html` | `partials/blog-en.html` | NO | Blog page |
| maak-je-spel | `maak-je-spel.html` | `partials/maak-je-spel-nl.html` | `partials/maak-je-spel-en.html` | NO | Make your game page |
| word-partner | `word-partner.html` | `partials/word-partner-nl.html` | `partials/word-partner-en.html` | NO | Become a partner page |
| cookiebeleid | `cookiebeleid.html` | `partials/cookiebeleid-nl.html` | `partials/cookiebeleid-en.html` | NO | Cookie policy |
| privacybeleid | `privacybeleid.html` | `partials/privacybeleid-nl.html` | `partials/privacybeleid-en.html` | NO | Privacy policy |
| toegankelijkheid | `toegankelijkheid.html` | `partials/toegankelijkheid-nl.html` | `partials/toegankelijkheid-en.html` | NO | Accessibility statement |

### Product Families (6)

| Family | Shell | NL Partial | EN Partial | Drift? | Notes |
|--------|-------|------------|------------|--------|-------|
| interactieve-vloer | `products/interactieve-vloer.html` | `partials/products/interactieve-vloer-nl.html` | `partials/products/interactieve-vloer-en.html` | NO | Interactive floor |
| interactieve-muur | `products/interactieve-muur.html` | `partials/products/interactieve-muur-nl.html` | `partials/products/interactieve-muur-en.html` | NO | Interactive wall |
| interactieve-zandbak | `products/interactieve-zandbak.html` | `partials/products/interactieve-zandbak-nl.html` | `partials/products/interactieve-zandbak-en.html` | NO | Interactive sandbox |
| interactieve-klimwand | `products/interactieve-klimwand.html` | `partials/products/interactieve-klimwand-nl.html` | `partials/products/interactieve-klimwand-en.html` | NO | Interactive climbing wall -- deletion candidate (row 46) |
| 2-in-1-vloer-muur | `products/2-in-1-vloer-muur.html` | `partials/products/2-in-1-vloer-muur-nl.html` | `partials/products/2-in-1-vloer-muur-en.html` | NO | 2-in-1 floor+wall combo (replaces former mobiele-vloer) |
| software-maatwerk | `products/software-maatwerk.html` | `partials/products/software-maatwerk-nl.html` | `partials/products/software-maatwerk-en.html` | NO | Software and custom development |

### Drift Detection Method

For each family with partials, nav link drift was checked by comparing href attributes:
```bash
diff <(grep -o 'href="[^"]*\.html[^"]*"' SHELL | sort) \
     <(grep -o 'href="[^"]*\.html[^"]*"' NL_PARTIAL | sort)
```
All 20 families showed NO drift on nav links as of 2026-04-01.

## Orphaned Partials

The following partials have no shell page referencing them and are cleanup candidates (per D-03, D-09):

| Partial | Referenced by shell? | Status |
|---------|---------------------|--------|
| `partials/content-nl.html` | No (verified via `grep -rn 'content-nl.html' --include='*.html'`) | Orphaned -- safe to remove |
| `partials/content-en.html` | No (verified via `grep -rn 'content-en.html' --include='*.html'`) | Orphaned -- safe to remove |

## Removal Investigation Targets

Per D-08, these families and sections are flagged for removal investigation (final decision in Phase 5):

### Page-Level Removal Candidates

| Family | Files | Reason | Nav Impact |
|--------|-------|--------|------------|
| bouw-een-park | `bouw-een-park.html`, `partials/bouw-een-park-nl.html`, `partials/bouw-een-park-en.html` (3 files) | Removal candidate per D-08 | Referenced in nav/footer across all HTML files |
| 3d-spellen | `3d-spellen.html`, `partials/3d-spellen-nl.html`, `partials/3d-spellen-en.html` (3 files) | Removal candidate per D-08 | Referenced in nav/footer across all HTML files |
| interactieve-klimwand | `products/interactieve-klimwand.html`, `partials/products/interactieve-klimwand-nl.html`, `partials/products/interactieve-klimwand-en.html` (3 files) | Spreadsheet row 46 says "Delete page" | Referenced in nav/footer across all HTML files |

### Section-Level Removal Candidates

| Section | Affected Files | Reason |
|---------|---------------|--------|
| "Choose Your Package" / "Kies Uw Pakket" / "Kies Jouw Pakket" | Product partials (up to 12 files across 6 product families) | Section removal candidate per D-08 |

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total HTML files | 62 |
| Root families (with partials) | 14 |
| Product families (with partials) | 6 |
| Total families | 20 |
| Orphaned partials | 2 |
| Page-level removal candidates | 3 families (9 files) |
| Section removal candidates | Up to 12 product partial files |
| Removed products (no longer on disk) | 2 (mobiele-vloer, interactieve-tekeningen) |

## File Checklist

All 62 HTML files for downstream phase tracking:

### Root Pages
- [ ] `3d-spellen.html`
- [ ] `blog.html`
- [ ] `bouw-een-park.html`
- [ ] `cookiebeleid.html`
- [ ] `index.html`
- [ ] `maak-je-spel.html`
- [ ] `onderwijs.html`
- [ ] `over-ons.html`
- [ ] `parken-speelhallen.html`
- [ ] `prijzen.html`
- [ ] `privacybeleid.html`
- [ ] `toegankelijkheid.html`
- [ ] `word-partner.html`
- [ ] `zorg-revalidatie.html`

### Product Pages
- [ ] `products/2-in-1-vloer-muur.html`
- [ ] `products/interactieve-klimwand.html`
- [ ] `products/interactieve-muur.html`
- [ ] `products/interactieve-vloer.html`
- [ ] `products/interactieve-zandbak.html`
- [ ] `products/software-maatwerk.html`

### Root Partials
- [ ] `partials/3d-spellen-en.html`
- [ ] `partials/3d-spellen-nl.html`
- [ ] `partials/blog-en.html`
- [ ] `partials/blog-nl.html`
- [ ] `partials/bouw-een-park-en.html`
- [ ] `partials/bouw-een-park-nl.html`
- [ ] `partials/content-en.html`
- [ ] `partials/content-nl.html`
- [ ] `partials/cookiebeleid-en.html`
- [ ] `partials/cookiebeleid-nl.html`
- [ ] `partials/index-en.html`
- [ ] `partials/index-nl.html`
- [ ] `partials/maak-je-spel-en.html`
- [ ] `partials/maak-je-spel-nl.html`
- [ ] `partials/onderwijs-en.html`
- [ ] `partials/onderwijs-nl.html`
- [ ] `partials/over-ons-en.html`
- [ ] `partials/over-ons-nl.html`
- [ ] `partials/parken-speelhallen-en.html`
- [ ] `partials/parken-speelhallen-nl.html`
- [ ] `partials/prijzen-en.html`
- [ ] `partials/prijzen-nl.html`
- [ ] `partials/privacybeleid-en.html`
- [ ] `partials/privacybeleid-nl.html`
- [ ] `partials/toegankelijkheid-en.html`
- [ ] `partials/toegankelijkheid-nl.html`
- [ ] `partials/word-partner-en.html`
- [ ] `partials/word-partner-nl.html`
- [ ] `partials/zorg-revalidatie-en.html`
- [ ] `partials/zorg-revalidatie-nl.html`

### Product Partials
- [ ] `partials/products/2-in-1-vloer-muur-en.html`
- [ ] `partials/products/2-in-1-vloer-muur-nl.html`
- [ ] `partials/products/interactieve-klimwand-en.html`
- [ ] `partials/products/interactieve-klimwand-nl.html`
- [ ] `partials/products/interactieve-muur-en.html`
- [ ] `partials/products/interactieve-muur-nl.html`
- [ ] `partials/products/interactieve-vloer-en.html`
- [ ] `partials/products/interactieve-vloer-nl.html`
- [ ] `partials/products/interactieve-zandbak-en.html`
- [ ] `partials/products/interactieve-zandbak-nl.html`
- [ ] `partials/products/software-maatwerk-en.html`
- [ ] `partials/products/software-maatwerk-nl.html`
