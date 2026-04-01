# Inter Active Move Website — Action Plan

Based on full review of all 74 HTML files, JS, and CSS against client feedback.
Generated: 2026-03-22

---

## PRIORITY 1: CRITICAL (Broken / Misleading Content)

### 1.1 Remove All Fake Statistics
**Owner decision: Otto confirmed stats are fake/placeholder — remove or make honest.**

| Location | Line(s) | Current Text | Action |
|----------|---------|-------------|--------|
| `index.html` | 156 | "98%" customer satisfaction | **Remove** or replace with honest qualifier ("hoge klanttevredenheid") |
| `index.html` | 153 | "60+" games | Verify actual game count with Otto; use real number |
| `over-ons.html` | 127 | "200+ locaties" | **Remove** — unverifiable |
| `over-ons.html` | 151 | "200+ tevreden klanten" | **Remove** — unverifiable |
| `partials/index-nl.html` | 70–106 | "100+ Basisscholen", "50+ Zorginstellingen", "75+ Speelparken", "30+ Revalidatiecentra", "25+ Musea", "15+ Gemeenten" | **Remove all** or replace with generic "Scholen, zorginstellingen en speelparken vertrouwen op ons" |
| `partials/index-en.html` | 70–106 | Same stats in English | **Remove all** — mirror NL changes |
| `partials/over-ons-nl.html` | 39 | "50+" with no context | **Remove** |
| `partials/over-ons-en.html` | 11–12, 27–39 | "200+ locations", "5+ continents", "15+ languages", "50+ team members" | **Remove all** — wildly unverifiable |
| `partials/onderwijs-nl.html` | various | "+67% concentratie", "+95% betrokkenheid", "+89% samenwerking", "+120% fysieke activiteit" | **Remove** progress bars and fake percentages |
| `partials/onderwijs-en.html` | 20, 26, 32, 289–327 | "95% higher engagement", "40% better retention", "100+ schools", progress bars | **Remove all** |
| `partials/onderwijs-en.html` | 327 | "Source: Internal research at 50 primary schools, 2025" | **Remove** — fake future-dated citation |
| `partials/parken-speelhallen-nl.html` | 71 | "50+ Spellen inbegrepen" | Verify and align with actual count |
| `partials/parken-speelhallen-en.html` | 18 | "+35% Return Visitors" | **Remove** — unverifiable |
| `partials/bouw-een-park-nl.html` | 13 | "500+ locaties" | **Remove** — unverifiable |
| `parken-speelhallen.html` | 130, 136 | "+35% Herhaalbezoekers", "2.5 Jaar ROI" | **Remove** — unverifiable |

### 1.2 Remove Fake Research Citations
| Location | Line(s) | Current Text | Action |
|----------|---------|-------------|--------|
| `partials/zorg-revalidatie-nl.html` | 121–124 | "Gamified revalidatie verhoogt therapietrouw met 67%" / "Journal of Rehabilitation Research, 2024" | **Remove entirely** — fabricated journal citation |
| `partials/zorg-revalidatie-en.html` | 121 | Same in English | **Remove entirely** |
| `onderwijs.html` | 233–236 | Same citation duplicated | **Remove entirely** |
| `zorg-revalidatie.html` | 232–236 | Same citation in shell page | **Remove entirely** |

### 1.3 Remove All Fake Testimonials & Review Counts
**Owner decision: Otto confirmed testimonials are fake — remove or soften.**

**Fake testimonials to remove (all pages):**

| Location | Line(s) | Fake Author | Action |
|----------|---------|-------------|--------|
| `index.html` | 509–541 | "Schooldirecteur", "Fysiotherapeut", "Ondernemer" | **Remove section** or replace with "Klanten vertellen binnenkort hun ervaringen" |
| `partials/index-nl.html` | 393–429 | Same three fake testimonials | **Remove** |
| `partials/index-en.html` | 381–429 | English versions (still uses Dutch titles like "Schooldirecteur") | **Remove** |
| `over-ons.html` | 376–384 | "Directeur, Kinderspeelparadijs, Amersfoort" | **Remove** |
| `prijzen.html` | 456–465 | "Directeur, Kinderspeelparadijs" with fake 8-month ROI claim | **Remove** |
| `partials/onderwijs-nl.html` | various | "Juf Lisa, Groep 4, Basisschool" | **Remove** |
| `partials/onderwijs-en.html` | 177–178 | "Teacher Lisa, Rainbow Primary School" | **Remove** |
| `products/interactieve-vloer.html` | 439–445 | "Locatiemanager, Basisschool, Utrecht" | **Remove** |
| `products/interactieve-muur.html` | 428–434 | "Klant, Gymleraar, Utrecht" | **Remove** |
| `products/interactieve-klimwand.html` | 422–428 | "Klant, Gymleraar" (also missing location) | **Remove** |
| `products/interactieve-zandbak.html` | 429–435 | "Manager, Science Museum, Amsterdam" | **Remove** |
| `products/interactieve-tekeningen.html` | 434–440 | "Ondernemer, Boulderhal, Amsterdam" | **Remove** |
| `products/2-in-1-vloer-muur.html` | 428–435 | "Gymleraar, Amsterdam" | **Remove** |
| `products/mobiele-vloer.html` | 413–419 | "Eigenaar, Evenementenverhuur, Rotterdam" | **Remove** |
| `products/software-maatwerk.html` | 407–413 | "Klant, Directeur Innovatie, Utrecht" | **Remove** |
| All product partials NL | ~318–320 | Generic testimonials | **Remove** |
| All product partials EN | ~318–320 | Generic testimonials | **Remove** |

**Duplicate testimonials (copy-paste with word swap):**
- `interactieve-muur.html:428` and `interactieve-klimwand.html:422` — identical text with "muur"→"klimwand" swap

**Fake review counts to remove:**

| File | Line | Count | Action |
|------|------|-------|--------|
| `products/2-in-1-vloer-muur.html` | 142 | "(52 reviews)" | **Remove** |
| `products/interactieve-vloer.html` | 138 | "(47 reviews)" | **Remove** |
| `products/interactieve-muur.html` | 138 | "(38 reviews)" | **Remove** |
| `products/interactieve-klimwand.html` | 135 | "(38 reviews)" | **Remove** |
| `products/interactieve-tekeningen.html` | 138 | "(32 reviews)" | **Remove** |
| `products/interactieve-zandbak.html` | 138 | "(47 reviews)" | **Remove** |
| `products/mobiele-vloer.html` | 138 | "(32 reviews)" | **Remove** |
| `products/software-maatwerk.html` | 125 | "(12 projecten voltooid)" | **Remove** |

### 1.4 Remove CE Certification Claims
**Owner decision: Otto says CE status is unknown — remove all claims.**

| Location | Line(s) | Claim | Action |
|----------|---------|-------|--------|
| `products/interactieve-vloer.html` | 192, 387 | "CE Gecertificeerd", "CE, RoHS, FCC" | **Remove** |
| `products/interactieve-muur.html` | 192, 300, 376 | "CE Gecertificeerd", "CE gecertificeerd met 2 jaar volledige garantie", "CE, RoHS, FCC" | **Remove CE references** (keep warranty separate) |
| `products/interactieve-klimwand.html` | 189, 298, 370 | Same pattern | **Remove** |
| `products/interactieve-zandbak.html` | 192, 308, 377 | "CE, EN 71 speelgoedrichtlijn" | **Remove** |
| `products/2-in-1-vloer-muur.html` | 196, 305, 377 | Same pattern | **Remove** |
| `products/interactieve-tekeningen.html` | 538 | "Het systeem is CE-gecertificeerd" (FAQ) | **Remove** |
| `partials/zorg-revalidatie-nl.html` | 20, 163 | "CE Medisch", "CE-gecertificeerd" | **Remove** |
| `partials/zorg-revalidatie-en.html` | 20 | "CE Medical" | **Remove** |
| All product partials (NL + EN) | ~74–195 | "CE Gecertificeerd" badges | **Remove from all** |

### 1.5 Fix Pricing: Lease/Payment to "Op Aanvraag"
**Owner decision: lease/payment prices should say "op aanvraag" / "on request".**

| Location | Line(s) | Current Text | Action |
|----------|---------|-------------|--------|
| `partials/prijzen-nl.html` | 12 | "Lease vanaf €199/mnd" | Change to "Lease mogelijk — op aanvraag" |
| `partials/prijzen-nl.html` | 412 | "Vanaf €299/maand" | Change to "Op aanvraag" |
| `partials/prijzen-nl.html` | 482 | "lease vanaf €299/maand" | Change to "lease mogelijk, neem contact op voor tarieven" |
| `partials/prijzen-en.html` | 12 | "Lease from €199/mo" | Change to "Leasing available — on request" |
| `prijzen.html` | 131, 536, 606 | Same €199/mnd and €299/maand claims | Change all to "op aanvraag" |
| `products/mobiele-vloer.html` | 488 | "Lease vanaf €449/maand" | Change to "Lease: op aanvraag" |

### 1.6 Soften ROI Claims
**Owner decision: soften to health/entertainment research-backed benefits.**

| Location | Line(s) | Current Text | Action |
|----------|---------|-------------|--------|
| `index.html` | 534 | "De investering was binnen 2 jaar terugverdiend" | Replace with benefit-focused language: "Kinderen en ouders zijn enthousiast" |
| `parken-speelhallen.html` | 287–346 | Full ROI Calculator section | Add prominent disclaimer: "Dit is een indicatieve schatting — werkelijke resultaten variëren" |
| `parken-speelhallen.html` | 136 | "2.5 Jaar ROI" badge | **Remove** or change to "Bewezen aantrekkingskracht" |
| `prijzen.html` | 456–465 | "binnen 8 maanden terugverdiend" testimonial | **Remove** (already in 1.3) |

### 1.7 Fix Delivery Time Claims
**Owner decision: delivery time is roughly 1 week.**

| Location | Line(s) | Current Text | Action |
|----------|---------|-------------|--------|
| `index.html` | 583 | "Gemiddelde levertijd: 4-6 weken" | Change to "Gemiddelde levertijd: ca. 1 week" |
| `partials/index-nl.html` | 470 | Same | Change to match |
| `partials/index-en.html` | 452 | "Average delivery time: 4-6 weeks" | Change to "Average delivery time: approx. 1 week" |
| `partials/prijzen-nl.html` | 390, 488 | "Standaard levertijd van 4-6 weken" | Change to "Standaard levertijd van ca. 1 week" |
| `partials/prijzen-en.html` | 390, 488 | "Standard delivery time of 4-6 weeks" | Change to "Standard delivery time of approximately 1 week" |
| `prijzen.html` | 514, 612 | Same Dutch claims | Change to match |

---

## PRIORITY 2: IMPORTANT (Professionalism / Consistency)

### 2.1 Brand Name: Standardize to "Inter Active Move"
**Owner decision: always "Inter Active Move" (with spaces). Legal: "Inter Active Move B.V."**

529 occurrences of "InterActiveMove" (no spaces) found across 66 files. Every instance must be changed to "Inter Active Move".

**Key files requiring bulk find-and-replace:**

| Pattern to Find | Replace With | Scope |
|----------------|-------------|-------|
| `InterActiveMove B.V.` | `Inter Active Move B.V.` | All files |
| `InterActiveMove` (standalone) | `Inter Active Move` | All files |
| `INTERACTIVEMOVE` | `INTER ACTIVE MOVE` | `over-ons.html:120` and anywhere else |
| `interactivemove` (in URLs like social links) | Keep as-is for URLs (facebook.com/interactivemove) | N/A |
| `alt="InterActiveMove"` | `alt="Inter Active Move"` | All image alt tags |

**Files with highest occurrence count (>10):**
- `over-ons.html` (17), `word-partner.html` (15), `maak-je-spel.html` (12)
- `partials/over-ons-nl.html` (14), `partials/over-ons-en.html` (14)
- `partials/word-partner-nl.html` (12), `partials/word-partner-en.html` (12)

### 2.2 Fix Game Count Inconsistencies
**Current claims are contradictory:**

| Source | Claim |
|--------|-------|
| Interactieve Vloer pages | 60+ games |
| Interactieve Muur pages | 100+ games |
| 2-in-1 Vloer-Muur pages | 100+ games |
| Mobiele Vloer pages | "100+ — dezelfde als de vaste vloer" (contradicts floor = 60+) |
| Parken & Speelhallen NL | 50+ games |
| 3D Spellen page | 60+ games |
| Onderwijs EN curriculum breakdown | Math 15 + Language 12 + PE 20 + Music 8 + Social 10 = 65 |

**Action:** Get real game count from Otto. Then update ALL pages to use one consistent, accurate number. Key files:
- All product partials (NL + EN)
- `partials/3d-spellen-nl.html:8`, `partials/3d-spellen-en.html:8`
- `partials/parken-speelhallen-nl.html:71`
- `partials/prijzen-nl.html:86,104,155,251`, `partials/prijzen-en.html` equivalents
- `partials/onderwijs-en.html:123–148` (curriculum breakdown must add up correctly)
- `partials/content-nl.html:319`, `partials/content-en.html` equivalent

### 2.3 Fix Mixed Dutch/English Content

**Dutch text in English partials:**

| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `partials/bouw-een-park-en.html` | 50, 62, 74, 99, 111 | Dutch product descriptions ("Projectie op de grond die reageert op beweging", "Wandprojectie voor sport en entertainment", etc.) | Translate to English |
| `partials/content-nl.html` | 6 | "Your browser does not support the video tag." (English in NL file) | Translate to "Uw browser ondersteunt geen video." |
| `partials/content-en.html` | 6 | Same text — correct for EN | Keep |
| `partials/index-en.html` | 381, 409 | Testimonial authors "Schooldirecteur", "Ondernemer" (Dutch job titles in English page) | Remove (fake testimonials) or translate |
| `partials/prijzen-en.html` | 337–339 | "Directeur" (Dutch title in English testimonial) | Remove (fake testimonial) |
| `partials/products/software-maatwerk-nl.html` | 223 | "Finale delivery met documentatie en training" — mixed EN/NL | Change to "Finale oplevering met documentatie en training" |

**English text leaking into Dutch sections:**

| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `partials/zorg-revalidatie-nl.html` | 32 | "Evidence-Based" | Change to "Wetenschappelijk onderbouwd" or keep with Dutch explanation |
| `partials/maak-je-spel-nl.html` | 7 | "IAM Game Editor" | Acceptable as product name, but add Dutch context |

**Footer copyright in English files still in Dutch:**

| File | Line | Text | Action |
|------|------|------|--------|
| `partials/3d-spellen-en.html` | 162 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| `partials/bouw-een-park-en.html` | 187 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| `partials/over-ons-en.html` | 408 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| `partials/toegankelijkheid-en.html` | 137 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| `partials/cookiebeleid-en.html` | 162 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| `partials/privacybeleid-en.html` | 196 | "Alle rechten voorbehouden" | Change to "All rights reserved" |
| All other EN partials | footer areas | Same pattern | Change to "All rights reserved" |

### 2.4 Fix Page Titles (Brand Name)
Every shell HTML page has `<title>... | InterActiveMove</title>` — must change to "Inter Active Move".

Affected files (all shell pages):
- `index.html`, `over-ons.html`, `prijzen.html`, `onderwijs.html`, `zorg-revalidatie.html`, `3d-spellen.html`, `bouw-een-park.html`, `maak-je-spel.html`, `word-partner.html`, `blog.html`, `cookiebeleid.html`, `privacybeleid.html`, `toegankelijkheid.html`, `parken-speelhallen.html`
- All 8 product shell pages in `products/`

### 2.5 Mission/Vision Section Needs Strengthening
**Client feedback: feels unfinished.**

| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `over-ons.html` | 255–310 | Mission & Vision cards — content is generic, reads like placeholder | Rewrite with specific company values, concrete goals, measurable ambitions. Ask Otto for real mission/vision statements |
| `partials/over-ons-nl.html` | equivalent | Same content in partial | Mirror changes |
| `partials/over-ons-en.html` | 127–130+ | English version | Mirror changes |

### 2.6 Warranty Wording Needs Legal Review
**Client feedback: warranty wording needs legal review.**

Current warranty tiers across product pages:
- Basic: 1 jaar garantie
- Professional: 2 jaar garantie
- Enterprise: 5 jaar garantie

**Action:** Flag all warranty claims for legal review. Do NOT change the actual terms, but:
1. Add "Zie onze algemene voorwaarden" / "See our terms and conditions" next to each warranty mention
2. Ensure warranty terms are consistent across shell pages and partials
3. Separate warranty claims from CE certification claims (currently bundled, e.g., "CE gecertificeerd met 2 jaar volledige garantie")

**Files with warranty mentions (30+ locations):**
- All 8 product shell pages (hero, specs table, and pricing tiers)
- All 16 product partials (NL + EN)

### 2.7 Privacy Policy: Update to Match Actual Tools
**Client feedback: policy doesn't match actual tools used.**

| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `privacybeleid.html` | 219 | "Geen externe trackingdiensten of fonts (self-hosted)" | Verify this is actually true — check if any analytics, tracking pixels, or external fonts are loaded |
| `privacybeleid.html` | 177 | "Toestemming (analytics)" — references analytics but also claims no external tracking | Reconcile: either analytics exists or it doesn't |
| `partials/privacybeleid-nl.html` | 65, 107 | Same contradiction | Fix |
| `partials/privacybeleid-en.html` | 65, 107 | Same in English | Fix |
| `privacybeleid.html` | 224 | Links to `/cookies` but cookie page is at `/cookiebeleid` | Fix URL |
| `partials/privacybeleid-nl.html` | 112, 168 | Same broken `/cookies` link | Fix to `/cookiebeleid` |

### 2.8 Fix "24 Hour Response" Claims
**Owner decision: 24/7 support IS real (AI-first) — keep, but clarify it's AI-first.**

47+ occurrences of "Reactie binnen 24 uur" / "Response within 24 hours" across the site.

**Action:** Keep the claim but add qualifier where space allows:
- Change "Reactie binnen 24 uur" → "Reactie binnen 24 uur (AI-ondersteund)"
- Change "Response within 24 hours" → "Response within 24 hours (AI-assisted)"
- On `over-ons.html:486` and `partials/over-ons-nl.html:362`: "Reactie binnen 24 uur gegarandeerd" — soften "gegarandeerd" or keep if truly guaranteed

### 2.9 Fix Phone Number Formatting Inconsistency

| File | Format Used |
|------|-------------|
| `partials/index-nl.html:354` | "+31 6 2399 8934" |
| `partials/zorg-revalidatie-nl.html:281` | "+31 6 2399 8934" |
| Other files | "+31 6 23 99 89 34" |

**Action:** Standardize to one format across all files. Recommended: `+31 6 23 99 89 34` (standard Dutch mobile formatting).

### 2.10 Social Media Links: Verify All Work
Social links appear in every page footer. All point to:
- `https://www.facebook.com/interactivemove`
- `https://www.instagram.com/interactivemove`
- LinkedIn (URL in footer)

**Action:** Manually verify each URL resolves to a real, active profile. If profiles don't exist yet, either create them or remove the links.

---

## PRIORITY 3: NICE-TO-HAVE (Polish)

### 3.1 Video Fallback Text
Some NL partials have English fallback text for `<video>` elements:

| File | Line | Current | Action |
|------|------|---------|--------|
| `partials/content-nl.html` | 6 | "Your browser does not support the video tag." | Change to "Uw browser ondersteunt geen video." |

EN partials correctly show English fallback. NL partials mostly correct ("Uw browser ondersteunt geen video.") except `content-nl.html`.

### 3.2 Blog Renderer: Minor Fixes
| File | Line | Issue | Action |
|------|------|-------|--------|
| `js/blog-renderer.js` | 27 | "Geinteresseerd" (missing diaeresis) | Change to "Geïnteresseerd" |
| `js/blog-renderer.js` | 174 | "Post not found" (hardcoded English) | Add bilingual support: check `isEn` flag |
| `js/blog-renderer.js` | 20, 24 | `blogTitle: isEn ? 'Blog' : 'Blog'` — redundant ternary | Simplify (cosmetic) |

### 3.3 Accessibility: Localize Aria Labels in JS
| File | Line | Issue | Action |
|------|------|-------|--------|
| `js/site.js` | 162 | `setAttribute('aria-label', 'Previous image')` — English only | Add language-aware aria-labels |
| `js/site.js` | 166 | `setAttribute('aria-label', 'Next image')` — English only | Add language-aware aria-labels |

### 3.4 Word Partner Page: Placeholder Content
| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `partials/word-partner-nl.html` | 90–91 | "Binnenkort delen onze partners hier hun ervaringen" / "Partnerverhalen volgen binnenkort" | Either remove the section entirely or keep as a subtle "coming soon" — it's honest at least |
| `partials/word-partner-nl.html` | 103 | "Wij nemen binnen 2 werkdagen contact met u op" | Verify this is achievable; Otto should confirm response SLA |

### 3.5 Parken & Speelhallen: ROI Calculator Disclaimer
| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `parken-speelhallen.html` | 287–346 | ROI calculator with no disclaimers | Add clear disclaimer text: "Deze berekening is indicatief en geeft geen garantie op daadwerkelijke resultaten" |
| `parken-speelhallen.html` | 494–526 | JS calculation logic | Review assumptions (price increase, repeat visitor %) with Otto for reasonableness |

### 3.6 Package Structure Clarity
**Client feedback: pricing package structure unclear.**

| File | Line(s) | Issue | Action |
|------|---------|-------|--------|
| `prijzen.html` | 191–294 | Package comparison table (Basic/Professional/Enterprise/Custom/Verhuur/Software) | Add clearer descriptions of what differentiates each tier; current descriptions are very brief |
| `partials/prijzen-nl.html` | 67–170 | Same table in partial | Mirror changes |
| `partials/prijzen-en.html` | 67–170 | English version | Mirror changes |

### 3.7 Contact Flow Clarity
**Client feedback: contact flow unclear.**

**Action:** Audit all CTA buttons and contact forms across the site. Ensure:
1. Every page has a clear path to contact (most already have "Reactie binnen 24 uur" CTA sections)
2. Contact form destination/behavior is clear to the user
3. Phone number, email, and form are consistently presented

### 3.8 Meta Description Brand Names
All `<meta name="description">` tags need brand name update from "InterActiveMove" to "Inter Active Move".

Affected: all 22 shell HTML files.

---

## EXECUTION ORDER (Recommended)

1. **Phase 1 — Content Removal** (1.1–1.4): Remove fake stats, testimonials, review counts, CE claims, fake citations. This is the most impactful change for credibility.

2. **Phase 2 — Content Correction** (1.5–1.7): Fix pricing to "op aanvraag", soften ROI claims, correct delivery time to ~1 week.

3. **Phase 3 — Brand Consistency** (2.1, 2.4, 3.8): Global find-and-replace "InterActiveMove" → "Inter Active Move" across all 66+ files (529 occurrences). Also fix page titles and meta descriptions.

4. **Phase 4 — Language Cleanup** (2.3): Fix all mixed Dutch/English content, translate footer copyright in EN files, fix Dutch text in English partials.

5. **Phase 5 — Game Count Alignment** (2.2): After confirming real count with Otto, update all pages consistently.

6. **Phase 6 — Legal & Policy** (2.6, 2.7): Warranty wording review, privacy policy update, broken cookie policy link.

7. **Phase 7 — Polish** (2.5, 2.8–2.10, 3.x): Mission/vision rewrite, 24h response qualifier, phone formatting, social media verification, JS fixes.

---

## FILES REQUIRING NO CHANGES
- `blog.html` — Otto says blog page can stay as-is
- `css/blog-styles.css` — no content issues
- `styles.css` — no content issues (pure CSS)

---

## NOTES FOR IMPLEMENTATION
- The site uses an HTMX partial-swap architecture: shell pages (`*.html`) load content from `partials/*-nl.html` and `partials/*-en.html`. **Both the shell page AND corresponding partials must be updated in sync** — the shell pages contain the default (NL) content inline, while the partials are swapped in by HTMX.
- Product pages follow the same pattern: `products/*.html` (shells) + `partials/products/*-nl.html` + `partials/products/*-en.html`.
- The `partials/content-nl.html` and `partials/content-en.html` files appear to be shared content blocks used across multiple pages.
- Use `git diff` after changes to verify no regressions in the bilingual toggle system.
