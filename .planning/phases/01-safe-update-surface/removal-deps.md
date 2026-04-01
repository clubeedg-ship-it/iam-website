# Route Dependency Map for Removal Candidates

**Generated:** 2026-04-01
**Method:** Automated grep across all 62 HTML files + sitemap.xml + robots.txt + server.js route table

> This document maps every reference to each removal candidate so Phase 5 can execute removals without re-scanning the codebase. All references use clean URLs (e.g., `/bouw-een-park`) rather than `.html` file paths because the site uses a Node.js server with a route table in `server.js`.

---

## Page-Level Removal Candidates

### 1. bouw-een-park.html

**Files in family:** `bouw-een-park.html`, `partials/bouw-een-park-nl.html`, `partials/bouw-een-park-en.html`

**Route:** `/bouw-een-park` (redirects to `/build-a-park` via `server.js` L38)
**Canonical route:** `/build-a-park` (maps to `bouw-een-park.html` via `server.js` L16)

**Sitemap:** `sitemap.xml` L43 -- `https://interactivemove.nl/build-a-park` (priority 0.8)

**Robots.txt:** No specific rules.

**Total href references:** 73 across 39 files (shell pages + partials)

**Nav references -- Desktop nav (shell pages only, line ~131 pattern):**
- `blog.html:131`
- `zorg-revalidatie.html:374`
- `index.html:718`
- `bouw-een-park.html:280`
- `over-ons.html:514`
- `word-partner.html:244`
- `maak-je-spel.html:232`
- `prijzen.html:667`
- `3d-spellen.html:267`

Note: Shell pages for root families contain footer references to `/bouw-een-park`. Product shell pages use the same route.

**Nav references -- Product shell pages (footer pattern):**
- `products/interactieve-vloer.html:649`
- `products/interactieve-zandbak.html:641`
- `products/interactieve-klimwand.html:630`
- `products/software-maatwerk.html:615`
- `products/2-in-1-vloer-muur.html:639`
- `products/interactieve-muur.html:638`

**Content references (non-nav/footer body links):**
- `products/interactieve-vloer.html:600` -- CTA button "Bouw Uw Eigen Park"
- `products/interactieve-zandbak.html:592` -- CTA button "Bouw Uw Eigen Park"
- `products/interactieve-klimwand.html:582` -- CTA button "Bouw Uw Eigen Park"
- `products/software-maatwerk.html:567` -- CTA button "Bouw Uw Eigen Park"
- `products/2-in-1-vloer-muur.html:590` -- CTA button "Bouw Uw Eigen Park"
- `products/interactieve-muur.html:589` -- CTA button "Bouw Uw Eigen Park"
- `parken-speelhallen.html:146` -- CTA button (btn-danger)
- `parken-speelhallen.html:411` -- CTA button (primary)
- `bouw-een-park.html:15` -- data-page attribute (self-reference)

**Partial references (NL partials):**
- `partials/bouw-een-park-nl.html:150` -- footer
- `partials/3d-spellen-nl.html:137` -- footer
- `partials/word-partner-nl.html:134` -- footer
- `partials/over-ons-nl.html:392` -- footer
- `partials/index-nl.html:607` -- footer
- `partials/parken-speelhallen-nl.html:36,301,344` -- 2 CTA buttons + footer
- `partials/maak-je-spel-nl.html:122` -- footer
- `partials/prijzen-nl.html:545` -- footer
- `partials/zorg-revalidatie-nl.html:262` -- footer
- `partials/products/interactieve-vloer-nl.html:478,527` -- CTA + footer
- `partials/products/interactieve-klimwand-nl.html:471,519` -- CTA + footer
- `partials/products/interactieve-muur-nl.html:479,528` -- CTA + footer
- `partials/products/2-in-1-vloer-muur-nl.html:479,528` -- CTA + footer
- `partials/products/interactieve-zandbak-nl.html:481,530` -- CTA + footer
- `partials/products/software-maatwerk-nl.html:457,505` -- CTA + footer

**Partial references (EN partials):**
- `partials/bouw-een-park-en.html:148` -- footer
- `partials/3d-spellen-en.html:136` -- footer
- `partials/cookiebeleid-en.html:136` -- footer
- `partials/word-partner-en.html:134` -- footer
- `partials/over-ons-en.html:382` -- footer
- `partials/index-en.html:601` -- footer
- `partials/toegankelijkheid-en.html:111` -- footer
- `partials/parken-speelhallen-en.html:36,299,342` -- 2 CTA buttons + footer
- `partials/privacybeleid-en.html:170` -- footer
- `partials/maak-je-spel-en.html:122` -- footer
- `partials/zorg-revalidatie-en.html:262` -- footer
- `partials/prijzen-en.html:545` -- footer
- `partials/products/interactieve-muur-en.html:479,528` -- CTA + footer
- `partials/products/2-in-1-vloer-muur-en.html:479,528` -- CTA + footer
- `partials/products/interactieve-vloer-en.html:478,527` -- CTA + footer
- `partials/products/interactieve-klimwand-en.html:471,519` -- CTA + footer
- `partials/products/interactieve-zandbak-en.html:481,530` -- CTA + footer
- `partials/products/software-maatwerk-en.html:457,505` -- CTA + footer

**Removal impact:** Requires updating **39 files** to remove footer links, plus **6 product shell pages** and **12 product partials** to remove CTA buttons, plus `parken-speelhallen` shell and partials for body CTA buttons. Also requires removing from `sitemap.xml` and `server.js` route table (L16, L38).

---

### 2. 3d-spellen.html

**Files in family:** `3d-spellen.html`, `partials/3d-spellen-nl.html`, `partials/3d-spellen-en.html`

**Route:** `/3d-spellen` (redirects to `/3d-games` via `server.js` L39)
**Canonical route:** `/3d-games` (maps to `3d-spellen.html` via `server.js` L17)

**Sitemap:** `sitemap.xml` L49 -- `https://interactivemove.nl/3d-games` (priority 0.7)

**Robots.txt:** No specific rules.

**Total href references:** 46 across 22 files

**Nav references -- Desktop nav (href="/3d-games", all shell pages):**
- `blog.html:46,97` -- desktop + mobile nav
- `zorg-revalidatie.html:46,97`
- `onderwijs.html:46,97`
- `index.html:46,96`
- `over-ons.html:46,97`
- `parken-speelhallen.html:46,97`
- `privacybeleid.html:46,97`
- `word-partner.html:46,97`
- `maak-je-spel.html:46,97`
- `prijzen.html:46,97`
- `3d-spellen.html:46,97` -- self-reference
- `toegankelijkheid.html:46,97`
- `cookiebeleid.html:46,97`
- `bouw-een-park.html:46,97`
- `products/interactieve-vloer.html:46,97`
- `products/interactieve-zandbak.html:46,97`
- `products/interactieve-klimwand.html:46,97`
- `products/software-maatwerk.html:46,97`
- `products/2-in-1-vloer-muur.html:46,97`
- `products/interactieve-muur.html:46,97`

Note: Every shell page (20 total) references `/3d-games` in both desktop nav (line ~46) and mobile nav (line ~97). That accounts for 40 of the 46 references.

**Content references (non-nav body links using `/3d-spellen`):**
- `products/interactieve-vloer.html:339` -- CTA button "Bekijk Alle Spellen"
- `parken-speelhallen.html:396` -- CTA button

**Partial content references (using `/3d-spellen`):**
- `partials/products/interactieve-vloer-nl.html:217` -- CTA "Bekijk Alle Spellen"
- `partials/products/interactieve-vloer-en.html:217` -- CTA "View All Games"
- `partials/parken-speelhallen-en.html:284` -- CTA button
- `partials/parken-speelhallen-nl.html:286` -- CTA button

Note: The 3D games page is NOT referenced in footer links (unlike bouw-een-park). It appears only in nav menus and a few body CTAs.

**Self-reference:** `3d-spellen.html:15` -- `data-page="3d-spellen"`

**Removal impact:** Requires updating **20 shell pages** to remove nav menu item (desktop + mobile = 40 line edits), plus **4 partial CTA links** and **2 shell CTA links**. Also requires removing from `sitemap.xml` and `server.js` route table (L17, L39).

---

### 3. interactieve-klimwand.html

**Files in family:** `products/interactieve-klimwand.html`, `partials/products/interactieve-klimwand-nl.html`, `partials/products/interactieve-klimwand-en.html`

**Route:** `/products/interactive-climbing-wall` (maps to `products/interactieve-klimwand.html` via `server.js` L27)

**Sitemap:** `sitemap.xml` L27 -- `https://interactivemove.nl/products/interactive-climbing-wall` (priority 0.9)

**Robots.txt:** No specific rules.

> **Note:** Spreadsheet row 46 says "Delete page" but D-08 does not list this as a confirmed removal target. Flagged for Phase 5 confirmation alongside the other removal candidates. The climbing wall page has the largest dependency footprint of all removal candidates.

**Total href references:** 97 across 48 files

**Nav references -- Desktop nav (href="/products/interactive-climbing-wall", all 20 shell pages):**
Every shell page references the climbing wall in both desktop nav (line ~38) and mobile nav (line ~87):
- All 14 root shell pages: `index.html`, `prijzen.html`, `over-ons.html`, `onderwijs.html`, `parken-speelhallen.html`, `zorg-revalidatie.html`, `3d-spellen.html`, `bouw-een-park.html`, `blog.html`, `maak-je-spel.html`, `word-partner.html`, `cookiebeleid.html`, `privacybeleid.html`, `toegankelijkheid.html`
- All 6 product shell pages: `products/interactieve-vloer.html`, `products/interactieve-muur.html`, `products/interactieve-zandbak.html`, `products/interactieve-klimwand.html`, `products/2-in-1-vloer-muur.html`, `products/software-maatwerk.html`

That accounts for 40 references (20 desktop + 20 mobile nav).

**Footer references (shell pages that include climbing wall in footer product list):**
- `zorg-revalidatie.html:385`
- `onderwijs.html:594`
- `products/interactieve-vloer.html:660`
- `products/interactieve-zandbak.html:653`
- `products/interactieve-klimwand.html:642` (self-reference)
- `products/software-maatwerk.html:627`
- `products/2-in-1-vloer-muur.html:651`
- `products/interactieve-muur.html:650`
- `bouw-een-park.html:291`
- `over-ons.html:525`
- `parken-speelhallen.html:465`
- `word-partner.html:255`
- `maak-je-spel.html:243`
- `prijzen.html:678`
- `3d-spellen.html:278`

**Content references (non-nav, non-footer body links):**
- `products/2-in-1-vloer-muur.html:572` -- related product card
- `products/interactieve-muur.html:579` -- related product card
- `bouw-een-park.html:208` -- park hotspot link

**Partial references (NL partials -- footer):**
- `partials/onderwijs-nl.html:483`
- `partials/bouw-een-park-nl.html:78,161` -- park hotspot + footer
- `partials/word-partner-nl.html:145`
- `partials/products/interactieve-vloer-nl.html:538`
- `partials/products/interactieve-klimwand-nl.html:531`
- `partials/products/interactieve-muur-nl.html:469,540` -- related product + footer
- `partials/products/2-in-1-vloer-muur-nl.html:461,540` -- related product + footer
- `partials/products/interactieve-zandbak-nl.html:542`
- `partials/products/software-maatwerk-nl.html:517`
- `partials/over-ons-nl.html:403`
- `partials/3d-spellen-nl.html:148`
- `partials/parken-speelhallen-nl.html:355`
- `partials/maak-je-spel-nl.html:133`
- `partials/prijzen-nl.html:556`
- `partials/zorg-revalidatie-nl.html:273`

**Partial references (EN partials -- footer):**
- `partials/3d-spellen-en.html:147`
- `partials/cookiebeleid-en.html:147`
- `partials/word-partner-en.html:145`
- `partials/products/interactieve-muur-en.html:469,540` -- related product + footer
- `partials/products/2-in-1-vloer-muur-en.html:461,540` -- related product + footer
- `partials/products/interactieve-vloer-en.html:538`
- `partials/products/interactieve-klimwand-en.html:531`
- `partials/products/interactieve-zandbak-en.html:542`
- `partials/products/software-maatwerk-en.html:517`
- `partials/over-ons-en.html:393`
- `partials/bouw-een-park-en.html:78,159` -- park hotspot + footer
- `partials/onderwijs-en.html:479`
- `partials/toegankelijkheid-en.html:122`
- `partials/parken-speelhallen-en.html:353`
- `partials/privacybeleid-en.html:181`
- `partials/maak-je-spel-en.html:133`
- `partials/zorg-revalidatie-en.html:273`
- `partials/prijzen-en.html:556`

**Image references (within climbing wall family files only):**
- `products/interactieve-klimwand.html:123,124` -- `../media/products/interactieve-klimwand.webp`
- `partials/products/interactieve-klimwand-nl.html:13,14` -- `../media/products/interactieve-klimwand.png`
- `partials/products/interactieve-klimwand-en.html:13,14` -- `../media/products/interactieve-klimwand.png`

**Removal impact:** Requires updating **all 62 HTML files** (20 shell pages x2 nav refs + footer in most + all partials). Also requires removing from `sitemap.xml` and `server.js` route table (L27). This is the highest-impact removal candidate.

---

## Section-Level Removal Candidates

### 4. "Choose Your Package" / "Kies Uw Pakket" / "Kies Jouw Pakket" Sections

Per D-08, these package selection sections are candidates for removal from product pages.

**Total occurrences:** 18 across 18 files

**Shell pages (6 product shells, using "Kies Uw Pakket"):**
- `products/interactieve-vloer.html:455`
- `products/interactieve-muur.html:444`
- `products/interactieve-zandbak.html:445`
- `products/interactieve-klimwand.html:437`
- `products/2-in-1-vloer-muur.html:445`
- `products/software-maatwerk.html:423`

**NL partials (6 files, using "Kies Uw Pakket"):**
- `partials/products/interactieve-vloer-nl.html:333`
- `partials/products/interactieve-muur-nl.html:334`
- `partials/products/interactieve-zandbak-nl.html:334`
- `partials/products/interactieve-klimwand-nl.html:326`
- `partials/products/2-in-1-vloer-muur-nl.html:334`
- `partials/products/software-maatwerk-nl.html:313`

**EN partials (6 files, using "Choose Your Package" or "Choose your package"):**
- `partials/products/interactieve-vloer-en.html:333` -- "Choose your package" (lowercase 'y')
- `partials/products/interactieve-muur-en.html:334` -- "Choose Your Package"
- `partials/products/interactieve-zandbak-en.html:334` -- "Choose Your Package"
- `partials/products/interactieve-klimwand-en.html:326` -- "Choose Your Package"
- `partials/products/2-in-1-vloer-muur-en.html:334` -- "Choose Your Package"
- `partials/products/software-maatwerk-en.html:313` -- "Choose Your Package"

**Removal impact:** These are `<h2>` section headers. Removal requires deleting the entire package comparison section beneath each header. The section boundaries need to be determined per file during Phase 5 execution. This is a section removal (not a page removal), so no nav/footer changes are needed.

**Note:** The spreadsheet specifically requests deletion of "Choose Your Package" sections from sandbox (row 45) and software-maatwerk (row 47). The remaining 4 product families may also need section removal -- to be confirmed in Phase 5.

---

## Orphaned Partials

### 5. partials/content-nl.html and partials/content-en.html

**Verification search:**
```
grep -rn 'content-nl.html\|content-en.html' --include='*.html' . | grep -v '.planning/'
```

**Result:** Zero references found across all 62 HTML files.

No shell page loads these partials via HTMX or any other mechanism. No `<a>` tag, `hx-get`, or script reference points to them.

**Sitemap:** Not listed.

**server.js route table:** Not listed.

**Removal impact:** Safe to remove per D-09. Zero files need updating. These 2 files can be deleted without any downstream effect.

---

## Route Integrity Check

### Clean URL Routes in Use

The site uses a Node.js server (`server.js`) with a route table mapping clean URLs to `.html` files. All internal `href` attributes use clean URLs.

| Clean URL | Mapped File | Status |
|-----------|-------------|--------|
| `/` | `index.html` | OK |
| `/blog` | `blog.html` | OK |
| `/about` | `over-ons.html` | OK |
| `/pricing` | `prijzen.html` | OK |
| `/education` | `onderwijs.html` | OK |
| `/healthcare` | `zorg-revalidatie.html` | OK |
| `/entertainment` | `parken-speelhallen.html` | OK |
| `/build-a-park` | `bouw-een-park.html` | OK |
| `/3d-games` | `3d-spellen.html` | OK |
| `/create-your-game` | `maak-je-spel.html` | OK |
| `/partner` | `word-partner.html` | OK |
| `/privacy` | `privacybeleid.html` | OK |
| `/cookies` | `cookiebeleid.html` | OK |
| `/accessibility` | `toegankelijkheid.html` | OK |
| `/products/2-in-1-floor-wall` | `products/2-in-1-vloer-muur.html` | OK |
| `/products/interactive-floor` | `products/interactieve-vloer.html` | OK |
| `/products/interactive-wall` | `products/interactieve-muur.html` | OK |
| `/products/interactive-sandbox` | `products/interactieve-zandbak.html` | OK |
| `/products/interactive-climbing-wall` | `products/interactieve-klimwand.html` | OK |
| `/products/software` | `products/software-maatwerk.html` | OK |

### Redirects (server.js)

| Old Route | Redirects To | Status |
|-----------|-------------|--------|
| `/over-ons` | `/about` | OK |
| `/prijzen` | `/pricing` | OK |
| `/onderwijs` | `/education` | OK |
| `/zorg` | `/healthcare` | OK |
| `/parken` | `/entertainment` | OK |
| `/bouw-een-park` | `/build-a-park` | OK |
| `/3d-spellen` | `/3d-games` | OK |

### Pre-Existing Broken Links

The following internal `href` values found in HTML files have **no corresponding route** in `server.js` and no matching `.html` file:

| Broken href | Referenced in | Line(s) | Impact |
|-------------|---------------|---------|--------|
| `/horeca-events` | `products/software-maatwerk.html` | L387 | CTA card link |
| | `partials/products/software-maatwerk-nl.html` | L277 | CTA card link |
| | `partials/products/software-maatwerk-en.html` | L277 | CTA card link |
| `/terms` | `privacybeleid.html` | L279 | Legal footer link |
| | `cookiebeleid.html` | L245 | Legal footer link |
| | `partials/cookiebeleid-nl.html` | L135 | Legal footer link |
| | `partials/privacybeleid-nl.html` | L169 | Legal footer link |

**Total pre-existing broken links:** 2 routes, 7 references across 5 files.

These broken links exist **before** any Phase 1-5 changes. Downstream phases must not introduce additional broken links beyond these 2 known issues.

---

## Summary

| Candidate | Type | Files in Family | Total References | Files to Update | Sitemap Entry |
|-----------|------|-----------------|------------------|-----------------|---------------|
| bouw-een-park | Page removal | 3 | 73 | 39 | Yes (L43) |
| 3d-spellen | Page removal | 3 | 46 | 22 | Yes (L49) |
| interactieve-klimwand | Page removal (unconfirmed) | 3 | 97 | 48 | Yes (L27) |
| "Kies Uw/Choose Your Package" | Section removal | N/A | 18 | 18 | N/A |
| content-nl/en (orphaned) | File deletion | 2 | 0 | 0 | No |
| **Pre-existing broken links** | Existing issue | N/A | 7 | 5 | N/A |
