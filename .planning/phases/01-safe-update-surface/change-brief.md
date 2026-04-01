# Change Brief

**Source:** `website-adjustments.xlsx`
**Parsed:** 2026-04-01
**Sheets:** "Website Adjustments" (48 rows, 10 columns), "More info" (86 rows, 1 column)

## Actionable Tasks

### Structured Tasks (rows 0-7)

| Row | Page | Section | Task | Current Situation | New Situation | Status |
|-----|------|---------|------|-------------------|---------------|--------|
| 0 | Homepage | Products | Update image | 2-in-1 floor & wall with yellow square | Small real image of 2-in-1 housing | Open |
| 1 | Homepage | FAQ | Update question | How many games are available | How many interactive programs are available | Open |
| 2 | Homepage | FAQ | Update answer | Old text | New text (see Detailed Instructions below) | Open |
| 3 | Product page 2-in-1 | Text | Replace 'free updates' | & free updates | no license costs | Open |
| 5 | Product page 2-in-1 | Text | Adjust wording | New games via updates | New programs | Open |
| 6 | Product page 2-in-1 | Text | Remove text | Free updates included | Remove | Open |
| 7 | Product page 2-in-1 | Images | Fix/remove screws | Screws visible on backside | Retouch or replace images | Open |

### Semi-Structured Tasks (rows 38-47)

These rows use Page + Section columns but lack a Task column. The Section column contains the instruction.

| Row | Page | Instruction |
|-----|------|-------------|
| 38 | Producten Interactive floor | Delete "And new games are regularly added via free updates" and all game content text |
| 41 | Producten Interactive floor | Change Movie |
| 42 | Producten Interactive Wall | Remove "2 in 1" in picture |
| 43 | Producten Interactive Wall | Change "100+ games" to "60+ games" |
| 44 | Producten Interactive Wall | Remove "& free updates" |
| 45 | Producten Sandbox | Delete "Choose Your Package" section |
| 46 | Products Interactive Climbing Wall | Delete page |
| 47 | Software & Custom Development | Delete "Choose Your Package" section |

## IAM Mobiel Package Definitions

The following is the free-text block from Sheet 1, rows 9-34. This contains the approved umbrella brand definition and three package tiers. The original wording is preserved for downstream phases.

---

**Overkoepelende naam productlijn:**

### IAM mobiel

Dat is sterker dan overal 2-in-1 noemen, omdat niet elke variant een 2-in-1 is.

### Pakketten:

#### 1. IAM mobiel solo -- EUR 9.950

Een mobiele interactieve vloer of een mobiele interactieve wand.
Voor klanten die een duidelijke toepassing zoeken.
Inclusief software, geen abonnement, mobiel en eenvoudig verplaatsbaar.
Ook te gebruiken voor het tonen van visuele content en video's.
Later uit te breiden naar duo.

#### 2. IAM mobiel duo -- EUR 14.950

Een mobiel systeem dat zowel als interactieve vloer als interactieve wand inzetbaar is.
Daarnaast ook te gebruiken voor video's, presentaties en andere projecties.
In veel situaties is een aparte beamer dan niet meer nodig.
Inclusief software, geen abonnement.
Dit zou ik positioneren als de standaard en meest gekozen optie.

#### 3. IAM mobiel premium -- vanaf EUR 16.950

De duo-uitvoering, maar dan in een gepersonaliseerde versie voor de klant.
Denk aan logo op de behuizing, keuze uit geselecteerde kleuren of afwerking, gepersonaliseerd startscherm en een professionelere uitstraling passend bij de organisatie.
Voor klanten die naast functionaliteit ook branding en uitstraling belangrijk vinden.

---

**Positioning note (from row 34):** "IAM mobiel -- Dat is sterker dan overal 2-in-1 noemen, omdat niet elke variant een 2-in-1 is."

## Detailed Instructions (More Info)

Content from Sheet 2 provides expanded instructions for the tasks listed above.

### Homepage -- Products Section

The current image in the Products section shows the 2-in-1 floor and wall with a yellow square.

**Action:** Please change this to a small real image of the 2-in-1 housing.

### Homepage -- Frequently Asked Questions

Please replace the current question and answer with the following:

**Question:** How many interactive programs are available?

**Answer:** The number of available programs depends on the product and the selected package. Our interactive wall and floor offer a wide range of programs, while the interactive sandbox has its own selection. Please contact us for an overview that fits your situation.

### 2-in-1 Product Page -- Text Changes

- Change "& free updates" to "no license costs"
- Change "Regularly new games through updates" to "Regularly new programs"
- Keep "Extensive Game Library", but remove "Free updates included"

### 2-in-1 Product Page -- Image Changes

On the back side of the 2-in-1, screws are visible.

**Action:** Please remove the screws in the photo, or remove/replace those photos.

### 2-in-1 Packages -- Specification Details

Important: the housing is always a 2-in-1 housing, but it can be used as: mobile floor only, mobile wall only, and both mobile floor and mobile wall.

#### Package: 2-in-1 mobile floor + sensor system

- 2-in-1 housing configured for use as an interactive mobile floor
- 60+ programs
- 2-year warranty
- Expandable later to an interactive mobile wall
- Training for your team
- Different support options available

#### Package: 2-in-1 mobile wall + sensor system

- 2-in-1 housing configured for use as an interactive mobile wall
- 60+ programs
- 2-year warranty
- Expandable later to an interactive mobile floor
- Training for your team
- Different support options available

#### Package: 2-in-1 mobile floor + wall + sensor system

- 2-in-1 housing suitable for both an interactive mobile floor and an interactive mobile wall
- 120+ programs
- 2-year warranty
- Training for your team
- Different support options available

### Interactive Floor

Delete "And new games are regularly added via free updates" and the rest under this.

## Cross-Reference to File Families

Mapping spreadsheet page names to file families from `inventory.md`:

| Spreadsheet Page Name | File Family | Shell Path |
|-----------------------|-------------|------------|
| Homepage | `index` | `index.html` |
| Product page 2-in-1 | `2-in-1-vloer-muur` | `products/2-in-1-vloer-muur.html` |
| Producten Interactive floor | `interactieve-vloer` | `products/interactieve-vloer.html` |
| Producten Interactive Wall | `interactieve-muur` | `products/interactieve-muur.html` |
| Producten Sandbox | `interactieve-zandbak` | `products/interactieve-zandbak.html` |
| Products Interactive Climbing Wall | `interactieve-klimwand` | `products/interactieve-klimwand.html` |
| Software & Custom Development | `software-maatwerk` | `products/software-maatwerk.html` |

## Open Questions

### 1. Climbing wall page deletion scope

Row 46 says "Delete page" for "Products Interactive Climbing Wall". This conflicts with D-08, which only lists `bouw-een-park` and `3d-spellen` as removal investigation targets. The climbing wall deletion is an additional removal candidate from the spreadsheet that was not in the original D-08 scope.

**Recommendation:** Flag for Phase 5 confirmation alongside the other removal candidates. The climbing wall page has the same nav dependency footprint (referenced in all HTML files via nav/footer).

### 2. "2-in-1" term vs current product naming

The spreadsheet extensively references "2-in-1" as a product name and the current codebase has a product page at `products/2-in-1-vloer-muur.html`. The IAM mobiel package definitions (rows 9-34) suggest repositioning away from the "2-in-1" name toward "IAM mobiel" as the umbrella brand. However, the physical housing is still called "2-in-1 housing" in the detailed instructions.

**Recommendation:** The term "2-in-1" should be preserved for the physical hardware description but the product line branding should shift to "IAM mobiel" per the package definitions.

### 3. Movie change for Interactive Floor (row 41)

Row 41 says "Change Movie" for the Interactive Floor page but provides no details about what the new movie should be or where to source it.

**Recommendation:** Flag as blocked pending asset/specification from stakeholder.

### 4. Image asset availability

Row 0 (Homepage products image) and row 7 (2-in-1 screws) require image changes. The change brief specifies what should change but the replacement image assets may not yet be available in the media directory.

**Recommendation:** Verify asset availability before executing image-related tasks in downstream phases.

### 5. Semi-structured task rows lack granularity

Rows 38-47 use a different format than rows 0-7 (Section contains the instruction, Task is NaN). These need to be interpreted as actionable tasks despite the format difference.

**Recommendation:** Treat the Section column as the task description for rows 38-47.
